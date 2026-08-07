#!/usr/bin/env python3
"""Merge graphify shard graphs, deduplicating on a NORMALISED label.

graphify's own merge-graphs dedupes on exact label, so the same entity survives as
variants: "Accountancy" / "Accountancy CBSE Class 12", "Economics" / "CBSE Class 12
Economics". Normalise first, then merge nodes and remap every edge onto the survivor.
"""
import json, re, pathlib, collections, sys

BATCHES = pathlib.Path.home()/"Downloads/cbse_kg_batches"
OUT     = pathlib.Path.home()/"Downloads/cbse_kg_topics/merged-graph-normalised.json"

BOILER = re.compile(
    r'\b(cbse|class\s*(xii|12|x|10)|senior\s*secondary|board|examination|exam)\b', re.I)
def norm(label: str) -> str:
    s = BOILER.sub(' ', label or '')
    s = re.sub(r'[^A-Za-z0-9 ]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    # singularise a trailing 's' only on multiword phrases (keeps "Physics" intact)
    if ' ' in s and s.endswith('s') and not s.endswith('ss'): s = s[:-1]
    return s

def pick(labels):
    """Prefer the shortest informative surface form, tie-broken alphabetically."""
    return sorted(labels, key=lambda l: (len(l), l))[0]

graphs = sorted(BATCHES.glob("*/graphify-out/graph.json"))
by_norm = collections.defaultdict(lambda: {"labels": set(), "ids": set(), "files": set(), "communities": set()})
edges = []
for gp in graphs:
    g = json.loads(gp.read_text())
    local = {}
    for n in g["nodes"]:
        k = norm(n.get("label") or n["id"])
        if not k: continue
        d = by_norm[k]
        d["labels"].add(n.get("label") or n["id"]); d["ids"].add(n["id"])
        if n.get("source_file"): d["files"].add(n["source_file"])
        local[n["id"]] = k
    for e in (g.get("links") or g.get("edges") or []):
        s, t = local.get(e.get("source")), local.get(e.get("target"))
        if s and t and s != t:
            edges.append((s, t, e.get("relation") or "references",
                          e.get("confidence"), float(e.get("confidence_score") or 0)))

nodes = []
for k, d in by_norm.items():
    nodes.append(dict(id=re.sub(r'[^a-z0-9]+','_',k).strip('_'), key=k, label=pick(d["labels"]),
                      aliases=sorted(d["labels"]), merged_from=len(d["ids"]),
                      source_files=sorted(d["files"])[:6]))
idx = {n["key"]: n["id"] for n in nodes}
seen, out_edges = set(), []
for s, t, rel, conf, score in edges:
    key = (idx[s], idx[t], rel)
    if key in seen: continue
    seen.add(key)
    out_edges.append(dict(source=idx[s], target=idx[t], relation=rel,
                          confidence=conf, confidence_score=score))

deg = collections.Counter()
for e in out_edges: deg[e["source"]] += 1; deg[e["target"]] += 1
for n in nodes: n["degree"] = deg[n["id"]]

OUT.write_text(json.dumps(dict(directed=True, multigraph=False,
    graph={"note":"graphify shards merged with normalised-label dedup"},
    nodes=nodes, links=out_edges), indent=1))

raw_nodes = sum(len(json.loads(p.read_text())["nodes"]) for p in graphs)
iso = sum(1 for n in nodes if n["degree"] == 0)
print(f"shards: {len(graphs)}   raw nodes across shards: {raw_nodes}")
print(f"merged: {len(nodes)} nodes, {len(out_edges)} edges | isolated {iso} ({iso/len(nodes):.0%})")
collapsed = [n for n in nodes if n["merged_from"] > 1 or len(n["aliases"]) > 1]
print(f"\nentities collapsed from variants: {len(collapsed)}")
for n in sorted(collapsed, key=lambda x: -len(x["aliases"]))[:12]:
    print(f"   {n['label']:34s} <- {', '.join(sorted(n['aliases']))[:90]}")
print("\ntop hubs:")
for n in sorted(nodes, key=lambda x: -x["degree"])[:12]:
    print(f"   {n['degree']:3d}  {n['label']}")
print("\nrelations:", dict(collections.Counter(e["relation"] for e in out_edges).most_common()))
print("->", OUT)
