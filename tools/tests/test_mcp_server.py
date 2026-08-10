"""The MCP server exposes exactly the policy's seven operations.

Skipped when the MCP SDK is absent, so the corpus verification suite stays
dependency-light. CI installs tools/mcp/requirements.txt for a dedicated step.
"""
from __future__ import annotations

import asyncio

import pytest

pytest.importorskip("mcp", reason="MCP SDK not installed; see tools/mcp/requirements.txt")

from tools.mcp.server import EXPECTED_TOOLS, build_server  # noqa: E402


def _tools(server):
    return asyncio.run(server.list_tools())


def test_server_registers_exactly_the_seven_operations():
    names = {t.name for t in _tools(build_server())}
    assert names == set(EXPECTED_TOOLS), f"tool surface drifted: {sorted(names)}"


def test_every_tool_has_a_description():
    missing = [t.name for t in _tools(build_server()) if not (t.description or "").strip()]
    assert not missing, f"tools without a description: {missing}"


def test_instructions_carry_the_policy_and_the_date_banner():
    instructions = build_server().instructions or ""
    assert "<!-- AGENT-POLICY v1 -->" in instructions
    assert "<!-- EFFECTIVE-DATE-DISCIPLINE v1 -->" in instructions
    assert "compliance deadline" in instructions


def test_get_article_omits_spanish_unless_requested():
    from tools.mcp import server

    without = server.get_article("19.628 Art. 8 bis")
    with_es = server.get_article("19.628 Art. 8 bis", include_spanish=True)
    assert "original_spanish" not in without
    assert with_es["original_spanish"].strip()
    assert without["english"] == with_es["english"]


def test_get_article_surfaces_source_footer():
    from tools.mcp import server

    assert "21.719" in server.get_article("19.628 Art. 8 bis")["source"]


def test_tool_errors_are_returned_not_raised():
    """A bad citation must come back as a structured error, not a crash."""
    from tools.mcp import server

    result = server.get_article("nonsense")
    assert result["error"], "expected an error field"


def test_traverse_returns_edges():
    from tools.mcp import server

    edges = server.get_cross_references("19.628 Art. 2")["edges"]
    assert any(e["citation"] == "19.628 Art. 12" for e in edges)
