"""Translation-status claims in the indexes and skill must match reality.

Phase H4 closed all 44 REVIEW markers; plugin.json declares 19628_consolidated
stable. Any leftover "pending review" language makes the skill warn users about
articles that are actually complete — and it does so on the sanctions and
penalties articles a compliance user cares most about.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

STATUS_CLAIM_FILES = [
    "indexes/by-topic.md",
    "indexes/glossary.md",
    "indexes/scenarios.md",
    "indexes/cross-references.md",
    "skills/chile-compliance/SKILL.md",
]

STALE_PATTERNS = [
    re.compile(r"await H4", re.IGNORECASE),
    re.compile(r"pending (literal )?H4", re.IGNORECASE),
    re.compile(r"pending H4 review", re.IGNORECASE),
    re.compile(r"currently summarized", re.IGNORECASE),
]


def test_corpus_has_no_review_markers():
    hits = [
        p.relative_to(ROOT).as_posix()
        for p in (ROOT / "corpus").rglob("*.md")
        if p.name != "README.md" and "<!-- REVIEW:" in p.read_text(encoding="utf-8")
    ]
    assert not hits, f"unresolved REVIEW markers in corpus: {hits}"


def test_no_stale_h4_language_in_status_claim_files():
    offenders: list[tuple[str, str]] = []
    for rel in STATUS_CLAIM_FILES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for pat in STALE_PATTERNS:
            for m in pat.finditer(text):
                line_no = text[: m.start()].count("\n") + 1
                offenders.append((rel, f"line {line_no}: {m.group(0)}"))
    assert not offenders, f"stale translation-status language: {offenders}"


def test_skill_partial_markers_match_plugin_status():
    status = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    corpus_status = status["corpus_status"]
    skill = (ROOT / "skills/chile-compliance/SKILL.md").read_text(encoding="utf-8")
    if corpus_status["19628_consolidated"] == "stable":
        bad = [
            line.strip()
            for line in skill.splitlines()
            if "19628-data-protection-consolidated" in line and "(partial)" in line
        ]
        assert not bad, f"SKILL.md marks 19.628 files partial while plugin.json says stable: {bad}"
