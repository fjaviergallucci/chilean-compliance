"""Generated distribution artifacts for hosts that cannot run the MCP server.

dist/ is committed and CI fails when it drifts from the corpus, so the no-code
path costs no ongoing maintenance — it is never hand-edited.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from tools import build_dist

ROOT = Path(__file__).resolve().parents[2]

# Custom GPT instruction fields cap out around here; leave no margin to chance.
INSTRUCTIONS_LIMIT = 8000


@pytest.fixture(scope="module")
def bundles(tmp_path_factory) -> list[Path]:
    out = tmp_path_factory.mktemp("dist")
    return build_dist.build_knowledge_bundles(out)


def test_bundle_count_within_upload_limit(bundles):
    assert len(bundles) <= 20, f"{len(bundles)} bundles exceeds the 20-file upload cap"


def test_every_corpus_file_appears_exactly_once(bundles):
    merged = "\n".join(p.read_text(encoding="utf-8") for p in bundles)
    sources = [
        p for p in sorted((ROOT / "corpus").rglob("*.md")) + sorted((ROOT / "indexes").glob("*.md"))
    ]
    missing, duplicated = [], []
    for src in sources:
        rel = src.relative_to(ROOT).as_posix()
        count = merged.count(f"<!-- source: {rel} -->")
        if count == 0:
            missing.append(rel)
        elif count > 1:
            duplicated.append(rel)
    assert not missing, f"corpus files absent from every bundle: {missing}"
    assert not duplicated, f"corpus files present in more than one bundle: {duplicated}"


def test_every_bundle_carries_both_sentinels(bundles):
    for path in bundles:
        text = path.read_text(encoding="utf-8")
        assert build_dist.GENERATED_MARKER in text, f"{path.name} missing generated marker"
        assert "<!-- EFFECTIVE-DATE-DISCIPLINE v1 -->" in text, f"{path.name} missing date banner"


def test_bundles_preserve_spanish_verbatim(bundles):
    merged = "\n".join(p.read_text(encoding="utf-8") for p in bundles)
    assert "Artículo 1°.- Objeto y ámbito de aplicación" in merged


def test_instructions_fit_the_field_limit():
    text = build_dist.build_gpt_instructions()
    assert len(text) <= INSTRUCTIONS_LIMIT, (
        f"instructions are {len(text)} chars, over the {INSTRUCTIONS_LIMIT} limit — "
        "trim the policy projection in build_dist.py rather than truncating"
    )


def test_instructions_keep_the_effective_date_rule_intact():
    text = build_dist.build_gpt_instructions()
    assert "2026-12-01" in text
    assert "compliance deadline" in text
    # The rule that a present-tense question is never deferred must survive trimming.
    assert "has not taken effect" in text


def test_instructions_are_retrieval_phrased_not_tool_phrased():
    text = build_dist.build_gpt_instructions()
    for token in ("`Grep`", "`Read`", "Claude Code"):
        assert token not in text, f"instructions leak host tooling: {token}"


def test_instructions_name_every_operation():
    text = build_dist.build_gpt_instructions()
    for op in ("LOCATE", "RETRIEVE", "DEFINE", "SCENARIO", "TRAVERSE", "ORIGINAL", "STATUS"):
        assert op in text, f"instructions dropped operation {op}"


def test_committed_dist_is_current(tmp_path):
    """The staleness gate, run as a test so contributors catch it before CI."""
    stale = build_dist.diff_against(ROOT / "dist", tmp_path)
    assert not stale, (
        f"dist/ is stale: {stale}. Run `python -m tools.build_dist` and commit the result."
    )
