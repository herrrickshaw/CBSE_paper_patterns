"""Tests for subject canonicalisation, English gate, n-grams and the marks map."""
import marks_map
import recurrence
import topics2


def test_canon_subject_aliases():
    assert topics2.canon_subject("12_Eng Core") == "English Core"
    assert topics2.canon_subject("poltical_science") == "Political Science"
    assert topics2.canon_subject("Biology") == "Biology"


def test_is_english_gate_rejects_mojibake():
    assert recurrence.is_english("the cat is on the mat and it was happy")
    assert not recurrence.is_english("moozmb ama omo amoj xyz abc")


def test_ngrams_skip_boilerplate_edges():
    assert list(recurrence.ngrams("Explain the electric field of a dipole")) == [
        "electric field", "field dipole", "electric field dipole"]


def test_topics2_reexports_for_sibling_scripts():
    for name in ("is_english", "ngrams", "norm", "CACHE", "BOILER", "FUNC"):
        assert hasattr(topics2, name)


def test_marks_map_ranges_are_ordered_and_non_overlapping():
    assert sum(len(v) for v in marks_map.ACADEMIC.values()) == 31
    assert sum(len(v) for v in marks_map.SKILL.values()) == 51
    for table in (marks_map.ACADEMIC, marks_map.SKILL):
        for subject, spec in table.items():
            last = 0
            for q_from, q_to, _marks, _any, _label in spec:
                assert q_from > last and q_to >= q_from, subject
                last = q_to
