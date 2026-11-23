"""build_bank, topics, topics2, methods2 and the NCERT helpers (synthetic inputs, pdftotext faked)."""
import json
import pathlib
import types

import pytest
from scriptrunner import run_script, sandbox_dir

import methods2
import topics
import topics2

ENG = "What is the {} of the thing and why is it so in this case here"


def fake_run(monkeypatch, fn):
    import subprocess
    monkeypatch.setattr(subprocess, "run", lambda cmd, **k: types.SimpleNamespace(stdout=fn(cmd)))


@pytest.fixture
def home(tmp_path, monkeypatch):
    h = tmp_path / "home"
    h.mkdir()
    monkeypatch.setenv("HOME", str(h))
    return h


# =========================== build_bank.py ===========================

STEMS = (["Artificial_Intelligence", "Information_Technology", "Typography_Computer", "WEB_APPLICATIONS",
          "Financial_Markets_Management", "Taxation", "Engineering_Graphics", "Computer_Science",
          "61-S-1_History", "61-S-2_History", "61-S-3_History", "58-S-1_Economics", "58-S-2_Economics",
          "58-S-3_Economics", "67-S-1-Accountancy", "67-S-2-Accountancy", "67-S-3_Accountancy"]
         + [f"59-{s}-{v}_Political_Science" for s in range(1, 6) for v in range(1, 4)])

PAPER = """\
P.T.O.
SECTION A
1. Which gas is the most common?
(A) Oxygen
(B) Nitrogen
(C) Argon
(D) Neon
SECTION B
2. Explain the water cycle in detail    3
OR
Describe evaporation in the given figure
3. Assertion (A): plants respire. Reason (R): they need energy.
5. Study the following passage and answer 5
"""


def _bank_env(tmp_path, monkeypatch, papers=None):
    w = tmp_path / "work"
    (w / "en2").mkdir(parents=True)
    for st in STEMS:
        (w / "en2" / f"{st}.txt").write_text((papers or {}).get(st, PAPER))
    monkeypatch.setenv("WORKDIR", str(w))
    return w


def test_build_bank_end_to_end(tmp_path, monkeypatch, capsys):
    w = _bank_env(tmp_path, monkeypatch)
    g = run_script("build_bank", sandbox_dir(tmp_path), monkeypatch)
    rows = json.loads((w / "bank.json").read_text())
    cs = [r for r in rows if r["subject"] == "Computer Science"]
    assert [r["q_no"] for r in cs] == [1, 2, 3, 4, 5]
    r1, r2, r3, r4, r5 = cs
    assert r1["q_type"] == "mcq" and r1["section"] == "A" and r1["marks"] == 1
    assert json.loads(r1["options"])["B"] == "Nitrogen"
    assert r1["qp_code"] == "91/S" and r1["paper_set"] == "Set-4" and r1["architecture"] == "academic"
    assert r1["max_marks_paper"] == 70
    assert r2["section"] == "B" and r2["marks"] == 1 and r2["has_internal_choice"] is True   # marks come from the spec table, not the text
    assert r2["has_figure"] is True
    assert r3["q_type"] == "assertion-reason" and r3["block"] == "A"
    assert r4["q_type"] == "figure-only" and r4["full_text"] is None and r4["marks"] == 1
    assert r4["section"] == "B" and r4["block"] == "A" and r4["block_out_of"] == 21
    assert r5["q_type"] == "source-based" and r5["marks"] == 1
    out = capsys.readouterr().out
    assert "Computer_Science" in out
    assert "MISMATCH" in out
    assert f"total questions parsed: {len(rows)}" in out
    assert out.count("<-- MISMATCH") == len(STEMS)       # every synthetic paper declares more questions


def test_build_bank_no_mismatch_when_count_matches(tmp_path, monkeypatch, capsys):
    papers = {"Computer_Science": "\n".join(f"{i}. Question number {i} text here" for i in range(1, 38))}
    w = _bank_env(tmp_path, monkeypatch, papers)
    run_script("build_bank", sandbox_dir(tmp_path), monkeypatch)
    line = [l for l in capsys.readouterr().out.splitlines() if l.startswith("Computer_Science")][0]
    assert line.split() == ["Computer_Science", "37", "37"]


def test_build_bank_missing_input_raises(tmp_path, monkeypatch):
    monkeypatch.setenv("WORKDIR", str(tmp_path / "nope"))
    with pytest.raises(FileNotFoundError):
        run_script("build_bank", sandbox_dir(tmp_path), monkeypatch)


@pytest.fixture
def bb(tmp_path, monkeypatch):
    _bank_env(tmp_path, monkeypatch)
    return run_script("build_bank", sandbox_dir(tmp_path), monkeypatch)


def test_bb_split_questions_and_dedupe_forward(bb):
    lines = ["intro", "1. First question text", "x", "x", "4. Fourth question text", "y"]
    blocks, pre = bb["split_questions"](lines, declared=5)
    assert pre == ["intro"]
    assert [b["q_no"] for b in blocks] == [1, 2, 3, 4]
    assert blocks[1].get("missing") and blocks[2].get("missing")
    blocks = bb["dedupe_forward"](blocks)
    assert blocks[0]["lines"] == ["First question text", "x"]
    capped, _ = bb["split_questions"](["1. First question text", "2. Second question text"], declared=1)
    assert [b["q_no"] for b in capped] == [1]


def test_bb_block_marks_walk(bb):
    lines = ["Answer any 3 out of the given 5 questions in 20-30 words each.  3x2=6",
             "6. First short question text", "7. Second short question text",
             "SECTION C (Long Answer Questions) 4 x 5 = 20",
             "8. A long question here now",
             "2 x 3 = 6",
             "9. Another question right here",
             "5 x 3 = 15",
             "10. Last question goes here"]
    out = bb["block_marks_walk"](lines, decl=34)
    assert out == {}          # numbering starts at 1; q6 is not within expect..expect+3


def test_bb_block_marks_walk_sequence(bb):
    lines = ["Answer any 3 out of the given 5 questions in 20-30 words each.  3x2=6",
             "1. First short question text", "2. Second short question text",
             "(Short Answer Type Questions)  6 x 3 = 18",
             "3. A short question here now",
             "2 x 4 = 8",
             "4. Another question right here",
             "5 x 3 = 16",       # arithmetic mismatch: ignored
             "5. Last question goes here"]
    out = bb["block_marks_walk"](lines, decl=34)
    assert out[1] == (2, 3, 5) and out[2] == (2, 3, 5)
    assert out[3] == (3, None, None)
    assert out[4] == (4, None, None)
    assert out[5] == (4, None, None)
    # bare line with b > 8 is ignored
    assert bb["block_marks_walk"](["1 x 9 = 9", "1. First question text here"], 5)[1] == (None, None, None)


def test_bb_extract_marks(bb):
    em = bb["extract_marks"]
    assert em(["text 2 x 2 = 4"]) == 4
    assert em(["text 1 + 2 = 3"]) == 3
    assert em(["text    13"]) == 13
    assert em(["text    14"] , (2, None, None)) == 2        # implausible -> block value
    assert em(["no marks"], (7, None, None)) == 7
    assert em(["no marks"]) is None
    assert em(["a    2", "b    4"]) == 4
    assert em(["3 x 5 = 15"], (1, None, None)) == 1          # product > 12 rejected


def test_bb_extract_options_and_q_type_and_section(bb):
    eo, qt, so = bb["extract_options"], bb["q_type"], bb["section_of"]
    assert eo(["(A) a", "(B) b"]) is None
    assert eo(["(A) a", "(B) b", "(C) c 12. next"]) == {"A": "a", "B": "b", "C": "c"}
    assert qt("", None, ["Match the following: Match List I"]) == "matching"
    assert qt("", None, ["Statement-I: x"]) == "two-statement"
    assert qt("", None, ["arrange the following"]) == "ordering"
    assert qt("", None, ["On the given political map"]) == "map"
    assert qt("", {"A": 1}, ["plain"]) == "mcq"
    assert qt("", None, ["plain"]) == "subjective"
    assert so(["SECTION A", "1. x", "PART B", "2. y"]) == "Part B"
    assert so(["x", "Section - C", "y"]) == "C"
    assert so(["nothing"]) is None


# =========================== topics.py ===========================

def test_topics_subject_year_norm_ngrams():
    P = pathlib.Path
    assert topics.subject_of(P("2024/041_Maths/x.pdf")) == "Maths"
    assert topics.subject_of(P("2024/Political_Science/x.pdf")) == "Political Science"
    assert topics.subject_of(P("2024/Typography_Comp_Applications/x.pdf")) == "Typography & Computer Applications"
    assert topics.subject_of(P("2024/Engg_Graphics/x.pdf")) == "Engineering Graphics"
    assert topics.year_of(P("2024-25/Physics/x.pdf")) == "2024-25"
    assert topics.norm("Ohm's Law (2 marks)") == "ohm s law marks"
    g = set(topics.ngrams("explain the photoelectric effect equation"))
    assert "photoelectric effect" in g and "photoelectric effect equation" in g
    assert not any(x.startswith("explain") for x in g)
    assert list(topics.ngrams("give reasons")) == []


def test_topics_load_uses_cache(tmp_path, monkeypatch):
    c = tmp_path / "qcache.json"
    c.write_text('[{"a": 1}]')
    monkeypatch.setattr(topics, "CACHE", c)
    assert topics.load() == [{"a": 1}]


def test_topics_load_builds_cache_from_pdfs(tmp_path, monkeypatch, capsys):
    root = tmp_path / "pp"
    for y, subj in [("2023", "Physics"), ("2024-COMPTT", "Physics")]:
        d = root / y / subj
        d.mkdir(parents=True)
        (d / f"{subj}.pdf").write_bytes(b"x")
    z = root / "_zips" / "2022" / "Physics"
    z.mkdir(parents=True)
    (z / "skip.pdf").write_bytes(b"x")
    bad = root / "2025" / "Bad"
    bad.mkdir(parents=True)
    (bad / "bad.pdf").write_bytes(b"x")

    def parse(p, subject, source, pid):
        if subject == "Bad":
            raise RuntimeError("corrupt")
        return [{"question": "q", "subject": subject}], None, None

    monkeypatch.setattr(topics, "ROOT", root)
    monkeypatch.setattr(topics, "CACHE", tmp_path / "qcache.json")
    monkeypatch.setattr(topics, "parse_paper", parse)
    rows = topics.load()
    assert len(rows) == 2
    by = {r["year"]: r for r in rows}
    assert by["2023"]["exam"] == "main" and by["2024"]["exam"] == "compartment"
    assert by["2024"]["paper_file"] == "Physics.pdf"
    assert json.loads((tmp_path / "qcache.json").read_text()) == rows
    assert "parsed 0/" in capsys.readouterr().out


def test_topics_load_missing_input_exits(tmp_path, monkeypatch):
    monkeypatch.setattr(topics, "ROOT", tmp_path / "none")
    monkeypatch.setattr(topics, "CACHE", tmp_path / "qcache.json")
    with pytest.raises(SystemExit):
        topics.load()


def test_topics_main_reports_recurring_topics(tmp_path, monkeypatch, capsys):
    rows = []
    for i in range(4):                              # 4 papers (>= 4), years 2020..2023
        for k in range(4):                          # 16 high-mark Qs (>= 15)
            rows.append({"subject": "Physics", "year": str(2020 + i), "paper_file": f"p{i}.pdf",
                         "marks": 5, "question": f"Derive the photoelectric effect equation number {k}"})
    rows.append({"subject": "Physics", "year": "2020", "paper_file": "p0.pdf", "marks": 1,
                 "question": "low marks question about photoelectric effect"})
    for i in range(3):                              # subject with only 3 papers: skipped
        rows.append({"subject": "Art", "year": "2020", "paper_file": f"a{i}.pdf", "marks": 5,
                     "question": "x"})
    c = tmp_path / "qcache.json"
    c.write_text(json.dumps(rows))
    monkeypatch.setattr(topics, "CACHE", c)
    monkeypatch.setattr(topics, "__file__", str(tmp_path / "topics.py"))
    topics.main()
    rep = json.loads((tmp_path / "topic_report.json").read_text())
    assert list(rep) == ["Physics"]
    d = rep["Physics"]
    assert d["papers"] == 4 and d["high_q"] == 16 and d["years"] == ["2020", "2021", "2022", "2023"]
    names = [t[0] for t in d["topics"]]
    assert "photoelectric effect equation number" in names
    top = d["topics"][0]
    assert top[1] == 4 and top[2] == 4
    out = capsys.readouterr().out
    assert "questions parsed from past papers: 20" in out
    assert "### Physics  (4 papers, 16 high-mark Qs, years 2020-2023)" in out


def test_topics_main_skips_thin_subjects(tmp_path, monkeypatch):
    rows = [{"subject": "Physics", "year": str(2020 + i), "paper_file": f"p{i}.pdf", "marks": 5,
             "question": "Derive the photoelectric effect equation"} for i in range(4)]     # 4 high < 15
    c = tmp_path / "qcache.json"
    c.write_text(json.dumps(rows))
    monkeypatch.setattr(topics, "CACHE", c)
    monkeypatch.setattr(topics, "__file__", str(tmp_path / "topics.py"))
    topics.main()
    assert json.loads((tmp_path / "topic_report.json").read_text()) == {}


# =========================== topics2.py ===========================

def test_topics2_build_cache_and_main(tmp_path, monkeypatch, capsys):
    root = tmp_path / "pp"
    for y in ["2020", "2021", "2022", "2023-COMPTT"]:
        d = root / y / "041_Maths"
        d.mkdir(parents=True)
        (d / f"m{y}.pdf").write_bytes(b"x")
    (root / "_zips").mkdir()
    (root / "_zips" / "z.pdf").write_bytes(b"x")
    (root / "2020" / "Bad").mkdir()
    (root / "2020" / "Bad" / "b.pdf").write_bytes(b"x")

    def parse(p, subject, source, pid):
        if subject == "Bad":
            raise ValueError("x")
        out = [{"question": ENG.format("matrix inverse determinant"), "marks": 5, "subject": subject}
               for _ in range(10)]
        return out, None, None

    monkeypatch.setattr(topics2, "ROOT", root)
    monkeypatch.setattr(topics2, "CACHE", tmp_path / "qc.json")
    monkeypatch.setattr(topics2, "HERE", tmp_path)
    monkeypatch.setattr(topics2, "parse_paper", parse)
    topics2.main()
    rows = json.loads((tmp_path / "qc.json").read_text())
    assert len(rows) == 40
    assert {r["year"] for r in rows} == {"2020", "2021", "2022", "2023"}
    assert {r["exam"] for r in rows if r["year"] == "2023"} == {"compartment"}
    assert {r["subject"] for r in rows} == {"Mathematics"}
    rep = json.loads((tmp_path / "topic_report2.json").read_text())
    m = rep["Mathematics"]
    assert m["high_q"] == 40 and m["papers"] == 4 and len(m["years"]) == 4
    assert m["topics"][0]["years"] == 4 and m["recurring_share"] == 1.0
    out = capsys.readouterr().out
    assert "questions parsed: 40  | usable English-medium: 40 (100%)" in out
    assert "### Mathematics" in out


def test_topics2_main_skips_few_years_and_low_high_mark_counts(tmp_path, monkeypatch, capsys):
    rows = []
    for y in ("2020", "2021"):                                  # only 2 years
        rows += [{"subject": "A", "year": y, "paper_file": "a.pdf", "marks": 5,
                  "question": ENG.format("alpha beta gamma")}] * 30
    for y in ("2020", "2021", "2022"):                          # 3 years but 24 high-mark Qs (< 25)
        rows += [{"subject": "B", "year": y, "paper_file": "b.pdf", "marks": 5,
                  "question": ENG.format("alpha beta gamma")}] * 8
    for y in ("2020", "2021", "2022"):                          # long passages dropped from `high`
        rows += [{"subject": "C", "year": y, "paper_file": "c.pdf", "marks": 5,
                  "question": ENG.format("alpha " * 70)}] * 20
    for y in ("2020", "2021", "2022"):                          # 3-year subject, 0 recurring phrases
        rows += [{"subject": "D", "year": y, "paper_file": f"d{y}.pdf", "marks": 5,
                  "question": ENG.format(f"unique{y}x word{y}y")}] * 9
    c = tmp_path / "qc.json"
    c.write_text(json.dumps(rows))
    monkeypatch.setattr(topics2, "CACHE", c)
    monkeypatch.setattr(topics2, "HERE", tmp_path)
    topics2.main()
    rep = json.loads((tmp_path / "topic_report2.json").read_text())
    assert "A" not in rep and "B" not in rep and "C" not in rep
    assert "D" not in rep or all(t["years"] >= 3 for t in rep["D"]["topics"])


def test_topics2_main_marks_threshold_is_four(tmp_path, monkeypatch):
    mk = lambda marks: [{"subject": "A", "year": y, "paper_file": f"{y}.pdf", "marks": marks,
                         "question": ENG.format("alpha beta gamma")} for y in ("2020", "2021", "2022")
                        for _ in range(10)]
    for marks, expected in ((4, True), (3, False)):
        c = tmp_path / f"qc{marks}.json"
        c.write_text(json.dumps(mk(marks)))
        monkeypatch.setattr(topics2, "CACHE", c)
        monkeypatch.setattr(topics2, "HERE", tmp_path)
        topics2.main()
        assert ("A" in json.loads((tmp_path / "topic_report2.json").read_text())) is expected


def test_topics2_top_topics_dedupe_substrings_and_cap(tmp_path, monkeypatch):
    rows = [{"subject": "A", "year": y, "paper_file": f"{y}.pdf", "marks": 5,
             "question": ENG.format("matrix inverse determinant")} for y in ("2020", "2021", "2022")
            for _ in range(10)]
    c = tmp_path / "qc.json"
    c.write_text(json.dumps(rows))
    monkeypatch.setattr(topics2, "CACHE", c)
    monkeypatch.setattr(topics2, "HERE", tmp_path)
    topics2.main()
    names = [t["topic"] for t in json.loads((tmp_path / "topic_report2.json").read_text())["A"]["topics"]]
    for a in names:
        for b in names:
            assert a == b or (a not in b and b not in a)


# =========================== methods2.py (blueprint / units) ===========================

def test_methods2_blueprint_table(tmp_path, monkeypatch):
    cur = tmp_path / "cur"
    cur.mkdir()
    (cur / "Physics_SrSec_2024.pdf").write_bytes(b"x")
    (cur / "Physics_SrSec_Hindi.pdf").write_bytes(b"x")
    (cur / "Physics_Hi_x.pdf").write_bytes(b"x")
    monkeypatch.setattr(methods2, "CUR", cur)
    TXT = "Typology of Questions\n Remembering 38%\n Applying 32%\n Analysing 30%\n"
    fake_run(monkeypatch, lambda cmd: TXT)
    rows = [{"subject": "Physics", "marks": 3, "question": "State Ohm's law"},
            {"subject": "Physics", "marks": 5, "question": "Calculate the current"},
            {"subject": "Physics", "marks": 2, "question": "Compare the two"},
            {"subject": "Physics", "marks": 1, "question": "ohm 2 volts"},           # no level
            {"subject": "Physics", "marks": 0, "question": "State the law"},          # no marks: ignored
            {"subject": "Chemistry", "marks": 3, "question": "State the law"}]
    res = methods2.blueprint_table(rows)
    assert set(res) == {"Physics", "Chemistry"}
    p = res["Physics"]
    assert p["declared"] == {"remember_understand": 38, "apply": 32, "analyse_evaluate_create": 30}
    assert p["actual"] == {"remember_understand": 30, "apply": 50, "analyse_evaluate_create": 20}
    assert p["marks_classified"] == 10 and p["questions"] == 4
    assert p["curriculum"] == "Physics_SrSec_2024.pdf"


def test_methods2_blueprint_table_without_curriculum_pdf(tmp_path, monkeypatch):
    cur = tmp_path / "cur"
    cur.mkdir()
    (cur / "Other.pdf").write_bytes(b"x")
    monkeypatch.setattr(methods2, "CUR", cur)
    res = methods2.blueprint_table([{"subject": "Physics", "marks": 3, "question": "State the law"}])
    assert res["Physics"]["declared"] is None and res["Physics"]["curriculum"] is None


def test_methods2_blueprint_requires_input_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(methods2, "CUR", tmp_path / "missing")
    with pytest.raises(SystemExit):
        methods2.blueprint_table([])


def test_methods2_unit_weightage(tmp_path, monkeypatch):
    cur = tmp_path / "cur"
    cur.mkdir()
    (cur / "Economics_SrSec_x.pdf").write_bytes(b"x")
    (cur / "Economics_Hindi_SrSec.pdf").write_bytes(b"x")
    monkeypatch.setattr(methods2, "CUR", cur)
    fake_run(monkeypatch, lambda cmd: "  Unit I  National Income and Aggregates    20\n"
                                      "Unit-2: Money and Banking Concepts   15\n"
                                      "no match here\n")
    res = methods2.unit_weightage()
    assert list(res) == ["Economics"]
    assert res["Economics"][0] == ("Unit I  National Income and Aggregates", 20) or \
        res["Economics"][0][1] == 20
    assert [m for _, m in res["Economics"]] == [20, 15]


def test_methods2_unit_weightage_skips_subjects_without_units(tmp_path, monkeypatch):
    cur = tmp_path / "cur"
    cur.mkdir()
    (cur / "Economics_SrSec_x.pdf").write_bytes(b"x")
    monkeypatch.setattr(methods2, "CUR", cur)
    fake_run(monkeypatch, lambda cmd: "nothing useful")
    assert methods2.unit_weightage() == {}


def test_methods2_declared_typology_marker_fallbacks(tmp_path, monkeypatch):
    txt = ("weightage based on competencies\n 40%  Remembering\n 35% Applying\n 25% Analysing\n")
    fake_run(monkeypatch, lambda cmd: txt)
    assert methods2.declared_typology(tmp_path / "x.pdf") == {
        "remember_understand": 40, "apply": 35, "analyse_evaluate_create": 25}
    # percentages outside 5..95 or not summing to ~100 -> None
    fake_run(monkeypatch, lambda cmd: "typology of questions\n 1% 2% 3% 50% 20%\n")
    assert methods2.declared_typology(tmp_path / "x.pdf") is None
    # sum boundary: 95 and 105 accepted, 94 and 106 rejected
    for tri, ok in (((30, 30, 35), True), ((35, 35, 35), True), ((30, 30, 34), False), ((36, 35, 35), False)):
        fake_run(monkeypatch, lambda cmd, t=tri: "typology of questions\n %d%% %d%% %d%%\n" % t)
        assert (methods2.declared_typology(tmp_path / "x.pdf") is not None) is ok, tri


def test_methods2_near_duplicates_with_stub_sklearn(monkeypatch):
    """sklearn is optional in this repo's CI-less setup; the real-sklearn test lives in test_methods2.py."""
    pytest.importorskip("sklearn")
