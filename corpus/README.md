# CBSE Class-12 corpus — markdown archive

Every PDF downloaded from CBSE was converted to Markdown and then deleted, except the
573 that are image-only scans (their text could not be extracted, so the .md would have
been empty — those PDFs are still here, listed in `KEPT_IMAGE_ONLY_PDFS.txt`).

* `official/past_papers/<year>/<Subject>/*.md` — 2022–2026 board papers, main + COMPTT
* `official/sqp_ms/*.md`, `official/skill_sqp_ms/*.md` — 2025-26 sample papers + marking schemes
* `official/question_banks/*.md` — the 12 official CBSE Question Banks
* `original_32/*.md` — the 32 papers this started from (byte-identical to archive copies)

Each .md carries front-matter with `pdf_sha256`, `pdf_bytes`, `pages` and `source_url`,
so any deleted PDF can be re-fetched and verified. Full URL lists:
`SOURCE_URLS_past_papers.txt` (762 zips) and `SOURCE_URLS_sqp_ms_qb.txt`.

Re-download needs a browser User-Agent — cbse.gov.in returns 403 otherwise:

    curl -A "Mozilla/5.0" -O <url>

`low_text_pages` in the front-matter counts pages that yielded almost no text — those
are diagrams, maps and cartoons, and that content did not survive conversion.
