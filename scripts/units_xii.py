#!/usr/bin/env python3
"""Extract CLASS XII unit/theme weightage from the CBSE curriculum PDFs.

Curricula cover Classes XI and XII in one document, so an un-split extraction mixes
Class XI units into the Class XII denominator - which silently distorts every
declared-vs-actual share. Track the Class XI / Class XII headings and keep only XII.
Units carry no common prefix ("Unit", "Theme") across subjects, so match on the
layout instead: an indented title followed by a wide gap and a mark count.
"""
import re, json, subprocess, pathlib, collections

CUR = pathlib.Path.home()/"Downloads/cbse_official/curriculum"
ROW = re.compile(r'^\s{2,}([A-Z][^\d]{5,58}?)\s{2,}(\d{1,3})\s*$')
CLS = re.compile(r'\bClass\s*[-–]?\s*(XI{1,2})\b', re.I)
SKIP = re.compile(r'total|project work|practical|internal assessment|grand|periods|^part\s*[a-c]\s*$', re.I)

def units_for(pdf):
    txt = subprocess.run(["pdftotext","-layout",str(pdf),"-"],
                         capture_output=True, text=True, timeout=120).stdout
    cur, out = None, []
    for line in txt.splitlines():
        c = CLS.search(line)
        if c: cur = c.group(1).upper()
        m = ROW.match(line)
        if m and cur == "XII":
            name, mk = re.sub(r'\s+',' ',m.group(1)).strip(), int(m.group(2))
            if SKIP.search(name) or not (1 <= mk <= 40): continue
            if len(name) < 6: continue
            out.append((name, mk))
    # dedupe, keep first occurrence
    seen, res = set(), []
    for n, m in out:
        k = n.lower()
        if k in seen: continue
        seen.add(k); res.append((n, m))
    return res

res = {}
for pdf in sorted(CUR.glob("*.pdf")):
    if re.search(r'Hi_|Hindi|_hi', pdf.name): continue
    u = units_for(pdf)
    tot = sum(m for _, m in u)
    if len(u) >= 3 and 60 <= tot <= 110:      # a plausible 80-mark theory paper
        subj = re.split(r'_SrSec', pdf.name)[0].replace('_',' ')
        res[subj] = u
json.dump(res, open(pathlib.Path(__file__).parent/"units_xii.json","w"), indent=1)
print(f"subjects with a clean Class-XII unit table: {len(res)}\n")
for s, u in sorted(res.items()):
    print(f"  {s:28s} {sum(m for _,m in u):3d} marks over {len(u)} units")
    for n, m in u[:6]: print(f"       {m:3d}  {n[:56]}")
