#!/usr/bin/env python3
"""Parse CBSE Class 12 question papers into a structured question bank."""
import re, json, os, pathlib, unicodedata
from collections import Counter
import sys; sys.path.insert(0, str(pathlib.Path(__file__).parent))
from marks_map import ACADEMIC, SKILL

SP = pathlib.Path(os.environ.get("WORKDIR", "."))   # holds en2/ text extracts
EN = SP / "en2"

META = {  # stem -> (subject, qp_code, set_label, max_marks, declared_q, architecture)
 "Artificial_Intelligence":      ("Artificial Intelligence","367/S","SET~4",50,21,"skill"),
 "Information_Technology":       ("Information Technology","326/S","Set-4",60,24,"skill"),
 "Typography_Computer":          ("Typography and Computer Applications","341/S","SET~4",60,24,"skill"),
 "WEB_APPLICATIONS":             ("Web Applications","327","SET-4",60,25,"skill"),
 "Financial_Markets_Management": ("Financial Markets Management","329","SET-4",60,24,"skill"),
 "Taxation":                     ("Taxation","346","SET~4",60,24,"skill"),
 "Engineering_Graphics":         ("Engineering Graphics","68/S","SET~4",70,25,"drawing"),
 "Computer_Science":             ("Computer Science","91/S","Set-4",70,37,"academic"),
 "61-S-1_History":               ("History","61/S/1","SET~1",80,34,"academic"),
 "61-S-2_History":               ("History","61/S/2","SET~2",80,34,"academic"),
 "61-S-3_History":               ("History","61/S/3","SET~3",80,34,"academic"),
 "58-S-1_Economics":             ("Economics","58/S/1","SET~1",80,34,"academic"),
 "58-S-2_Economics":             ("Economics","58/S/2","SET~2",80,34,"academic"),
 "58-S-3_Economics":             ("Economics","58/S/3","SET~3",80,34,"academic"),
 "67-S-1-Accountancy":           ("Accountancy","67/S/1","SET~1",80,34,"academic"),
 "67-S-2-Accountancy":           ("Accountancy","67/S/2","SET~2",80,34,"academic"),
 "67-S-3_Accountancy":           ("Accountancy","67/S/3","SET~3",80,34,"academic"),
}
for s in range(1,6):
    for v in range(1,4):
        META[f"59-{s}-{v}_Political_Science"] = ("Political Science",f"59/{s}/{v}",f"SET~{v}",80,30,"academic")

NOISE = re.compile(
    r'^(P\.T\.O|\[ ?P\.T\.O|Page \d+|\*\d|\d+/S|\d+ +\*|Series ?:|Q\.P\. ?Code|Roll No|'
    r'Candidates must write|SET[-~]|\*[A-Z ]+\*|#|g #|b$|\d+ of \d+)', re.I)

def clean(stem):
    """Lines of the English text, minus running headers/footers."""
    out=[]
    for l in (EN/f"{stem}.txt").read_text().splitlines():
        s=l.strip()
        if not s or NOISE.match(s): continue
        if re.fullmatch(r'[\W\d_]{0,6}', s): continue
        out.append(s)
    return out

def latin_words(s):
    return len(re.findall(r'[A-Za-z]{2,}', s))

def split_questions(lines, declared):
    """State machine: advance only on the next expected question number."""
    blocks, cur, expect = [], None, 1
    preamble=[]
    for l in lines:
        m = re.match(r'^(\d{1,2})\.\s+(.*)', l)
        n = int(m.group(1)) if m else None
        # tolerate a gap of up to 3: some stems live only in a figure or the Hindi column
        if m and expect <= n <= expect+3 and n <= declared and latin_words(m.group(2)) >= 2:
            if cur: blocks.append(cur)
            for missing in range(expect, n):          # placeholder for un-extractable stem
                blocks.append({"q_no": missing, "lines": [], "missing": True})
            cur = {"q_no": n, "lines": [m.group(2).strip()]}
            expect = n + 1
            continue
        (cur["lines"] if cur else preamble).append(l)
    if cur: blocks.append(cur)
    return blocks, preamble

def dedupe_forward(blocks):
    """Drop lines that reappear verbatim in a LATER block (pdftotext facing-page spill)."""
    later = [Counter() for _ in blocks]
    acc = Counter()
    for b in reversed(range(len(blocks))):
        later[b] = acc.copy()
        acc.update(blocks[b]["lines"])
    for b in blocks:
        seen=set(); keep=[]
        for l in b["lines"]:
            if l in seen: continue                 # intra-block repeat only
            seen.add(l); keep.append(l)
        b["lines"]=keep
    return blocks

BLOCK_RE = [
  # "Answer any 3 out of the given 5 questions in 20-30 words each.  3x2=6"
  (re.compile(r'Answer any\s+(\d+).{0,80}?given\s+(\d+)\s+questions.*?(\d+)\s*[\u00b4\u00d7x*]\s*(\d+)\s*=\s*(\d+)', re.I), "answer_any"),
  # "SECTION B (Short-Answer Type Questions)  6 3=18"  /  "21 1= 21"
  (re.compile(r'^\(?(?:Short|Long|Objective|Subjective|Multiple|Source|Map|Passage)[^)]*\)?\s*(\d+)\s*[\u00b4\u00d7x* ]\s*(\d+)\s*=\s*(\d+)\s*$', re.I), "section_hdr"),
  (re.compile(r'^(\d+)\s*[\u00b4\u00d7x*]\s*(\d+)\s*=\s*(\d+)\s*$'), "bare"),
]
def block_marks_walk(lines, decl):
    """Return {q_no: (per_q_marks, answer_any, out_of)} inherited from instruction lines."""
    out={}; per=None; anyn=None; ofn=None; expect=1
    for l in lines:
        for rx,kind in BLOCK_RE:
            m=rx.search(l)
            if not m: continue
            if kind=="answer_any":
                anyn,ofn,per = int(m.group(1)), int(m.group(2)), int(m.group(4))
            elif kind=="section_hdr":
                per=int(m.group(2)); anyn=ofn=None
            else:
                a,b,c=(int(x) for x in m.groups())
                if a*b==c and b<=8: per, anyn, ofn = b, None, None
            break
        mm=re.match(r'^(\d{1,2})\.\s+(.*)', l)
        if mm and expect <= int(mm.group(1)) <= expect+3 and int(mm.group(1))<=decl and latin_words(mm.group(2))>=2:
            n=int(mm.group(1))
            for k in range(expect,n+1): out[k]=(per,anyn,ofn)
            expect=n+1
    return out

MARKS_PAT = [
    (re.compile(r'(\d+)\s*[´×x*]\s*(\d+)\s*=\s*(\d+)\s*$'), lambda m: int(m.group(3))),
    (re.compile(r'(?:^|\s)(\d+)\+(\d+)(?:\+(\d+))?\s*=\s*(\d+)\s*$'), lambda m: int(m.group(4))),
    (re.compile(r'(?:^|\s)([1-9]|1[0-9]|2[0-7])\s*$'), lambda m: int(m.group(1))),
]
def extract_marks(lines, block=None):
    """Trailing per-question marks if present and plausible, else inherit the block value."""
    per, anyn, ofn = (block or (None,None,None))
    parts=[]
    for l in lines:
        m = re.search(r'(\d+)\s*[\u00b4\u00d7x*]\s*(\d+)\s*=\s*(\d+)\s*$', l)
        if m and int(m.group(1))*int(m.group(2))==int(m.group(3)) and int(m.group(3))<=12:
            parts.append(int(m.group(3))); continue
        m = re.search(r'(?:^|\s)(\d+)\s*\+\s*(\d+)(?:\s*\+\s*(\d+))?\s*=\s*(\d+)\s*$', l)
        if m and int(m.group(4))<=12: parts.append(int(m.group(4))); continue
        m = re.search(r'(?:^|\s{2,})([1-9]|1[0-3])\s*$', l)
        if m: parts.append(int(m.group(1)))
    if parts:
        v=max(parts)
        if v<=13: return v
    return per

MARK = re.compile(r'\((A|B|C|D)\)')
def extract_options(lines):
    """Split on (A)..(D) markers positionally so nested parens survive."""
    text = "\n".join(lines)
    hits = list(MARK.finditer(text))
    if len(hits) < 3: return None
    opts = {}
    for i, h in enumerate(hits):
        end = hits[i+1].start() if i+1 < len(hits) else len(text)
        val = re.sub(r'\s+', ' ', text[h.end():end]).strip(' .;\n')
        val = re.split(r'\s(?=\d{1,2}\.\s)', val)[0].strip()      # stop at next question
        if val and h.group(1) not in opts:
            opts[h.group(1)] = val[:300]
    return opts if len(opts) >= 3 else None

def q_type(text, opts, lines):
    t=" ".join(lines)
    if re.search(r'Assertion \(A\)', t): return "assertion-reason"
    if re.search(r'Statement[- ]?(I|1)\s*:', t): return "two-statement"
    if re.search(r'Match (List|Column)', t, re.I): return "matching"
    if re.search(r'chronological|correct sequence|Arrange the following', t, re.I): return "ordering"
    if re.search(r'Read the (given |following )?(source|passage|text)|Study the (given|following)', t, re.I): return "source-based"
    if re.search(r'outline map|On the given political', t, re.I): return "map"
    if opts: return "mcq"
    return "subjective"

def section_of(lines_before):
    for l in reversed(lines_before):
        m=re.match(r'^(?:SECTION|Section)\s*[-–—]?\s*([A-E])\b', l)
        if m: return m.group(1)
        if re.match(r'^PART\s+([AB])\b', l): return "Part "+re.match(r'^PART\s+([AB])\b', l).group(1)
    return None

rows=[]
report=[]
for stem,(subj,code,setl,maxm,decl,arch) in META.items():
    lines = clean(stem)
    blocks, preamble = split_questions(lines, decl)
    blocks = dedupe_forward(blocks)
    spec = ACADEMIC.get(subj) or SKILL.get(subj)
    def lookup(q):
        for a,b,mk,anyn,label in spec:
            if a<=q<=b: return mk,anyn,(b-a+1),label
        return None,None,None,None
    # section tracking: walk original lines, remember last SECTION header before each q
    sec_at={}; cur_sec=None; expect=1
    for l in lines:
        m=re.match(r'^(?:SECTION|Section)\s*[-–—]?\s*([A-E])\b', l)
        if m: cur_sec=m.group(1)
        p=re.match(r'^PART\s+([AB])\b', l)
        if p: cur_sec="Part "+p.group(1)
        mm=re.match(r'^(\d{1,2})\.\s+(.*)', l)
        if mm and expect <= int(mm.group(1)) <= expect+3 and int(mm.group(1))<=decl and latin_words(mm.group(2))>=2:
            n=int(mm.group(1))
            for miss in range(expect,n): sec_at[miss]=cur_sec
            sec_at[n]=cur_sec; expect=n+1
    for b in blocks:
        txt=" ".join(b["lines"])
        opts=extract_options(b["lines"])
        if b.get("missing"):
            rows.append(dict(subject=subj, qp_code=code, paper_set=setl, architecture=arch,
                max_marks_paper=maxm, section=sec_at.get(b["q_no"]), q_no=b["q_no"],
                marks=lookup(b["q_no"])[0], block=lookup(b["q_no"])[3],
                block_answer_any=lookup(b["q_no"])[1], block_out_of=lookup(b["q_no"])[2],
                q_type="figure-only", has_figure=True, has_internal_choice=False,
                employability=False,
                question="[stem not present in extractable text — figure-only or Hindi-column question]",
                options=None, full_text=None))
            continue
        stem_text=b["lines"][0]
        for l in b["lines"][1:]:
            if re.match(r'^\((A|B|C|D|i|ii|iii|iv|v|vi|vii|a|b|c|d)\)', l): break
            if len(stem_text)<400: stem_text+=" "+l
        rows.append(dict(
            subject=subj, qp_code=code, paper_set=setl, architecture=arch,
            max_marks_paper=maxm, section=sec_at.get(b["q_no"]), q_no=b["q_no"],
            marks=lookup(b["q_no"])[0],
            block_answer_any=lookup(b["q_no"])[1],
            block_out_of=lookup(b["q_no"])[2],
            block=lookup(b["q_no"])[3],
            q_type=q_type(txt,opts,b["lines"]),
            has_figure=bool(re.search(r'given (image|figure|cartoon)|Fig\.|the given map|following image', txt, re.I)),
            has_internal_choice=bool(re.search(r'^\s*OR\s*$', "\n".join(b["lines"]), re.M)),
            employability=bool(re.search(r'Employability [Ss]kills', txt)),
            question=re.sub(r'\s+',' ',stem_text).strip()[:1200],
            options=json.dumps(opts, ensure_ascii=False) if opts else None,
            full_text="\n".join(b["lines"])[:6000],
        ))
    report.append((stem, decl, len(blocks)))

print(f"{'paper':32s} declared parsed")
bad=0
for stem,decl,got in report:
    flag="" if decl==got else "  <-- MISMATCH"
    if decl!=got: bad+=1
    print(f"{stem:32s} {decl:>8d} {got:>6d}{flag}")
print(f"\ntotal questions parsed: {len(rows)}   papers with count mismatch: {bad}")
json.dump(rows, open(SP/"bank.json","w"), ensure_ascii=False, indent=1)
