#!/usr/bin/env python3
"""PDF -> Markdown for the CBSE corpus.

Keeps BOTH language columns (text is tiny next to the PDFs, so there is no reason
to throw the Hindi away) and records provenance in front-matter: source URL where
known, page count, byte size and SHA-256 of the original PDF. If the PDFs are
deleted afterwards, the hash still identifies exactly which file each .md came from.

Records `figures: N` — pages whose text is nearly empty are almost certainly
diagram/map/cartoon pages, and that content does NOT survive this conversion.
"""
import subprocess, pathlib, hashlib, sys, re, json

def convert(pdf: pathlib.Path, md: pathlib.Path, source_url: str = "") -> dict:
    data = pdf.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                         capture_output=True, text=True, timeout=300).stdout
    pages = txt.split("\f")
    if pages and not pages[-1].strip(): pages.pop()
    sparse = sum(1 for p in pages if len(re.sub(r'\s', '', p)) < 40)
    body = []
    for i, p in enumerate(pages, 1):
        body.append(f"\n\n---\n\n## page {i}\n\n```\n{p.rstrip()}\n```")
    fm = {
        "title": pdf.stem.replace("_", " "),
        "source_pdf": pdf.name,
        "source_url": source_url,
        "pages": len(pages),
        "pdf_bytes": len(data),
        "pdf_sha256": sha,
        "text_chars": len(txt),
        "low_text_pages": sparse,
        "converter": "pdftotext -layout",
    }
    head = "---\n" + "\n".join(f"{k}: {json.dumps(v)}" for k, v in fm.items()) + "\n---\n"
    md.parent.mkdir(parents=True, exist_ok=True)
    md.write_text(head + f"\n# {fm['title']}\n" + "".join(body))
    fm["md_bytes"] = md.stat().st_size
    return fm

if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1]).expanduser()
    out_root = pathlib.Path(sys.argv[2]).expanduser()
    urlmap = {}
    if len(sys.argv) > 3 and pathlib.Path(sys.argv[3]).exists():
        for line in pathlib.Path(sys.argv[3]).read_text().splitlines():
            urlmap[line.rstrip('/').split('/')[-1].replace(' ', '_')] = line
    pdfs = sorted(root.rglob("*.pdf"))
    manifest, pdf_b, md_b, fails = [], 0, 0, []
    for p in pdfs:
        rel = p.relative_to(root).with_suffix(".md")
        try:
            fm = convert(p, out_root / rel, urlmap.get(p.name, ""))
        except Exception as e:
            fails.append(f"{p}: {e}"); continue
        fm["md_path"] = str(rel)
        manifest.append(fm); pdf_b += fm["pdf_bytes"]; md_b += fm["md_bytes"]
    (out_root / "MANIFEST.json").write_text(json.dumps(manifest, indent=1))
    print(f"converted {len(manifest)}/{len(pdfs)} PDFs")
    print(f"  PDF  {pdf_b/1048576:9.1f} MB")
    print(f"  MD   {md_b/1048576:9.1f} MB   ({md_b/pdf_b:.1%} of original)")
    print(f"  pages with almost no text (figures lost): "
          f"{sum(m['low_text_pages'] for m in manifest)}")
    if fails:
        print(f"  FAILED {len(fails)}:"); [print("   ", f) for f in fails[:10]]
