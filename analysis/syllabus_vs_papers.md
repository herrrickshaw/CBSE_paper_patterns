# Does the paper follow its own syllabus blueprint?

CBSE publishes, per subject, a Class-XII **unit-wise marks weightage** in the curriculum
document. That is the board's own taxonomy — not mined phrases — so it is the right
yardstick for asking whether the question papers distribute marks the way the syllabus
says they will.

Method: extract the Class-XII unit table from each curriculum PDF, assign every parsed
English question to a unit, sum the marks per unit across 2022–2026, and compare that
share against the declared share.

> ## ⚠️ Read this before any number below
>
> Unit-level shares are **highly sensitive to how the unit description is built**.
> The same subject, same questions, same model, produces opposite headlines depending
> on where the description text is taken from:
>
> | Subject | Unit-description source | Accuracy | Headline gap |
> |---|---|---:|---|
> | Accountancy | enriched keyword (no NCERT) | 59.0% | Companies **+8** |
> | Accountancy | curriculum paragraph, embedded | 47.1% | Partnership +25 |
> | Accountancy | NCERT chapter head (with heading) | **67.1%** | Companies **+20** |
> | Accountancy | NCERT chapter head (heading stripped) | 62.5% | Companies **+19** |
> | Accountancy | NCERT chapter, windowed sample | 28.6% | Partnership +34 |
> | Biology | keyword | 62%, 15% mapped | Human Welfare +48 |
> | Biology | curriculum paragraph, embedded | 56.7% | Human Welfare −15 |
> | Biology | NCERT chapters, from PDF text | **78.4%** | none clear the bar |
> | Biology | NCERT chapters, from markdown | 49–55% | Ecology +17 |
>
> The pipeline is deterministic — three identical runs give identical numbers — so this
> is sensitivity to preprocessing choices, not randomness. But it means **no unit-level
> gap should be believed unless it survives across the higher-accuracy configurations.**
>
> Exactly one does: **Accountancy's Accounting for Companies is over-tested**, at +20
> and +19 in the two most accurate configurations (67.1% and 62.5%). The keyword method
> agrees on direction (+8) at 59%.
>
> Everything else in this document is **not established**, including findings reported
> in earlier revisions: Psychology's "Psychological Disorders +15" falls to +5–8 under
> NCERT chapter descriptions, and Biology has now been read five ways with four
> different headlines.

---|---|
> | ≥ ±14 pts | probably real |
> | ±8 to ±13 pts | suggestive, not established |
> | < ±8 pts | **indistinguishable from noise** |

---

## How questions are assigned to units, and how well

Two methods, and **neither wins outright** — the right one depends on whether the
subject's unit names are distinctive:

| Subject | Method | Coverage | Accuracy | Correctly placed |
|---|---|---:|---:|---:|
| Accountancy | enriched keyword | 87% | 59% | **51%** |
| Accountancy | embedding | 90% | 47% | 42% |
| Biology | enriched keyword | 15% | 62% | 9% |
| Biology | embedding (curriculum para) | 57% | 57% | 32% |
| Biology | **embedding (NCERT chapters)** | 70% | **78%** | **55%** |

Embeddings (`all-MiniLM-L6-v2`, each unit described by its name plus the syllabus prose
beneath it) are decisively better where unit names are generic single words — Biology's
"Reproduction", "Ecology and Environment" — placing **3.5× more questions correctly**
despite slightly lower per-item accuracy. Hand-enriched keyword sets stay ahead where
the domain vocabulary is distinctive and curated, as in Accountancy.

**Accuracy is measured against a gold set** of questions containing a term that belongs
to exactly one unit by definition (`debenture` → Companies, `embryo sac` → Reproduction):
395 gold questions for Accountancy, 171 for Biology. Every word appearing in a gold
pattern is **banned from the keyword features** before scoring — without that ban the
keyword method scores an inflated 92.4%, because it is being tested on the very terms it
was built from.

---

## Accountancy — 87% mapped, keyword method

| Unit | Declared | Actual | Gap | Verdict |
|---|---:|---:|---:|---|
| Accounting for Partnership Firms | 45% | 49% | +4 | noise |
| Accounting for Companies | 30% | 38% | +8 | suggestive |
| Analysis of Financial Statements | 15% | 7% | −8 | suggestive |
| Cash Flow Statement | 10% | 6% | −4 | noise |

Nothing here clears the ±14 bar. The suggestion is that the paper leans heavier on
company accounts and lighter on Part B, but at 59% assignment accuracy that is not
established. The embedding method, on the same data, puts Partnership at 70% and
Companies at 10% — a disagreement far larger than either gap, which is itself the
clearest evidence that this subject's numbers are not yet settled.

A structural caveat compounds it: Part B is an *either/or* — candidates choose Analysis
of Financial Statements **or** Computerised Accounting — so its questions split across
two alternative tracks while the declared weightage counts one.

## Economics — 83% mapped, embedding method

| Unit | Declared | Actual | Gap | Verdict |
|---|---:|---:|---:|---|
| Current Challenges facing Indian Economy | 33% | 27% | −6 | noise |
| Determination of Income and Employment | 20% | 30% | +10 | suggestive |
| National Income and Related Aggregates | 17% | 9% | −8 | suggestive |
| Balance of Payments | 10% | 16% | +6 | noise |
| Money and Banking | 10% | 11% | +1 | noise |
| Government Budget and the Economy | 10% | 7% | −3 | noise |

The keyword run on the same subject gave Current Challenges −14 and Government Budget
+9 — i.e. it disagreed on both direction and magnitude for Government Budget. Treat
**Determination of Income and Employment being over-tested** as the one durable signal;
it is the only unit both methods place above its declared weight.

## Psychology — 80% mapped, embedding method

| Unit | Declared | Actual | Gap | Verdict |
|---|---:|---:|---:|---|
| IV Psychological Disorders | 17% | 32% | **+15** | probably real |
| II Self and Personality | 19% | 7% | **−12** | suggestive |
| V Therapeutic Approaches | 13% | 4% | −9 | suggestive |
| VI Attitude and Social Cognition | 11% | 15% | +3 | noise |
| I Variations in Psychological Attributes | 19% | 21% | +2 | noise |
| III Meeting Life Challenges | 13% | 13% | 0 | noise |
| VII Social Influence and Group Processes | 9% | 8% | −1 | noise |

**Psychological Disorders at roughly twice its declared weight** is the single largest
gap in the corpus that clears the noise floor. Note this reverses the earlier
keyword-based reading, which had Psychology as the most blueprint-faithful subject with
every unit inside ±4 — that reading came from mapping only 41% of its questions.

## Biology — 70% mapped, NCERT chapter descriptions

**Assignment accuracy 78.4%** — the best in the corpus, up from 56.7% with a curriculum
paragraph. Uncertainty band ≈ ±6pp.

| Unit | Declared | Actual | Gap | Verdict |
|---|---:|---:|---:|---|
| VII Genetics and Evolution | 27% | 18% | -8 | suggestive |
| VI Reproduction | 21% | 31% | +10 | suggestive |
| VIII Biology and Human Welfare | 16% | 11% | -5 | noise |
| IX Biotechnology and its Applications | 16% | 21% | +5 | noise |
| X Ecology and Environment | 13% | 14% | +1 | noise |
| Identification/Familiarity with the apparatus | 7% | 3% | -4 | noise |

Nothing clears the bar. Biology is **broadly blueprint-faithful**, with a hint that
Reproduction is over-tested and Genetics under-tested. This is the third and final
reading of this subject; the two before it were both artifacts:

| Reading | Method | Headline | Why it was wrong |
|---|---|---|---|
| 1st | keyword | Human Welfare **+48** | only 15% mapped; `disease`/`health`/`drug` absorbed everything |
| 2nd | NCERT, shared chapters | Human Welfare **−15** | Human Welfare and Biotechnology were given the *same three chapters*, so Biotech absorbed every question |
| 3rd | NCERT, exclusive chapters | Human Welfare **−5, noise** | each chapter assigned to one unit, no unit left empty |

## How NCERT chapter text was attached to units

286 Class-XII chapter PDFs from `ncert.nic.in` (~5.7 GB, book codes and chapter counts
read out of the inline JavaScript that builds the dropdowns on `textbook.php`). Chapter
titles are useless for this — `pdftotext` returns body prose like *"Y ou have learnt
about..."* — so chapters are attached to units by embedding the **chapter text** and
assigning **exclusively**: highest similarity first, each chapter used once, and any
unit left empty takes its best unclaimed chapter. That last clause is what fixed the
2nd reading above.

The resulting assignment is verifiably correct against the NCERT contents page:
Reproduction ← ch1–3, Genetics and Evolution ← ch4–6, Biology and Human Welfare ←
ch8 *Microbes in Human Welfare*, Ecology ← ch11–13.

**It does not help every subject.** Accountancy went 47.1% → 45.1% with NCERT text;
its enriched keyword sets remain the best method there at 59%. Chapter text helps where
units are semantically broad (Biology) and not where they turn on fine-grained
vocabulary the model doesn't separate (`debenture` vs `goodwill`).

## Superseded: Biology — 57% mapped, embedding method

| Unit | Declared | Actual | Gap | Verdict |
|---|---:|---:|---:|---|
| VII Genetics and Evolution | 27% | 19% | −8 | suggestive |
| VI Reproduction | 21% | 20% | −1 | noise |
| VIII Biology and Human Welfare | 16% | 18% | +2 | noise |
| IX Biotechnology and its Applications | 16% | 8% | −8 | suggestive |
| X Ecology and Environment | 13% | 20% | +6 | noise |

Nothing clears the bar; Biology looks broadly blueprint-faithful. This supersedes the
earlier keyword result, which showed "Biology and Human Welfare" at **+48** — an
artifact of mapping only 15% of questions with keywords (`disease`, `health`, `drug`)
generic enough to absorb questions from every other unit.

---

## Limits

- **Unit tables extract cleanly for only 5 of 12 subjects.** Curricula cover Classes XI
  and XII in one document with no consistent unit prefix and differing layouts per
  subject. Un-split extraction mixes Class XI units into the Class XII denominator and
  distorts every share — Accountancy's table is hand-split for that reason.
- **Unit descriptions come from a paragraph of curriculum prose.** An earlier version
  silently sourced them from the course-structure *table* instead ("Ecology and
  Environment" described as `10 Total 70 Unit-VI Reproduction`), which is what put
  Accountancy's Analysis of Financial Statements at an impossible 0%.
- **The obvious improvement is NCERT chapter text.** The curriculum gives a paragraph per
  unit; NCERT gives a whole chapter. That should lift both coverage and accuracy well
  past 60% and shrink the uncertainty band enough to make the ±8 gaps decidable.
- Marks in the archive are regex-parsed and approximate; only the 32-paper `questions`
  table has marks verified against each paper's stated maximum.

## Withdrawn

An earlier pass reported an **answer-letter bias** in the marking schemes (A 39%,
B 25%, C 22%, D 14%, chi-square 232). **Withdrawn.** The extraction cannot distinguish a
genuine MCQ answer key from the part labels `(a)`, `(b)` used in descriptive answers:
58% of question slots yield only A and/or B, and the same skew appears past Q35 where no
MCQs exist. Gating on questions with four detected options reduced the sample to n=3.
There is no measurement here, in either direction.
