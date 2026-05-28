# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Planned for later releases:

- Optional MCP server wrapper for non-Claude-Code AI hosts.
- Sample agent integrations for OpenAI SDK and LangChain.
- Coverage for CMF circulars and APDP guidance once issued (separate corpus directories).

## [1.0.0] — 2026-05-27

First fully-stable release. All `corpus_status` entries are now `stable` and the consolidated 19.628 corpus carries literal lexicon-conformant translations across every article.

### Changed

- **Ley 19.628 consolidated Títulos VI, VII, VIII** (Arts. 30–55) — English text replaced with literal lexicon-conformant translations. The Phase F2 build had landed structured English summaries with verbatim Spanish; Phase H4 (PRs #2, #3, #4) finalized 43 article translations across the regulatory framework (APDP Agency), sanctions framework, and constitutional bodies. Translator's notes added where the lexicon does not directly map a Chilean administrative-law or procedural-law term.
- **Ley 19.628 consolidated Título III** — 3 REVIEW markers that documented pre-21.719 amendment-layer history (Leyes 19.812 / 20.463 / 20.575 / 21.214 / 21.504) converted from REVIEW markers to TN notes; the audit trail is preserved in TN form.
- **Ley 19.628 consolidated Título Preliminar Art. 2** — renumbering audit REVIEW resolved (interpretation of item 5.dos confirmed).
- **Disposiciones transitorias Art. 1° transitorio** — eliminated-paragraph audit REVIEW resolved with verbatim Spanish + literal English of the 1999 baseline paragraphs that Ley 21.719 item 16 removed.
- **plugin.json** — `corpus_status.19628_consolidated` flipped from `partial` to `stable`; the `notes` field documenting the gap removed (no longer applicable).
- **Documentation** — main README status table and Spanish section updated; consolidated 19.628 README's "Known limitations" section replaced with a "Translation status" section.

### Notable improvements caught during literal translation

The literal-translation pass surfaced real corrections that the prior summaries had hidden:

- **Art. 30 septies (Título VI)** — old summary said "two-thirds"; the Spanish says **85%**.
- **Art. 32 bis (Título VI)** — old summary mis-categorized two fund-source items.
- **Arts. 54 and 55 (Título VIII)** — old summaries omitted the body enumeration, Title IV cross-references with exceptions (Arts. 14 quinquies, 44–46, Ley 18.834), the supervisory-authority duties paragraph, and the judicially-reviewable-vs-self-supervised distinction. All now present in the literal text.

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

[Unreleased]: https://github.com/fjaviergallucci/chilean-compliance/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/fjaviergallucci/chilean-compliance/releases/tag/v1.0.0
[0.1.0]: https://github.com/fjaviergallucci/chilean-compliance/releases/tag/v0.1.0
