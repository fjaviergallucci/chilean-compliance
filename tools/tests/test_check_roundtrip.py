from tools.check_roundtrip import ANCHOR_BLOCK_RE


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
