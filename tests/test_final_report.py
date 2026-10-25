"""Formula/mojibake filters and the repetition index of scripts/final_report.py,
run end-to-end on a synthetic question cache written to tmp_path."""
import json
import string

import final_report as fr


def test_is_formula_and_mojibake():
    assert fr.is_formula("find value")
    assert not fr.is_formula("find focal length")
    assert fr.looks_mojibake("vrz maum")
    assert not fr.looks_mojibake("focal length")


def _word(i, tag):
    a, b = string.ascii_lowercase[i // 26], string.ascii_lowercase[i % 26]
    return f"{tag}{a}{b}on"


def _q(i, tag):
    # >= 6 words, >= 3 function words (English gate), unique content words
    w = [_word(i, tag + x) for x in "pqrs"]
    return f"What is the {w[0]} {w[1]} of the {w[2]} {w[3]} and why is it so?"


def _run(tmp_path, monkeypatch, rows):
    cache = tmp_path / "qcache.json"
    cache.write_text(json.dumps(rows))
    monkeypatch.setattr(fr, "CACHE", cache)
    monkeypatch.setattr(fr, "HERE", tmp_path)
    fr.main()
    return json.loads((tmp_path / "final_topics.json").read_text())


def test_repetition_index_counts_every_recurring_content_phrase(tmp_path, monkeypatch, capsys):
    # 30 content questions each repeated in 2022/2023/2024 (recurring in 3 years)
    # plus 10 one-off questions. Docstring definition: share of high-mark marks
    # on a phrase recurring in >= 3 years = 450 / 500 = 0.9.
    rows = []
    for i in range(30):
        for y in ("2022", "2023", "2024"):
            rows.append({"subject": "Physics", "year": y, "question": _q(i, "r"),
                         "marks": 5, "paper_file": f"p{y}.pdf"})
    for i in range(10):
        rows.append({"subject": "Physics", "year": "2022", "question": _q(i, "u"),
                     "marks": 5, "paper_file": "p2022.pdf"})
    out = _run(tmp_path, monkeypatch, rows)
    s = out["subjects"]["Physics"]
    assert s["high_marks"] == 500
    assert s["repetition_index"] == 0.9


def test_subject_with_too_few_years_is_skipped(tmp_path, monkeypatch, capsys):
    rows = [{"subject": "Art", "year": "2022", "question": _q(i, "a"), "marks": 5,
             "paper_file": "a.pdf"} for i in range(40)]
    assert _run(tmp_path, monkeypatch, rows)["subjects"] == {}
