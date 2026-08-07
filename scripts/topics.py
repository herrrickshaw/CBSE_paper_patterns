#!/usr/bin/env python3
"""Do CBSE papers test the same topics repeatedly in the high-mark questions?

Method (no hand-written topic list, so the answer isn't smuggled in by the lexicon):
 1. parse every paper into questions with marks (parse_generic)
 2. keep the HIGH-MARK questions only (subject-specific threshold = the paper's
    upper mark bands, i.e. >= 4 marks)
 3. mine candidate topics as 2-4 word n-grams that recur in >= 3 DISTINCT papers,
    after stripping exam boilerplate ("explain the following", "give reasons"...)
 4. for each topic report: how many distinct papers, how many distinct exam years,
    total marks attached, and the recurrence rate = papers_hit / papers_in_subject

A topic that shows up in most years at high marks is a topic the board keeps re-testing.
"""
import re, sys, json, pathlib, collections, subprocess
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from parse_generic import parse_paper

ROOT = pathlib.Path.home() / "Downloads/cbse_official/past_papers"
CACHE = pathlib.Path(__file__).parent / "qcache.json"

BOILER = set("""answer following question questions explain describe discuss give reason reasons
state write briefly any two three four five give example examples justify statement support
above given below mentioned choose correct option options alternative alternatives marks mark
candidate candidates section part note read carefully attempt words each which what when where
who whom how why the and for with from that this these those are was were will would shall
your you their there here also more most other others such same than then them they have has
had been being into out over under about after before during through between among within
also true false identify name list mention define differentiate distinguish elaborate examine
analyse analyze assess evaluate highlight suitable following terms term context light view
value values case study based source passage cartoon map picture image figure diagram
one two three four five six seven eight nine ten first second third pass necessary entry
entries account accounts amount amounts year years ended march april date dates rs crore lakh""".split())

def norm(s):
    s = re.sub(r'[^a-z ]', ' ', s.lower())
    return re.sub(r'\s+', ' ', s).strip()

def ngrams(text, lo=2, hi=4):
    w = [x for x in norm(text).split() if len(x) > 2]
    for n in range(lo, hi+1):
        for i in range(len(w)-n+1):
            g = w[i:i+n]
            if all(x in BOILER for x in g):      # pure boilerplate
                continue
            if g[0] in BOILER or g[-1] in BOILER: # boilerplate at the edges
                continue
            yield " ".join(g)

def subject_of(path):
    """<year>/<Subject>/file.pdf -> canonical subject name"""
    sub = path.parent.name
    s = re.sub(r'^\d+_', '', sub).replace('_', ' ').strip().lower()
    s = re.sub(r'\s+', ' ', s)
    ALIAS = {
      'accountancy':'Accountancy','economics':'Economics','history':'History',
      'political science':'Political Science','computer science':'Computer Science',
      'artificial intelligence':'Artificial Intelligence','artificial  intelligence':'Artificial Intelligence',
      'information technology':'Information Technology','web applications':'Web Applications',
      'web application':'Web Applications','taxation':'Taxation','cost accounting':'Cost Accounting',
      'financial market management':'Financial Markets Management',
      'financial markets management':'Financial Markets Management',
      'engineering graphics':'Engineering Graphics','engg graphics':'Engineering Graphics',
      'typography computer':'Typography & Computer Applications',
      'typography comp applications':'Typography & Computer Applications',
      'typography and computer applications':'Typography & Computer Applications',
      'typography  computer applications':'Typography & Computer Applications',
      'typography and com app':'Typography & Computer Applications',
    }
    return ALIAS.get(s, s.title())

def year_of(path):
    y = path.parent.parent.name
    return y

def load():
    if CACHE.exists():
        return json.loads(CACHE.read_text())
    rows = []
    pdfs = sorted(ROOT.rglob("*.pdf"))
    for i, p in enumerate(pdfs):
        if "_zips" in str(p): continue
        try:
            qs, _, _ = parse_paper(p, subject_of(p), "past_paper", p.stem)
        except Exception:
            continue
        y = year_of(p)
        for q in qs:
            q["year"] = y.replace("-COMPTT", "")
            q["exam"] = "compartment" if "COMPTT" in y else "main"
            q["paper_file"] = p.name
        rows += qs
        if i % 50 == 0: print(f"  parsed {i}/{len(pdfs)}", flush=True)
    CACHE.write_text(json.dumps(rows))
    return rows

def main():
    rows = load()
    print(f"\nquestions parsed from past papers: {len(rows)}")
    by_subj = collections.defaultdict(list)
    for r in rows: by_subj[r["subject"]].append(r)

    report = {}
    for subj, qs in sorted(by_subj.items(), key=lambda x: -len(x[1])):
        papers = {q["paper_file"] for q in qs}
        if len(papers) < 4: continue
        high = [q for q in qs if (q.get("marks") or 0) >= 4]
        if len(high) < 15: continue
        # topic -> set(papers), set(years), marks
        hit_papers = collections.defaultdict(set)
        hit_years  = collections.defaultdict(set)
        hit_marks  = collections.Counter()
        hit_qs     = collections.defaultdict(list)
        for q in high:
            seen = set()
            for g in ngrams(q["question"]):
                if g in seen: continue
                seen.add(g)
                hit_papers[g].add(q["paper_file"])
                hit_years[g].add(q["year"])
                hit_marks[g] += q.get("marks") or 0
                hit_qs[g].append(q)
        cands = [(g, len(hit_papers[g]), len(hit_years[g]), hit_marks[g])
                 for g in hit_papers if len(hit_papers[g]) >= 3]
        # prefer longer, more specific phrases when one contains another
        cands.sort(key=lambda x: (-x[1], -len(x[0].split())))
        chosen, used = [], []
        for g, np_, ny, mk in cands:
            if any(g in u or u in g for u in used): continue
            used.append(g); chosen.append((g, np_, ny, mk))
            if len(chosen) >= 25: break
        report[subj] = dict(papers=len(papers), high_q=len(high),
                            years=sorted({q["year"] for q in qs}), topics=chosen)
    out = pathlib.Path(__file__).parent / "topic_report.json"
    out.write_text(json.dumps(report, indent=1))
    for subj, d in report.items():
        print(f"\n### {subj}  ({d['papers']} papers, {d['high_q']} high-mark Qs, years {d['years'][0]}-{d['years'][-1]})")
        for g, np_, ny, mk in d["topics"][:12]:
            print(f"   {np_:3d} papers | {ny} yrs | {mk:4d} marks | {g}")

if __name__ == "__main__":
    main()
