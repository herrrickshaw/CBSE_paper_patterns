# Do CBSE Class-12 papers re-test the same topics?

Corpus: **1,955 question papers** downloaded from `cbse.gov.in/cbsenew/question-paper.html`
— every Class-XII subject, 2022–2026, main sittings *and* compartment (COMPTT) sittings.
**30,734 questions** parsed; **16,633** are usable English-medium text.

The question is whether the high-mark half of the paper keeps returning to the same
material. Short answer: **it depends enormously on the subject, and the split is not
where you'd expect** — it tracks how formulaic the subject's questions are, not how
big its syllabus is.

---

## 1. The repetition index

For each subject: take every question worth **≥ 4 marks**, mine 2–4 word phrases that
appear in **≥ 3 of the 5 exam years**, and measure the share of high-mark *marks* that
sit on one of those recurring phrases.

| Subject | Papers | Questions | High-mark Qs | **Repetition index** |
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

**Read this as lexical repetition, not conceptual repetition.** The index measures
repeated *wording*. Chemistry and Biology score 5% not because the board roams freely
but because their content words are compound names that vary between questions
(`Calculate emf of the following cell…` vs `Consider the following standard electrode
potential values…` are the same topic in different words). Accountancy scores 49%
because its questions are near-templates. English Core scores 0% correctly — its
long questions quote unseen passages, which by design never repeat.

---

## 2. What actually recurs, at high marks

### Accountancy — the most repetitive paper in the corpus
Almost half the high-mark marks sit on one of two machines:

| Recurs in | Papers | Marks | Topic |
|---|---:|---:|---|
| 2023, 2025, 2026 | 14 | 139 | **partners in a firm** — admission/retirement of a partner |
| 2024, 2025, 2026 | 20 | 139 | **balance sheet** — incl. Common Size Balance Sheet |
| 2023, 2025, 2026 | 13 | 121 | **firm sharing profits** — profit-sharing ratio changes |
| 2024, 2025, 2026 | 9 | 57 | **cash flow from investing activities** |
| 2022, 2025, 2026 | 7 | 41 | **dissolution of the firm** |

The partnership cycle — admission, retirement, dissolution, goodwill, sacrificing/gaining
ratio — plus cash-flow and comparative statements *is* the high-mark paper, year after year.

### Physics — the two fields, every single year
| Recurs in | Papers | Marks | Topic |
|---|---:|---:|---|
| 2023, 2024, 2025, 2026 | 14 | 84 | **electric field** |
| 2023, 2024, 2025, 2026 | 11 | 73 | **magnetic field** |
| 2024, 2025, 2026 | 10 | 55 | **parallel plate capacitor** |
| 2024, 2025, 2026 | 8 | 54 | **refractive index** |
| 2024, 2025, 2026 | 6 | 32 | **uniform magnetic field**, charged particle motion |

Electric field and magnetic field are the only content topics in the whole corpus that
appear at high marks in **4 of 5 years**.

### Economics
`aggregate demand` (4 years), `hypothetical economy` numericals, `commercial banks` /
`Reserve Bank of India`, `gross value added`. The APS/APC-style "for a hypothetical
economy, it is known that…" numerical is a fixture: 14 papers, 133 marks.

### History — narrow and predictable at 8 marks
`Vijayanagara Empire` (11 papers, 88 marks), `Quit India Movement` (48), `Salt
Satyagraha` (40), `Bombay Deccan riots` (32). The 8-mark long answers circle a small
set of set-pieces even though the index looks low at 16%.

### Business Studies
`functions of management` — directing, planning — 16 papers and 80 marks in three
consecutive years. `importance of planning` recurs almost verbatim.

### Geography
`demographic transition` (93 marks), `international trade`, uneven population distribution.

---

## 3. Recurring stem formulas (separate from topics)

Distinct from content: the *wording* the board reuses to ask. These are phrases made
entirely of generic academic verbs, so they mark question templates rather than syllabus:

| Subject | Years | Formula |
|---|---|---|
| Physics | 3 | **derive an expression / obtain an expression for…** |
| Economics | 3 | **give valid arguments in support of your answer** |
| Business Studies, Geography | 3 | **factors affecting / influencing…** |
| Geography | 3 | **main features / main characteristics of…** |
| Political Science | 3 | **steps taken by…** |
| Mathematics | 3 | **find the general solution / find the probability** |

Combined with the objective-question templates from the structural analysis
(Assertion–Reason, Statement I/II, Match List-I with List-II, chronological ordering),
these are trainable independently of any content.

---

## 4. Method, and what would undermine it

- Topics are **mined, not hand-listed** — 2–4 word n-grams recurring across ≥3 distinct
  exam years, with exam boilerplate stripped from phrase edges. No curated topic list,
  so the conclusion isn't smuggled in by the lexicon.
- **Recurrence is counted in exam years, not papers.** Sets within one sitting are ~75%
  the same paper, so paper counts manufacture recurrence — an early version of this
  analysis "found" an English Core topic that was one year's comprehension passage
  counted three times. Paper counts appear in the tables above for texture only; the
  year count is the load-bearing number.
- **Hindi-medium papers extract as mojibake** (`moozmb ama omo amoj`) because the
  embedded Devanagari fonts map onto Latin code points — a Devanagari-codepoint filter
  does *not* catch it. Questions are gated on English function words instead. This is
  why only 54% of parsed questions are usable, and why some example snippets in the
  underlying data still show Hindi: bilingual papers interleave both columns.
- **Marks for these papers are parsed heuristically** (`marks_source='parsed'`), unlike
  the 32 papers in `questions`, whose marks come from each paper's own General
  Instructions and reconcile exactly to the stated maximum. Treat the index as
  ±few points, not exact.
- Questions longer than 60 words are excluded so quoted passages don't masquerade as topics.

---

## 5. Where it lives

`~/Downloads/cbse_question_bank/cbse_question_bank.duckdb`

| Table | Rows | Contents |
|---|---:|---|
| `questions` | 960 | the original 32 papers, marks verified against each paper's maximum |
| `past_paper_questions` | 30,734 | full 2022–2026 archive, all subjects, `is_english` flag |
| `recurring_topics` | 56 | mined topics + stem formulas, with year lists and marks |
| `subject_repetition` | 11 | the index table above |
| `papers` | 32 | per-paper structure and reconciliation |

```bash
duckdb ~/Downloads/cbse_question_bank/cbse_question_bank.duckdb -c "SELECT subject, phrase, years, marks FROM recurring_topics WHERE kind='content_topic' ORDER BY marks DESC LIMIT 20"
```
