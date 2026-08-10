"""MCP server exposing the Chilean compliance corpus.

One server serves every MCP-speaking client — ChatGPT connectors, Claude Desktop,
Cursor — so there is a single portable runtime rather than one bundle per host.

Why MCP rather than a knowledge-file upload: the policy's decision tree depends on
retrieving an *exact* citation and traversing the cross-reference graph. Semantic
retrieval over uploaded documents returns plausible-looking fragments and will not
reliably follow the law -> NCG bridge, which is what turns a legal question into an
operational answer. Exact retrieval is the whole point.

The server's ``instructions`` are the full text of ``corpus/_agent-policy.md``, so
the connecting client inherits the policy — including the effective-date
discipline — without a second copy being maintained here.

Run it:  python -m tools.mcp.server
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from mcp.server import MCPServer

from tools import corpus_api as api

POLICY_PATH = Path(__file__).resolve().parents[2] / "corpus/_agent-policy.md"

EXPECTED_TOOLS = (
    "search_topics",
    "get_article",
    "get_definition",
    "get_scenario",
    "get_cross_references",
    "get_spanish_original",
    "get_corpus_status",
)


def _load_policy() -> str:
    return POLICY_PATH.read_text(encoding="utf-8")


def _fail(exc: Exception) -> dict[str, Any]:
    """Return errors as data.

    A tool that raises gives the model a transport failure it cannot reason
    about; a structured error lets it correct the citation and retry.
    """
    return {"error": f"{type(exc).__name__}: {exc}"}


# ---------------------------------------------------------------------------
# Tool implementations — plain functions so they are unit-testable without MCP
# ---------------------------------------------------------------------------

def search_topics(query: str) -> dict[str, Any]:
    """LOCATE. Topic bullets matching a keyword, each with its citations."""
    try:
        hits = api.search_topics(query)
    except Exception as exc:  # noqa: BLE001 - surfaced to the model as data
        return _fail(exc)
    return {
        "query": query,
        "hits": [
            {"topic": h.topic, "bullet": h.bullet, "citations": h.citations} for h in hits
        ],
        "note": (
            "Bullets summarise; they do not substitute for the article. "
            "Call get_article on each citation before answering."
        ),
    }


def get_article(citation: str, include_spanish: bool = False) -> dict[str, Any]:
    """RETRIEVE. The full article or section block for a citation."""
    try:
        art = api.get_article(api.parse_citation(citation))
    except Exception as exc:  # noqa: BLE001
        return _fail(exc)
    out: dict[str, Any] = {
        "citation": art.citation,
        "title": art.title,
        "english": art.english,
        "cross_references": art.cross_refs,
        "source": art.source_footer or "",
        "path": art.path,
    }
    if art.tn_notes:
        out["translator_notes"] = art.tn_notes
    if include_spanish:
        out["original_spanish"] = art.spanish
    return out


def get_definition(term: str) -> dict[str, Any]:
    """DEFINE. Glossary entry for a term, with its Spanish original."""
    try:
        d = api.get_definition(term)
    except Exception as exc:  # noqa: BLE001
        return _fail(exc)
    return {
        "term": d.term,
        "spanish_term": d.spanish_term,
        "defined_in": d.defined_in,
        "english": d.english,
        "original_spanish": d.spanish,
    }


def get_scenario(query: str) -> dict[str, Any]:
    """SCENARIO. Compliance checklist for a feature, or a scenario number."""
    try:
        s = api.get_scenario(query)
    except Exception as exc:  # noqa: BLE001
        return _fail(exc)
    return {
        "number": s.number,
        "title": s.title,
        "fintech_scope": s.fintech_scope,
        "data_protection_scope": s.data_scope,
        "checklist": s.items,
        "note": (
            "Checklist items summarise. Call get_article on every citation "
            "before relying on an item."
        ),
    }


def get_cross_references(citation: str) -> dict[str, Any]:
    """TRAVERSE. Related citations, including the law -> NCG bridge."""
    try:
        edges = api.get_cross_references(api.parse_citation(citation))
    except Exception as exc:  # noqa: BLE001
        return _fail(exc)
    return {
        "citation": citation,
        "edges": [{"citation": target, "reason": reason} for target, reason in edges],
    }


def get_spanish_original(citation: str) -> dict[str, Any]:
    """ORIGINAL. The verbatim Spanish block for a citation."""
    try:
        art = api.get_article(api.parse_citation(citation))
    except Exception as exc:  # noqa: BLE001
        return _fail(exc)
    return {
        "citation": art.citation,
        "original_spanish": art.spanish,
        "source": art.source_footer or "",
    }


def get_corpus_status() -> dict[str, Any]:
    """STATUS. Coverage and translation status per corpus."""
    try:
        return {"corpus_status": api.get_corpus_status()}
    except Exception as exc:  # noqa: BLE001
        return _fail(exc)


_IMPLEMENTATIONS = {
    "search_topics": search_topics,
    "get_article": get_article,
    "get_definition": get_definition,
    "get_scenario": get_scenario,
    "get_cross_references": get_cross_references,
    "get_spanish_original": get_spanish_original,
    "get_corpus_status": get_corpus_status,
}


def build_server() -> MCPServer:
    """Construct the server with the policy as its instructions."""
    server = MCPServer(
        name="chile-compliance",
        title="Chilean Fintech & Data-Protection Corpus",
        description=(
            "Structured, citable access to Ley 21.521 (Fintec), Ley 19.628 as amended "
            "by Ley 21.719, and CMF regulations NCG 502/503/514/530."
        ),
        instructions=_load_policy(),
        version="1.3.0",
    )
    for name, fn in _IMPLEMENTATIONS.items():
        server.add_tool(fn, name=name)
    return server


def main() -> None:
    build_server().run(transport="stdio")


if __name__ == "__main__":
    main()
