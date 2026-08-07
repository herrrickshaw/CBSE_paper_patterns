#!/usr/bin/env python3
"""Extract answer keys and per-question marks from CBSE marking schemes.

Marking schemes are NOT uniform answer keys. Measured across 1,337 files:
only ~5% carry a clean "12. (b)" MCQ letter key; the rest are worked solutions in
a Q.No | Expected Answer | Marks table, or free prose (language subjects).
So extract three separate things and report coverage for each, rather than
pretending a single "answer key" exists.
"""
import re, json, pathlib, collections

MD = pathlib.Path.home()/"Downloads/cbse_md/sqp_archive"
OUT = pathlib.Path(__file__).parent

# The real CBSE layout is a table flattened by pdftotext:
#     1    (c) reacts with Benzenesulphonyl chloride ...        1
# i.e. q-number, whitespace, (letter), then the answer text and trailing marks.
# Anchoring to end-of-line after the letter (an earlier mistake here) matches almost
# nothing - 1% of files instead of the true rate.
MCQ = [
    re.compile(r'^\s{0,8}(\d{1,3})[.)]?\s{1,10}\(([a-dA-D])\)', re.M),
    re.compile(r'^\s{0,8}(\d{1,3})[.)]?\s{1,10}([a-dA-D])[.)]\s', re.M),
    re.compile(r'^\s*A\s?(\d{1,3})\s*[:.]\s*\(?([a-dA-D])\)?[\s.)]', re.M),
    re.compile(r'^\s*(?:Ans\.?|Answer)\s*(\d{1,3})\s*[:.\-]\s*\(?([a-dA-D])\)?[\s.)]', re.M|re.I),
]
# answer blocks: "A18:" / "Ans 18." / a Q.No column entry followed by text
BLOCK = [
    re.compile(r'^\s*A\s?(\d{1,3})\s*[:.]\s*(.+)$', re.M),
    re.compile(r'^\s{0,8}(\d{1,3})[.)]?\s{2,10}([A-Z(].{12,})$', re.M),
    re.compile(r'^\s*(?:Ans\.?|Answer)\s*(\d{1,3})\s*[:.\-]\s*(.+)$', re.M|re.I),
]
MARKTOK = re.compile(r'(?:^|\s)(½|¼|\d+(?:\s*/\s*\d+)?)\s*M(?:ark)?s?\b')
MARKSUM = re.compile(r'\((\d+)\s*(?:[+x×]\s*\d+\s*)*=\s*(\d+)\)')

def subject_of(p):
    s = re.split(r'[-_]', p.stem)[0]
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s).strip()

def session_of(p):
    m = re.search(r'(20\d\d)[_-]?(\d\d)?', str(p.parent))
    return m.group(0).replace('_','-') if m else None

def parse(p):
    t = p.read_text(errors="ignore")
    body = re.sub(r'^---.*?^---', '', t, flags=re.S|re.M)   # strip front-matter
    keys = {}
    for rx in MCQ:
        for q, a in rx.findall(body):
            q = int(q)
            if 1 <= q <= 120: keys.setdefault(q, a.upper())
    blocks = {}
    for rx in BLOCK:
        for q, txt in rx.findall(body):
            q = int(q)
            if 1 <= q <= 120: blocks.setdefault(q, re.sub(r'\s+',' ',txt).strip()[:400])
    marks = len(MARKTOK.findall(body)) + len(MARKSUM.findall(body))
    return keys, blocks, marks

files = [p for p in MD.rglob("*.md") if re.search(r'(^|[_-])MS([_.-]|$)', p.name, re.I)]
rows, stat = [], collections.Counter()
for p in files:
    keys, blocks, marks = parse(p)
    subj, sess = subject_of(p), session_of(p)
    stat["files"] += 1
    if keys: stat["with_mcq_keys"] += 1
    if blocks: stat["with_answer_blocks"] += 1
    if marks: stat["with_mark_tokens"] += 1
    for q, a in keys.items():
        rows.append(dict(kind="mcq_key", subject=subj, session=sess, file=p.name, q_no=q, answer=a))
    for q, txt in blocks.items():
        if q in keys: continue
        rows.append(dict(kind="answer_text", subject=subj, session=sess, file=p.name, q_no=q, answer=txt))
json.dump(rows, open(OUT/"answer_keys.json","w"), indent=1)

print(f"marking schemes parsed : {stat['files']}")
print(f"  with MCQ letter keys : {stat['with_mcq_keys']:4d} ({stat['with_mcq_keys']/stat['files']:.0%})")
print(f"  with answer blocks   : {stat['with_answer_blocks']:4d} ({stat['with_answer_blocks']/stat['files']:.0%})")
print(f"  with mark tokens     : {stat['with_mark_tokens']:4d} ({stat['with_mark_tokens']/stat['files']:.0%})")
print(f"\nextracted rows: {len(rows)}  "
      f"(mcq keys {sum(1 for r in rows if r['kind']=='mcq_key')}, "
      f"answer text {sum(1 for r in rows if r['kind']=='answer_text')})")
bysub = collections.Counter(r["subject"] for r in rows if r["kind"]=="mcq_key")
print("\nsubjects with the most MCQ answer keys:")
for s,n in bysub.most_common(12): print(f"   {n:5d}  {s}")
