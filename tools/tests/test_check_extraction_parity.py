import textwrap
from pathlib import Path

from tools.check_extraction_parity import check_parity

FIXTURE_PDF = Path(__file__).parent / "fixtures" / "mini.pdf"


def _write_corpus(tmp_path: Path, files: dict[str, str]) -> Path:
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    for name, body in files.items():
        (corpus / name).write_text(textwrap.dedent(body), encoding="utf-8")
    return corpus


def test_passes_when_all_articles_present(tmp_path):
    corpus = _write_corpus(
        tmp_path,
        {
            "titulo-01.md": "## Article 1\n\n## Article 2\n",
            "titulo-02.md": "## Article 3\n",
        },
    )
    result = check_parity(FIXTURE_PDF, corpus)
    assert result.missing == []
    assert result.duplicated == []
    assert result.ok is True


def test_flags_missing_article(tmp_path):
    corpus = _write_corpus(
        tmp_path,
        {
            "titulo-01.md": "## Article 1\n## Article 2\n",
            # Article 3 omitted.
        },
    )
    result = check_parity(FIXTURE_PDF, corpus)
    assert "3" in result.missing
    assert result.ok is False


def test_flags_duplicate_article(tmp_path):
    corpus = _write_corpus(
        tmp_path,
        {
            "titulo-01.md": "## Article 1\n## Article 2\n## Article 3\n",
            "titulo-02.md": "## Article 3\n",  # duplicate
        },
    )
    result = check_parity(FIXTURE_PDF, corpus)
    assert "3" in result.duplicated
    assert result.ok is False


def test_anchor_re_matches_extended_suffixes(tmp_path):
    """check_parity should treat ## Article 14 quinquies as distinct from ## Article 14."""
    corpus = _write_corpus(
        tmp_path,
        {
            "titulo-01.md": "## Article 1\n## Article 2\n## Article 3\n",
            "titulo-02.md": "## Article 2 bis\n## Article 14 quinquies\n",
        },
    )
    result = check_parity(FIXTURE_PDF, corpus)
    # mini.pdf has only Arts. 1, 2, 3 — no quinquies. So 2 bis and 14 quinquies
    # are extras (in corpus but not in PDF). check_parity only flags missing
    # and duplicated, so the extras are fine; the test confirms NO duplicates
    # are flagged just because of the suffix.
    assert "14" not in result.duplicated, "false duplicate from suffix mismatch"
    assert "2" not in result.duplicated, "false duplicate from bis suffix"


def test_exclude_titulo_drops_articles_from_expected_set(tmp_path):
    """When --exclude-titulo is passed, articles from that Título are not expected."""
    corpus = _write_corpus(
        tmp_path,
        {
            # Only article 1 (Título I) in the corpus. The mini.pdf fixture has
            # articles 1, 2 (Título I) and 3 (Título II). Without exclusion,
            # 2 and 3 are missing. With --exclude-titulo II, only 2 is missing.
            "titulo-01.md": "## Article 1\n",
        },
    )
    result = check_parity(FIXTURE_PDF, corpus, exclude_titulos=["II"])
    assert result.missing == ["2"], f"expected only ['2'] missing, got {result.missing}"
    assert result.ok is False  # because article 2 is still missing
