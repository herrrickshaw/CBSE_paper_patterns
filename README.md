# CBSE paper patterns

Structural and topic-recurrence analysis of CBSE board papers — **1,955 Class XII papers**
(2022–2026) analysed in depth, plus a **6,409-document corpus** spanning Class X, and every
sample paper and marking scheme back to 2015-16
covering **30,734 parsed questions**.

It answers one question: **do the papers keep re-testing the same material in the
high-mark questions?**

Answer: yes — in three subjects. Elsewhere, much less than the coaching-industry
folklore suggests.

---

## The repetition index

Share of marks in **≥ 4-mark questions** sitting on a phrase that recurs in **≥ 3 of
the 5 exam years**:

| Subject | Papers | Questions | High-mark Qs | Repetition index |
|---|---:|---:|---:|---:|
| Accountancy | 50 | 1,020 | 109 | **49%** |
| Physics | 64 | 1,266 | 120 | **44%** |
| Economics | 61 | 1,269 | 173 | **38%** |
| Mathematics | 62 | 1,072 | 90 | 22% |
| Business Studies | 54 | 1,035 | 119 | 16% |
| History | 67 | 1,569 | 167 | 16% |
| Geography | 60 | 1,036 | 229 | 14% |
| Political Science | 60 | 989 | 200 | 7% |
| Chemistry | 72 | 1,384 | 133 | 5% |
| Biology | 62 | 1,373 | 169 | 5% |
| English Core | 72 | 757 | 259 | 0% |

**This measures lexical repetition, not conceptual repetition.** Chemistry and Biology
score 5% because their content words vary in wording between questions, not because
the board roams freely there. English Core scores 0% correctly — its long questions
quote unseen passages, which by design never repeat.

Only two content topics in the entire corpus recur at high marks in **4 of 5 years**:
Physics's `electric field` and `magnetic field`.

Full detail: [analysis/topic_recurrence.md](analysis/topic_recurrence.md).

## Two paper architectures

Skill subjects set 24–25 questions and require only 17 — choice everywhere. Academic
subjects are "all compulsory, no overall choice". Full breakdown, including the shared
Employability Skills block worth 10 of 50–60 marks in *every* skill paper:
[analysis/paper_structure.md](analysis/paper_structure.md).

## Three traps worth knowing if you parse these papers yourself

1. **`pdftotext` duplicates content.** CBSE reprints each question's options on the
   facing page. Dedupe at *page* level — text-level dedupe silently eats legitimately
   repeated Assertion–Reason option blocks.
2. **Hindi-medium papers extract as mojibake** — `moozmb ama omo amoj`. The embedded
   Devanagari fonts map onto Latin code points, so a Devanagari-codepoint filter does
   **not** catch it. Gate on English function words instead. Only 54% of parsed
   questions survive this.
3. **Sets within one sitting are ~75% the same paper.** Counting *papers* manufactures
   recurrence. Count distinct exam years. An early version of this analysis
   "discovered" a recurring English Core topic that was one year's comprehension
   passage counted three times.

## Reproducing it

The question papers are © CBSE. They are published free by the board; this repository
carries the extracted text under `corpus/` for research use, and `sources/` has every
original URL so anything here can be verified against the source:

```bash
# 1. fetch the corpus (~6 GB; needs a browser UA — cbse.gov.in 403s otherwise)
while read u; do curl -sS -A "Mozilla/5.0" -O "$u"; done < sources/SOURCE_URLS_past_papers.txt

# 2. parse to a DuckDB question bank
python3 scripts/build_bank.py       # the 32 hand-verified papers
python3 scripts/topics2.py          # parse the full archive, mine recurring phrases
python3 scripts/final_report.py     # split content topics from stem formulas

# 3. optional: OCR the ~25% of papers that are image-only scans
swiftc -O scripts/ocr.swift -o ocrpdf && python3 scripts/run_ocr.py
```

| Script | Does |
|---|---|
| `parse_generic.py` | PDF → questions; page-level reprint dedupe, option/marks extraction |
| `build_bank.py` + `marks_map.py` | the 32-paper bank, marks taken from each paper's own General Instructions and checksummed against its stated maximum |
| `topics2.py` | English gate, subject canonicalisation, n-gram topic mining by exam year |
| `final_report.py` | separates content topics from reused stem formulas |
| `pdf2md.py` | PDF → Markdown with SHA-256 provenance front-matter |
| `ocr.swift` | macOS Vision OCR for scanned papers, two-column reading order |

## Data published here

**The full corpus is included** — `corpus/markdown/` holds every paper as Markdown
(2,270 files, ~69 MB) with SHA-256 provenance front-matter, plus the parsed question
tables. The PDFs themselves are not mirrored; each `.md` records the hash and source
URL of the PDF it came from.

- `corpus/markdown/past_papers/<year>/<Subject>/*.md` — 1,955 Class XII board papers, 2022–2026, main + compartment
- `corpus/markdown_class_X/` — 1,194 **Class X** board papers, 2022–2026, main + compartment
- `corpus/markdown_sqp_archive/` — 2,945 documents from the sample-paper archive, sessions **2015-16 → 2024-25**, of which **1,892 are marking schemes** (answer keys)
- `corpus/markdown/sqp_ms/`, `corpus/markdown/skill_sqp_ms/` — 2025-26 sample papers and marking schemes
- `corpus/markdown/question_banks/` — the 12 official CBSE Question Banks
- `corpus/past_paper_questions.csv` — 30,734 parsed questions with `is_english`, marks, type
- `corpus/questions.csv` — the 960 questions from the 32 hand-verified papers
- `corpus/OCR_MANIFEST.json` — 572 scanned papers recovered by OCR (5.34M characters)

573 of the papers were image-only scans; macOS Vision OCR recovered 523 of them to
usable text. 49 remain thin — they are Hindi-medium, and Vision has no Devanagari model.

Derived aggregates:

- `data/subject_repetition.csv` — the index table above
- `data/recurring_topics.csv` — mined topic phrases and stem formulas, with year lists and marks
- `data/question_type_mix.csv` — question-type counts per subject
- `data/paper_structures.csv` — per-paper section structure and marks reconciliation
- `data/SCHEMA.md` — the local question-bank schema

## Caveats

- Marks in the full archive are regex-parsed and approximate. Only the 32-paper
  `questions` table has marks verified against each paper's stated maximum (all 32
  reconcile exactly).
- Topics are **mined, not hand-listed** — 2–4 word n-grams recurring across ≥3 exam
  years — so the conclusion isn't smuggled in via a curated lexicon. The cost is that
  generic phrasing sometimes surfaces; `final_report.py` separates those into a
  "stem formula" bucket.
- macOS Vision has no Devanagari model, so OCR recovers the English column of bilingual
  papers and not the Hindi one.

## Licence

Code: MIT. Analysis text: CC BY 4.0. The question papers under `corpus/` remain the
intellectual property of the Central Board of Secondary Education and are reproduced
here for research and educational use; CBSE publishes them free of charge at the URLs
in `sources/`. If CBSE objects, the corpus directory will be removed.
