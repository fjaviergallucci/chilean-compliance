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


# --------------------------------------------------------------------------
# Single-file bundles — the path for someone who just attaches one document
# --------------------------------------------------------------------------

@pytest.fixture(scope="module")
def single_files(tmp_path_factory) -> list[Path]:
    out = tmp_path_factory.mktemp("single")
    return build_dist.build_single_file_bundles(out)


def test_single_bundles_exist_for_both_audiences(single_files):
    names = {p.stem for p in single_files}
    assert names == {"proteccion-datos", "fintech"}, names


def test_single_bundles_stay_attachable(single_files):
    """One chat attachment. Past ~1 MB, hosts start rejecting or truncating."""
    for path in single_files:
        size_kb = path.stat().st_size / 1024
        assert size_kb < 1024, f"{path.name} is {size_kb:,.0f} KB — too big to attach"


def test_single_bundles_instruct_the_assistant_in_spanish(single_files):
    for path in single_files:
        text = path.read_text(encoding="utf-8")
        assert "## Instrucciones para el asistente de IA" in text
        assert "Responde siempre en español" in text
        # The effective-date rule must be stated in Spanish, not only in the
        # English banner — this is the rule most likely to be answered wrongly.
        assert "2026-12-01" in text
        assert "plazo" in text
        assert "todavía no entra en vigencia" in text, (
            f"{path.name} must explicitly forbid the deferral answer"
        )


def test_single_bundles_carry_the_canonical_banner(single_files):
    for path in single_files:
        assert "<!-- EFFECTIVE-DATE-DISCIPLINE v1 -->" in path.read_text(encoding="utf-8")


def test_data_protection_bundle_has_law_scenarios_and_glossary(single_files):
    text = next(p for p in single_files if p.stem == "proteccion-datos").read_text(
        encoding="utf-8"
    )
    assert "<!-- incluye: indexes/scenarios.md -->" in text
    assert "<!-- incluye: indexes/glossary.md -->" in text
    assert "<!-- incluye: corpus/19628-data-protection-consolidated/titulo-02-derechos.md -->" in text
    # Spanish original must survive so exact quotes stay available.
    assert "Artículo 1°.- Objeto y ámbito de aplicación" in text


def test_fintech_bundle_scoped_to_21521(single_files):
    text = next(p for p in single_files if p.stem == "fintech").read_text(encoding="utf-8")
    assert "<!-- incluye: corpus/21521-fintech/titulo-02-servicios.md -->" in text
    assert "19628-data-protection-consolidated" not in text.split("## FUENTE:")[1][:200]


def test_committed_dist_is_current(tmp_path):
    """The staleness gate, run as a test so contributors catch it before CI."""
    stale = build_dist.diff_against(ROOT / "dist", tmp_path)
    assert not stale, (
        f"dist/ is stale: {stale}. Run `python -m tools.build_dist` and commit the result."
    )
