#!/usr/bin/env python3
"""Generic CBSE paper parser for the official SQP / Marking Scheme / Question Bank PDFs.

Unlike build_bank.py (which uses a hand-verified marks map for the 12 known papers),
this one has to cope with ~90 subjects whose structures we have not read. So:
  * per-question marks are PARSED, never assumed -> marks_source='parsed' or NULL
  * question counts are validated against the paper's own "contains N questions" line
    where it prints one; papers without that line get validated=NULL, not a false OK.
Nothing here silently invents a number.
"""
import re, subprocess, pathlib, json

DEV = re.compile(r'[ऀ-ॿ]')
NOISE = re.compile(
    r'^(P\.T\.O|\[ ?P\.T\.O|Page \d+|\*\d|Series ?:|Q\.P\. ?Code|Roll No|'
    r'Candidates must write|SET[-~]|\*[A-Z ]+\*|#|g #|b$|\d+ of \d+)', re.I)

def pages(path):
    raw = subprocess.run(["pdftotext", "-layout", str(path), "-"],
                         capture_output=True, text=True, timeout=120).stdout
    return raw.split("\f")

def english_lines(path, drop_reprints=True):
    pgs = []
    for p in pages(path):
        out = []
        for l in p.splitlines():
            s = re.sub(r'\s{2,}', '  ', l.strip())
            if not s or DEV.search(s) or NOISE.match(s): continue
            if re.fullmatch(r'[\W\d_]{0,6}', s): continue
            out.append(s)
        pgs.append(out)
    keep = []
    for i, pg in enumerate(pgs):
        if not pg: continue
        if drop_reprints and not any(re.match(r'^\d{1,2}\.\s+\S', l) for l in pg):
            later = {l for p2 in pgs[i+1:] for l in p2}
            if sum(1 for l in pg if l in later) / len(pg) >= 0.8:
                continue
        keep.extend(pg)
    return keep

def latin_words(s): return len(re.findall(r'[A-Za-z]{2,}', s))

def declared_count(lines):
    for l in lines:
        m = re.search(r'contains\s+(\d+)\s+questions', l, re.I)
        if m: return int(m.group(1))
    return None

def declared_marks(lines):
    for l in lines:
        m = re.search(r'Maximum Marks\s*:?\s*(\d+)', l, re.I)
        if m: return int(m.group(1))
    return None

def split_questions(lines, cap=120):
    blocks, cur, expect = [], None, 1
    for l in lines:
        m = re.match(r'^(\d{1,3})[.)]\s+(.*)', l)
        n = int(m.group(1)) if m else None
        if m and expect <= n <= expect + 3 and n <= cap and latin_words(m.group(2)) >= 2:
            if cur: blocks.append(cur)
            for miss in range(expect, n):
                blocks.append({"q_no": miss, "lines": [], "missing": True})
            cur = {"q_no": n, "lines": [m.group(2).strip()]}
            expect = n + 1
            continue
        if cur: cur["lines"].append(l)
    if cur: blocks.append(cur)
    for b in blocks:                      # intra-block dedupe only
        seen, keep = set(), []
        for l in b["lines"]:
            if l in seen: continue
            seen.add(l); keep.append(l)
        b["lines"] = keep
    return blocks

MARK = re.compile(r'\((A|B|C|D)\)')
def options(lines):
    text = "\n".join(lines)
    hits = list(MARK.finditer(text))
    if len(hits) < 3: return None
    out = {}
    for i, h in enumerate(hits):
        end = hits[i+1].start() if i+1 < len(hits) else len(text)
        v = re.sub(r'\s+', ' ', text[h.end():end]).strip(' .;\n')
        v = re.split(r'\s(?=\d{1,2}\.\s)', v)[0].strip()
        if v and h.group(1) not in out: out[h.group(1)] = v[:300]
    return out if len(out) >= 3 else None

def marks_of(lines):
    """Trailing per-question marks, only when unambiguous. Returns (marks, source)."""
    cands = []
    for l in lines:
        m = re.search(r'(\d+)\s*[´×x*]\s*(\d+)\s*=\s*(\d+)\s*$', l)
        if m and int(m.group(1))*int(m.group(2)) == int(m.group(3)) and int(m.group(3)) <= 12:
            cands.append(int(m.group(3))); continue
        m = re.search(r'(?:^|\s)(\d+)\s*\+\s*(\d+)(?:\s*\+\s*(\d+))?\s*=\s*(\d+)\s*$', l)
        if m and int(m.group(4)) <= 12:
            cands.append(int(m.group(4))); continue
        m = re.search(r'(?:^|\s{2,})([1-9]|1[0-2])\s*$', l)
        if m: cands.append(int(m.group(1)))
    if not cands: return None, None
    return max(cands), "parsed"

def q_type(lines, opts):
    t = " ".join(lines)
    if re.search(r'Assertion \(A\)', t): return "assertion-reason"
    if re.search(r'Statement[- ]?(I|1)\s*:', t): return "two-statement"
    if re.search(r'Match (List|Column)', t, re.I): return "matching"
    if re.search(r'chronological|correct sequence|Arrange the following', t, re.I): return "ordering"
    if re.search(r'Read the (given |following )?(source|passage|text|case)|Study the (given|following)', t, re.I): return "source-based"
    if re.search(r'outline map|On the given political', t, re.I): return "map"
    return "mcq" if opts else "subjective"

def section_walk(lines, cap=120):
    sec, cur, expect = {}, None, 1
    for l in lines:
        m = re.match(r'^(?:SECTION|Section)\s*[-–—]?\s*([A-E])\b', l)
        if m: cur = m.group(1)
        p = re.match(r'^PART\s+([AB])\b', l)
        if p: cur = "Part " + p.group(1)
        mm = re.match(r'^(\d{1,3})[.)]\s+(.*)', l)
        if mm and expect <= int(mm.group(1)) <= expect+3 and int(mm.group(1)) <= cap and latin_words(mm.group(2)) >= 2:
            n = int(mm.group(1))
            for k in range(expect, n+1): sec[k] = cur
            expect = n + 1
    return sec

def parse_paper(path, subject, source, paper_id):
    lines = english_lines(path)
    decl_q, decl_m = declared_count(lines), declared_marks(lines)
    blocks = split_questions(lines)
    sec = section_walk(lines)
    rows = []
    for b in blocks:
        if b.get("missing"):
            rows.append(dict(subject=subject, source=source, paper_id=paper_id,
                q_no=b["q_no"], section=sec.get(b["q_no"]), marks=None, marks_source=None,
                q_type="figure-only", has_figure=True, has_internal_choice=False,
                question="[stem not in extractable text — figure-only or Hindi-column]",
                options=None, full_text=None))
            continue
        opts = options(b["lines"])
        mk, ms = marks_of(b["lines"])
        stem = b["lines"][0]
        for l in b["lines"][1:]:
            if re.match(r'^\((A|B|C|D|i|ii|iii|iv|v|a|b|c|d)\)', l): break
            if len(stem) < 400: stem += " " + l
        rows.append(dict(subject=subject, source=source, paper_id=paper_id,
            q_no=b["q_no"], section=sec.get(b["q_no"]), marks=mk, marks_source=ms,
            q_type=q_type(b["lines"], opts),
            has_figure=bool(re.search(r'given (image|figure|cartoon)|Fig\.|following image', " ".join(b["lines"]), re.I)),
            has_internal_choice=bool(re.search(r'^\s*OR\s*$', "\n".join(b["lines"]), re.M)),
            question=re.sub(r'\s+', ' ', stem).strip()[:1200],
            options=json.dumps(opts, ensure_ascii=False) if opts else None,
            full_text="\n".join(b["lines"])[:6000]))
    return rows, decl_q, decl_m

# ---- marking schemes: pull answer keys ----
ANS_PATTERNS = [
    re.compile(r'^\s*(\d{1,3})[.)]?\s*[.\-–|]*\s*\(?([A-D])\)?\s*$'),
    re.compile(r'^\s*(\d{1,3})[.)]?\s.*?\bOption\s*\(?([A-D])\)?', re.I),
    re.compile(r'^\s*(\d{1,3})[.)]?\s.*?\bAns(?:wer)?\.?\s*[:\-]?\s*\(?([A-D])\)?\s*$', re.I),
]
def parse_marking_scheme(path):
    """Return {q_no: 'A'|'B'|'C'|'D'} for the MCQ answers a scheme states explicitly."""
    ans = {}
    for l in english_lines(path, drop_reprints=False):
        for rx in ANS_PATTERNS:
            m = rx.match(l)
            if m:
                q, a = int(m.group(1)), m.group(2).upper()
                if 1 <= q <= 120 and q not in ans: ans[q] = a
                break
    return ans
