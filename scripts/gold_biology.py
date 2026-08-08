#!/usr/bin/env python3
"""A larger Biology gold set, mined from NCERT chapter vocabulary.

A term that occurs in exactly ONE unit's chapters, and never in another's, is a strong
label for that unit. That is a different signal from the mapping method being tested
(which embeds the unit NAME), so it does not leak.

Guards, because a big noisy gold set is worse than a small clean one:
  * term must appear >= 8 times inside its own unit's chapters (not a passing mention)
  * term must appear ZERO times in every other unit's chapters
  * term must be >= 5 characters and not a general-science word
  * a question matching terms from two different units is dropped as ambiguous
"""
import re, json, pathlib, collections, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topics2 import is_english

MD   = pathlib.Path.home()/"Downloads/cbse_md/ncert_xii"
HERE = pathlib.Path(__file__).parent
UNIT_CH = {                       # NCERT Biology XII, verified against chapter content
 "VI Reproduction":                       [1,2,3],
 "VII Genetics and Evolution":            [4,5,6],
 "VIII Biology and Human Welfare":        [7,8],
 "IX Biotechnology and its Applications": [9,10],
 "X Ecology and Environment":             [11,12,13],
}
# Mined terms that survived the frequency filters but fail a precision audit:
#   'flowers'  -> labels Mendel's pea-plant crosses (Genetics) as Reproduction
#   'referred' -> generic English, matched Biotechnology and Genetics questions alike
#   'round'/'mechanism'/'expression' -> too general to carry a unit on their own
BLOCK = {"flowers", "referred", "round", "mechanism", "expression", "ovary"}

GENERAL = set("""biology chapter figure reprint example examples student process processes
organism organisms living called different various important several general study studies
following shown given result results structure structures function functions system systems
plants animals human humans body cell cells reprinted table section units unit level levels
formed produced present number numbers types type form forms first second third fourth""".split())

def text(ch):
    p = MD/f"lebo1{ch:02d}.md"
    if not p.exists(): return ""
    t = re.sub(r'^---.*?^---', '', p.read_text(errors="ignore"), flags=re.S|re.M)
    return re.sub(r'```|## page \d+|\s+', ' ', t).lower()

unit_text = {u: " ".join(text(c) for c in chs) for u, chs in UNIT_CH.items()}
counts = {}
for u, t in unit_text.items():
    terms = re.findall(r'\b[a-z]{5,}(?:\s+[a-z]{4,}){0,2}\b', t)
    counts[u] = collections.Counter(x for x in terms if not set(x.split()) & GENERAL)

# Dominance ratio, not absence: NCERT chapters cross-reference each other constantly
# ("plasmid" appears in both Molecular Basis and Biotechnology), so requiring zero
# occurrences elsewhere deletes precisely the diagnostic vocabulary.
exclusive = collections.defaultdict(list)
for u, c in counts.items():
    others = [o for o in counts if o != u]
    for term, n in c.items():
        if n < 8: continue
        worst = max(counts[o].get(term, 0) for o in others)
        if n < 8 * max(worst, 1): continue          # >=8x more frequent here than anywhere else
        exclusive[u].append((term, n))

rows = json.loads((HERE/"qcache_all.json").read_text())
qs = [r for r in rows if r.get("question") and is_english(r["question"])
      and r.get("marks") and r["subject"] == "Biology"]

# keep only terms that actually occur in exam questions
useful = collections.defaultdict(list)
for u, terms in exclusive.items():
    for term, n in sorted(terms, key=lambda x: -x[1]):
        hits = sum(1 for q in qs if term in q["question"].lower())
        if term in BLOCK: continue
        if hits >= 2: useful[u].append((term, n, hits))

print("unit-exclusive NCERT terms that also appear in exam questions:")
for u in UNIT_CH:
    print(f"\n  {u}  ({len(useful[u])} terms)")
    for term, n, h in useful[u][:10]: print(f"      {h:4d} questions  {term!r}  ({n}x in chapters)")

# union with the hand-written patterns already in gold_patterns.json
hand = json.loads((HERE/"gold_patterns.json").read_text()).get("Biology", {})
pats = {u: [re.escape(t) for t, _, _ in useful[u]] + hand.get(u, []) for u in UNIT_CH}
lab, amb = collections.Counter(), 0
for q in qs:
    t = q["question"].lower()
    hit = [u for u, ps in pats.items() if any(re.search(p, t) for p in ps)]
    if len(hit) == 1: lab[hit[0]] += 1
    elif len(hit) > 1: amb += 1
tot = sum(lab.values())
print(f"\nGOLD SET: {tot} questions of {len(qs)} ({tot/len(qs):.0%}); {amb} ambiguous dropped")
for u, n in lab.most_common(): print(f"   {n:5d}  {u}")
json.dump({u: [t for t, _, _ in useful[u]] for u in UNIT_CH}, open(HERE/"gold_biology_terms.json","w"), indent=1)
