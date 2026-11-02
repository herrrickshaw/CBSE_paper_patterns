"""Characterisation tests for scripts/parse_generic.py using synthetic text (no real paper content).

Expected values were captured from the pre-refactor code.
"""
import parse_generic as g

LINES = [
    "General Instructions", "This question paper contains 4 questions.", "Maximum Marks: 40",
    "SECTION A", "1. Which of the following is a prime number among these",
    "(A) four", "(B) six", "(C) seven", "(D) nine",
    "2. Assertion (A) is stated here for testing purposes", "Reason (R) is stated here too for the test",
    "SECTION B", "3. Explain the working of a simple lever with an example 3",
    "OR", "Describe the working of a simple pulley with an example",
    "5. Define the term velocity in your own words 2 x 2 = 4",
]


def test_declared_values():
    assert g.declared_count(LINES) == 4
    assert g.declared_marks(LINES) == 40
    assert g.declared_count(["nothing"]) is None


def test_split_questions_tolerates_gap_and_flags_missing():
    blocks = g.split_questions(LINES)
    assert [b["q_no"] for b in blocks] == [1, 2, 3, 4, 5]
    assert blocks[3] == {"q_no": 4, "lines": [], "missing": True}
    assert blocks[2]["lines"][1] == "OR"


def test_options_needs_three_markers():
    blocks = g.split_questions(LINES)
    assert g.options(blocks[0]["lines"]) == {"A": "four", "B": "six", "C": "seven", "D": "nine"}
    assert g.options(["(A) only", "(B) two"]) is None


def test_marks_of_variants():
    assert g.marks_of(["Compute 2 x 2 = 4"]) == (4, "parsed")
    assert g.marks_of(["Do 1 + 2 + 3 = 6"]) == (6, "parsed")
    assert g.marks_of(["Nothing here"]) == (None, None)
    assert g.marks_of(["value 40"]) == (None, None)  # >12 is not a per-question mark


def test_q_type_and_sections():
    blocks = g.split_questions(LINES)
    types = [g.q_type(b["lines"], g.options(b["lines"])) for b in blocks]
    assert types == ["mcq", "assertion-reason", "subjective", "subjective", "subjective"]
    assert g.section_walk(LINES) == {1: "A", 2: "A", 3: "B", 4: "B", 5: "B"}


def test_latin_words_counts_two_letter_plus():
    assert g.latin_words("a bc def 12") == 2


def test_marking_scheme_patterns_use_explicit_answers_only():
    rx = g.ANS_PATTERNS[0]
    assert rx.match("12. (B)").groups() == ("12", "B")
    assert rx.match("12. some text") is None
