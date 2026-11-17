"""English gate, subject canonicalisation and n-gram mining in scripts/topics2.py."""
import topics2 as t


def test_is_english_gate():
    assert t.is_english("What is the role of the enzyme in this reaction and why is it needed?")
    assert not t.is_english("moozmb ama omo amoj vrz maum kxt pql")  # Hindi-font mojibake
    assert not t.is_english("Define the term")  # < 6 words


def test_canon_subject_aliases_and_prefixes():
    assert t.canon_subject("041_Maths") == "Mathematics"
    assert t.canon_subject("Poltical_Science") == "Political Science"
    assert t.canon_subject("12 Bs") == "Business Studies"
    assert t.canon_subject("Sociology") == "Sociology"


def test_norm():
    assert t.norm("Ohm's Law: V=IR (2 marks)") == "ohm s law v ir marks"


def test_ngrams_skip_boilerplate_edges_and_short_words():
    grams = set(t.ngrams("Explain the photoelectric effect equation"))
    # 'explain' is boilerplate so no gram may start with it; 'the' (<=2? no, 3) is boiler too
    assert "photoelectric effect" in grams
    assert "photoelectric effect equation" in grams
    assert not any(g.startswith("explain") for g in grams)
    assert not any(g.endswith(" the") or g.startswith("the ") for g in grams)
    assert list(t.ngrams("")) == []
