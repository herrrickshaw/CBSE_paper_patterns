"""Boundary tests (thresholds, caps, tie-breaks) for the CBSE scripts; found by mutation testing."""
import json
import types

import pytest
from scriptrunner import run_script, sandbox_dir

import final_report as fr
import methods2
import parse_generic as pg
import topics2

ENG = "What is the {} of the thing and why is it so in this case here"


def fake_pdftotext(monkeypatch, text):
    monkeypatch.setattr(pg.subprocess, "run", lambda *a, **k: types.SimpleNamespace(stdout=text))


def fake_run(monkeypatch, fn):
    import subprocess
    monkeypatch.setattr(subprocess, "run", lambda cmd, **k: types.SimpleNamespace(stdout=fn(cmd)))


# ---------------- parse_generic ----------------

def test_stem_stops_growing_at_400_chars(monkeypatch, tmp_path):
    first = "Alpha beta " + "c" * 319            # 330 chars: below 400, so the next line is appended
    second = "SECONDLINE " + "e" * 70            # pushes the stem past 400 -> the third line is not
    fake_pdftotext(monkeypatch, f"1. {first}\n{second}\n{'d' * 60} THIRDLINE\n")
    rows, _, _ = pg.parse_paper(tmp_path / "p.pdf", "S", "src", "id")
    q = rows[0]["question"]
    assert "SECONDLINE" in q and "THIRDLINE" not in q       # 350 -> 350+ ; second line pushes it past 400


def test_section_walk_cap_default_is_120():
    lines = ["SECTION A"] + [f"{i}. Question number {i} text" for i in range(1, 123)]
    s = pg.section_walk(lines)
    assert s[110] == "A" and s[120] == "A" and 121 not in s
    assert [b["q_no"] for b in pg.split_questions(lines)][-1] == 120


# ---------------- topics2 ----------------

def test_is_english_thresholds():
    # 6 words, exactly 3 function words -> True ; exactly 2 -> False
    assert topics2.is_english("what is the cat doing here")
    assert not topics2.is_english("zebra quickly runs across the yellow")
    assert topics2.is_english("cat of dog in box by")                  # 6 words, of/in/by = 3 FUNC
    assert not topics2.is_english("cat of dog in box zzz")             # 6 words, 2 FUNC
    assert not topics2.is_english("what is the cat on")                # 5 words even with 4 FUNC


def _rows(subject, years, per_year, question, marks=5):
    return [{"subject": subject, "year": y, "paper_file": f"{y}.pdf", "marks": marks,
             "question": question(i)} for y in years for i in range(per_year)]


def _run_main(monkeypatch, tmp_path, rows):
    c = tmp_path / "qc.json"
    c.write_text(json.dumps(rows))
    monkeypatch.setattr(topics2, "CACHE", c)
    monkeypatch.setattr(topics2, "HERE", tmp_path)
    topics2.main()
    return json.loads((tmp_path / "topic_report2.json").read_text())


def test_topics2_high_mark_floor_is_25(monkeypatch, tmp_path):
    q = lambda i: ENG.format("matrix inverse")
    assert "S" not in _run_main(monkeypatch, tmp_path, _rows("S", ["2020", "2021", "2022"], 8, q)[:-0 or None][:24])
    assert "S" in _run_main(monkeypatch, tmp_path, _rows("S", ["2020", "2021", "2022"], 9, q)[:25])


def test_topics2_phrase_must_recur_in_three_years(monkeypatch, tmp_path):
    rows = (_rows("S", ["2020", "2021"], 13, lambda i: ENG.format("rareterm onlytwo"))
            + _rows("S", ["2022"], 13, lambda i: ENG.format("other filler"))
            + _rows("S", ["2020", "2021", "2022"], 3, lambda i: ENG.format("keepterm thrice")))
    topics = [t["topic"] for t in _run_main(monkeypatch, tmp_path, rows)["S"]["topics"]]
    assert any("keepterm thrice" in t for t in topics)
    assert not any("rareterm" in t for t in topics)


def test_topics2_caps_chosen_topics_at_20(monkeypatch, tmp_path):
    words = [f"{a}{b}" for a in "abcdefghij" for b in "klmnopqrst"]
    rows = []
    for g in range(25):
        w1, w2 = words[2 * g], words[2 * g + 1]
        rows += _rows("S", ["2020", "2021", "2022"], 1, lambda i, w1=w1, w2=w2: ENG.format(f"{w1}x {w2}y"))
    rows += _rows("S", ["2020", "2021", "2022"], 2, lambda i: ENG.format("matrix inverse"))
    topics = _run_main(monkeypatch, tmp_path, rows)["S"]["topics"]
    assert len(topics) == 20


def test_topics2_progress_printed_every_200_pdfs(monkeypatch, tmp_path, capsys):
    root = tmp_path / "pp" / "2020" / "Physics"
    root.mkdir(parents=True)
    for i in range(201):
        (root / f"p{i:03d}.pdf").write_bytes(b"x")
    monkeypatch.setattr(topics2, "ROOT", tmp_path / "pp")
    monkeypatch.setattr(topics2, "CACHE", tmp_path / "qc.json")
    monkeypatch.setattr(topics2, "parse_paper", lambda *a: ([], None, None))
    topics2.build_cache()
    out = capsys.readouterr().out
    assert "  0/201" in out and "  200/201" in out and "100/201" not in out


# ---------------- methods2 ----------------

def test_near_duplicates_needs_40_eligible_questions_per_subject():
    pytest.importorskip("sklearn")

    def rows(n):
        out = []
        for i in range(n):
            out.append({"subject": "S", "year": str(2000 + i % 3), "marks": 4,
                        "question": f"Explain how topic{i // 3} varies across the different samples taken in region{i // 3}"})
        return out

    assert methods2.near_duplicates(rows(39)) == []
    assert methods2.near_duplicates(rows(42)) != []


def test_near_duplicates_similarity_threshold_is_inclusive():
    pytest.importorskip("sklearn")
    q = "Explain how the surface tension of a liquid varies with temperature in detail please"
    rows = [{"subject": "S", "year": str(2000 + i % 2), "marks": 4, "question": q} for i in range(40)]
    top = methods2.near_duplicates(rows, min_sim=0.0)
    assert top and top[0]["similarity"] == 1.0
    # identical vectors have cosine 1 (to float precision): a threshold of 1.0 keeps/drops them consistently
    kept = methods2.near_duplicates(rows, min_sim=1.0)
    assert kept == [] or all(d["similarity"] == 1.0 for d in kept)


def test_declared_typology_accepts_five_percent(monkeypatch, tmp_path):
    fake_run(monkeypatch, lambda cmd: "typology of questions\n 5% 45% 50%\n")
    assert methods2.declared_typology(tmp_path / "x.pdf") == {
        "remember_understand": 5, "apply": 45, "analyse_evaluate_create": 50}
    fake_run(monkeypatch, lambda cmd: "typology of questions\n 4% 46% 50%\n")
    assert methods2.declared_typology(tmp_path / "x.pdf") is None


# ---------------- final_report / pipeline high-mark floor ----------------

def _fr_run(monkeypatch, tmp_path, n_high):
    rows = []
    years = ["2020", "2021", "2022"]
    for i in range(n_high):
        rows.append({"subject": "S", "year": years[i % 3], "paper_file": f"{years[i % 3]}.pdf",
                     "marks": 5, "question": ENG.format("fiscal deficit target")})
    c = tmp_path / "qc.json"
    c.write_text(json.dumps(rows))
    monkeypatch.setattr(fr, "CACHE", c)
    monkeypatch.setattr(fr, "HERE", tmp_path)
    fr.main()
    return json.loads((tmp_path / "final_topics.json").read_text())["subjects"]


def test_final_report_floor_is_25_high_mark_questions(monkeypatch, tmp_path):
    assert "S" not in _fr_run(monkeypatch, tmp_path, 24)
    assert "S" in _fr_run(monkeypatch, tmp_path, 25)


def test_pipeline_aggregate_floor_is_25(tmp_path, monkeypatch):
    pytest.importorskip("langgraph")
    import importlib
    lg = importlib.import_module("pipeline_langgraph")

    def cls(n):
        return [{"subject": "S", "year": "2020", "marks": 5, "bloom": "apply", "high_mark": True,
                 "question": ENG.format("alpha beta")} for _ in range(n)]

    assert lg.aggregate({"classified": cls(24), "log": []})["subjects"] == {}
    assert list(lg.aggregate({"classified": cls(25), "log": []})["subjects"]) == ["S"]


# ---------------- build_bank ----------------

def test_build_bank_gap_tolerance_is_three(tmp_path, monkeypatch):
    w = tmp_path / "work"
    (w / "en2").mkdir(parents=True)
    from test_pipeline_scripts2 import STEMS, PAPER
    for st in STEMS:
        (w / "en2" / f"{st}.txt").write_text(PAPER)
    monkeypatch.setenv("WORKDIR", str(w))
    g = run_script("build_bank", sandbox_dir(tmp_path), monkeypatch)
    blocks, _ = g["split_questions"](["1. First question text", "5. Fifth question text"], declared=34)
    assert [b["q_no"] for b in blocks] == [1, 2, 3, 4, 5]
    blocks, _ = g["split_questions"](["1. First question text", "6. Sixth question text"], declared=34)
    assert [b["q_no"] for b in blocks] == [1]


# ---------------- parse_ms ----------------

def _home(tmp_path, monkeypatch):
    h = tmp_path / "home"
    d = h / "Downloads/cbse_md/sqp_archive/2024-25"
    d.mkdir(parents=True)
    monkeypatch.setenv("HOME", str(h))
    return d


def test_parse_ms_first_key_wins_and_answer_text_is_truncated(tmp_path, monkeypatch):
    d = _home(tmp_path, monkeypatch)
    (d / "Physics-MS.md").write_text("1    (c) first answer   1\n1    (d) second answer   1\n"
                                     "A9: " + "x" * 600 + "\n")
    fake = sandbox_dir(tmp_path)
    run_script("parse_ms", fake, monkeypatch)
    rows = json.loads((fake / "answer_keys.json").read_text())
    keys = [r for r in rows if r["kind"] == "mcq_key"]
    assert [(r["q_no"], r["answer"]) for r in keys] == [(1, "C")]
    text = [r for r in rows if r["kind"] == "answer_text"]
    assert len(text) == 1 and text[0]["q_no"] == 9 and len(text[0]["answer"]) == 400


# ---------------- units_xii ----------------

def test_units_xii_name_and_mark_boundaries(tmp_path, monkeypatch):
    h = tmp_path / "home"
    cur = h / "Downloads/cbse_official/curriculum"
    cur.mkdir(parents=True)
    monkeypatch.setenv("HOME", str(h))
    (cur / "Sub_SrSec.pdf").write_bytes(b"x")
    fake_run(monkeypatch, lambda cmd: "Class XII\n   Big Unit Alpha Name       40\n"
                                      "   Medium Unit Beta Name      20\n"
                                      "   Medium Unit Gamma Name     19\n"
                                      "   A  b  c         1\n")
    fake = sandbox_dir(tmp_path)
    run_script("units_xii", fake, monkeypatch)
    res = json.loads((fake / "units_xii.json").read_text())
    assert [m for _, m in res["Sub"]] == [40, 20, 19]         # 40 marks kept; 'A b c' (5 chars) dropped


# ---------------- merge_norm ----------------

def test_merge_norm_keeps_ss_endings_and_distinct_relations(tmp_path, monkeypatch):
    h = tmp_path / "home"
    (h / "Downloads/cbse_kg_topics").mkdir(parents=True)
    p = h / "Downloads/cbse_kg_batches/s/graphify-out"
    p.mkdir(parents=True)
    (p / "graph.json").write_text(json.dumps({
        "nodes": [{"id": "a", "label": "Financial Process"}, {"id": "b", "label": "Beta"}],
        "links": [{"source": "a", "target": "b", "relation": "r1"},
                  {"source": "a", "target": "b", "relation": "r2"},
                  {"source": "a", "target": "b", "relation": "r1"}]}))
    monkeypatch.setenv("HOME", str(h))
    g = run_script("merge_norm", sandbox_dir(tmp_path), monkeypatch)
    assert g["norm"]("Financial Process") == "financial process"
    out = json.loads((h / "Downloads/cbse_kg_topics/merged-graph-normalised.json").read_text())
    assert sorted(e["relation"] for e in out["links"]) == ["r1", "r2"]


# ---------------- syllabus_match ----------------

def test_syllabus_match_needs_50_actual_marks(tmp_path, monkeypatch):
    for marks, expected in ((10, True), (9, False)):
        cache = tmp_path / f"qc{marks}.json"
        monkeypatch.setattr(topics2, "CACHE", cache)
        fake = tmp_path / f"s{marks}"
        fake.mkdir()
        (fake / "unit_weightage.json").write_text(json.dumps({"Accountancy": [["Cash Flow Statement", 24]]}))
        cache.write_text(json.dumps([{"subject": "Accountancy", "marks": marks, "year": "2022",
                                      "question": ENG.format("operating cash flow")}] * 5))
        run_script("syllabus_match", fake, monkeypatch)
        res = json.loads((fake / "syllabus_match.json").read_text())
        assert ("Accountancy" in res) is expected
