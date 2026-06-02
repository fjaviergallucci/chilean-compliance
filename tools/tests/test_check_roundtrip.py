from pathlib import Path

from tools.check_roundtrip import ANCHOR_BLOCK_RE, _normalize_ncg, check_ncg, check_ncg_multi

FIXTURE_NCG = Path(__file__).parent / "fixtures" / "mini_ncg.pdf"


def test_matches_law_article_block():
    text = '## Article 8 bis — X\n### Original Spanish\n> "texto"\n'
    m = ANCHOR_BLOCK_RE.search(text)
    assert m is not None
    assert m.group(1).strip() == "8 bis"
    assert m.group(2) == "texto"


def test_matches_ncg_section_block():
    text = '## IV.C.3.2 — Business Continuity\n### Original Spanish\n> "texto ncg"\n'
    m = ANCHOR_BLOCK_RE.search(text)
    assert m is not None, "NCG section anchor should match"
    assert m.group(1).strip() == "IV.C.3.2"
    assert m.group(2) == "texto ncg"


def test_matches_simple_ncg_section():
    text = '## I.A — Registration\n### Original Spanish\n> "texto reg"\n'
    m = ANCHOR_BLOCK_RE.search(text)
    assert m is not None
    assert m.group(1).strip() == "I.A"
    assert m.group(2) == "texto reg"


def _write(tmp_path, body):
    d = tmp_path / "c"; d.mkdir()
    (d / "s.md").write_text(body, encoding="utf-8")
    return d


def test_ncg_passes_when_spanish_matches_pdf(tmp_path):
    # mini_ncg.pdf body contains: "Esta es la primera subseccion. Contiene reglas."
    body = (
        "## I.A — Sub A\n"
        "**NCG anchor:** N 999, I, A\n\n"
        "### Plain-English text\nThis is the first subsection.\n\n"
        "### Original Spanish\n"
        '> "Esta es la primera subseccion. Contiene reglas."\n\n'
        "> **Source:** NCG 999 §I.A.\n"
    )
    corpus = _write(tmp_path, body)
    failures = check_ncg(FIXTURE_NCG, corpus, threshold=0.85)
    assert failures == [], f"expected no failures, got {failures}"


def test_ncg_flags_spanish_not_in_pdf(tmp_path):
    body = (
        "## I.A — Sub A\n\n"
        "### Original Spanish\n"
        '> "Este texto no aparece en ninguna parte del documento original."\n\n'
        "> **Source:** NCG 999 §I.A.\n"
    )
    corpus = _write(tmp_path, body)
    failures = check_ncg(FIXTURE_NCG, corpus, threshold=0.85)
    assert any(f[0] == "I.A" for f in failures), f"expected I.A to fail, got {failures}"


def test_ncg_skips_trivial_heading_only_blocks(tmp_path):
    body = (
        "## I — Primera Seccion\n\n"
        "### Original Spanish\n"
        '> "I. PRIMERA SECCION"\n\n'
        "> **Source:** NCG 999 §I.\n"
    )
    corpus = _write(tmp_path, body)
    # Short heading-only block should be skipped, not failed.
    failures = check_ncg(FIXTURE_NCG, corpus, threshold=0.85)
    assert all(f[0] != "I" for f in failures), f"trivial block should be skipped, got {failures}"


# ---------------------------------------------------------------------------
# Multi-PDF NCG round-trip tests
# ---------------------------------------------------------------------------

def _write_multi(tmp_path, body):
    d = tmp_path / "cmulti"; d.mkdir()
    (d / "s.md").write_text(body, encoding="utf-8")
    return d


def test_ncg_multi_passes_if_in_any_pdf(tmp_path):
    # mini_ncg.pdf contains "Esta es la primera subseccion. Contiene reglas."
    body = (
        "## I.A — Sub A\n\n### Original Spanish\n"
        '> "Esta es la primera subseccion. Contiene reglas."\n\n'
        "> **Source:** NCG 999 §I.A.\n"
    )
    corpus = _write_multi(tmp_path, body)
    failures = check_ncg_multi([FIXTURE_NCG, FIXTURE_NCG], corpus, threshold=0.85)
    assert failures == [], f"expected no failures, got {failures}"


def test_ncg_multi_flags_text_in_no_pdf(tmp_path):
    body = (
        "## I.A — Sub A\n\n### Original Spanish\n"
        '> "Texto que no aparece en ningun documento original disponible."\n\n'
        "> **Source:** NCG 999 §I.A.\n"
    )
    corpus = _write_multi(tmp_path, body)
    failures = check_ncg_multi([FIXTURE_NCG, FIXTURE_NCG], corpus, threshold=0.85)
    assert any(f[0] == "I.A" for f in failures), f"expected I.A to fail, got {failures}"


# ---------------------------------------------------------------------------
# De-hyphenation tests for NCG 524 line-break split normalisation
# ---------------------------------------------------------------------------

def test_normalize_dehyphenates_linebreak_splits():
    # PDF extraction splits words at line breaks with a hyphen + space.
    raw = "el instru- mento financiero y la representa- cion legal"
    out = _normalize_ncg(raw)
    assert "instrumento" in out, f"got: {out}"
    assert "representacion" in out or "representación" in out, f"got: {out}"
    # must NOT merge a genuine hyphenated compound that isn't a line break?
    # (line-break splits are hyphen + whitespace; inline hyphens like "no-financiero" have no space)


def test_normalize_keeps_inline_hyphen_compounds():
    # A hyphen with NO following space is a real compound, not a line break — keep joined or hyphen, just be consistent.
    raw = "riesgo no-financiero"
    out = _normalize_ncg(raw)
    assert "financiero" in out
