"""Pure text/recurrence helpers shared by topics2.py and final_report.py.

No I/O here: everything takes rows (dicts with ``subject``, ``year``, ``paper_file``,
``question``, ``marks``) and returns data. Hindi-medium PDFs extract as Latin-looking
mojibake, so ``is_english`` gates on English function words rather than on codepoints.
"""
from __future__ import annotations

import collections
import re
from typing import Dict, Iterable, Iterator, List, Set, Tuple

HIGH_MARKS = 4        # a "high-mark" question carries at least this many marks
MAX_QUESTION_WORDS = 60   # longer stems quote an unseen passage, which is not a syllabus topic
MIN_RECURRING_YEARS = 3   # a phrase must appear in this many distinct exam years to recur

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


def usable_rows(rows: Iterable[dict]) -> List[dict]:
    """Keep rows whose question text is non-empty and English-medium."""
    return [r for r in rows if r.get("question") and is_english(r["question"])]


def group_by_subject(rows: Iterable[dict]) -> Dict[str, List[dict]]:
    """Group rows by their ``subject`` field, preserving row order."""
    by: Dict[str, List[dict]] = collections.defaultdict(list)
    for r in rows:
        by[r["subject"]].append(r)
    return by


def high_mark_questions(qs: Iterable[dict]) -> List[dict]:
    """Questions worth >= HIGH_MARKS marks and short enough not to be a quoted passage."""
    return [q for q in qs if (q.get("marks") or 0) >= HIGH_MARKS
            and len(q["question"].split()) <= MAX_QUESTION_WORDS]


def ngram_stats(high: Iterable[dict], example_len: int) -> Tuple[
        Dict[str, Set[str]], Dict[str, Set[str]], collections.Counter, Dict[str, str]]:
    """Per n-gram: exam years, paper files, summed marks and the first example question
    (truncated to ``example_len`` characters)."""
    yrs: Dict[str, Set[str]] = collections.defaultdict(set)
    pap: Dict[str, Set[str]] = collections.defaultdict(set)
    mk: collections.Counter = collections.Counter()
    ex: Dict[str, str] = {}
    for q in high:
        for g in set(ngrams(q["question"])):
            yrs[g].add(q["year"])
            pap[g].add(q["paper_file"])
            mk[g] += q.get("marks") or 0
            ex.setdefault(g, q["question"][:example_len])
    return yrs, pap, mk, ex


def unique_phrases(phrases: Iterable[str]) -> Iterator[str]:
    """Yield phrases, skipping any that contains, or is contained in, one already yielded."""
    used: List[str] = []
    for g in phrases:
        if any(g in u or u in g for u in used):
            continue
        used.append(g)
        yield g
