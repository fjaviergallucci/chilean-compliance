# chile-compliance

> A structured, AI-queryable knowledge base of Chilean fintech and personal-data law — built for use by AI agents, not humans.

If you're building software that handles Chilean users' financial or personal data, your AI assistant probably needs to reason about two laws — and the CMF regulation that implements them:

- **Ley 21.521** (*Ley Fintec*, 2023) — financial-services innovation, crowdfunding, investment advisory, open finance, custody, intermediation.
- **Ley 19.628** as amended by **Ley 21.719** (*data protection*, in force **2026-12-01**) — consent, lawful basis, data-subject rights, sensitive data, breach notification, the new APDP regulator and sanctions framework.
- **NCG 502** (CMF *Norma de Carácter General*, 2024) — the implementing regulation for Ley 21.521 Título II: how financial-service providers actually register, get authorized, govern risk, secure systems, hold capital, and report. The operational layer beneath the Fintech law. Consolidated with NCG 524 (116 amendments applied).

These texts are all published in Spanish. Without help, an AI session about Chilean compliance spends most of its tokens translating, re-translating, and searching the same legal text from scratch every time. This plugin makes that knowledge available as a structured corpus with topical indexes, a glossary, scenario checklists, and a query-decision-tree skill — so your AI agent can answer compliance questions in seconds, with verifiable citations.

> [!IMPORTANT]
> This skill is **not** legal advice. It's a structured citation aid for AI agents. For decisions with material risk, consult Chilean counsel.

---

## En español

**chile-compliance** es una base de conocimiento estructurada y consultable por agentes de inteligencia artificial sobre la regulación chilena de servicios financieros y protección de datos personales. Está pensada para asistentes y agentes de IA (no para uso humano directo) que necesitan razonar sobre el cumplimiento normativo aplicable a software desarrollado para usuarios en Chile.

### Leyes incluidas

- **Ley N° 21.521 (Ley Fintec)** — promueve la competencia e inclusión financiera mediante la innovación y tecnología en la prestación de servicios financieros. Cubre plataformas de financiamiento colectivo (*crowdfunding*), asesoría crediticia y de inversión, custodia de instrumentos financieros, enrutamiento de órdenes, intermediación, sistemas alternativos de transacción y el Sistema de Finanzas Abiertas (SFA). En vigor desde el **3 de febrero de 2023**.
- **Ley N° 19.628 sobre Protección de Datos Personales** (consolidada con las modificaciones de la **Ley N° 21.719**) — regula el tratamiento de datos personales, el consentimiento del titular, los derechos del titular (acceso, rectificación, supresión, oposición, portabilidad), los datos personales sensibles, la transferencia internacional, las obligaciones del responsable y del mandatario, y crea la **Agencia de Protección de Datos Personales (APDP)** con su régimen sancionatorio. Entra en vigor el **1 de diciembre de 2026**.
- **NCG N°502 (CMF)** — norma de carácter general que implementa el Título II de la Ley 21.521: registro, autorización, obligaciones de divulgación, gobierno corporativo y gestión de riesgos, capital y garantías, y reportes de los prestadores de servicios financieros. Es la capa operativa ("cómo cumplir en la práctica"). Texto base del 12-ene-2024; las 116 modificaciones de la NCG 524 están catalogadas, consolidación pendiente.
- **NCG N°503 (CMF) — Exigencias de Idoneidad** — requisitos de acreditación de conocimientos para el personal que ejerce funciones definidas; Secciones I–IV traducidas; vinculada a Ley 21.521 arts. 7 y 9. Deroga la NCG 412.
- **NCG N°530 (CMF) — Reportes MSI Fintec (capa de obligaciones)** — cuerpo normativo (lista FINTEC01–16, creación de MSI Fintec, vigencia) + Instrucciones Generales (Anexo N°1) + catálogo derivado FINTEC01–16. Los formatos de registro (Anexo N°2/N°3) están fuera del alcance de este corpus.

### ¿Qué hay en el repositorio?

- Traducciones literales al inglés del articulado, con el texto original en español preservado verbatim en cada artículo.
- Léxico jurídico bilingüe (`corpus/_lexicon.md`) que fija las equivalencias de términos clave.
- Índices: por tema (`indexes/by-topic.md`), glosario de términos definidos (`indexes/glossary.md`), listas de verificación de cumplimiento por caso de uso (`indexes/scenarios.md`) y grafo de referencias cruzadas entre artículos (`indexes/cross-references.md`).
- Skill para Claude Code con un árbol de decisión de consultas y convenciones de citación.
- Herramientas Python de verificación con cobertura de pruebas (paridad de extracción, fidelidad del texto en español, completitud del glosario).

### Estado actual

El corpus incluye la NCG 502 consolidada con NCG 524 (116 modificaciones aplicadas, 02-dic-2024), la NCG 514 (Finanzas Abiertas), la NCG 503 (Exigencias de Idoneidad) y la NCG 530 (Reportes MSI Fintec, capa de obligaciones).

El corpus principal está en inglés, ya que ese es el idioma operativo de los agentes de IA. Las citas verbatim del texto original en español siempre están disponibles dentro de cada artículo (bloque `### Original Spanish`). Todo el articulado cuenta con traducciones literales lexicon-conformes; las notas del traductor (`> **TN:** ...`) explican los renderings que no calzan exactamente con el léxico (por ejemplo, instituciones procesales chilenas sin equivalente directo en inglés).

### Documentación completa y contribuciones

La documentación principal (instalación, uso desde Claude Code y otros hosts de IA, arquitectura, convenciones de contribución) está en inglés más abajo en este mismo archivo y en [CONTRIBUTING.md](CONTRIBUTING.md). Las contribuciones son bienvenidas, especialmente para finalizar las traducciones literales de los Títulos VI-VIII de la Ley 19.628 consolidada.

### Licencia y procedencia

El código fuente, las traducciones al inglés, los índices y la documentación se distribuyen bajo licencia [MIT](LICENSE). El texto en español de las leyes reproducido verbatim en este repositorio proviene de la **Biblioteca del Congreso Nacional de Chile (BCN)** ([leychile.cl](https://www.leychile.cl/)) y es de **dominio público** como obra del Estado de Chile. Ver [NOTICE](NOTICE) para más detalle.

> [!IMPORTANT]
> Este repositorio **no constituye asesoría legal**. Es una ayuda estructurada de citas para agentes de IA. Para decisiones con riesgo material legal o financiero, consulte a un abogado o abogada chileno/a habilitado/a.

---

## Status

| Component | Status | Notes |
|---|---|---|
| Ley 21.521 — Títulos I-IV (Fintech provisions) | **Stable** | 29 articles fully translated |
| Ley 21.521 — Título V (modifications to other statutes) | **Out of scope** | Documented as reference-only; see `corpus/21521-fintech/titulo-05-modificaciones.md` |
| Ley 19.628 consolidated — Preliminar through Título V (Arts. 1-29) | **Stable** | Core data-protection regime |
| Ley 19.628 consolidated — Títulos VI-VIII (Arts. 30-55, Agency + sanctions framework) | **Stable** | Literal translations complete (Phase H4 closed all 44 REVIEW markers) |
| Ley 21.719 amendments changelog | **Stable** | Reference only — quote consolidated 19.628 as operative law |
| NCG 502 — PSF obligations (Ley 21.521 implementing reg) | **Stable** | consolidated with NCG 524 (116 amendments applied) |
| NCG 514 — Open Finance / SFA (Ley 21.521 Título III implementing reg) | **Stable** | 80 sections across 6 Secciones |
| NCG 503 — Exigencias de Idoneidad / fit-and-proper | **Stable** | Secciones I–IV; bridged to Ley 21.521 arts. 7 & 9; derogates NCG 412 |
| NCG 530 — MSI Fintec reporting (obligations layer) | **Stable** | Body + Anexo N°1 + FINTEC01–16 catalog; record layouts (Anexo N°2/N°3) out of scope |
| Indexes (topical, glossary, scenarios, cross-references) | **Stable** | 149 topical · 82 glossary · 7 scenarios/100 items · 338 cross-refs |
| Tooling + tests | **Stable** | 32/32 pytest passing |

The `corpus_status` field in `.claude-plugin/plugin.json` is the canonical source of truth for an AI consumer.

---

## What this gives an AI

A consuming AI gets five kinds of lookup:

1. **Direct article retrieval** — *"What does Art. 8 bis of 19.628 say?"*
2. **Definition lookup** — *"Define 'datos personales sensibles'."*
3. **Scenario checklists** — *"What do I need to comply with if my feature aggregates bank statements?"*
4. **Topical search** — *"What rules cover AI-based recommendations?"*
5. **Operational/how-to lookup** — *"What does the CMF actually require us to do to register / report an incident / hold capital?"* — follows the law→regulation bridge into NCG 502.

Every answer cites a specific article in the corpus, so a human reviewer can click through and verify. Spanish original text is one hop away whenever a verbatim quote is needed.

### What a session looks like

```
You:  We're building an investment tracker that aggregates user holdings
      from Chilean brokers via Open Finance. Are we Fintec-regulated?

AI:   [reads corpus/21521-fintech/titulo-02-servicios.md#article-2,
        corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-16,
        indexes/scenarios.md (Scenario 3)]

      Read-only aggregation is unlikely to fall under Ley 21.521 Art. 2's
      enumerated services (no custody, no order routing, no advisory).
      But if you consume data through the Sistema de Finanzas Abiertas
      (SFA), you become an "information-receiving institution" under
      Ley 21.521 Art. 17 with corresponding registration and operating
      requirements. Verify against the customer-consent rules in
      Ley 21.521 Art. 23 — express, informed consent is required.

      For the personal-data side, you're a data controller under
      Ley 19.628 Art. 2(n). See the scenario checklist at
      indexes/scenarios.md (Scenario 3) for the full obligations list.
```

The AI didn't translate anything from scratch. It read curated, vetted English with Spanish on demand.

---

## Quick start — Claude Code

The plugin is published as a Claude Code plugin marketplace at this repository. Install it with two commands from any Claude Code session:

```text
/plugin marketplace add fjaviergallucci/chilean-compliance
/plugin install chile-compliance@chile-compliance
```

The first command registers this repo as a marketplace named `chile-compliance` (per `.claude-plugin/marketplace.json`). The second installs the `chile-compliance` plugin from that marketplace.

By default, plugins install at user scope (available across all your projects). To scope to one project instead:

```text
/plugin install chile-compliance@chile-compliance --scope project
```

After install, the skill activates automatically when Claude sees Chilean fintech or data-protection contexts (see `skills/chile-compliance/SKILL.md` for triggers). You can also invoke it explicitly with `/chile-compliance:chile-compliance`.

To enable, disable, or uninstall later:

```text
/plugin disable chile-compliance@chile-compliance
/plugin enable chile-compliance@chile-compliance
/plugin uninstall chile-compliance@chile-compliance
```

### Pin to a specific release

To install at a tagged version rather than `main`:

```text
/plugin marketplace add https://github.com/fjaviergallucci/chilean-compliance.git#v1.3.0
/plugin install chile-compliance@chile-compliance
```

---

## Quick start — other AI hosts

The corpus is plain markdown — it doesn't depend on Claude Code. You can use it from:

- **Custom agents (OpenAI SDK, Claude API, LangChain, etc.)** — load relevant files at session start, or use a tool-call that reads `corpus/`, `indexes/`, and `.claude-plugin/plugin.json` paths.
- **MCP server** — wrap the corpus with a thin MCP layer exposing `search`, `get_article`, `get_definition`, and `find_obligations` tools. The folder structure was designed to make this straightforward; no rework needed.
- **RAG pipelines** — embed `corpus/**/*.md` with your preferred embedding model. Each article is a self-contained chunk (English + Spanish + cross-references + source footer).
- **Manual reading** — yes, humans can read it too, though it wasn't optimized for that.

The `SKILL.md` file documents the query decision tree the corpus expects — port it to your platform's agent prompt format.

---

## What's in the box

```
chile-compliance/
├── .claude-plugin/
│   ├── marketplace.json                # Marketplace catalog (this repo as marketplace)
│   └── plugin.json                     # Plugin manifest with corpus_status
├── skills/chile-compliance/SKILL.md    # Query decision tree for consuming AIs
├── corpus/
│   ├── _lexicon.md                     # Spanish ↔ English legal-term mapping
│   ├── 21521-fintech/                  # Ley 21.521 by Título
│   ├── 19628-data-protection-consolidated/  # Ley 19.628 (post-21.719) by Título
│   ├── 21719-amendments-changelog/     # Reference: which 21.719 item changed what
│   └── ncg/                            # CMF NCG regulations
│       ├── 502-psf-obligations-consolidated/  # NCG 502 consolidated (baseline + NCG 524)
│       ├── 503-idoneidad/              # NCG 503 (fit-and-proper / Exigencias de Idoneidad)
│       ├── 514-open-finance/           # NCG 514 (Open Finance / SFA), Ley 21.521 Título III
│       ├── 524-amendments-changelog/   # NCG 524 amendments catalogue (116 items)
│       └── 530-fintec-reporting/       # NCG 530 (MSI Fintec reporting, obligations layer)
├── indexes/
│   ├── by-topic.md                     # Topical lookup, 149 citations
│   ├── glossary.md                     # 82 defined terms (English + Spanish)
│   ├── scenarios.md                    # 7 compliance scenarios, 100 checklist items
│   └── cross-references.md             # 338 article-to-article edges
├── sources/                            # Original PDF sources (BCN, public)
└── tools/                              # Python QC scripts + pytest tests
```

### Corpus file format

Each article in the corpus is a self-contained block:

```markdown
## Article N — <English short title>
**Spanish anchor:** Art. N°
**Tags:** consent, lawful-basis, ...

### Plain-English text
<Literal English translation, lexicon-conforming.>

### Original Spanish
> "<Verbatim Spanish from the PDF, preserved exactly.>"

### Cross-references
- Related articles, glossary pointers.

> **Source:** Ley 19.628 Art. N as amended by Ley 21.719 Art. 1° item M (in force 2026-12-01).
```

Translation conventions live in `corpus/_lexicon.md`. When a translator deviated from the lexicon, an inline `> **TN:**` (translator's note) explains why. Articles pending review carry `<!-- REVIEW: ... -->` markers — consuming AIs surface these as caveats.

---

## What this does NOT cover

Be explicit with your users about the corpus's limits:

- **CMF general regulations: NCG 502 only.** The corpus now includes NCG 502 (the core implementing regulation for Ley 21.521 Título II). Other CMF circulars and normas issued under Ley 21.521 Art. 4 remain out of scope until added separately.
- **No APDP guidance.** The Agencia de Protección de Datos Personales becomes operational with Ley 21.719 in force; its guidance and enforcement decisions are out of scope.
- **No case law.** Chilean Supreme Court and Court of Appeals decisions interpreting these laws aren't in the corpus.
- **No other laws.** Ley 21.521 amends Leyes 18.045 (capital markets), 18.046 (corporations), 18.840 (Central Bank), 19.220, 20.712, 20.950, and 21.000 — those amendments live in 21.521 Título V, which is documented as out-of-scope here. If your use case touches one of those statutes, you need a separate corpus.
- **Not legal advice.** Consuming AIs must say so when asked.

The skill body teaches the consuming AI to refuse questions about anything outside the corpus rather than guess.

---

## Effective-date discipline

Ley 21.719 enters into force on **2026-12-01**. Before that date:
- The operative data-protection law is the pre-21.719 Ley 19.628 (the 1999 baseline).
- The new APDP regulator, sanctions framework, and many new data-subject rights are not yet in force.

After 2026-12-01, the consolidated 19.628 in this corpus is the operative text. Every consolidated article carries a `> **Source:**` footer naming the amending 21.719 provision and the effective date. The skill teaches consuming AIs to surface this date when answering any 21.719-derived question.

The pre-amendment baseline is in git history (search for the `19628-baseline/` directory in commits before `b35f9d6` if you need it).

---

## Architecture

The build philosophy is **markdown-first, tooling-light**:

- **Source of truth**: a small set of structured markdown files in `corpus/` and `indexes/`. Editable by humans, greppable by AIs.
- **Tooling** (`tools/`): verification scripts only — no runtime servers, no embeddings, no databases. Each script is single-purpose with pytest coverage:
  - `extract_articles.py` — parses Chilean BCN-formatted PDFs into article blocks.
  - `check_extraction_parity.py` — verifies every article in a PDF appears once in the corpus.
  - `check_glossary_completeness.py` — verifies every glossary term cites a real article.
  - `check_roundtrip.py` — verifies corpus Spanish text matches the source PDF.
  - `parse_21719_amendments.py` — one-off parser for Ley 21.719's amendment list.
  - `extract_ncg_sections.py` — parses CMF NCG-format PDFs (hierarchical ToC) into section blocks.
  - `check_ncg_parity.py` — verifies every NCG section in the ToC appears once in the corpus.
  - `parse_524_amendments.py` — catalogues NCG 524's amendments to NCG 502.
- **Distribution**: a Claude Code plugin manifest (`.claude-plugin/plugin.json`) + a marketplace catalog (`.claude-plugin/marketplace.json`) + a skill (`skills/chile-compliance/SKILL.md`). The skill's frontmatter description triggers auto-activation when an AI sees fintech or data-protection contexts. The repo doubles as its own single-plugin marketplace, so a user installs it with `/plugin marketplace add` + `/plugin install`.

---

## Contributing

Translations, scenario additions, and corpus expansions are welcome. The corpus is meant to be community-improvable.

### Where help is welcome

As of v1.0.0, all article-level REVIEW markers in the corpus are resolved. The most useful contributions now are:

- **Translation corrections.** If you find an English rendering that doesn't track the Spanish, or a Chilean legal term that deserves a clearer treatment, open an issue (use the `Translation fix or improvement` template) or send a PR with the change plus a `> **TN:** ...` note explaining the rationale.
- **New scenarios.** If your real-world use case isn't covered by the seven scenarios in `indexes/scenarios.md`, add one (see [Adding a new scenario](#adding-a-new-scenario) below).
- **CMF circulars and APDP guidance.** These are out of scope today but valuable additions as they're published. See [Adding new amendments, circulars, or laws](#adding-new-amendments-circulars-or-laws) below.
- **Coverage for other Chilean statutes** that fintech-adjacent products touch — Leyes 18.045, 18.046, 18.840, etc. Each becomes its own corpus subdirectory.

### Adding a new scenario

`indexes/scenarios.md` is a compliance checklist by use case. To add one:

1. Identify the feature (e.g., "consumer credit scoring with ML").
2. Walk through the laws and identify obligations.
3. Add a `## Scenario N: <feature>` block following the existing template.
4. Every checklist item must end with an article citation like `Ley 19.628 Art. 12` and a `(See corpus/...md#article-N)` link.
5. Run the citation-resolution check (see below).

### Adding new amendments or sources

When the APDP issues guidance, when CMF publishes a circular, or when an amendment passes:

1. Drop the source PDF in `sources/`.
2. Add a new section under `corpus/` (e.g., `corpus/apdp-circular-001/`) — don't intermix.
3. Update `.claude-plugin/plugin.json` to add the new section to `corpus_status`.
4. Update `SKILL.md`'s "What this skill covers" section.

### Adding a new law entirely

If you want to add another Chilean statute (e.g., Ley 18.045 capital markets):

1. Create `corpus/18045-capital-markets/` with the same per-Título file structure.
2. Add the source PDF to `sources/`.
3. Run `python -m tools.extract_articles <pdf>` to get a baseline article inventory.
4. Translate each Título following the conventions used in `corpus/21521-fintech/`.
5. Add the law to `.claude-plugin/plugin.json` `corpus_status`.

The tooling is law-agnostic — the same scripts work on any Chilean BCN PDF following standard `Artículo N.-` / `TÍTULO N` structure. NCG-format (hierarchical, ToC-based) PDFs are handled by `extract_ncg_sections.py` instead, following the NCG 502 corpus as the pattern.

### Quality gates

Before opening a PR, run:

```bash
python -m pytest tools/tests/ -v
python -m tools.check_extraction_parity sources/Ley-21521_04-ENE-2023-1.pdf corpus/21521-fintech --exclude-titulo V
python -m tools.check_extraction_parity sources/LEY-19628_28-AGO-1999.pdf corpus/19628-data-protection-consolidated --exclude-titulo Transitorio
python -m tools.check_roundtrip sources/Ley-21521_04-ENE-2023-1.pdf corpus/21521-fintech --sample 0
python -m tools.check_roundtrip sources/LEY-19628_28-AGO-1999.pdf corpus/19628-data-protection-consolidated --sample 0
python -m tools.check_glossary_completeness indexes/glossary.md corpus/21521-fintech
python -m tools.check_glossary_completeness indexes/glossary.md corpus/19628-data-protection-consolidated
```

All eight commands must exit `0` with their "OK" message.

### Development setup

```bash
git clone <repo-url>
cd chilean-compliance
python -m pip install -r tools/requirements.txt
python -m pytest tools/tests/ -v
```

Python 3.11+ required.

---

## Source materials

Original Spanish source text is from the **Biblioteca del Congreso Nacional de Chile** (BCN, [leychile.cl](https://www.leychile.cl/)) and is public-domain Chilean government text. PDFs in `sources/` are unchanged from BCN; verbatim Spanish quoted in the corpus tracks them exactly (verified by the round-trip checker).

| Law | Source PDF |
|---|---|
| Ley 21.521 | `sources/Ley-21521_04-ENE-2023-1.pdf` |
| Ley 19.628 (1999 baseline) | `sources/LEY-19628_28-AGO-1999.pdf` |
| Ley 21.719 | `sources/Ley-21719_13-DIC-2024.pdf` |
| NCG 502 (PSF obligations, baseline) | `sources/NCG 502.pdf` |
| NCG 524 (amends NCG 502) | `sources/ncg_524_2024.pdf` |

---

## License

MIT — see [LICENSE](LICENSE).

The English translations and structural commentary are original work, released under MIT. The verbatim Spanish text reproduced in the corpus is public-domain Chilean government work and remains as such.

---

## Disclaimer

This corpus and the AI tooling around it are **not legal advice**. The translations are literal renderings made by humans assisted by AI; they may contain errors, omissions, or contextual nuances the lexicon cannot capture. Articles tagged with `<!-- REVIEW: ... -->` markers are explicitly flagged as pending review. For any decision with material legal or financial risk, consult a Chilean attorney.

The maintainers make no warranty as to the accuracy, completeness, or currency of any content in this repository.
