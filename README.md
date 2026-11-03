# CBSE paper patterns

Structural and topic-recurrence analysis of CBSE board papers: **1,955 Class XII papers** (2022-2026)
analysed in depth, plus a **6,409-document corpus** that also spans Class X and every sample paper and
marking scheme back to 2015-16, covering **30,734 parsed questions**. It answers one question: do the
papers keep re-testing the same material in the high-mark questions? Outputs are CSV tables under `data/`
and Markdown reports under `analysis/`.

> Status: research-only snapshot. The question papers are (c) CBSE; the repository carries extracted text
> and derived aggregates for research and education. Not advice for exam preparation or prediction.

**Answer:** yes in three subjects (Accountancy, Physics, Economics); elsewhere much less than coaching-industry
folklore suggests. See [How to use this repo with AI](HOW_TO_USE_WITH_AI.md) for a non-programmer route in.

## What it does
- Parses CBSE PDFs into questions with marks, type, section and MCQ options (`scripts/parse_generic.py`).
- Mines 2-4 word recurring phrases across exam years and splits content topics from reused stem formulas.
- Computes a per-subject repetition index (`scripts/final_report.py`).
- Converts PDFs to Markdown with SHA-256 provenance front-matter (`scripts/pdf2md.py`) and OCRs image-only scans.
- Builds a hand-verified 32-paper DuckDB question bank with marks reconciled to each paper's stated maximum.
- Maps questions to NCERT/syllabus units and builds a knowledge graph (`knowledge_graph/`).

## Quick start
```bash
git clone https://github.com/herrrickshaw/CBSE_paper_patterns.git
cd CBSE_paper_patterns
python3 -m venv .venv && source .venv/bin/activate
pip install pytest ruff            # tests only; the analysis scripts need poppler's `pdftotext`
pytest -q
```
Reproducing the headline table needs the source PDFs (not mirrored here); see "Data sources". Then:
```bash
export CBSE_PAPERS_ROOT=~/Downloads/cbse_official/past_papers   # default location
python3 scripts/topics2.py          # parse the archive, mine recurring phrases
python3 scripts/final_report.py     # repetition index + content topics vs stem formulas
```

## The repetition index
Share of marks in **>= 4-mark questions** sitting on a phrase that recurs in **>= 3 of the 5 exam years**:

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

**This measures lexical repetition, not conceptual repetition.** Chemistry and Biology score 5% because their
content words vary in wording between questions. English Core scores 0% correctly: its long questions quote
unseen passages. Only two content topics recur at high marks in **4 of 5 years**: Physics's `electric field`
and `magnetic field`. Detail: [analysis/topic_recurrence.md](analysis/topic_recurrence.md); paper layouts
(skill vs academic, 10 marks of Employability Skills in every skill paper):
[analysis/paper_structure.md](analysis/paper_structure.md).

## How it works
| Stage | Module | Output |
|---|---|---|
| PDF to text/Markdown | `pdf2md.py`, `ocr.swift` + `run_ocr.py` / `ocr_new.py` (macOS Vision) | `corpus/markdown*/` |
| Question parsing | `parse_generic.py` (marks parsed, never assumed); `build_bank.py` + `marks_map.py` (32 verified papers) | question rows |
| Marking schemes | `parse_ms.py`, `parse_generic.parse_marking_scheme` | `answer_keys.json` (published as `data/answer_keys.csv`) |
| Recurrence mining | `recurrence.py` (pure helpers), `topics2.py` | `scripts/topic_report2.json` |
| Index and topic split | `final_report.py` | `scripts/final_topics.json`; published tables in `data/*.csv` |
| Syllabus mapping | `ncert_*.py`, `units_xii.py`, `embed_units.py`, `syllabus_match.py` | `scripts/ncert_all_final.json`, `syllabus_match.json`; published as `data/syllabus_vs_actual.csv` |
| Pipeline / graph | `pipeline_langgraph.py`, `merge_norm.py` | `knowledge_graph/` |

Design decisions that matter:
1. **`pdftotext` duplicates content.** CBSE reprints each question's options on the facing page. Dedupe at
   *page* level; text-level dedupe silently eats legitimately repeated Assertion-Reason option blocks.
2. **Hindi-medium papers extract as mojibake.** Devanagari fonts map onto Latin code points, so gate on English
   function words (`recurrence.is_english`), not on Devanagari codepoints. Only 54% of parsed questions survive.
3. **Sets within one sitting are ~75% the same paper.** Recurrence counts distinct exam *years*, never papers.

## Repository layout
| Path | Purpose |
|---|---|
| `scripts/` | parsers, miners, OCR, syllabus mapping (script names and CLIs unchanged) |
| `tests/` | pytest characterisation tests on synthetic text and rows |
| `analysis/` | Markdown reports |
| `data/` | derived aggregates (`subject_repetition.csv`, `recurring_topics.csv`, `question_type_mix.csv`, `paper_structures.csv`, `syllabus_vs_actual.csv`, `answer_keys.csv`) and `SCHEMA.md` |
| `corpus/` | extracted Markdown, `past_paper_questions.csv` (30,734 questions), `questions.csv` (960), OCR manifests |
| `sources/` | every source URL list |
| `knowledge_graph/` | merged graphify graph and notes |

## Data sources
| Source | What is taken | Access route | Licence / caveat |
|---|---|---|---|
| cbse.gov.in past papers, sample papers, marking schemes, question banks | PDFs, converted to text | URLs in `sources/SOURCE_URLS_past_papers.txt` (762 zips), `SOURCE_URLS_sqp_ms_qb.txt`, `sqp_archive_new.txt`, `zip_urls_*.txt`; needs a browser User-Agent (403 otherwise) | (c) CBSE; free to download |
| ncert.nic.in textbooks | chapter text for unit mapping | `sources/SOURCE_URLS_ncert_xii.txt` | (c) NCERT |

```bash
while read u; do curl -sS -A "Mozilla/5.0" -O "$u"; done < sources/SOURCE_URLS_past_papers.txt
```
1,048 papers were image-only scans (573 Class XII, 416 Class X, 59 sample archive); macOS Vision OCR recovered
1,046 (8.9 million characters). Eight Hindi-medium files still lack text (`corpus/UNRECOVERABLE_TEXT.txt`);
they need a Devanagari-capable engine such as tesseract with `hin`. Source PDFs are not kept; each Markdown
file records `pdf_sha256` and `source_url`.

## Configuration
| Variable | Default | Meaning |
|---|---|---|
| `CBSE_PAPERS_ROOT` | `~/Downloads/cbse_official/past_papers` | where `topics2.py` looks for PDFs when `scripts/qcache_all.json` is absent |
| `WORKDIR` | `.` | `build_bank.py` reads text extracts from `$WORKDIR/en2/` |

No credentials are needed or committed. `scripts/qcache_all.json` is a gitignored parse cache.

## Testing
```bash
pytest -q          # 18 tests, no network, no paper content
ruff check scripts tests
```

## Limitations and known issues
- Marks in the full archive are regex-parsed and approximate; only the 32-paper `questions` table is verified
  against each paper's stated maximum (all 32 reconcile).
- Topics are mined, not hand-listed, so generic phrasing sometimes surfaces; `final_report.py` moves it into a
  "stem formula" bucket.
- macOS Vision has no Devanagari model, so bilingual papers recover the English column only.
- Several scripts hard-code `~/Downloads/...` input paths and the OCR step is macOS-only.

## Licence
Code: MIT (see `LICENSE`). Analysis text: CC BY 4.0. The question papers under `corpus/` remain the property of
the Central Board of Secondary Education, reproduced for research and educational use; if CBSE objects, the
corpus directory will be removed.
