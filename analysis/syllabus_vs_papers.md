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
> Question→unit assignment is **47–62% accurate**, measured against a gold set (below).
> Every "actual" share therefore carries roughly **±10 percentage points** of
> uncertainty. Gaps smaller than that are not evidence of anything.
>
> | Gap size | Verdict |
> |---|---|
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
| Biology | **embedding** | 57% | 57% | **32%** |

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

## Biology — 57% mapped, embedding method

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
