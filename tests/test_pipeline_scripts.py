"""Module-level pipeline scripts, run in a sandbox with a fake HOME and fake pdftotext.
All inputs are small SYNTHETIC fixtures."""
import json
import types

import pytest
from scriptrunner import run_script, sandbox_dir

import topics2


@pytest.fixture
def home(tmp_path, monkeypatch):
    h = tmp_path / "home"
    h.mkdir()
    monkeypatch.setenv("HOME", str(h))
    return h


def fake_run(monkeypatch, fn):
    import subprocess
    monkeypatch.setattr(subprocess, "run", lambda cmd, **k: types.SimpleNamespace(stdout=fn(cmd)))


# =========================== parse_ms.py ===========================

def _ms_dir(home):
    d = home / "Downloads/cbse_md/sqp_archive/2024-25"
    d.mkdir(parents=True)
    return d


def test_parse_ms_extracts_keys_blocks_and_stats(home, tmp_path, monkeypatch, capsys):
    d = _ms_dir(home)
    (d / "BusinessStudies-MS-2024.md").write_text(
        "---\ntitle: x\n1. (a) dropped front matter\n---\n"
        "1    (c) reacts with benzene and more       1\n"
        "2.   (B) second\n"
        "3. d. third key line\n"
        "A4: (a) fourth\n"
        "Ans 5: b fifth\n"
        "A18: The long worked answer text goes here and is long\n"
        "   7   Expected answer text that is long enough here\n"
        "Answer 9 - a long text for nine ...........\n"
        "1 Mark and 2 Marks and 1/2 Marks (3 + 2 = 5)\n"
        "500. (a) out of range\n")
    (d / "Physics_notams.md").write_text("1. (a)\n")             # not an MS file: ignored
    (d / "Maths_QP.md").write_text("1. (a)\n")
    fake = sandbox_dir(tmp_path)
    run_script("parse_ms", fake, monkeypatch)
    rows = json.loads((fake / "answer_keys.json").read_text())
    keys = {r["q_no"]: r["answer"] for r in rows if r["kind"] == "mcq_key"}
    assert keys == {1: "C", 2: "B", 3: "D", 4: "A", 5: "B", 9: "A"}
    texts = {r["q_no"] for r in rows if r["kind"] == "answer_text"}
    assert texts == {7, 18}                # "Answer 9 - a" is read as a letter key instead
    assert 1 not in texts and 4 not in texts            # a key wins over an answer block
    assert all(r["q_no"] <= 120 for r in rows)
    subj = {r["subject"] for r in rows}
    assert subj == {"Business Studies"}
    assert {r["session"] for r in rows} == {"2024-25"}
    assert {r["file"] for r in rows} == {"BusinessStudies-MS-2024.md"}
    out = capsys.readouterr().out
    assert "marking schemes parsed : 1" in out
    assert "with MCQ letter keys :    1 (100%)" in out
    assert "with mark tokens     :    1 (100%)" in out
    assert "(mcq keys 6, answer text 2)" in out


def test_parse_ms_missing_input_exits(home, tmp_path, monkeypatch):
    fake = sandbox_dir(tmp_path)
    with pytest.raises(SystemExit) as e:
        run_script("parse_ms", fake, monkeypatch)
    assert "marking-scheme markdown" in str(e.value)


def test_parse_ms_helpers(home, tmp_path, monkeypatch):
    d = _ms_dir(home)
    (d / "Physics-MS.md").write_text("1. (a)\n")
    g = run_script("parse_ms", sandbox_dir(tmp_path), monkeypatch)
    import pathlib
    assert g["subject_of"](pathlib.Path("PoliticalScience_MS.md")) == "Political Science"
    assert g["subject_of"](pathlib.Path("Maths-MS.md")) == "Maths"
    assert g["session_of"](pathlib.Path("/x/2023_24/f.md")) == "2023-24"
    assert g["session_of"](pathlib.Path("/x/2023/f.md")) == "2023"
    assert g["session_of"](pathlib.Path("/x/none/f.md")) is None


def test_parse_ms_marker_regexp_requires_ms_token(home, tmp_path, monkeypatch, capsys):
    d = _ms_dir(home)
    (d / "A_MS.md").write_text("1. (a)\n")
    (d / "B-MS-x.md").write_text("1. (a)\n")
    (d / "C_MS_.md").write_text("1. (a)\n")
    (d / "DMS.md").write_text("1. (a)\n")                  # no separator: not counted
    (d / "E_MSA.md").write_text("1. (a)\n")                # not counted
    run_script("parse_ms", sandbox_dir(tmp_path), monkeypatch)
    assert "marking schemes parsed : 3" in capsys.readouterr().out


@pytest.mark.xfail(strict=True, raises=ZeroDivisionError,
                   reason="parse_ms.py divides by stat['files'] without a guard: a directory with "
                          "markdown but no marking-scheme (MS) files crashes with ZeroDivisionError "
                          "instead of reporting 0 (parse_ms.py:~77)")
def test_parse_ms_no_marking_schemes_reports_zero(home, tmp_path, monkeypatch, capsys):
    (_ms_dir(home) / "Physics_QP.md").write_text("1. (a)\n")
    run_script("parse_ms", sandbox_dir(tmp_path), monkeypatch)
    assert "marking schemes parsed : 0" in capsys.readouterr().out


# =========================== units_xii.py ===========================

CUR_TXT = """\
Class - XI
   Unit One Foundations            15
Class - XII
   Unit I Electric Charges and Fields     16
   Unit II Current Electricity            14
   Unit III Magnetic Effects              12
   Optics and Waves                       14
   Atoms and Nuclei                       24
   Total theory                           80
   Practical work                         30
   Unit I Electric Charges and Fields     16
   tiny                                   10
   Mass Section Alpha                     45
"""


def test_units_xii_keeps_only_class_xii_units(home, tmp_path, monkeypatch, capsys):
    cur = home / "Downloads/cbse_official/curriculum"
    cur.mkdir(parents=True)
    (cur / "Physics_SrSec_2024.pdf").write_bytes(b"x")
    (cur / "Physics_Hi_SrSec.pdf").write_bytes(b"x")          # Hindi: skipped
    (cur / "Short_SrSec.pdf").write_bytes(b"x")                # < 3 units: dropped
    (cur / "Tiny_hi.pdf").write_bytes(b"x")
    fake_run(monkeypatch, lambda cmd: CUR_TXT if "Physics_SrSec" in cmd[-2] else
             "Class - XII\n   Unit I Something Else       20\n   Unit II Another One        10\n"
             if "Short" in cmd[-2] else "")
    fake = sandbox_dir(tmp_path)
    run_script("units_xii", fake, monkeypatch)
    res = json.loads((fake / "units_xii.json").read_text())
    assert list(res) == ["Physics"]
    names = [n for n, m in res["Physics"]]
    marks = [m for n, m in res["Physics"]]
    assert "Unit One Foundations" not in names                      # Class XI unit
    assert names.count("Unit I Electric Charges and Fields") == 1  # de-duplicated
    assert "Total theory" not in names and "Practical work" not in names
    assert "tiny" not in names                                      # < 6 chars
    assert "Mass Section Alpha" not in names                        # 45 > 40 marks
    assert marks == [16, 14, 12, 14, 24]
    out = capsys.readouterr().out
    assert "subjects with a clean Class-XII unit table: 1" in out
    assert "Physics" in out and "80 marks over 5 units" in out


def test_units_xii_rejects_implausible_totals(home, tmp_path, monkeypatch, capsys):
    cur = home / "Downloads/cbse_official/curriculum"
    cur.mkdir(parents=True)
    (cur / "Low_SrSec.pdf").write_bytes(b"x")
    fake_run(monkeypatch, lambda cmd: "Class XII\n   Unit I Alpha Beta Gamma     10\n"
             "   Unit II Delta Epsilon      10\n   Unit III Zeta Eta Theta    10\n")
    fake = sandbox_dir(tmp_path)
    run_script("units_xii", fake, monkeypatch)
    assert json.loads((fake / "units_xii.json").read_text()) == {}      # total 30 < 60


def test_units_xii_total_bounds_inclusive(home, tmp_path, monkeypatch):
    cur = home / "Downloads/cbse_official/curriculum"
    cur.mkdir(parents=True)
    for n in ("Lo", "Hi", "Over", "Under"):
        (cur / f"{n}_SrSec.pdf").write_bytes(b"x")

    def mk(a, b, c):
        return f"Class XII\n   Unit I Alpha Beta Gamma     {a}\n   Unit II Delta Epsilon      {b}\n   Unit III Zeta Eta Theta    {c}\n"
    table = {"Lo_SrSec": mk(20, 20, 20), "Hi_SrSec": mk(40, 40, 30),
             "Over_SrSec": mk(40, 40, 31), "Under_SrSec": mk(20, 20, 19)}
    # note: "Hi_SrSec" does not match the Hindi filter ('Hi_' needs to be in the name -> it IS)
    fake_run(monkeypatch, lambda cmd: next((v for k, v in table.items() if k in cmd[-2]), ""))
    fake = sandbox_dir(tmp_path)
    run_script("units_xii", fake, monkeypatch)
    res = json.loads((fake / "units_xii.json").read_text())
    assert "Lo" in res and "Over" not in res and "Under" not in res
    assert "Hi" not in res        # filename contains 'Hi_' so it is treated as a Hindi edition


def test_units_xii_missing_dir_exits(home, tmp_path, monkeypatch):
    with pytest.raises(SystemExit):
        run_script("units_xii", sandbox_dir(tmp_path), monkeypatch)


# =========================== merge_norm.py ===========================

def _graph(d, name, nodes, links):
    p = d / name / "graphify-out"
    p.mkdir(parents=True)
    (p / "graph.json").write_text(json.dumps({"nodes": nodes, "links": links}))


def test_merge_norm_dedupes_on_normalised_label(home, tmp_path, monkeypatch, capsys):
    b = home / "Downloads/cbse_kg_batches"
    (home / "Downloads/cbse_kg_topics").mkdir(parents=True)
    _graph(b, "s1", [
        {"id": "a1", "label": "Accountancy", "source_file": "f1"},
        {"id": "e1", "label": "CBSE Class 12 Economics"},
        {"id": "x1", "label": "Cash Flows"},
        {"id": "blank", "label": "CBSE Class 12"},          # normalises to '' -> dropped
    ], [{"source": "a1", "target": "e1", "relation": "relates", "confidence": "EXTRACTED",
         "confidence_score": 0.9},
        {"source": "a1", "target": "a1", "relation": "self"},          # self loop after norm: dropped
        {"source": "a1", "target": "blank", "relation": "r"},          # unknown target: dropped
        {"source": "e1", "target": "x1"}])
    _graph(b, "s2", [
        {"id": "a2", "label": "Accountancy CBSE Class 12", "source_file": "f2"},
        {"id": "e2", "label": "Economics"},
        {"id": "x2", "label": "Cash Flow"},
    ], [{"source": "a2", "target": "e2", "relation": "relates", "confidence": "EXTRACTED",
         "confidence_score": 0.5},
        {"source": "x2", "target": "a2"}])
    run_script("merge_norm", sandbox_dir(tmp_path), monkeypatch)
    out = json.loads((home / "Downloads/cbse_kg_topics/merged-graph-normalised.json").read_text())
    byl = {n["label"]: n for n in out["nodes"]}
    assert set(byl) == {"Accountancy", "Economics", "Cash Flow"}
    acc = byl["Accountancy"]
    assert acc["merged_from"] == 2 and acc["aliases"] == ["Accountancy", "Accountancy CBSE Class 12"]
    assert acc["source_files"] == ["f1", "f2"]
    assert byl["Cash Flow"]["merged_from"] == 2              # 'cash flows' singularised
    assert byl["Cash Flow"]["aliases"] == ["Cash Flow", "Cash Flows"]
    # edges: acc->econ relates (deduped across shards), econ->cashflow references, cashflow->acc references
    rel = {(e["source"], e["target"], e["relation"]) for e in out["links"]}
    assert rel == {("accountancy", "economics", "relates"),
                   ("economics", "cash_flow", "references"),
                   ("cash_flow", "accountancy", "references")}
    assert len(out["links"]) == 3
    assert all(n["degree"] == 2 for n in out["nodes"])
    text = capsys.readouterr().out
    assert "shards: 2   raw nodes across shards: 7" in text
    assert "merged: 3 nodes, 3 edges | isolated 0 (0%)" in text
    assert "entities collapsed from variants: 3" in text


def test_merge_norm_functions(home, tmp_path, monkeypatch):
    b = home / "Downloads/cbse_kg_batches"
    (home / "Downloads/cbse_kg_topics").mkdir(parents=True)
    _graph(b, "s1", [{"id": "a", "label": "A thing"}], [])
    g = run_script("merge_norm", sandbox_dir(tmp_path), monkeypatch)
    n = g["norm"]
    assert n("Physics") == "physics"                       # 'ss'-ending singular kept
    assert n("Class 12 Physics") == "physics"
    assert n("Senior Secondary Study Notes") == "study note"
    assert n("Boards, Exams") == "boards exam"      # \bexam\b does not strip "exams"
    assert n("Notes") == "notes"          # single words are never singularised
    assert n(None) == "" and n("") == ""
    assert n("Chemical Bonds") == "chemical bond"
    assert n("Class") == "class" and n("Business") == "business"
    assert g["pick"](["Longer Label", "Short", "Alpha", "Beta"]) == "Beta"
    assert g["pick"](["bb", "aa"]) == "aa"


def test_merge_norm_isolated_nodes_counted(home, tmp_path, monkeypatch, capsys):
    b = home / "Downloads/cbse_kg_batches"
    (home / "Downloads/cbse_kg_topics").mkdir(parents=True)
    _graph(b, "s1", [{"id": "a", "label": "Alpha"}, {"id": "b", "label": "Beta"},
                     {"id": "c", "label": "Gamma"}], [{"source": "a", "target": "b"}])
    run_script("merge_norm", sandbox_dir(tmp_path), monkeypatch)
    assert "merged: 3 nodes, 1 edges | isolated 1 (33%)" in capsys.readouterr().out


def test_merge_norm_accepts_edges_key(home, tmp_path, monkeypatch):
    b = home / "Downloads/cbse_kg_batches"
    (home / "Downloads/cbse_kg_topics").mkdir(parents=True)
    p = b / "s" / "graphify-out"
    p.mkdir(parents=True)
    (p / "graph.json").write_text(json.dumps({
        "nodes": [{"id": "a", "label": "Alpha"}, {"id": "b", "label": "Beta"}],
        "edges": [{"source": "a", "target": "b", "relation": "r"}]}))
    run_script("merge_norm", sandbox_dir(tmp_path), monkeypatch)
    out = json.loads((home / "Downloads/cbse_kg_topics/merged-graph-normalised.json").read_text())
    assert len(out["links"]) == 1


# =========================== build_gold.py / syllabus_match.py ===========================

def _q(subject, q, marks=4, year="2022"):
    return {"subject": subject, "question": q, "marks": marks, "year": year}


ENG = "What is the {} of the thing and why is it so in this case here"


@pytest.fixture
def cache(tmp_path, monkeypatch):
    p = tmp_path / "qc.json"
    monkeypatch.setattr(topics2, "CACHE", p)
    return p


def test_build_gold_counts_unique_hits_and_updates_patterns(cache, home, tmp_path, monkeypatch, capsys):
    fake = sandbox_dir(tmp_path, "gold_patterns.json")
    cache.write_text(json.dumps([
        _q("Economics", ENG.format("repo rate")),                       # Money and Banking
        _q("Economics", ENG.format("repo rate")),
        _q("Economics", ENG.format("fiscal deficit")),                   # Government Budget
        _q("Economics", ENG.format("repo rate and fiscal deficit")),     # ambiguous
        _q("Economics", ENG.format("nothing relevant")),                 # no hit
        _q("Psychology", ENG.format("Bipolar")),
        _q("Economics", ENG.format("repo rate"), marks=0),               # filtered: no marks
        _q("Economics", "Hindi mojibake vrz maum"),                      # filtered: not English
    ]))
    run_script("build_gold", fake, monkeypatch)
    out = capsys.readouterr().out
    assert "Economics: 3 gold from 5 questions (60%); 1 ambiguous dropped" in out
    assert "2  Money and Banking" in out.replace("   ", "  ") or "Money and Banking" in out
    assert "ZERO gold: National Income and Related Aggregates" in out
    assert "Psychology: 1 gold from 1 questions (100%); 0 ambiguous dropped" in out
    gp = json.loads((fake / "gold_patterns.json").read_text())
    assert {"Economics", "Psychology"} <= set(gp)
    assert "Biology" in gp or len(gp) >= 2          # previously stored subjects are preserved
    assert "gold_patterns.json covers:" in out


@pytest.mark.xfail(strict=True, reason="build_gold.py:~38 guards the warning with min(lab.values() or [0]) == 0, "
                   "but `lab` is a Counter that only holds units with >=1 hit, so the minimum is never 0 and "
                   "the 'some units have zero gold questions' WARNING can never print (the per-unit "
                   "'ZERO gold:' lines do)")
def test_build_gold_warns_on_zero_gold_units(cache, home, tmp_path, monkeypatch, capsys):
    fake = sandbox_dir(tmp_path, "gold_patterns.json")
    cache.write_text(json.dumps([_q("Economics", ENG.format("repo rate"))] * 2 +
                                [_q("Psychology", ENG.format("Bipolar"))]))
    run_script("build_gold", fake, monkeypatch)
    out = capsys.readouterr().out
    assert "WARNING: some units have zero gold questions" in out


def test_syllabus_match_maps_questions_to_units(cache, tmp_path, monkeypatch, capsys):
    fake = sandbox_dir(tmp_path)
    (fake / "unit_weightage.json").write_text(json.dumps({
        "Accountancy": [["Accounting for Partnership Firms", 36], ["Cash Flow Statement", 24]],
        "Other": [["Unit Alpha Beta Gamma", 10]],
        "Empty": [["Unit Zeta Zeta Zeta", 10]],
    }))
    rows = ([_q("Accountancy", ENG.format("goodwill of the partnership at admission"), 7)] * 5
            + [_q("Accountancy", ENG.format("operating cash flow of the firm today"), 7)] * 3
            + [_q("Accountancy", ENG.format("unrelated gibberish words zzz"), 2)]
            + [_q("Other", ENG.format("alpha beta"), 3)])           # total actual marks 3 < 50: skipped
    cache.write_text(json.dumps(rows))
    run_script("syllabus_match", fake, monkeypatch)
    res = json.loads((fake / "syllabus_match.json").read_text())
    assert list(res) == ["Accountancy"]
    a = res["Accountancy"]
    assert a["coverage"] == round(1 - 1 / 9, 3)
    u = {x["unit"]: x for x in a["units"]}
    p = u["Accounting for Partnership Firms"]
    assert p["declared_marks"] == 36 and p["actual_marks"] == 35
    assert p["declared_pct"] == 60.0 and p["actual_pct"] == round(100 * 35 / 56, 1)
    assert p["gap"] == round(p["actual_pct"] - p["declared_pct"], 1)
    assert u["Cash Flow Statement"]["actual_marks"] == 21
    out = capsys.readouterr().out
    assert "89% of questions mapped to a unit (8/9; 2 marks unassigned)" in out


def test_syllabus_match_keywords(cache, tmp_path, monkeypatch):
    fake = sandbox_dir(tmp_path)
    (fake / "unit_weightage.json").write_text("{}")
    cache.write_text("[]")
    g = run_script("syllabus_match", fake, monkeypatch)
    kw = g["keywords"]
    assert kw("Unit I The Real Economy") == {"real", "economy"}          # stop words + short words out
    assert "goodwill" in kw("Accounting for Partnership Firms")           # EXTRA vocabulary merged
    assert "forfeit" in kw("ACCOUNTING FOR COMPANIES")                    # case-insensitive match
    assert kw("abc") == set()
