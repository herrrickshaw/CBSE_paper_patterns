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
> Every unit share depends on a question→unit assignment that is **54–78% accurate**,
> measured against gold sets of questions containing a term belonging to exactly one
> unit by definition. Gold sets: Accountancy 395, Economics 248, Biology 171 questions.
>
> **Psychology cannot be validated at all** — the corpus holds only 107 Psychology
> questions and yields 22 gold, 1–5 per unit. Its numbers are therefore withdrawn, not
> reported. The "Psychological Disorders +15" headline from an earlier revision was
> never validatable.
>
> A gap is only believed here if it **survives across configurations**, because the same
> subject produces different headlines depending on how the unit description is built.

---

## The result, one method, three validated subjects

Assignment by embedding the **unit name alone** — which turns out to match or beat every
richer description tried (see the sensitivity table below):

| Subject | Gold | Accuracy | Largest gap | Verdict |
|---|---:|---:|---|---|
| Biology | 171 | **77.8%** | Reproduction +17 | contested — see below |
| Economics | 248 | **68.5%** | ±2.3pp | **blueprint-faithful** |
| Accountancy | 395 | 54.4% | Companies +12 | **over-tested, direction robust** |

### Economics — follows its blueprint almost exactly

| Unit | Declared | Actual | Gap |
|---|---:|---:|---:|
| Current Challenges facing Indian Economy | 33% | 34% | +0.7 |
| Determination of Income and Employment | 20% | 20% | −0.4 |
| National Income and Related Aggregates | 17% | 18% | +1.3 |
| Money and Banking | 10% | 10% | +0.2 |
| Government Budget and the Economy | 10% | 11% | +0.5 |
| Balance of Payments | 10% | 8% | −2.3 |

At the highest accuracy available for this subject, **no unit deviates by more than
2.3 points**. This supersedes every earlier Economics reading in this document
(Current Challenges −14, Government Budget +9, Determination +12/+14), all of which came
from lower-accuracy configurations.

### Accountancy — Companies over-tested, magnitude uncertain

All four configurations agree on the direction, which is what makes this the one
durable finding in the analysis:

| Configuration | Accuracy | Companies gap |
|---|---:|---:|
| NCERT chapter head (with heading) | 67.1% | +20 |
| NCERT chapter head (heading stripped) | 62.5% | +19 |
| enriched keyword | 59.0% | +8 |
| unit name only | 54.4% | +12 |

**Accounting for Companies is tested above its declared 30%**, by somewhere between 8
and 20 points. Partnership Firms is correspondingly under-tested. Part B being an
either/or (Analysis of Financial Statements *or* Computerised Accounting) plausibly
explains part of the Part B shortfall.

### Biology — contested

The two most accurate configurations disagree, so nothing is concluded:

| Configuration | Accuracy | Headline |
|---|---:|---|
| NCERT chapters, from PDF text | 78.4% | nothing clears the bar |
| unit name only | 77.8% | Reproduction +17, Human Welfare −14 |

Two runs a whisker apart in accuracy, opposite conclusions. Biology needs a larger gold
set or human labelling to settle.

---

## The NCERT apparatus was mostly unnecessary

286 chapter PDFs were downloaded and mapped to units to build richer descriptions. On
the evidence, **the unit name alone is competitive or better**:

| Subject | name only | best NCERT | best other |
|---|---:|---:|---:|
| Biology | 77.8% | 78.4% | 62% (keyword) |
| Economics | **68.5%** | 54.8% | — |
| Accountancy | 54.4% | **67.1%** | 59.0% (keyword) |

NCERT chapter text helps Accountancy and roughly ties on Biology; it actively hurts
Economics. The lesson is that a short, precise label embeds better than a long passage
whose bulk is worked examples, figure captions and scientist biographies — the same
reason sampling chapter interiors made things worse, not better.

## Sensitivity table (why "survives across configurations" is the rule)

| Subject | Unit-description source | Accuracy | Headline gap |
|---|---|---:|---|
| Accountancy | NCERT chapter head (with heading) | 67.1% | Companies +20 |
| Accountancy | NCERT chapter head (heading stripped) | 62.5% | Companies +19 |
| Accountancy | enriched keyword | 59.0% | Companies +8 |
| Accountancy | unit name only | 54.4% | Companies +12 |
| Accountancy | curriculum paragraph | 47.1% | Partnership +25 |
| Accountancy | NCERT chapter, windowed sample | 28.6% | Partnership +34 |
| Biology | NCERT chapters from PDF | 78.4% | none clear |
| Biology | unit name only | 77.8% | Reproduction +17 |
| Biology | curriculum paragraph | 56.7% | Human Welfare −15 |
| Biology | keyword (15% mapped) | 62% | Human Welfare +48 |
| Economics | unit name only | 68.5% | none clear |
| Economics | NCERT chapters | 54.8% | Determination +14 |

The pipeline is deterministic — three identical runs give identical output — so this is
sensitivity to preprocessing choices, not randomness.

## Withdrawn

An earlier pass reported an **answer-letter bias** in the marking schemes (A 39%,
B 25%, C 22%, D 14%, chi-square 232). **Withdrawn.** The extraction cannot distinguish a
genuine MCQ answer key from the part labels `(a)`, `(b)` used in descriptive answers:
58% of question slots yield only A and/or B, and the same skew appears past Q35 where no
MCQs exist. Gating on questions with four detected options reduced the sample to n=3.
There is no measurement here, in either direction.
