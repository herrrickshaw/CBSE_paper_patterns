#!/usr/bin/env python3
"""LangGraph pipeline over the CBSE question corpus.

The analysis so far has been a pile of one-off scripts where each stage silently
assumed the previous one worked — which is exactly how the paper-count bug and the
mojibake got as far as they did. This models it as an explicit StateGraph with a
quality gate that can route work back or halt, so a bad stage fails loudly.

    load ─► clean ─► classify ─► [gate] ─► aggregate ─► report
                       ▲            │
                       └── retry ◄──┘ (relaxes the English gate once, then halts)

Nodes are plain functions - no LLM calls, so this runs offline and deterministically.
"""
from __future__ import annotations
import json, re, sys, pathlib, collections
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from topics2 import is_english, ngrams, CACHE
from methods2 import bloom_of, INSTRUCTION

class S(TypedDict, total=False):
    rows: list
    clean: list
    classified: list
    subjects: dict
    report: dict
    attempts: int
    strict: bool
    errors: list
    log: list

def load(s: S) -> S:
    rows = json.loads(CACHE.read_text())
    return {"rows": rows, "attempts": 0, "strict": True, "errors": [], "log": [f"load: {len(rows)} raw questions"]}

def clean(s: S) -> S:
    out, dropped = [], collections.Counter()
    for r in s["rows"]:
        q = r.get("question") or ""
        if not q: dropped["empty"] += 1; continue
        if s["strict"] and not is_english(q): dropped["not_english"] += 1; continue
        if INSTRUCTION.search(q): dropped["instruction_boilerplate"] += 1; continue
        out.append(r)
    return {"clean": out, "log": s["log"] + [f"clean(strict={s['strict']}): kept {len(out)}, dropped {dict(dropped)}"]}

def classify(s: S) -> S:
    out = []
    for r in s["clean"]:
        r = dict(r)
        r["bloom"] = bloom_of(r["question"])
        r["high_mark"] = (r.get("marks") or 0) >= 4
        out.append(r)
    return {"classified": out, "attempts": s["attempts"] + 1,
            "log": s["log"] + [f"classify: {sum(1 for r in out if r['bloom'])}/{len(out)} assigned a Bloom level"]}

def gate(s: S) -> Literal["aggregate", "retry", "halt"]:
    """Quality gate. Refuses to publish an aggregate built on too little evidence."""
    c = s["classified"]
    if not c: return "halt" if s["attempts"] > 1 else "retry"
    covered = sum(1 for r in c if r["bloom"]) / len(c)
    high = sum(1 for r in c if r["high_mark"])
    if covered < 0.5 or high < 200:
        return "retry" if s["attempts"] < 2 else "halt"
    return "aggregate"

def retry(s: S) -> S:
    return {"strict": False, "log": s["log"] + ["gate FAILED -> relaxing the English filter and retrying once"]}

def halt(s: S) -> S:
    return {"errors": s.get("errors", []) + ["quality gate failed twice; refusing to emit an aggregate"],
            "log": s["log"] + ["HALT"]}

def aggregate(s: S) -> S:
    by = collections.defaultdict(lambda: {"marks": collections.Counter(), "years": set(),
                                          "high_q": 0, "topics": collections.defaultdict(set)})
    for r in s["classified"]:
        d = by[r["subject"]]
        d["years"].add(r.get("year"))
        if r["bloom"] and r.get("marks"): d["marks"][r["bloom"]] += r["marks"]
        if r["high_mark"]:
            d["high_q"] += 1
            for g in set(ngrams(r["question"])): d["topics"][g].add(r.get("year"))
    out = {}
    for subj, d in by.items():
        if d["high_q"] < 25: continue
        rec = {g: len(y) for g, y in d["topics"].items() if len(y) >= 3}
        tot = sum(d["marks"].values()) or 1
        out[subj] = dict(years=sorted(x for x in d["years"] if x), high_q=d["high_q"],
                         bloom_pct={k: round(100*v/tot) for k, v in d["marks"].items()},
                         recurring_topics=len(rec),
                         top=sorted(rec.items(), key=lambda x: -x[1])[:8])
    return {"subjects": out, "log": s["log"] + [f"aggregate: {len(out)} subjects passed the >=25 high-mark-question floor"]}

def report(s: S) -> S:
    rep = dict(subjects=s["subjects"], log=s["log"], errors=s.get("errors", []))
    pathlib.Path(__file__).parent.joinpath("langgraph_report.json").write_text(json.dumps(rep, indent=1))
    return {"report": rep}

g = StateGraph(S)
for name, fn in [("load", load), ("clean", clean), ("classify", classify),
                 ("retry", retry), ("halt", halt), ("aggregate", aggregate), ("report", report)]:
    g.add_node(name, fn)
g.set_entry_point("load")
g.add_edge("load", "clean")
g.add_edge("clean", "classify")
g.add_conditional_edges("classify", gate, {"aggregate": "aggregate", "retry": "retry", "halt": "halt"})
g.add_edge("retry", "clean")            # loop back with the relaxed filter
g.add_edge("aggregate", "report")
g.add_edge("report", END)
g.add_edge("halt", END)
app = g.compile()

if __name__ == "__main__":
    final = app.invoke({}, {"recursion_limit": 25})
    print("\n".join(final["log"]))
    if final.get("errors"): print("ERRORS:", final["errors"]); raise SystemExit(1)
    subs = final["report"]["subjects"]
    print(f"\n{'subject':22s} {'highQ':>6s} {'recurring':>10s}  bloom R+U/App/AEC")
    for s_, d in sorted(subs.items(), key=lambda x: -x[1]["high_q"])[:14]:
        b = d["bloom_pct"]
        print(f"  {s_[:20]:20s} {d['high_q']:6d} {d['recurring_topics']:10d}  "
              f"{b.get('remember_understand',0):>2}/{b.get('apply',0):>2}/{b.get('analyse_evaluate_create',0):>2}")
    try:
        png = app.get_graph().draw_mermaid()
        pathlib.Path(__file__).parent.joinpath("pipeline.mmd").write_text(png)
        print("\nmermaid graph -> pipeline.mmd")
    except Exception:
        pass
