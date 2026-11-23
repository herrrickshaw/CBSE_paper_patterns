"""scripts/parse_generic.py: SYNTHETIC paper text only (pdftotext is faked)."""
import types

import pytest

import parse_generic as pg


def fake_pdftotext(monkeypatch, text):
    monkeypatch.setattr(pg.subprocess, "run",
                        lambda *a, **k: types.SimpleNamespace(stdout=text))


# ---------------- pages / english_lines ----------------

def test_pages_splits_on_form_feed_and_calls_pdftotext(monkeypatch, tmp_path):
    seen = {}

    def run(cmd, **kw):
        seen["cmd"], seen["kw"] = cmd, kw
        return types.SimpleNamespace(stdout="p1\fp2\fp3")

    monkeypatch.setattr(pg.subprocess, "run", run)
    assert pg.pages(tmp_path / "x.pdf") == ["p1", "p2", "p3"]
    assert seen["cmd"][:3] == ["pdftotext", "-layout", str(tmp_path / "x.pdf")]
    assert seen["kw"]["timeout"] == 120 and seen["kw"]["capture_output"] is True


def test_latin_words_counts_only_two_plus_letter_tokens():
    assert pg.latin_words("a bc def 12 x-yz") == 3
    assert pg.latin_words("") == 0


def test_english_lines_filters_noise_devanagari_and_symbol_lines(monkeypatch, tmp_path):
    page = "\n".join([
        "P.T.O.", "Page 3", "Series : ABC", "Roll No. 123", "SET-1", "*12*",
        "   ", "हिन्दी text here", "12", "---",
        "1.   What  is   the  meaning of life",
        "Candidates must write the Q.P. Code",
        "3 of 12",
    ])
    fake_pdftotext(monkeypatch, page)
    out = pg.english_lines(tmp_path / "x.pdf")
    # only the real question survives; its internal 3-space runs shrink to 2 spaces
    assert out == ["1.  What  is  the  meaning of life"]


def test_english_lines_collapses_whitespace_runs_to_two_spaces(monkeypatch, tmp_path):
    fake_pdftotext(monkeypatch, "alpha        beta   gamma delta")
    assert pg.english_lines(tmp_path / "x.pdf") == ["alpha  beta  gamma delta"]


def test_symbol_only_short_lines_dropped_but_six_char_boundary(monkeypatch, tmp_path):
    # fullmatch [\W\d_]{0,6}: 6 chars dropped, 7 kept
    fake_pdftotext(monkeypatch, "1234567\n123456\n(1)(2)\n(1) (2)")
    assert pg.english_lines(tmp_path / "x.pdf") == ["1234567", "(1) (2)"]


def test_reprint_pages_dropped_only_when_no_numbered_question(monkeypatch, tmp_path):
    reprint = "\n".join(f"reprint line number {c}" for c in "abcde")
    page1 = reprint                                   # pure reprint of page 2
    page2 = reprint + "\n1. Real question text here"  # has a numbered question
    fake_pdftotext(monkeypatch, page1 + "\f" + page2)
    out = pg.english_lines(tmp_path / "x.pdf")
    assert out == [f"reprint line number {c}" for c in "abcde"] + ["1. Real question text here"]


def test_reprint_page_with_question_number_is_kept(monkeypatch, tmp_path):
    lines = "\n".join(["1. keep question one", "line b", "line c", "line d", "line e"])
    fake_pdftotext(monkeypatch, lines + "\f" + lines)
    assert len(pg.english_lines(tmp_path / "x.pdf")) == 10


def test_reprint_threshold_is_80_percent(monkeypatch, tmp_path):
    base = [f"stable line {c}" for c in "abcd"]
    page1 = base + ["only here"]            # 4/5 = 0.8 later -> dropped
    page2 = base + ["1. last question here"]
    fake_pdftotext(monkeypatch, "\n".join(page1) + "\f" + "\n".join(page2))
    assert "only here" not in pg.english_lines(tmp_path / "x.pdf")
    page1b = base[:3] + ["only here", "also here"]   # 3/5 = 0.6 -> kept
    fake_pdftotext(monkeypatch, "\n".join(page1b) + "\f" + "\n".join(page2))
    assert "only here" in pg.english_lines(tmp_path / "x.pdf")


def test_drop_reprints_false_keeps_everything(monkeypatch, tmp_path):
    body = "\n".join(f"same line {c}" for c in "abcde")
    fake_pdftotext(monkeypatch, body + "\f" + body)
    assert len(pg.english_lines(tmp_path / "x.pdf", drop_reprints=False)) == 10


def test_empty_pages_skipped(monkeypatch, tmp_path):
    fake_pdftotext(monkeypatch, "\n\f1. Alpha bravo charlie")
    assert pg.english_lines(tmp_path / "x.pdf") == ["1. Alpha bravo charlie"]


# ---------------- declared_* ----------------

def test_declared_count_and_marks():
    L = ["Maximum Marks: 80", "This paper contains 34 questions", "x"]
    assert pg.declared_count(L) == 34
    assert pg.declared_marks(L) == 80
    assert pg.declared_marks(["MAXIMUM MARKS 70"]) == 70
    assert pg.declared_count(["contains   5   QUESTIONS"]) == 5
    assert pg.declared_count(["nothing"]) is None
    assert pg.declared_marks([]) is None


def test_declared_count_first_match_wins():
    assert pg.declared_count(["contains 10 questions", "contains 20 questions"]) == 10


# ---------------- split_questions ----------------

def test_split_questions_sequential_and_continuations():
    L = ["1. First question about biology", "continued line", "2. Second question about chemistry",
         "(A) opt", "3. Third question about physics"]
    b = pg.split_questions(L)
    assert [x["q_no"] for x in b] == [1, 2, 3]
    assert b[0]["lines"] == ["First question about biology", "continued line"]
    assert b[1]["lines"] == ["Second question about chemistry", "(A) opt"]


def test_split_questions_fills_gap_with_missing_placeholders():
    L = ["1. First question about biology", "4. Fourth question about chemistry"]
    b = pg.split_questions(L)
    assert [x["q_no"] for x in b] == [1, 2, 3, 4]
    assert [bool(x.get("missing")) for x in b] == [False, True, True, False]
    assert b[1]["lines"] == []


def test_split_questions_jump_of_three_missing_accepted_four_rejected():
    ok = pg.split_questions(["1. First question here ok", "5. Fifth question here ok"])
    assert [x["q_no"] for x in ok] == [1, 2, 3, 4, 5]    # expect+3 is the last accepted
    bad = pg.split_questions(["1. First question here ok", "6. Sixth question here ok"])
    assert [x["q_no"] for x in bad] == [1]
    assert "6. Sixth question here ok" in bad[0]["lines"]


def test_split_questions_requires_two_latin_words_and_respects_cap():
    L = ["1. 12345 67", "1. Valid question text here", "2. x", "2. Another real question"]
    b = pg.split_questions(L)
    assert [x["q_no"] for x in b] == [1, 2]
    capped = pg.split_questions(["1. First question text", "2. Second question text",
                                 "3. Third question text"], cap=2)
    assert [x["q_no"] for x in capped] == [1, 2]
    assert capped[1]["lines"][-1] == "3. Third question text"


def test_split_questions_lines_before_first_question_ignored_and_dedupe():
    L = ["preamble line", "1. First question text", "dup", "dup", "other", "dup"]
    b = pg.split_questions(L)
    assert b[0]["lines"] == ["First question text", "dup", "other"]


def test_split_questions_accepts_paren_numbering_and_empty_input():
    assert pg.split_questions([]) == []
    assert pg.split_questions(["1) First question text"])[0]["q_no"] == 1


def test_split_questions_cap_boundary_inclusive():
    L = ["1. First question text", "2. Second question text"]
    assert [x["q_no"] for x in pg.split_questions(L, cap=2)] == [1, 2]


# ---------------- options ----------------

def test_options_parses_four_options():
    o = pg.options(["Which one?", "(A) apple", "(B) banana", "(C) cherry", "(D) date"])
    assert o == {"A": "apple", "B": "banana", "C": "cherry", "D": "date"}


def test_options_needs_three_markers():
    assert pg.options(["(A) one", "(B) two"]) is None
    assert pg.options([]) is None
    assert pg.options(["(A) one", "(B) two", "(C) three"]) == {"A": "one", "B": "two", "C": "three"}


def test_options_stops_at_next_numbered_question_and_trims_punctuation():
    o = pg.options(["(A) alpha;", "(B) beta.", "(C) gamma", "(D) delta 12. Next question"])
    assert o["A"] == "alpha" and o["B"] == "beta" and o["D"] == "delta"


def test_options_duplicate_letter_first_wins_and_truncates_at_300():
    o = pg.options(["(A) first", "(B) two", "(A) again", "(C) " + "x" * 400])
    assert o["A"] == "first"
    assert len(o["C"]) == 300


def test_options_needs_three_non_empty_values():
    assert pg.options(["(A) one", "(B)", "(C)"]) is None


# ---------------- marks_of ----------------

@pytest.mark.parametrize("line,expected", [
    ("Answer any five 5 x 2 = 10", 10),
    ("something 3 × 4 = 12", 12),
    ("something 3 ´ 5 = 15", None),        # 15 > 12: rejected
    ("bad 3 x 4 = 13", None),                  # arithmetic mismatch
    ("thing 1 + 2 = 3", 3),
    ("thing 1 + 2 + 3 = 6", 6),
    ("thing 6 + 7 = 13", None),                # 13 > 12
    ("question text    5", 5),
    ("question text    12", 12),
    ("question text    13", None),
    ("question text    0", None),
    ("question text 5", None),                 # one space before the digit: not a marks column
    ("no marks here", None),
])
def test_marks_of_single_line(line, expected):
    m, src = pg.marks_of([line])
    assert m == expected
    assert src == ("parsed" if expected else None)


def test_marks_of_takes_max_of_candidates():
    assert pg.marks_of(["a    2", "b    5", "c    3"]) == (5, "parsed")
    assert pg.marks_of([]) == (None, None)


# ---------------- q_type ----------------

@pytest.mark.parametrize("text,opts,expected", [
    ("Assertion (A): x Reason (R): y", None, "assertion-reason"),
    ("Statement-I: x", None, "two-statement"),
    ("Statement 1 : x", None, "two-statement"),
    ("Match List I with List II", None, "matching"),
    ("match column A", None, "matching"),
    ("arrange the following events", None, "ordering"),
    ("in correct sequence", None, "ordering"),
    ("Read the passage and answer", None, "source-based"),
    ("Study the following case", None, "source-based"),
    ("On the given political outline map", None, "map"),
    ("plain question", {"A": "x"}, "mcq"),
    ("plain question", None, "subjective"),
])
def test_q_type(text, opts, expected):
    assert pg.q_type([text], opts) == expected


def test_q_type_priority_assertion_beats_options():
    assert pg.q_type(["Assertion (A) is"], {"A": "1"}) == "assertion-reason"


# ---------------- section_walk ----------------

def test_section_walk_assigns_sections_and_parts():
    L = ["SECTION A", "1. First question text", "2. Second question text",
         "Section - B", "3. Third question text", "PART B", "4. Fourth question text"]
    s = pg.section_walk(L)
    assert s == {1: "A", 2: "A", 3: "B", 4: "Part B"}


def test_section_walk_fills_gaps_with_current_section():
    s = pg.section_walk(["SECTION C", "1. First question text", "3. Third question text"])
    assert s == {1: "C", 2: "C", 3: "C"}


def test_section_walk_respects_cap_and_latin_words():
    s = pg.section_walk(["SECTION A", "1. 12 34", "1. Real question text"], cap=1)
    assert s == {1: "A"}
    assert pg.section_walk(["SECTION A", "1. Real question text", "2. Next question text"], cap=1) == {1: "A"}


def test_section_walk_before_any_header_is_none():
    assert pg.section_walk(["1. Real question text"]) == {1: None}


# ---------------- parse_paper ----------------

PAPER = "\n".join([
    "Maximum Marks: 80",
    "This question paper contains 5 questions",
    "SECTION A",
    "1. Which gas is most abundant?",
    "(A) Oxygen",
    "(B) Nitrogen",
    "(C) Argon",
    "(D) Neon",
    "SECTION B",
    "2. Explain the water cycle in detail 3 x 1 = 3",
    "OR",
    "Describe evaporation in the given figure 5",
    "5. Assertion (A): plants respire. Reason (R): they need energy.",
])


def test_parse_paper_end_to_end(monkeypatch, tmp_path):
    fake_pdftotext(monkeypatch, PAPER)
    rows, dq, dm = pg.parse_paper(tmp_path / "p.pdf", "Biology", "sqp", "P1")
    assert (dq, dm) == (5, 80)
    assert [r["q_no"] for r in rows] == [1, 2, 3, 4, 5]
    r1, r2 = rows[0], rows[1]
    assert r1["q_type"] == "mcq" and r1["section"] == "A"
    assert r1["marks"] is None and r1["marks_source"] is None
    import json
    opts = json.loads(r1["options"])
    assert [opts[k] for k in "ABC"] == ["Oxygen", "Nitrogen", "Argon"]
    assert opts["D"].startswith("Neon")
    assert r1["subject"] == "Biology" and r1["source"] == "sqp" and r1["paper_id"] == "P1"
    assert r2["section"] == "B" and r2["marks"] == 3 and r2["marks_source"] == "parsed"
    assert r2["has_internal_choice"] is True and r2["has_figure"] is True
    assert r2["q_type"] == "subjective" and r2["options"] is None
    assert r2["question"].startswith("Explain the water cycle")
    for miss in rows[2:4]:
        assert miss["q_type"] == "figure-only" and miss["has_figure"] is True
        assert miss["full_text"] is None and miss["marks"] is None
        assert miss["question"].startswith("[stem not in extractable text")
    assert rows[4]["q_type"] == "assertion-reason"


def test_parse_paper_stem_stops_at_option_marker_and_caps_length(monkeypatch, tmp_path):
    long_line = "word " * 100            # 500 chars -> stem stops growing after >= 400
    text = "1. Start of question here\n" + long_line + "\n" + long_line + "\n(i) sub part"
    fake_pdftotext(monkeypatch, text)
    rows, _, _ = pg.parse_paper(tmp_path / "p.pdf", "S", "src", "id")
    q = rows[0]["question"]
    assert "sub part" not in q
    assert len(q) <= 1200
    assert q.startswith("Start of question here")


def test_parse_paper_without_declarations(monkeypatch, tmp_path):
    fake_pdftotext(monkeypatch, "1. Some question text here")
    rows, dq, dm = pg.parse_paper(tmp_path / "p.pdf", "S", "src", "id")
    assert dq is None and dm is None and len(rows) == 1
    assert rows[0]["section"] is None


# ---------------- marking schemes ----------------

def test_parse_marking_scheme_patterns(monkeypatch, tmp_path):
    text = "\n".join([
        "1. (A)",
        "2 B",
        "3) - C",
        "4. See Option (d) for this",
        "5 the answer is Ans: b",
        "6. nothing here",
        "1. (D)",              # duplicate q: first wins
        "0. (A)",              # out of range
        "121. (A)",            # out of range
        "120. (C)",            # boundary
    ])
    fake_pdftotext(monkeypatch, text)
    ans = pg.parse_marking_scheme(tmp_path / "ms.pdf")
    assert ans == {1: "A", 2: "B", 3: "C", 4: "D", 5: "B", 120: "C"}


def test_parse_marking_scheme_keeps_reprinted_pages(monkeypatch, tmp_path):
    page = "1. (A)\n2. (B)\n3. (C)\n4. (D)\n5. (A)"
    fake_pdftotext(monkeypatch, page + "\f" + page)
    assert pg.parse_marking_scheme(tmp_path / "ms.pdf") == {1: "A", 2: "B", 3: "C", 4: "D", 5: "A"}


@pytest.mark.xfail(strict=True, reason="ANS_PATTERNS[0] is compiled without re.I, so the lowercase "
                   "key style '12. (b)' (the common CBSE format, see parse_ms.py docstring) is not "
                   "matched although the code calls .upper() on the capture (parse_generic.py:~146)")
def test_parse_marking_scheme_lowercase_letter_key(monkeypatch, tmp_path):
    fake_pdftotext(monkeypatch, "1. (a)\n2. (b)")
    assert pg.parse_marking_scheme(tmp_path / "ms.pdf") == {1: "A", 2: "B"}


def test_options_three_markers_but_two_distinct_letters_is_none():
    assert pg.options(["(A) x", "(B) y", "(A) z"]) is None


def test_marks_of_product_boundary_is_twelve():
    assert pg.marks_of(["something 12 x 1 = 12"]) == (12, "parsed")
    assert pg.marks_of(["something 13 x 1 = 13"]) == (None, None)
