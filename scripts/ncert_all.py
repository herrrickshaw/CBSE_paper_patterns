#!/usr/bin/env python3
"""NCERT chapter text -> unit descriptions, for every subject with a Class-XII unit table.

Chapter text now comes from the converted MARKDOWN (the PDFs were deleted). Chapters
attach to units EXCLUSIVELY - highest similarity first, each chapter used once, and any
unit left empty takes its best unclaimed chapter. Sharing chapters between units gives
adjacent units near-identical descriptions and manufactures spurious gaps.
"""
import re, json, sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topics2 import is_english, CACHE
from embed_units import units, DROP

HERE = pathlib.Path(__file__).parent
MD   = pathlib.Path.home()/"Downloads/cbse_md/ncert_xii"
units["Accountancy"] = [("Accounting for Partnership Firms",36),("Accounting for Companies",24),
                        ("Analysis of Financial Statements",12),("Cash Flow Statement",8)]
BOOKS = {                       # subject -> NCERT book codes used at Class XII
 "Biology":      ["lebo1"],
 "Accountancy":  ["leac1","leac2","leca1"],
 "Economics":    ["leec1","keec1"],          # Macroeconomics + Indian Economic Development
 "Psychology":   ["lepy1"],
}
def chapters(codes):
    out=[]
    for c in codes:
        for p in sorted(MD.glob(f"{c}*.md")):
            t = re.sub(r'^---.*?^---', '', p.read_text(errors="ignore"), flags=re.S|re.M)
            t = re.sub(r'```|## page \d+|#\s*\w+\d+|\s+', ' ', t).strip()
            if len(t) > 1500: out.append((p.stem, t))
    return out

def gist(t, n=4000):
    """Representative span of a chapter, NOT its opening.

    NCERT chapters open with a scientist biography and figure captions - embedding the
    first 4k chars therefore compares author bios, not subject matter, and cost Biology
    26 points of assignment accuracy. Sample evenly across the body instead.
    """
    body = t[len(t)//10:]                      # drop the opening sidebar
    if len(body) <= n: return body
    k = n // 4
    step = len(body) // 4
    return " ".join(body[i*step : i*step + k] for i in range(4))

def main():
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer("all-MiniLM-L6-v2", device="mps")
    gold = json.loads((HERE/"gold_patterns.json").read_text())
    rows = [r for r in json.loads(CACHE.read_text())
            if r.get("question") and is_english(r["question"]) and r.get("marks")]
    by = collections.defaultdict(list)
    for r in rows: by[r["subject"]].append(r)
    final = {}
    for subj, codes in BOOKS.items():
        names = [n for n,_ in units[subj] if not DROP.search(n)]
        decl  = dict((n,m) for n,m in units[subj] if not DROP.search(n))
        chs = chapters(codes)
        if not chs: print(f"{subj}: no chapter text"); continue
        C = model.encode([t[:4000] for _,t in chs], convert_to_tensor=True,
                         normalize_embeddings=True, batch_size=16)
        core = [re.sub(r'^[IVX]+\s+|^Unit[\s\-–]*[IVX0-9]+[.:]?\s*','',n).strip() for n in names]
        S = util.cos_sim(C, model.encode(core, convert_to_tensor=True, normalize_embeddings=True))
        pairs = sorted(((float(S[i][j]), i, j) for i in range(len(chs)) for j in range(len(names))), reverse=True)
        taken, assign = set(), collections.defaultdict(list)
        for s,i,j in pairs:
            if i in taken or len(assign[names[j]]) >= 3: continue
            taken.add(i); assign[names[j]].append(i)
        for j,n in enumerate(names):
            if assign[n]: continue
            for s,i,jj in pairs:
                if jj==j and i not in taken: taken.add(i); assign[n].append(i); break
        desc = {n: (f"{core[j]}. " + " ".join(chs[i][1][:9000] for i in assign[n]))[:14000]
                for j,n in enumerate(names)}
        qs = by.get(subj) or []
        U = model.encode([desc[n] for n in names], convert_to_tensor=True, normalize_embeddings=True)
        # accuracy on the gold set, where one exists
        acc = None
        if subj in gold:
            lab=[(q,h[0]) for q in qs for h in [[u for u,ps in gold[subj].items()
                  if any(re.search(p,q["question"].lower()) for p in ps)]] if len(h)==1 and h[0] in names]
            if len(lab) >= 40:
                QL = model.encode([q["question"][:400] for q,_ in lab], convert_to_tensor=True,
                                  normalize_embeddings=True, batch_size=128)
                acc = sum(names[b]==g for (q,g),b in zip(lab, util.cos_sim(QL,U).argmax(dim=1).tolist()))/len(lab)
        Q = model.encode([q["question"][:400] for q in qs], convert_to_tensor=True,
                         normalize_embeddings=True, batch_size=128)
        sim = util.cos_sim(Q,U); best=sim.argmax(dim=1).tolist(); top=sim.max(dim=1).values.tolist()
        got, un = collections.Counter(), 0
        for q,b,s in zip(qs,best,top):
            if s < 0.22: un += 1; continue
            got[names[b]] += q["marks"]
        td, ta = sum(decl.values()), sum(got.values())
        band = 14 if acc is None else max(6, round(10*(1-acc)/0.45))
        print(f"\n### {subj} — mapped {1-un/len(qs):.0%}"
              + (f", accuracy {acc:.1%}" if acc else ", accuracy not measured (no gold set)")
              + f", band ±{band}pp")
        for j,n in enumerate(names):
            print(f"      {n[:38]:40s} <- {','.join(chs[i][0] for i in assign[n])}")
        print(f"  {'unit':44s} {'declared':>9s} {'actual':>7s} {'gap':>6s}  verdict")
        recs=[]
        for n in sorted(names, key=lambda x:-decl[x]):
            dp, ap = 100*decl[n]/td, 100*got[n]/ta; g = ap-dp
            v = "probably real" if abs(g)>=band+6 else ("suggestive" if abs(g)>=band else "noise")
            print(f"  {n[:44]:44s} {dp:8.0f}% {ap:6.0f}% {g:+6.0f}  {v}")
            recs.append(dict(unit=n, declared_pct=round(dp,1), actual_pct=round(ap,1), gap=round(g,1), verdict=v))
        final[subj]=dict(mapped=round(1-un/len(qs),3), accuracy=acc and round(acc,3), band=band,
                         chapters={n:[chs[i][0] for i in assign[n]] for n in names}, units=recs)
    json.dump(final, open(HERE/"ncert_all_final.json","w"), indent=1)

if __name__ == "__main__":
    main()
