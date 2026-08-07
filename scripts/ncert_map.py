#!/usr/bin/env python3
"""Unit descriptions from NCERT chapter text, with chapters assigned to units by
embedding the CHAPTER TEXT (not its title - title extraction off these PDFs is
unreliable, returning body prose like 'Y ou have learnt about...').

Then re-run the gold-set validation: does a chapter-text description beat the
single curriculum paragraph?
"""
import re, json, sys, pathlib, collections, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topics2 import is_english, CACHE
from ncert_units import chapter_text, SUBJ_BOOKS
from embed_units import describe as describe_curriculum, units, DROP

HERE = pathlib.Path(__file__).parent
units["Accountancy"] = [("Accounting for Partnership Firms",36),("Accounting for Companies",24),
                        ("Analysis of Financial Statements",12),("Cash Flow Statement",8)]

GOLD = json.loads((HERE/"gold.json").read_text()) if (HERE/"gold.json").exists() else None

def build(subject, names, model, util):
    books = SUBJ_BOOKS.get(subject, [])
    chaps = [(b["code"], i) for b in sorted(books, key=lambda x: x["code"])
             for i in range(1, b["chapters"]+1)]
    texts = {k: chapter_text(*k, 14000) for k in chaps}
    chaps = [k for k in chaps if len(texts[k]) > 1500]
    if not chaps: return {}
    C = model.encode([texts[k][:4000] for k in chaps], convert_to_tensor=True,
                     normalize_embeddings=True, batch_size=16)
    core = [re.sub(r'^[IVX]+\s+|^Unit[\s\-–]*[IVX0-9]+[.:]?\s*','',n).strip() for n in names]
    U = model.encode(core, convert_to_tensor=True, normalize_embeddings=True)
    sim = util.cos_sim(C, U)                      # chapter x unit
    best = sim.argmax(dim=1).tolist()
    assign = collections.defaultdict(list)
    for k, b in zip(chaps, best): assign[names[b]].append(k)
    out = {}
    for n, c in zip(names, core):
        ks = assign.get(n, [])
        body = " ".join(texts[k][:9000] for k in ks[:3])
        out[n] = (f"{c}. {body}")[:14000] if body else c
    return out, {n: [f"{a}{b:02d}" for a,b in assign.get(n,[])] for n in names}

def main():
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer("all-MiniLM-L6-v2", device="mps")
    gold = json.loads((HERE/"gold_patterns.json").read_text())
    rows = [r for r in json.loads(CACHE.read_text())
            if r.get("question") and is_english(r["question"]) and r.get("marks")]
    by = collections.defaultdict(list)
    for r in rows: by[r["subject"]].append(r)

    print(f"{'subject':12s} {'gold':>5s} {'curric-para':>12s} {'NCERT-chapter':>14s}   chapters per unit")
    final = {}
    for subj, g in gold.items():
        names = [n for n,_ in units[subj] if not DROP.search(n)]
        lab = []
        for q in by[subj]:
            t = q["question"].lower()
            hit = [u for u, ps in g.items() if any(re.search(p, t) for p in ps)]
            if len(hit) == 1 and hit[0] in names: lab.append((q, hit[0]))
        if len(lab) < 40: continue
        Q = model.encode([q["question"][:400] for q,_ in lab], convert_to_tensor=True,
                         normalize_embeddings=True, batch_size=128)
        # A: curriculum paragraph
        dA = describe_curriculum(subj, names)
        UA = model.encode([dA[n] for n in names], convert_to_tensor=True, normalize_embeddings=True)
        accA = sum(names[b]==gg for (q,gg),b in zip(lab, util.cos_sim(Q,UA).argmax(dim=1).tolist()))
        # B: NCERT chapter text
        dB, assign = build(subj, names, model, util)
        UB = model.encode([dB[n] for n in names], convert_to_tensor=True, normalize_embeddings=True)
        accB = sum(names[b]==gg for (q,gg),b in zip(lab, util.cos_sim(Q,UB).argmax(dim=1).tolist()))
        n = len(lab)
        print(f"{subj:12s} {n:5d} {accA/n:11.1%} {accB/n:13.1%}")
        for u in names: print(f"{'':32s} {u[:38]:40s} {','.join(assign.get(u,[])) or '-'}")
        final[subj] = dict(gold=n, curriculum_acc=round(accA/n,3), ncert_acc=round(accB/n,3),
                           chapters={u: assign.get(u,[]) for u in names})
        json.dump(dB, open(HERE/f"ncert_desc_{subj}.json","w"))
    json.dump(final, open(HERE/"ncert_validation.json","w"), indent=1)

if __name__ == "__main__":
    main()
