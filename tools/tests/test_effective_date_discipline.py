"""The effective-date discipline must live in the corpus, not only in SKILL.md.

Any consumer that reads the corpus without the Claude Code skill (a Custom GPT,
a RAG index, someone browsing GitHub) must still inherit the rule that
2026-12-01 is a compliance deadline, not a reason to defer.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

BANNER_MARKER = "<!-- EFFECTIVE-DATE-DISCIPLINE v1 -->"

BANNER_REQUIRED_IN = [
    "indexes/scenarios.md",
    "indexes/by-topic.md",
    "indexes/glossary.md",
    "indexes/cross-references.md",
    "corpus/19628-data-protection-consolidated/README.md",
    "skills/chile-compliance/SKILL.md",
]

# Phrasings that let an agent dismiss a present-tense compliance question,
# or that send a non-git host to git history for the 1999 baseline.
FORBIDDEN_SUBSTRINGS = [
    "not yet in force",
    "isn't in force yet",
    "exists in git history",
    "preserved in git history",
    "default to post-2026-12-01",
]


def _read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def _plain(text: str) -> str:
    """Strip markdown emphasis so phrase checks survive `**bold**` inside a phrase."""
    return text.replace("*", "").replace("`", "").lower()


def test_banner_present_in_every_required_file():
    missing = [rel for rel in BANNER_REQUIRED_IN if BANNER_MARKER not in _read(rel)]
    assert not missing, f"effective-date banner missing from: {missing}"


def test_banner_states_deadline_framing():
    for rel in BANNER_REQUIRED_IN:
        text = _read(rel)
        assert "compliance deadline" in text, f"{rel}: banner must call 2026-12-01 a compliance deadline"
        assert "2026-12-01" in text, f"{rel}: banner must name the date"


def test_no_deferral_or_git_history_phrasing():
    offenders: list[tuple[str, str]] = []
    for rel in BANNER_REQUIRED_IN:
        text = _plain(_read(rel))
        for bad in FORBIDDEN_SUBSTRINGS:
            if _plain(bad) in text:
                offenders.append((rel, bad))
    assert not offenders, f"deferral/git-history phrasing found: {offenders}"
