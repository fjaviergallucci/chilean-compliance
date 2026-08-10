"""Resolver over citations, articles, and the four indexes.

Pure stdlib — the MCP server is a thin binding over this, but nothing here
depends on the MCP SDK, so the corpus verification suite stays dependency-light.
"""
from __future__ import annotations

import pytest

from tools import corpus_api as api


# --------------------------------------------------------------------------
# Citation grammar
# --------------------------------------------------------------------------

@pytest.mark.parametrize(
    "raw,kind,body,anchor,sub",
    [
        ("19.628 Art. 8 bis", "law", "19.628", "8 bis", None),
        ("Ley 19.628 Art. 8(g)", "law", "19.628", "8", "g"),
        ("21.521 Art. 3(2)", "law", "21.521", "3", "2"),
        ("Ley 21.521 Art. 17", "law", "21.521", "17", None),
        ("NCG 502 §IV.C.3.1", "ncg", "502", "IV.C.3.1", None),
        ("NCG 530 §II.A", "ncg", "530", "II.A", None),
        ("NCG 503 §I", "ncg", "503", "I", None),
    ],
)
def test_parse_citation_grammar(raw, kind, body, anchor, sub):
    c = api.parse_citation(raw)
    assert (c.kind, c.body, c.anchor, c.sub) == (kind, body, anchor, sub)


def test_parse_citation_rejects_garbage():
    with pytest.raises(api.CitationError):
        api.parse_citation("not a citation")


def test_citation_normalises_bis_spacing():
    """The adjacency list writes Art.8bis; headings write Article 8 bis."""
    assert api.parse_citation("19.628 Art. 8bis").anchor == "8 bis"
    assert api.parse_citation("19.628 Art. 8 bis").anchor == "8 bis"


# --------------------------------------------------------------------------
# RETRIEVE
# --------------------------------------------------------------------------

def test_get_article_law_returns_both_languages_and_footer():
    art = api.get_article(api.parse_citation("19.628 Art. 8 bis"))
    assert "Automated" in art.title
    assert art.english.strip(), "English body must not be empty"
    assert art.spanish.strip(), "Spanish original must not be empty"
    assert art.source_footer and "21.719" in art.source_footer
    assert art.path.endswith("titulo-01-utilizacion.md")


def test_get_article_captures_translator_notes():
    art = api.get_article(api.parse_citation("19.628 Art. 1"))
    assert any("item 2" in n for n in art.tn_notes)


def test_get_article_ncg_section():
    art = api.get_article(api.parse_citation("NCG 502 §I.A"))
    assert "Registration Application" in art.title
    assert art.spanish.strip()


def test_get_article_unknown_citation_raises():
    with pytest.raises(api.NotFoundError):
        api.get_article(api.parse_citation("19.628 Art. 9999"))


def test_spanish_original_is_verbatim_blockquote():
    art = api.get_article(api.parse_citation("19.628 Art. 1"))
    assert "Artículo 1" in art.spanish
    # Blockquote markers are stripped; the text itself is preserved.
    assert not art.spanish.lstrip().startswith(">")


# --------------------------------------------------------------------------
# TRAVERSE
# --------------------------------------------------------------------------

def test_get_cross_references_returns_edges_with_reasons():
    edges = api.get_cross_references(api.parse_citation("19.628 Art. 2"))
    targets = {t for t, _ in edges}
    assert {"19.628 Art. 1", "19.628 Art. 1 bis", "19.628 Art. 12"} <= targets
    assert all(reason for _, reason in edges), "every edge carries a reason"


def test_cross_references_empty_for_unlinked_citation():
    assert api.get_cross_references(api.parse_citation("19.628 Art. 9999")) == []


# --------------------------------------------------------------------------
# DEFINE / LOCATE / SCENARIO / STATUS
# --------------------------------------------------------------------------

def test_get_definition_resolves_ncg_term():
    d = api.get_definition("accepted risk")
    assert d.spanish_term == "riesgo aceptado"
    assert d.defined_in == "NCG 502 Anexo N°1"
    assert "risk" in d.english.lower()
    assert d.spanish.strip()


def test_get_definition_is_case_insensitive():
    assert api.get_definition("ACCEPTED RISK").defined_in == "NCG 502 Anexo N°1"


def test_search_topics_finds_national_ids():
    hits = api.search_topics("cédula")
    assert hits, "expected at least one topic hit"
    assert any("National ID" in h.topic for h in hits)
    assert all(h.citations for h in hits), "each hit carries citations"


def test_get_scenario_matches_by_keyword():
    s = api.get_scenario("bank statements")
    assert s.number == 2
    assert s.items, "scenario must carry checklist items"


def test_get_corpus_status_all_stable():
    status = api.get_corpus_status()
    assert status["19628_consolidated"] == "stable"
    assert set(status) >= {"21521_fintech", "ncg_502_consolidated", "ncg_530_reporting"}
