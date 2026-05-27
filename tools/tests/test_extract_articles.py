import re
from pathlib import Path

from tools.extract_articles import TITULO_RE, extract_articles

FIXTURE = Path(__file__).parent / "fixtures" / "mini.pdf"


def test_finds_all_articles_in_fixture():
    blocks = extract_articles(FIXTURE)
    nums = [b["article_num"] for b in blocks]
    assert nums == ["1", "2", "3"], f"got {nums}"


def test_assigns_titulo_correctly():
    blocks = extract_articles(FIXTURE)
    by_num = {b["article_num"]: b for b in blocks}
    assert by_num["1"]["titulo"] == "I"
    assert by_num["2"]["titulo"] == "I"
    assert by_num["3"]["titulo"] == "II"


def test_captures_article_body():
    blocks = extract_articles(FIXTURE)
    by_num = {b["article_num"]: b for b in blocks}
    assert "Cosa" in by_num["2"]["spanish_text"]
    assert "Otra cosa" in by_num["2"]["spanish_text"]


def test_titulo_regex_matches_leading_quote():
    # Regression: BCN PDFs sometimes emit the law text starting with a straight
    # double-quote before TÍTULO I (e.g. Ley 21521).  TITULO_RE must match it.
    text_with_quote = 'Proyecto de ley:\n"TÍTULO I\nDisposiciones generales\n'
    text_without_quote = "TÍTULO II\nServicios\n"
    assert TITULO_RE.search(text_with_quote), "should match \"TÍTULO I with leading quote"
    assert TITULO_RE.search(text_without_quote), "should match TÍTULO II without quote"
    m = TITULO_RE.search(text_with_quote)
    assert m.group(1) == "I"


def test_article_body_does_not_leak_next_titulo_header():
    """Last article in a Título must not include the next Título's header."""
    blocks = extract_articles(FIXTURE)
    by_num = {b["article_num"]: b for b in blocks}
    # Article 2 is the last article of Título I; Título II header follows.
    assert "TITULO II" not in by_num["2"]["spanish_text"], (
        f"Article 2 leaked next Título header: {by_num['2']['spanish_text']!r}"
    )
    assert "Disposiciones varias" not in by_num["2"]["spanish_text"]
    # And the body still ends with the actual article content.
    assert by_num["2"]["spanish_text"].rstrip().endswith("cualquiera.")


def test_titulo_uppercase_form_matches():
    """21.521-style uppercase TÍTULO heading is matched."""
    import re
    from tools.extract_articles import TITULO_RE
    assert TITULO_RE.search("\nTÍTULO I\n") is not None
    assert TITULO_RE.search("\nTÍTULO VII\n") is not None


def test_titulo_titlecase_form_matches():
    """19.628-style title-case Título heading is matched."""
    from tools.extract_articles import TITULO_RE
    assert TITULO_RE.search("\nTítulo Preliminar\n") is not None
    assert TITULO_RE.search("\nTítulo Final\n") is not None
    assert TITULO_RE.search("\nTítulo I\n") is not None


def test_titulo_lowercase_not_matched():
    """Lowercase 'título' inside body text must NOT match — it appears in
    amendment quotations like 'el título XXIX de la ley N° 18.045'."""
    from tools.extract_articles import TITULO_RE
    assert TITULO_RE.search("\ntítulo XXIX\n") is None
    assert TITULO_RE.search("el título VII de la ley") is None


def test_titulo_re_matches_extended_suffixes():
    """ARTICLE_RE should capture articles with bis/ter/quáter/quinquies/sexies/septies/octies/nonies."""
    from tools.extract_articles import ARTICLE_RE
    for suffix in ['bis', 'ter', 'quáter', 'quater', 'quinquies', 'sexies', 'septies', 'octies', 'nonies']:
        text = f"\nArtículo 14 {suffix}.- Definiciones.\n"
        m = ARTICLE_RE.search(text)
        assert m is not None, f"failed to match {suffix!r}"
        assert m.group(1) == f"14 {suffix}", f"got {m.group(1)!r} for {suffix!r}"


def test_21521_titulo_v_not_phantom_split():
    """Regression: 21.521's Título V articles must NOT be split into a
    phantom 'Título XXIX' bucket caused by nested references in amendment
    text. All articles 30-46 (excluding nested 'Artículo N' references
    inside quoted amendment text) should be in Título V."""
    from pathlib import Path
    from tools.extract_articles import extract_articles
    pdf = Path(__file__).parent.parent.parent / "sources" / "Ley-21521_04-ENE-2023-1.pdf"
    if not pdf.exists():
        import pytest
        pytest.skip(f"source PDF not available at {pdf}")
    blocks = extract_articles(pdf)
    titulos = {b["titulo"] for b in blocks}
    # The real 21.521 Títulos are I-V only. No phantom XXIX/Transitorio etc.
    assert titulos == {"I", "II", "III", "IV", "V"}, f"unexpected Títulos: {titulos}"
