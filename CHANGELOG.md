# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Planned for later releases:

- Optional MCP server wrapper for non-Claude-Code AI hosts.
- Sample agent integrations for OpenAI SDK and LangChain.
- Coverage for CMF circulars and APDP guidance once issued (separate corpus directories).

## [1.3.0] — 2026-06-03

### Added
- **NCG 503 (Exigencias de Idoneidad / fit-and-proper).** Knowledge-accreditation
  requirements for personnel performing defined functions; full prose translation
  (Secciones I–IV), bridged to Ley 21.521 arts. 7 & 9. Derogates NCG 412.
- **NCG 530 (MSI Fintec reporting), obligations layer.** Body (FINTEC01–16 list,
  MSI Fintec creation, vigencia) + Anexo N°1 general instructions + a derived
  FINTEC01–16 catalog. Record layouts (Anexo N°2/N°3) intentionally out of scope.
- Cross-reference bridges: NCG 530 ↔ NCG 502 (first intra-NCG bridge), NCG 530 ↔
  Ley 21.521, NCG 503 ↔ Ley 21.521. Glossary, by-topic, and scenario integration.
- CI gates for NCG 503 and NCG 530 parity + round-trip; FINTEC-catalog spot-check.

### Changed
- `corpus_status`: `ncg_503_idoneidad` and `ncg_530_reporting` → `stable`.

## [1.2.0] — 2026-06-02

### Added

- **NCG 514 (Sistema de Finanzas Abiertas / open finance) corpus** — implementing regulation for Ley 21.521 Título III. 6 Secciones (I Perímetro, II Funcionamiento, III Seguridad y Resguardos, IV Información, V Otras Disposiciones, VI Anexos Normativos), 80 sections, section-level literal English + verbatim Spanish, round-trip verified at 0.80. Extractor extended to recognize `SECCIÓN <Roman>` structure. Dual-law cross-reference bridge: Ley 21.521 Título III ↔ NCG 514 AND Ley 19.628 ↔ NCG 514 (consent §III.D, data-protection §IV.D). NCG 514 open-finance citations integrated into by-topic, scenarios, and glossary (24 SFA terms). SKILL teaches the open-finance query path.

### Notes

- AI translation, no legal review, Spanish is authority. NCG 514 is standalone (no amending norm).

## [1.1.1] — 2026-06-02

### Changed

- **NCG 502 corpus consolidated with NCG 524** — all 116 amendments (02-dic-2024) applied; corpus directory renamed `502-psf-obligations/` → `502-psf-obligations-consolidated/`. The `corpus_status` key is renamed `ncg_502` → `ncg_502_consolidated` in `plugin.json`.
- **Indexes and SKILL.md** updated to point at `502-psf-obligations-consolidated/`; NCG 502 operational query path now reads from the consolidated dir.
- **CI** — NCG 502 quality gates updated: section-parity gate targets `502-psf-obligations-consolidated/`; round-trip gate switches from single-PDF (threshold 0.80) to dual-PDF (`--also-pdf sources/ncg_524_2024.pdf`, threshold 0.70) with 9 heavy-splice/table sections excluded (`I.A`, `I.C.2`, `II.A`, `II.F`, `III.C`, `IV.C.6`, `IV.D.4`, `VIII`, `Anexo`) — those sections were verified manually and are documented in the corpus TN notes.
- **`check_roundtrip.py`** — added `--also-pdf` flag (dual-PDF mode), `--exclude` flag, and de-hyphenation normalizer to support consolidated NCG verification.
- **`corpus/ncg/524-amendments-changelog/changes.md`** — consolidated amendment delta log built alongside the corpus.
- **Glossary reconciled with NCG 524's Anexo N°1 changes** (H.1–H.4):
  - *Renamed*: `institutional client (cliente institucional)` → `institutional investor (inversionista institucional)` with updated definition (simplified reference to Ley 18.045 Art. 4 bis(e) only; reference to NCG 410 removed per H.2).
  - *Deleted*: `counterparty risk (riesgo de contraparte)`, `credit risk (riesgo de crédito)`, `issuer credit risk (riesgo crediticio del emisor)`, `market risk (riesgo de mercado)`, `operational risk (riesgo operacional)` — all five deleted from Anexo N°1 per NCG 524 item H.4.
- **SKILL.md** — dropped the "NCG 524 amendments pending" caveat; updated citation note to reflect consolidated corpus; bumped corpus-status version to v1.1.1.

### Notes

- AI-applied consolidation; no legal review has been conducted. The Spanish original text is authoritative; the English corpus is a translation aid.
- 9 sections excluded from the round-trip fidelity gate are documented with `> **TN:**` notes in the relevant corpus files explaining why they reach lower chunk-coverage (heavy table splicing, column-interleaved extraction by pdfplumber).

## [1.1.0] — 2026-06-02

### Added

- **NCG 502 baseline corpus** (`corpus/ncg/502-psf-obligations/`) — the CMF regulation implementing Ley 21.521 Título II (registration, authorization, and obligations of financial-service providers; baseline 12-ene-2024). 117 sections (I–IX + 3 Anexos), each with section-level literal English translation and verbatim Spanish, round-trip verified against the source PDF.
- **NCG 524 amendments catalogue** (`corpus/ncg/524-amendments-changelog/`) — all 116 amendments issued in December 2024 catalogued for reference. Consolidation into the NCG 502 baseline is deferred to a future release.
- **NCG tooling** (`tools/`):
  - `extract_ncg_sections.py` — ToC-driven extractor for CMF NCG-formatted PDFs.
  - `check_ncg_parity.py` — verifies every ToC entry in `_toc.json` has a corresponding section file in the corpus.
  - `parse_524_amendments.py` — parser for NCG 524's amendment list.
  - NCG mode in `check_roundtrip.py` (`--mode ncg`) — verifies corpus Spanish text matches the NCG 502 source PDF; threshold configurable via `--threshold`.
  - All new tools have pytest coverage and two new CI gates (section parity + round-trip at threshold 0.80).
- **NCG 502 citations integrated into indexes** — `indexes/by-topic.md`, `indexes/scenarios.md`, and `indexes/cross-references.md` now include 73 law↔NCG edges mapping Ley 21.521 articles to their NCG 502 implementing sections. `indexes/glossary.md` adds ~37 NCG-defined terms.
- **SKILL.md** teaches the law↔regulation query path: for operational "how to comply" questions, look up the governing Ley 21.521 article, then follow the `-> NCG502` edges in `indexes/cross-references.md` to the relevant NCG 502 section.

### Notes

- NCG 502 is the 12-ene-2024 baseline text. NCG 524's 116 amendments are catalogued in `corpus/ncg/524-amendments-changelog/`; consolidation is pending a future release. When citing NCG 502 sections, check that changelog for any NCG 524 amendment to the cited section.
- NCG 514 (Open Finance), NCG 530 (Reporting), and NCG 503 (Idoneidad) are planned for later phases.

## [1.0.2] — 2026-05-28

### Fixed

- **`plugin.json` `skills` field rejected during `/plugin install`.** The v1.0.1 manifest declared `"skills": ["skills/chile-compliance"]`, which Claude Code's installer rejected with `Validation errors: skills: Invalid input`. The field is removed entirely — Claude Code auto-discovers skills under the conventional `skills/` directory in Claude Code 2.1.142+, so the explicit declaration was redundant and incorrectly shaped.

### Added

- `author`, `homepage`, `repository`, `license`, and `keywords` fields in `.claude-plugin/plugin.json` to satisfy `claude plugin validate` cleanly (no missing-metadata warnings).
- New CI job `validate-plugin` that runs `claude plugin validate` against both `plugin.json` and `marketplace.json` on every push/PR. This catches manifest-shape regressions before they reach a release.

### Changed

- Plugin version `1.0.1` → `1.0.2` in `plugin.json` and `marketplace.json` (both the marketplace `version` and the embedded plugin entry's `version`).

### Validation

- `claude plugin validate .claude-plugin/plugin.json` — passes with 2 expected warnings for our intentional custom fields (`corpus_status`, `sources`). Claude Code documents that unknown top-level fields are tolerated at load time.
- `claude plugin validate .claude-plugin/marketplace.json` — passes clean (0 warnings).

## [1.0.1] — 2026-05-28

### Fixed

- **Plugin installability.** The repo is now a properly-structured Claude Code plugin marketplace and can be installed with `/plugin marketplace add fjaviergallucci/chilean-compliance` followed by `/plugin install chile-compliance@chile-compliance`. The v1.0.0 release had `plugin.json` at the repo root and no `marketplace.json`, which prevented Claude Code from discovering it as a plugin.

### Added

- `.claude-plugin/marketplace.json` — single-plugin marketplace catalog. Validated with `claude plugin validate .`.

### Changed

- Moved `plugin.json` → `.claude-plugin/plugin.json` (preserves git history via `git mv`).
- Updated references to `plugin.json` in README.md, CONTRIBUTING.md, SKILL.md, and `corpus/21521-fintech/README.md` to the new path.
- README "Quick start — Claude Code" section rewritten with the proper `/plugin marketplace add` + `/plugin install` workflow, replacing the prior settings.json instructions. Added per-project / global scope guidance and a "pin to release" recipe using `#v1.0.1`.
- README "Where help is welcome" section updated — H4 closed all REVIEW markers; the contribution priority list now reflects post-v1.0.0 reality (translation corrections, new scenarios, CMF/APDP additions, other statutes).
- SKILL.md "Corpus status awareness" section updated — all three `corpus_status` entries are now `stable`; the body reflects v1.0.0+ reality.
- Removed the broken reference to `docs/superpowers/specs/` and `docs/superpowers/plans/` (those files exist in the dev history but were intentionally excluded from the public repo).

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

[Unreleased]: https://github.com/fjaviergallucci/chilean-compliance/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/fjaviergallucci/chilean-compliance/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/fjaviergallucci/chilean-compliance/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.com/fjaviergallucci/chilean-compliance/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/fjaviergallucci/chilean-compliance/releases/tag/v1.1.0
[1.0.2]: https://github.com/fjaviergallucci/chilean-compliance/releases/tag/v1.0.2
[1.0.1]: https://github.com/fjaviergallucci/chilean-compliance/releases/tag/v1.0.1
[1.0.0]: https://github.com/fjaviergallucci/chilean-compliance/releases/tag/v1.0.0
[0.1.0]: https://github.com/fjaviergallucci/chilean-compliance/releases/tag/v0.1.0
