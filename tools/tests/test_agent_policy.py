"""The host-neutral policy is the single source of truth for agent behaviour.

SKILL.md, the MCP server, and the generated ChatGPT instructions are all
*bindings*: they map their own retrieval mechanism onto the operations the
policy defines. They must not restate policy, because a second copy is a
second thing to forget to update.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POLICY = ROOT / "corpus/_agent-policy.md"
SKILL = ROOT / "skills/chile-compliance/SKILL.md"

OPERATIONS = ["LOCATE", "RETRIEVE", "DEFINE", "SCENARIO", "TRAVERSE", "ORIGINAL", "STATUS"]

# The policy must not name any single host's tooling — that is a binding's job.
HOST_SPECIFIC_TOKENS = ["`Read`", "`Grep`", "Claude Code", "slash command"]


def test_policy_file_exists_and_is_versioned():
    assert POLICY.exists(), "corpus/_agent-policy.md is missing"
    assert "<!-- AGENT-POLICY v1 -->" in POLICY.read_text(encoding="utf-8")


def test_policy_defines_every_operation():
    text = POLICY.read_text(encoding="utf-8")
    found = set(re.findall(r"^## Operation: ([A-Z]+)$", text, re.MULTILINE))
    assert set(OPERATIONS) == found, f"expected {sorted(OPERATIONS)}, found {sorted(found)}"


def test_policy_is_host_neutral():
    text = POLICY.read_text(encoding="utf-8")
    offenders = [tok for tok in HOST_SPECIFIC_TOKENS if tok in text]
    assert not offenders, f"policy names host-specific tooling: {offenders}"


def test_policy_carries_effective_date_banner():
    assert "<!-- EFFECTIVE-DATE-DISCIPLINE v1 -->" in POLICY.read_text(encoding="utf-8")


def test_skill_defers_to_policy_and_maps_every_operation():
    text = SKILL.read_text(encoding="utf-8")
    assert "corpus/_agent-policy.md" in text, "SKILL.md must point at the policy file"
    missing = [op for op in OPERATIONS if op not in text]
    assert not missing, f"SKILL.md does not map these operations onto a tool: {missing}"
