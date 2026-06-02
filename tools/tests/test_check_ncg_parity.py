import json
import textwrap
from pathlib import Path

from tools.check_ncg_parity import check_ncg_parity


def _setup(tmp_path, toc, files, exclude=None):
    toc_path = tmp_path / "_toc.json"
    toc_path.write_text(json.dumps(toc), encoding="utf-8")
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    for name, body in files.items():
        (corpus / name).write_text(textwrap.dedent(body), encoding="utf-8")
    return check_ncg_parity(toc_path, corpus, exclude=exclude or [])


def test_passes_when_all_sections_present(tmp_path):
    toc = [{"number": "I", "title": "x", "page": 1},
           {"number": "I.A", "title": "y", "page": 1}]
    result = _setup(tmp_path, toc, {"s1.md": "## I — X\n## I.A — Y\n"})
    assert result.missing == []
    assert result.duplicated == []
    assert result.ok is True


def test_flags_missing_section(tmp_path):
    toc = [{"number": "I", "title": "x", "page": 1},
           {"number": "II", "title": "z", "page": 2}]
    result = _setup(tmp_path, toc, {"s1.md": "## I — X\n"})
    assert "II" in result.missing
    assert result.ok is False


def test_exclude_drops_section_from_expected(tmp_path):
    toc = [{"number": "I", "title": "x", "page": 1},
           {"number": "VIII", "title": "Derogación", "page": 9}]
    result = _setup(tmp_path, toc, {"s1.md": "## I — X\n"}, exclude=["VIII"])
    assert result.missing == []
    assert result.ok is True
