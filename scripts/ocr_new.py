import json, os, pathlib, subprocess, hashlib
from concurrent.futures import ThreadPoolExecutor
HOME=pathlib.Path.home(); MD=HOME/"Downloads/cbse_md"
OCR=pathlib.Path("/private/tmp/claude-501/-Users-umashankar/30fcafbc-5849-4772-b0b4-4b4693b70cf8/scratchpad/ocr/ocrpdf")
SRC={"sqp_archive":HOME/"Downloads/cbse_official/sqp_archive","past_papers_X":HOME/"Downloads/cbse_official/past_papers_X"}
items=[]
for tree,rel in json.load(open("/tmp/risky_new.json")):
    pdf=SRC[tree]/pathlib.Path(rel).with_suffix(".pdf")
    if pdf.exists(): items.append((tree,rel,pdf))
def one(t):
    tree,rel,pdf=t
    tmp=f"/tmp/o_{os.getpid()}_{abs(hash(str(pdf)))%99999}.txt"
    try:
        subprocess.run([str(OCR),str(pdf),tmp,"200"],check=True,capture_output=True,timeout=900)
        txt=pathlib.Path(tmp).read_text()
    except Exception as e: return dict(ok=False,pdf=str(pdf),err=str(e)[:100])
    finally: pathlib.Path(tmp).unlink(missing_ok=True)
    pages=txt.split("\f"); data=pdf.read_bytes()
    fm=dict(title=pdf.stem.replace("_"," "),source_pdf=pdf.name,source_url="",pages=len(pages),
            pdf_bytes=len(data),pdf_sha256=hashlib.sha256(data).hexdigest(),text_chars=len(txt),
            low_text_pages=sum(1 for x in pages if len(x.strip())<40),
            converter="macOS Vision OCR (accurate, en-US) @200dpi",ocr=True,
            ocr_note="Devanagari NOT recognised - Vision has no Hindi model")
    body="".join(f"\n\n---\n\n## page {i}\n\n```\n{x.rstrip()}\n```" for i,x in enumerate(pages,1))
    m=MD/tree/rel; m.parent.mkdir(parents=True,exist_ok=True)
    m.write_text("---\n"+"\n".join(f"{k}: {json.dumps(v)}" for k,v in fm.items())+"\n---\n"+f"\n# {fm['title']}\n"+body)
    return dict(ok=True,pdf=str(pdf),chars=len(txt),pages=len(pages),cpp=round(len(txt)/max(len(pages),1)))
print(f"OCR-ing {len(items)} image-only PDFs",flush=True)
res=[]
with ThreadPoolExecutor(max_workers=4) as ex:
    for i,r in enumerate(ex.map(one,items),1):
        res.append(r)
        if i%50==0: print(f"  {i}/{len(items)}",flush=True)
json.dump(res,open(MD/"OCR_MANIFEST_new.json","w"),indent=1)
ok=[r for r in res if r["ok"]]
print(f"\ndone {len(ok)}/{len(items)}  chars={sum(r['chars'] for r in ok):,}  usable={sum(1 for r in ok if r['cpp']>=120)}")
