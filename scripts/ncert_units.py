#!/usr/bin/env python3
"""Build unit descriptions from NCERT chapter text instead of a curriculum paragraph.

The curriculum names the chapters that sit under each unit ("Chapter-4: Principles of
Inheritance and Variation"), so chapters can be attached to units on the board's own
authority. Where it doesn't, fall back to title similarity against the unit name.
"""
import re, json, subprocess, pathlib, collections

NC   = pathlib.Path.home()/"Downloads/ncert_xii/pdf"
CUR  = pathlib.Path.home()/"Downloads/cbse_official/curriculum"
HERE = pathlib.Path(__file__).parent
BOOKS = {b["code"]: b for b in json.loads((HERE/"ncert_books12.json").read_text())}
SUBJ_BOOKS = collections.defaultdict(list)
for b in BOOKS.values():
    if b["code"].startswith("le"): SUBJ_BOOKS[b["subject"]].append(b)

def chapter_text(code, n, maxchars=20000):
    p = NC/f"{code}{n:02d}.pdf"
    if not p.exists(): return ""
    t = subprocess.run(["pdftotext","-layout",str(p),"-"],
                       capture_output=True, text=True, timeout=180).stdout
    return re.sub(r'\s+', ' ', t)[:maxchars]

def chapter_title(code, n):
    p = NC/f"{code}{n:02d}.pdf"
    if not p.exists(): return ""
    t = subprocess.run(["pdftotext","-layout","-f","1","-l","1",str(p),"-"],
                       capture_output=True, text=True, timeout=60).stdout
    for line in t.splitlines():
        s = line.strip()
        if 6 < len(s) < 70 and not re.search(r'\d{3}|chapter|reprint|©', s, re.I) and s[:1].isalpha():
            return s
    return ""

def curriculum_text(subject):
    for p in CUR.glob("*.pdf"):
        if re.search(r'Hi_|Hindi|_hi', p.name): continue
        if re.split(r'_SrSec', p.name)[0].replace('_',' ').lower() == subject.lower():
            return subprocess.run(["pdftotext","-layout",str(p),"-"],
                                  capture_output=True, text=True, timeout=120).stdout
    return ""

def unit_chapters(subject, unit_names):
    """unit -> [chapter numbers], read from the curriculum's own Chapter-N references"""
    txt = curriculum_text(subject)
    pos = {}
    for n in unit_names:
        core = re.sub(r'^[IVX]+\s+|^Unit[\s\-–]*[IVX0-9]+[.:]?\s*', '', n).strip()
        best, bs = None, -1
        for m in re.finditer(re.escape(core), txt, re.I):
            chunk = txt[m.end():m.end()+2500]
            s = len(re.findall(r'Chapter[\s\-–]*\d+', chunk, re.I))
            if s > bs: bs, best = s, m.end()
        pos[n] = best
    out = {}
    for n, p in pos.items():
        if p is None: out[n] = []; continue
        chunk = txt[p:p+2500]
        nums = [int(x) for x in re.findall(r'Chapter[\s\-–]*(\d{1,2})', chunk, re.I)]
        # stop at the next unit's heading if it appears
        out[n] = sorted(set(nums))[:8]
    return out

def describe_from_ncert(subject, unit_names):
    books = SUBJ_BOOKS.get(subject, [])
    if not books: return {}
    uc = unit_chapters(subject, unit_names)
    # chapter numbering restarts per book part; build a flat list across parts in order
    flat = []
    for b in sorted(books, key=lambda x: x["code"]):
        for i in range(1, b["chapters"]+1): flat.append((b["code"], i))
    titles = {(c,i): chapter_title(c,i) for c,i in flat}
    out = {}
    for n in unit_names:
        chs = uc.get(n) or []
        picked = []
        for num in chs:
            for c,i in flat:
                if i == num: picked.append((c,i))
        if not picked:   # fall back: title closest to the unit name
            core = set(re.findall(r'[a-z]{4,}', n.lower()))
            scored = sorted(flat, key=lambda k: -len(core & set(re.findall(r'[a-z]{4,}', titles[k].lower()))))
            if scored and core & set(re.findall(r'[a-z]{4,}', titles[scored[0]].lower())):
                picked = [scored[0]]
        txt = " ".join(chapter_text(c,i, 12000) for c,i in picked[:4])
        core = re.sub(r'^[IVX]+\s+|^Unit[\s\-–]*[IVX0-9]+[.:]?\s*','',n).strip()
        out[n] = (f"{core}. " + txt)[:12000] if txt else core
    return out

if __name__ == "__main__":
    units = json.loads((HERE/"units_xii.json").read_text())
    units["Accountancy"] = [("Accounting for Partnership Firms",36),("Accounting for Companies",24),
                            ("Analysis of Financial Statements",12),("Cash Flow Statement",8)]
    DROP = re.compile(r'write up|viva|spotting|practical|project', re.I)
    res = {}
    for subj in ["Biology","Accountancy","Economics"]:
        names = [n for n,_ in units[subj] if not DROP.search(n)]
        d = describe_from_ncert(subj, names)
        res[subj] = d
        print(f"\n{subj}:")
        for n in names:
            print(f"   {len(d.get(n,'')):6d} chars  {n[:44]:46s} {'NCERT text' if len(d.get(n,''))>500 else 'name only'}")
    json.dump(res, open(HERE/"ncert_unit_desc.json","w"))
