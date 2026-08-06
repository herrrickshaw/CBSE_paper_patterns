#!/usr/bin/env python3
"""Final pass: split recurring CONTENT topics from recurring STEM FORMULAS, quantify
how repetitive the high-mark half of each paper is, and export everything to DuckDB.

Repetition index = share of high-mark MARKS attached to a content topic that appears
in >= 3 of the 5 exam years (2022-2026). It answers the actual question: is the board
re-testing the same material, or moving around inside the syllabus?
"""
import re, sys, json, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topics2 import is_english, ngrams, norm, CACHE

HERE = pathlib.Path(__file__).parent
OUT  = pathlib.Path.home() / "Downloads/cbse_question_bank"

# words that make a phrase a QUESTION FORMULA rather than a topic
GENERIC = set("""find calculate derive obtain prove show explain state define describe discuss
compare distinguish differentiate justify examine analyse analyze evaluate assess suggest
identify name list mention write draw solve determine estimate compute establish deduce
expression value values solution answer reason reasons meaning importance significance
features characteristics factors affecting influencing main basis given following data
blank blanks fill choose correct alternative valid arguments support statement steps taken
term terms types kind kinds role uses advantages disadvantages merits demerits need
brief briefly short long any two three four help suitable example examples his her their
much many more less high low large small new old first second general particular various
different same other such under over between within during through after before
hypothetical imaginary suppose assume let india government""".split())

def is_formula(g):
    w = g.split()
    return all(x in GENERIC for x in w)

def looks_mojibake(g):
    """Devanagari fonts that map to Latin produce vowel-starved strings like 'vrz maum'."""
    for w in g.split():
        v = sum(1 for c in w if c in "aeiou")
        if len(w) >= 3 and v == 0: return True
    return False

def main():
    rows = json.loads(CACHE.read_text())
    rows = [r for r in rows if r.get("question") and is_english(r["question"])]
    by = collections.defaultdict(list)
    for r in rows: by[r["subject"]].append(r)

    subjects, all_topics, all_formulas = {}, [], []
    for subj, qs in by.items():
        yrs_all = sorted({q["year"] for q in qs})
        if len(yrs_all) < 3: continue
        high = [q for q in qs if (q.get("marks") or 0) >= 4
                and len(q["question"].split()) <= 60]
        if len(high) < 25: continue
        yrs, pap, mk, ex = (collections.defaultdict(set), collections.defaultdict(set),
                            collections.Counter(), {})
        for q in high:
            for g in set(ngrams(q["question"])):
                yrs[g].add(q["year"]); pap[g].add(q["paper_file"])
                mk[g] += q.get("marks") or 0
                ex.setdefault(g, q["question"][:180])
        cands = [g for g in yrs if len(yrs[g]) >= 3 and not looks_mojibake(g)]
        cands.sort(key=lambda g: (-len(yrs[g]), -mk[g], -len(g.split())))
        topics, formulas, used_t, used_f = [], [], [], []
        for g in cands:
            rec = dict(subject=subj, phrase=g, years=len(yrs[g]), year_list=sorted(yrs[g]),
                       papers=len(pap[g]), marks=mk[g], example=ex[g])
            if is_formula(g):
                if any(g in u or u in g for u in used_f): continue
                used_f.append(g); formulas.append(rec)
            else:
                if any(g in u or u in g for u in used_t): continue
                used_t.append(g); topics.append(rec)
        top_t = topics[:25]
        tset = {t["phrase"] for t in top_t}
        hit_marks = sum(q["marks"] for q in high
                        if tset & set(ngrams(q["question"])))
        hi_marks = sum(q["marks"] for q in high)
        subjects[subj] = dict(
            years=yrs_all, papers=len({q["paper_file"] for q in qs}),
            questions=len(qs), high_q=len(high), high_marks=hi_marks,
            repetition_index=round(hit_marks / hi_marks, 3) if hi_marks else None,
            n_recurring_topics=len(topics), n_recurring_formulas=len(formulas))
        all_topics += top_t; all_formulas += formulas[:15]

    (HERE/"final_topics.json").write_text(json.dumps(
        dict(subjects=subjects, topics=all_topics, formulas=all_formulas), indent=1))

    print(f"{'subject':26s} {'papers':>6s} {'Qs':>6s} {'highQ':>6s} {'rep.index':>9s}  years")
    for s, d in sorted(subjects.items(), key=lambda x: -(x[1]['repetition_index'] or 0)):
        print(f"  {s[:24]:24s} {d['papers']:6d} {d['questions']:6d} {d['high_q']:6d} "
              f"{(d['repetition_index'] or 0):9.0%}  {len(d['years'])}")
    print("\n=== most persistent CONTENT topics (>=4 of 5 years) ===")
    for t in sorted([t for t in all_topics if t["years"] >= 4], key=lambda x: -x["marks"])[:25]:
        print(f"  {t['subject'][:20]:20s} {t['years']}yr {t['marks']:4d}mk  {t['phrase']}")
    print("\n=== most persistent STEM FORMULAS (question wording reused) ===")
    for t in sorted(all_formulas, key=lambda x: (-x["years"], -x["marks"]))[:20]:
        print(f"  {t['subject'][:20]:20s} {t['years']}yr {t['marks']:4d}mk  {t['phrase']}")

if __name__ == "__main__":
    main()
