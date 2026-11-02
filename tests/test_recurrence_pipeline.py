"""Characterisation of the topics2 / final_report pipelines on a synthetic cache."""
import json
import random

import final_report
import recurrence
import topics2


def synthetic_rows():
    rnd = random.Random(7)
    topics = ["electric field", "market equilibrium", "partnership firm", "magnetic flux"]
    stem = "Explain the concept of {t} with the help of a suitable example in the given context of the study"
    rows = []
    for subj in ("Physics", "Economics"):
        for yr in ("2022", "2023", "2024", "2025", "2026"):
            for p in range(3):
                for q in range(1, 14):
                    rows.append(dict(subject=subj, year=yr, paper_file=f"{subj}_{yr}_{p}.pdf", q_no=q,
                                     marks=rnd.choice([1, 2, 4, 5, 6]), question=stem.format(t=rnd.choice(topics))))
    return rows


def test_high_mark_filter_drops_low_marks_and_long_stems():
    qs = [dict(question="a b c", marks=4), dict(question="a b c", marks=3),
          dict(question="w " * 61, marks=6), dict(question="a", marks=None)]
    assert len(recurrence.high_mark_questions(qs)) == 1


def test_unique_phrases_drops_overlaps_in_order():
    assert list(recurrence.unique_phrases(["electric field", "field", "magnetic flux", "flux"])) == [
        "electric field", "magnetic flux"]


def test_ngram_stats_collects_years_marks_and_first_example():
    qs = [dict(question="electric field strength", year="2022", paper_file="a", marks=4),
          dict(question="electric field strength", year="2023", paper_file="b", marks=5)]
    yrs, pap, mk, ex = recurrence.ngram_stats(qs, example_len=8)
    assert yrs["electric field"] == {"2022", "2023"} and pap["electric field"] == {"a", "b"}
    assert mk["electric field"] == 9 and ex["electric field"] == "electric"


def test_build_report_and_final_are_consistent():
    rows = synthetic_rows()
    report = topics2.build_report(recurrence.usable_rows(rows))
    final = final_report.build_final(rows)
    assert set(report) == set(final["subjects"]) == {"Physics", "Economics"}
    for subj, d in final["subjects"].items():
        assert d["papers"] == 15 and d["questions"] == 195
        assert 0 <= d["repetition_index"] <= 1
    assert all(t["years"] >= 3 for t in final["topics"])
    assert final["formulas"] == [] or all(final_report.is_formula(f["phrase"]) for f in final["formulas"])


def test_mains_write_expected_files(tmp_path, monkeypatch, capsys):
    cache = tmp_path / "qcache_all.json"
    cache.write_text(json.dumps(synthetic_rows()))
    for mod in (topics2, final_report):
        monkeypatch.setattr(mod, "CACHE", cache)
        monkeypatch.setattr(mod, "HERE", tmp_path)
    topics2.main()
    final_report.main()
    assert set(json.loads((tmp_path / "topic_report2.json").read_text())) == {"Physics", "Economics"}
    assert "rep.index" in capsys.readouterr().out
    assert set(json.loads((tmp_path / "final_topics.json").read_text())) == {"subjects", "topics", "formulas"}


def test_is_formula_and_mojibake():
    assert final_report.is_formula("find calculate")
    assert not final_report.is_formula("electric field")
    assert final_report.looks_mojibake("vrz maum")
    assert not final_report.looks_mojibake("electric field")
