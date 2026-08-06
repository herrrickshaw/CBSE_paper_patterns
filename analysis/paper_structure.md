# CBSE Class 12 question papers — structural analysis

Corpus: 32 papers in `~/Downloads` (8 skill subjects at top level + `History/`, `Economics/`,
`Accountancy/`, `Political_Science/`). Session referenced in the papers: **2024–25**.
Text extracted with `pdftotext -layout`; both language columns present, English side analysed.

---

## 1. There are two paper architectures, not one

Every paper in the corpus follows one of two designs. Which one you get depends on whether the
subject is a **Skill Education** subject or an **academic** subject — and the two designs have
opposite philosophies about choice.

### Architecture A — Skill subjects: *choice everywhere*

| Subject | Code | Marks | Time | Questions set → to attempt |
|---|---|---|---|---|
| Artificial Intelligence | 367/S | 50 | 2 h | (5 + 16) = 21 → (5 + 10) = **15** |
| Information Technology | 326/S | 60 | 3 h | (6 + 18) = 24 → (6 + 11) = **17** |
| Typography & Computer Applications | 341/S | 60 | 3 h | (6 + 18) = 24 → **17** |
| Financial Markets Management | 329 | 60 | 3 h | (6 + 18) = 24 → **17** |
| Taxation | 346 | 60 | 3 h | (6 + 18) = 24 → **17** |
| Web Applications | 327 | 60 | 3 h | (6 + 19) = 25 → **17** |

Fixed shape (60-mark version): **Section A objective 30 marks in 6 questions**, each question a
bundle of 6–7 parts of which you answer 4–6; **Section B subjective 30 marks in 18–19 questions,
answer 11**. No negative marking. Sections must be attempted in order.

Section B always climbs the same ladder, with the word limit *printed in the instruction line*:

```
3 × 2 = 6   Employability Skills   20–30 words
3 × 2 = 6   subject                20–30 words
2 × 3 = 6   subject                30–50 words
3 × 4 = 12  subject                50–80 words
```

AI is the odd one out only in size (50 marks / 2 hours, Sec A 24 + Sec B 26) — the grammar is identical.

**Employability Skills is a shared 17–20% of every skill paper.** Q1 of Section A (any 4 of 6 × 1 = 4)
plus the first Section B block (any 3 of 5 × 2 = 6) = 10 marks out of 50/60, and it is the *same
five-unit syllabus in all six subjects*: communication (sentence types, active listening, barriers),
self-management (Five Factor Model / FFM, motivation intrinsic vs extrinsic, personality disorders,
self-awareness), ICT (spreadsheet cell/AutoSum/password-protect, presentation Ctrl+M), entrepreneurship
(risk-taking, entrepreneur vs manager/wage-employed), green skills (green jobs, green-collar workers,
biofuel policy, waste segregation). The same items recur near-verbatim across subjects — e.g. "which is
*not* a stage of active listening" appears in both Taxation and Web Applications; "Ctrl + M adds a
slide" appears in both AI and Typography. **Learn this block once and it pays across all six papers.**

Engineering Graphics (68/S, 70 marks) is a third thing: a drawing-sheet paper — Section A 14 MCQs +
2 case-paragraph blocks of 4 MCQs, then Section B/C are drawing questions (sleeve-and-cotter joint,
isometric projection, BSW thread profile) worth 13–27 marks each, first-angle projection, SP:46-2003.

### Architecture B — Academic subjects: *no overall choice*

Wording is identical across all of them: *"All questions are compulsory… There is no overall choice.
However, an internal choice has been provided in [some] questions."*

| Subject | Code | Marks | Qs | Section ladder |
|---|---|---|---|---|
| History | 61/S | 80 | 34 | A 21×1 MCQ · B 6×3 (60–80 w) · C 3×8 (300–350 w) · D 3×4 source · E map 5 |
| Political Science | 59/n | 80 | 30 | A 12×1 · B 6×2 (50–60 w) · C 5×4 (100–120 w) · D 3×4 passage/cartoon/map · E 4×6 (170–180 w) |
| Economics | 58/S | 80 | 34 | 20×1 · 4×3 (60–80 w) · 6×4 (80–100 w) · 4×6 (100–150 w), split Macro / Indian Economic Development |
| Accountancy | 67/S | 80 | 34 | Part A compulsory (Partnership + Companies); Part B **pick one**: Analysis of Financial Statements *or* Computerised Accounting. 1/3/4/6 ladder |
| Computer Science | 91/S | 70 | 37 | A 21×1 · B 7×2 · C 3×3 · D 4×4 · E 2×5 — Python only, MCQ answers must be written out in full |

Accountancy is the only academic paper with a genuine either/or *option* (Part B), and Economics the
only one split by content domain rather than by mark weight.

---

## 2. The question grammar is shared across every subject

A small set of question templates is reused verbatim — same stem wording, same four options —
across History, Political Science, Economics, Accountancy, Computer Science and FMM:

- **Assertion (A) / Reason (R)** with the canonical four options ("both true and R is the correct
  explanation…"). Note the option *order is not stable*: PolSci 59/1/1 Q5 puts "A false, R true" at
  (C), everyone else puts it at (D). Read the options, don't answer from muscle memory.
- **Statement-I / Statement-II** truth-table block (Economics, PolSci, AI, Web Applications).
- **Match List-I with List-II** → a-iv, b-iii, c-i, d-ii style codes (History coins/rulers, Engineering
  Graphics flange-joint parts, PolSci treaties).
- **Chronological ordering** of four events (History Satyagrahas and Santhal sequence, PolSci Lok Sabha
  events).
- **"Which of the following statements are true — I/II/III/IV"** with paired options.
- **Source/case-based** passage with `1 + 1 + 2 = 4` sub-parts (History Section D, PolSci Section D,
  Economics Q16/Q34, Engineering Graphics case paragraphs).
- **Named-scenario framing** for application questions — "Suman is an intern…", "Keshav is the IT
  Head…", "Rohit visited a shopping website…", "Gurmeet turned on her computer…". The name is noise;
  the question underneath is a standard one.
- **Visually-impaired substitute**: every academic paper carries a parallel non-visual question in
  lieu of each map/image/cartoon item, printed inline with a "for Visually Impaired Candidates only"
  note. Also present in the skill papers wherever a figure appears.

---

## 3. Set variants: what actually changes

This is the practically useful finding.

- **Within a series** (e.g. `61/S/1`, `61/S/2`, `61/S/3`), the three sets are **largely the same
  paper**: 25 of 34 question stems in History are byte-identical between S-1 and S-2; Economics 27 of
  34; Political Science 31 of 39. Word-set overlap ≈ 0.92. Only the remaining ~20–25% are swapped,
  and the swaps are same-topic substitutions (Chola/Bhakti ↔ another 3-marker).
- **Across series** (`59/1/1` vs `59/2/1` vs … `59/5/1` in Political Science) the papers are
  **genuinely different** — word-set overlap drops to 0.30–0.35. Five series × three sets = 15
  distinct-enough Political Science papers, which is the largest single-subject pool here.
- So: for revision, treat S-1/S-2/S-3 as **one** paper with variants, and treat 59/1…59/5 as **five**.
- Series labels (`WXYZ/S`, `SR3PQ`, `S3RQP`, `SQRP1`) and `SET~1`/`SET~4` are anti-copying scramblers,
  not difficulty tiers.
- Codes carrying `/S` (61/S, 58/S, 67/S, 91/S, 68/S, 326/S, 341/S, 367/S) are one exam series and the
  plain-numbered ones (327, 329, 346, 59/n) another. CBSE conventionally uses `/S` for the
  supplementary/compartment series — that reading is consistent with the corpus but is not stated
  anywhere in the papers themselves.

---

## 4. Content notes worth carrying forward

**Artificial Intelligence (367/S)** — contains no programming at all. The whole paper is the AI project
lifecycle (scoping → data → feature definition → build → test → deploy), data storytelling (three key
elements, narrative-with-conflict), Design Thinking's five stages, and evaluation vocabulary
(train-test split, cross-validation, RMSE, classification vs regression loss, data validation). Tools
named: TensorFlow as the open framework, R/Anaconda/BigML as distractors.

**Web Applications (327)** — the most current paper in the set. JavaScript (array methods, `slice`,
`Math.ceil/pow/random`, event handlers, `parseInt`), plus **Canva AI features by name** (Magic Media,
Magic Edit, Magic Animate, Beat Sync), Adobe Express (ex-Adobe Spark), IoT / edge computing / ML /
cloud, and Indian cyber-law (IT Rules 2011 on sensitive personal data, cyber-stalking, ethical
hacking, plagiarism taxonomy: direct / paraphrasing / mosaic).

**Financial Markets Management (329)** — NSE market microstructure end to end: NEAT (order-driven,
price-then-time priority, 5-minute inactivity logout, corporate-manager/branch-manager/dealer
hierarchy, market watch / message / auction inquiry windows), NSCCL settlement and bad deliveries
(report within 2 days), UCC, contract notes, ISIN construction, margins, credit rating agencies, then
derivatives (cost of carry = financing cost − dividends, forward counterparty risk, option premium as
the buyer's maximum loss, CME currency futures 1972, NSE USD-INR futures 2008). Directly adjacent to
the put-call-parity and screening work in this repo.

**Taxation (346)** — AY-specific numbers that date the paper: 87A rebate ₹12,500 at ₹5 lakh total
income, health & education cess 4%, 80D HUF cap, 80EE house cost ≤ ₹50 lakh, 194B lottery TDS 30%,
112A LTCG 10% above ₹1 lakh, super-senior at 80, advance tax in 4 instalments, GSTIN 15 digits, CGST
max 20%, Kelkar task force. Numerical questions are small computations (80D aggregation, GST split on
a 20%-margin sale, advance-tax schedule), not multi-page problems.

**Computer Science (91/S)** — Python + MySQL + networking in fixed proportions: string/list/dict/tuple
output-prediction MCQs, one error-correction question ("underline all corrections"), one stack
implementation (push/pop/isEmpty), CSV and binary file handling, SQL query writing *and* query-output
reading, one Python-MySQL connectivity function, and one 5-mark network case study (block layout,
server placement, cable layout, repeater/gateway choice).

**History / Political Science / Economics** — standard NCERT coverage. Economics is dated by its
sources: a 10 August 2023 RBI Governor quote on commercial borrowings and the PM-PRANAM scheme.
Political Science Section E is entirely predictable in shape: UN organs/agencies, USSR
disintegration/shock therapy, India's foreign policy, coalition era post-1989.

**Accountancy (67/S)** — Part A is the classic partnership cycle (admission, retirement, dissolution,
goodwill by super-profit/capitalisation, sacrificing and gaining ratios, guarantee of profit) plus
company accounts (share forfeiture and reissue, debenture issue at premium/discount redeemable at
premium, pro-rata allotment). Almost every 1-marker is a small computation with four numeric options,
not a definition.

---

## 5. Practical read

1. **Skill-subject candidates get to discard a third of the paper.** 24 of 25 questions set vs 17 to
   answer means the winning tactic is triage, not coverage — and the 10 Employability Skills marks are
   the cheapest in the paper.
2. **Academic candidates get no such escape** — only internal choice inside a question. Coverage has
   to be complete.
3. **Word limits are marks-coded and printed**: 2 mk→20–30 w, 3 mk→30–50/60–80 w, 4 mk→50–80/100–120 w,
   6 mk→100–180 w, 8 mk→300–350 w. Length is part of the rubric, not a suggestion.
4. **The template blocks (A/R, Statement I-II, matching, ordering) are worth ~15–25% of every academic
   paper** and are trainable independently of content.
