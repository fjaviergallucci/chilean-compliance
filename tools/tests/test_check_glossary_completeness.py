import textwrap
from pathlib import Path

from tools.check_glossary_completeness import check_glossary


def _setup(tmp_path: Path, glossary: str, corpus_files: dict[str, str]):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    for name, body in corpus_files.items():
        (corpus / name).write_text(textwrap.dedent(body), encoding="utf-8")
    glossary_file = tmp_path / "glossary.md"
    glossary_file.write_text(textwrap.dedent(glossary), encoding="utf-8")
    return glossary_file, corpus


def test_passes_when_all_terms_resolve(tmp_path):
    g, c = _setup(
        tmp_path,
        """
        ## sensitive personal data
        **Defined in:** 19.628 Art. 2
        """,
        {"titulo-01.md": "## Article 2\n_law:_ 19.628\n"},
    )
    result = check_glossary(g, c)
    assert result.unresolved == []
    assert result.ok is True


def test_glossary_extended_suffixes_resolve(tmp_path):
    """check_glossary should resolve articles like 14 quinquies."""
    g, c = _setup(
        tmp_path,
        """
        ## new term
        **Defined in:** 19.628 Art. 14 quinquies
        """,
        {"titulo-01.md": "## Article 14 quinquies\n_law:_ 19.628\n"},
    )
    result = check_glossary(g, c)
    assert result.unresolved == []
    assert result.ok is True


def test_flags_unresolved_term(tmp_path):
    g, c = _setup(
        tmp_path,
        """
        ## phantom term
        **Defined in:** 19.628 Art. 99
        """,
        {"titulo-01.md": "## Article 2\n_law:_ 19.628\n"},
    )
    result = check_glossary(g, c)
    assert ("phantom term", "19.628", "99") in result.unresolved
    assert result.ok is False
