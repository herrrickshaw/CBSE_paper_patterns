#!/usr/bin/env python3
"""Map exam questions onto the CBSE curriculum's own units, then compare the marks a
unit ACTUALLY attracts against the weightage CBSE DECLARES for it.

The unit list and its marks come from the curriculum PDFs, so the taxonomy is the
board's own - not mined phrases. A question is assigned to the unit whose name-derived
keywords it best matches; unassignable questions are reported, not hidden.
"""
import re, json, sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topics2 import is_english, CACHE

HERE=pathlib.Path(__file__).parent
units=json.loads((HERE/"unit_weightage.json").read_text())

STOP=set("unit and the of for to in a an with from part i ii iii iv v vi accounting".split())
EXTRA={  # a few unit names are too terse to match on their own words
 "Accounting for Partnership Firms":{"partner","partnership","goodwill","admission","retirement","dissolution","sacrificing","gaining","firm"},
 "Accounting for Companies":{"share","debenture","forfeit","issue","company","capital","allotment","premium"},
 "Analysis of Financial Statements":{"ratio","common","comparative","liquidity","solvency","turnover","statement"},
 "Cash Flow Statement":{"cash","flow","operating","investing","financing"},
}
def keywords(name):
    base={w for w in re.findall(r'[a-z]{4,}', name.lower()) if w not in STOP}
    for k,v in EXTRA.items():
        if k.lower() in name.lower(): base |= v
    return base

rows=[r for r in json.loads(CACHE.read_text()) if r.get("question") and is_english(r["question"]) and r.get("marks")]
by=collections.defaultdict(list)
for r in rows: by[r["subject"]].append(r)

print(f"{'subject':20s} {'assigned':>9s} {'unit':38s} {'declared':>9s} {'actual':>7s} {'gap':>6s}")
out={}
for subj, us in units.items():
    qs=by.get(subj) or []
    if not qs: continue
    kw={name:keywords(name) for name,_ in us}
    tot_decl=sum(m for _,m in us)
    got=collections.Counter(); unassigned=0; unassigned_marks=0
    for q in qs:
        w=set(re.findall(r'[a-z]{4,}', q["question"].lower()))
        best,score=None,0
        for name,k in kw.items():
            s=len(w & k)
            if s>score: best,score=name,s
        if best: got[best]+=q["marks"]
        else: unassigned+=1; unassigned_marks+=q["marks"]
    tot_act=sum(got.values())
    if tot_act<50: continue
    cov=1-unassigned/len(qs)
    print(f"\n{subj:20s} {cov:8.0%} of questions mapped to a unit "
          f"({len(qs)-unassigned}/{len(qs)}; {unassigned_marks} marks unassigned)")
    rowsout=[]
    for name,decl in us:
        d=100*decl/tot_decl; a=100*got[name]/tot_act if tot_act else 0
        rowsout.append(dict(unit=name, declared_pct=round(d,1), actual_pct=round(a,1),
                            gap=round(a-d,1), declared_marks=decl, actual_marks=got[name]))
        print(f"{'':20s} {'':9s} {name[:38]:38s} {d:8.0f}% {a:6.0f}% {a-d:+6.0f}")
    out[subj]=dict(coverage=round(cov,3), units=rowsout)
(HERE/"syllabus_match.json").write_text(json.dumps(out, indent=1))
