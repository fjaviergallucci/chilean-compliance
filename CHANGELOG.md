# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Planned for v0.2.0 or later:

- Finish literal translations of Ley 19.628 consolidated Títulos VI–VIII (44 REVIEW markers pending).
- Optional MCP server wrapper for non-Claude-Code AI hosts.
- Sample agent integrations for OpenAI SDK and LangChain.

## [0.1.0] — 2026-05-27

### Added

- **Plugin manifest** (`plugin.json`) with per-law `corpus_status` tracking.
- **Skill** (`skills/chile-compliance/SKILL.md`) with full query decision tree for consuming AIs.
- **Corpus** of Chilean law in English with verbatim Spanish blocks:
  - **Ley 21.521** (Fintec) — Títulos I–IV fully translated (29 articles). Título V documented as out of scope.
  - **Ley 19.628 consolidated** (post-Ley 21.719) — Preliminar through Título V fully translated. Títulos VI–VIII contain structured English summaries with verbatim Spanish; literal translations pending.
  - **Ley 21.719 amendments changelog** — reference-only, all 21 amendment items extracted and mapped.
- **Lexicon** (`corpus/_lexicon.md`) — hand-curated Spanish-to-English mapping for ~50 legal terms.
- **Indexes**:
  - `indexes/by-topic.md` — 113 citations across 20 compliance topics.
  - `indexes/glossary.md` — 40 defined terms (English + Spanish).
  - `indexes/scenarios.md` — 7 compliance checklists for common features (78 checklist items, 98 citations).
  - `indexes/cross-references.md` — 265 article-to-article relationships.
- **Tooling** (`tools/`) with pytest coverage (18 tests):
  - `extract_articles.py` — PDF → structured article blocks.
  - `check_extraction_parity.py` — verifies every PDF article appears once in the corpus (`--exclude-titulo` flag for known out-of-scope sections).
  - `check_glossary_completeness.py` — verifies every glossary term cites a real article.
  - `check_roundtrip.py` — verifies corpus Spanish text matches the source PDF.
  - `parse_21719_amendments.py` — one-off parser for Ley 21.719's amendment list.

### Documentation

- Public-facing README with status table, quick-start guides for Claude Code and other AI hosts, architecture overview, contributing guide, and disclaimers.
- MIT LICENSE with explicit acknowledgement that the verbatim Spanish source text from BCN remains public-domain.
- CONTRIBUTING.md with priority guidance for finishing pending REVIEW markers.

### Known limitations

- Ley 19.628 consolidated Títulos VI (Agency), VII (Sanctions), VIII (Constitutional bodies) — Arts. 30–55 — currently contain English structured summaries. Verbatim Spanish is preserved; 44 `<!-- REVIEW -->` markers flag passages awaiting literal translation. The consuming AI surfaces these as caveats when citing.
- CMF circulars, APDP guidance, and case law are not included. The skill instructs consuming AIs to say so when asked.
- Pre-effective-date Ley 19.628 (1999 baseline) is not in the active corpus — for pre-2026-12-01 questions, consult the source PDF directly.

[Unreleased]: https://github.com/fjaviergallucci/chilean-compliance/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/fjaviergallucci/chilean-compliance/releases/tag/v0.1.0
