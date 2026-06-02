from pathlib import Path
import pytest
from tools.extract_ncg_sections import parse_toc, extract_sections

FIXTURE = Path(__file__).parent / "fixtures" / "mini_ncg.pdf"
NCG502 = Path(__file__).parent.parent.parent / "sources" / "NCG 502.pdf"


def test_parse_toc_finds_all_entries():
    toc = parse_toc(FIXTURE)
    numbers = [e["number"] for e in toc]
    assert numbers == ["I", "I.A", "I.B", "II", "II.A"], f"got {numbers}"


def test_parse_toc_captures_titles_and_pages():
    toc = parse_toc(FIXTURE)
    first = toc[0]
    assert first["number"] == "I"
    assert "Primera Seccion" in first["title"]
    assert first["page"] == 2


def test_extract_sections_returns_body_blocks():
    sections = extract_sections(FIXTURE)
    a_blocks = [s for s in sections if s["number"] == "I.A"]
    assert any("primera subseccion" in s["spanish_text"] for s in a_blocks)
    assert all("segunda subseccion" not in s["spanish_text"]
               for s in a_blocks if "primera subseccion" in s["spanish_text"])


def test_full_paths_prefix_roman_section():
    toc = parse_toc(FIXTURE)
    by_num = {e["number"]: e for e in toc}
    assert "I.A" in by_num and "I.B" in by_num
    assert "II.A" in by_num
    # The two 'A' subsections are now distinct, not collapsed.
    assert by_num["I.A"]["title"].startswith("Sub A")
    assert by_num["II.A"]["title"].startswith("Otra Sub")


# Regression test: long ToC (multi-page) must not break early when a wrapped
# ToC line is encountered; all Roman sections I-IX must be captured.
@pytest.mark.skipif(not NCG502.exists(), reason="NCG 502.pdf not present")
def test_parse_toc_ncg502_captures_all_roman_sections():
    toc = parse_toc(NCG502)
    numbers = [e["number"] for e in toc]
    for roman in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]:
        assert roman in numbers, f"Roman section {roman!r} missing from ToC (got {numbers})"
