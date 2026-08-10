# chile-compliance

> A structured, AI-queryable knowledge base of Chilean fintech and personal-data law. Written to be read by AI assistants, so that people can get straight, citable answers about what the law actually requires.

> [!TIP]
> **¿No eres programador/a y solo quieres saber cómo te afecta la ley?**
> No necesitas instalar nada. → **[Empieza aquí](#1-solo-quiero-saber-cómo-me-afecta-la-ley)**

If you're building software that handles Chilean users' financial or personal data, your AI assistant probably needs to reason about two laws — and the CMF regulations that implement them:

- **Ley 21.521** (*Ley Fintec*, 2023) — financial-services innovation, crowdfunding, investment advisory, open finance, custody, intermediation.
- **Ley 19.628** as amended by **Ley 21.719** (*data protection*, in force **2026-12-01**) — consent, lawful basis, data-subject rights, sensitive data, breach notification, the new APDP regulator and sanctions framework.
- **CMF implementing regulations** (*Normas de Carácter General*) — the operational layer beneath the Fintech law, telling financial-service providers how to actually comply:
  - **NCG 502** (consolidated with NCG 524, 116 amendments applied) — registration, authorization, disclosure, risk governance, security, capital, and reporting for Ley 21.521 Título II.
  - **NCG 514** — the Sistema de Finanzas Abiertas (open finance) regime under Título III: participant registration, APIs, consent, data sets, security.
  - **NCG 503** — knowledge-accreditation (fit-and-proper / *idoneidad*) requirements for personnel performing defined functions.
  - **NCG 530** — the MSI Fintec periodic-reporting obligations (the sixteen FINTEC01–16 reporting files).

These texts are all published in Spanish. Without help, an AI session about Chilean compliance spends most of its tokens translating, re-translating, and searching the same legal text from scratch every time. This plugin makes that knowledge available as a structured corpus with topical indexes, a glossary, scenario checklists, and a query-decision-tree skill — so your AI agent can answer compliance questions in seconds, with verifiable citations.

> [!IMPORTANT]
> This skill is **not** legal advice. It's a structured citation aid for AI agents. For decisions with material risk, consult Chilean counsel.

---

## How to use this — pick your path

Three ways in, by what you're trying to do. They differ in setup cost and in answer quality; the table says how.

| | **1. I want answers about my situation** | **2. I'm building software** | **3. I'm integrating the corpus** |
|---|---|---|---|
| **Who** | Business owner, lawyer, anyone non-technical | Developer using an AI coding assistant | Developer embedding this in a product or pipeline |
| **Setup** | None — download one file | Two commands (Claude Code) or one `pip install` (MCP) | Import a module, or run your own retrieval |
| **You get** | [`dist/single/`](dist/single/) — one self-contained file per law, instructions included | The Claude Code plugin, or the MCP server's seven tools | [`tools/corpus_api.py`](tools/corpus_api.py), or the raw markdown |
| **Retrieval** | Semantic — the assistant searches inside the file | **Exact** — retrieves a cited article whole, follows the cross-reference graph | Yours to choose |
| **Cross-references** | Not traversed | **Traversed**, including the 119 law→regulation bridges | Available via `get_cross_references` |
| **Stays current** | Re-download when you want the latest | Automatically | Automatically |
| **Best for** | "What does this law require of my business?" | "What must we file, build, and report?" | Custom agents, RAG, internal tools |

**Which fidelity actually matters to you.** Paths 2 and 3 retrieve exact citations and follow the graph; path 1 does not. That gap is largest for **fintech questions**, where answering "what must we actually do?" means crossing from Ley 21.521 into the CMF regulation that implements it. It is much smaller for **data-protection questions**: Ley 19.628 is standalone, with no NCG layer beneath it, so path 1 gives up very little there.

All three produce citations you can verify. None of them is legal advice.

---

## 1. Solo quiero saber cómo me afecta la ley

*(Esta sección está en español porque está dirigida a quienes consultan la ley, no a quienes programan.)*

Si tienes un negocio en Chile y quieres entender qué te exige la ley, esto toma unos dos minutos. No necesitas saber programar ni instalar nada. Funciona con ChatGPT, Claude, Gemini o cualquier asistente que permita adjuntar un archivo.

### 1. Descarga un archivo

Elige el que corresponda a tu caso, abre el enlace y presiona el botón de descarga (**Download raw file**, arriba a la derecha):

| Tu situación | Archivo |
|---|---|
| Manejo datos de personas: nombres, RUT, correos, datos de salud, historial de compras… | **[proteccion-datos.md](dist/single/proteccion-datos.md)** (486 KB) |
| Ofrezco servicios financieros: inversiones, crowdfunding, asesoría, custodia, pagos… | **[fintech.md](dist/single/fintech.md)** (296 KB) |

Cada archivo trae la ley completa, listas de verificación organizadas por tipo de negocio y un glosario de términos legales.

### 2. Adjúntalo a una conversación

Abre tu asistente de IA (ChatGPT, Claude, Gemini…), presiona el clip 📎 y sube el archivo que descargaste.

### 3. Copia y pega este mensaje

```text
Adjunté un archivo con legislación chilena estructurada. Léelo y sigue las
instrucciones que trae al inicio.

Actúa como asistente de cumplimiento normativo. Antes de darme recomendaciones:

1. Pregúntame qué hace mi negocio y qué datos de personas manejo.
2. Busca en el archivo la lista de verificación que corresponda a mi caso.
3. Explícame en español, sin tecnicismos, qué debo hacer y para cuándo.
4. Cita siempre el artículo específico en el que te basas.

Importante: la fiscalización empieza el 1 de diciembre de 2026, pero las
obligaciones ya están definidas y debo prepararme desde ahora. No me digas que
"todavía no entra en vigencia": dime qué tengo que hacer y cuál es el plazo.

Empecemos: ¿qué necesitas saber sobre mi negocio?
```

Eso es todo. El asistente te preguntará por tu negocio y te irá indicando las obligaciones que aplican, citando los artículos para que puedas verificarlos o mostrárselos a un abogado.

### Cómo obtener mejores respuestas

- **Describe tu negocio en concreto.** «Tengo una tienda online, guardo nombre, RUT, dirección e historial de compras, y uso un servicio de correos masivos» sirve mucho más que «¿qué dice la ley?». El archivo trae listas de verificación organizadas por lo que hace una empresa en la práctica, y con esa descripción el asistente puede encontrar la que te corresponde.
- **Pide el texto original en español** cuando algo importe de verdad: *«muéstrame el texto original en español de ese artículo»*. El corpus está en inglés con el español textual incluido, así que tu respuesta pasa por una traducción de ida y vuelta; el original elimina esa duda.
- **Un tema por conversación.** Las conversaciones largas se desvían y el asistente pierde de vista las instrucciones del archivo.
- **Pregunta qué te falta.** *«¿Qué otras obligaciones aplican a mi caso que no hayamos revisado?»* suele sacar puntos que la primera respuesta omitió.

### Preguntas frecuentes

**¿Sirve con la versión gratuita?** Adjuntar un archivo a una conversación normal es la vía más disponible. Si tu plan no te deja subirlo, prueba con el archivo más pequeño (`fintech.md`).

**¿Funciona con Claude, Gemini u otro asistente?** Sí. El archivo es texto plano y las instrucciones van dentro, así que el procedimiento es el mismo.

**¿Tengo que volver a descargarlo?** Solo si quieres la versión más reciente. Los archivos se regeneran automáticamente cuando cambia el corpus.

**¿Y si uso esto todos los días?** Si tu plan permite crear un Proyecto o un GPT personalizado, sube los 13 archivos de [`dist/knowledge/`](dist/knowledge/) y pega [`dist/instructions-gpt.md`](dist/instructions-gpt.md) en el campo de instrucciones. Las instrucciones quedan siempre presentes en lugar de depender de que el asistente las encuentre dentro del archivo.

**¿Hay algo mejor todavía?** Sí: las rutas 2 y 3, que recuperan el artículo exacto y siguen el grafo de referencias cruzadas. Requieren instalar algo. Si tienes cerca a alguien que programe, pídele que consulte por ti las preguntas de mayor riesgo — obtendrá las citas exactas y tú te ahorras la instalación.

> [!IMPORTANT]
> Esto **no es asesoría legal**. Es una ayuda para encontrar y citar los artículos que te aplican. Para decisiones con riesgo legal o financiero relevante, consulta a un abogado o abogada en Chile.

---

## 2. I'm building software

You want exact citations and real cross-reference traversal, inside the tool you already work in. Two options depending on your assistant.

**Pros:** retrieves the cited article whole rather than a similar-looking fragment; follows the 119 law→regulation bridges, so "what must we file and report?" reaches the CMF regulation instead of stopping at the statute; always current with the repo; all laws and regulations available at once, not one file per question.
**Cons:** requires an install. The MCP route needs Python 3.11+ and a server process running locally.

### Claude Code — install the plugin

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

### Cursor, ChatGPT connectors, Claude Desktop — run the MCP server

The corpus does not depend on Claude Code. For every other host, the bundled MCP server is the way in:

```bash
python -m pip install -r tools/mcp/requirements.txt
python -m tools.mcp.server
```

Full setup, per-client configuration, and the tool reference are in [`tools/mcp/README.md`](tools/mcp/README.md). The server exposes seven tools — `search_topics`, `get_article`, `get_definition`, `get_scenario`, `get_cross_references`, `get_spanish_original`, `get_corpus_status` — and hands the connecting model the full text of `corpus/_agent-policy.md` as its MCP instructions, so it inherits the behavioural policy without a second copy existing anywhere.

---

## 3. I'm integrating the corpus

You're building your own agent, pipeline, or internal tool and want the corpus underneath it.

**Pros:** full control over retrieval and presentation; no server process if you don't want one; the resolver is pure stdlib with no dependency to adopt.
**Cons:** you become responsible for delivering the agent policy. If `corpus/_agent-policy.md` doesn't reach your model, the effective-date discipline goes with it — and that is the rule most likely to produce a confidently wrong answer.

- **Import the resolver.** [`tools/corpus_api.py`](tools/corpus_api.py) implements the same seven operations the MCP server exposes — `parse_citation`, `get_article`, `get_definition`, `search_topics`, `get_scenario`, `get_cross_references`, `get_corpus_status`. Pure stdlib; it parses the indexes into memory on first use, with no database.
- **RAG pipelines.** Embed `corpus/**/*.md` with your preferred model. Each article is a self-contained chunk (English + Spanish + cross-references + source footer). Put `corpus/_agent-policy.md` in your system prompt.
- **Uploaded knowledge files** (Custom GPTs, Projects). Upload the 13 files in [`dist/knowledge/`](dist/knowledge/) — under the usual 20-file cap — and paste [`dist/instructions-gpt.md`](dist/instructions-gpt.md) into the instructions field. Both are generated from the corpus and CI fails if they drift, so they are never stale. Retrieval is semantic, so the fidelity note in the table applies.
- **Reading it directly.** The corpus is plain markdown. It was not optimised for human reading, but nothing stops you.
- **Manual reading** — humans can read it, though it was not optimised for that.

---

## En español

**chile-compliance** es una base de conocimiento estructurada y consultable por agentes de inteligencia artificial sobre la regulación chilena de servicios financieros y protección de datos personales. Está escrita para que la lea un asistente de IA, de modo que las personas obtengan respuestas directas y citables sobre lo que exige la ley. Si solo quieres consultarla con un asistente de IA, ve a [Solo quiero saber cómo me afecta la ley](#1-solo-quiero-saber-cómo-me-afecta-la-ley); el resto de esta sección describe el contenido y está dirigido a quienes desarrollan software.

### Leyes incluidas

- **Ley N° 21.521 (Ley Fintec)** — promueve la competencia e inclusión financiera mediante la innovación y tecnología en la prestación de servicios financieros. Cubre plataformas de financiamiento colectivo (*crowdfunding*), asesoría crediticia y de inversión, custodia de instrumentos financieros, enrutamiento de órdenes, intermediación, sistemas alternativos de transacción y el Sistema de Finanzas Abiertas (SFA). En vigor desde el **3 de febrero de 2023**.
- **Ley N° 19.628 sobre Protección de Datos Personales** (consolidada con las modificaciones de la **Ley N° 21.719**) — regula el tratamiento de datos personales, el consentimiento del titular, los derechos del titular (acceso, rectificación, supresión, oposición, portabilidad), los datos personales sensibles, la transferencia internacional, las obligaciones del responsable y del mandatario, y crea la **Agencia de Protección de Datos Personales (APDP)** con su régimen sancionatorio. Entra en vigor el **1 de diciembre de 2026**.
- **NCG N°502 (CMF)** — norma de carácter general que implementa el Título II de la Ley 21.521: registro, autorización, obligaciones de divulgación, gobierno corporativo y gestión de riesgos, capital y garantías, y reportes de los prestadores de servicios financieros. Es la capa operativa ("cómo cumplir en la práctica"). Texto base del 12-ene-2024, consolidada con las 116 modificaciones de la NCG 524 (02-dic-2024).
- **NCG N°514 (CMF) — Sistema de Finanzas Abiertas (SFA)** — implementa el Título III de la Ley 21.521: perímetro del SFA, registro de participantes, operación de APIs, consentimiento, conjuntos de datos, seguridad y resguardos. 6 Secciones, 80 secciones traducidas. Sus reglas de consentimiento (§III.D) y protección de datos (§IV.D) se vinculan a la Ley 19.628.
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

La documentación principal (instalación, uso desde Claude Code y otros hosts de IA, arquitectura, convenciones de contribución) está en inglés más abajo en este mismo archivo y en [CONTRIBUTING.md](CONTRIBUTING.md). Las contribuciones son bienvenidas, especialmente la revisión legal humana de las traducciones (hechas con asistencia de IA, sin revisión jurídica), nuevos escenarios de cumplimiento, y la cobertura de otras normas a medida que se publiquen (circulares de la CMF, guías de la APDP).

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
| Indexes (topical, glossary, scenarios, cross-references) | **Stable** | 198 topical · 109 glossary · 7 scenarios/122 items · 392 cross-refs |
| Tooling + tests | **Stable** | 98/98 pytest passing |
| Consumption paths | **Stable** | Claude Code plugin · MCP server (7 tools) · generated `dist/` bundles |

The `corpus_status` field in `.claude-plugin/plugin.json` is the canonical source of truth for an AI consumer.

---

## What this gives an AI

A consuming AI gets five kinds of lookup:

1. **Direct article retrieval** — *"What does Art. 8 bis of 19.628 say?"*
2. **Definition lookup** — *"Define 'datos personales sensibles'."*
3. **Scenario checklists** — *"What do I need to comply with if my feature aggregates bank statements?"*
4. **Topical search** — *"What rules cover AI-based recommendations?"*
5. **Operational/how-to lookup** — *"What does the CMF actually require us to do to register / report an incident / hold capital / accredit staff?"* — follows the law→regulation bridge into the NCG layer (502 Título II, 514 open finance, 503 idoneidad, 530 reporting).

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

## What's in the box

```
chile-compliance/
├── .claude-plugin/
│   ├── marketplace.json                # Marketplace catalog (this repo as marketplace)
│   └── plugin.json                     # Plugin manifest with corpus_status
├── skills/chile-compliance/SKILL.md    # Claude Code binding over the agent policy
├── corpus/
│   ├── _agent-policy.md                # Host-neutral agent policy (source of truth)
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
├── dist/                               # GENERATED — regenerate, never hand-edit
│   ├── instructions-gpt.md             # Instruction text for hosted assistants
│   └── knowledge/                      # Corpus merged into 13 upload-ready files
├── sources/                            # Original PDF sources (BCN, public)
└── tools/
    ├── corpus_api.py                   # Resolver for the seven operations (stdlib only)
    ├── build_dist.py                   # Generates dist/ (CI fails if it is stale)
    ├── mcp/                            # MCP server — the binding for non-Claude hosts
    └── tests/                          # pytest coverage for QC scripts and resolver
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

- **CMF general regulations: NCG 502, 514, 503, and 530.** The corpus includes the four in-scope implementing NCGs (502 Título II obligations, 514 open finance, 503 idoneidad, 530 MSI Fintec reporting). NCG 530's field-level record layouts (Anexo N°2/N°3) and other CMF circulars/normas issued under Ley 21.521 Art. 4 remain out of scope until added separately.
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
- **Policy vs. bindings**: `corpus/_agent-policy.md` is the host-neutral behavioural contract — scope, the seven operations (LOCATE, RETRIEVE, DEFINE, SCENARIO, TRAVERSE, ORIGINAL, STATUS), citation format, effective-date discipline, caveat surfacing. Everything that consumes the corpus is a thin *binding* that maps those operations onto one host's retrieval mechanism: `skills/chile-compliance/SKILL.md` for Claude Code, `tools/mcp/` for MCP clients. Behaviour is changed in the policy, never in a binding, so hosts cannot drift apart. A test rejects host-specific tooling names in the policy file.
- **Tooling** (`tools/`): verification scripts plus a resolver and an MCP server. No embeddings and no databases — `tools/corpus_api.py` parses the indexes into memory on first use and is pure stdlib, and the MCP SDK is isolated in `tools/mcp/requirements.txt` so the verification gates never depend on it. Each verification script is single-purpose with pytest coverage:
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
- **CMF circulars and APDP guidance.** These are out of scope today but valuable additions as they're published. See [Adding new amendments or sources](#adding-new-amendments-or-sources) below.
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

These cover the two laws. The NCG 502/514/503/530 parity and round-trip gates are listed in full in [CONTRIBUTING.md](CONTRIBUTING.md). Every gate command must exit `0` with its "OK" message, and `pytest` must be fully green (98 tests).

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
| NCG 514 (Open Finance / SFA) | `sources/ncg_514_2024.pdf` |
| NCG 503 (Exigencias de Idoneidad) | `sources/ncg_503_2024.pdf` |
| NCG 530 (MSI Fintec reporting) | `sources/ncg_530_2025-2.pdf` |

---

## License

MIT — see [LICENSE](LICENSE).

The English translations and structural commentary are original work, released under MIT. The verbatim Spanish text reproduced in the corpus is public-domain Chilean government work and remains as such.

---

## Disclaimer

This corpus and the AI tooling around it are **not legal advice**. The translations are literal renderings made by humans assisted by AI; they may contain errors, omissions, or contextual nuances the lexicon cannot capture. Articles tagged with `<!-- REVIEW: ... -->` markers are explicitly flagged as pending review. For any decision with material legal or financial risk, consult a Chilean attorney.

The maintainers make no warranty as to the accuracy, completeness, or currency of any content in this repository.
