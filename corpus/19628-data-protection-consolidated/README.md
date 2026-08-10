# Ley 19.628 — Protection of Personal Data (consolidated, post-21.719)

**Status:** Operative compliance target now; enforcement begins **2026-12-01**. See *Effective-date discipline* below.
**Sources:**
- Baseline: `sources/LEY-19628_28-AGO-1999.pdf`
- Amendments: `sources/Ley-21719_13-DIC-2024.pdf` Art. 1°

This is the primary data-protection artifact in this plugin. Every article carries a footer noting which 21.719 numbered amendment(s) shaped its current wording. Amendments are tracked in `corpus/21719-amendments-changelog/changes.md`.

## Effective-date discipline

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

## Law title note
Ley 21.719 Art. 1° item 1 substituted, in the name of the law, the phrase "LA VIDA PRIVADA" with "LOS DATOS PERSONALES". The consolidated short title of the law is now "Sobre Protección de los Datos Personales" / "On the Protection of Personal Data".

## File layout
- `titulo-00-preliminar.md` — Título Preliminar (Arts. 1, 1 bis, 2, 3). General provisions, territorial scope, definitions, principles.
- `titulo-01-utilizacion.md` — Título I (Arts. 4–11). Rights of the data subject: access, rectification, erasure, opposition, automated decisions, blocking, portability, procedure. **Title content entirely replaced by item 7.**
- `titulo-02-derechos.md` — Título II (Arts. 12–16 sexies). Processing of data; consent, lawful bases, controller obligations, security, breach reporting, cession, processor relationship, DPIA, sensitive data (health, biometric), children, scientific research, geolocation. **Title content entirely replaced by item 8.**
- `titulo-03-datos-financieros.md` — Título III (Arts. 17, 18, 19). Financial / banking / commercial obligation data. Amended by items 9, 10, 11.
- `titulo-04-organismos-publicos.md` — Título IV (Arts. 20–26). Processing by public bodies. **Title content entirely replaced by item 12.**
- `titulo-05-responsabilidad.md` — Título V (Arts. 27, 28, 29). International data transfer. **Title content entirely replaced by item 13.**
- `titulo-06-agencia.md` — Título VI (Arts. 30–32 bis). Personal Data Protection Agency. **Title inserted by item 14.**
- `titulo-07-sanciones.md` — Título VII (Arts. 33–53). Sanctions, procedures, civil liability, prevention models. **Title inserted by item 14.**
- `titulo-08-organos-constitucionales.md` — Título VIII (Arts. 54–55). Processing by Congress, Judiciary, and constitutionally autonomous bodies. **Title inserted by item 14.**
- `titulo-final.md` — Título Final. **Repealed by item 15** (formerly contained Art. 24, an amendment to the Health Code).
- `transitorios.md` — Disposiciones transitorias (Arts. 1°, 2°, 3° transitorios). Amended by item 16 (paragraphs 2 and 3 of Art. 1° transitorio eliminated).

## Translation status

All articles in this consolidated corpus carry literal lexicon-conformant English translations of the verbatim Spanish. The Phase H4 review pass closed the 44 `<!-- REVIEW: -->` markers that the F2 consolidation pass had left in place; those resolutions landed in PRs #2 (Título VII), #3 (Título VI), and #4 (cleanup batch — Preliminar, III, VIII, transitorios).

Translator's notes (`> **TN:** ...`) are present where the lexicon does not directly map a Chilean legal-drafting term, where a paragraph reflects a pre-21.719 amendment layer (Título III), or where the rendering preserves a constitutional-law or administrative-law nuance.

## Audit trail
Each article in this corpus carries a "Source" footer naming the Ley 21.719 amendment item(s) that produced its current wording (where amended). The complete change index lives at `corpus/21719-amendments-changelog/changes.md`. The pre-21.719 baseline content is not carried in this corpus. Retrospective questions about the pre-amendment regime should be answered from the official BCN source, not from this consolidated text.
