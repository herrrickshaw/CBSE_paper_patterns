# Knowledge graph + LangGraph pipeline

## graphify knowledge graph

`merged-graph.json` — 241 nodes, 183 edges over topics, curriculum units, exam years,
question types and subjects, built with [graphify](https://pypi.org/project/graphifyy/)
(Gemini backend) from a generated topic-first corpus.

**Shard the corpus before extracting.** Running graphify over all 89 documents at once
sends them as a single chunk; the model emits ~30 output tokens per file, extracts
richly until its output budget runs out, then silently omits the rest — 61 of 89 files
"produced no nodes". Sharding into 11 per-subject batches (each carrying that subject's
topics and units plus all year and question-type documents, so cross-links stay visible
inside every batch) and merging with `graphify merge-graphs`:

| | one corpus | 11 shards merged |
|---|---:|---:|
| nodes | 88 | 241 |
| edges | 26 | 183 |
| isolated nodes | 54 (61%) | 76 (32%) |

**Corpus shape matters too.** A subject-per-document corpus yields only hub-and-spoke
`references` edges into whatever summary document everything cites. A topic-first corpus
— one document per topic, naming its subject, years, unit and marks, with those entity
names repeated verbatim in the year/unit/subject documents — is what produces
`implements` (topic→curriculum unit) and `conceptually_related_to` (topic→topic) edges.

**Known limitations.** Merge dedupes on exact label, so `Accountancy` and
`Accountancy CBSE Class 12` survive as separate nodes; normalise labels before merging.
Unit documents are the ones the extractor drops most often.

## LangGraph pipeline

`../scripts/pipeline_langgraph.py` — the analysis as an explicit `StateGraph` with a
quality gate that routes back or halts:

    load ─► clean ─► classify ─► [gate] ─► aggregate ─► report
                       ▲            │
                       └── retry ◄──┘

It currently **halts by design**: the Bloom command-verb classifier fires on only 49% of
questions, under the gate's 50% floor, and relaxing the English filter makes coverage
worse (30%) by readmitting mojibake. That is the intended behaviour — the earlier
blueprint-vs-actual table was computed over exactly this unvalidated half, and a linear
script would have printed it without complaint.
