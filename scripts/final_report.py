#!/usr/bin/env python3
"""Final pass: split recurring CONTENT topics from recurring STEM FORMULAS, quantify
how repetitive the high-mark half of each paper is, and export everything to DuckDB.

Repetition index = share of high-mark MARKS attached to a content topic that appears
in >= 3 of the 5 exam years (2022-2026). It answers the actual question: is the board
re-testing the same material, or moving around inside the syllabus?
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topics2 import CACHE
from recurrence import (
    MIN_RECURRING_YEARS, group_by_subject, high_mark_questions, ngram_stats, ngrams, unique_phrases,
    usable_rows,
)

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

MIN_YEARS_FOR_SUBJECT = 3   # subjects seen in fewer exam years are skipped
MIN_HIGH_QUESTIONS = 25     # subjects with fewer high-mark questions are skipped
TOP_TOPICS = 25             # content topics counted towards the repetition index
TOP_FORMULAS = 15           # stem formulas kept per subject


def analyse_subject(subj, qs):
    """Return (summary dict, top topics, formulas) for one subject, or None if too little data."""
    yrs_all = sorted({q["year"] for q in qs})
    if len(yrs_all) < MIN_YEARS_FOR_SUBJECT: return None
    high = high_mark_questions(qs)
    if len(high) < MIN_HIGH_QUESTIONS: return None
    yrs, pap, mk, ex = ngram_stats(high, example_len=180)
    cands = [g for g in yrs if len(yrs[g]) >= MIN_RECURRING_YEARS and not looks_mojibake(g)]
    cands.sort(key=lambda g: (-len(yrs[g]), -mk[g], -len(g.split())))
    topics, formulas = [], []
    # formulas and topics are de-duplicated independently of each other
    for is_f, bucket in ((True, formulas), (False, topics)):
        for g in unique_phrases(g for g in cands if is_formula(g) == is_f):
            bucket.append(dict(subject=subj, phrase=g, years=len(yrs[g]), year_list=sorted(yrs[g]),
                               papers=len(pap[g]), marks=mk[g], example=ex[g]))
    top_t = topics[:TOP_TOPICS]
    tset = {t["phrase"] for t in top_t}
    hit_marks = sum(q["marks"] for q in high if tset & set(ngrams(q["question"])))
    hi_marks = sum(q["marks"] for q in high)
    summary = dict(
        years=yrs_all, papers=len({q["paper_file"] for q in qs}),
        questions=len(qs), high_q=len(high), high_marks=hi_marks,
        repetition_index=round(hit_marks / hi_marks, 3) if hi_marks else None,
        n_recurring_topics=len(topics), n_recurring_formulas=len(formulas))
    return summary, top_t, formulas[:TOP_FORMULAS]


def build_final(rows):
    """Aggregate per-subject results into {subjects, topics, formulas}."""
    subjects, all_topics, all_formulas = {}, [], []
    for subj, qs in group_by_subject(usable_rows(rows)).items():
        res = analyse_subject(subj, qs)
        if res is None: continue
        subjects[subj] = res[0]
        all_topics += res[1]; all_formulas += res[2]
    return dict(subjects=subjects, topics=all_topics, formulas=all_formulas)


def main():
    final = build_final(json.loads(CACHE.read_text()))
    subjects, all_topics, all_formulas = final["subjects"], final["topics"], final["formulas"]
    (HERE/"final_topics.json").write_text(json.dumps(final, indent=1))

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
