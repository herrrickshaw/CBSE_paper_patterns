#!/usr/bin/env python3
"""Three stronger methods than n-gram mining, none needing a model download.

1. NEAR-DUPLICATE DETECTION (TF-IDF + cosine). Finds questions repeated near-verbatim
   across DIFFERENT exam years. This is the hardest evidence of "they re-test the same
   thing" - not a shared topic, the same question.
2. BLOOM / COMPETENCY CLASSIFICATION vs CBSE's OWN BLUEPRINT. Every senior-secondary
   curriculum PDF publishes a "Typology of Questions" table with target percentages
   (Physics: 38% Remembering+Understanding / 32% Applying / 30% Analysing). Classify the
   real questions by command verb and compare against the target.
3. CURRICULUM UNIT WEIGHTAGE. The same PDFs give marks per unit. Extract them so actual
   marks per unit can be checked against the declared weightage.
"""
import re, json, sys, pathlib, collections, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topics2 import is_english, CACHE

HERE = pathlib.Path(__file__).parent
CUR  = pathlib.Path.home() / "Downloads/cbse_official/curriculum"

# ---------- 1. near-duplicate questions across years ----------
INSTRUCTION = re.compile(
    r'^\s*(answer|attempt|read|write)\s+(any|the following|all)\b|'
    r'following in about\s*\d+|in about \d+\s*[-\u2013]?\s*\d*\s*words|'
    r'^\s*answer the following|^\s*do as directed', re.I)

def near_duplicates(rows, min_sim=0.80):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    out = []
    by = collections.defaultdict(list)
    for r in rows:
        if (r.get("marks") or 0) >= 3 and 8 <= len(r["question"].split()) <= 80 \
           and not INSTRUCTION.search(r["question"]):
            by[r["subject"]].append(r)
    for subj, qs in by.items():
        if len(qs) < 40: continue
        texts = [q["question"] for q in qs]
        try:
            X = TfidfVectorizer(ngram_range=(1,2), min_df=2, sublinear_tf=True,
                                stop_words="english").fit_transform(texts)
        except ValueError:
            continue
        S = cosine_similarity(X, dense_output=False)
        S = S.tocoo()
        seen = set()
        for i, j, v in zip(S.row, S.col, S.data):
            if i >= j or v < min_sim: continue
            a, b = qs[i], qs[j]
            if a["year"] == b["year"]: continue          # same sitting = same paper, ignore
            key = (min(i,j), max(i,j))
            if key in seen: continue
            seen.add(key)
            out.append(dict(subject=subj, similarity=round(float(v),3),
                            year_a=a["year"], year_b=b["year"],
                            marks=a.get("marks"), q_a=a["question"][:220], q_b=b["question"][:220]))
    out.sort(key=lambda d: -d["similarity"])
    return out

# ---------- 2. Bloom classification vs declared blueprint ----------
BLOOM = {
 "remember_understand": r"\b(state|define|name|list|write|mention|identify|recall|label|"
                        r"what is|who|when|expand|full form|choose|fill in|match|arrange|"
                        r"explain|describe|discuss|outline|summarise|summarize|illustrate|"
                        r"give an account|briefly)\b",
 "apply":               r"\b(calculate|compute|find|solve|determine|derive|prepare|pass |"
                        r"draw|construct|estimate|apply|show that|prove|obtain|use the|"
                        r"complete the|journal ?is|record)\b",
 "analyse_evaluate_create": r"\b(analyse|analyze|examine|evaluate|assess|justify|compare|"
                        r"contrast|differentiate|distinguish|critically|interpret|infer|"
                        r"suggest|comment|do you agree|give reasons|support your|argue|"
                        r"validate|elaborate|why do|to what extent)\b",
}
def bloom_of(q):
    t = q.lower()
    hits = [k for k, rx in BLOOM.items() if re.search(rx, t)]
    if not hits: return None
    # most demanding level wins - CBSE counts a question at its highest demand
    for lvl in ("analyse_evaluate_create", "apply", "remember_understand"):
        if lvl in hits: return lvl

TYPO_RX = re.compile(r'(\d{1,3})\s*%')
def declared_typology(pdf):
    txt = subprocess.run(["pdftotext","-layout",str(pdf),"-"],capture_output=True,text=True,timeout=120).stdout
    low = txt.lower()
    i = -1
    for marker in ("typology of questions", "weightage based on competencies",
                   "competencies                    marks", "question paper design"):
        i = low.find(marker)
        if i >= 0: break
    if i < 0: return None
    chunk = txt[i:i+2500]
    pcts = [int(x) for x in TYPO_RX.findall(chunk) if 5 <= int(x) <= 95]
    # keep the first three distinct percentages that sum near 100
    for a in range(len(pcts)):
        tri = pcts[a:a+3]
        if len(tri) == 3 and 95 <= sum(tri) <= 105:
            return dict(remember_understand=tri[0], apply=tri[1], analyse_evaluate_create=tri[2])
    return None

CUR_ALIAS = {
 "Accountancy":"Accountancy_SrSec","Economics":"Economics_SrSec","History":"History_SrSec",
 "Political Science":"PoliticalScience_SrSec","Physics":"Physics_SrSec","Chemistry":"Chemistry_SrSec",
 "Biology":"Biology_SrSec","Mathematics":"Mathematics_SrSec","Business Studies":"BusinessStudies_SrSec",
 "Geography":"Geography_SrSec","Computer Science":"Computer_Science_SrSec","English Core":"English_core_SrSec",
}
def blueprint_table(rows):
    res = {}
    for subj, cur in CUR_ALIAS.items():
        cands = sorted(CUR.glob(cur+"*.pdf"))
        cands = [c for c in cands if "Hi_" not in c.name and "Hindi" not in c.name]
        decl = declared_typology(cands[0]) if cands else None
        qs = [r for r in rows if r["subject"] == subj and r.get("marks")]
        if not qs: continue
        got = collections.Counter()
        for q in qs:
            b = bloom_of(q["question"])
            if b: got[b] += q["marks"]
        tot = sum(got.values()) or 1
        actual = {k: round(100*v/tot) for k, v in got.items()}
        res[subj] = dict(declared=decl, actual=actual, marks_classified=tot,
                         questions=len(qs), curriculum=cands[0].name if cands else None)
    return res

# ---------- 3. unit weightage from the curriculum ----------
UNIT_RX = re.compile(r'^\s*(Unit[- ]?\s*[IVX0-9]+[.:]?\s*[^\d]{3,60}?)\s{2,}(\d{1,3})\s*$', re.M)
def unit_weightage():
    out = {}
    for subj, cur in CUR_ALIAS.items():
        cands = [c for c in sorted(CUR.glob(cur+"*.pdf")) if "Hi_" not in c.name and "Hindi" not in c.name]
        if not cands: continue
        txt = subprocess.run(["pdftotext","-layout",str(cands[0]),"-"],capture_output=True,text=True,timeout=120).stdout
        units = [(re.sub(r'\s+',' ',m.group(1)).strip(), int(m.group(2))) for m in UNIT_RX.finditer(txt)]
        if units: out[subj] = units
    return out

if __name__ == "__main__":
    rows = [r for r in json.loads(CACHE.read_text()) if r.get("question") and is_english(r["question"])]
    print(f"corpus: {len(rows)} English questions\n")

    print("=" * 70); print("1. NEAR-DUPLICATE QUESTIONS ACROSS DIFFERENT YEARS"); print("=" * 70)
    dups = near_duplicates(rows)
    json.dump(dups, open(HERE/"near_duplicates.json","w"), indent=1)
    print(f"pairs at cosine >= 0.80, different exam years: {len(dups)}")
    per = collections.Counter(d["subject"] for d in dups)
    for s, n in per.most_common(12): print(f"   {n:5d}  {s}")
    print("\n  strongest examples:")
    for d in dups[:6]:
        print(f"   [{d['similarity']}] {d['subject']} {d['year_a']} vs {d['year_b']} ({d['marks']}mk)")
        print(f"      A: {d['q_a'][:120]}")
        print(f"      B: {d['q_b'][:120]}")

    print("\n" + "=" * 70); print("2. ACTUAL BLOOM MIX vs CBSE's DECLARED TYPOLOGY"); print("=" * 70)
    bp = blueprint_table(rows)
    json.dump(bp, open(HERE/"blueprint_vs_actual.json","w"), indent=1)
    print(f"{'subject':20s} {'declared R+U/App/AEC':>22s}   {'actual R+U/App/AEC':>20s}")
    for s, d in bp.items():
        dec = d["declared"]; act = d["actual"]
        ds = f"{dec['remember_understand']}/{dec['apply']}/{dec['analyse_evaluate_create']}" if dec else "not published"
        as_ = f"{act.get('remember_understand',0)}/{act.get('apply',0)}/{act.get('analyse_evaluate_create',0)}"
        print(f"  {s[:18]:18s} {ds:>22s}   {as_:>20s}")

    print("\n" + "=" * 70); print("3. DECLARED UNIT WEIGHTAGE (authoritative topic taxonomy)"); print("=" * 70)
    uw = unit_weightage()
    json.dump(uw, open(HERE/"unit_weightage.json","w"), indent=1)
    for s, units in list(uw.items())[:6]:
        print(f"\n  {s}:")
        for name, mk in units[:8]: print(f"     {mk:3d} mk  {name[:64]}")
