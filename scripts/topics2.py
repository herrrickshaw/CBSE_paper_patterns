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
from __future__ import annotations

import json
import logging
import os
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from parse_generic import parse_paper
from recurrence import (  # noqa: F401  (re-exported for sibling scripts)
    BOILER, FUNC, group_by_subject, high_mark_questions, is_english, ngram_stats, ngrams, norm,
    unique_phrases, usable_rows,
)

DEFAULT_ROOT = pathlib.Path.home() / "Downloads/cbse_official/past_papers"
ROOT = pathlib.Path(os.environ.get("CBSE_PAPERS_ROOT", DEFAULT_ROOT))  # directory of downloaded PDFs
HERE = pathlib.Path(__file__).parent
CACHE = HERE / "qcache_all.json"
log = logging.getLogger(__name__)

MIN_YEARS_FOR_SUBJECT = 3   # subjects seen in fewer exam years are skipped
MIN_HIGH_QUESTIONS = 25     # subjects with fewer high-mark questions are skipped
TOP_TOPICS = 20

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

def build_cache():
    """Parse every PDF under ROOT into question rows and write them to CACHE."""
    rows, pdfs = [], [p for p in sorted(ROOT.rglob("*.pdf")) if "_zips" not in str(p)]
    for i, p in enumerate(pdfs):
        try:
            qs, _, _ = parse_paper(p, canon_subject(p.parent.name), "past_paper", p.stem)
        except Exception as exc:  # one unreadable PDF must not stop the batch
            log.warning("skipping %s: %s", p.name, exc)
            continue
        yr = p.parent.parent.name
        for q in qs:
            q["year"] = yr.replace("-COMPTT", "")
            q["exam"] = "compartment" if "COMPTT" in yr else "main"
            q["paper_file"] = p.name
        rows += qs
        if i % 200 == 0: print(f"  {i}/{len(pdfs)}", flush=True)
    CACHE.write_text(json.dumps(rows)); return rows


def analyse_subject(qs):
    """Recurring high-mark topics for one subject's rows, or None if there is too little data."""
    yrs_all = sorted({q["year"] for q in qs})
    if len(yrs_all) < MIN_YEARS_FOR_SUBJECT: return None
    high = high_mark_questions(qs)
    if len(high) < MIN_HIGH_QUESTIONS: return None
    yrs, pap, mk, ex = ngram_stats(high, example_len=150)
    cands = [(g, len(yrs[g]), len(pap[g]), mk[g]) for g in yrs if len(yrs[g]) >= MIN_YEARS_FOR_SUBJECT]
    cands.sort(key=lambda x: (-x[1], -x[3], -len(x[0].split())))
    by_phrase = {c[0]: c for c in cands}
    chosen = []
    for g in unique_phrases(c[0] for c in cands):
        _, ny, np_, m = by_phrase[g]
        chosen.append(dict(topic=g, years=ny, papers=np_, marks=m,
                           year_list=sorted(yrs[g]), example=ex[g]))
        if len(chosen) >= TOP_TOPICS: break
    if not chosen: return None
    topics = {c["topic"] for c in chosen}
    covered = {id(q) for q in high for g in set(ngrams(q["question"])) if g in topics}
    return dict(years=yrs_all, papers=len({q["paper_file"] for q in qs}),
                high_q=len(high), high_marks=sum(q.get("marks") or 0 for q in high),
                recurring_share=round(len(covered)/len(high), 3), topics=chosen)


def build_report(rows):
    """Subject -> analysis dict for every subject with enough data."""
    report = {}
    for subj, qs in group_by_subject(rows).items():
        res = analyse_subject(qs)
        if res: report[subj] = res
    return report


def main():
    rows = json.loads(CACHE.read_text()) if CACHE.exists() else build_cache()
    tot = len(rows)
    rows = usable_rows(rows)
    print(f"\nquestions parsed: {tot}  | usable English-medium: {len(rows)} ({len(rows)/tot:.0%})")
    report = build_report(rows)
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
