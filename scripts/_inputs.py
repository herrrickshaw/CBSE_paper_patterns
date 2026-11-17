"""Shared guard: fail early with a clear message when the CBSE input files are absent.

The CBSE question papers, marking schemes, curriculum PDFs and NCERT books are third-party
copyrighted material and are NOT distributed in this repository. Download your own copies from
the URLs listed in ../sources/ (cbse.gov.in needs a browser User-Agent) and place them at the
locations the scripts expect.
"""
import pathlib
import sys

HELP = (
    "Download them yourself from the URLs in sources/ (curl -A 'Mozilla/5.0' -O <url>), "
    "convert/extract as described in the README, and put them at that path. "
    "They are not included in this repository."
)


def require_dir(path, what, pattern="*"):
    """Exit with a clear error unless `path` is a directory holding at least one `pattern` match."""
    path = pathlib.Path(path)
    if not path.is_dir() or next(path.rglob(pattern), None) is None:
        sys.exit(f"ERROR: no {what} found at {path}\n{HELP}")
    return path
