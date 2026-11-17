"""Tests use only small SYNTHETIC fixtures; no CBSE paper text is needed or shipped."""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "scripts"))

from _inputs import require_dir  # noqa: E402
from topics2 import is_english  # noqa: E402


def test_missing_input_dir_fails_with_clear_message(tmp_path):
    with pytest.raises(SystemExit) as exc:
        require_dir(tmp_path / "nope", "CBSE past-paper PDFs", "*.pdf")
    msg = str(exc.value)
    assert "CBSE past-paper PDFs" in msg and "not included in this repository" in msg


def test_empty_input_dir_fails(tmp_path):
    with pytest.raises(SystemExit):
        require_dir(tmp_path, "PDFs", "*.pdf")


def test_present_input_dir_passes(tmp_path):
    (tmp_path / "synthetic.pdf").write_bytes(b"%PDF-1.4 synthetic")
    assert require_dir(tmp_path, "PDFs", "*.pdf") == tmp_path


def test_is_english_gate_on_synthetic_strings():
    assert is_english("this is a synthetic question that has the function words in it")
    assert not is_english("moozmb ama omo amoj")
