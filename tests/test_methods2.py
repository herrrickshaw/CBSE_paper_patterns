"""Bloom classifier, TF-IDF cross-year near-duplicates and blueprint
percentage parsing in scripts/methods2.py (pdftotext mocked)."""
import types

import methods2 as m


def test_bloom_highest_level_wins():
    assert m.bloom_of("State Ohm's law.") == "remember_understand"
    assert m.bloom_of("Calculate the current in the circuit.") == "apply"
    assert m.bloom_of("Define resistivity and justify your answer.") == "analyse_evaluate_create"
    assert m.bloom_of("Calculate and compare the two currents.") == "analyse_evaluate_create"
    assert m.bloom_of("Ohm 2 volts") is None


def _row(subject, year, q, marks=3):
    return {"subject": subject, "year": year, "question": q, "marks": marks}


def test_near_duplicates_cross_year_only():
    base = "Explain the working principle of a transformer with a neat labelled diagram of core"
    rows = [_row("Physics", "2022", base), _row("Physics", "2024", base + " windings"),
            _row("Physics", "2022", base + " windings")]
    # filler so the subject has >= 40 eligible questions with shared vocabulary (min_df=2)
    for i in range(40):
        rows.append(_row("Physics", str(2000 + i), f"Describe experiment number {'abcdefghij'[i % 10]} about optics lens focal length measurement setup {'xyz'[i % 3]}"))
    dups = m.near_duplicates(rows, min_sim=0.95)
    pairs = {(d["year_a"], d["year_b"]) for d in dups if "transformer" in d["q_a"]}
    assert pairs and all(a != b for a, b in pairs)
    assert all(d["year_a"] != d["year_b"] for d in dups)


def test_near_duplicates_skips_small_subjects_and_instructions():
    rows = [_row("Tiny", "2022", "Explain the working principle of a transformer in detail please")] * 10
    assert m.near_duplicates(rows) == []
    assert m.INSTRUCTION.search("Answer any four of the following questions")


def test_declared_typology_parses_first_triple_summing_to_100(monkeypatch, tmp_path):
    txt = ("Question Paper Design\n  Typology of Questions  Marks  Percentage\n"
           "Remembering, Understanding 27 38%\nApplying 22 32%\nAnalysing 21 30%\nTotal 70 100%\n")
    monkeypatch.setattr(m.subprocess, "run", lambda *a, **k: types.SimpleNamespace(stdout=txt))
    assert m.declared_typology(tmp_path / "x.pdf") == {
        "remember_understand": 38, "apply": 32, "analyse_evaluate_create": 30}
    monkeypatch.setattr(m.subprocess, "run", lambda *a, **k: types.SimpleNamespace(stdout="no table"))
    assert m.declared_typology(tmp_path / "x.pdf") is None
