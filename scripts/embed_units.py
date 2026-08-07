#!/usr/bin/env python3
"""Assign exam questions to CBSE curriculum units by sentence embedding, not keywords.

Keyword overlap worked for Accountancy (87% mapped) and collapsed for Biology (15%),
because Biology's unit names are generic words that appear everywhere. Two changes:

 1. Each unit is described by its NAME **plus the syllabus text underneath it** in the
    curriculum document, so "Reproduction" carries pollen/embryo/gamete/placenta with it.
 2. Assignment is cosine similarity in embedding space with an explicit floor - a
    question below the floor is reported unassigned rather than forced into its
    nearest-but-meaningless unit.

Model: all-MiniLM-L6-v2 (local, no API).
"""
import re, json, sys, pathlib, collections, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topics2 import is_english, CACHE

HERE = pathlib.Path(__file__).parent
CUR  = pathlib.Path.home()/"Downloads/cbse_official/curriculum"
FLOOR = 0.28          # below this a question is left unassigned

units = json.loads((HERE/"units_xii.json").read_text())
units["Accountancy"] = [("Accounting for Partnership Firms",36),("Accounting for Companies",24),
                        ("Analysis of Financial Statements",12),("Cash Flow Statement",8)]
DROP = re.compile(r'write up|viva|spotting|practical|project|reading comprehension|writing skill', re.I)

def curriculum_text(subject):
    for p in CUR.glob("*.pdf"):
        if re.search(r'Hi_|Hindi|_hi', p.name): continue
        stem = re.split(r'_SrSec', p.name)[0].replace('_',' ').lower()
        if stem == subject.lower():
            return subprocess.run(["pdftotext","-layout",str(p),"-"],
                                  capture_output=True, text=True, timeout=120).stdout
    return ""

def describe(subject, unit_names):
    """unit name + the syllabus prose that follows it in the curriculum document"""
    txt = curriculum_text(subject)
    out = {}
    for n in unit_names:
        core = re.sub(r'^[IVX]+\s+|^Unit[\s\-–]*[IVX0-9]+[.:]?\s*', '', n).strip()
        desc, best = "", -1.0
        if txt and core:
            for m in re.finditer(re.escape(core), txt, re.I):
                chunk = re.sub(r'\s+', ' ', txt[m.end(): m.end()+1400])
                if len(chunk) < 80: continue
                # Prefer syllabus PROSE over the course-structure table. Table regions are
                # dense in digits and in other units' names; prose is mostly letters.
                letters = sum(c.isalpha() for c in chunk)
                digits  = sum(c.isdigit() for c in chunk)
                others  = sum(1 for o in unit_names if o is not n and
                              re.sub(r'^[IVX]+\s+|^Unit[\s\-–]*[IVX0-9]+[.:]?\s*','',o).strip().lower()[:18] in chunk.lower())
                score = letters/max(len(chunk),1) - 3.0*digits/max(len(chunk),1) - 0.15*others
                if score > best: best, desc = score, chunk
        out[n] = f"{core}. {desc[:900]}" if desc else core
    return out

def main():
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer("all-MiniLM-L6-v2", device="mps")
    rows = [r for r in json.loads(CACHE.read_text())
            if r.get("question") and is_english(r["question"]) and r.get("marks")]
    by = collections.defaultdict(list)
    for r in rows: by[r["subject"]].append(r)

    report = {}
    for subj, us in units.items():
        us = [(n,m) for n,m in us if not DROP.search(n)]
        qs = by.get(subj) or []
        if len(us) < 3 or len(qs) < 80: continue
        descs = describe(subj, [n for n,_ in us])
        names = [n for n,_ in us]
        U = model.encode([descs[n] for n in names], convert_to_tensor=True, normalize_embeddings=True)
        texts = [q["question"][:400] for q in qs]
        Q = model.encode(texts, convert_to_tensor=True, normalize_embeddings=True,
                         batch_size=128, show_progress_bar=False)
        sim = util.cos_sim(Q, U)
        best = sim.argmax(dim=1).tolist()
        top  = sim.max(dim=1).values.tolist()
        got, un = collections.Counter(), 0
        for q, b, s in zip(qs, best, top):
            if s < FLOOR: un += 1; continue
            got[names[b]] += q["marks"]
        td, ta = sum(m for _,m in us), sum(got.values())
        if not ta: continue
        recs = []
        for n, d in sorted(us, key=lambda x: -x[1]):
            dp, ap = 100*d/td, 100*got[n]/ta
            recs.append(dict(unit=n, declared_pct=round(dp,1), actual_pct=round(ap,1), gap=round(ap-dp,1)))
        report[subj] = dict(mapped=round(1-un/len(qs),3), questions=len(qs), units=recs)
        print(f"\n### {subj}   {len(qs)-un}/{len(qs)} mapped ({1-un/len(qs):.0%})")
        print(f"  {'unit':44s} {'declared':>9s} {'actual':>7s} {'gap':>6s}")
        for r in recs:
            flag = "  <<" if abs(r['gap']) >= 8 else ""
            print(f"  {r['unit'][:44]:44s} {r['declared_pct']:8.0f}% {r['actual_pct']:6.0f}% {r['gap']:+6.0f}{flag}")
    (HERE/"syllabus_vs_actual_embed.json").write_text(json.dumps(report, indent=1))

if __name__ == "__main__":
    main()
