import json, os, pathlib, subprocess, hashlib, sys
from concurrent.futures import ThreadPoolExecutor
HOME=pathlib.Path.home()
MD=HOME/"Downloads/cbse_md"
OCR=pathlib.Path(os.environ.get("OCRPDF","./ocrpdf"))  # built from ocr.swift
files=[pathlib.Path(l) for l in (MD/"KEPT_IMAGE_ONLY_PDFS.txt").read_text().splitlines() if l.strip()]
files=[f for f in files if f.exists()]
roots={HOME/"Downloads/cbse_official":"official"}
def md_path(p):
    for root,tree in roots.items():
        try: return MD/tree/p.relative_to(root).with_suffix(".md")
        except ValueError: pass
    return MD/"ocr_misc"/(p.stem+".md")
def one(p):
    tmp=f"/tmp/ocr_{os.getpid()}_{abs(hash(str(p)))%99999}.txt"
    try:
        subprocess.run([str(OCR),str(p),tmp,"200"],check=True,capture_output=True,timeout=900)
        txt=pathlib.Path(tmp).read_text()
    except Exception as e:
        return dict(pdf=str(p), ok=False, err=str(e)[:120], chars=0)
    finally:
        pathlib.Path(tmp).unlink(missing_ok=True)
    pages=txt.split("\f")
    data=p.read_bytes()
    fm=dict(title=p.stem.replace("_"," "), source_pdf=p.name, source_url="",
            pages=len(pages), pdf_bytes=len(data), pdf_sha256=hashlib.sha256(data).hexdigest(),
            text_chars=len(txt), low_text_pages=sum(1 for x in pages if len(x.strip())<40),
            converter="macOS Vision OCR (accurate, en-US) @200dpi via ocr.swift",
            ocr=True, ocr_note="Devanagari NOT recognised - Vision has no Hindi model; the Hindi column of bilingual papers is noise")
    body="".join(f"\n\n---\n\n## page {i}\n\n```\n{x.rstrip()}\n```" for i,x in enumerate(pages,1))
    m=md_path(p); m.parent.mkdir(parents=True,exist_ok=True)
    m.write_text("---\n"+"\n".join(f"{k}: {json.dumps(v)}" for k,v in fm.items())+"\n---\n"+f"\n# {fm['title']}\n"+body)
    return dict(pdf=str(p), md=str(m), ok=True, chars=len(txt), pages=len(pages),
                pdf_bytes=len(data), md_bytes=m.stat().st_size,
                chars_per_page=round(len(txt)/max(len(pages),1)))
print(f"OCR-ing {len(files)} scanned PDFs", flush=True)
res=[]
with ThreadPoolExecutor(max_workers=4) as ex:
    for i,r in enumerate(ex.map(one, files),1):
        res.append(r)
        if i%25==0: print(f"  {i}/{len(files)}", flush=True)
json.dump(res, open(MD/"OCR_MANIFEST.json","w"), indent=1)
ok=[r for r in res if r["ok"]]
print(f"\nOCR complete: {len(ok)}/{len(files)}")
print(f"  total chars recovered: {sum(r['chars'] for r in ok):,}")
good=[r for r in ok if r['chars_per_page']>=120]
print(f"  files now with usable text (>=120 chars/page): {len(good)}")
print(f"  still thin (mostly Devanagari or true images): {len(ok)-len(good)}")
