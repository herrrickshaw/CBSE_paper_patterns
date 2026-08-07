# Does the paper follow its own syllabus blueprint?

CBSE publishes, per subject, a Class-XII **unit-wise marks weightage** in the curriculum
document. That is the board's own taxonomy — not mined phrases — so it is the right
yardstick for asking whether the question papers distribute marks the way the syllabus
says they will.

Method: extract the Class-XII unit table from each curriculum PDF, assign every parsed
English question to the unit whose name-derived keywords it best matches, sum the marks
per unit across 2022–2026, and compare that share against the declared share.

**Read the mapped-coverage column first.** A subject whose questions mostly failed to
map cannot support a claim about its weightage, however large the gap looks.

---

## Accountancy — 87% of questions mapped

| Unit | Declared | Actual | Gap |
|---|---:|---:|---:|
| Accounting for Partnership Firms | 45% | 49% | +4 |
| Accounting for Companies | 30% | 38% | **+8** |
| Analysis of Financial Statements | 15% | 7% | **−8** |
| Cash Flow Statement | 10% | 6% | −4 |

The partnership block lands almost exactly on its declared weight. The paper leans
**heavier on company accounts** than the blueprint says, and **lighter on Part B**
(Analysis of Financial Statements + Cash Flow) by a combined 12 points.

One caveat that could explain much of the Part B shortfall: Part B is an *either/or*
— candidates choose Analysis of Financial Statements **or** Computerised Accounting —
so its questions are split across two alternative tracks while the declared weightage
counts one. Treat the −8 as an upper bound on genuine under-testing.

## Economics — 73% mapped

| Unit | Declared | Actual | Gap |
|---|---:|---:|---:|
| Current Challenges facing Indian Economy | 33% | 19% | **−14** |
| Determination of Income and Employment | 20% | 18% | −2 |
| National Income and Related Aggregates | 17% | 21% | +5 |
| Government Budget and the Economy | 10% | 19% | **+9** |
| Money and Banking | 10% | 13% | +3 |
| Balance of Payments | 10% | 10% | 0 |

The two macro-policy units — **Government Budget** and **National Income** — are tested
well above their declared share, and **Current Challenges facing Indian Economy** is
tested at little over half its blueprint weight despite being the single largest unit
on paper. For a candidate, that is the actionable asymmetry in this subject.

## Psychology — 41% mapped

Every unit lands within ±4 points of its declared weight — the most blueprint-faithful
subject measured. Coverage is only 41%, so this is suggestive rather than settled, but
no unit shows the kind of gap Accountancy and Economics do.

## Biology — 15% mapped: NOT RELIABLE

The table shows "Biology and Human Welfare" at +48 points. **Do not believe it.** Only
129 of 873 questions mapped, and that unit's keywords (`disease`, `health`, `drug`,
`immune`) are common enough to absorb questions belonging to other units. This is a
measurement artifact of poor coverage, not a finding about the paper. Biology needs a
proper chapter-level keyword set — most plausibly from the NCERT textbooks — before its
weightage can be assessed.

---

## Limits

- **Unit tables extract cleanly for only 5 of 12 subjects.** Curricula cover Classes XI
  and XII in one document with no consistent unit prefix, and the layouts differ per
  subject. Un-split extraction mixes Class XI units into the Class XII denominator and
  silently distorts every share — Accountancy's table here is hand-split for that reason.
- **Question→unit assignment is keyword overlap**, not semantic. It works where unit
  names are distinctive (Accountancy, Economics) and fails where they are generic
  (Biology). Embedding-based assignment would fix this and is the obvious next step.
- Marks in the archive are regex-parsed and approximate; only the 32-paper `questions`
  table has marks verified against each paper's stated maximum.

## Withdrawn

An earlier pass reported an **answer-letter bias** in the marking schemes (A 39%,
B 25%, C 22%, D 14%, chi-square 232). That is **withdrawn**. The extraction cannot
distinguish a genuine MCQ answer key from the part labels `(a)`, `(b)` used in
descriptive answers: 58% of question slots yield only A and/or B, and the same skew
appears in question bands past Q35 where no MCQs exist. An attempt to gate the sample
on questions with four detected options reduced it to n=3. There is no measurement here,
in either direction.
