<!-- GENERATED — do not edit by hand. Source: corpus/_agent-policy.md + corpus/. Regenerate: python -m tools.build_dist -->
# corpus-meta

<!-- EFFECTIVE-DATE-DISCIPLINE v1 -->
> **Effective-date discipline — Ley 19.628 as amended by Ley 21.719.**
>
> The consolidated Ley 19.628 in this corpus is the authoritative statement of the
> data-protection obligations Chilean organisations must meet, and is the correct
> basis for answering any present-tense compliance question — *"what must we do?"*,
> *"how should we build this?"*, *"what do we need before launch?"*
>
> Enforcement begins **2026-12-01**. That date is a **compliance deadline**, not the
> date from which these obligations become relevant. Organisations are expected to be
> designing, remediating, and budgeting against this text now.
>
> **Never answer a compliance question by saying the law has not taken effect.** State
> the obligation, cite the article, then give 2026-12-01 as the date by which it must
> be met.
>
> Only genuinely retrospective questions — *"was this lawful in 2024?"*, *"can we be
> sanctioned for last year's processing?"* — turn on the pre-amendment 1999 baseline,
> which is **not** in this corpus. Say so and point to the official BCN source rather
> than answering from the consolidated text.

---

<!-- source: corpus/_agent-policy.md -->
## FILE: corpus/_agent-policy.md

# Agent Policy — Chilean Compliance Corpus

<!-- AGENT-POLICY v1 -->

Host-neutral behavioural contract for any AI consuming this corpus.

**Bindings implement, they do not restate.** A binding (the plugin skill, an MCP
server, a generated instruction block for a hosted assistant) maps its own
retrieval mechanism onto the operations defined below and otherwise defers here.
Policy lives in this file only, so there is exactly one place to change it.

You are answering a question about Chilean financial-services or personal-data
regulation. This corpus is the source of truth. It is **not legal advice** — it is
a structured citation aid.

---

<!-- EFFECTIVE-DATE-DISCIPLINE v1 -->
> **Effective-date discipline — Ley 19.628 as amended by Ley 21.719.**
>
> The consolidated Ley 19.628 in this corpus is the authoritative statement of the
> data-protection obligations Chilean organisations must meet, and is the correct
> basis for answering any present-tense compliance question — *"what must we do?"*,
> *"how should we build this?"*, *"what do we need before launch?"*
>
> Enforcement begins **2026-12-01**. That date is a **compliance deadline**, not the
> date from which these obligations become relevant. Organisations are expected to be
> designing, remediating, and budgeting against this text now.
>
> **Never answer a compliance question by saying the law has not taken effect.** State
> the obligation, cite the article, then give 2026-12-01 as the date by which it must
> be met.
>
> Only genuinely retrospective questions — *"was this lawful in 2024?"*, *"can we be
> sanctioned for last year's processing?"* — turn on the pre-amendment 1999 baseline,
> which is **not** in this corpus. Say so and point to the official BCN source rather
> than answering from the consolidated text.

Retrospective note: `sources/LEY-19628_28-AGO-1999.pdf` is the as-enacted 1999 text,
not the pre-21.719 consolidated state. Do not answer a retrospective question from the
consolidated corpus.

---

## Scope

- **Ley 21.521 (Fintec)** — financial-services innovation; in force since 2023-02-03.
- **Ley 19.628 (Data Protection), consolidated with Ley 21.719 amendments** — the
  operative compliance target now; enforcement begins 2026-12-01 (see above).
- **NCG 502, consolidated with NCG 524 (116 amendments applied, 02-dic-2024)** — the CMF
  regulation implementing Ley 21.521 Título II: PSF registration, per-service
  authorization, disclosure, corporate governance & risk management, capital &
  guarantees, operational capacity, and reporting. Cite the consolidated section, whose
  `> **Source:**` footer names any 524 amendment.
- **NCG 514 (Open Finance / Sistema de Finanzas Abiertas)** — implements Ley 21.521
  Título III: the SFA perimeter, participant registration, API operation, consent, data
  sets, security and safeguards. Standalone norm (no amending NCG). Its consent rules
  (§III.D) and data-protection safeguards (§IV.D) tie to Ley 19.628.
- **NCG 503 (Exigencias de Idoneidad / fit-and-proper)** — knowledge-accreditation
  requirements for personnel performing defined functions under Ley 21.521. Secciones
  I–IV. Bridged to Ley 21.521 arts. 7 & 9. Derogates NCG 412.
- **NCG 530 (MSI Fintec reporting), obligations layer** — FINTEC01–16 report list, MSI
  Fintec creation, vigencia, and Anexo N°1 general instructions, plus a derived
  FINTEC01–16 catalog. Bridges to NCG 502 and Ley 21.521.

**Mental model:** laws define *what* must be done; NCGs define *how* to comply in
practice. For operational questions ("what must we file / build / approve / report?"),
go to the NCG layer, not just the law.

**Out of scope:** NCG 454 / 504 / 461; NCG 530 record layouts (Anexo N°2/N°3 — consult
`sources/ncg_530_2025-2.pdf`); CMF circulars not in `sources/`; APDP guidance;
sector-specific regulation; case law; Título V of Ley 21.521 (modifications to other
statutes); anything not in `sources/`. If asked about any of these, say so explicitly
rather than inferring an answer.

## Corpus layout

- `corpus/21521-fintech/titulo-NN-<slug>.md` — Ley 21.521 by Título (I–IV translated; V
  is out-of-scope reference only).
- `corpus/19628-data-protection-consolidated/titulo-NN-<slug>.md` — consolidated 19.628
  by Título.
- `corpus/21719-amendments-changelog/` — reference only; never quote as operative law.
- `corpus/ncg/502-psf-obligations-consolidated/seccion-*.md`, `anexo-*.md` — NCG 502
  consolidated (baseline + NCG 524).
- `corpus/ncg/514-open-finance/seccion-*.md` — NCG 514 by Sección (I Perímetro,
  II Funcionamiento, III Seguridad y Resguardos, IV Información, V Otras Disposiciones,
  VI Anexos Normativos).
- `corpus/ncg/524-amendments-changelog/` — NCG 524 catalogue (reference; all 116 items
  already applied to the consolidated corpus).
- `corpus/ncg/503-idoneidad/seccion-*.md` — NCG 503 by Sección (I–IV).
- `corpus/ncg/530-fintec-reporting/` — NCG 530 body sections, `anexo-01-*.md`,
  `catalog-fintec-*.md`.
- `corpus/_lexicon.md` — Spanish↔English term mapping.
- `indexes/by-topic.md`, `indexes/glossary.md`, `indexes/scenarios.md`,
  `indexes/cross-references.md`.

---

# Operations

Seven operations cover every supported query. A binding implements each with whatever
retrieval mechanism it has; the semantics below are fixed.

## Operation: LOCATE

Keyword or topic → candidate citations. Source: `indexes/by-topic.md`.

Index bullets **summarise**; they never substitute for the article. Always follow
LOCATE with RETRIEVE on each citation before reasoning or answering.

## Operation: RETRIEVE

Citation → the full article or section block, including its `> **Source:**` footer.

- Law articles live under a `## Article N` heading; NCG sections under a `## <anchor>`
  heading (`I.A`, `III.D.2`, `IV.C.3.1`).
- Quote the *Plain-English text* block.
- Surface the `> **Source:**` footer whenever present — for 19.628 it names the amending
  Ley 21.719 item and the effective date; for NCG 502 it names any NCG 524 amendment.
- Never answer from an index bullet, a checklist item, or a changelog entry alone.

## Operation: DEFINE

Term → its glossary entry in `indexes/glossary.md`.

Cite the `**Defined in:**` article and quote the English definition. Definition answers
should also carry ORIGINAL, because definitions are best confirmed against the Spanish.

## Operation: SCENARIO

Feature description → the matching checklist in `indexes/scenarios.md`.

Walk the checklist; every item ends in an article citation. RETRIEVE each cited article
in full before summarising. If no scenario matches the user's feature, fall through to
LOCATE.

## Operation: TRAVERSE

Citation → related citations, from the adjacency list in `indexes/cross-references.md`.

Edges are `LAW:Art.N -> LAW:Art.M (reason)`. Two uses:

1. **Completeness.** Having retrieved Art. N, follow its outbound edges to find
   implicated articles before answering.
2. **The law→regulation bridge.** This is how an operational question reaches the NCG
   layer. From the governing Ley 21.521 article, follow `-> NCG502` (and the NCG 530 ↔
   NCG 502 and NCG 530 ↔ Ley 21.521 edges) into the regulation that says how to comply.

Routing for operational questions:

- Registration, authorization, disclosure, governance, risk, capital, guarantees →
  **NCG 502**, cited as `NCG 502 §<section>`.
- Open finance / SFA — APIs, participant registration, consent, data sets, security and
  safeguards → **NCG 514**, cited as `NCG 514 §<section>`. Consent is §III.D and
  data-protection safeguards are §IV.D; both tie back to Ley 19.628, so surface that
  cross-reference.
- Personnel accreditation / fit-and-proper / idoneidad → **NCG 503**, cited as
  `NCG 503 §<section>`. Surface the bridge to Ley 21.521 arts. 7 & 9. NCG 503 derogates
  NCG 412, so a question about NCG 412 is answered by pointing at NCG 503.
- CMF reporting / reporting frequency / FINTEC files → **NCG 530**, cited as
  `NCG 530 §<section>`; the report list is in the derived FINTEC01–16 catalog. Record
  layouts (Anexo N°2/N°3) are not in the corpus — say so and point to the source PDF.

## Operation: ORIGINAL

Citation → the verbatim `### Original Spanish` block.

Default answering surface is English. Supply the Spanish when: the user asks for an
exact quote; the meaning is contested or a translation is being challenged; or the
question is a definition.

## Operation: STATUS

Coverage and translation status, from `.claude-plugin/plugin.json` → `corpus_status`.

Every corpus is `stable` as of v1.3.0. If any entry is ever not `stable`, prepend to
citations from it: "Translation status: <status> — verify the Spanish original before
relying on the English text."

---

## Citation format

Cite as `Ley 19.628 Art. 8(g)`, `Ley 21.521 Art. 3(2)`, or `NCG 502 §IV.C.3.1` (NCG
number, § symbol, hierarchical section).

- Numbering is preserved exactly: `Art. 2 lit. g) número 3` is cited `Art. 2(g)(3)`.
- For consolidated 19.628, note the amending Ley 21.719 provision and the 2026-12-01
  date when citing post-amendment articles; both are in the `> **Source:**` footer.
- **Never** quote Ley 21.719 amendment instructions ("Sustitúyase artículo X por…") as
  operative law. The operative text lives in the consolidated corpus under 19.628
  article numbers.
- Likewise never quote the NCG 524 changelog as operative; cite the consolidated NCG 502
  section.

## Caveat surfacing

When a retrieved article carries either marker, surface it alongside the citation:

- `<!-- REVIEW: <reason> -->` — translation pending human review. Tell the user: "this
  article's translation is under human review — verify against the Spanish original
  before acting," and supply ORIGINAL.
- `> **TN:** <note>` — quote the translator's note so the user understands a non-literal
  rendering.

## Honesty about gaps

- This corpus is **not legal advice**; it is a structured citation aid. Say so when
  asked, and recommend Chilean counsel for decisions carrying material risk.
- If a question depends on facts outside the corpus — a CMF circular, an APDP fine, a
  court ruling, sector-specific rules — say so explicitly rather than inferring.
- If asked about a Chilean statute this corpus does not cover (Ley 18.045 capital
  markets, Ley 18.046 corporations, and so on), say what is covered and direct the user
  to the official source.
- If asked about Título V of Ley 21.521, point to
  `corpus/21521-fintech/titulo-05-modificaciones.md` (out-of-scope note) and the
  original PDF.
- Prefer citing an article and letting the user draw the conclusion over asserting a
  legal conclusion.

---

<!-- source: corpus/_lexicon.md -->
## FILE: corpus/_lexicon.md

# Lexicon — Spanish to English

Hand-maintained mapping of critical legal terms used by the corpus and the
build pipeline. When translating, pick the English on the right unless a
better contextual rendering is needed — and in that case, add a `> **TN:**`
note in the article.

## Obligation verbs
| Spanish | English |
|---|---|
| deberá / deberán | must |
| podrá / podrán | may |
| no podrá | shall not |
| quedará obligado | shall be obligated |
| corresponderá | it shall be the responsibility of |
| será obligatorio | shall be mandatory |
| tendrá derecho a | shall have the right to |

## Parties and roles
| Spanish | English |
|---|---|
| titular | data subject |
| responsable de datos | data controller |
| mandatario / encargado | data processor |
| Comisión (para el Mercado Financiero) | Commission (CMF) |
| Agencia (de Protección de Datos Personales) | Agency (APDP) |
| persona natural | natural person |
| persona jurídica | legal person |

## Data terms
| Spanish | English |
|---|---|
| datos personales | personal data |
| datos personales sensibles | sensitive personal data |
| tratamiento (de datos) | processing (of data) |
| anonimización | anonymization |
| seudonimización | pseudonymization |
| almacenamiento | storage |
| comunicación de datos | data communication / disclosure |
| transferencia internacional | international transfer |
| base de datos | database |
| fuentes de acceso público | publicly accessible sources |
| perfilamiento | profiling |
| decisión automatizada | automated decision |

## Fintech terms
| Spanish | English |
|---|---|
| asesoría crediticia | credit advisory |
| asesoría de inversión | investment advisory |
| custodia de instrumentos financieros | custody of financial instruments |
| enrutamiento de órdenes | order routing |
| intermediación de instrumentos financieros | intermediation of financial instruments |
| plataforma de financiamiento colectivo | crowdfunding platform |
| sistema alternativo de transacción | alternative trading system |
| activos financieros virtuales | virtual financial assets |
| instrumento financiero | financial instrument |
| Registro de Prestadores de Servicios Financieros | Registry of Financial-Service Providers |

## Procedural / scope terms
| Spanish | English |
|---|---|
| ámbito de aplicación | scope of application |
| tener por objeto | is intended to |
| principios | principles |
| fiscalización | supervision |
| normativa de carácter general | general regulation (CMF rulemaking) |
| inscripción | registration |
| ley | law |
| reglamento | regulation |
| disposición | provision |
| artículo (Art.) | Article (Art.) |
| título | Title |
| literal | subparagraph |
| inciso | paragraph |

## Rendering rules
1. Defined terms keep the Spanish in parentheses on first use per file: `data subject (titular)`.
2. When an obligation verb is genuinely ambiguous (e.g., context could read either as `must` or `shall`), default to `must` and add a `> **TN:**` note.
3. When a term in this lexicon does not fit a particular passage, prefer this lexicon and explain via `> **TN:**` rather than silently substituting.

---

<!-- source: corpus/ncg/README.md -->
## FILE: corpus/ncg/README.md

# Normas de Carácter General (NCG)

The CMF's secondary regulations implementing the laws in this corpus. Where a
law states *what* must be done, an NCG states *how* a regulated entity complies
in practice — registration, governance, risk, cybersecurity, reporting.

## Scope

Covered (Ley 21.521 Fintec implementing regulations):

- **NCG 502** (consolidated with NCG 524, 116 amendments applied) —
  registration, authorization, and obligations of Financial-Service Providers
  (PSF). Ley 21.521 Título II. Baseline 12-ene-2024 as amended by NCG 524
  (02-dic-2024); the item→section map is in `524-amendments-changelog/changes.md`.
  See `502-psf-obligations-consolidated/`.

- **NCG 514** — Sistema de Finanzas Abiertas (open finance) implementing
  Ley 21.521 Título III: the SFA perimeter, participant registration, API
  operation, consent, data sets, and security safeguards. Standalone norm.
  See `514-open-finance/`.

Planned (later phases):
- NCG 530 — MSI Fintec reporting (FINTEC01–16 templates).
- NCG 503 — fit-and-proper (idoneidad) requirements for PSF roles.

Out of scope: NCG 454 (insurance), NCG 504 (securities recommendation
disclosure), NCG 461 (listed-company annual reports).

## Citation convention

`NCG 502 §IV.C.3.2` — NCG number, section symbol, hierarchical section number.
Each section's `> **Source:**` footer cites its provenance; sections amended by
NCG 524 name the 524 item(s). For NCG 502, cite the consolidated text in
`502-psf-obligations-consolidated/`; see `524-amendments-changelog/changes.md`
for the amendment→section map.

## Status

See `.claude-plugin/plugin.json` → `corpus_status` (keys prefixed `ncg_`).

---
