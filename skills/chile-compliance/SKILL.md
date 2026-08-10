---
name: chile-compliance
description: Use when reasoning about Chilean regulatory compliance for fintech (Ley 21.521) or personal data protection (Ley 19.628 as amended by Ley 21.719). Triggers on storing/processing IDs, names, contact info, bank statements; investment tracking or advisory features; AI-based recommendations, analysis, or document parsing for users in Chile; or any question citing these laws.
---

# Chile Compliance

You are answering a question about Chilean financial-services or personal-data
regulation. This corpus is the source of truth. It is **not legal advice** — it is a
structured citation aid.

## Read the policy first

**`corpus/_agent-policy.md` is authoritative** for scope, the seven operations, citation
format, caveat surfacing, and honesty about gaps. `Read` it before answering anything
non-trivial. This file is only the Claude Code *binding*: it maps those operations onto
the tools you have. Where this file and the policy appear to disagree, the policy wins.

## Effective-date discipline

Repeated here because it is the single most consequential rule and you may be invoked
without having read the policy yet.

<!-- EFFECTIVE-DATE-DISCIPLINE v1 -->
Ley 21.719 amended Ley 19.628; enforcement begins **2026-12-01**. Treat that date as a
**compliance deadline**, never as a reason to defer an answer.

- **Present-tense questions are answered from the consolidated corpus.** "What must we
  do?", "how do we build this?", "what's needed before launch?" — all answered from the
  consolidated Ley 19.628 text, because these are the obligations organisations must be
  designing and remediating against now.
- **State the obligation first, the deadline second.** Cite the article, then note that
  it must be met by 2026-12-01. Do not lead with the date, and never dismiss a
  compliance question on the ground that the law has not yet taken effect.
- **Surface the `> **Source:**` footer** on any 21.719-derived article — it names the
  amending item and the effective date.
- **Retrospective questions are the only exception.** "Was this lawful in 2024?" turns
  on the pre-amendment 1999 baseline, which is **not** in this corpus. Say so explicitly
  and point to the official BCN source (`sources/LEY-19628_28-AGO-1999.pdf` is the
  as-enacted 1999 text, not the pre-21.719 consolidated state). Do not answer a
  retrospective question from the consolidated text.

## Operation bindings

The policy defines seven operations. Here is how to perform each one:

| Operation | How to do it here |
|---|---|
| **LOCATE** | `Grep` the keyword(s) in `indexes/by-topic.md`, then RETRIEVE every citation you get back. Bullets summarise; they never substitute. |
| **RETRIEVE** | `Read` the cited corpus file and go to the `## Article N` heading (laws) or `## <anchor>` heading (NCGs, e.g. `IV.C.3.1`). Quote the *Plain-English text* and surface the `> **Source:**` footer. |
| **DEFINE** | `Grep '^## '` in `indexes/glossary.md` for the term, `Read` the matched entry, cite its `**Defined in:**` article, and pair with ORIGINAL. |
| **SCENARIO** | `Read indexes/scenarios.md`. If a scenario matches the feature, walk its checklist and RETRIEVE every cited article before summarising. If none matches, fall through to LOCATE. |
| **TRAVERSE** | `Grep` the citation in `indexes/cross-references.md` (edges read `19.628:Art.2 -> 19.628:Art.12 (reason)`). Use it both for completeness and for the law→NCG bridge — the routing table for NCG 502/514/503/530 is in the policy. |
| **ORIGINAL** | `Read` the article's `### Original Spanish` block and quote it verbatim. |
| **STATUS** | `Read .claude-plugin/plugin.json` → `corpus_status`. All entries are `stable` as of v1.3.0. |

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
| Agency (APDP) | `corpus/19628-data-protection-consolidated/titulo-06-agencia.md` |
| Sanctions framework | `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md` |
| PSF obligations (registration, capital, governance) | `corpus/ncg/502-psf-obligations-consolidated/` |
| Open finance operational rules | `corpus/ncg/514-open-finance/` |
| Personnel accreditation (idoneidad) | `corpus/ncg/503-idoneidad/` |
| CMF reporting (FINTEC01–16) | `corpus/ncg/530-fintec-reporting/` |
| Spanish ↔ English terms | `corpus/_lexicon.md` |
| Defined terms | `indexes/glossary.md` |
| Compliance scenarios | `indexes/scenarios.md` |
| Topic lookups | `indexes/by-topic.md` |
| Article-to-article links | `indexes/cross-references.md` |
| **Full behavioural policy** | `corpus/_agent-policy.md` |
