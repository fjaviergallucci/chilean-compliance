# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

**chile-compliance** — an AI-queryable corpus of Chilean fintech and data-protection law, distributed as a Claude Code plugin (this repo is its own single-plugin marketplace via `.claude-plugin/marketplace.json`) and as an MCP server for every other host. The deliverable is structured markdown: literal English translations of Ley 21.521 (Fintec), Ley 19.628 consolidated with Ley 21.719 amendments, and four CMF implementing regulations (NCG 502+524 consolidated, 514, 503, 530). Python in `tools/` verifies the corpus against the source PDFs and serves it; there are no embeddings and no database.

`.claude-plugin/plugin.json` (`corpus_status`) is the canonical machine-readable statement of what's covered. `corpus/_agent-policy.md` is the host-neutral behavioural contract consuming AIs follow; `skills/chile-compliance/SKILL.md` is the Claude Code binding over it.

## Commands

```bash
python -m pip install -r tools/requirements.txt       # Python 3.11+, verification tooling
python -m pip install -r tools/mcp/requirements.txt   # only if working on the MCP server
python -m pytest tools/tests/ -v                      # all tests (must be fully green)
python -m pytest tools/tests/test_check_roundtrip.py -v          # one test file
python -m pytest tools/tests/test_check_roundtrip.py -k <name>   # one test
python -m tools.mcp.server                            # run the MCP server over stdio
```

Quality gates (CI runs all of these on every PR — see `.github/workflows/test.yml` for the authoritative list and exact flags):

```bash
# Laws: parity (every PDF article appears once in corpus) + round-trip (Spanish matches PDF) + glossary
python -m tools.check_extraction_parity sources/Ley-21521_04-ENE-2023-1.pdf corpus/21521-fintech --exclude-titulo V
python -m tools.check_roundtrip sources/Ley-21521_04-ENE-2023-1.pdf corpus/21521-fintech --sample 0
python -m tools.check_glossary_completeness indexes/glossary.md corpus/21521-fintech
# (same three for corpus/19628-data-protection-consolidated with sources/LEY-19628_28-AGO-1999.pdf, --exclude-titulo Transitorio)

# NCGs: parity against each corpus dir's _toc.json + round-trip in --mode ncg
python -m tools.check_ncg_parity corpus/ncg/514-open-finance/_toc.json corpus/ncg/514-open-finance
python -m tools.check_roundtrip sources/ncg_514_2024.pdf corpus/ncg/514-open-finance --mode ncg --threshold 0.80
# NCG 502 is special: dual-PDF (--also-pdf sources/ncg_524_2024.pdf), threshold 0.70, several --exclude sections
```

Every gate must exit 0 with its "OK" message. NCG round-trips run at threshold 0.80 (0.70 for 502) due to known pdfplumber page-break artifacts; law round-trips use the default.

CI also runs `claude plugin validate` on both `.claude-plugin/*.json` manifests.

## Architecture

- **`corpus/`** — source of truth. One directory per law (`21521-fintech/`, `19628-data-protection-consolidated/`) split by Título, and `corpus/ncg/<num>-<slug>/` per CMF regulation split by Sección. `*-amendments-changelog/` dirs are reference-only — never cite them as operative law. Leading-underscore files are meta, not articles: `corpus/_lexicon.md` is the authoritative Spanish↔English term mapping, `corpus/_agent-policy.md` is the agent policy (below).
- **`indexes/`** — derived lookup layers: `by-topic.md`, `glossary.md`, `scenarios.md` (compliance checklists), `cross-references.md` (article-to-article edges, including law→NCG bridges like `-> NCG502`).
- **`tools/`** — one single-purpose verification script each, with pytest coverage. Law-format PDFs (BCN `Artículo N.-` structure) use `extract_articles.py` / `check_extraction_parity.py`; NCG-format PDFs (hierarchical ToC) use `extract_ncg_sections.py` / `check_ncg_parity.py` driven by a per-corpus `_toc.json`. Separately, `corpus_api.py` resolves citations and parses the indexes for runtime consumers, and `mcp/` is the MCP server over it.
- **`sources/`** — unmodified BCN/CMF PDFs. The round-trip checker enforces that corpus Spanish tracks them exactly.
- **`dist/`** — **generated, committed, never hand-edited.** Knowledge bundles and ChatGPT instruction text for hosts that can't run the MCP server. Regenerate with `python -m tools.build_dist`; CI's `dist-freshness` job runs `--check` and fails on drift. The instruction file is a *projection* of the policy: the effective-date rule, citation format, and caveat surfacing are carried verbatim, and only host-specific parts are rewritten. It sits near the 8,000-character field limit, so if the builder warns, trim the projection in `build_dist.py` rather than truncating legal guidance.
- **`docs/superpowers/`** — design specs and implementation plans from past corpus-expansion phases; useful as patterns when adding a new NCG. Gitignored.

### Policy vs. bindings

`corpus/_agent-policy.md` (marked `<!-- AGENT-POLICY v1 -->`) is the single source of truth for how a consuming AI should behave: scope, the seven operations (LOCATE, RETRIEVE, DEFINE, SCENARIO, TRAVERSE, ORIGINAL, STATUS), citation format, caveat surfacing, honesty about gaps, and the law→NCG routing table. It is deliberately host-neutral — `tools/tests/test_agent_policy.py` fails the build if it names any host's tooling.

Everything else is a *binding* that maps those operations onto one host's retrieval mechanism and defers to the policy for the rest. There are two: `skills/chile-compliance/SKILL.md` (Claude Code tools) and `tools/mcp/server.py` (MCP tools, which delegate to `tools/corpus_api.py`). **Add behaviour to the policy, not to a binding** — a rule written into a binding is invisible to every other consumer.

The MCP server passes the policy file verbatim to clients as its MCP `instructions`, so connecting models inherit it with no second copy. `tools/tests/test_mcp_server.py` asserts the tool surface is exactly the seven operations and that the policy plus date banner reach the client.

**Dependency boundary:** `tools/corpus_api.py` is pure stdlib and the MCP SDK lives only in `tools/mcp/requirements.txt`, so the corpus verification gates never need it. The MCP tests `importorskip` when the SDK is absent, and CI runs them in a separate `mcp-server` job. Keep it that way — don't add `mcp` to `tools/requirements.txt`.

### Corpus article format

Each article/section is a self-contained block: `## Article N — <title>`, `**Spanish anchor:**`, `**Tags:**`, `### Plain-English text`, `### Original Spanish` (blockquoted verbatim), `### Cross-references`, and a `> **Source:**` footer naming the amending provision and effective date. NCG sections use the same shape with a hierarchical anchor (`## I.C.1 — <title>`).

**This structure is now load-bearing at runtime, not just in CI.** `tools/corpus_api.py` parses these headings and `###` subsections, and the index formats too: `cross-references.md` edges as `LAW:Art.N -> LAW:Art.M (reason)`, glossary entries as `## term (término)` plus `**Defined in:**`, `by-topic.md` as `## Topic:` headings with indented child bullets carrying the citations, and `scenarios.md` as `## Scenario N:` with `- [ ]` items. Changing any of those shapes breaks retrieval for every MCP client — run `pytest tools/tests/test_corpus_api.py` after touching index structure.

## Hard rules

- **Never edit the `### Original Spanish` blocks** — they are verbatim from the PDF, typos included (`como como` stays `como como`). The English translation fixes it; the round-trip gate will fail otherwise.
- **Lexicon-conforming translations**: pull terms from `corpus/_lexicon.md`. Obligation verbs are rigorous: *deberá* → must, *podrá* → may, *no podrá* → shall not, *quedará obligado* → shall be obligated. Non-literal renderings get an inline `> **TN:** ...` note explaining why. Passages needing human review get `<!-- REVIEW: <reason> -->` markers.
- **Numbering preserved exactly**: `Art. 2 lit. g) número 3` → `Art. 2(g)(3)`.
- **Effective-date discipline**: enforcement of the 21.719-amended Ley 19.628 begins **2026-12-01**, and that date is a *compliance deadline*, not a switch deciding which text to quote. The consolidated corpus is the operative answer to any present-tense question ("what must we do?") because organisations must be designing against it now; state the obligation, then the deadline. Only genuinely retrospective questions fall back to the 1999 baseline, which is **not** in this corpus. The canonical wording lives behind `<!-- EFFECTIVE-DATE-DISCIPLINE v1 -->` and must appear byte-identically in all four `indexes/*.md`, `corpus/_agent-policy.md`, `corpus/19628-data-protection-consolidated/README.md`, and `SKILL.md` — `tools/tests/test_effective_date_discipline.py` enforces presence and bans deferral phrasing. Never drop a `> **Source:**` footer, which carries the per-article date.
- **Scenario checklist items** in `indexes/scenarios.md` must each end with an article citation and a `(See corpus/...md#article-N)` link — `check_glossary_completeness` and citation checks enforce resolvability.
- **Translation-status claims must match `plugin.json`.** Don't write "pending review" / "(partial)" into an index or binding unless `corpus_status` actually says so; `tools/tests/test_no_stale_review_markers.py` enforces it. `<!-- REVIEW: -->` markers are for corpus articles only — meta files (READMEs, leading-underscore) may describe the convention.

## Adding content — files that must move together

Adding a new law/NCG/circular touches all of: the PDF in `sources/`, a new `corpus/` subdirectory (never intermix with existing law dirs), `corpus_status` + `sources` in `.claude-plugin/plugin.json`, the **Scope** and **Corpus layout** sections of `corpus/_agent-policy.md` (not `SKILL.md` — the binding no longer carries scope), the `SKILL.md` quick-reference path table, the `_BUNDLES` list and `_SCOPE` text in `tools/build_dist.py` plus a regenerated `dist/`, the README status table, and new gate steps in `.github/workflows/test.yml` (plus CONTRIBUTING's gate list). NCG corpora also need a `_toc.json` for the parity checker.

`tools/tests/test_build_dist.py` catches the `_BUNDLES` omission — it asserts every corpus file lands in exactly one bundle — but nothing catches a stale `_SCOPE` or `_SINGLE_BUNDLES`, so update those deliberately.

`dist/single/` is the non-technical entry point: two self-contained Spanish-instructed files (`proteccion-datos.md`, `fintech.md`) that a user attaches to one chat, reached from the README's **Empieza aquí** section. They must stay under ~1 MB to remain attachable, and their Spanish header — not just the English banner — carries the effective-date rule, because that audience is asking what to do *now*. If you add a law that a business owner would plausibly ask about, consider whether it needs its own single-file bundle rather than only appearing in `dist/knowledge/`.

If the new source has its own in-force date, decide explicitly whether it needs deadline framing like the 19.628 banner, and say so in its corpus README either way.

## Conventions

- Conventional commits (`feat:`, `fix:`, `docs:`, `chore:`, `test:`), optional scope like `feat(21521):` or `fix(tools):`. One logical change per PR; PR descriptions list which quality gates were run.
- This corpus is a citation aid, not legal advice — content changes must cite articles rather than assert legal conclusions.
