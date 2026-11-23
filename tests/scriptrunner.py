"""Run a module-level pipeline script in a sandbox.

The script is executed with ``__file__`` pointing at a symlink inside a temp directory, so
everything it writes next to itself (``HERE/...``) lands in tmp_path, while coverage (which
resolves symlinks) still attributes the executed lines to the real source file. ``Path.home()`` is redirected by the caller via HOME.
"""
import pathlib
import shutil
import sys

SCRIPTS = pathlib.Path(__file__).resolve().parent.parent / "scripts"


def sandbox_dir(tmp_path, *data_files):
    d = tmp_path / "scripts"
    d.mkdir(exist_ok=True)
    for f in data_files:
        shutil.copy(SCRIPTS / f, d / f)
    return d


def run_script(name, fake_dir, monkeypatch, run_name="__main__"):
    monkeypatch.setattr(sys, "path", list(sys.path))   # scripts insert their own dir
    real = SCRIPTS / f"{name}.py"
    link = fake_dir / f"{name}.py"
    if not link.exists():
        link.symlink_to(real)       # coverage resolves __file__ through the symlink to the real file
    g = {"__name__": run_name, "__file__": str(link)}
    exec(compile(real.read_text(), str(real), "exec"), g)
    return g
