---
name: chile-compliance
description: Use when reasoning about Chilean regulatory compliance for fintech (Ley 21.521) or personal data protection (Ley 19.628 as amended by Ley 21.719). Triggers on storing/processing IDs, names, contact info, bank statements; investment tracking or advisory features; AI-based recommendations, analysis, or document parsing for users in Chile; or any question citing these laws.
---

# Chile Compliance

You are answering a question about Chilean financial-services or
personal-data regulation. Use this skill's corpus as the source of truth.

## What this skill covers
- **Ley 21.521 (Fintec)** — financial-services innovation; in force since 2023-02-03.
- **Ley 19.628 (Data Protection), consolidated with Ley 21.719 amendments** — in force from **2026-12-01**.
- **NCG 502 (baseline, 12-ene-2024)** — the CMF regulation implementing Ley 21.521 Título II: PSF registration, per-service authorization, disclosure, corporate governance & risk management, capital & guarantees, operational capacity, and reporting. The operational "how to comply in practice" layer. *NCG 524's 116 amendments (Dec 2024) are catalogued in `corpus/ncg/524-amendments-changelog/` but not yet consolidated — cite the baseline and check that changelog for any amended section.*

**Mental model:** laws define *what* must be done; NCGs define *how* to comply in practice. For operational questions ("what must we file / build / approve / report?"), check the NCG layer, not just the law.

**Out of scope:** NCG 524 consolidation (pending — amendments catalogued only); NCG 514 / 530 / 503 (planned, later phases); NCG 454 / 504 / 461 (out of scope); CMF circulars not in `sources/`; APDP guidance; sector-specific regulation; case law; Título V of Ley 21.521 (modifications to other statutes); and anything not in `sources/`. If asked about anything beyond what is covered above, say so explicitly.

## Where the corpus is
- `corpus/21521-fintech/titulo-NN-<slug>.md` — Ley 21.521 articles by Título (I-IV translated; V is out-of-scope reference only).
- `corpus/19628-data-protection-consolidated/titulo-NN-<slug>.md` — consolidated 19.628 by Título.
- `corpus/21719-amendments-changelog/` — reference only; do NOT quote as operative law.
- `corpus/ncg/502-psf-obligations/seccion-*.md` and `anexo-*.md` — NCG 502 baseline by section.
- `corpus/ncg/524-amendments-changelog/` — NCG 524 amendments catalogue (reference; not yet consolidated).
- `corpus/_lexicon.md` — Spanish↔English terms.
- `indexes/by-topic.md` — topical index.
- `indexes/glossary.md` — defined terms.
- `indexes/scenarios.md` — pre-built compliance checklists.
- `indexes/cross-references.md` — article-to-article graph.

## Query decision tree

### "What does Article N of <law> say?"
1. `Read corpus/<law>/titulo-NN-*.md`.
2. Find the `## Article N` anchor; quote the Plain-English text.
3. If the user wants the original wording or asks for an exact quote, also include the `### Original Spanish` block.
4. Surface the `> **Source:**` footer if present — it identifies the amending 21.719 provision and the 2026-12-01 effective date.

### "Define <term>"
1. `Grep '^## ' indexes/glossary.md` for the term.
2. `Read` the matched section.
3. Cite the `**Defined in:**` article and quote the English definition.

### "What applies to <scenario>?"
1. `Read indexes/scenarios.md`.
2. If a scenario matches the user's feature, walk through its checklist; each item ends in an article citation.
3. `Read` each cited article in full before summarizing — the checklist items summarize, they do not substitute.
4. If no scenario matches, fall through to topical lookup.

### "What does the CMF actually require in practice for <X>?" (operational/how-to)
1. Find the governing Ley 21.521 article.
2. `Grep` `indexes/cross-references.md` for `-> NCG502` edges from that article.
3. `Read` the cited NCG 502 section in `corpus/ncg/502-psf-obligations/`.
4. Cite as `NCG 502 §<section>`. Note it is the 12-ene-2024 baseline; check `corpus/ncg/524-amendments-changelog/_amendments.json` for any NCG 524 amendment to that section.

### Topical question ("What does the law say about X?")
1. `Grep` the keyword(s) in `indexes/by-topic.md`.
2. `Read` each cited article block in the corpus.
3. Cross-check using `indexes/cross-references.md`: when you read Art. N, look for `19.628:Art.N -> ...` lines to find implicated articles.

## Citation format

Cite as `Ley 19.628 Art. 8(g)` or `Ley 21.521 Art. 3(2)` or `NCG 502 §IV.C.3.1` (NCG number, § symbol, hierarchical section). For NCG 502 citations, note it is the 12-ene-2024 baseline and flag if `corpus/ncg/524-amendments-changelog/_amendments.json` catalogues an NCG 524 amendment to the cited section. For the consolidated 19.628:
- Always note the amending 21.719 provision and the 2026-12-01 effective date when citing post-amendment articles. This information is in the article's `> **Source:**` footer.
- **Never** quote 21.719 amendment instructions ("Sustitúyase artículo X por...") as if they were operative law. The operative text lives in the consolidated corpus under 19.628 article numbers.

## Effective-date discipline

- Ley 21.719 enters into force **2026-12-01**.
- For any 21.719-derived provision, state whether the question concerns pre- or post-2026-12-01 systems.
- If the user does not specify a timeframe, default to **post-2026-12-01** (forward-looking compliance) and say so explicitly.
- Pre-effective-date questions need the pre-amendment Ley 19.628. The baseline isn't in the active corpus anymore but exists in git history (search the repo's git log for the 19628-baseline directory before commit `b35f9d6`).

## Spanish-on-demand

- Default surface: English.
- Quote the `### Original Spanish` block verbatim when:
  - The user/calling AI asks for an exact quote.
  - The meaning is contested or the user is challenging a translation.
  - You're answering a definition question (definitions are best confirmed via the Spanish original).

## Caveat surfacing

When citing an article that carries any of these markers, surface the marker alongside the citation:

- `<!-- REVIEW: <reason> -->` — translation is pending human review. Tell the user: "Note: this article's translation is under human review — verify against the Spanish original before acting." Provide the Spanish original.
- `> **TN:** <translator's note>` — quote the translator's note so the user understands a non-literal rendering.

## Corpus status awareness

Read `.claude-plugin/plugin.json` → `corpus_status`. As of v1.0.0:

- `21521_fintech: stable` — covers Títulos I-IV. Título V is out of scope.
- `19628_consolidated: stable` — all Títulos fully translated (literal lexicon-conformant English with verbatim Spanish).
- `21719_changelog: stable` — reference only.
- `ncg_502: stable` — NCG 502 baseline (12-ene-2024), fully translated. NCG 524 amendments pending consolidation.
- `ncg_514_open_finance`, `ncg_530_reporting`, `ncg_503_idoneidad`: `planned` (later phases).

When citing from a law whose status is anything other than `stable`, prepend "Translation status: <status> — verify the Spanish original before relying on the English text."

When citing from a `partial` or `draft` law, prepend: "Translation status: partial — verify the Spanish original before relying on the English text."

## Honesty about gaps

- This skill is **not** legal advice; it is a structured citation aid.
- For decisions with material risk, recommend the user consult counsel.
- If the question depends on facts outside the corpus (a CMF circular, an APDP fine, a Supreme Court ruling, sector-specific rules), say so explicitly.
- If the user asks about a Chilean law NOT covered by this plugin (e.g., Ley 18.045 capital markets, Ley 18.046 corporations), tell them this skill covers only Ley 21.521 and Ley 19.628 — direct them to the official source.
- If the user asks about Título V of Ley 21.521, point them to `corpus/21521-fintech/titulo-05-modificaciones.md` (out-of-scope note) and the original PDF.

## Quick reference — file paths

| Need | Path |
|---|---|
| Fintech scope / regulated services | `corpus/21521-fintech/titulo-02-servicios.md` |
| Open Finance system | `corpus/21521-fintech/titulo-03-finanzas-abiertas.md` |
| Suitability + bank-access | `corpus/21521-fintech/titulo-04-otras-disposiciones.md` |
| Data definitions | `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md` |
| Lawful processing | `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md` |
| Data subject rights | `corpus/19628-data-protection-consolidated/titulo-02-derechos.md` |
| Financial / credit data | `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md` |
| Public bodies | `corpus/19628-data-protection-consolidated/titulo-04-organismos-publicos.md` |
| International transfers | `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md` |
| Agency (APDP) | `corpus/19628-data-protection-consolidated/titulo-06-agencia.md` (partial) |
| Sanctions framework | `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md` (partial) |
| Defined terms | `indexes/glossary.md` |
| Compliance scenarios | `indexes/scenarios.md` |
| Topic lookups | `indexes/by-topic.md` |
| Article-to-article links | `indexes/cross-references.md` |
