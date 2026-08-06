#!/usr/bin/env python3
"""Are CBSE Class-12 papers re-testing the same topics in their high-mark questions?

Fixes over v1, each of which was inflating or corrupting the answer:
 1. ENGLISH GATE. Hindi-medium PDFs extract as mojibake ("moozmb ama omo amoj") because
    the embedded Devanagari font maps to Latin code points. A Devanagari-codepoint filter
    does not catch it. Gate on English function words instead.
 2. RECURRENCE = DISTINCT EXAM YEARS, not papers. Sets within one sitting are ~75% the
    same paper, so paper counts manufacture recurrence out of a single year's passage.
    A topic must appear in >= 3 distinct years to count as recurring.
 3. SUBJECT CANONICALISATION. CBSE renames zips year to year (Math/Mathematics,
    Bs/Business_Studies, Eng Core/English_Core, and its own typo "Poltical Science").
 4. COMPREHENSION PASSAGES EXCLUDED. In language papers the long questions quote an
    unseen passage; that is not a syllabus topic. Questions >60 words are dropped.
"""
import re, sys, json, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from parse_generic import parse_paper

ROOT = pathlib.Path.home() / "Downloads/cbse_official/past_papers"
HERE = pathlib.Path(__file__).parent
CACHE = HERE / "qcache_all.json"

FUNC = set("the of and to in is are was were for with that this from which by as an on at "
           "it its has have had be been will would should can could not or if what why how".split())
def is_english(s):
    w = re.findall(r'[a-z]+', s.lower())
    if len(w) < 6: return False
    return sum(1 for x in w if x in FUNC) >= 3

BOILER = set("""answer following question questions explain describe discuss give reason reasons
state write briefly any two three four five six give example examples justify statement support
above given below mentioned choose correct option options alternative alternatives marks mark
candidate candidates section part note read carefully attempt words each which what when where
who whom how why the and for with from that this these those are was were will would shall
your you their there here also more most other others such same than then them they have has
had been being into out over under about after before during through between among within
true false identify name list mention define differentiate distinguish elaborate examine
analyse analyze assess evaluate highlight suitable terms term context light view point points
value values case study based source passage cartoon map picture image figure diagram following
one two three four five six seven eight nine ten first second third pass necessary entry entries
year years ended march april date dates crore lakh rupees respectively また following short long""".split())

ALIAS = {
 'math':'Mathematics','maths':'Mathematics','mathematics':'Mathematics',
 'bs':'Business Studies','business studies':'Business Studies',
 'eng core':'English Core','english core':'English Core','englishcore':'English Core',
 'eng elective':'English Elective','english elective':'English Elective',
 'poltical science':'Political Science','political science':'Political Science',
 'pol science':'Political Science','polsci':'Political Science',
 'hindi core':'Hindi Core','hindi elective':'Hindi Elective',
 'engg graphics':'Engineering Graphics','engineering graphics':'Engineering Graphics',
 'artificial intelligence':'Artificial Intelligence','artificial  intelligence':'Artificial Intelligence',
 'financial market management':'Financial Markets Management',
 'financial markets management':'Financial Markets Management',
 'web application':'Web Applications','web applications':'Web Applications',
 'typography computer':'Typography & Computer Applications',
 'typography comp applications':'Typography & Computer Applications',
 'typography and computer applications':'Typography & Computer Applications',
 'typography  computer applications':'Typography & Computer Applications',
 'typography and com app':'Typography & Computer Applications',
 'info tech':'Information Technology','information technology':'Information Technology',
 'phy edu':'Physical Education','physical education':'Physical Education',
 'home science':'Home Science','computer science':'Computer Science',
 'ip':'Informatics Practices','informatics practices':'Informatics Practices',
}
def canon_subject(d):
    s = re.sub(r'^\d+[_ ]', '', d).replace('_', ' ').strip().lower()
    s = re.sub(r'\s+', ' ', s)
    return ALIAS.get(s, s.title())

def norm(s):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z ]', ' ', s.lower())).strip()

def ngrams(text, lo=2, hi=4):
    w = [x for x in norm(text).split() if len(x) > 2]
    for n in range(lo, hi+1):
        for i in range(len(w)-n+1):
            g = w[i:i+n]
            if g[0] in BOILER or g[-1] in BOILER: continue
            if all(x in BOILER for x in g): continue
            yield " ".join(g)

def build_cache():
    rows, pdfs = [], [p for p in sorted(ROOT.rglob("*.pdf")) if "_zips" not in str(p)]
    for i, p in enumerate(pdfs):
        try:
            qs, _, _ = parse_paper(p, canon_subject(p.parent.name), "past_paper", p.stem)
        except Exception:
            continue
        yr = p.parent.parent.name
        for q in qs:
            q["year"] = yr.replace("-COMPTT", "")
            q["exam"] = "compartment" if "COMPTT" in yr else "main"
            q["paper_file"] = p.name
        rows += qs
        if i % 200 == 0: print(f"  {i}/{len(pdfs)}", flush=True)
    CACHE.write_text(json.dumps(rows)); return rows

def main():
    rows = json.loads(CACHE.read_text()) if CACHE.exists() else build_cache()
    tot = len(rows)
    rows = [r for r in rows if r.get("question") and is_english(r["question"])]
    print(f"\nquestions parsed: {tot}  | usable English-medium: {len(rows)} ({len(rows)/tot:.0%})")

    by = collections.defaultdict(list)
    for r in rows: by[r["subject"]].append(r)

    report = {}
    for subj, qs in by.items():
        yrs_all = sorted({q["year"] for q in qs})
        if len(yrs_all) < 3: continue
        high = [q for q in qs if (q.get("marks") or 0) >= 4
                and len(q["question"].split()) <= 60]     # drop quoted passages
        if len(high) < 25: continue
        yrs, pap, mk, ex = (collections.defaultdict(set), collections.defaultdict(set),
                            collections.Counter(), collections.defaultdict(list))
        for q in high:
            for g in set(ngrams(q["question"])):
                yrs[g].add(q["year"]); pap[g].add(q["paper_file"])
                mk[g] += q.get("marks") or 0; ex[g].append(q["question"][:150])
        cands = [(g, len(yrs[g]), len(pap[g]), mk[g]) for g in yrs if len(yrs[g]) >= 3]
        cands.sort(key=lambda x: (-x[1], -x[3], -len(x[0].split())))
        chosen, used = [], []
        for g, ny, np_, m in cands:
            if any(g in u or u in g for u in used): continue
            used.append(g); chosen.append(dict(topic=g, years=ny, papers=np_, marks=m,
                                               year_list=sorted(yrs[g]), example=ex[g][0]))
            if len(chosen) >= 20: break
        if not chosen: continue
        hi_marks = sum(q.get("marks") or 0 for q in high)
        covered = {id(q) for q in high for g in set(ngrams(q["question"]))
                   if g in {c["topic"] for c in chosen}}
        report[subj] = dict(years=yrs_all, papers=len({q["paper_file"] for q in qs}),
                            high_q=len(high), high_marks=hi_marks,
                            recurring_share=round(len(covered)/len(high), 3), topics=chosen)
    (HERE/"topic_report2.json").write_text(json.dumps(report, indent=1))
    order = sorted(report.items(), key=lambda x: -x[1]["high_q"])
    for subj, d in order:
        print(f"\n### {subj} — {d['papers']} papers, {d['high_q']} high-mark Qs, "
              f"years {','.join(d['years'])}, top-20 topics touch {d['recurring_share']:.0%} of them")
        for c in d["topics"][:10]:
            print(f"   {c['years']} yrs ({','.join(c['year_list'])}) | {c['papers']:2d} papers | "
                  f"{c['marks']:4d} mk | {c['topic']}")

if __name__ == "__main__":
    main()
