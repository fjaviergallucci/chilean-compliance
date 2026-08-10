<!-- GENERATED — do not edit by hand. Source: corpus/_agent-policy.md + corpus/. Regenerate: python -m tools.build_dist -->
# 19628-data-protection

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

<!-- source: corpus/19628-data-protection-consolidated/README.md -->
## FILE: corpus/19628-data-protection-consolidated/README.md

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

---

<!-- source: corpus/19628-data-protection-consolidated/titulo-00-preliminar.md -->
## FILE: corpus/19628-data-protection-consolidated/titulo-00-preliminar.md

# Ley 19.628 — Título Preliminar: General Provisions (Disposiciones generales — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** In force from 2026-12-01.

> **Law title note:** Ley 21.719 Art. 1° item 1 substituted, in the name of the law, the phrase "LA VIDA PRIVADA" with "LOS DATOS PERSONALES". The consolidated short title of the law is therefore "Sobre Protección de los Datos Personales" / "On the Protection of Personal Data".

---

## Article 1 — Purpose and scope of application
**Spanish anchor:** Art. 1°
**Tags:** scope, processing, fundamental-rights, purpose, applicable-law, press-carveout

### Plain-English text

This law is intended to regulate the form and conditions under which the processing (tratamiento) and protection of the personal data (datos personales) of natural persons (personas naturales) is carried out, in accordance with Article 19, No. 4, of the Political Constitution of the Republic.

Every processing of personal data carried out by a natural or legal person, including public bodies (órganos públicos), must respect the rights and liberties of persons and shall be subject to the provisions of this law.

The regime of data processing and protection established by this law shall not apply to the processing of data carried out in the exercise of the freedoms to express opinions and to inform, governed by the laws referred to in Article 19, No. 12, of the Political Constitution of the Republic. Social media (medios de comunicación social) shall be subject to the provisions of this law in respect of any processing of data they carry out for a purpose other than to express opinions or inform.

The rules of this law shall likewise not apply to the processing of data carried out by natural persons in connection with their personal activities.

> **TN:** This article was entirely replaced by Ley 21.719 Art. 1° item 2. The new text expands the scope of the law beyond "registries or databases" (the 1999 baseline framing) to all processing, anchors the law in the right protected by Art. 19, No. 4, of the Constitution, and adds a personal-activities (household) exemption analogous to the GDPR.

### Original Spanish

> Artículo 1°.- Objeto y ámbito de aplicación. La
> presente ley tiene por objeto regular la forma y condiciones
> en la cual se efectúa el tratamiento y protección de los
> datos personales de las personas naturales, en conformidad
> al artículo 19, N° 4, de la Constitución Política de la
> República.
> Todo tratamiento de datos personales que realice una
> persona natural o jurídica, incluidos los órganos
> públicos, debe respetar los derechos y libertades de las
> personas y quedará sujeto a las disposiciones de esta ley.
> El régimen de tratamiento y protección de datos
> establecido en esta ley no se aplicará al tratamiento de
> datos que se realice en el ejercicio de las libertades de
> emitir opinión y de informar reguladas por las leyes a que
> se refiere el artículo 19, N° 12, de la Constitución
> Política de la República. Los medios de comunicación
> social quedarán sujetos a las disposiciones de esta ley en
> lo relativo al tratamiento de datos que efectúen con una
> finalidad distinta a la de opinar e informar.
> Tampoco serán aplicables las normas de la presente ley
> al tratamiento de datos que efectúen las personas naturales
> en relación con sus actividades personales.

### Cross-references
- Art. 1° bis (territorial scope of application).
- Art. 19 No. 4 and No. 12, Chilean Political Constitution.
- Art. 12, Art. 13 (lawful bases for processing).

> **Source:** Ley 19.628 Art. 1° as substituted by Ley 21.719 Art. 1° item 2 (in force 2026-12-01).

---

## Article 1 bis — Territorial scope of application
**Spanish anchor:** Art. 1° bis
**Tags:** territorial-scope, extraterritoriality, establishment, controller, processor, offering-goods-services, monitoring

### Plain-English text

The provisions of this law shall apply to the processing of personal data (tratamiento de datos personales) carried out under any of the following circumstances:

a) Where the data controller (responsable) or data processor (mandatario) is established or constituted in the national territory.

b) Where the data processor (mandatario), regardless of its place of establishment or incorporation, carries out the processing operations on personal data on behalf of a data controller established or constituted in the national territory.

c) Where the data controller or data processor is not established in the national territory but its personal-data processing operations are aimed at offering goods or services to data subjects (titulares) located in Chile — regardless of whether the data subjects are required to pay — or at monitoring the behaviour of data subjects located in the national territory, including its analysis, tracking, profiling (perfilamiento), or prediction of behaviour.

This law shall also apply to the processing of personal data carried out by a data controller that, without being established in the national territory, is subject to national legislation by virtue of a contract or of international law.

> **TN:** New article introduced by Ley 21.719 Art. 1° item 3. The territorial-scope framework parallels GDPR Art. 3 (establishment, processor-on-behalf, and targeting/monitoring criteria). "Mandatario" is rendered as "data processor" per the lexicon; "responsable" as "data controller".

### Original Spanish

> Artículo 1° bis.- Ámbito de aplicación
> territorial. Las disposiciones de la presente ley se
> aplicarán al tratamiento de datos personales que se realice
> bajo cualquiera de las siguientes circunstancias:
> a) Cuando el responsable o mandatario estén
> establecidos o constituidos en el territorio nacional.
> b) Cuando el mandatario, con independencia de su lugar
> de establecimiento o constitución, realice las operaciones
> de tratamiento de datos personales a nombre de un
> responsable establecido o constituido en el territorio
> nacional.
> c) Cuando el responsable o mandatario no se encuentren
> establecidos en el territorio nacional pero sus operaciones
> de tratamiento de datos personales estén destinadas a
> ofrecer bienes o servicios a titulares que se encuentren en
> Chile, independientemente de si a éstos se les requiere un
> pago, o a monitorear el comportamiento de titulares que se
> encuentran en el territorio nacional, incluyendo su
> análisis, rastreo, perfilamiento o predicción de
> comportamiento.
> La presente ley también se aplicará al tratamiento de
> datos personales que sea realizado por un responsable al
> que, sin estar establecido en el territorio nacional, le
> resulte aplicable la legislación nacional a causa de un
> contrato o del derecho internacional.

### Cross-references
- Art. 1 (purpose and scope of application).
- Art. 2 (definitions: responsable / mandatario / titular).

> **Source:** Ley 19.628 Art. 1° bis as inserted by Ley 21.719 Art. 1° item 3 (in force 2026-12-01).

---

## Article 2 — Definitions
**Spanish anchor:** Art. 2°
**Tags:** definitions, storage, disclosure, sensitive-data, personal-data, publicly-accessible-sources, anonymization, pseudonymization, database, controller, subject, processing, consent, access, rectification, erasure, opposition, portability, cession, profiling, agency

### Plain-English text

For the purposes of this law:

a) **Storage of data** (almacenamiento de datos): the conservation or custody of data in a registry or database.

b) **Blocking of data** (bloqueo de datos): the temporary suspension of any processing operation on stored data.

c) **Communication of personal data** (comunicación de datos personales): the act by which the data controller, in any form, discloses personal data to persons other than the data subject (titular) to whom the data concern, without amounting to cession (cesión) or transfer thereof.

d) **Expired data** (dato caduco): data that has lost its currency by operation of law, by fulfilment of a condition or expiry of the period set for its validity, or — if no express rule exists — by a change in the facts or circumstances it records.

e) **Statistical data** (dato estadístico): data that, at its origin or as a result of its processing, cannot be associated with an identified or identifiable data subject.

f) **Personal data** (dato personal): any information linked or referring to an identified or identifiable natural person. A person shall be deemed identifiable when their identity may be determined, directly or indirectly, in particular by reference to one or more identifiers — such as the name, the identity-card (cédula de identidad) number, or the analysis of elements particular to the physical, physiological, genetic, mental, economic, cultural, or social identity of that person.

In determining whether a person is identifiable, account shall be taken of all the means and objective factors that could reasonably be used for that identification at the time of the processing.

g) **Sensitive personal data** (datos personales sensibles): those personal data which refer to the physical or moral characteristics of persons, or to facts or circumstances of their private life or intimacy, that reveal racial or ethnic origin; political, trade-union, or guild affiliation; socio-economic situation; ideological or philosophical convictions; religious beliefs; data relating to health, to the human biological profile, biometric data; and information relating to a person's sexual life, sexual orientation, and gender identity.

h) **Erasure or cancellation of data** (eliminación o cancelación de datos): the destruction of data stored in registries or databases, by whatever procedure is employed.

i) **Publicly accessible sources** (fuentes de acceso público): all those databases or sets of personal data whose access or consultation may be lawfully effected by any person — such as the Official Gazette (Diario Oficial), the media, or the public registries provided by law. The processing of personal data originating from publicly accessible sources shall be subject to the provisions of this law.

j) **Public bodies** (organismos públicos): the authorities, State organs, and bodies described and regulated by the Political Constitution of the Republic, and those covered by the second paragraph of Article 1 of Law No. 18.575, the Organic Constitutional Law on the General Bases of State Administration. (Former subparagraph k; renumbered following the elimination of the former subparagraph j on "modification of data" by Ley 21.719 Art. 1° item 5.dos.)

k) **Anonymization** (anonimización): the irreversible procedure by which personal data can no longer be linked or associated with a particular person, nor permit their identification, because the link with the information that links, associates, or identifies that person has been destroyed or eliminated. Anonymized data ceases to be personal data.

l) **Pseudonymization** (seudonimización): the processing of personal data carried out in such a way that the data can no longer be attributed to a data subject without using additional information, provided that such additional information is kept separately and is subject to technical and organisational measures designed to ensure that the personal data is not attributed to an identified or identifiable natural person.

m) **Personal database** (base de datos personales): an organised set of personal data, whatever its purpose, form, or modality of creation, storage, organisation, and access, that permits the data to be related to one another, and the carrying out of any processing on them.

n) **Data controller** (responsable de datos / responsable): any natural or legal person, public or private, that decides on the purposes and means of the processing of personal data, regardless of whether the data are processed directly by it or through a third-party mandatary or processor (tercero mandatario o encargado).

ñ) **Data subject** (titular de datos / titular): a natural person, identified or identifiable, to whom the personal data concern or refer.

o) **Processing of data** (tratamiento de datos): any operation or set of operations or technical procedures, whether automated or not, that permit the collection, processing, storage, communication, transmission, or use, in any form, of personal data or sets of personal data.

p) **Consent** (consentimiento): any free, specific, unequivocal, and informed manifestation of will, given through a statement or a clear affirmative action, by which the data subject, their legal representative, or mandatary, as appropriate, authorises the processing of the personal data that concern them.

q) **Right of access** (derecho de acceso): the right of the data subject to request and obtain from the controller confirmation as to whether their personal data are being processed by it, to access them as appropriate, and to obtain the information provided for in this law.

r) **Right of rectification** (derecho de rectificación): the right of the data subject to request and obtain from the controller the modification or completion of their personal data, when they are being processed by it and are inaccurate, outdated, or incomplete.

s) **Right of erasure** (derecho de supresión): the right of the data subject to request and obtain from the controller the deletion or erasure of their personal data, in accordance with the grounds provided by law.

t) **Right of opposition** (derecho de oposición): the right of the data subject to request and obtain from the controller that a given processing of data not be carried out, in accordance with the grounds provided by law.

u) **Right to portability of personal data** (derecho a la portabilidad de los datos personales): the right of the data subject to request and obtain from the controller a copy of their personal data in a structured, generic, and commonly used electronic format, which can be operated by different systems, and to be able to communicate or transfer them to another data controller. The data subject shall have the right to have their personal data transmitted directly from controller to controller where technically feasible.

v) **Cession of personal data** (cesión de datos personales): the transfer of personal data by a data controller to another data controller.

w) **Profiling** (elaboración de perfiles): any form of automated processing of personal data that consists in using such data to evaluate, analyse, or predict aspects relating to the professional performance, economic situation, health, personal preferences, interests, reliability, behaviour, location, or movements of a natural person.

x) **Third-party mandatary or processor** (tercero mandatario o encargado): the natural or legal person that processes personal data on behalf of the data controller.

y) **Agency** (Agencia): the Personal Data Protection Agency (Agencia de Protección de Datos Personales).

z) **National Registry of Sanctions and Compliance** (Registro Nacional de Sanciones y Cumplimiento): a public national registry administered by the Agency, recording certified prevention models, the data controllers that have adopted them, and the sanctions imposed on data controllers that have infringed the law.

> **TN:** The definitions article was extensively reworked by Ley 21.719 Art. 1° item 5. Item 4 prepended the epigraph "Definiciones." to the article. Item 5.uno replaced subparagraphs a, c, f, g, and i. Item 5.dos eliminated the former subparagraph j (modification of data), causing all subsequent subparagraphs to renumber by one letter. Item 5.tres substituted the former l, m, n, ñ, and o (now k, l, m, n, ñ, and o) with new definitions of anonymization, pseudonymization, database, controller, subject, and processing. Items 5.cuatro and 5.cinco added new subparagraphs p–u (consent, access, rectification, erasure, opposition, portability) and v–z (cession, profiling, processor, Agency, sanctions registry).
>
> The former subparagraph d (expired data), e (statistical data), and h (erasure or cancellation) survive from the 1999 baseline without textual modification by 21.719. The former subparagraph b (blocking) likewise survives. The 1999 baseline subparagraph j ("modification of data") was eliminated; the concept survives indirectly through the new right of rectification (subparagraph r) and remains relevant for the historical Art. 6 framework which is replaced by the new rights regime in Title I.

### Original Spanish

> Artículo 2°.- Definiciones. Para los efectos de esta ley se
> entenderá por:
> a) Almacenamiento de datos: la conservación o custodia
> de datos en un registro o base de datos.
> b) Bloqueo de datos, la suspensión temporal de
> cualquier operación de tratamiento de los datos
> almacenados.
> c) Comunicación de datos personales: dar a conocer por
> el responsable de datos, de cualquier forma, datos
> personales a personas distintas del titular a quien
> conciernen los datos, sin llegar a cederlos o transferirlos.
> d) Dato caduco, el que ha perdido actualidad por
> disposición de la ley, por el cumplimiento de la condición
> o la expiración del plazo señalado para su vigencia o, si
> no hubiese norma expresa, por el cambio de los hechos o
> circunstancias que consigna.
> e) Dato estadístico, el dato que, en su origen, o como
> consecuencia de su tratamiento, no puede ser asociado a un
> titular identificado o identificable.
> f) Dato personal: cualquier información vinculada o
> referida a una persona natural identificada o identificable.
> Se considerará identificable toda persona cuya identidad
> pueda determinarse, directa o indirectamente, en particular
> mediante uno o más identificadores, tales como el nombre,
> el número de cédula de identidad, el análisis de
> elementos propios de la identidad física, fisiológica,
> genética, psíquica, económica, cultural o social de dicha
> persona.
> Para determinar si una persona es identificable
> deberán considerarse todos los medios y factores objetivos
> que razonablemente se podrían usar para dicha
> identificación en el momento del tratamiento.
> g) Datos personales sensibles: tendrán esta condición
> aquellos datos personales que se refieren a las
> características físicas o morales de las personas o a
> hechos o circunstancias de su vida privada o intimidad, que
> revelen el origen étnico o racial, la afiliación
> política, sindical o gremial, la situación
> socioeconómica, las convicciones ideológicas o
> filosóficas, las creencias religiosas, los datos relativos
> a la salud, al perfil biológico humano, los datos
> biométricos, y la información relativa a la vida sexual, a
> la orientación sexual y a la identidad de género de una
> persona natural.
> h) Eliminación o cancelación de datos, la
> destrucción de datos almacenados en registros o bancos de
> datos, cualquiera fuere el procedimiento empleado para ello.
> i) Fuentes de acceso público: todas aquellas bases de
> datos o conjuntos de datos personales, cuyo acceso o
> consulta puede ser efectuada en forma lícita por cualquier
> persona, tales como el Diario Oficial, medios de
> comunicación o los registros públicos que disponga la ley.
> El tratamiento de datos personales provenientes de fuentes
> de acceso público se someterá a las disposiciones de esta
> ley.
> j) Organismos públicos, las autoridades, órganos del
> Estado y organismos, descritos y regulados por la
> Constitución Política de la República, y los comprendidos
> en el inciso segundo del artículo 1º de la ley N° 18.575,
> Orgánica Constitucional de Bases Generales de la
> Administración del Estado.
> k) Anonimización: procedimiento irreversible en
> virtud del cual un dato personal no puede vincularse o
> asociarse a una persona determinada, ni permitir su
> identificación, por haberse destruido o eliminado el nexo
> con la información que vincula, asocia o identifica a esa
> persona. Un dato anonimizado deja de ser un dato personal.
> l) Seudonimización: tratamiento de datos personales
> que se efectúa de manera tal que ya no puedan atribuirse a
> un titular sin utilizar información adicional, siempre que
> dicha información adicional figure por separado y esté
> sujeta a medidas técnicas y organizativas destinadas a
> garantizar que los datos personales no se atribuyan a una
> persona natural identificada o identificable.
> m) Base de datos personales: conjunto organizado de
> datos personales, cualquiera sea la finalidad, forma o
> modalidad de su creación, almacenamiento, organización y
> acceso, que permita relacionar los datos entre sí, así
> como realizar su tratamiento.
> n) Responsable de datos o responsable: toda persona
> natural o jurídica, pública o privada, que decide acerca
> de los fines y medios del tratamiento de datos personales,
> con independencia de si los datos son tratados directamente
> por ella o a través de un tercero mandatario o encargado.
> ñ) Titular de datos o titular: persona natural,
> identificada o identificable, a quien conciernen o se
> refieren los datos personales.
> o) Tratamiento de datos: cualquier operación o
> conjunto de operaciones o procedimientos técnicos, de
> carácter automatizado o no, que permitan de cualquier forma
> recolectar, procesar, almacenar, comunicar, transmitir o
> utilizar datos personales o conjuntos de datos personales.
> p) Consentimiento: toda manifestación de voluntad
> libre, específica, inequívoca e informada, otorgada a
> través de una declaración o una clara acción afirmativa,
> mediante la cual el titular de datos, su representante legal
> o mandatario, según corresponda, autoriza el tratamiento de
> los datos personales que le conciernen.
> q) Derecho de acceso: derecho del titular de datos a
> solicitar y obtener del responsable, confirmación acerca de
> si sus datos personales están siendo tratados por él,
> acceder a ellos en su caso, y a la información prevista en
> esta ley.
> r) Derecho de rectificación: derecho del titular de
> datos a solicitar y obtener del responsable, que modifique o
> complete sus datos personales, cuando están siendo tratados
> por él, y sean inexactos, desactualizados o incompletos.
> s) Derecho de supresión: derecho del titular de datos
> a solicitar y obtener del responsable, que suprima o elimine
> sus datos personales, de acuerdo a las causales previstas en
> la ley.
> t) Derecho de oposición: derecho del titular de datos
> a solicitar y obtener del responsable, que no se lleve a
> cabo un tratamiento de datos determinado, de conformidad a
> las causales previstas en la ley.
> u) Derecho a la portabilidad de los datos personales:
> derecho del titular de datos a solicitar y obtener del
> responsable, una copia de sus datos personales en un formato
> electrónico estructurado, genérico y de uso común, que
> permita ser operado por distintos sistemas, y poder
> comunicarlos o transferirlos a otro responsable de datos.
> El titular tendrá derecho a que sus datos personales
> se transmitan directamente de responsable a responsable
> cuando sea técnicamente posible.
> v) Cesión de datos personales: transferencia de datos
> personales por parte del responsable de datos a otro
> responsable de datos.
> w) Elaboración de perfiles: toda forma de tratamiento
> automatizado de datos personales que consista en utilizar
> esos datos para evaluar, analizar o predecir aspectos
> relativos al rendimiento profesional, situación económica,
> de salud, preferencias personales, intereses, fiabilidad,
> comportamiento, ubicación o movimientos de una persona
> natural.
> x) Tercero mandatario o encargado: la persona natural o
> jurídica que trate datos personales, por cuenta del
> responsable de datos.
> y) Agencia: la Agencia de Protección de Datos
> Personales.
> z) Registro Nacional de Sanciones y Cumplimiento: es un
> registro nacional de carácter público administrado por la
> Agencia, que consigna los modelos certificados de
> prevención, los responsables de datos que los hayan
> adoptado y las sanciones que se hayan impuesto a los
> responsables de datos que hayan infringido la ley.

### Cross-references
- Art. 1, Art. 1 bis (general and territorial scope).
- Art. 4 (rights of data subjects).
- Art. 8 bis (automated decisions and profiling).
- Art. 12, Art. 13 (lawful bases for processing).
- Art. 15 (cession of personal data).
- Art. 15 bis (processing through a mandatary or processor).
- Art. 16, Art. 16 bis (sensitive personal data, including health).
- Art. 30 et seq. (Agency).
- Law No. 18.575 (definition of public bodies, subparagraph j).

> **TN — renumbering audit:** The 1999 baseline subparagraphs d (dato caduco), e (dato estadístico), and h (eliminación o cancelación) were not addressed by Ley 21.719 Art. 1° item 5 and are preserved here verbatim from the 1999 baseline. They remain operative under the consolidated law. On the renumbering scheme: a literal reading of item 5.dos ("Elimínase el literal j), pasando el actual literal k) a ser literal j) y así sucesivamente") would renumber every subsequent subparagraph, meaning the surviving 1999 subparagraphs l, m, n, ñ, o would shift up by one. However, item 5.tres immediately re-substitutes subparagraphs k–o with new content using the new numbering, making this question moot for those positions. The remaining baseline subparagraphs (b, d, e, h) keep their original letters because they precede the eliminated j.

> **Source:** Ley 19.628 Art. 2° as amended by Ley 21.719 Art. 1° items 4, 5.uno, 5.dos, 5.tres, 5.cuatro, and 5.cinco (in force 2026-12-01).

---

## Article 3 — Principles
**Spanish anchor:** Art. 3°
**Tags:** principles, lawfulness, fairness, purpose-limitation, proportionality, data-minimization, retention, quality, accountability, security, transparency, confidentiality

### Plain-English text

The processing of personal data is governed by the following principles:

a) **Principles of lawfulness and fairness** (licitud y lealtad). Personal data may only be processed in a lawful and fair manner. The data controller (responsable) shall be able to demonstrate the lawfulness of the personal-data processing it carries out.

b) **Principle of purpose** (finalidad). Personal data must be collected for specific, explicit, and lawful purposes. The processing of personal data must be limited to the fulfilment of those purposes.

In application of this principle, personal data may not be processed for purposes other than those informed at the time of collection, unless: the processing is for purposes compatible with those originally authorised; there exists a contractual or pre-contractual relationship between the data subject and the controller that justifies processing for a different purpose, provided that it falls within the purposes of the contract or is consistent with negotiations or dealings prior to its conclusion; the data subject grants their consent again; or the law so provides.

c) **Principle of proportionality** (proporcionalidad). The personal data processed must be strictly limited to those that are necessary, adequate, and relevant in relation to the purposes of the processing.

Personal data may be retained only for the period of time necessary to fulfil the purposes of the processing, after which they must be erased or anonymized — without prejudice to the exceptions established by law. A longer retention period requires statutory authorisation or the data subject's consent.

d) **Principle of quality** (calidad). Personal data must be accurate, complete, current, and relevant in relation to their provenance and the purposes of the processing.

e) **Principle of accountability** (responsabilidad). Those who process personal data shall be legally accountable for compliance with the principles set out in this article and with the duties and obligations established by law.

f) **Principle of security** (seguridad). In processing personal data, the controller must ensure appropriate standards of security, protecting them against unauthorised or unlawful processing, and against their loss, leakage (filtración), accidental damage, or destruction. Security measures must be appropriate and consistent with the processing to be undertaken and the nature of the data.

g) **Principle of transparency and information** (transparencia e información). The controller must provide the data subject with all information necessary for the exercise of the rights established by this law, including the policies and practices on personal-data processing — which must also be permanently accessible and at the disposal of any interested party, in a precise, clear, unambiguous, and gratuitous manner.

The controller must adopt the appropriate and timely measures to facilitate the data subject's access to all information specified in this law, as well as any other communication relating to the processing it carries out.

h) **Principle of confidentiality** (confidencialidad). The data controller and those who have access to the data shall maintain secrecy or confidentiality (guardar secreto o confidencialidad) with respect to them. The controller shall establish appropriate controls and measures to preserve secrecy or confidentiality. This duty subsists even after the relationship with the data subject has ended.

> **TN:** The 1999 baseline Art. 3 (surveys and market research, including the opt-out for commercial use) was entirely replaced by Ley 21.719 Art. 1° item 6 with a principles framework analogous to GDPR Art. 5. The pre-21.719 substantive content of the survey/opt-out provision has no direct successor in this article; the right of opposition to commercial marketing is now reflected in Art. 8(b) (consolidated). The opt-out to personal data being used for advertising, market research, or opinion polls is now subsumed under the right of opposition (Art. 8) and the general lawfulness regime (Arts. 12, 13).

### Original Spanish

> Artículo 3°.- Principios. El tratamiento de los
> datos personales se rige por los siguientes principios:
> a) Principios de licitud y lealtad. Los datos
> personales sólo pueden tratarse de manera lícita y leal.
> El responsable deberá ser capaz de acreditar la
> licitud del tratamiento de datos personales que realiza.
> b) Principio de finalidad. Los datos personales deben
> ser recolectados con fines específicos, explícitos y
> lícitos. El tratamiento de los datos personales debe
> limitarse al cumplimiento de estos fines.
> En aplicación de este principio, no se pueden tratar
> los datos personales con fines distintos a los informados al
> momento de la recolección, salvo que el tratamiento sea
> para fines compatibles con los autorizados originalmente;
> que exista una relación contractual o precontractual entre
> el titular y el responsable que justifique el tratamiento de
> los datos con una finalidad distinta, siempre que se
> enmarque dentro de los fines del contrato o sea coherente
> con las tratativas o negociaciones previas a la celebración
> del mismo; que el titular otorgue nuevamente su
> consentimiento, y cuando lo disponga la ley.
> c) Principio de proporcionalidad. Los datos personales
> que se traten deben limitarse estrictamente a aquéllos que
> resulten necesarios, adecuados y pertinentes en relación
> con los fines del tratamiento.
> Los datos personales pueden ser conservados sólo por
> el período de tiempo que sea necesario para cumplir con los
> fines del tratamiento, luego de lo cual deben ser suprimidos
> o anonimizados, sin perjuicio de las excepciones que
> establezca la ley. Un período de tiempo mayor requiere
> autorización legal o consentimiento del titular.
> d) Principio de calidad. Los datos personales deben ser
> exactos, completos, actuales y pertinentes en relación con
> su proveniencia y los fines del tratamiento.
> e) Principio de responsabilidad. Quienes realicen
> tratamiento de los datos personales serán legalmente
> responsables del cumplimiento de los principios contenidos
> en este artículo y de las obligaciones y deberes de
> conformidad a la ley.
> f) Principio de seguridad. En el tratamiento de los
> datos personales, el responsable debe garantizar estándares
> adecuados de seguridad, protegiéndolos contra el
> tratamiento no autorizado o ilícito, y contra su pérdida,
> filtración, daño accidental o destrucción. Las medidas de
> seguridad deben ser apropiadas y acordes con el tratamiento
> que se vaya a efectuar y con la naturaleza de los datos.
> g) Principio de transparencia e información. El
> responsable debe entregar al titular toda la información
> que sea necesaria para el ejercicio de los derechos que
> establece esta ley, incluyendo las políticas y las
> prácticas sobre el tratamiento de los datos personales, las
> que además deberán encontrarse permanentemente accesibles
> y a disposición de cualquier interesado de manera precisa,
> clara, inequívoca y gratuita.
> El responsable debe adoptar las medidas adecuadas y
> oportunas para facilitar al titular el acceso a toda la
> información que señala esta ley, así como cualquier otra
> comunicación relativa al tratamiento que realiza.
> h) Principio de confidencialidad. El responsable de
> datos personales y quienes tengan acceso a ellos deberán
> guardar secreto o confidencialidad acerca de los mismos. El
> responsable establecerá controles y medidas adecuadas para
> preservar el secreto o confidencialidad. Este deber subsiste
> aún después de concluida la relación con el titular.

### Cross-references
- Art. 1, Art. 1 bis (scope).
- Art. 12, Art. 13 (lawful bases — operationalise the lawfulness principle).
- Art. 14 et seq. (controller obligations — operationalise accountability and security).
- Art. 14 ter (information duty — operationalises transparency).
- Art. 14 quinquies, Art. 14 sexies (security measures and breach notification).

> **Source:** Ley 19.628 Art. 3° as substituted by Ley 21.719 Art. 1° item 6 (in force 2026-12-01).

---

---

<!-- source: corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md -->
## FILE: corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md

# Ley 19.628 — Título I: Rights of the Data Subject (De los derechos del titular de datos personales — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** In force from 2026-12-01.

> **Title note:** Ley 21.719 Art. 1° item 7 replaced the entire Título I. The 1999 baseline Título I ("De la utilización de datos personales") and its substantive content (Arts. 4–11 on authorisation, automated transmission, mandatory erasure, confidentiality, mandate, purpose limitation, sensitive-data prohibition, and duty of care) are superseded by a unified rights-of-the-data-subject framework. The consolidated Título I now houses Arts. 4–11 covering rights of access, rectification, erasure, opposition, automated decisions, blocking, portability, and the procedural framework for exercising those rights.
>
> The previous Título I content (lawfulness of processing, controller obligations, mandate, sensitive-data rules, etc.) is now found in the consolidated Título II (Arts. 12 et seq.) as replaced by Ley 21.719 Art. 1° item 8. The filename `titulo-01-utilizacion.md` is preserved for git-history continuity even though the title is no longer "De la utilización".

---

## Article 4 — Rights of the data subject
**Spanish anchor:** Art. 4°
**Tags:** data-subject-rights, access, rectification, erasure, opposition, portability, blocking, non-waiver, heirs

### Plain-English text

Every person, acting on their own behalf or through their legal representative or mandatary (mandatario), as appropriate, has the right of access, rectification, erasure, opposition, portability, and blocking of their personal data (datos personales), in accordance with this law.

Such rights are personal, non-transferable, and irrevocable, and may not be limited by any act or agreement (acto o convención).

In the event of the data subject's death, the rights recognised by this law may be exercised by the data subject's heirs.

However, heirs may not access the decedent's data, nor request its rectification or erasure, where the deceased person had expressly prohibited it, or where the law so provides.

### Original Spanish

> Artículo 4º.- Derechos del titular de datos. Toda
> persona, actuando por sí o a través de su representante
> legal o mandatario, según corresponda, tiene derecho de
> acceso, rectificación, supresión, oposición, portabilidad
> y bloqueo de sus datos personales, de conformidad a la
> presente ley.
> Tales derechos son personales, intransferibles e
> irrenunciables y no pueden limitarse por ningún acto o
> convención.
> En caso de fallecimiento del titular de datos, los
> derechos que reconoce esta ley pueden ser ejercidos por sus
> herederos.
> Con todo, los herederos no podrán acceder a los datos
> del causante, ni solicitar su rectificación o supresión,
> cuando la persona fallecida lo hubiese prohibido
> expresamente o así lo establezca una ley.

### Cross-references
- Art. 5 (right of access — substantive content).
- Art. 6 (right of rectification).
- Art. 7 (right of erasure).
- Art. 8 (right of opposition).
- Art. 8 bis (automated decisions).
- Art. 8 ter (right of blocking).
- Art. 9 (right of portability).
- Art. 10 (form and means of exercising rights).
- Art. 11 (procedure before the controller).

> **Source:** Ley 19.628 Art. 4° as substituted by Ley 21.719 Art. 1° item 7 (in force 2026-12-01).

---

## Article 5 — Right of access
**Spanish anchor:** Art. 5°
**Tags:** access, information-duty, origin, purposes, recipients, retention-period, legitimate-interests, automated-decisions

### Plain-English text

The data subject has the right to request and obtain from the controller confirmation as to whether the personal data concerning them are being processed by the controller and, if so, to access those data and the following information:

a) The data processed and their origin.

b) The purpose or purposes of the processing.

c) The categories, classes, or types of recipients, or alternatively the identity of each recipient — at the data subject's request — to whom the data have been communicated or ceded, or to whom they are intended to be communicated or ceded.

d) The period of time during which the data will be processed.

e) The legitimate interests of the controller, where the processing is based on the provision of Article 13, subparagraph (d).

f) Meaningful information about the logic applied where the controller carries out processing in accordance with Article 8° bis.

The controller shall always be obliged to provide information and grant access to the requested data, except where a law expressly provides otherwise.

### Original Spanish

> Artículo 5º.- Derecho de acceso. El titular de datos
> tiene derecho a solicitar y obtener del responsable,
> confirmación acerca de si los datos personales que le
> conciernen están siendo tratados por él, y en tal caso,
> acceder a dichos datos y a la siguiente información:
> a) Los datos tratados y su origen.
> b) La finalidad o finalidades del tratamiento.
> c) Las categorías, clases o tipos de destinatarios, o
> bien, la identidad de cada destinatario, en caso de
> solicitarlo así el titular, a los que se les hayan
> comunicado o cedido los datos o se prevea hacerlo.
> d) El período de tiempo durante el cual los datos
> serán tratados.
> e) Los intereses legítimos del responsable, cuando el
> tratamiento se base en lo dispuesto en el artículo 13,
> letra d).
> f) La información significativa sobre la lógica
> aplicada en el caso de que el responsable realice
> tratamiento de datos de conformidad con el artículo 8°
> bis.
> El responsable siempre estará obligado a entregar
> información y a dar acceso a los datos solicitados excepto
> cuando una ley disponga expresamente lo contrario.

### Cross-references
- Art. 4 (rights of the data subject).
- Art. 8 bis (automated decisions, including profiling).
- Art. 13(d) (legitimate-interests lawful basis).
- Art. 11 (procedure for exercising the right).

> **Source:** Ley 19.628 Art. 5° as substituted by Ley 21.719 Art. 1° item 7 (in force 2026-12-01).

---

## Article 6 — Right of rectification
**Spanish anchor:** Art. 6°
**Tags:** rectification, accuracy, completeness, communication-of-changes

### Plain-English text

The data subject has the right to request and obtain from the controller the rectification of the personal data concerning them and being processed by the controller, where they are inaccurate, outdated, or incomplete.

The rectified data must be communicated to the persons, entities, or bodies to whom the controller has communicated or ceded the said data, except where such communication is impossible or requires a disproportionate effort.

Once the rectification has been carried out, the unrectified data may not be reprocessed.

### Original Spanish

> Artículo 6º.- Derecho de rectificación. El titular
> de datos tiene derecho a solicitar y obtener del
> responsable, la rectificación de los datos personales que
> le conciernen y que están siendo tratados por él, cuando
> sean inexactos, desactualizados o incompletos.
> Los datos rectificados deberán ser comunicados a las
> personas, entidades u organismos a los cuales el responsable
> haya comunicado o cedido los referidos datos, salvo en los
> casos en que dicha comunicación sea imposible o exija un
> esfuerzo desproporcionado.
> Efectuada la rectificación, no se podrán volver a
> tratar los datos sin rectificar.

### Cross-references
- Art. 4 (rights of the data subject).
- Art. 11 (procedure for exercising the right).

> **Source:** Ley 19.628 Art. 6° as substituted by Ley 21.719 Art. 1° item 7 (in force 2026-12-01).

---

## Article 7 — Right of erasure
**Spanish anchor:** Art. 7°
**Tags:** erasure, deletion, withdrawal-of-consent, unlawful-processing, expired-data, judicial-order, opposition, exceptions

### Plain-English text

The data subject has the right to request and obtain from the controller the deletion of the personal data concerning them, in the following cases:

a) Where the data are no longer necessary in relation to the purposes of the processing for which they were collected.

b) Where the data subject has withdrawn consent (revocado su consentimiento) for the processing and the processing has no other legal basis.

c) Where the data have been obtained or processed unlawfully by the controller.

d) Where the data are expired (datos caducos).

e) Where the data must be erased for compliance with a court judgment, a decision of the data-protection authority, or a legal obligation.

f) Where the data subject has exercised the right of opposition pursuant to the following article, and no other legal basis exists for the processing.

Erasure shall not proceed where the processing is necessary:

i. For the exercise of the freedoms of expression and information.

ii. For compliance with a legal obligation or for the performance of a contract entered into between the data subject and the controller.

iii. For the performance of a public function or for the exercise of an activity in the public interest.

iv. For reasons of public interest in the area of public health, in accordance with the conditions and guarantees established by law.

v. For processing for historical, statistical, or scientific purposes, and for studies or research that serve purposes of public interest.

vi. For the establishment, exercise, or defence of an administrative or judicial claim.

### Original Spanish

> Artículo 7°.- Derecho de supresión. El titular de
> datos tiene derecho a solicitar y obtener del responsable,
> la eliminación de los datos personales que le conciernen,
> en los siguientes casos:
> a) Cuando los datos no resulten necesarios en relación
> con los fines del tratamiento para el cual fueron recogidos.
> b) Cuando el titular haya revocado su consentimiento
> para el tratamiento y éste no tenga otro fundamento legal.
> c) Cuando los datos hayan sido obtenidos o tratados
> ilícitamente por el responsable.
> d) Cuando se trate de datos caducos.
> e) Cuando los datos deban suprimirse para el
> cumplimiento de una sentencia judicial, de una resolución
> de la autoridad de protección de datos o de una obligación
> legal.
> f) Cuando el titular haya ejercido su derecho de
> oposición de conformidad al artículo siguiente y no exista
> otro fundamento legal para su tratamiento.
> No procede la supresión cuando el tratamiento sea
> necesario:
> i. Para ejercer el derecho a las libertades de emitir
> opinión y de informar.
> ii. Para el cumplimiento de una obligación legal o la
> ejecución de un contrato suscrito entre el titular y el
> responsable.
> iii. Para el cumplimiento de una función pública o
> para el ejercicio de una actividad de interés público.
> iv. Por razones de interés público en el área de la
> salud pública, de conformidad con las condiciones y
> garantías establecidas en la ley.
> v. Para tratamientos con fines históricos,
> estadísticos o científicos y para estudios o
> investigaciones que atiendan fines de interés público.
> vi. Para la formulación, ejercicio o defensa de una
> reclamación administrativa o judicial.

### Cross-references
- Art. 4 (rights of the data subject).
- Art. 8 (right of opposition).
- Art. 8 ter (right of blocking — alternative to erasure).
- Art. 11 (procedure for exercising the right).
- Art. 16 quinquies (historical/statistical/scientific purposes).

> **Source:** Ley 19.628 Art. 7° as substituted by Ley 21.719 Art. 1° item 7 (in force 2026-12-01).

---

## Article 8 — Right of opposition
**Spanish anchor:** Art. 8°
**Tags:** opposition, legitimate-interests, direct-marketing, profiling, publicly-accessible-sources, scientific-research, statistical-purposes

### Plain-English text

The data subject has the right to object before the controller to a specific or determined processing of the personal data concerning them, in the following cases:

a) Where the lawful basis of the processing is the satisfaction of legitimate interests of the controller. In that case, the data subject may exercise the right of opposition at any time. The controller must cease processing the personal data unless it can demonstrate compelling legitimate grounds for the processing that override the interests, rights, and liberties of the data subject, or grounds for the establishment, exercise, or defence of claims.

b) Where the processing is carried out exclusively for direct marketing or marketing purposes (mercadotecnia o marketing directo) for goods, products, or services, including profiling, in accordance with Article 8° bis.

c) Where the processing is carried out on data obtained from a publicly accessible source and there is no other legal basis for the processing.

Opposition shall not proceed where the processing is carried out for scientific or historical research purposes or for statistical purposes, and the processing is necessary for the performance of a public function or for the exercise of an activity in the public interest.

### Original Spanish

> Artículo 8°.- Derecho de Oposición. El titular de
> datos tiene derecho a oponerse ante el responsable a que se
> realice un tratamiento específico o determinado de los
> datos personales que le conciernan, en los siguientes casos:
> a) Cuando la base de licitud del tratamiento sea la
> satisfacción de intereses legítimos del responsable. En
> dicho caso podrá ejercer su derecho de oposición en
> cualquier momento. El responsable del tratamiento deberá
> dejar de tratar los datos personales, salvo que acredite
> motivos legítimos imperiosos para el tratamiento que
> prevalezcan sobre los intereses, los derechos y las
> libertades del titular, o para la formulación, el ejercicio
> o la defensa de reclamaciones.
> b) Si el tratamiento se realiza exclusivamente con
> fines de mercadotecnia o marketing directo de bienes,
> productos o servicios, incluida la elaboración de perfiles,
> de conformidad con el artículo 8° bis.
> c) Si el tratamiento se realiza respecto de datos
> obtenidos de una fuente de acceso público y no existe otro
> fundamento legal para su tratamiento.
> No procederá la oposición al tratamiento cuando éste
> se realice con fines de investigación científica o
> histórica o fines estadísticos, y siempre que fueran
> necesarios para el cumplimiento de una función pública o
> para el ejercicio de una actividad de interés público.

### Cross-references
- Art. 4 (rights of the data subject).
- Art. 8 bis (automated decisions, including profiling).
- Art. 13(d) (legitimate-interests lawful basis).
- Art. 11 (procedure for exercising the right).

> **Source:** Ley 19.628 Art. 8° as substituted by Ley 21.719 Art. 1° item 7 (in force 2026-12-01).

---

## Article 8 bis — Automated individual decisions, including profiling
**Spanish anchor:** Art. 8° bis
**Tags:** automated-decisions, profiling, contract, consent, legal-authorisation, human-intervention, explanation, review

### Plain-English text

The data subject has the right to object and not to be subject to decisions based on the automated processing of their personal data, including profiling (elaboración de perfiles), that produces legal effects on them or significantly affects them.

The preceding paragraph shall not apply in the following cases:

a) Where the decision is necessary for the conclusion or performance of a contract between the data subject and the controller.

b) Where there exists prior and express consent of the data subject in the manner prescribed in Article 12.

c) Where the law so provides, insofar as it establishes safeguards for the rights and liberties of the data subject.

In all cases of decisions based on the automated processing of personal data — including those mentioned in subparagraphs (a), (b), and (c) above — the controller must adopt the necessary measures to ensure the rights and liberties of the data subject, the right to information and transparency, the right to obtain an explanation, to human intervention, to express the data subject's point of view, and to request review of the decision.

### Original Spanish

> Artículo 8° bis.- Decisiones individuales
> automatizadas, incluida la elaboración de perfiles. El
> titular de datos tiene derecho a oponerse y a no ser objeto
> de decisiones basadas en el tratamiento automatizado de sus
> datos personales, incluida la elaboración de perfiles, que
> produzca efectos jurídicos en él o le afecte
> significativamente.
> El inciso anterior no se aplicará en los siguientes
> casos:
> a) Cuando la decisión sea necesaria para la
> celebración o ejecución de un contrato entre el titular y
> el responsable.
> b) Cuando exista consentimiento previo y expreso del
> titular en la forma prescrita en el artículo 12.
> c) Cuando lo señale la ley, en la medida en que ésta
> disponga el empleo de salvaguardas a los derechos y
> libertades del titular.
> En todos los casos de decisiones basadas en el
> tratamiento automatizado de datos personales, inclusive
> aquéllos señalados en las letras a), b) y c) precedentes,
> el responsable deberá adoptar las medidas necesarias para
> asegurar los derechos y libertades del titular, su derecho a
> la información y transparencia, el derecho a obtener una
> explicación, a la intervención humana, a expresar su punto
> de vista y a solicitar la revisión de la decisión.

### Cross-references
- Art. 4 (rights of the data subject).
- Art. 5(f) (information about the logic of automated processing).
- Art. 8 (right of opposition).
- Art. 12 (consent).

> **Source:** Ley 19.628 Art. 8° bis as inserted by Ley 21.719 Art. 1° item 7 (in force 2026-12-01).

---

## Article 8 ter — Right of blocking of processing
**Spanish anchor:** Art. 8° ter
**Tags:** blocking, temporary-suspension, rectification, erasure, opposition

### Plain-English text

The data subject has the right to request the temporary suspension of any operation of processing of their personal data when they submit a request for rectification, erasure, or opposition pursuant to Article 11 of this law, while that request is pending resolution.

The data subject may also exercise this right as an alternative to erasure in the cases set out in Article 7°.

The exercise of this right shall not affect the storage of the data by the controller.

### Original Spanish

> Artículo 8° ter.- Derecho de bloqueo del tratamiento.
> El titular de datos tiene derecho a solicitar la suspensión
> temporal de cualquier operación de tratamiento de sus datos
> personales cuando formule una solicitud de rectificación,
> supresión u oposición, de conformidad con el artículo 11
> de la presente ley, mientras dicha solicitud no se resuelva.
> Asimismo, el titular podrá ejercer este derecho
> alternativamente al de supresión en los casos del artículo
> 7°.
> El ejercicio de este derecho no afectará el
> almacenamiento de los datos por parte del responsable.

### Cross-references
- Art. 4 (rights of the data subject).
- Art. 7 (right of erasure).
- Art. 11 (procedure for exercising rights).

> **Source:** Ley 19.628 Art. 8° ter as inserted by Ley 21.719 Art. 1° item 7 (in force 2026-12-01).

---

## Article 9 — Right of portability of personal data
**Spanish anchor:** Art. 9°
**Tags:** portability, structured-format, electronic, consent, automated-processing, direct-transmission

### Plain-English text

The data subject has the right to request and receive a copy of the personal data concerning them that the data subject has provided to the controller, in a structured, generic, and commonly used electronic format that can be operated by different systems, and to communicate or transfer them to another data controller, where the following circumstances concur:

a) The processing is carried out by automated means, and

b) The processing is based on the consent of the data subject.

The controller must use the most expedient and least burdensome means without raising obstacles to the exercise of this right.

The controller must also communicate to the data subject — clearly and precisely — the necessary measures to obtain the personal data and specify the technical characteristics for carrying out these operations.

The data subject shall have the right to have their personal data transmitted directly from controller to controller where technically feasible.

In any event, the exercise of the right of portability shall not entail the erasure of the data before the transferring controller (responsable cedente), unless the data subject so requests jointly in the request.

### Original Spanish

> Artículo 9º.- Derecho a la portabilidad de los datos
> personales. El titular de datos tiene derecho a solicitar y
> recibir una copia de los datos personales que le conciernen,
> que haya facilitado al responsable, en un formato
> electrónico estructurado, genérico y de uso común, que
> permita ser operado por distintos sistemas, y a comunicarlos
> o transferirlos a otro responsable de datos, cuando
> concurran las siguientes circunstancias:
> a) El tratamiento se realice en forma automatizada, y
> b) El tratamiento esté basado en el consentimiento del
> titular.
> El responsable debe utilizar los medios más expeditos,
> menos onerosos y sin poner trabas u obstáculos para el
> ejercicio de este derecho.
> El responsable también debe comunicar al titular de
> manera clara y precisa las medidas necesarias para obtener
> sus datos personales y especificar las características
> técnicas para llevar a cabo estas operaciones.
> El titular tendrá derecho a que sus datos personales
> se transmitan directamente de responsable a responsable
> cuando sea técnicamente posible.
> Con todo, el ejercicio del derecho de portabilidad no
> supondrá la supresión de los datos ante el responsable
> cedente, a menos que el titular de ellos así lo pida
> conjuntamente en la solicitud.

### Cross-references
- Art. 4 (rights of the data subject).
- Art. 12 (consent).
- Art. 11 (procedure for exercising rights).

> **Source:** Ley 19.628 Art. 9° as substituted by Ley 21.719 Art. 1° item 7 (in force 2026-12-01).

---

## Article 10 — Form and means of exercising the rights of the data subject
**Spanish anchor:** Art. 10
**Tags:** procedure, multiple-controllers, foreign-controller, designated-contact, free-of-charge, costs, mechanisms

### Plain-English text

The rights recognised by this law are exercised by the data subject before the data controller (responsable de datos). If the data subject's personal data are processed by multiple controllers, the data subject may exercise their rights before any of them.

In the case of legal persons not constituted in Chile, the controller must designate in writing, before the Agency (Agencia), an email address or equivalent operative and valid electronic-communication medium for a natural or legal person capable of acting on its behalf, for the purpose of enabling the data subject to exercise their rights and to communicate with the controller, and where the administrative communications and notifications provided for by law may be validly served. The controller must keep this information up to date.

Data controllers must implement mechanisms and technological tools that enable the data subject to exercise their rights expeditiously, agilely, and effectively. The means provided by the controller must be simple in their operation.

The exercise of the rights of rectification, erasure, and opposition shall always be free of charge (gratuitos) for the data subject. The right of access shall also be exercised free of charge, at least quarterly.

The data controller may only require payment of the direct costs incurred when the data subject exercises the right of access and the right to portability more than once in a quarter. The controller may not require this payment in the cases referred to in the fourth paragraph of Article 28.

The parameters and mechanisms for determining the costs arising from the exercise of the rights referred to in the preceding paragraph shall be determined by the Agency through a general instruction (instrucción general), taking into account, among other factors, the volume of data to be delivered, the legal nature and size of the entity or enterprise that is the controller.

The Agency shall ensure the effective exercise of and compliance with the rights that this law grants to the data subject, in accordance with the provisions of this law.

### Original Spanish

> Artículo 10.- Forma y medios de ejercer los derechos
> del titular de datos. Los derechos reconocidos en esta ley
> se ejercen por el titular ante el responsable de datos. Si
> los datos personales del titular son tratados por diversos
> responsables, el titular puede ejercer sus derechos ante
> cualquiera de ellos.
> En el caso de las personas jurídicas no constituidas
> en Chile, el responsable deberá señalar por escrito, ante
> la Agencia, un correo electrónico o un medio de
> comunicación electrónico equivalente válido y operativo
> de una persona natural o jurídica capaz de actuar en su
> nombre, para los efectos de que el titular pueda ejercer sus
> derechos y comunicarse con el responsable, y donde se le
> practiquen válidamente las comunicaciones y notificaciones
> administrativas que disponga la ley. El responsable deberá
> mantener actualizada esta información.
> Los responsables de datos deberán implementar
> mecanismos y herramientas tecnológicas que permitan que el
> titular ejerza sus derechos en forma expedita, ágil y
> eficaz. Los medios dispuestos por el responsable deben ser
> sencillos en su operación.
> El ejercicio de los derechos de rectificación,
> supresión y oposición siempre serán gratuitos para el
> titular. El derecho de acceso también se ejercerá en forma
> gratuita, al menos trimestralmente.
> El responsable de datos sólo puede exigir el pago de
> los costos directos en que incurra, cuando el titular ejerza
> su derecho de acceso y derecho a la portabilidad más de una
> vez en el trimestre. El responsable no podrá exigir este
> pago en los casos del inciso cuarto del artículo 28.
> Los parámetros y mecanismos para determinar los costos
> derivados del ejercicio de los derechos señalados en el
> inciso anterior serán determinados por la Agencia, a
> través de una instrucción general que considerará, entre
> otros antecedentes, el volumen de los datos a ser
> entregados, la naturaleza jurídica y el tamaño de la
> entidad o empresa que tenga la calidad de responsable.
> La Agencia velará por el efectivo ejercicio y
> cumplimiento de los derechos que esta ley reconoce al
> titular de datos, en conformidad a lo dispuesto en esta ley.

### Cross-references
- Art. 4–9 (substantive rights).
- Art. 11 (procedure before the controller).
- Art. 28 (international transfer — referenced for fee waiver context).
- Art. 30 et seq. (Agency).

> **Source:** Ley 19.628 Art. 10 as substituted by Ley 21.719 Art. 1° item 7 (in force 2026-12-01).

---

## Article 11 — Procedure before the data controller
**Spanish anchor:** Art. 11
**Tags:** procedure, individualisation, deadlines, response, denial, claim-before-agency, temporary-blocking, downstream-notification

### Plain-English text

To exercise the rights granted by this law, the data subject must submit a written application or requirement (solicitud o requerimiento escrito) before the controller, addressed to the email address established for this purpose, a contact form, or an equivalent electronic medium. The application must contain at least the following items:

a) Individualisation of the data subject and of their legal representative or mandatary, as appropriate, and authentication of their identity in accordance with the procedures, forms, and modalities established by the Agency.

b) Indication of a domicile or an email address or equivalent medium for communicating the response.

c) Identification of the personal data or of the specific processing in respect of which the corresponding right is exercised.

d) For requests of rectification, the data subject must indicate the precise modifications or updates to be made and attach, where applicable, the supporting evidence. Where the request is for erasure, the data subject must indicate the ground invoked and attach the supporting evidence, where appropriate. For opposition requests, the data subject must indicate the ground invoked, and in the case of subparagraph (a) of Article 8°, must briefly substantiate the petition and may, likewise, attach evidence considered appropriate. In the case of the right of access, the individualisation of the data subject is sufficient.

Upon receiving the application, the controller must acknowledge receipt and rule on it no later than within thirty calendar days following the date of entry of the application. This period may be extended, once only, for up to thirty calendar days.

The controller must respond in writing to the data subject at the domicile or email address designated by the latter. The controller must store records demonstrating the delivery of the response to the physical or electronic address, its date, and its full content.

In the event of total or partial denial of the application, the controller must give reasons for its decision indicating the ground invoked and the supporting evidence. At the same time, the controller must inform the data subject of the thirty-business-day period to bring a claim before the Agency in accordance with the procedure established in Article 41.

If the period referred to in the second preceding paragraph expires without a response from the controller, the data subject may directly bring a claim before the Agency, on the same terms as in the preceding paragraph.

When a request for rectification, erasure, or opposition is submitted, the data subject shall have the right to request and obtain from the controller the temporary blocking of the data or of the processing being carried out, as appropriate. The temporary-blocking request must be substantiated, and the controller must respond to the requirement within the two business days following its receipt. While this request remains pending, the controller may not process the data subject's data that form part of the requirement. Temporary blocking of the data does not affect their storage by the controller. In the event of refusal, the controller must give reasons for its response and electronically communicate its decision to the Agency. The data subject may appeal this decision before the Agency, applying the provision of subparagraph (a) of the second paragraph of Article 41.

The rectification, erasure, or opposition to processing shall apply only with respect to the controllers to which the application has been made. Nonetheless, where the controller has communicated such data to other persons, it must communicate to them the changes made by virtue of the rectification, erasure, or opposition.

The data subject may provide any other information that facilitates the location of the personal data.

### Original Spanish

> Artículo 11.- Procedimiento ante el responsable de
> datos. Para ejercer los derechos que le reconoce esta ley,
> el titular deberá presentar una solicitud o requerimiento
> escrito ante el responsable, dirigido a la dirección de
> correo electrónico establecida para este fin, un formulario
> de contacto o un medio electrónico equivalente. La
> solicitud deberá contener, a lo menos, las siguientes
> menciones:
> a) Individualización del titular y de su representante
> legal o mandatario, según corresponda, y autenticación de
> su identidad de acuerdo con los procedimientos, formas y
> modalidades que establezca la Agencia.
> b) Indicación de un domicilio o una dirección de
> correo electrónico o de otro medio equivalente para
> comunicar la respuesta.
> c) Identificación de los datos personales o del
> tratamiento determinado, respecto de los cuales se ejerce el
> derecho correspondiente.
> d) En las solicitudes de rectificación, el titular
> deberá indicar las modificaciones o actualizaciones
> precisas a realizar y acompañar, en su caso, los
> antecedentes que las sustenten. Cuando se trate de
> solicitudes de supresión, el titular deberá indicar la
> causal invocada y acompañar los antecedentes que la
> sustenten, si correspondiere. Para las solicitudes de
> oposición, el titular deberá indicar la causal invocada y
> en el caso de la letra a) del artículo 8°, deberá
> fundamentar brevemente su petición y podrá, igualmente,
> acompañar los antecedentes que estime procedentes. En el
> caso del derecho de acceso, bastará con la
> individualización del titular.
> Recibida la solicitud el responsable deberá acusar
> recibo de ella y pronunciarse a más tardar dentro de los
> treinta días corridos siguientes a la fecha de ingreso de
> la solicitud. Este plazo podrá ser prorrogado, por una sola
> vez, hasta por treinta días corridos.
> El responsable deberá responder por escrito al titular
> a su domicilio o la dirección de correo electrónico fijada
> por éste. El responsable debe almacenar los respaldos que
> le permitan demostrar la remisión de la respuesta a la
> dirección física o electrónica que corresponda, su fecha
> y el contenido íntegro de ella.
> En caso de denegación total o parcial de la solicitud,
> el responsable deberá fundar su decisión indicando la
> causa invocada y los antecedentes que la justifican. En esta
> misma oportunidad el responsable debe señalar al titular
> que dispone de un plazo de treinta días hábiles para
> formular una reclamación ante la Agencia, de acuerdo con el
> procedimiento establecido en el artículo 41.
> Transcurrido el plazo al que hace referencia el inciso
> segundo anterior, sin que haya respuesta del responsable, el
> titular podrá formular directamente una reclamación ante
> la Agencia, en los mismos términos del inciso anterior.
> Cuando se formule una solicitud de rectificación,
> supresión u oposición, el titular tendrá derecho a
> solicitar y obtener del responsable el bloqueo temporal de
> sus datos o del tratamiento que realice, según corresponda.
> La solicitud de bloqueo temporal deberá ser fundada y el
> responsable deberá responder al requerimiento dentro de los
> dos días hábiles siguientes a su recepción. En tanto no
> resuelva esta solicitud, el responsable no podrá tratar los
> datos del titular que forman parte del requerimiento. El
> bloqueo temporal de los datos no afectará su almacenamiento
> por parte del responsable. En caso de rechazo el responsable
> deberá fundar su respuesta y comunicar en forma
> electrónica su decisión a la Agencia. El titular podrá
> reclamar de esta decisión ante la Agencia, aplicándose lo
> dispuesto en la letra a) del inciso segundo del artículo
> 41.
> La rectificación, supresión u oposición al
> tratamiento de los datos se aplicará sólo respecto de los
> responsables a quienes se les haya formulado la solicitud.
> Con todo, cuando el responsable haya comunicado dichos datos
> a otras personas, deberá comunicar a éstas los cambios
> realizados en virtud de la rectificación, supresión u
> oposición.
> El titular podrá aportar cualquier otro antecedente
> que facilite la localización de los datos personales.

### Cross-references
- Art. 4–9 (substantive rights).
- Art. 10 (form and means of exercising rights).
- Art. 41 (procedure before the Agency).

> **Source:** Ley 19.628 Art. 11 as substituted by Ley 21.719 Art. 1° item 7 (in force 2026-12-01).

---

---

<!-- source: corpus/19628-data-protection-consolidated/titulo-02-derechos.md -->
## FILE: corpus/19628-data-protection-consolidated/titulo-02-derechos.md

# Ley 19.628 — Título II: Processing of Personal Data and Special Categories of Data (Del tratamiento de los datos personales y de las categorías especiales de datos — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** In force from 2026-12-01.

> **Title note:** Ley 21.719 Art. 1° item 8 replaced the entire Título II. The 1999 baseline Título II ("De los derechos de los titulares de datos") and its substantive content (Arts. 12–16 on access, modification, erasure, blocking, non-waiver, multiple-controller access, exceptions, and habeas-data remedy) are superseded. The data-subject-rights regime now lives in the consolidated Título I (Arts. 4–11). The consolidated Título II reorganises into three paragraphs (Párrafos):
>
> - **Párrafo Primero:** Consent, controller obligations, and general processing (Arts. 12, 13, 14, 14 bis, 14 ter, 14 quáter, 14 quinquies, 14 sexies, 14 septies, 15, 15 bis, 15 ter).
> - **Párrafo Segundo:** Sensitive personal data (Arts. 16, 16 bis, 16 ter).
> - **Párrafo Tercero:** Special categories of personal data (Arts. 16 quáter, 16 quinquies, 16 sexies).
>
> The filename `titulo-02-derechos.md` is preserved for git-history continuity even though the title content is now about processing, not derechos.

---

## Párrafo Primero — Consent of the data subject, obligations and duties of the controller, and processing of data in general

---

## Article 12 — General rule for the processing of data; consent
**Spanish anchor:** Art. 12
**Tags:** consent, lawful-processing, revocation, free-informed-specific, contract-conditionality, burden-of-proof

### Plain-English text

The processing of personal data concerning the data subject is lawful when the data subject grants consent (consentimiento) for it.

The consent of the data subject must be free, informed, and specific as to its purpose or purposes. Consent must also be expressed in advance and in an unequivocal manner, through a verbal, written, or equivalent electronic-medium statement, or through an affirmative act that clearly evidences the data subject's will.

Where the consent is given by a mandatary (mandatario), the mandatary must be expressly empowered with this faculty.

The data subject may revoke the consent granted at any time and without giving reasons, using means similar or equivalent to those employed for granting it. The revocation of consent shall not have retroactive effect.

The means used for granting or revoking consent must be expeditious, reliable, free of charge, and permanently available to the data subject.

It is presumed that consent for processing data has not been freely granted where the controller obtains it in the context of the performance of a contract or the provision of a service in which it is not necessary to carry out such collection.

However, the provision of the preceding paragraph shall not apply where the party offering goods, services, or benefits requires, as the sole consideration (única contraprestación), consent to process data.

It is for the controller to prove that it had the consent of the data subject and that the processing of data was carried out in a lawful, fair, and transparent manner.

### Original Spanish

> Artículo 12.- Regla general del tratamiento de datos.
> Es lícito el tratamiento de los datos personales que le
> conciernen al titular, cuando otorgue su consentimiento para
> ello.
> El consentimiento del titular debe ser libre, informado
> y específico en cuanto a su finalidad o finalidades. El
> consentimiento debe manifestarse, además, en forma previa y
> de manera inequívoca, mediante una declaración verbal,
> escrita o expresada a través de un medio electrónico
> equivalente, o mediante un acto afirmativo que dé cuenta
> con claridad de la voluntad del titular.
> Cuando el consentimiento lo otorgue un mandatario,
> éste deberá encontrarse expresamente premunido de esta
> facultad.
> El titular puede revocar el consentimiento otorgado en
> cualquier momento y sin expresión de causa, utilizando
> medios similares o equivalentes a los empleados para su
> otorgamiento. La revocación del consentimiento no tendrá
> efectos retroactivos.
> Los medios utilizados para el otorgamiento o la
> revocación del consentimiento deben ser expeditos,
> fidedignos, gratuitos y estar permanentemente disponibles
> para el titular.
> Se presume que el consentimiento para tratar datos no
> ha sido libremente otorgado cuando el responsable lo recaba
> en el marco de la ejecución de un contrato o la prestación
> de un servicio en que no es necesario efectuar esa
> recolección.
> Con todo, lo dispuesto en el inciso anterior no se
> aplicará cuando quien ofrezca bienes, servicios o
> beneficios, requiera como única contraprestación el
> consentimiento para tratar datos.
> Corresponde al responsable probar que contó con el
> consentimiento del titular y que el tratamiento de datos fue
> realizado en forma lícita, leal y transparente.

### Cross-references
- Art. 2(p) (definition of consent).
- Art. 8 bis (consent for automated decisions).
- Art. 13 (other lawful bases).

> **Source:** Ley 19.628 Art. 12 as substituted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 13 — Other sources of lawfulness for processing
**Spanish anchor:** Art. 13
**Tags:** lawful-bases, financial-data, legal-obligation, contract, legitimate-interests, judicial-claims

### Plain-English text

Processing of personal data is lawful, without the consent of the data subject, in the following cases:

a) Where the processing concerns data relating to economic, financial, banking, or commercial obligations and is carried out in accordance with the rules of Title III of this law, including data relating to the data subject's socio-economic situation.

b) Where the processing is necessary for the performance or fulfilment of a legal obligation, or the law so provides.

c) Where the processing of data is necessary for the conclusion or performance of a contract between the data subject and the controller, or for the carrying out of pre-contractual measures taken at the data subject's request.

d) Where the processing is necessary for the satisfaction of the legitimate interests of the controller or of a third party, provided that the rights and liberties of the data subject are not thereby affected. In any case, the data subject may always require to be informed of the processing affecting them and of the legitimate interest on the basis of which the processing is carried out.

e) Where the processing of data is necessary for the establishment, exercise, or defence of a right before the courts of justice or public bodies.

The controller shall be required to demonstrate the lawfulness of the processing of data.

### Original Spanish

> Artículo 13.- Otras fuentes de licitud del tratamiento
> de datos. Es lícito el tratamiento de datos personales, sin
> el consentimiento del titular, en los siguientes casos:
> a) Cuando el tratamiento esté referido a datos
> relativos a obligaciones de carácter económico,
> financiero, bancario o comercial y se realice de conformidad
> con las normas del Título III de esta ley, incluidos los
> datos referidos a la situación socioeconómica del titular.
> b) Cuando el tratamiento sea necesario para la
> ejecución o el cumplimiento de una obligación legal o lo
> disponga la ley.
> c) Cuando el tratamiento de datos sea necesario para la
> celebración o ejecución de un contrato entre el titular y
> el responsable, o para la ejecución de medidas
> precontractuales adoptadas a solicitud del titular.
> d) Cuando el tratamiento sea necesario para la
> satisfacción de intereses legítimos del responsable o de
> un tercero, siempre que con ello no se afecten los derechos
> y libertades del titular. En todo caso, el titular podrá
> exigir siempre ser informado sobre el tratamiento que lo
> afecta y el interés legítimo en base al cual se efectúa
> dicho tratamiento.
> e) Cuando el tratamiento de datos sea necesario para la
> formulación, ejercicio o defensa de un derecho ante los
> tribunales de justicia u órganos públicos.
> El responsable deberá acreditar la licitud del
> tratamiento de datos.

### Cross-references
- Art. 12 (consent).
- Art. 8 (right of opposition — interaction with legitimate-interests basis).
- Title III (financial obligation data).

> **Source:** Ley 19.628 Art. 13 as substituted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 14 — Obligations of the data controller
**Spanish anchor:** Art. 14
**Tags:** controller-obligations, information, lawful-collection, accuracy, anonymisation, foreign-controller, contact

### Plain-English text

Without prejudice to the other provisions of this law, the data controller has the following obligations:

a) To inform and make available to the data subject the supporting information demonstrating the lawfulness of the processing of data it carries out. Likewise, it must provide such information expeditiously when requested.

b) To ensure that the personal data is collected from lawful sources of access (fuentes de acceso lícitas) for specific, explicit, and lawful purposes, and that its processing is limited to the fulfilment of those purposes.

c) To communicate or cede, in accordance with this law, accurate, complete, and current information.

d) To erase or anonymize the data subject's personal data when obtained for the performance of pre-contractual measures.

e) To comply with the other duties, principles, and obligations governing the processing of personal data established in this law.

A data controller without domicile in Chile that processes the data of persons residing in the national territory must designate and keep updated and operative an email address or other suitable contact method for receiving communications from the data subjects and from the Agency.

### Original Spanish

> Artículo 14.- Obligaciones del responsable de datos.
> El responsable de datos, sin perjuicio de las demás
> disposiciones previstas en esta ley, tiene las siguientes
> obligaciones:
> a) Informar y poner a disposición del titular los
> antecedentes que acrediten la licitud del tratamiento de
> datos que realiza. Asimismo, deberá entregar de manera
> expedita dicha información cuando le sea requerida.
> b) Asegurar que los datos personales se recojan de
> fuentes de acceso lícitas con fines específicos,
> explícitos y lícitos, y que su tratamiento se limite al
> cumplimiento de estos fines.
> c) Comunicar o ceder, en conformidad a las
> disposiciones de esta ley, información exacta, completa y
> actual.
> d) Suprimir o anonimizar los datos personales del
> titular cuando fueron obtenidos para la ejecución de
> medidas precontractuales.
> e) Cumplir con los demás deberes, principios y
> obligaciones que rigen el tratamiento de los datos
> personales previstos en esta ley.
> El responsable de datos que no tenga domicilio en Chile
> y que realice tratamiento de datos de personas que residan
> en el territorio nacional, deberá señalar y mantener
> actualizado y operativo, un correo electrónico u otro medio
> de contacto idóneo para recibir comunicaciones de los
> titulares de datos y de la Agencia.

### Cross-references
- Art. 3 (principles).
- Art. 12, Art. 13 (lawful bases).
- Art. 14 bis–14 septies (specific duties).

> **Source:** Ley 19.628 Art. 14 as substituted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 14 bis — Duty of secrecy or confidentiality
**Spanish anchor:** Art. 14 bis
**Tags:** secrecy, confidentiality, publicly-accessible-sources, post-termination, dependents

### Plain-English text

The data controller is obliged to maintain secrecy or confidentiality with respect to the personal data concerning a data subject, except where the data subject has manifestly made them public. This duty subsists even after the end of the relationship with the data subject. In the event that the controller has carried out any action on personal data obtained from publicly accessible sources — such as organising or classifying them under some criterion, or combining or supplementing them with other data — the personal data resulting from such action shall be protected under this duty of secrecy or confidentiality.

The duty of secrecy or confidentiality does not preclude the communications or cessions of data that the controller must carry out in accordance with the law, or the fulfilment of the obligation to grant the data subject access and to disclose the origin of the data, where this information is required by the data subject or by a public body within the scope of its legal competences.

The controller must adopt the necessary measures so that its dependents or the natural or legal persons that carry out processing operations on data under its responsibility comply with the duty of secrecy or confidentiality established in this article.

The persons, institutions, and their dependents referred to in Article 24 shall be subject to the obligation of confidentiality as regards the requirement and the fact of having transmitted that information.

### Original Spanish

> Artículo 14 bis.- Deber de secreto o confidencialidad.
> El responsable de datos está obligado a mantener secreto o
> confidencialidad acerca de los datos personales que
> conciernan a un titular, salvo cuando el titular los hubiere
> hecho manifiestamente públicos. Este deber subsiste aún
> después de concluida la relación con el titular. En caso
> de que el responsable haya realizado alguna acción sobre
> datos personales obtenidos de fuentes de acceso público,
> tales como organizarlos o clasificarlos bajo algún
> criterio, o combinarlos o complementarlos con otros datos,
> los datos personales que resulten de dicha acción se
> encontrarán protegidos bajo el presente deber de secreto o
> confidencialidad.
> El deber de secreto o confidencialidad no obsta a las
> comunicaciones o cesiones de datos que deba realizar el
> responsable en conformidad a la ley, y al cumplimiento de la
> obligación de dar acceso al titular e informar el origen de
> los datos, cuando esta información le sea requerida por el
> titular o por un órgano público dentro del ámbito de sus
> competencias legales.
> El responsable debe adoptar las medidas necesarias con
> el objeto que sus dependientes o las personas naturales o
> jurídicas que ejecuten operaciones de tratamiento de datos
> bajo su responsabilidad, cumplan el deber de secreto o
> confidencialidad establecidos en este artículo.
> Quedan sujetas a la obligación de confidencialidad las
> personas e instituciones y sus dependientes a que se refiere
> el artículo 24, en cuanto al requerimiento y al hecho de
> haber remitido dicha información.

### Cross-references
- Art. 3(h) (principle of confidentiality).
- Art. 24 (special regimes — criminal/security data confidentiality).

> **Source:** Ley 19.628 Art. 14 bis as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 14 ter — Duty of information and transparency
**Spanish anchor:** Art. 14 ter
**Tags:** information-duty, transparency, privacy-policy, website-disclosure, profile, automated-decisions, retention, sources

### Plain-English text

The data controller must facilitate and keep permanently available to the public, on its website or any other equivalent means of information, at least the following information:

a) The data-processing policy it has adopted, including its date and version.

b) The individualisation of the data controller, its legal representative, and the identification of the prevention officer (encargado de prevención), if any.

c) The postal address, email address, contact form, or identification of the equivalent technological medium of common use and easy access through which the requests made by data subjects are notified to it.

d) The categories, classes, or types of data it processes; the generic description of the universe of persons covered by its databases; the recipients to whom it foresees communicating or ceding the data; the purposes of the processing it carries out; the basis of legitimacy of the processing; and, in case of processing based on the satisfaction of legitimate interests, what such interests are.

e) The policy and security measures adopted to protect the personal databases it administers.

f) The right of the data subject to request before the controller access, rectification, erasure, opposition, and portability of their personal data, in accordance with the law.

g) The right of the data subject to appeal before the Agency, in case the controller rejects or does not respond timely to the requests submitted.

h) Where applicable, the transfer of personal data to a third country or international organisation, and whether they offer an adequate level of protection. Where they do not have an adequate level of protection, the controller must inform whether there are guarantees that justify such transfer.

i) The period during which the personal data will be retained.

j) The source from which the personal data originate and, where applicable, whether they come from publicly accessible sources.

k) Where the processing is based on the data subject's consent, the existence of the right to withdraw it at any time, without affecting the lawfulness of the processing based on the consent prior to its withdrawal.

l) The existence of automated decisions, including profiling. In such cases, meaningful information about the logic applied, as well as the foreseen consequences of such processing for the data subject.

### Original Spanish

> Artículo 14 ter.- Deber de información y
> transparencia. El responsable de datos debe facilitar y
> mantener permanentemente a disposición del público, en su
> sitio web o en cualquier otro medio de información
> equivalente, al menos, la siguiente información:
> a) La política de tratamiento de datos personales que
> haya adoptado, la fecha y versión de la misma.
> b) La individualización del responsable de datos y su
> representante legal y la identificación del encargado de
> prevención, si existiere.
> c) El domicilio postal, la dirección de correo
> electrónico, el formulario de contacto o la identificación
> del medio tecnológico equivalente de uso común y fácil
> acceso mediante el cual se le notifican las solicitudes que
> realicen los titulares.
> d) Las categorías, clases o tipos de datos que trata;
> la descripción genérica del universo de personas que
> comprenden sus bases de datos; los destinatarios a los que
> se prevé comunicar o ceder los datos; las finalidades de
> los tratamientos que realiza; la base de legitimidad del
> tratamiento; y en caso de tratamientos que se basan en la
> satisfacción de intereses legítimos, cuáles serían
> éstos.
> e) La política y las medidas de seguridad adoptadas
> para proteger las bases de datos personales que administra.
> f) El derecho que le asiste al titular para solicitar
> ante el responsable, acceso, rectificación, supresión,
> oposición y portabilidad de sus datos personales, de
> conformidad a la ley.
> g) El derecho que le asiste al titular de recurrir ante
> la Agencia, en caso de que el responsable rechace o no
> responda oportunamente las solicitudes que le formule.
> h) En su caso, la transferencia de datos personales a
> un tercer país u organización internacional y si éstos
> ofrecen o no un nivel adecuado de protección. En caso de
> que no cuenten con un nivel adecuado de protección, se
> deberá informar si existen garantías que justifiquen tal
> transferencia.
> i) El periodo durante el que se conservarán los datos
> personales.
> j) La fuente de la cual provienen los datos personales
> y, en su caso, si proceden de fuentes de acceso público.
> k) Cuando el tratamiento está basado en el
> consentimiento del titular, la existencia del derecho a
> retirarlo en cualquier momento, sin que ello afecte a la
> licitud del tratamiento basado en el consentimiento previo a
> su retirada.
> l) La existencia de decisiones automatizadas, incluida
> la elaboración de perfiles. En tales casos, información
> significativa sobre la lógica aplicada, así como las
> consecuencias previstas de dicho tratamiento para el
> titular.

### Cross-references
- Art. 3(g) (principle of transparency).
- Art. 5 (right of access).
- Art. 8 bis (automated decisions).
- Art. 27 et seq. (international transfers).

> **Source:** Ley 19.628 Art. 14 ter as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 14 quáter — Duty of protection by design and by default
**Spanish anchor:** Art. 14 quáter
**Tags:** privacy-by-design, privacy-by-default, technical-measures, organisational-measures, data-minimisation

### Plain-English text

For the purpose of complying with the principles and rights of data subjects established in this law, the controller must apply appropriate technical and organisational measures by design (desde el diseño) before and during the processing of the personal data. The measures to be applied must take into account the state of the art; the costs of implementation; the nature, scope, context, and purposes of the processing of data; and the risks associated with that activity.

Likewise, the data controller must apply technical and organisational measures to ensure that, by default, only the specific personal data strictly necessary for that activity are processed. For this purpose, account shall be taken of the amount of data collected, the extent of the processing, the retention period, and its accessibility.

### Original Spanish

> Artículo 14 quáter.- Deber de protección desde el
> diseño y por defecto. Con la finalidad de cumplir los
> principios y los derechos de los titulares establecidos en
> esta ley, el responsable debe aplicar medidas técnicas y
> organizativas adecuadas desde el diseño con anterioridad y
> durante el tratamiento de los datos personales. Las medidas
> a aplicar deberán tener en consideración el estado de la
> técnica; los costos de implementación; la naturaleza,
> ámbito, contexto y fines del tratamiento de datos; así
> como los riesgos asociados a dicha actividad.
> Asimismo, el responsable de datos deberá aplicar
> medidas técnicas y organizativas para garantizar que, por
> defecto, sólo sean objeto de tratamiento los datos
> personales específicos y estrictamente necesarios para
> dicha actividad. Para ello, se tendrá en consideración el
> número de datos recogidos, la extensión del tratamiento,
> el plazo de conservación y su accesibilidad.

### Cross-references
- Art. 3(c) (proportionality).
- Art. 3(f) (security).
- Art. 14 quinquies (security measures).

> **Source:** Ley 19.628 Art. 14 quáter as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 14 quinquies — Duty to adopt security measures
**Spanish anchor:** Art. 14 quinquies
**Tags:** security, technical-measures, organisational-measures, pseudonymisation, encryption, resilience, restoration, verification

### Plain-English text

The controller must adopt the necessary measures to safeguard compliance with the principle of security established in this law, considering the current state of the art and the costs of application, together with the nature, scope, context, and purposes of the processing, as well as the probability of the risks and the severity of their effects in relation to the type of data processed. The measures applied by the controller must ensure the confidentiality, integrity, availability, and resilience of the data-processing systems. They must also prevent alteration, destruction, loss, unauthorised processing, or unauthorised access.

Taking into account the state of the art, the costs of application, and the nature, scope, context, and purposes of the processing, as well as the risks of varying likelihood and severity for the rights and liberties of the data subjects, the controller and the processor shall apply appropriate technical and organisational measures to ensure a level of security appropriate to the risk, which may include, among others:

a) The pseudonymisation and encryption of personal data.

b) The ability to ensure the ongoing confidentiality, integrity, availability, and resilience of the processing systems and services.

c) The ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident.

d) A process for regular verification, assessment, and evaluation of the effectiveness of the technical and organisational measures to ensure the security of processing.

In the event of a security incident and in case of judicial or administrative controversy, it shall be for the controller to demonstrate the existence and operation of the security measures adopted on the basis of the risk levels and the available technology.

### Original Spanish

> Artículo 14 quinquies.- Deber de adoptar medidas de
> seguridad. El responsable de datos debe adoptar las medidas
> necesarias para resguardar el cumplimiento del principio de
> seguridad establecido en esta ley, considerando el estado
> actual de la técnica y los costos de aplicación, junto con
> la naturaleza, alcance, contexto y fines del tratamiento,
> así como la probabilidad de los riesgos y la gravedad de
> sus efectos en relación con el tipo de datos tratados. Las
> medidas aplicadas por el responsable deben asegurar la
> confidencialidad, integridad, disponibilidad y resiliencia
> de los sistemas de tratamiento de datos. Asimismo, deberán
> evitar la alteración, destrucción, pérdida, tratamiento o
> acceso no autorizado.
> En consideración al estado de la técnica, los costos
> de aplicación, y la naturaleza, el alcance, el contexto y
> los fines del tratamiento, así como los riesgos de
> probabilidad y gravedad variables para los derechos y
> libertades de los titulares, el responsable y el encargado
> del tratamiento aplicarán medidas técnicas y organizativas
> apropiadas para garantizar un nivel de seguridad adecuado al
> riesgo, que en su caso incluya, entre otros:
> a) La seudonimización y el cifrado de datos
> personales.
> b) La capacidad de garantizar la confidencialidad,
> integridad, disponibilidad y resiliencia permanentes de los
> sistemas y servicios de tratamiento.
> c) La capacidad de restaurar la disponibilidad y el
> acceso a los datos personales de forma rápida en caso de
> incidente físico o técnico.
> d) Un proceso de verificación, evaluación y
> valoración regulares de la eficacia de las medidas
> técnicas y organizativas para garantizar la seguridad del
> tratamiento.
> Ante la ocurrencia de un incidente de seguridad, y en
> caso de controversia judicial o administrativa,
> corresponderá al responsable acreditar la existencia y el
> funcionamiento de las medidas de seguridad adoptadas en base
> a los niveles de riesgo y a la tecnología disponible.

### Cross-references
- Art. 3(f) (principle of security).
- Art. 14 quáter (privacy by design).
- Art. 14 sexies (breach reporting).
- Art. 15 bis (processor security obligations).

> **Source:** Ley 19.628 Art. 14 quinquies as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 14 sexies — Duty to report security breaches
**Spanish anchor:** Art. 14 sexies
**Tags:** breach-notification, Agency, data-subjects, sensitive-data, children, financial-data, record-keeping

### Plain-English text

The controller must report to the Agency, by the most expedient means possible and without undue delay, breaches of the security measures (vulneraciones a las medidas de seguridad) that cause the accidental or unlawful destruction, leakage, loss, or alteration of the personal data it processes, or the unauthorised communication of or access to such data, where there is a reasonable risk to the rights and liberties of the data subjects.

The controller must record these communications, describing the nature of the breaches suffered, their effects, the categories of data and the approximate number of data subjects affected, and the measures adopted to manage them and to prevent future incidents.

Where such breaches concern sensitive personal data, data concerning children under fourteen years of age (niños y niñas menores de catorce años), or data relating to economic, financial, banking, or commercial obligations, the controller must also make this communication to the data subjects of such data, through their representatives where appropriate. This communication must be made in clear and simple language, singularising the affected data, the possible consequences of the security breaches, and the resolution or safeguard measures adopted. The notification must be made to each affected data subject, and if that is not possible, it shall be made through the dissemination or publication of a notice in a mass-circulation, nationally-distributed media outlet.

The information duties set out in this article are without prejudice to the other information duties established by other laws.

### Original Spanish

> Artículo 14 sexies.- Deber de reportar las
> vulneraciones a las medidas de seguridad. El responsable
> deberá reportar a la Agencia, por los medios más expeditos
> posibles y sin dilaciones indebidas, las vulneraciones a las
> medidas de seguridad que ocasionen la destrucción,
> filtración, pérdida o alteración accidental o ilícita de
> los datos personales que trate o la comunicación o acceso
> no autorizados a dichos datos, cuando exista un riesgo
> razonable para los derechos y libertades de los titulares.
> El responsable deberá registrar estas comunicaciones,
> describiendo la naturaleza de las vulneraciones sufridas,
> sus efectos, las categorías de datos y el número
> aproximado de titulares afectados y las medidas adoptadas
> para gestionarlas y precaver incidentes futuros.
> Cuando dichas vulneraciones se refieran a datos
> personales sensibles, datos relativos a niños y niñas
> menores de catorce años o datos relativos a obligaciones de
> carácter económico, financiero, bancario o comercial, el
> responsable deberá también efectuar esta comunicación a
> los titulares de estos datos, a través de sus
> representantes, cuando corresponda. Esta comunicación
> deberá realizarse en un lenguaje claro y sencillo,
> singularizando los datos afectados, las posibles
> consecuencias de las vulneraciones de seguridad y las
> medidas de solución o resguardo adoptadas. La notificación
> se deberá realizar a cada titular afectado y si ello no
> fuere posible, se realizará mediante la difusión o
> publicación de un aviso en un medio de comunicación social
> masivo y de alcance nacional.
> Los deberes de información señalados en este
> artículo no obstan a los demás deberes de información que
> establezcan otras leyes.

### Cross-references
- Art. 14 quinquies (security measures).
- Art. 16 (sensitive data).
- Art. 16 quáter (data of children and adolescents).
- Art. 30 et seq. (Agency).

> **Source:** Ley 19.628 Art. 14 sexies as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 14 septies — Differentiation of compliance standards
**Spanish anchor:** Art. 14 septies
**Tags:** proportionality, SME, Ley-20416, Agency-instruction, differentiated-compliance

### Plain-English text

The standards or minimum conditions imposed on the data controller for compliance with the information and security duties established in Articles 14 ter and 14 quinquies, respectively, shall be determined by considering the type of data involved; whether the controller is a natural or legal person; the size of the entity or enterprise according to the categories established in Article 2 of Law No. 20.416, which establishes special rules for smaller-sized enterprises (empresas de menor tamaño); the activity it carries out; and the volume, nature, and purposes of the personal data it processes.

The standards or minimum compliance conditions and the differentiated measures referred to in the preceding paragraph shall be determined by the Agency through general instruction.

### Original Spanish

> Artículo 14 septies.- Diferenciación de estándares
> de cumplimiento. Los estándares o condiciones mínimas que
> se impongan al responsable de datos para el cumplimiento de
> los deberes de información y de seguridad establecidos en
> los artículos 14 ter y 14 quinquies, respectivamente,
> serán determinados considerando el tipo de dato del que se
> trata, si el responsable es una persona natural o jurídica,
> el tamaño de la entidad o empresa de acuerdo a las
> categorías establecidas en el artículo segundo de la ley
> N° 20.416, que fija normas especiales para las empresas de
> menor tamaño, la actividad que desarrolla y el volumen,
> naturaleza y las finalidades de los datos personales que
> trata.
> Los estándares o condiciones mínimas de cumplimiento
> y las medidas diferenciadas a que alude el inciso anterior,
> serán determinados por la Agencia mediante instrucción
> general.

### Cross-references
- Art. 14 ter (information duty).
- Art. 14 quinquies (security measures).
- Law No. 20.416 (SME categories).

> **Source:** Ley 19.628 Art. 14 septies as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 15 — Cession of personal data
**Spanish anchor:** Art. 15
**Tags:** cession, transfer, consent, contract, legitimate-interests, writing, cedente, cesionario, nullity

### Plain-English text

Personal data may be ceded (cedidos) with the data subject's consent and for the fulfilment of the purposes of the processing. Personal data may also be ceded where the cession is necessary for the fulfilment and performance of a contract to which the data subject is a party; where there exists a legitimate interest of the transferring controller (cedente) or of the transferee (cesionario), in the terms provided in subparagraph (d) of Article 13; and where the law so provides.

Where the consent granted by the data subject at the time of the collection of the personal data did not contemplate their cession, consent must be obtained before the cession occurs — being considered for all legal purposes as a new processing operation.

The cession of data must be recorded in writing or through any suitable electronic medium. It must individualise the parties, the data subject to the cession, the foreseen purposes for the processing, and any other relevant information or stipulations agreed between the cedente and the cesionario.

The processing of the ceded personal data must be carried out by the cesionario in accordance with the purposes established in the cession contract.

Once the cession is perfected, the cesionario acquires the status of data controller for all legal purposes. The cedente, in turn, also retains the status of data controller in respect of the processing operations it continues to carry out.

If a cession of data takes place without the data subject's consent — where such consent is required — the cession shall be null and void, and the cesionario must erase all data received, without prejudice to the corresponding legal responsibilities.

### Original Spanish

> Artículo 15.- Cesión de datos personales. Los datos
> personales podrán ser cedidos con el consentimiento del
> titular y para el cumplimiento de los fines del tratamiento.
> También se podrán ceder los datos personales cuando la
> cesión sea necesaria para el cumplimiento y la ejecución
> de un contrato en que es parte el titular; cuando exista un
> interés legítimo del cedente o del cesionario, en los
> términos previstos en la letra d) del artículo 13, y
> cuando lo disponga la ley.
> En caso de que el consentimiento otorgado por el
> titular al momento de realizarse la recolección de los
> datos personales no haya considerado la cesión de los
> mismos, éste debe recabarse antes que se produzca,
> considerándose para todos los efectos legales como una
> nueva operación de tratamiento.
> La cesión de datos deberá constar por escrito o a
> través de cualquier medio electrónico idóneo. En ella se
> deberá individualizar a las partes, los datos que son
> objeto de la cesión, las finalidades previstas para el
> tratamiento y los demás antecedentes o estipulaciones que
> acuerden el cedente y el cesionario.
> El tratamiento de los datos personales cedidos deberá
> realizarse por el cesionario de conformidad a las
> finalidades establecidas en el contrato de cesión.
> Una vez perfeccionada la cesión, el cesionario
> adquiere la condición de responsable de datos para todos
> los efectos legales. El cedente, por su parte, también
> mantiene la calidad de responsable de datos, respecto de las
> operaciones de tratamiento que continúe realizando.
> Si se verifica una cesión de datos sin contar con el
> consentimiento del titular, siendo éste necesario, la
> cesión será nula, debiendo el cesionario suprimir todos
> los datos recibidos, sin perjuicio de las responsabilidades
> legales que correspondan.

### Cross-references
- Art. 2(v) (definition of cession of personal data).
- Art. 12 (consent).
- Art. 13(d) (legitimate interests).
- Art. 15 bis (processor relationship distinguished from cession).

> **Source:** Ley 19.628 Art. 15 as substituted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 15 bis — Processing of data through a third-party mandatary or processor
**Spanish anchor:** Art. 15 bis
**Tags:** processor, mandatary, instructions, sub-processing, joint-liability, contract, model-contracts, breach-reporting

### Plain-English text

The data controller may carry out the processing of data directly or through a third-party mandatary or processor (tercero mandatario o encargado). In the latter case, the third-party mandatary or processor carries out the processing of personal data in accordance with the assignment and instructions given by the controller, and is prohibited from processing the data for a purpose other than that agreed with the controller, as well as from ceding or delivering the data in cases in which the controller has not expressly and specifically authorised it for fulfilling the purpose of the assignment.

If the third-party mandatary or processor processes the data for a purpose other than the assignment, or cedes or delivers it without authorisation under the preceding paragraph, the processor shall be regarded as a data controller for all legal purposes — personally liable for the infringements it commits, and jointly and severally liable with the data controller for the damages caused — without prejudice to any contractual responsibilities towards the principal or data controller.

The processing of data through a third-party mandatary or processor shall be governed by the contract entered into between the controller and the processor, in accordance with applicable legislation. The contract must establish the subject of the assignment, its duration, the purpose of the processing, the type of personal data processed, the categories of data subjects to whom the data concern, and the rights and obligations of the parties. The processor may not delegate part or all of the assignment, except with specific written authorisation from the controller. A processor that delegates part or all of the assignment to another processor shall continue to be jointly and severally liable for the assignment and may not exempt itself from liability by arguing that it has delegated the processing. The Agency shall make standard model contracts available to the public on its website.

The third-party mandatary or processor must comply with the provisions of Articles 14 bis and 14 quinquies. The differentiation of compliance standards established in the first paragraph of Article 14 septies shall also apply to the third-party mandatary or processor. In the event of a breach of security measures, the third-party or mandatary must report this fact to the controller.

Once the data-processing service rendered by the third-party mandatary or processor has been completed, the data in its possession must be erased or returned to the data controller, as appropriate.

### Original Spanish

> Artículo 15 bis.- Tratamiento de datos a través de un
> tercero mandatario o encargado. El responsable puede
> efectuar el tratamiento de datos en forma directa o a
> través de un tercero mandatario o encargado. En este
> último caso, el tercero mandatario o encargado realiza el
> tratamiento de datos personales conforme al encargo y a las
> instrucciones que le imparta el responsable, quedándole
> prohibido su tratamiento para un objeto distinto del
> convenido con el responsable, así como su cesión o entrega
> en los casos en que el responsable no lo haya autorizado de
> manera expresa y específicamente para cumplir con el objeto
> del encargo.
> Si el tercero mandatario o encargado trata los datos
> con un objeto distinto del encargo convenido o los cede o
> entrega sin haber sido autorizado en los términos
> dispuestos en el inciso anterior, se le considerará como
> responsable de datos para todos los efectos legales,
> debiendo responder personalmente por las infracciones en que
> incurra y solidariamente con el responsable de datos por los
> daños ocasionados, sin perjuicio de las responsabilidades
> contractuales que le correspondan frente al mandante o
> responsable de datos.
> El tratamiento de datos a través de un tercero
> mandatario o encargado se regirá por el contrato celebrado
> entre el responsable y el encargado, con arreglo a la
> legislación vigente. En el contrato se deberá establecer
> el objeto del encargo, la duración del mismo, la finalidad
> del tratamiento, el tipo de datos personales tratados, las
> categorías de titulares a quienes conciernen los datos, y
> los derechos y obligaciones de las partes. El encargado no
> podrá delegar parte o la totalidad del encargo, salvo que
> conste una autorización específica y por escrito del
> responsable. El encargado que delegue a otro encargado parte
> o la totalidad del encargo, continuará siendo
> solidariamente responsable sobre dicho encargo y no podrá
> eximirse de responsabilidad argumentando que ha delegado el
> tratamiento. La Agencia pondrá a disposición del público
> modelos tipo de contratos en su página web.
> El tercero mandatario o encargado deberá cumplir con
> lo dispuesto en los artículos 14 bis y 14 quinquies. La
> diferenciación de estándares de cumplimiento establecida
> en el inciso primero del artículo 14 septies también será
> aplicable al tercero mandatario o encargado. Tratándose de
> una vulneración a las medidas de seguridad, el tercero o
> mandatario deberá reportar este hecho al responsable.
> Cumplida la prestación del servicio de tratamiento por
> parte del tercero mandatario o encargado, los datos que
> obran en su poder deben ser suprimidos o devueltos al
> responsable de datos, según corresponda.

### Cross-references
- Art. 2(x) (definition of third-party mandatary or processor).
- Art. 14 bis (confidentiality).
- Art. 14 quinquies (security).
- Art. 14 septies (differentiation of compliance standards).
- Art. 15 (cession distinguished from processor relationship).

> **Source:** Ley 19.628 Art. 15 bis as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 15 ter — Personal data protection impact assessment
**Spanish anchor:** Art. 15 ter
**Tags:** DPIA, impact-assessment, high-risk, profiling, large-scale-processing, monitoring, sensitive-data, Agency-consultation

### Plain-English text

Where it is likely that a type of processing — by its nature, scope, context, technology used, or purposes — may produce a high risk to the rights of the data subjects, the data controller must, prior to the start of the processing operations, carry out a personal-data protection impact assessment (evaluación del impacto en protección de datos personales).

An impact assessment shall always be required in cases of:

a) Systematic and exhaustive evaluation of the personal aspects of data subjects, based on automated processing or decisions — such as profiling — and that produce significant legal effects on them.

b) Large-scale or massive processing of data.

c) Processing involving systematic observation or monitoring of a publicly accessible area.

d) Processing of sensitive and specially protected data, in the exception cases to consent.

The Personal Data Protection Agency shall establish and publish an indicative list of the types of processing operations that do or do not require an impact assessment relating to the protection of personal data. The Agency shall also establish minimum guidelines for carrying out this assessment, considering at least, among such criteria, the description of the processing operations, their purpose, the assessment of necessity and proportionality with respect to their purpose, the assessment of risks, and mitigation measures.

Controllers may consult the Personal Data Protection Agency where — based on the result of the assessment — the processing proves to be high-risk, with a view to obtaining recommendations from said entity.

### Original Spanish

> Artículo 15 ter.- Evaluación de impacto en
> protección de datos personales. Cuando sea probable que un
> tipo de tratamiento, por su naturaleza, alcance, contexto,
> tecnología utilizada o fines, pueda producir un alto riesgo
> para los derechos de las personas titulares de los datos
> personales, el responsable del tratamiento deberá realizar,
> previo al inicio de las operaciones del tratamiento, una
> evaluación del impacto en protección de datos personales.
> La evaluación de impacto se requerirá siempre en
> casos de:
> a) Evaluación sistemática y exhaustiva de aspectos
> personales de los titulares de datos, basadas en tratamiento
> o decisiones automatizadas, como la elaboración de
> perfiles, y que produzcan en ellos efectos jurídicos
> significativos.
> b) Tratamiento masivo de datos o a gran escala.
> c) Tratamiento que implique observación o monitoreo
> sistemático de una zona de acceso público.
> d) Tratamiento de datos sensibles y especialmente
> protegidos, en las hipótesis de excepción del
> consentimiento.
> La Agencia de Protección de Datos Personales
> establecerá y publicará una lista orientativa de los tipos
> de operaciones de tratamiento que requieran o no una
> evaluación de impacto relativa a la protección de datos
> personales. La Agencia también establecerá las
> orientaciones mínimas para realizar esta evaluación,
> considerando a lo menos en dichos criterios, la descripción
> de las operaciones de tratamiento, su finalidad, la
> evaluación de la necesidad y la proporcionalidad con
> respecto a su finalidad, la evaluación de los riesgos y
> medidas de mitigación.
> Los responsables podrán consultar a la Agencia de
> Protección de Datos Personales, cuando en virtud del
> resultado de la evaluación, el tratamiento demuestre ser de
> alto riesgo a efectos de obtener recomendaciones de parte de
> dicha entidad.

### Cross-references
- Art. 8 bis (automated decisions).
- Art. 14 quáter (privacy by design).
- Art. 16 (sensitive data).
- Art. 30 et seq. (Agency).

> **Source:** Ley 19.628 Art. 15 ter as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Párrafo Segundo — Processing of sensitive personal data

---

## Article 16 — General rule for the processing of sensitive personal data
**Spanish anchor:** Art. 16
**Tags:** sensitive-data, express-consent, exceptions, public-disclosure, non-profit, vital-interests, labour, social-security, judicial-claims

### Plain-English text

The processing of sensitive personal data may only be carried out when the data subject to whom such data concern manifests express consent, given through a written, verbal, or equivalent technological-medium statement.

Without prejudice to the foregoing, the processing of sensitive personal data is lawful, without the data subject's consent, in the following cases:

a) Where the processing concerns sensitive personal data that the data subject has manifestly made public, and the processing is related to the purposes for which they were published.

b) Where the processing is based on a legitimate interest pursued by a public-law or private-law legal person not pursuing for-profit purposes, and the following conditions are met:

i. Its purpose is political, philosophical, religious, cultural, trade-union, or guild-related (gremial);

ii. The processing it carries out concerns exclusively its members or affiliates;

iii. The processing of data has the object of fulfilling the institution's specific purposes;

iv. The legal person provides the necessary guarantees to prevent leaks, theft, or unauthorised use or processing of the data; and

v. The personal data are not communicated or ceded to third parties.

If these conditions are met, the legal person shall not require the data subject's consent to process its data, including sensitive personal data. In case of doubt or administrative or judicial controversy, the controller must demonstrate compliance.

When a member of the legal person ceases to belong to it, their data must be anonymized or erased.

c) Where the processing of the data subject's personal data is indispensable for safeguarding the life, health, or physical or psychological integrity of the data subject or another person, or where the data subject is physically or legally prevented from giving consent. Once the impediment ceases, the controller must inform the data subject in detail of the data that were processed and the specific processing operations that were carried out.

d) Where the processing of the data is necessary for the establishment, exercise, or defence of a right before the courts of justice or an administrative body.

e) Where the processing of data is necessary for the exercise of rights and the fulfilment of obligations of the controller or the data subject, in the labour or social-security sphere, and it is carried out within the framework of the law.

f) Where the law expressly authorises or mandates the processing of sensitive personal data.

The exceptions for processing data without consent set out in this article are also applicable to the processing of data that are not sensitive.

### Original Spanish

> Artículo 16.- Regla general para el tratamiento de
> datos personales sensibles. El tratamiento de los datos
> personales sensibles sólo puede realizarse cuando el
> titular a quien conciernen estos datos manifiesta su
> consentimiento en forma expresa, otorgado a través de una
> declaración escrita, verbal o por un medio tecnológico
> equivalente.
> Sin perjuicio de lo anterior, es lícito el tratamiento
> de datos personales sensibles, sin el consentimiento del
> titular, en los siguientes casos:
> a) Cuando el tratamiento se refiere a datos personales
> sensibles que el titular ha hecho manifiestamente públicos
> y su tratamiento esté relacionado con los fines para los
> cuales fueron publicados.
> b) Cuando el tratamiento se basa en un interés
> legítimo realizado por una persona jurídica de derecho
> público o de derecho privado que no persiga fines de lucro
> y se cumplan las siguientes condiciones:
> i. Su finalidad sea política, filosófica, religiosa,
> cultural, sindical o gremial;
> ii. El tratamiento que realice se refiera
> exclusivamente a sus miembros o afiliados;
> iii. El tratamiento de datos tenga por objeto cumplir
> las finalidades específicas de la institución;
> iv. La persona jurídica otorgue las garantías
> necesarias para evitar filtraciones, sustracciones o un uso
> o tratamiento no autorizado de los datos, y
> v. Los datos personales no se comuniquen o cedan a
> terceros.
> Cumpliéndose estas condiciones, la persona jurídica
> no requerirá el consentimiento del titular para tratar sus
> datos, incluidos los datos personales sensibles. En caso de
> duda o controversia administrativa o judicial, el
> responsable de datos deberá acreditar su concurrencia.
> Cuando un integrante de la persona jurídica deje de
> pertenecer a ella, sus datos deberán ser anonimizados o
> suprimidos.
> c) Cuando el tratamiento de los datos personales del
> titular resulte indispensable para salvaguardar la vida,
> salud o integridad física o psíquica del titular o de otra
> persona o, cuando el titular se encuentre física o
> jurídicamente impedido de otorgar su consentimiento. Una
> vez que cese el impedimento, el responsable debe informar
> detalladamente al titular los datos que fueron tratados y
> las operaciones específicas de tratamiento que fueron
> realizadas.
> d) Cuando el tratamiento de los datos sea necesario
> para la formulación, ejercicio o defensa de un derecho ante
> los tribunales de justicia o un órgano administrativo.
> e) Cuando el tratamiento de datos sea necesario para el
> ejercicio de derechos y el cumplimiento de obligaciones del
> responsable o del titular de datos, en el ámbito laboral o
> de seguridad social, y se realice en el marco de la ley.
> f) Cuando el tratamiento de datos personales sensibles
> lo autorice o mandate expresamente la ley.
> Las excepciones para tratar datos sin consentimiento,
> mencionadas en este artículo, se entienden aplicables al
> tratamiento de datos que no revisten el carácter de datos
> sensibles.

### Cross-references
- Art. 2(g) (definition of sensitive personal data).
- Art. 16 bis (health data).
- Art. 16 ter (biometric data).
- Art. 16 quáter (children and adolescents).

> **Source:** Ley 19.628 Art. 16 as substituted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 16 bis — Sensitive personal data relating to health and the human biological profile
**Spanish anchor:** Art. 16 bis
**Tags:** health-data, biological-profile, genetic, biometric, public-health, research, employment-prohibition, scientific-research

### Plain-English text

If the provision of the first paragraph of Article 16 is met, personal data relating to the data subject's health — as well as data relating to the data subject's biological profile, such as genetic, proteomic, or metabolic data — may only be processed for the purposes provided for by special laws on health matters.

Sensitive personal data relating to the data subject's health and biological profile may only be processed without consent — respecting the principles and rules established in this law — in the following cases:

a) Where it is indispensable to safeguard the life or physical or psychological integrity of the data subject or another person, or where the data subject is physically or legally prevented from giving consent. Once the impediment ceases, the controller must inform the data subject in detail of the data that were processed and the specific processing operations carried out.

b) In cases of legally decreed sanitary alert.

c) Where used for historical, statistical, or scientific purposes, for studies or research that serve purposes of public interest or for the benefit of human health, or for the development of medical products or supplies that could not be developed otherwise. The results of scientific studies and research using personal data relating to health or the biological profile may be freely published or disseminated. For this purpose, the data published must first be anonymized.

d) Where the processing of data is necessary for the establishment, exercise, or defence of a right before the courts of justice or before an administrative body.

e) Where the processing is necessary for purposes of preventive or occupational medicine, evaluation of the employee's working capacity, medical diagnosis, provision of health or social care or treatment, or management of health and social-care systems and services.

f) Where the law so permits and expressly indicates the purpose that such processing shall have.

The processing and cession of data relating to the health and biological profile of a data subject — and of the biological samples associated with an identified or identifiable person, including the storage of the biological material — is prohibited where the data or samples have been collected in the labour, educational, sports, social, insurance, security, or identification sphere, unless the law expressly authorises their processing in qualified cases and refers to one of the cases mentioned in this article.

The exceptions for processing data without consent mentioned in this article are also applicable to the processing of data that do not have the special character referred to in this provision.

### Original Spanish

> Artículo 16 bis.- Datos personales sensibles relativos
> a la salud y al perfil biológico humano. Si se cumple lo
> dispuesto en el inciso primero del artículo 16, los datos
> personales relativos a la salud del titular, así como
> aquéllos relativos al perfil biológico del titular, tales
> como los datos genéticos, proteómicos o metabólicos,
> sólo podrán ser tratados para los fines previstos por las
> leyes especiales en materia sanitaria.
> Sólo se podrán tratar los datos personales sensibles
> relativos a la salud del titular y a su perfil biológico,
> sin contar con su consentimiento, respetando los principios
> y reglas establecidos en la presente ley, en los siguientes
> casos:
> a) Cuando éste resulte indispensable para salvaguardar
> la vida o integridad física o psíquica del titular o de
> otra persona o, cuando el titular se encuentre física o
> jurídicamente impedido de otorgar su consentimiento. Una
> vez que cese el impedimento, el responsable debe informar
> detalladamente al titular los datos que fueron tratados y
> las operaciones específicas de tratamiento que fueron
> realizadas.
> b) En casos de alerta sanitaria legalmente decretada.
> c) Cuando sean utilizados con fines históricos,
> estadísticos o científicos, para estudios o
> investigaciones que atiendan fines de interés público o
> vayan en beneficio de la salud humana, o para el desarrollo
> de productos o insumos médicos que no podrían
> desarrollarse de otra manera. Los resultados de los estudios
> e investigaciones científicas que utilicen datos personales
> relativos a la salud o al perfil biológico pueden ser
> publicados o difundidos libremente. Para ello deberán
> previamente anonimizarse los datos que se publiquen.
> d) Cuando el tratamiento de los datos sea necesario
> para la formulación, ejercicio o defensa de un derecho ante
> los tribunales de justicia o ante un órgano administrativo.
> e) Cuando el tratamiento sea necesario para fines de
> medicina preventiva o laboral, evaluación de la capacidad
> laboral del trabajador, diagnóstico médico, prestación de
> asistencia o tratamiento de tipo sanitario o social, o
> gestión de sistemas y servicios de asistencia sanitaria y
> social.
> f) Cuando la ley así lo permita e indique expresamente
> la finalidad que deberá tener dicho tratamiento.
> Se prohíbe el tratamiento y la cesión de los datos
> relativos a la salud y al perfil biológico de un titular y
> las muestras biológicas asociadas a una persona
> identificada o identificable, incluido el almacenamiento del
> material biológico, cuando los datos o muestras han sido
> recolectados en el ámbito laboral, educativo, deportivo,
> social, de seguros, de seguridad o identificación, salvo
> que la ley expresamente autorice su tratamiento en casos
> calificados y que se refiera a alguno de los casos
> mencionados en este artículo.
> Las excepciones para tratar datos sin el consentimiento
> mencionado en este artículo se entienden aplicables al
> tratamiento de datos que no revisten el carácter especial a
> que se refiere este precepto.

### Cross-references
- Art. 16 (general sensitive-data rule).
- Art. 16 quinquies (historical/statistical/scientific research).

> **Source:** Ley 19.628 Art. 16 bis as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 16 ter — Biometric personal data
**Spanish anchor:** Art. 16 ter
**Tags:** biometric, fingerprint, iris, facial, voice, information-duty, consent

### Plain-English text

Biometric personal data are those obtained from a specific technical processing, relating to the physical, physiological, or behavioural characteristics of a person, that permit or confirm the unique identification of that person — such as fingerprints, the iris, hand or facial features, and the voice.

These data may only be processed where the provision of the first paragraph of Article 16 is met, and provided that the controller provides the data subject with the following specific information:

a) Identification of the biometric system used;

b) The specific purpose for which the data collected by the biometric system will be used;

c) The period during which the biometric data will be used; and

d) The form in which the data subject may exercise their rights.

Biometric personal data may only be processed without consent in the cases set out in the second paragraph of Article 16 bis.

### Original Spanish

> Artículo 16 ter.- Datos personales biométricos. Son
> datos personales biométricos aquellos obtenidos a partir de
> un tratamiento técnico específico, relativos a las
> características físicas, fisiológicas o conductuales de
> una persona que permitan o confirmen la identificación
> única de ella, tales como la huella digital, el iris, los
> rasgos de la mano o faciales y la voz.
> Sólo podrán tratarse estos datos cuando se cumpliere
> con lo dispuesto en el inciso primero del artículo 16 y
> siempre que el responsable proporcione al titular la
> siguiente información específica:
> a) La identificación del sistema biométrico usado;
> b) La finalidad específica para la cual los datos
> recolectados por el sistema biométrico serán utilizados;
> c) El período durante el cual los datos biométricos
> serán utilizados, y
> d) La forma en que el titular puede ejercer sus
> derechos.
> Los datos personales biométricos podrán tratarse sin
> consentimiento sólo en los casos señalados en el inciso
> segundo del artículo 16 bis.

### Cross-references
- Art. 2(g) (definition of sensitive personal data).
- Art. 16 (general sensitive-data rule).
- Art. 16 bis (health-data exceptions cross-referenced).

> **Source:** Ley 19.628 Art. 16 ter as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Párrafo Tercero — Processing of special categories of personal data

---

## Article 16 quáter — Personal data relating to children, girls, and adolescents
**Spanish anchor:** Art. 16 quáter
**Tags:** children, girls, adolescents, best-interests, progressive-autonomy, parental-consent, sixteen-years, fourteen-years, schools

### Plain-English text

The processing of the personal data concerning children, girls, and adolescents may only be carried out attending to their best interests (interés superior) and to the respect for their progressive autonomy (autonomía progresiva).

Subject to the requirement established in the preceding paragraph, processing of the personal data of children and girls requires the consent granted by their parents or legal representatives or by the person in charge of the personal care of the child or girl, unless the law expressly authorises or mandates it.

The personal data of adolescents may be processed in accordance with the authorisation rules provided in this law for adults, except for the provision of the following paragraph.

Sensitive personal data of adolescents under sixteen years of age may be processed only with the consent granted by their parents or legal representatives or by the person in charge of the personal care of the minor, unless the law expressly authorises or mandates it.

For the purposes of this law, children or girls are considered to be those under fourteen years of age, and adolescents are those over fourteen and under eighteen years of age.

It is a special obligation of educational establishments and of all persons or public or private entities that process or administer personal data of children, girls, and adolescents — including those exercising their personal care — to ensure the lawful use and protection of the personal information concerning children, girls, and adolescents.

### Original Spanish

> Artículo 16 quáter.- Datos personales relativos a los
> niños, niñas y adolescentes. El tratamiento de los datos
> personales que conciernen a los niños, niñas y
> adolescentes, sólo puede realizarse atendiendo al interés
> superior de éstos y al respeto de su autonomía progresiva.
> Cumpliéndose la exigencia establecida en el inciso
> anterior, para tratar los datos personales de los niños y
> niñas se requiere el consentimiento otorgado por sus padres
> o representantes legales o por quien tiene a su cargo el
> cuidado personal del niño o niña, salvo que expresamente
> lo autorice o mandate la ley.
> Los datos personales de los adolescentes se podrán
> tratar de acuerdo a las normas de autorización previstas en
> esta ley para los adultos, salvo lo dispuesto en el inciso
> siguiente.
> Los datos personales sensibles de los adolescentes
> menores de dieciséis años sólo se podrán tratar con el
> consentimiento otorgado por sus padres o representantes
> legales o quien tiene a su cargo el cuidado personal del
> menor, salvo que expresamente lo autorice o mandate la ley.
> Para los efectos de esta ley, se consideran niños o
> niñas a los menores de catorce años, y adolescentes, a los
> mayores de catorce y menores de dieciocho años.
> Constituye una obligación especial de los
> establecimientos educacionales y de todas las personas o
> entidades públicas o privadas que traten o administren
> datos personales de niños, niñas y adolescentes, incluidos
> quienes ejercen su cuidado personal, velar por el uso
> lícito y la protección de la información personal que
> concierne a los niños, niñas y adolescentes.

### Cross-references
- Art. 12 (consent).
- Art. 14 sexies (breach reporting for children's data).
- Art. 16 (sensitive data).

> **Source:** Ley 19.628 Art. 16 quáter as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 16 quinquies — Personal data for historical, statistical, scientific, and study or research purposes
**Spanish anchor:** Art. 16 quinquies
**Tags:** historical, statistical, scientific, research, public-interest, legitimate-interest, anonymisation

### Plain-English text

There is deemed to be a legitimate interest in the processing of personal data carried out by natural or legal persons, public or private — including public bodies — where the processing is carried out exclusively for historical, statistical, scientific, and study or research purposes, all of which must serve purposes of public interest.

Data controllers must adopt and demonstrate that they have complied with all quality and security measures necessary to safeguard that the data are used exclusively for such purposes. In the case of sensitive personal data, the controller must identify possible risks and implement measures aimed at their reduction or mitigation. Once these conditions are met, the controller may store and use the data for an indeterminate period of time.

Controllers that have processed personal data exclusively for these purposes may make publications with the results and analyses obtained, having previously adopted the necessary measures to anonymize the data that are published.

### Original Spanish

> Artículo 16 quinquies.- Datos personales con fines
> históricos, estadísticos, científicos y de estudios o
> investigaciones. Se entiende que existe un interés
> legítimo en el tratamiento de datos personales que realicen
> las personas naturales o jurídicas, públicas o privadas,
> incluidos los organismos públicos, cuando el tratamiento se
> realiza exclusivamente con fines históricos, estadísticos,
> científicos y para estudios o investigaciones, todos los
> cuales deben atender fines de interés público.
> Los responsables de datos deberán adoptar y acreditar
> que han cumplido con todas las medidas de calidad y
> seguridad necesarias para resguardar que los datos se
> utilicen exclusivamente para tales fines. En el caso de los
> datos personales sensibles, el responsable debe identificar
> los riesgos posibles e implementar las medidas tendientes a
> su reducción o mitigación. Cumplidas estas condiciones, el
> responsable podrá almacenar y utilizar los datos por un
> período indeterminado de tiempo.
> Los responsables que hayan tratado datos personales
> exclusivamente con estas finalidades podrán efectuar
> publicaciones con los resultados y análisis obtenidos,
> debiendo previamente adoptar las medidas necesarias para
> anonimizar los datos que se publiquen.

### Cross-references
- Art. 13(d) (legitimate interest).
- Art. 16 (sensitive data).

> **Source:** Ley 19.628 Art. 16 quinquies as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

## Article 16 sexies — Geolocation data
**Spanish anchor:** Art. 16 sexies
**Tags:** geolocation, lawful-bases, information-duty, value-added-services

### Plain-English text

The processing of the data subject's geolocation personal data may be carried out under the same sources of lawfulness established in Articles 12 and 13.

The data subject must be informed clearly, sufficiently, and in a timely manner of the type of geolocation data that will be processed, the purpose and duration of the processing, and whether the data will be communicated or ceded to a third party for the provision of a value-added service.

### Original Spanish

> Artículo 16 sexies.- Datos de geolocalización. El
> tratamiento de los datos personales de geolocalización del
> titular se podrá realizar bajo las mismas fuentes de
> licitud establecidas en los artículos 12 y 13.
> El titular de datos deberá ser informado de manera
> clara, suficiente y oportuna, del tipo de datos de
> geolocalización que serán tratados, de la finalidad y
> duración del tratamiento y si los datos se comunicarán o
> cederán a un tercero para la prestación de un servicio con
> valor añadido.

### Cross-references
- Art. 12, Art. 13 (lawful bases).
- Art. 14 ter (information duty).

> **Source:** Ley 19.628 Art. 16 sexies as inserted by Ley 21.719 Art. 1° item 8 (in force 2026-12-01).

---

---

<!-- source: corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md -->
## FILE: corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md

# Ley 19.628 — Título III: Use of Personal Data Relating to Economic, Financial, Banking, or Commercial Obligations (De la utilización de datos personales relativos a obligaciones de carácter económico, financiero, bancario o comercial — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** In force from 2026-12-01.

---

## Article 17 — General rule for processing of data relating to financial, banking, or commercial obligations
**Spanish anchor:** Art. 17°
**Tags:** financial-data, commercial-obligations, credit-data, protest, default, performance, unemployment-blocking, Commercial-Bulletin, purpose-limitation, prescribed-obligations

> **Epigraph note:** Ley 21.719 Art. 1° item 9.b.i added the epigraph "Regla general del tratamiento de datos relativos a obligaciones de carácter financiero, bancario o comercial." to the first paragraph of this article.

### Plain-English text

**General rule for processing data relating to obligations of a financial, banking, or commercial nature.** Data controllers of personal-data registries or databases (responsables de los registros o bases de datos personales) may only communicate (comunicar) information concerning economic, financial, banking, or commercial obligations (obligaciones de carácter económico, financiero, bancario o comercial) where those obligations appear in protested bills of exchange and promissory notes (letras de cambio y pagarés protestados); cheques protested for insufficient funds (falta de fondos), for having been drawn against a closed current account, or for any other cause; as well as the performance or non-performance (el cumplimiento o incumplimiento) of obligations arising from mortgage loans (mutuos hipotecarios) and from loans or credits of banks, financial companies, mortgage-loan administrators, savings and credit cooperatives, public bodies (organismos públicos) and State enterprises subject to general legislation, and companies that administer credits granted for purchases at commercial retailers (casas comerciales). Excluded from this rule is information relating to credits granted by the National Institute of Agricultural Development (Instituto Nacional de Desarrollo Agropecuario) to its users, and information relating to economic, financial, banking, or commercial obligations that have been rescheduled (repactadas), renegotiated, or novated, or that are subject to some pending condition.

> **TN:** "Repactadas" (rescheduled) is a Chilean financial term for an agreement to reschedule a debt. The 1999 baseline uses "repactadas, renegociadas o novadas" as three alternative debt-restructuring modalities; all three are rendered with their literal English equivalents. "Casas comerciales" are Chilean retail credit establishments (stores offering in-house credit); "commercial retailers" captures the concept.

The following monetary obligations may also be communicated: other monetary obligations (obligaciones de dinero) as determined by the President of the Republic by supreme decree, provided they are supported by validly issued payment or credit instruments in which the express consent of the debtor or obligor to payment is recorded, together with the maturity date. The following debts may not be communicated: debts contracted with public or private enterprises that provide electricity, water, telephone, and gas services; debts contracted with higher-education institutions under Laws No. 18.591 and No. 19.287; debts contracted with banks or financial institutions under Law No. 20.027, or within the framework of student financing lines for higher education administered by the Production Development Corporation (Corporación de Fomento de la Producción); any debt contracted for the purpose of obtaining, for oneself or for third parties, a formal educational service at any level; debts contracted with public or private health-care providers and related companies — whether financial institutions, commercial retailers, or similar entities — in the context of outpatient, inpatient, or emergency health care, including consultations, procedures, tests, programmes, surgeries, or operations; nor may debts contracted with motorway concessionaires (concesionarios de autopistas) for use of their infrastructure be communicated.

> **TN — amendment-layer history:** The second paragraph above (additional communicable obligations and exclusions list) reflects pre-21.719 amendments incorporated inline in the BCN baseline extraction. It was substantially amended by Ley 19.812 (Art. 1° N° 2, D.O. 13.06.2002) and further modified by Ley 20.575 (Art. 7 a, D.O. 17.02.2012). These prior amendment layers are preserved verbatim here and are not affected by Ley 21.719.

The data controller entities (entidades responsables) that administer personal data banks (bancos de datos personales) may not publish or communicate the information referred to in this article — in particular the protests and defaults contained in it — when those protests or defaults arose during a period of unemployment (cesantía) affecting the debtor.

For these purposes, the Unemployment Insurance Administrator (Administradora de Fondos de Cesantía) must communicate the data of its beneficiaries to the Commercial Bulletin (Boletín de Informaciones Comerciales) only for as long as the benefits subsist, so that the Bulletin may block the information concerning those persons.

> **TN:** "Boletín de Informaciones Comerciales" is the specific Chilean commercial publication established by Ministry of Finance Supreme Decree No. 950 of 1928, commonly translated as the "Commercial Bulletin." "Administradora de Fondos de Cesantía" is the unemployment insurance fund administrator established by Law No. 19.728; it is rendered by its full English description on first use, with the Spanish retained for identification.

However, persons not enrolled in the unemployment insurance scheme must prove that condition to the Commercial Bulletin by submitting the legally executed settlement agreement (finiquito) or, if there is a dispute, the attendance record from the Labour Inspectorate (Inspección del Trabajo), in order to invoke this right for a period of three months, renewable once. To obtain that renewal, the debtor must attach a sworn declaration (declaración jurada) stating that the debtor remains unemployed.

The blocking of data shall be free of charge (sin costo) for the debtor.

Data blocking shall not apply with respect to persons who incurred annotations in the commercial information system during the year prior to the date of termination of their employment relationship.

The entities responsible for administering personal data banks may not, under any circumstances, indicate — by any sign or characterisation — that a person is a beneficiary of this law.

Data controllers must erase from their registries or databases (registros o bases de datos) all personal information relating to prescribed obligations (obligaciones prescritas), without need for a request, court order, or instruction from the data-protection authority.

> **TN — item 9.c:** The above paragraph was inserted as a new eighth paragraph (inciso octavo) by Ley 21.719 Art. 1° item 9.c. The former eighth paragraph (on the prohibition of any sign indicating the data subject is a beneficiary of this law) becomes the ninth paragraph.

> **TN — amendment-layer history:** The unemployment-blocking mechanism (paragraphs 3 through 8 above, on the role of the Administradora de Fondos de Cesantía, the Boletín de Informaciones Comerciales, finiquito-based proof, three-month renewable blocking, no cost to the debtor, and the prior-year-anotaciones exception) reflects multiple pre-21.719 amendments incorporated inline in the BCN baseline extraction: Ley 19.812 (Art. 1° N° 3, D.O. 13.06.2002), Ley 20.463 (Art. Único, D.O. 25.10.2010), Ley 20.575 (Art. 7 b, D.O. 17.02.2012), Ley 21.214 (Art. Único, D.O. 28.02.2020), and Ley 21.504 (Art. Único, D.O. 10.11.2022). These prior amendment layers are preserved verbatim here. Ley 21.719 did not substitute any of these paragraphs; it only added the new paragraph on erasure of data relating to prescribed obligations (item 9.c, noted above).

### Original Spanish

> Artículo 17.- Los responsables de los registros o
> bases de datos personales sólo podrán comunicar
> información que verse sobre obligaciones de carácter
> económico, financiero, bancario o comercial, cuando éstas
> consten en letras de cambio y pagarés protestados; cheques
> protestados por falta de fondos, por haber sido girados
> contra cuenta corriente cerrada o por otra causa; como
> asimismo el cumplimiento o incumplimiento de obligaciones derivadas de
> mutuos hipotecarios y de préstamos o créditos de bancos,
> sociedades financieras, administradoras de mutuos
> hipotecarios, cooperativas de ahorros y créditos,
> organismos públicos y empresas del Estado sometidas a la
> legislación común, y de sociedades administradoras de
> créditos otorgados para compras en casas comerciales. Se
> exceptúa la información relacionada con los créditos
> concedidos por el Instituto Nacional de Desarrollo
> Agropecuario a sus usuarios, y la información relacionada
> con obligaciones de carácter económico, financiero,
> bancario o comercial en cuanto hayan sido repactadas,
> renegociadas o novadas, o éstas se encuentren con alguna
> modalidad pendiente.
> También podrán comunicarse aquellas otras
> obligaciones de dinero que determine el Presidente de la
> República mediante decreto supremo, las que deberán estar
> sustentadas en instrumentos de pago o de crédito
> válidamente emitidos, en los cuales conste el
> consentimiento expreso del deudor u obligado al pago y su
> fecha de vencimiento. No podrá comunicarse la información
> relacionada con las deudas contraídas con empresas
> públicas o privadas que proporcionen servicios de
> electricidad, agua, teléfono y gas; tampoco las deudas
> contraídas con instituciones de educación superior de
> conformidad a las leyes números 18.591 y 19.287, ni
> aquellas adquiridas con bancos o instituciones financieras
> de conformidad a la ley N° 20.027, o en el marco de las
> líneas de financiamiento a estudiantes para cursar estudios
> en educación superior, administradas por la Corporación de
> Fomento de la Producción, ni alguna deuda contraída con la
> finalidad de recibir para sí o para terceros un servicio
> educacional formal en cualquiera de sus niveles; ni las
> deudas contraídas con prestadores de salud públicos o
> privados y empresas relacionadas, sean instituciones
> financieras, casas comerciales u otras similares, en el
> marco de una atención o acción de salud ambulatoria,
> hospitalaria o de emergencia sean éstas consultas,
> procedimientos, exámenes, programas, cirugías u
> operaciones; tampoco podrán comunicarse las deudas
> contraídas con concesionarios de autopistas por el uso de
> su infraestructura.
> Las entidades responsables que administren bancos de
> datos personales no podrán publicar o comunicar la
> información referida en el presente artículo, en especial
> los protestos y morosidades contenidas en él, cuando éstas
> se hayan originado durante el período de cesantía que
> afecte al deudor.
> Para estos efectos, la Administradora de Fondos de
> Cesantía comunicará los datos de sus beneficiarios al
> Boletín de Informaciones Comerciales sólo mientras
> subsistan sus beneficios para los efectos de que éste
> bloquee la información concerniente a tales personas.
> Sin embargo, las personas que no estén incorporadas al
> seguro de cesantía deberán acreditar dicha condición ante
> el Boletín de Informaciones Comerciales, acompañando el
> finiquito extendido en forma legal o, si existiese
> controversia, con el acta de comparecencia ante la
> Inspección del Trabajo, para los efectos de impetrar este
> derecho por tres meses renovable hasta por una vez. Para que
> opere dicha renovación se deberá adjuntar una declaración
> jurada del deudor en la que manifieste que mantiene su
> condición de cesante.
> El bloqueo de datos será sin costo para el deudor.
> No procederá el bloqueo de datos respecto de quienes
> consignen anotaciones en el sistema de información
> comercial durante el año anterior a la fecha de término de
> su relación laboral.
> Los responsables deberán suprimir de sus registros o
> bases de datos, toda aquella información personal relativa
> a obligaciones prescritas, sin necesidad de mediar
> solicitud, orden judicial, ni instrucción de la autoridad
> de protección de datos.
> Las entidades responsables de la administración de
> bases de datos personales no podrán señalar bajo ninguna
> circunstancia, signo o caracterización que la persona se
> encuentra beneficiada por esta ley.

### Cross-references
- Art. 2(c) (definition of communication or transmission of data).
- Art. 4 (processing from publicly accessible sources; no-consent rule for economic/financial data).
- Art. 9 (purpose-limitation; prohibition on non-objective risk assessments).
- Art. 16 (judicial remedy — enhanced fine range for violations of Arts. 17 and 18).
- Art. 18 (five-year limit on communicating financial obligation data; post-payment prohibition).
- Art. 19 (update obligations upon payment or extinction of obligation).
- Art. 23 (civil liability for unlawful processing).
- Disposición transitoria Art. 1 (Ley 19812 transitional provisions applicable to this article).

> **Source:** Ley 19.628 Art. 17 as amended by Ley 21.719 Art. 1° item 9 (in force 2026-12-01). Item 9.a replaced "bancos de datos" with "bases de datos" throughout the article; item 9.b.i added the epigraph "Regla general del tratamiento de datos relativos a obligaciones de carácter financiero, bancario o comercial." to the first paragraph; item 9.b.ii inserted "cumplimiento o" before "incumplimiento" in the first paragraph; item 9.c inserted the new eighth paragraph on erasure of data relating to prescribed obligations.

---

## Article 18 — Limitation on processing data for financial, banking, or commercial obligations
**Spanish anchor:** Art. 18°
**Tags:** financial-data, time-limit, five-year-rule, post-payment-prohibition, courts, limitation-epigraph

> **Epigraph note:** Ley 21.719 Art. 1° item 10 added the epigraph "Limitación del tratamiento de datos para obligaciones financieras, bancarias o comerciales." to the first paragraph of this article.

### Plain-English text

**Limitation on the processing of data for financial, banking, or commercial obligations.** In no case may the data referred to in the preceding article, relating to an identified or identifiable person (persona identificada o identificable), be communicated once five years have elapsed since the respective obligation became enforceable (exigible).

Nor may data relating to that obligation continue to be communicated after it has been paid or has been extinguished by any other legal means.

Notwithstanding the foregoing, information required by courts of justice in connection with pending proceedings (juicios pendientes) may be communicated.

> **TN:** The five-year limitation runs from when the obligation became "exigible" (enforceable / fell due), not from when it was recorded or protested. This is a key distinction preserved in the translation. "Extinguished by any other legal means" covers novation, set-off, prescription, and other civil-law modes of extinction.

> **TN — amendment-layer history:** Article 18 was modified by Ley 19.812 (Art. 1° N° 4, D.O. 13.06.2002), a pre-21.719 amendment incorporated inline in the BCN baseline extraction. This prior amendment layer is preserved verbatim here. Ley 21.719 only added the article epigraph "Limitación del tratamiento de datos para obligaciones financieras, bancarias o comerciales." (item 10).

### Original Spanish

> Artículo 18.- Limitación del tratamiento de datos
> para obligaciones financieras, bancarias o comerciales.
> En ningún caso pueden comunicarse
> los datos a que se refiere el artículo anterior, que
> se relacionen con una persona identificada o
> identificable, luego de transcurridos cinco años desde
> que la respectiva obligación se hizo exigible.
> Tampoco se podrá continuar comunicando los datos
> relativos a dicha obligación después de haber sido
> pagada o haberse extinguido por otro modo legal.
> Con todo, se comunicará a los tribunales de
> Justicia la información que requieran con motivo de
> juicios pendientes.

### Cross-references
- Art. 2(d) (expired data — five-year expiry rule creates expired data under Art. 2(d)).
- Art. 17 (types of financial obligation data subject to this rule).
- Art. 19 (duty to update data upon payment or extinction; interaction with this article's prohibition).
- Art. 23 (civil liability for unlawful processing).
- Title VII (sanctions regime — applicable to violations of this article under the post-21.719 framework).

> **Source:** Ley 19.628 Art. 18 as amended by Ley 21.719 Art. 1° item 10 (in force 2026-12-01). Item 10 added the epigraph "Limitación del tratamiento de datos para obligaciones financieras, bancarias o comerciales." to the first paragraph.

---

## Article 19 — Effects of the extinction of the economic, banking, or commercial obligation
**Spanish anchor:** Art. 19°
**Tags:** financial-data, update-duty, payment-notification, creditor-duty, seven-day-rule, blocking, extinction-epigraph

> **Epigraph note:** Ley 21.719 Art. 1° item 11.a.i added the epigraph "Efectos de la extinción de la obligación económica, bancaria o comercial." to the first paragraph of this article.

### Plain-English text

**Effects of the extinction of the economic, banking, or commercial obligation.** The payment or extinction of these obligations by any other legal means does not cause the expiry (caducidad) or loss of legal basis (pérdida de fundamento legal) of the respective data for the purposes of Article 4° (rights of the data subject), while the time periods established in the preceding article are still pending.

When payment is made or the obligation is extinguished by any other means in which the creditor directly intervenes, the creditor must notify that fact to the data controller (responsable del registro o base de datos accesible al público) that at the time communicated the protest or default, at the latest within the following seven business days (días hábiles), so that the controller records the corresponding new data, following payment of the applicable fee, which shall be charged to the debtor. The debtor may choose instead to request the modification directly from the database (base de datos) and to release the creditor from that obligation, provided the creditor gives the debtor sufficient proof of payment; decisions that the debtor must express in writing.

Those who carry out the processing of personal data originating from or collected from the said publicly accessible source must modify the data in the same sense as soon as that source communicates the payment or extinction of the obligation, or within the following three days. If it is not possible for them to do so, they must block the data of the relevant data subject (titular) until the information is updated.

Violation of any of these obligations shall be investigated and sanctioned in accordance with the provisions of Title VII of this law.

> **TN:** The seven-business-day deadline on the creditor's notification obligation is a specific procedural rule in the 1999 baseline that has no direct equivalent in GDPR-style frameworks. "Fundamento legal" is rendered as "legal basis" to align with the term used throughout the consolidated law (e.g., Arts. 4, 12, 13).

### Original Spanish

> Artículo 19.- Efectos de la extinción de la
> obligación económica, bancaria o comercial. El pago o la extinción de estas
> obligaciones por cualquier otro modo no produce la caducidad
> o la pérdida de fundamento legal de los datos respectivos
> para los efectos del artículo 4°, mientras estén
> pendientes los plazos que establece el artículo precedente.
> Al efectuarse el pago o extinguirse la obligación por
> otro modo en que intervenga directamente el acreedor, éste
> avisará tal hecho, a más tardar dentro de los siguientes
> siete días hábiles, al responsable del registro o base de
> datos accesible al público que en su oportunidad comunicó
> el protesto o la morosidad, a fin de que consigne el nuevo
> dato que corresponda, previo pago de la tarifa si fuere
> procedente, con cargo al deudor. El deudor podrá optar por
> requerir directamente la modificación a la base de datos y
> liberar del cumplimiento de esa obligación al acreedor que
> le entregue constancia suficiente del pago; decisiones que
> deberá expresar por escrito.
> Quienes efectúen el tratamiento de datos personales
> provenientes o recolectados de la aludida fuente accesible
> al público deberán modificar los datos en el mismo sentido
> tan pronto aquélla comunique el pago o la extinción de la
> obligación, o dentro de los tres días siguientes. Si no
> les fuera posible, bloquearán los datos del respectivo
> titular hasta que esté actualizada la información.
> La infracción de cualquiera de estas obligaciones se
> conocerá y sancionará de conformidad a lo dispuesto en el
> Título VII de esta ley.

### Cross-references
- Art. 2(b) (definition of blocking).
- Art. 2(i) (definition of publicly accessible sources).
- Art. 4 (rights of the data subject — legal basis persistence while Art. 18 periods run).
- Art. 17 (types of financial obligation data subject to the update duty).
- Art. 18 (five-year time limit and post-payment prohibition — legal basis persistence rule of this article applies within that framework).
- Title VII (sanctions regime — applicable to violations of this article).

> **Source:** Ley 19.628 Art. 19 as amended by Ley 21.719 Art. 1° item 11 (in force 2026-12-01). Item 11.a.i added the epigraph "Efectos de la extinción de la obligación económica, bancaria o comercial." to the first paragraph; item 11.a.ii replaced the reference to "artículo 12" with "artículo 4°"; item 11.b replaced "o banco de datos" with "o base de datos" and "al banco de datos" with "a la base de datos" in the second paragraph; item 11.c substituted in the final paragraph the phrase "de acuerdo a lo previsto en el artículo 16" with "de conformidad a lo dispuesto en el Título VII de esta ley".

---

---

<!-- source: corpus/19628-data-protection-consolidated/titulo-04-organismos-publicos.md -->
## FILE: corpus/19628-data-protection-consolidated/titulo-04-organismos-publicos.md

# Ley 19.628 — Título IV: Processing of Personal Data by Public Bodies (Del tratamiento de datos personales por los órganos públicos — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** In force from 2026-12-01.

> **Title note:** Ley 21.719 Art. 1° item 12 replaced the entire Título IV. The 1999 baseline Título IV (Arts. 20–22 on processing by public bodies within competence, criminal-record data, and Civil Registry registration) is superseded by a comprehensive framework (Arts. 20–26) for processing by public bodies (órganos públicos), covering general rule, principles, inter-agency communications, rights exercise, special regimes (criminal/security/emergency), criminal-record data, and a regulation.

---

## Article 20 — General rule for processing of data by public bodies
**Spanish anchor:** Art. 20
**Tags:** public-bodies, legal-functions, competence, consent-exception, no-consent-required

### Plain-English text

The processing of personal data carried out by public bodies (órganos públicos) is lawful when it is carried out for the fulfilment of their legal functions, within the scope of their competence, in accordance with the rules established by law and the provisions of this Title. Under these conditions, public bodies act as data controllers and do not require the data subject's consent to process their personal data.

### Original Spanish

> Artículo 20.- Regla general del tratamiento de datos
> por órganos públicos. Es lícito el tratamiento de los
> datos personales que efectúan los órganos públicos cuando
> se realiza para el cumplimiento de sus funciones legales,
> dentro del ámbito de sus competencias, de conformidad a las
> normas establecidas en la ley, y a las disposiciones
> previstas en este Título. En esas condiciones, los órganos
> públicos actúan como responsables de datos y no requieren
> el consentimiento del titular para tratar sus datos
> personales.

### Cross-references
- Art. 2(j) (definition of public bodies).
- Art. 21 (applicable principles).
- Art. 22 (communication or cession between public bodies).
- Art. 23 (exercise of rights).

> **Source:** Ley 19.628 Art. 20 as substituted by Ley 21.719 Art. 1° item 12 (in force 2026-12-01).

---

## Article 21 — Principles and rules applicable to processing of data by public bodies
**Spanish anchor:** Art. 21
**Tags:** public-bodies, principles, coordination, probity, efficiency, interoperability, cross-referenced-provisions

### Plain-English text

The processing of personal data carried out by public bodies is governed by the principles established in Article 3 of this law and the general principles governing the Administration of the State, especially the principles of coordination, probity, and efficiency.

Under the principle of coordination, public agencies must achieve a high degree of interoperability and coherence, in order to avoid contradictions in stored information and reiteration of requirements for information or documents from data subjects. Under the principle of efficiency, the duplication of procedures and formalities among public agencies, and between them and the holders of the information, must be avoided.

Without prejudice to the other rules established in this Title, the processing of data carried out by public bodies is subject to the provisions established in Articles 2, 14, 14 bis, 14 ter, 14 quáter, 14 quinquies, 14 sexies, and 15 bis; the articles of Paragraphs Second and Third of Title II; and the articles of Title V and Title VII of this law. Likewise, Articles 4, 5, 6, 7, and 8 apply to them, in accordance with the provisions of Article 23.

### Original Spanish

> Artículo 21.- Principios y normas aplicables al
> tratamiento de datos de los órganos públicos. El
> tratamiento de los datos personales que realicen los
> órganos públicos se rige por los principios establecidos
> en el artículo 3° de esta ley y los principios generales
> que rigen la Administración del Estado, especialmente los
> principios de coordinación, probidad y eficiencia.
> En virtud del principio de coordinación los organismos
> públicos deben alcanzar un alto grado de interoperabilidad
> y coherencia, de modo de evitar contradicciones en la
> información almacenada y reiteración de requerimientos de
> información o documentos a los titulares de datos. Conforme
> al principio de eficiencia se debe evitar la duplicación de
> procedimientos y trámites entre los organismos públicos y
> entre éstos y los titulares de la información.
> Sin perjuicio de las demás normas establecidas en el
> presente Título, son aplicables al tratamiento de datos que
> efectúen los órganos públicos, las disposiciones
> establecidas en los artículos 2°, 14, 14 bis, 14 ter, 14
> quáter, 14 quinquies, 14 sexies y 15 bis, los artículos de
> los Párrafos Segundo y Tercero del Título II y los
> artículos del Título V y del Título VII de esta ley.
> Asimismo, le son aplicables los artículos 4°, 5°, 6°,
> 7° y 8°, en conformidad a lo dispuesto en el artículo 23.

### Cross-references
- Art. 3 (principles).
- Art. 23 (exercise of rights against public bodies).

> **Source:** Ley 19.628 Art. 21 as substituted by Ley 21.719 Art. 1° item 12 (in force 2026-12-01).

---

## Article 22 — Communication or cession of data by a public body
**Spanish anchor:** Art. 22
**Tags:** public-bodies, communication, cession, inter-agency, citizen-benefits, retention, fiscalisation, transparency-website, law-20285

### Plain-English text

Public bodies are empowered to communicate or cede specific personal data, or all or part of their personal databases or sets of data, to other public bodies, provided that the communication or cession of the data is necessary for the fulfilment of their legal functions and both bodies act within the scope of their competence. The communication or cession of data must be carried out for a specific processing, and the receiving public body may not use them for other purposes.

Likewise, data or personal databases may be communicated or ceded between public agencies, exclusively when required for processing intended to grant benefits to the data subject, avoid duplication of procedures for citizens, or avoid reiteration of requirements for information or documents from the same data subjects.

The public body receiving the data may retain them only for the time necessary to carry out the specific processing for which they were requested, after which they must be erased or anonymized. These data may be stored for a longer period when the public body needs to handle claims or challenges, conduct control or follow-up activities, or use them as a guarantee for decisions adopted.

In order to be able to communicate or cede personal data to private persons or entities, public agencies must obtain the data subject's consent, unless the communication or cession of data is necessary to fulfil the public agency's functions in matters of supervision or inspection.

Where the communication or cession of personal data is made by virtue of a request for access to information made under Article 10 of Law No. 20.285, public agencies must obtain the data subject's consent on the occasion provided for in Article 20 of that law.

With respect to the communication of data relating to criminal, civil, administrative, and disciplinary infringements, the provisions of Article 25 shall apply.

Public agencies must inform monthly through their institutional website of the agreements signed with other public agencies and with private entities relating to the cession or transfer of personal data. This obligation shall be supervised by the Agency.

### Original Spanish

> Artículo 22.- Comunicación o cesión de datos por un
> órgano público. Los órganos públicos están facultados
> para comunicar o ceder datos personales específicos, o todo
> o parte de sus bases de datos o conjuntos de datos, a otros
> órganos públicos, siempre que la comunicación o cesión
> de los datos resulte necesaria para el cumplimiento de sus
> funciones legales y ambos órganos actúen dentro del
> ámbito de sus competencias. La comunicación o cesión de
> los datos se debe realizar para un tratamiento específico y
> el órgano público receptor no los podrá utilizar para
> otros fines.
> Asimismo, se podrá comunicar o ceder datos o bases de
> datos personales entre organismos públicos, exclusivamente
> cuando ellos se requieran para un tratamiento que tenga por
> finalidad otorgar beneficios al titular, evitar duplicidad
> de trámites para los ciudadanos o reiteración de
> requerimientos de información o documentos para los mismos
> titulares.
> El órgano público receptor de los datos sólo puede
> conservarlos por el tiempo necesario para efectuar el
> tratamiento específico para el cual fueron requeridos,
> luego de lo cual deberán ser suprimidos o anonimizados.
> Estos datos se podrán almacenar por un tiempo mayor cuando
> el órgano público requiera atender reclamaciones o
> impugnaciones, realizar actividades de control o
> seguimiento, o sirvan para dar garantía de las decisiones
> adoptadas.
> Para los efectos de poder comunicar o ceder datos
> personales a personas o entidades privadas, los organismos
> públicos deberán contar con el consentimiento del titular,
> salvo que la comunicación o cesión de datos sea necesaria
> para cumplir las funciones del organismo público en materia
> de fiscalización o inspección.
> Cuando se trate de comunicar o ceder datos personales
> en virtud de una solicitud de acceso a la información
> formulada con arreglo a lo establecido en el artículo 10 de
> la ley N° 20.285, los organismos públicos deberán contar
> con el consentimiento del titular obtenido en la oportunidad
> prevista en el artículo 20 de dicha ley.
> Respecto de la comunicación de los datos relativos a
> infracciones penales, civiles, administrativas y
> disciplinarias, se aplicará lo dispuesto en el artículo
> 25.
> Los organismos públicos deberán informar mensualmente
> a través de su página web institucional los convenios
> suscritos con otros organismos públicos y con entidades
> privadas relativos a cesión o transferencia de datos
> personales. Esta obligación será fiscalizada por la
> Agencia.

### Cross-references
- Art. 20 (general rule for public bodies).
- Art. 25 (criminal/civil/administrative/disciplinary infringement data).
- Law No. 20.285 (transparency law cross-reference).
- Art. 30 et seq. (Agency oversight).

> **Source:** Ley 19.628 Art. 22 as substituted by Ley 21.719 Art. 1° item 12 (in force 2026-12-01).

---

## Article 23 — Exercise of the data subject's rights; administrative tutela procedure and illegality claim
**Spanish anchor:** Art. 23
**Tags:** public-bodies, rights-exercise, access, rectification, opposition, supervisory-exception, secret-information, claim-before-agency, art-41

### Plain-English text

The data subject may exercise before the public body the rights of access, rectification, and opposition recognised by this law. The data subject may also object to specific processing where this is contrary to the provisions of this Title. The data subject may exercise the right of erasure in the cases provided for in the third paragraph of the preceding article.

Public agencies shall not accept requests for access, rectification, opposition, erasure, or temporary blocking of personal data in the following cases:

a) Where doing so would prevent or hinder compliance with the supervisory, investigative, victim and witness protection, or sanctioning functions of the public agency, and

b) Where doing so would affect the secret character of the information established by law.

The exercise of the data subject's rights must be carried out in accordance with the procedure established in Article 11 of this law, addressed to the chief of the relevant service (jefe superior del servicio).

The data subject may bring a claim before the Agency where the public agency has denied — expressly or tacitly — a request in which the data subject exercises any of the rights recognised by this law. The claim shall be subject to the rules provided for in the administrative procedure for the protection of rights established in Article 41.

### Original Spanish

> Artículo 23.- Ejercicio de los derechos del titular,
> procedimiento administrativo de tutela y reclamo de
> ilegalidad. El titular de datos podrá ejercer ante el
> órgano público los derechos de acceso, rectificación y
> oposición que le reconoce esta ley. El titular también
> podrá oponerse a un tratamiento específico cuando éste
> sea contrario a las disposiciones de este Título. El
> titular podrá ejercer el derecho de supresión en los casos
> previstos en el inciso tercero del artículo anterior.
> Los organismos públicos no acogerán las solicitudes
> de acceso, rectificación, oposición, supresión o bloqueo
> temporal de los datos personales en los siguientes casos:
> a) Cuando con ello se impida o entorpezca el
> cumplimiento de las funciones fiscalizadoras,
> investigativas, de protección a víctimas y testigos o
> sancionatorias del organismo público, y
> b) Cuando con ello se afecte el carácter secreto de la
> información establecido por la ley.
> El ejercicio de los derechos del titular se deberá
> realizar de acuerdo al procedimiento establecido en el
> artículo 11 de esta ley, dirigiéndose al jefe superior del
> servicio.
> El titular podrá reclamar ante la Agencia cuando el
> organismo público le haya denegado, en forma expresa o
> tácita, una solicitud en que ejerce cualquiera de los
> derechos que le reconoce esta ley. La reclamación se
> sujetará a las normas previstas en el procedimiento
> administrativo de tutela de derechos establecido en el
> artículo 41.

### Cross-references
- Art. 4–9 (substantive rights).
- Art. 11 (procedure before the controller).
- Art. 41 (procedure before the Agency).

> **Source:** Ley 19.628 Art. 23 as substituted by Ley 21.719 Art. 1° item 12 (in force 2026-12-01).

---

## Article 24 — Special regimes
**Spanish anchor:** Art. 24
**Tags:** public-bodies, criminal-prosecution, national-security, emergency, reserved-information, secret-information, special-regime

### Plain-English text

The processing, communication, or cession of sensitive personal data carried out by public bodies with competence in the matters indicated below shall be subject exclusively to the special regulation regime established in this article:

a) Those carried out for the purposes of prevention, investigation, detection, or prosecution of criminal infringements or execution of criminal sanctions — including activities for protection and prevention against threats and risks to public security, protection of victims and witnesses, criminal analysis, and reportability of criminal information. With respect to data processed for this purpose, the provisions of Article 25 shall not apply.

b) Those concerning matters directly related to national security, national defence, and the country's foreign policy.

c) Those carried out for the exclusive object of addressing an emergency or catastrophe situation, declared in accordance with the law, and only while that declaration remains in force.

d) Those that are protected by rules of secrecy, reserve, or confidentiality established in their respective laws. This exception also includes data that, in compliance with a legal obligation, public bodies must cede to another public body or to third parties, the recipient in such case being required to process them maintaining the same obligation of secrecy, reserve, or confidentiality.

The relevant public bodies may lawfully process, cede, and communicate personal data, provided this is done for the fulfilment of their legal functions, within the scope of their competence, and respecting the fundamental guarantees established in Article 19, No. 4, of the Political Constitution of the Republic and the principles established in Article 3.

In order to carry out the processing, cessions, and communications of data for the purposes provided in subparagraphs (a), (b), and (c) above, public bodies and their authorities shall be obliged to exchange information and provide the personal data requested for these purposes — provided that they refer to processing carried out for a specific purpose authorised by law or, when this is not possible, that the requirement is a necessary and proportionate measure.

The Personal Data Protection Agency may — after consulting the relevant competent bodies — issue instructions to specify the manner of applying the said guarantees and principles to the cases mentioned, in order to ensure their safeguard and to permit the proper fulfilment of the relevant bodies' legal functions.

### Original Spanish

> Artículo 24.- Regímenes especiales. El tratamiento,
> comunicación o cesión de datos personales sensibles,
> realizado por órganos públicos competentes en las materias
> que a continuación se indican, estarán sujetos
> exclusivamente al régimen de regulación especial
> establecido en este artículo:
> a) Aquellos que se realicen con fines de prevención,
> investigación, detección o enjuiciamiento de infracciones
> penales o de ejecución de sanciones penales, incluidas las
> actividades de protección y prevención frente a las
> amenazas y riesgos contra la seguridad pública, protección
> a víctimas y testigos, análisis criminal y reportabilidad
> de la información criminal. Respecto de los datos que se
> realicen con esta finalidad, no será aplicable lo dispuesto
> en el artículo 25.
> b) Aquellos en materias relacionadas directamente con
> la seguridad de la Nación, la defensa nacional y la
> política exterior del país.
> c) Aquellos realizados con el objeto exclusivo de
> atender una situación de emergencia o catástrofe,
> declarada de conformidad a la ley y sólo mientras
> permanezca vigente esta declaración.
> d) Aquellos que se encuentren protegidos por normas de
> secreto, reserva o confidencialidad, establecidas en sus
> respectivas leyes. Dentro de esta excepción se entienden
> también comprendidos los datos que, en cumplimiento de una
> obligación legal, los órganos públicos deban ceder a otro
> órgano público o a terceros, debiendo en tal caso el
> receptor tratarlos manteniendo la misma obligación de
> secreto, reserva o confidencialidad.
> Los órganos públicos correspondientes podrán tratar,
> ceder y comunicar datos personales de forma lícita, siempre
> y cuando se realice para el cumplimiento de sus funciones
> legales, dentro del ámbito de sus competencias y respetando
> las garantías fundamentales establecidas en el artículo
> 19, N° 4, de la Constitución Política de la República y
> los principios establecidos en el artículo 3°.
> Con el objeto de realizar los tratamientos, cesiones y
> comunicaciones de datos para la finalidad prevista en las
> letras a), b) y c) anteriores, los órganos públicos y sus
> autoridades estarán obligadas a intercambiar información y
> proporcionar los datos personales que les sean requeridos
> para estos fines, siempre que se refieran a tratamientos que
> se realicen con una finalidad específica autorizada por ley
> o, cuando esto no sea posible, el requerimiento sea una
> medida necesaria y proporcional.
> La Agencia de Protección de Datos Personales podrá,
> oyendo previamente a los órganos competentes, dictar
> instrucciones para especificar la forma de aplicar las
> referidas garantías y principios a los casos mencionados,
> de manera de asegurar su resguardo y permitir el debido
> cumplimiento de las funciones legales de los órganos
> correspondientes.

### Cross-references
- Art. 14 bis (confidentiality — special application to Art. 24 data).
- Art. 25 (criminal/civil/administrative/disciplinary infringement data — interaction).
- Art. 3 (principles).

> **Source:** Ley 19.628 Art. 24 as substituted by Ley 21.719 Art. 1° item 12 (in force 2026-12-01).

---

## Article 25 — Data relating to criminal, civil, administrative, and disciplinary infringements
**Spanish anchor:** Art. 25
**Tags:** infringement-data, criminal-records, prescription, accuracy, registries, five-year-publication, mass-processing-prohibition, reserved

### Plain-English text

Personal data relating to the commission and sanction of criminal, civil, administrative, and disciplinary infringements may only be processed by public agencies for the fulfilment of their legal functions, within the scope of their competence and in the cases expressly provided for by law.

In the communications carried out by public agencies on the occasion of the processing of these personal data, they must at all times ensure that the information communicated or made public is accurate, sufficient, current, and complete.

Personal data relating to the commission and conviction of criminal, civil, administrative, or disciplinary infringements may not be communicated or made public once the respective criminal, civil, administrative, or disciplinary action has prescribed, or once the imposed penalty or sanction has been served or has prescribed — which must be declared or established by the competent public authority. The foregoing is without prejudice to the incorporation, maintenance, and consultation of this information in the registries kept by public bodies by express provision of the law, in the form and for the time provided in the law that establishes the corresponding specific obligation. Persons who serve in public bodies are obligated to maintain secrecy with respect to this information, which must be kept as reserved information.

Where the law provides that information relating to the commission and sanction of criminal, civil, administrative, and disciplinary infringements must be made public through its incorporation in a sanctions registry, or its publication on the website of a public body or in any other communication or dissemination medium — without fixing a period of time during which such information must remain available — the following rules shall apply:

a) With respect to criminal infringements, the publicity periods shall be governed by the specific rules governing this type of infringement.

b) With respect to civil, administrative, and disciplinary infringements, they shall remain accessible to the public for a period of five years.

The massive processing of personal data contained in the electronic registries of criminal, civil, administrative, and disciplinary infringements maintained by public agencies is prohibited. Failure to comply with this prohibition constitutes a very serious infringement (infracción gravísima) in accordance with this law.

The cases in which the information is requested by the courts of justice or another public agency for the fulfilment of their legal functions and within the scope of their competence are excepted from the prohibition of communication; they must maintain due reserve.

Notwithstanding the provisions of the third paragraph of this article, personal data relating to the commission and sanction of criminal infringements have a reserved character and — except for the legal provisions that authorise their processing — may not be communicated or ceded to third parties by the public agencies that hold them.

### Original Spanish

> Artículo 25.- Datos relativos a infracciones penales,
> civiles, administrativas y disciplinarias. Los datos
> personales relativos a la comisión y sanción de
> infracciones penales, civiles, administrativas y
> disciplinarias sólo pueden ser tratados por los organismos
> públicos para el cumplimiento de sus funciones legales,
> dentro del ámbito de sus competencias y en los casos
> expresamente previstos en la ley.
> En las comunicaciones que realicen los organismos
> públicos, con ocasión del tratamiento de estos datos
> personales, deberán velar en todo momento por que la
> información comunicada o hecha pública sea exacta,
> suficiente, actual y completa.
> No podrán comunicarse o hacerse públicos los datos
> personales relativos a la comisión y condena de
> infracciones penales, civiles, administrativas o
> disciplinarias, una vez prescrita la acción penal, civil,
> administrativa o disciplinaria respectiva, o una vez que se
> haya cumplido o prescrito la pena o la sanción impuesta, lo
> que deberá ser declarado o constatado por la autoridad
> pública competente. Lo anterior es sin perjuicio de la
> incorporación, mantenimiento y consulta de esta
> información en los registros que llevan los órganos
> públicos por expresa disposición de la ley, en la forma y
> por el tiempo previsto en la ley que establece la
> obligación específica correspondiente. Las personas que se
> desempeñen en los órganos públicos están obligadas a
> guardar secreto respecto de esta información, la que
> deberá ser mantenida como información reservada.
> Cuando la ley disponga que la información relativa a
> la comisión y sanción de infracciones penales, civiles,
> administrativas y disciplinarias deba hacerse pública a
> través de su incorporación en un registro de sanciones, o
> su publicación en el sitio web de un órgano público o en
> cualquier otro medio de comunicación o difusión, sin fijar
> un período de tiempo durante el cual deba permanecer
> disponible esta información, se seguirán las siguientes
> reglas:
> a) Respecto de las infracciones penales, los plazos de
> publicidad se regirán por las normas particulares que rigen
> para este tipo de infracciones.
> b) Respecto de las infracciones civiles,
> administrativas y disciplinarias, permanecerán accesibles
> al público por el período de cinco años.
> Se prohíbe el tratamiento masivo de los datos
> personales contenidos en los registros electrónicos de
> infracciones penales, civiles, administrativas y
> disciplinarias que lleven los organismos públicos. El
> incumplimiento de esta prohibición constituye una
> infracción gravísima de conformidad a esta ley.
> Exceptúanse de la prohibición de comunicación los
> casos en que la información sea solicitada por los
> tribunales de justicia u otro organismo público para el
> cumplimiento de sus funciones legales y dentro del ámbito
> de su competencia, quienes deberán mantener la debida
> reserva.
> No obstante lo dispuesto en el inciso tercero del
> presente artículo, los datos personales relativos a la
> comisión y sanción de infracciones penales revisten
> carácter reservado y, salvo las disposiciones legales que
> autorizan su tratamiento, no podrán ser comunicados o
> cedidos a terceras personas por los organismos públicos que
> los posean.

### Cross-references
- Art. 24 (special regimes — criminal-prosecution data carved out).
- Title VII (sanctions regime — very serious infringement classification).

> **Source:** Ley 19.628 Art. 25 as substituted by Ley 21.719 Art. 1° item 12 (in force 2026-12-01).

---

## Article 26 — Regulation
**Spanish anchor:** Art. 26
**Tags:** regulation, inter-agency-cession, anonymisation-procedures, ministry-secretaría-general, treasury, economy, Title-VIII-exclusion

### Plain-English text

The conditions, modalities, and instruments for the communication or cession of personal data among public agencies and with private persons or organisations shall be regulated through a regulation (reglamento) issued by the Ministry of the General Secretariat of the Presidency (Ministerio Secretaría General de la Presidencia) and signed by the Minister of Finance and by the Minister of Economy, Development, and Tourism, after a report from the Agency. This regulation shall also regulate the procedures for the anonymization of personal data, especially sensitive personal data.

This regulation shall not apply to those cessions in which any of the bodies referred to in Title VIII of this law participates.

### Original Spanish

> Artículo 26.- Reglamento. Las condiciones, modalidades
> e instrumentos para la comunicación o cesión de datos
> personales entre organismos públicos y con personas u
> organismos privados, se regularán a través de un
> reglamento expedido por el Ministerio Secretaría General de
> la Presidencia y suscrito por el Ministro de Hacienda y por
> el Ministro de Economía, Fomento y Turismo, previo informe
> de la Agencia. En este mismo reglamento se regularán los
> procedimientos de anonimización de los datos personales,
> especialmente los datos personales sensibles.
> Con todo, este reglamento no será aplicable a aquellas
> cesiones en las que tenga participación alguno de los
> órganos a los que se refiere el Título VIII de esta ley.

### Cross-references
- Art. 22 (inter-agency communication).
- Title VIII (data agencies/treasury bodies exclusion).

> **Source:** Ley 19.628 Art. 26 as substituted by Ley 21.719 Art. 1° item 12 (in force 2026-12-01).

---

---

<!-- source: corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md -->
## FILE: corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md

# Ley 19.628 — Título V: International Transfer of Personal Data (De la transferencia internacional de datos personales — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** In force from 2026-12-01.

> **Title note:** Ley 21.719 Art. 1° item 13 replaced the entire Título V. The 1999 baseline Título V ("De la responsabilidad por las infracciones a esta ley", Art. 23 on civil liability for unlawful processing) is superseded by the new "Transferencia internacional de datos personales" framework (Arts. 27, 28, 29). The substantive civil-liability regime survives indirectly in the new Title VII (sanctions) inserted by item 14, and damages remain claimable under general civil law. The filename `titulo-05-responsabilidad.md` is preserved for git-history continuity even though the title is now about international transfers.

---

## Article 27 — General rule of authorisation
**Spanish anchor:** Art. 27
**Tags:** international-transfer, adequacy-decision, contractual-clauses, binding-corporate-rules, certification, ad-hoc-transfers, consent, treaty-obligations

### Plain-English text

Subject to the requirements that, in accordance with this law, authorise the processing of data, international transfer operations of data are lawful in any of the following cases:

a) Where the transfer is made to a public or private person, entity, or organisation subject to the legal order of a country that provides adequate levels of personal-data protection, in accordance with the provisions of Article 28.

b) Where the transfer of data is covered by contractual clauses, binding corporate rules (normas corporativas vinculantes), or other legal instruments signed between the controller carrying out the transfer and the controller or third-party mandatary receiving the transfer — and provided that they establish adequate guarantees, in accordance with Article 28.

c) Where the controller carrying out the transfer and the controller or third-party mandatary receiving the transfer adopt a compliance model or certification mechanism, and adequate guarantees are established therein, in accordance with Article 28.

In the absence of an adequacy decision or adequate guarantees, a specific and non-habitual transfer may be made if one of the following circumstances is met:

a) Where the data subject has expressly consented to making a specific and determined international transfer of data.

b) Where it concerns specific banking, financial, or stock-exchange transfers carried out in accordance with the laws that regulate such transfers.

c) Where data must be transferred to comply with obligations acquired in international treaties or conventions that have been ratified by the Chilean State and are in force.

d) Where the transfer is necessary by application of cooperation agreements, information exchange, or supervision that have been signed by public bodies for the fulfilment of their functions and in the exercise of their competences.

e) Where the data transfer made by a natural or legal person, public or private, has been expressly authorised by the law for a determined purpose.

f) Where the transfer is made for the purpose of providing or requesting international judicial cooperation.

g) Where the transfer is necessary for the conclusion or performance of a contract between the data subject and the controller, or for the performance of pre-contractual measures taken at the data subject's request.

h) Where it is necessary to adopt urgent measures in medical or health matters, for the prevention or diagnosis of diseases, for medical treatments, or for the management of health or sanitary services.

### Original Spanish

> Artículo 27.- Regla general de autorización.
> Cumpliéndose los requisitos que, de conformidad a esta ley,
> autorizan al tratamiento de datos, son lícitas las
> operaciones de transferencia internacional de datos en
> cualquiera de los siguientes casos:
> a) Cuando la transferencia se realice a una persona,
> entidad u organización pública o privada, sujeta al
> ordenamiento jurídico de un país que proporcione niveles
> adecuados de protección de datos personales, de conformidad
> a lo dispuesto en el artículo 28.
> b) Cuando la transferencia de datos quede amparada por
> cláusulas contractuales, normas corporativas vinculantes, u
> otros instrumentos jurídicos suscritos entre el responsable
> que efectúa la transferencia y el responsable o tercero
> mandatario que la reciba, y en ellas se establezcan
> garantías adecuadas, de conformidad a lo dispuesto en el
> artículo 28.
> c) Cuando el responsable que efectúa la transferencia
> y el responsable o tercero mandatario que la recibe, adopten
> un modelo de cumplimiento o mecanismo de certificación y en
> ellos se establezcan garantías adecuadas, de conformidad
> con el artículo 28.
> En ausencia de una decisión de adecuación o de
> garantías adecuadas, se podrá realizar una transferencia
> específica y que no sea habitual, si se cumple alguno de
> los siguientes supuestos:
> a) Cuando exista consentimiento expreso del titular de
> datos para realizar una transferencia internacional de datos
> específica y determinada.
> b) Cuando se refiera a transferencias bancarias,
> financieras o bursátiles específicas y que se realicen
> conforme a las leyes que regulan estas transferencias.
> c) Cuando se deban transferir datos para dar
> cumplimiento a obligaciones adquiridas en tratados o
> convenios internacionales que hayan sido ratificados por el
> Estado chileno y se encuentren vigentes.
> d) Cuando la transferencia resulte necesaria por
> aplicación de convenios de cooperación, intercambio de
> información o supervisión que hayan sido suscritos por
> órganos públicos para el cumplimiento de sus funciones y
> en el ejercicio de sus competencias.
> e) Cuando la transferencia de datos realizada por una
> persona natural o jurídica, pública o privada, haya sido
> autorizada expresamente por la ley y para una finalidad
> determinada.
> f) Cuando la transferencia sea efectuada con el objeto
> de prestar o solicitar colaboración judicial internacional.
> g) Cuando la transferencia sea necesaria para la
> celebración o ejecución de un contrato entre el titular y
> el responsable, o para la ejecución de medidas
> precontractuales adoptadas a solicitud del titular.
> h) Cuando sea necesario adoptar medidas urgentes en
> materia médica o sanitaria, para la prevención o
> diagnóstico de enfermedades, para tratamientos médicos o
> para la gestión de servicios sanitarios o de salud.

### Cross-references
- Art. 12 (consent).
- Art. 28 (adequacy determination and guarantees).
- Art. 29 (Agency supervision).

> **Source:** Ley 19.628 Art. 27 as substituted by Ley 21.719 Art. 1° item 13 (in force 2026-12-01).

---

## Article 28 — Rule for determining adequate countries and other rules applicable to international data transfer
**Spanish anchor:** Art. 28
**Tags:** adequacy, Agency-determination, model-clauses, binding-corporate-rules, intra-group-transfers, ad-hoc-authorisation, burden-of-proof

### Plain-English text

The legal order of a country is deemed to possess adequate levels of data protection where it complies with similar or higher standards than those established in this law. The Agency shall determine, in a reasoned manner, the countries that possess adequate levels of data protection, considering at least the following:

a) The establishment of principles governing the processing of personal data.

b) The existence of rules recognising and guaranteeing the rights of data subjects and the existence of a jurisdictional or administrative public authority for control or tutela.

c) The imposition of information and security obligations on data controllers and third-party mandataries.

d) The determination of responsibilities in the event of infringements.

Adequate guarantees shall be those instruments, mechanisms, or clauses that contain principles, rights, and guarantees similar to or greater than those offered by this law — and in particular, that grant enforceable rights and effective legal actions to data subjects. The Agency may approve model clauses and other legal instruments only if they contain such guarantees for cross-border data flows, which shall be made available to controllers. Model clauses and other legal instruments establishing adequate guarantees approved by the Agency shall not require any additional guarantee or authorisation.

The Agency shall make available to interested parties on its website a list of adequate countries and standard model contractual clauses and other legal instruments for the international transfer of data.

Where the transfer is carried out between companies or entities belonging to the same business group, related companies, or those subject to the same controller under the terms provided in the Securities Market Law (Ley de Mercado de Valores), provided that they all operate under the same standards and policies on personal-data processing, the transfers may be covered by binding corporate rules previously approved by the Agency. The controller carrying out the transfer of data shall assume responsibility for any infringement of the binding corporate standards and policies incurred by any of the members of the business group. The controller may exonerate itself from this responsibility only when it demonstrates that the infringement was not attributable to the corresponding member of the business group.

Where none of the circumstances indicated in the preceding article occur, the Agency may authorise — by reasoned decision (resolución fundada) — the international transfer of data for a particular case, provided that the transmitter and receiver of the data provide adequate guarantees regarding the protection of the rights of the persons who are data subjects of these data and the security of the transferred information, in accordance with this law.

It shall be for the data controller that effected the international transfer of data to demonstrate before the Agency that the transfer was carried out in accordance with the rules established in this law.

### Original Spanish

> Artículo 28.- Regla de determinación de países
> adecuados y demás normas aplicables a la transferencia
> internacional de datos. Se entiende que el ordenamiento
> jurídico de un país posee niveles adecuados de protección
> de datos, cuando cumple con estándares similares o
> superiores a los fijados en esta ley. La Agencia
> determinará fundadamente los países que poseen niveles
> adecuados de protección de datos considerando, a lo menos,
> los siguientes:
> a) El establecimiento de principios que rigen el
> tratamiento de los datos personales.
> b) La existencia de normas que reconozcan y garanticen
> los derechos de los titulares de datos y la existencia de
> una autoridad pública jurisdiccional o administrativa de
> control o tutela.
> c) La imposición de obligaciones de información y
> seguridad a los responsables del tratamiento de los datos y
> terceros mandatarios.
> d) La determinación de responsabilidades en caso de
> infracciones.
> Se considerarán garantías adecuadas aquellos
> instrumentos, mecanismos, cláusulas que contengan similares
> o mayores principios, derechos y garantías a aquellas que
> ofrece la presente ley, y en particular, que otorguen
> derechos exigibles y acciones legales efectivas a los
> titulares de los datos. La Agencia podrá aprobar cláusulas
> modelo y otros instrumentos jurídicos, sólo si contienen
> dichas garantías para el flujo transfronterizo de datos,
> las que estarán a disposición de los responsables. Las
> cláusulas modelo y otros instrumentos jurídicos que
> establezcan garantías adecuadas aprobados por la Agencia,
> no requerirán ninguna otra garantía adicional ni
> autorización.
> La Agencia pondrá en su página web a disposición de
> los interesados un listado de países adecuados y modelos
> tipo de cláusulas contractuales y otros instrumentos
> jurídicos para la transferencia internacional de datos.
> Cuando la transferencia se efectúe entre sociedades o
> entidades que pertenezcan a un mismo grupo empresarial,
> empresas relacionadas o sujetas a un mismo controlador en
> los términos previstos en la Ley de Mercado de Valores,
> siempre que todas ellas operen bajo los mismos estándares y
> políticas en materia de tratamiento de datos personales,
> las transferencias podrán quedar amparadas en normas
> corporativas vinculantes previamente aprobadas por la
> Agencia. El responsable que efectúe la transferencia de
> datos asumirá la responsabilidad por cualquier infracción
> a los estándares y políticas corporativas vinculantes en
> que incurra algunos de los miembros del grupo empresarial.
> El responsable sólo podrá exonerarse de esta
> responsabilidad cuando acredite que la infracción no fue
> imputable al miembro del grupo empresarial correspondiente.
> Cuando no se verifique ninguna de las circunstancias
> señaladas en el artículo anterior, la Agencia podrá
> autorizar, mediante resolución fundada, la transferencia
> internacional de datos para un caso particular, siempre que
> el transmisor y el receptor de los datos otorguen las
> garantías adecuadas en relación con la protección de los
> derechos de las personas que son titulares de estos datos y
> la seguridad de la información transferida, de conformidad
> con la presente ley.
> Corresponderá al responsable de datos que efectuó la
> transferencia internacional de datos, acreditar ante la
> Agencia que ésta se practicó de conformidad a las reglas
> establecidas en esta ley.

### Cross-references
- Art. 27 (general rule).
- Art. 29 (Agency supervision).
- Art. 30 et seq. (Agency powers).

> **Source:** Ley 19.628 Art. 28 as substituted by Ley 21.719 Art. 1° item 13 (in force 2026-12-01).

---

## Article 29 — Supervision
**Spanish anchor:** Art. 29
**Tags:** supervision, Agency, recommendations, precautionary-measures, suspension

### Plain-English text

The Agency shall supervise international data-transfer operations and may issue recommendations, adopt precautionary measures, and — in qualified cases — temporarily suspend the sending of data.

### Original Spanish

> Artículo 29.- Fiscalización. La Agencia fiscalizará
> las operaciones de transferencia internacional de datos,
> pudiendo formular recomendaciones, adoptar medidas
> conservativas y en casos calificados, suspender
> temporalmente el envío de los datos.

### Cross-references
- Art. 27, Art. 28 (international transfer framework).
- Art. 30 et seq. (Agency powers).

> **Source:** Ley 19.628 Art. 29 as substituted by Ley 21.719 Art. 1° item 13 (in force 2026-12-01).

---

---

<!-- source: corpus/19628-data-protection-consolidated/titulo-06-agencia.md -->
## FILE: corpus/19628-data-protection-consolidated/titulo-06-agencia.md

# Ley 19.628 — Título VI: Control Authority on Personal Data Protection (Autoridad de Control en materia de Protección de Datos Personales — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** In force from 2026-12-01.

> **Title note:** New Title VI inserted by Ley 21.719 Art. 1° item 14. Establishes the Personal Data Protection Agency (Agencia de Protección de Datos Personales) — the autonomous public-law corporation that supervises this law. Articles 30–32 bis cover the Agency's creation, functions and powers, Directive Council, eligibility, removal, remuneration, statutes, coordination with the Council for Transparency, personnel, and assets.
>
> Note on article numbering: the amendment uses the sequence Art. 30, 30 bis, 30 ter, 30 quáter, 30 quinquies, 30 sexies, 30 septies, 30 octies, 30 nonies, 31, 32, 32 bis.

---

## Article 30 — Creation of the Personal Data Protection Agency
**Spanish anchor:** Artículo 30

### Plain-English text

Personal Data Protection Agency. The Personal Data Protection Agency (Agencia de Protección de Datos Personales) is hereby created, as an autonomous public-law corporation, of a technical character, decentralized, with legal personality and its own assets (patrimonio propio), which shall relate to the President of the Republic through the Ministry of Economy, Development, and Tourism.

The Agency shall have as its purpose to ensure the effective protection of the rights that guarantee the private life of persons and their personal data, in conformity with what is established in this law, and to supervise (fiscalizar) compliance with its provisions.

The domicile of the Agency shall be fixed in the regulation, without prejudice to the domiciles it may establish at other points in the country.

### Original Spanish

> Artículo 30.- Agencia de Protección de Datos
> Personales. Créase la Agencia de Protección de Datos
> Personales, corporación autónoma de derecho público, de
> carácter técnico, descentralizado, con personalidad
> jurídica y patrimonio propio, que se relacionará con el
> Presidente de la República a través del Ministerio de
> Economía, Fomento y Turismo.
> La Agencia tendrá por objeto velar por la efectiva
> protección de los derechos que garantizan la vida privada
> de las personas y sus datos personales, de conformidad a lo
> establecido en la presente ley, y fiscalizar el cumplimiento
> de sus disposiciones.
> El domicilio de la Agencia será fijado en el
> reglamento, sin perjuicio de los domicilios que pueda
> establecer en otros puntos del país.

> **Source:** Ley 19.628 Artículo 30 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 30 bis — Functions and powers of the Agency
**Spanish anchor:** Artículo 30 bis

### Plain-English text

Functions and powers of the Agency. The Agency shall have the following functions and powers (atribuciones):

a) To issue instructions and general and binding rules with the purpose of regulating the operations of processing of personal data in accordance with the principles established in this law. The instructions and general rules issued by the Agency must be emitted following a prior public consultation conducted through the institutional website, and must be related strictly to the regulation of processing of personal data and necessary for the faithful compliance with this law, the necessary mechanisms being provided so that interested parties may formulate observations thereon.

b) To apply and interpret administratively the legal and regulatory provisions on the matter of protection of personal data and the instructions and general rules issued by the Agency.

c) To supervise (fiscalizar) compliance with the provisions of this law, its regulations, and the instructions and general rules issued in respect of the processing of personal data. To that end, it may require those who carry out processing of personal data to deliver any document, book, or background record and all information necessary for compliance with its supervisory function.

d) To determine the infringements and non-compliances incurred by those who carry out processing of personal data, in their data-processing operations, in respect of the principles and obligations established in this law, its regulations, and the instructions and general rules issued by the Agency. For such purposes, and in a reasoned manner, it may summon to declare, among others, the data subject (titular), the legal representatives, administrators, advisors, and employees of those who process personal data, as well as any person who has had participation or knowledge of any fact relevant to resolving a sanctioning proceeding. Likewise, it may take the respective declarations by other means that ensure their fidelity.

e) To exercise the sanctioning power over the natural persons or legal persons who process personal data in infringement of this law, its regulations, and the instructions and general rules issued by the Agency, applying the sanctions established in this law.

f) To resolve the applications and claims that data subjects formulate against those who process personal data in infringement of this law, its regulations, or the instructions and general rules issued by the Agency.

g) To develop programs, projects, and actions of dissemination, promotion, and information to the citizenry, in relation to respect for the protection of their personal data.

h) To propose to the President of the Republic and to the National Congress, as the case may be, the legal and regulatory rules to ensure persons the due protection of their personal data and to perfect the regulation on the processing and use of this information.

i) To render technical assistance, when so required, to the National Congress, the Judiciary, the Comptroller General of the Republic, the Public Prosecutor's Office, the Constitutional Court, the Central Bank, the Electoral Service, the Electoral Justice, and the other special tribunals created by law, in the issuance and execution of the policies and internal rules of these bodies, with the purpose that their operations and activities of processing of personal data are carried out in conformity with the principles and obligations established in this law.

j) To relate and collaborate with public bodies in the design and implementation of policies and actions aimed at safeguarding the protection of personal data and their correct processing.

k) To enter into agreements of cooperation and collaboration with public or private entities, national, foreign, or international, that have competence or are related to the field of personal data. In the cases of entering into agreements with international public entities, prior consultation with the Ministry of Foreign Affairs shall be required, in conformity with what is established in Article 35 of Law No. 21.080.

l) To participate in, receive cooperation from, and collaborate with international bodies on matters of protection of personal data.

m) To certify, register, and supervise infringement-prevention models and compliance programs, and to administer the National Registry of Sanctions and Compliance.

n) To exercise the other functions and powers entrusted to it by law.

When a body of the Administration is required for the exercise of the functions or powers that this law confers on the Agency, it must comply with what is set forth in the second paragraph of Article 14 of Law No. 19.880.

### Original Spanish

> Artículo 30 bis.- Funciones y atribuciones de la
> Agencia. La Agencia tendrá las siguientes funciones y
> atribuciones:
> a) Dictar instrucciones y normas generales y
> obligatorias con el objeto de regular las operaciones de
> tratamiento de datos personales conforme a los principios
> establecidos en esta ley. Las instrucciones y normas
> generales que dicte la Agencia deberán ser emitidas previa
> consulta pública efectuada a través de la página web
> institucional y deberán estar relacionadas estrictamente
> con la regulación de tratamiento de datos personales y que
> sea necesaria para el fiel cumplimiento de la presente ley,
> disponiéndose los mecanismos necesarios para que los
> interesados puedan formular observaciones a ésta.
> b) Aplicar e interpretar administrativamente las
> disposiciones legales y reglamentarias en materia de
> protección de los datos personales y las instrucciones y
> normas generales que dicte la Agencia.
> c) Fiscalizar el cumplimiento de las disposiciones de
> esta ley, sus reglamentos y las instrucciones y normas
> generales que se dicten respecto de los tratamientos de
> datos personales. Para ello, podrá requerir a quienes
> realicen tratamiento de datos personales la entrega de
> cualquier documento, libro o antecedente y toda la
> información que fuere necesaria para el cumplimiento de su
> función fiscalizadora.
> d) Determinar las infracciones e incumplimientos en que
> incurran quienes realicen tratamiento de datos personales,
> en sus operaciones de tratamiento de datos, respecto de los
> principios y obligaciones establecidos en esta ley, sus
> reglamentos y las instrucciones y normas generales que emita
> la Agencia. Para tales efectos, y de manera fundada, podrá
> citar a declarar, entre otros, al titular, a los
> representantes legales, administradores, asesores y
> dependientes de quien trate datos personales, así como a
> toda persona que haya tenido participación o conocimiento
> respecto de algún hecho que sea relevante para resolver un
> procedimiento sancionatorio. Asimismo, podrá tomar las
> declaraciones respectivas por otros medios que aseguren su
> fidelidad.
> e) Ejercer la potestad sancionadora sobre las personas
> naturales o jurídicas que traten datos personales con
> infracción a esta ley, sus reglamentos y a instrucciones y
> normas generales dictadas por la Agencia, aplicando las
> sanciones establecidas en la presente ley.
> f) Resolver las solicitudes y reclamos que formulen los
> titulares de datos en contra de quienes traten datos
> personales con infracción a esta ley, sus reglamentos o las
> instrucciones y normas generales dictadas por la Agencia.
> g) Desarrollar programas, proyectos y acciones de
> difusión, promoción e información a la ciudadanía, en
> relación al respeto a la protección de sus datos
> personales.
> h) Proponer al Presidente de la República y al
> Congreso Nacional, en su caso, las normas legales y
> reglamentarias para asegurar a las personas la debida
> protección de sus datos personales y perfeccionar la
> regulación sobre el tratamiento y uso de esta información.
> i) Prestar asistencia técnica, cuando le sea
> requerida, al Congreso Nacional, al Poder Judicial, a la
> Contraloría General de la República, al Ministerio
> Público, al Tribunal Constitucional, al Banco Central, al
> Servicio Electoral, a la Justicia Electoral y los demás
> tribunales especiales creados por ley, en la dictación y
> ejecución de las políticas y normas internas de estos
> organismos, con el objeto que sus operaciones y actividades
> de tratamiento de datos personales se realicen conforme a
> los principios y obligaciones establecidos en esta ley.
> j) Relacionarse y colaborar con los órganos públicos
> en el diseño e implementación de políticas y acciones
> destinadas a velar por la protección de los datos
> personales y su correcto tratamiento.
> k) Suscribir convenios de cooperación y colaboración
> con entidades públicas o privadas, nacionales, extranjeras
> o internacionales, que tengan competencia o estén
> relacionadas al ámbito de los datos personales. En los
> casos de suscribir convenios con entidades públicas
> internacionales se requerirá consultar previamente al
> Ministerio de Relaciones Exteriores, de conformidad a lo
> establecido en el artículo 35 de la ley N° 21.080.
> l) Participar, recibir cooperación y colaborar con
> organismos internacionales en materias de protección de
> datos personales.
> m) Certificar, registrar y supervisar los modelos de
> prevención de infracciones y los programas de cumplimiento
> y administrar el Registro Nacional de Sanciones y
> Cumplimiento.
> n) Ejercer las demás funciones y atribuciones que la
> ley le encomiende.
> Requerido un organismo de la Administración para el
> ejercicio de las funciones o atribuciones que esta ley le
> entrega a la Agencia, deberá dar cumplimiento a lo
> dispuesto en el inciso segundo del artículo 14 de la ley
> N° 19.880.

> **Source:** Ley 19.628 Artículo 30 bis as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 30 ter — Direction of the Agency
**Spanish anchor:** Artículo 30 ter

### Plain-English text

Direction of the Agency. Senior direction of the Agency shall correspond to the Governing Board of the Agency (Consejo Directivo), which shall have the following functions and powers (atribuciones):

a) To exercise the powers and fulfil the functions that the law entrusts to the Agency.

b) To establish internal operating rules of the Agency for the fulfilment of the functions entrusted by law.

c) To establish policies for the planning, organization, direction, supervision, coordination, and control of the operation of the Agency, as well as those for the administration, acquisition, and disposal of assets.

d) To issue rules of general character, circulars, circular letters (oficios circulares), and other resolutions as may be required.

e) To formulate to the President of the Republic or to the National Congress proposals for the reform of legal and regulatory rules.

f) To prepare, within the first four months of each year, an annual public account detailing the work carried out by the Agency in the immediately preceding year.

### Original Spanish

> Artículo 30 ter.- Dirección de la Agencia. La
> dirección superior de la Agencia le corresponderá al
> Consejo Directivo de la Agencia, el cual tendrá las
> siguientes funciones y atribuciones:
> a) Ejercer las atribuciones y cumplir las funciones que
> la ley le encomiende a la Agencia.
> b) Establecer normativa interna de funcionamiento de la
> Agencia para el cumplimiento de las funciones encomendadas
> por la ley.
> c) Establecer políticas de planificación,
> organización, dirección, supervisión, coordinación y
> control de funcionamiento de la Agencia, así como las de
> administración, adquisición y enajenación de bienes.
> d) Dictar normas de carácter general, circulares,
> oficios circulares y otras resoluciones que se requieran.
> e) Formular al Presidente de la República o al
> Congreso Nacional las propuestas de reforma a normas legales
> y reglamentarias.
> f) Elaborar, dentro del primer cuatrimestre de cada
> año, una cuenta pública anual en que se detalle el trabajo
> efectuado por la Agencia en el año inmediatamente anterior.

> **Source:** Ley 19.628 Artículo 30 ter as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 30 quáter — Members of the Agency's Directive Council
**Spanish anchor:** Artículo 30 quáter

### Plain-English text

Members of the Agency's Governing Board. The Governing Board of the Agency shall be composed of three Directors (consejeros), designated by the President of the Republic, with the agreement of the Senate, adopted by two-thirds of its members in office.

For purposes of their designation, the President of the Republic shall make the proposal of the corresponding list, and the Senate must rule on the proposal.

Candidates for Director must be persons of recognized professional or academic prestige in matters of personal data protection.

The Governing Board of the Agency shall designate its president and vice-president, from among its members, in conformity with what is established in the Agency's statutes. The offices of president and vice-president shall last three years or the time remaining to them as Directors in each case.

The Directors shall hold office for six years, may not be designated for a new term, and shall be renewed on an individual basis, every two years.

The office of Director of the Governing Board of the Agency requires exclusive dedication.

The Governing Board of the Agency shall adopt its decisions by the majority of its members and, in case of a tie, the president shall decide, or the vice-president in case of absence of the president. The minimum quorum to convene shall be two Directors. The regulation shall establish the other rules necessary for its operation.

The Governing Board of the Agency must hold ordinary sessions at least once a week, and extraordinary sessions when its president specially summons them, on his own initiative or upon written request of two Directors, in the form and conditions determined by its internal operating rules. The president shall not refuse to make the indicated summons, the respective session having to take place within the two business days following the indicated request.

### Original Spanish

> Artículo 30 quáter.- Miembros del Consejo Directivo
> de la Agencia. El Consejo Directivo de la Agencia estará
> integrado por tres consejeros, designados por el Presidente
> de la República, con acuerdo del Senado, adoptado por los
> dos tercios de sus miembros en ejercicio.
> Para efectos de su designación, el Presidente de la
> República hará la proposición de la nómina que
> corresponda y el Senado deberá pronunciarse respecto de la
> propuesta.
> Los candidatos a consejero deberán ser personas de
> reconocido prestigio profesional o académico en materias de
> protección de datos personales.
> El Consejo Directivo de la Agencia designará a su
> presidente y vicepresidente, de entre sus miembros, de
> conformidad con lo establecido en los estatutos de la
> Agencia. Los cargos de presidente y vicepresidente durarán
> tres años o el tiempo que les reste como consejeros en cada
> caso.
> Los consejeros durarán seis años en sus cargos, no
> podrán ser designados para un nuevo periodo y se renovarán
> de forma individual, cada dos años.
> El cargo de consejero del Consejo Directivo de la
> Agencia exige dedicación exclusiva.
> El Consejo Directivo de la Agencia adoptará sus
> decisiones por la mayoría de sus miembros y, en caso de
> empate, resolverá su presidente, o su vicepresidente en
> caso de ausencia del presidente. El quorum mínimo para
> sesionar será de dos consejeros. El reglamento establecerá
> las demás normas necesarias para su funcionamiento.
> El Consejo Directivo de la Agencia deberá celebrar
> sesiones ordinarias a lo menos una vez por semana, y
> sesiones extraordinarias cuando las cite especialmente su
> presidente por sí o a requerimiento escrito de dos
> consejeros, en la forma y condiciones que determine su
> normativa interna de funcionamiento. El presidente no podrá
> negarse a realizar la citación indicada, debiendo la
> respectiva sesión tener lugar dentro de los dos días
> hábiles siguientes al requerimiento señalado.

> **Source:** Ley 19.628 Artículo 30 quáter as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 30 quinquies — Disqualifications and incompatibilities
**Spanish anchor:** Artículo 30 quinquies

### Plain-English text

Disqualifications and incompatibilities. The office of Director is incompatible with the performance of any office or service, whether remunerated or not, that is rendered in the private sector. Likewise, it is incompatible with the status of member of the governing bodies of political parties, officials of the State Administration, and with any employment or service remunerated with fiscal or municipal funds, and with the functions, remunerated or not, of Director, board member, or worker of institutions, autonomous national or foreign bodies, State enterprises and, in general, of any public service created by law, as well as of enterprises, companies, or entities, public or private, in which the State, its enterprises, companies, or centralized or decentralized institutions hold a majority capital contribution or in equal proportion or, under the same conditions, representation or participation. Likewise, it is incompatible with any other remunerated or gratuitous service or employment in any branch of the State.

The office of Director is compatible with the performance of teaching positions in public or private institutions recognized by the State, up to a maximum of twelve hours per week.

The spouse or civil partner of any of the Directors and their relatives up to the second degree of consanguinity inclusive, shall not be a director nor have participation in the ownership of an enterprise whose corporate purpose or commercial line of business deals with the collection, processing, or communication of personal data.

Additionally, the following may not be designated as a Director:

a) The person who has been convicted of a crime carrying an afflictive penalty or perpetual disqualification from holding public offices or positions, for crimes of malfeasance, bribery and those committed in the exercise of the public function, tax crimes, and crimes against the public faith.

b) The person who has a dependency on illegal narcotic or psychotropic substances or drugs, unless they justify their consumption by medical treatment.

c) The person who has been sanctioned, within the last five years, for a serious or very serious infringement of the rules that regulate the processing of personal data and their protection.

d) Those who, within the last year, have been managers, data delegates, directors, or have had participation in the ownership of an enterprise whose corporate purpose or commercial line of business deals with the processing of personal data.

In all matters not expressly regulated in this Article, the rules of Paragraph 2 of Title III of Decree with Force of Law No. 1-19.653, of 2000, of the Ministry General Secretariat of the Presidency, which fixes the consolidated, coordinated, and systematized text of Law No. 18.575, Constitutional Organic Law on General Bases of the State Administration, shall govern.

> **TN:** "delegados de datos" in subparagraph d) is rendered literally as "data delegates"; the law uses this expression for in-house data-protection officers/representatives, but there is no standard lexicon term, so the literal form is preserved.

### Original Spanish

> Artículo 30 quinquies.- Inhabilidades e
> incompatibilidades. El cargo de consejero es incompatible
> con el desempeño de todo cargo o servicio, sea o no
> remunerado, que se preste en el sector privado. De igual
> forma, es incompatible con la calidad de integrante de los
> órganos de dirección de los partidos políticos,
> funcionarios de la Administración del Estado, y de todo
> empleo o servicio retribuido con fondos fiscales o
> municipales, y con las funciones, remuneradas o no, de
> consejero, director o trabajador de instituciones,
> organismos autónomos nacionales o extranjeros, empresas del
> Estado y, en general, de todo servicio público creado por
> ley, como asimismo, de empresas, sociedades o entidades
> públicas o privadas en que el Estado, sus empresas,
> sociedades o instituciones centralizadas o descentralizadas,
> tengan aportes de capital mayoritario o en igual proporción
> o, en las mismas condiciones, representación o
> participación. Asimismo, es incompatible con cualquier otro
> servicio o empleo remunerado o gratuito en cualquier poder
> del Estado.
> El cargo de consejero es compatible con el desempeño
> de cargos docentes en instituciones públicas o privadas
> reconocidas por el Estado, hasta un máximo de doce horas
> semanales.
> El cónyuge o conviviente civil de cualquiera de los
> consejeros y sus parientes hasta el segundo grado de
> consanguinidad inclusive, no podrán ser director ni tener
> participación en la propiedad de una empresa cuyo objeto o
> giro comercial verse sobre recolección, tratamiento o
> comunicación de datos personales.
> Adicionalmente, no podrá ser designado consejero:
> a) La persona que hubiere sido condenada por delito que
> merezca pena aflictiva o inhabilitación perpetua para
> desempeñar cargos u oficios públicos, por delitos de
> prevaricación, cohecho y aquéllos cometidos en el
> ejercicio de la función pública, delitos tributarios y los
> delitos contra la fe pública.
> b) La persona que tuviere dependencia de sustancias o
> drogas estupefacientes o sicotrópicas ilegales, a menos que
> justifique su consumo por tratamiento médico.
> c) La persona que haya sido sancionada, dentro de los
> últimos cinco años, por infracción grave o gravísima a
> las normas que regulan el tratamiento de los datos
> personales y su protección.
> d) Quienes, dentro del último año, hayan sido
> gerentes, delegados de datos, directores o hayan tenido
> participación en la propiedad de una empresa cuyo objeto o
> giro comercial verse sobre el tratamiento de datos
> personales.
> En todo lo no expresamente regulado en este artículo,
> regirán las normas del Párrafo 2° del Título III del
> decreto con fuerza de ley N° 1-19.653, de 2000, del
> Ministerio Secretaría General de la Presidencia, que fija
> el texto refundido, coordinado y sistematizado de la ley N°
> 18.575, Orgánica Constitucional de Bases Generales de la
> Administración del Estado.

> **Source:** Ley 19.628 Artículo 30 quinquies as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 30 sexies — Removal of council members and causes of cessation
**Spanish anchor:** Artículo 30 sexies

### Plain-English text

Removal of Directors and grounds for cessation. The Directors shall be removed by the Supreme Court, upon request of the President of the Republic or of the Chamber of Deputies by agreement adopted by simple majority, or upon petition of fifteen deputies, on grounds of incapacity, misconduct, or manifest negligence in the exercise of their functions. The Supreme Court shall hear the matter in plenary specially convened for this purpose, and in order to agree the removal it must obtain the affirmative vote of the majority of its members in office.

In addition to removal, the following shall be grounds for cessation in the office of Director:

a) Expiration of the term for which the Director was designated.

b) Resignation before the President of the Republic.

c) Standing for an office of popular election.

d) Supervening disqualification or incompatibility, a circumstance that shall be assessed by the majority of the Directors with the exclusion of the affected one.

In the event that one or more Directors cease for any cause, the designation of a new Director shall proceed, by means of a proposal of the President of the Republic, subject to the same procedure set forth in Article 30 quáter, for the remaining period.

If the Director who ceases in office under this Article holds the status of president or vice-president of the Governing Board of the Agency, the replacement shall be designated in the form provided in Article 30 quáter, for the time remaining to the one who produced the vacancy.

### Original Spanish

> Artículo 30 sexies.- Remoción de consejeros y
> causales de cesación. Los consejeros serán removidos por
> la Corte Suprema, a requerimiento del Presidente de la
> República o de la Cámara de Diputados mediante acuerdo
> adoptado por simple mayoría, o a petición de quince
> diputados, por incapacidad, mal comportamiento o negligencia
> manifiesta en el ejercicio de sus funciones. La Corte
> Suprema conocerá del asunto en pleno especialmente
> convocado al efecto y para acordar la remoción deberá
> reunir el voto conforme de la mayoría de sus miembros en
> ejercicio.
> Además de la remoción, serán causales de cesación
> en el cargo de consejero, las siguientes:
> a) Expiración del plazo por el que fue designado.
> b) Renuncia ante el Presidente de la República.
> c) Postulación a un cargo de elección popular.
> d) Inhabilidad o incompatibilidad sobreviniente,
> circunstancia que será calificada por la mayoría de los
> consejeros con exclusión del afectado.
> En caso de que uno o más consejeros cesare por
> cualquier causa, procederá la designación de un nuevo
> consejero, mediante una proposición del Presidente de la
> República, sujeto al mismo procedimiento dispuesto en el
> artículo 30 quáter, por el período que restare.
> Si el consejero que cesare en el cargo en virtud del
> presente artículo invistiere la condición de presidente o
> vicepresidente del Consejo Directivo de la Agencia, su
> reemplazante será designado en la forma prevista en el
> artículo 30 quáter, por el tiempo que faltare al que
> produjo la vacante.

> **Source:** Ley 19.628 Artículo 30 sexies as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 30 septies — Remuneration
**Spanish anchor:** Artículo 30 septies

### Plain-English text

Remuneration. The president of the Governing Board of the Agency shall receive a gross monthly remuneration equivalent to that of an Undersecretary of State, and it shall correspond to him to exercise the functions set forth in Article 30 nonies and in the other pertinent legal provisions.

The other Directors shall receive a remuneration equivalent to 85% of the remuneration corresponding to the president of the Governing Board of the Agency.

### Original Spanish

> Artículo 30 septies.- Remuneración. El presidente del
> Consejo Directivo de la Agencia percibirá una remuneración
> bruta mensualizada equivalente a la de un Subsecretario de
> Estado, y le corresponderá ejercer las funciones señaladas
> en el artículo 30 nonies y en las demás disposiciones
> legales pertinentes.
> Los demás consejeros percibirán una remuneración
> equivalente al 85% de la remuneración que corresponda al
> presidente del Consejo Directivo de la Agencia.

> **Source:** Ley 19.628 Artículo 30 septies as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 30 octies — Agency statutes
**Spanish anchor:** Artículo 30 octies

### Plain-English text

Agency statutes. The statutes of the Agency shall establish its operating rules. The statutes and their modifications shall be proposed by the Agency to the President of the Republic, and their approval shall be ordered by means of a supreme decree (decreto supremo) issued through the Ministry of Economy, Development, and Tourism.

### Original Spanish

> Artículo 30 octies.- Estatutos Agencia. Los estatutos
> de la Agencia establecerán sus normas de funcionamiento.
> Los estatutos y sus modificaciones serán propuestos por la
> Agencia al Presidente de la República y su aprobación se
> dispondrá mediante decreto supremo expedido a través del
> Ministerio de Economía, Fomento y Turismo.

> **Source:** Ley 19.628 Artículo 30 octies as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 30 nonies — Functions and powers of the president of the Directive Council
**Spanish anchor:** Artículo 30 nonies

### Plain-English text

Functions and powers of the president of the Governing Board of the Agency. The president of the Governing Board of the Agency shall be the head of service (jefe de servicio) of the Agency and shall have its judicial and extrajudicial representation. He shall be in charge of the organization and administration of the Agency, and it shall correspond to him to exercise the supervision and hierarchical control of the conduct of the Agency's personnel.

To the president of the Governing Board of the Agency, the following functions and powers shall especially correspond:

a) To exercise the role of head of service.

b) To execute and give compliance to the rules and resolutions adopted by the Governing Board of the Agency.

c) To convene and chair the sessions of the Governing Board of the Agency, as well as to establish the agenda of matters to be addressed at each session.

d) To represent the Agency legally, judicially, and extrajudicially.

e) To issue the internal regulations necessary for the proper operation of the Governing Board of the Agency, with the prior agreement of the Governing Board of the Agency, ensuring compliance with the rules applicable to the Agency.

f) To hire the personnel of the Agency and terminate their services, in conformity with the law.

g) To execute the acts and enter into the conventions necessary for the fulfilment of the purposes of the Governing Board of the Agency.

h) To delegate specific powers or faculties on officials of the Agency.

i) To conduct the relations of the Agency with public bodies and other organs of the State and with the persons or entities subject to its supervision, as well as with international personal-data regulatory entities.

j) To exercise the other functions delegated to him by the Governing Board of the Agency.

The vice-president of the Governing Board of the Agency shall assume the functions and powers of the president of the Governing Board of the Agency in case of his absence.

### Original Spanish

> Artículo 30 nonies.- Funciones y atribuciones del
> presidente del Consejo Directivo de la Agencia. El
> presidente del Consejo Directivo de la Agencia será el jefe
> de servicio de la Agencia y tendrá la representación
> judicial y extrajudicial de ésta. Tendrá a su cargo la
> organización y administración de la Agencia, y le
> corresponderá ejercer la vigilancia y control jerárquico
> de la actuación del personal de la Agencia.
> Al presidente del Consejo Directivo de la Agencia le
> corresponderán especialmente las siguientes funciones y
> atribuciones:
> a) Ejercer el rol de jefe de servicio.
> b) Ejecutar y dar cumplimiento a las normas y acuerdos
> adoptados por el Consejo Directivo de la Agencia.
> c) Citar y presidir las sesiones del Consejo Directivo
> de la Agencia, así como establecer la tabla de materias a
> ser tratadas en cada sesión.
> d) Representar legal, judicial y extrajudicialmente a
> la Agencia.
> e) Dictar los reglamentos internos necesarios para el
> buen funcionamiento del Consejo Directivo de la Agencia,
> previo acuerdo del Consejo Directivo de la Agencia, velando
> por el cumplimiento de las normas aplicables a la Agencia.
> f) Contratar al personal de la Agencia y poner término
> a sus servicios, de conformidad a la ley.
> g) Ejecutar los actos y celebrar las convenciones
> necesarias para el cumplimiento de los fines del Consejo
> Directivo de la Agencia.
> h) Delegar atribuciones o facultades específicas en
> funcionarios de la Agencia.
> i) Conducir las relaciones de la Agencia con los
> organismos públicos y demás órganos del Estado y con las
> personas o entidades sujetas a la fiscalización de ésta,
> como también con las entidades reguladoras internacionales
> de datos personales.
> j) Ejercer las demás funciones que le sean delegadas
> por el Consejo Directivo de la Agencia.
> El vicepresidente del Consejo Directivo de la Agencia
> asumirá las funciones y atribuciones del presidente del
> Consejo Directivo de la Agencia en caso de ausencia de
> éste.

> **Source:** Ley 19.628 Artículo 30 nonies as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 31 — Regulatory coordination with the Council for Transparency
**Spanish anchor:** Artículo 31

### Plain-English text

Regulatory coordination with the Council for Transparency. When the Agency must issue an instruction or rule of general and binding character that may have effects in the areas of competence of the Council for Transparency (Consejo para la Transparencia), in accordance with the functions and powers set forth in Law No. 20.285, it shall transmit to the Council all background records and shall request from it a report, for the purposes of avoiding or preventing potential conflicts of rules and ensuring coordination, cooperation, and collaboration between the two bodies.

The Council for Transparency must deliver the requested report within the period of thirty calendar days, counted from the date on which it received the request referred to in the preceding paragraph.

The Agency shall consider the content of the opinion of the Council for Transparency by expressing it in the reasoning of the instruction or rule it issues. Once the period has elapsed without the report having been received, the procedure shall continue in conformity with the second paragraph of Article 38 of Law No. 19.880.

In turn, when the Council for Transparency must issue a general instruction that has clear effects in the areas of competence of the Agency, in accordance with the functions and powers set forth in this law, the Council for Transparency shall transmit the background records and request a report from the Agency, which must deliver it within the period of thirty calendar days, counted from the date on which it received the request. The Council for Transparency shall consider the content of the opinion of the Agency by expressing it in the reasoning of the general instruction it issues for the purpose. Once the period has elapsed without the report having been received, the procedure shall continue in conformity with the second paragraph of Article 38 of Law No. 19.880.

### Original Spanish

> Artículo 31.- Coordinación regulatoria con el Consejo
> para la Transparencia. Cuando la Agencia deba dictar una
> instrucción o norma de carácter general y obligatoria que
> pueda tener efectos en los ámbitos de competencia del
> Consejo para la Transparencia, de acuerdo a las funciones y
> atribuciones señaladas en la ley N° 20.285, le remitirá
> todos los antecedentes y requerirá de éste un informe para
> efectos de evitar o precaver potenciales conflictos de
> normas y asegurar la coordinación, cooperación y
> colaboración entre ambos órganos.
> El Consejo para la Transparencia deberá evacuar el
> informe solicitado dentro del plazo de treinta días
> corridos, contado desde la fecha en que hubiere recibido el
> requerimiento a que se refiere el inciso precedente.
> La Agencia considerará el contenido de la opinión del
> Consejo para la Transparencia expresándolo en la
> motivación de la instrucción o norma que dicte.
> Transcurrido el plazo sin que se hubiere recibido el
> informe, se procederá conforme al inciso segundo del
> artículo 38 de la ley N° 19.880.
> A su vez, cuando el Consejo para la Transparencia deba
> dictar una instrucción general que tenga claros efectos en
> los ámbitos de competencia de la Agencia, de acuerdo a las
> funciones y atribuciones señaladas en esta ley, el Consejo
> para la Transparencia remitirá los antecedentes y
> requerirá informe a la Agencia, la cual deberá evacuarlo
> en el plazo de treinta días corridos, contado desde la
> fecha en que hubiere recibido el requerimiento. El Consejo
> para la Transparencia considerará el contenido de la
> opinión de la Agencia expresándolo en la motivación de la
> instrucción general que dicte al efecto. Transcurrido el
> plazo sin que se hubiere recibido el informe, se procederá
> conforme al inciso segundo del artículo 38 de la ley N°
> 19.880.

> **Source:** Ley 19.628 Artículo 31 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 32 — Agency personnel and supervision
**Spanish anchor:** Artículo 32

### Plain-English text

Personnel of the Agency and supervision. The persons who render services to the Agency shall be governed by the Labour Code (Código del Trabajo).

Notwithstanding the foregoing, the rules on probity established in Law No. 20.880, on probity in the public function and prevention of conflicts of interest, and in Title III of Decree with Force of Law No. 1-19.653, of 2000, of the Ministry General Secretariat of the Presidency, which fixes the consolidated, coordinated, and systematized text of Law No. 18.575, Constitutional Organic Law on General Bases of the State Administration, shall be applicable to this personnel, a clause so providing having to be set out in the respective contracts.

The persons who perform directive functions in the Agency shall be selected by means of a public competition (concurso público) conducted by the National Civil Service Directorate, on the basis of a shortlist (terna) formed by the Council of Senior Public Management for each case, in accordance with the rules governing the selection processes of the Senior Public Management under Law No. 19.882.

In the event that third parties exercise, against the Directors or the personnel of the Agency, judicial actions for formal acts or for acts or omissions produced in the exercise of their offices, the Agency must provide them with legal defence. This defence shall extend to all those actions that are initiated against them even after they have ceased in office.

The defence referred to in the preceding paragraph shall not be available in cases in which the formal acts, acts, or omissions in question have constituted a ground for cessation imputable to the conduct of the respective official.

The Agency must comply with the rules established in Decree Law No. 1.263, of 1975, on Financial Administration of the State.

Likewise, the Agency shall be subject to the supervision (fiscalización) of the Comptroller General of the Republic, in respect of its personnel and the examination and judgement of its accounts.

The resolutions of the Agency shall be exempt from the procedure of taking of reason (toma de razón) by the Comptroller General of the Republic.

### Original Spanish

> Artículo 32.- Personal de la Agencia y fiscalización.
> Las personas que presten servicios a la Agencia se regirán
> por el Código del Trabajo.
> Sin perjuicio de lo anterior, serán aplicables a este
> personal las normas de probidad establecidas en la ley N°
> 20.880, sobre probidad en la función pública y prevención
> de los conflictos de intereses y en el Título III del
> decreto con fuerza de ley N° 1-19.653, de 2000, del
> Ministerio Secretaría General de la Presidencia, que fija
> el texto refundido, coordinado y sistematizado de la ley N°
> 18.575, Orgánica Constitucional de Bases Generales de la
> Administración del Estado, debiendo dejarse constancia en
> los contratos respectivos de una cláusula que así lo
> disponga.
> Las personas que desempeñen funciones directivas en la
> Agencia serán seleccionadas mediante concurso público
> efectuado por la Dirección Nacional del Servicio Civil,
> sobre la base de una terna conformada por el Consejo de Alta
> Dirección Pública para cada caso, de acuerdo con las
> normas que regulan los procesos de selección de la Alta
> Dirección Pública según la ley N° 19.882.
> En caso de que terceros ejerzan, en contra de los
> consejeros o del personal de la Agencia, acciones judiciales
> por actos formales o por acciones u omisiones producidas en
> el ejercicio de sus cargos, la Agencia deberá
> proporcionarles defensa jurídica. Esta defensa se
> extenderá a todas aquellas acciones que se inicien en su
> contra incluso después de haber cesado en el cargo.
> No procederá la defensa a que se refiere el inciso
> anterior en los casos en que los actos formales, acciones u
> omisiones en cuestión hayan configurado una causal de
> cesación imputable a la conducta del respectivo
> funcionario.
> La Agencia deberá cumplir con las normas establecidas
> en el decreto ley N° 1.263, de 1975, sobre Administración
> Financiera del Estado.
> Asimismo, la Agencia estará sometida a la
> fiscalización de la Contraloría General de la República,
> en lo que concierne a su personal y al examen y juzgamiento
> de sus cuentas.
> Las resoluciones de la Agencia estarán exentas del
> trámite de toma de razón por la Contraloría General de la
> República.

> **Source:** Ley 19.628 Artículo 32 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 32 bis — Assets
**Spanish anchor:** Artículo 32 bis

### Plain-English text

On the assets. The assets (patrimonio) of the Agency shall be formed by:

a) The contribution annually contemplated in the Public Sector Budget Law.

b) The movable and immovable assets transferred to it or that it acquires by any title and the fruits derived from them.

c) The donations that the Agency accepts. The donations shall not require the procedure of judicial intimation referred to in Article 1401 of the Civil Code.

d) The inheritances and legacies that the Agency accepts, which it must always do with benefit of inventory. Such assignments shall be exempt from any kind of taxes and from any tax or charge affecting them.

e) The contributions from international cooperation.

### Original Spanish

> Artículo 32 bis.- Del patrimonio. El patrimonio de la
> Agencia estará formado por:
> a) El aporte que se contemple anualmente en la Ley de
> Presupuestos del Sector Público.
> b) Los bienes muebles e inmuebles que se le transfieran
> o que adquieran a cualquier título y por los frutos que de
> ellos se perciban.
> c) Las donaciones que la Agencia acepte. Las donaciones
> no requerirán del trámite de insinuación judicial a que
> se refiere el artículo 1401 del Código Civil.
> d) Las herencias y legados que la Agencia acepte, lo
> que deberá hacer siempre con beneficio de inventario.
> Dichas asignaciones estarán exentas de toda clase de
> impuestos y de todo gravamen o pago que les afecten.
> e) Los aportes de la cooperación internacional.
> Título VII
> De las infracciones y sus sanciones, de los
> procedimientos y de las responsabilidades

> **Source:** Ley 19.628 Artículo 32 bis as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

---

<!-- source: corpus/19628-data-protection-consolidated/titulo-07-sanciones.md -->
## FILE: corpus/19628-data-protection-consolidated/titulo-07-sanciones.md

# Ley 19.628 — Título VII: Infringements, Sanctions, Procedures, and Responsibilities (De las infracciones y sus sanciones, de los procedimientos y de las responsabilidades — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** In force from 2026-12-01.

> **Title note:** New Title VII inserted by Ley 21.719 Art. 1° item 14. Establishes the administrative sanctions regime, procedures, and responsibilities. Articles 33–53 cover: general liability regime (Art. 33); the three-tier classification of infringements (minor, serious, very serious — Arts. 34, 34 bis, 34 ter, 34 quáter); sanctions and fines (Art. 35); mitigating and aggravating circumstances (Art. 36); determination of fine amount (Art. 37); accessory sanctions (Art. 38); the National Registry of Sanctions and Compliance (Art. 39); prescription (Art. 40); administrative procedure for tutela of rights (Art. 41); administrative procedure for infringement of law (Art. 42); judicial claim procedure (Art. 43); responsibility of public-body heads and officers (Arts. 44, 45, 46); the substantive civil-liability rule (Art. 47); and the prevention-model framework (Arts. 48, 49, 50, 51, 52, 53).

---

## Article 33 — General liability regime
**Spanish anchor:** Artículo 33

### Plain-English text

Article 33.- General liability regime. The data controller (responsable de datos), whether a natural person (persona natural) or legal person (persona jurídica), of public or private law, that in its personal-data processing operations infringes the principles set out in Article 3° and the rights and obligations established in this law, shall be sanctioned in accordance with the rules of the present Title.

Paragraph One

On liability, infringements, and sanctions applicable to natural or private-law legal persons

### Original Spanish

> Artículo 33.- Régimen general de responsabilidad. El
> responsable de datos, sea una persona natural o jurídica,
> de derecho público o privado, que en sus operaciones de
> tratamiento de datos personales infrinja los principios
> señalados en el artículo 3° y los derechos y obligaciones
> establecidos en esta ley, será sancionado de conformidad
> con las normas del presente Título.
> Párrafo Primero
> De la responsabilidad, las infracciones y las sanciones
> aplicables a las personas naturales o jurídicas de derecho
> privado

> **Source:** Ley 19.628 Artículo 33 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 34 — Minor, serious, and very serious infringements
**Spanish anchor:** Artículo 34

### Plain-English text

Article 34.- Minor, serious, and very serious infringements. Infringements committed by data controllers against the principles set out in Article 3° and against the rights and obligations established in this law are classified, attending to their gravity, as minor (leves), serious (graves), and very serious (gravísimas).

The liabilities in which a natural or legal person incurs for the infringements established in this law are understood without prejudice to the other legal, civil, or criminal liabilities that may correspond.

### Original Spanish

> Artículo 34.- Infracciones leves, graves y
> gravísimas. Las infracciones cometidas por los responsables
> de datos a los principios señalados en el artículo 3° y a
> los derechos y obligaciones establecidos en esta ley se
> califican, atendida su gravedad, en leves, graves y
> gravísimas.
> Las responsabilidades en que incurra una persona
> natural o jurídica por las infracciones establecidas en
> esta ley, se entienden sin perjuicio de las demás
> responsabilidades legales, civiles o penales, que pudieran
> corresponderle.

> **Source:** Ley 19.628 Artículo 34 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 34 bis — Minor infringements
**Spanish anchor:** Artículo 34 bis

### Plain-English text

Article 34 bis.- Minor infringements. The following shall be considered minor infringements:

a) Failing to comply, in whole or in part, with the duty of information and transparency, established in Article 14 ter.

b) Lacking the individualization of the postal address, electronic mail, or equivalent electronic medium that allows communication with the data controller or its legal representative, kept up to date and operative, through which data subjects can direct their communications or exercise their rights.

c) Omitting to respond, responding incompletely, or responding outside the legal term, to the requests made by the data subject in accordance with this law.

d) Omitting to send to the Agency (APDP) the communications mandatorily provided for in this law or its regulations.

e) Failing to comply with the general instructions issued by the Agency in cases that are not sanctioned as a serious or very serious infringement.

f) Committing any other infringement of the rights and obligations established in this law that is not classified as a serious or very serious infringement.

### Original Spanish

> Artículo 34 bis.- Infracciones leves. Se consideran
> infracciones leves, las siguientes:
> a) Incumplir total o parcialmente el deber de
> información y transparencia, establecido en el artículo 14
> ter.
> b) Carecer de la individualización del domicilio
> postal, correo electrónico o medio electrónico equivalente
> que permita comunicarse con el responsable de datos o su
> representante legal, actualizado y operativo, a través del
> cual los titulares de datos puedan dirigir sus
> comunicaciones o ejercer sus derechos.
> c) Omitir la respuesta, responder en forma incompleta o
> fuera de plazo, las solicitudes formuladas por el titular de
> datos en conformidad a esta ley.
> d) Omitir el envío a la Agencia de las comunicaciones
> previstas obligatoriamente en esta ley o sus reglamentos.
> e) Incumplir las instrucciones generales impartidas por
> la Agencia en los casos que no esté sancionado como
> infracción grave o gravísima.
> f) Cometer cualquier otra infracción a los derechos y
> obligaciones establecidos en esta ley, que no sea calificada
> como una infracción grave o gravísima.

> **Source:** Ley 19.628 Artículo 34 bis as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 34 ter — Serious infringements
**Spanish anchor:** Artículo 34 ter

### Plain-English text

Article 34 ter.- Serious infringements. The following shall be considered serious infringements:

a) Processing personal data without the consent of the data subject or without an antecedent or legal basis that grants lawfulness to the processing, or processing them for a purpose distinct from that for which they were collected.

b) Communicating or assigning personal data, without the consent of the data subject, in cases where such consent is necessary, or communicating or assigning the data for a purpose distinct from the one authorized.

c) Carrying out processing of personal data that is unnecessary in relation to the purposes of the processing, in violation of the provision of subparagraph c) of Article 3°.

d) Processing inaccurate, incomplete, or out-of-date personal data in relation to the purposes of the processing, except where the updating of these data falls upon the data subject by virtue of the law or the contract.

e) Impeding or obstructing the legitimate exercise of the data subject's rights of access, rectification, erasure, opposition, or portability.

f) Omitting to respond, responding belatedly, or denying the petition without justified cause, in cases of well-founded requests for temporary blocking of the processing of a data subject's personal data.

g) Carrying out processing of personal data of children and adolescents in infringement of the rules provided in this law.

h) Carrying out processing of personal data without complying with the requirements established for private-law legal persons without profit purposes whose object is political, philosophical, religious, cultural, union, or trade-association, with respect to the data of their members.

i) Violating the duty of secrecy or confidentiality established in Article 14 bis.

j) Violating or infringing the security obligations on the processing of personal data established in Article 14 quinquies.

k) Omitting the communications or registries in cases of breach of the security measures established in Article 14 quinquies.

l) Adopting insufficient or unsuitable quality and security measures for the processing of personal data for historical, statistical, or scientific purposes, and for studies or research that pursue purposes of public interest.

m) Carrying out international data-transfer operations in contravention of the rules provided in this law.

n) Failing to comply with a resolution or specific and direct requirement issued by the Agency.

### Original Spanish

> Artículo 34 ter.- Infracciones graves. Se consideran
> infracciones graves, las siguientes:
> a) Tratar los datos personales sin contar con el
> consentimiento del titular de datos o sin un antecedente o
> fundamento legal que otorgue licitud al tratamiento, o
> tratarlos con una finalidad distinta de aquélla para la
> cual fueron recolectados.
> b) Comunicar o ceder datos personales, sin el
> consentimiento del titular, en los casos en que dicho
> consentimiento sea necesario, o comunicar o ceder los datos
> para un fin distinto del autorizado.
> c) Efectuar tratamiento de datos personales
> innecesarios en relación con los fines del tratamiento
> vulnerando lo dispuesto en el literal c) del artículo 3°.
> d) Tratar datos personales inexactos, incompletos o
> desactualizados en relación con los fines del tratamiento,
> salvo que la actualización de estos datos corresponda al
> titular en virtud de la ley o el contrato.
> e) Impedir u obstaculizar el ejercicio legítimo de los
> derechos de acceso, rectificación, supresión, oposición o
> portabilidad del titular.
> f) Omitir la respuesta, responder tardíamente o
> denegar la petición sin causa justificada, en los casos de
> solicitudes fundadas de bloqueo temporal del tratamiento de
> datos personales de un titular.
> g) Realizar tratamiento de datos personales de niños,
> niñas y adolescentes con infracción a las normas previstas
> en esta ley.
> h) Realizar tratamiento de datos personales sin cumplir
> los requisitos establecidos para las personas jurídicas de
> derecho privado sin fines de lucro y cuya finalidad sea
> política, filosófica, religiosa, cultural, sindical o
> gremial, respecto de los datos de sus asociados.
> i) Vulnerar el deber de secreto o confidencialidad
> establecido en el artículo 14 bis.
> j) Vulnerar o infringir las obligaciones de seguridad
> en el tratamiento de los datos personales establecidas en el
> artículo 14 quinquies.
> k) Omitir las comunicaciones o los registros en los
> casos de vulneración de las medidas de seguridad
> establecidas en el artículo 14 quinquies.
> l) Adoptar medidas de calidad y seguridad insuficientes
> o no idóneas para el tratamiento de datos personales con
> fines históricos, estadísticos o científicos y para
> estudios o investigaciones que atiendan fines de interés
> público.
> m) Realizar operaciones de transferencia internacional
> de datos en contravención a las normas previstas en esta
> ley.
> n) Incumplir una resolución o un requerimiento
> específico y directo que haya impartido la Agencia.

> **Source:** Ley 19.628 Artículo 34 ter as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 34 quáter — Very serious infringements
**Spanish anchor:** Artículo 34 quáter

### Plain-English text

Article 34 quáter.- Very serious infringements. The following shall be considered very serious infringements:

a) Carrying out processing of personal data in a fraudulent manner.

b) Maliciously destining personal data to a purpose distinct from that consented to by the data subject or provided for in the law that authorizes their processing.

c) Communicating or assigning, knowingly, information that is untrue, incomplete, inaccurate, or out of date about the data subject.

d) Violating the duty of secrecy or confidentiality with respect to sensitive personal data and personal data relating to the commission and sanction of criminal, civil, administrative, and disciplinary infringements.

e) Processing, communicating, or assigning, knowingly, sensitive personal data or personal data of children and adolescents, in contravention of the rules of this law.

f) Deliberately omitting the communication of breaches of security measures that may affect the confidentiality, availability, or integrity of personal data.

g) Carrying out mass processing of personal data contained in electronic registries of criminal, civil, administrative, and disciplinary infringements kept by public bodies, without having legal authorization to do so.

h) Carrying out, knowingly, international data-transfer operations in contravention of the rules provided in this law.

i) Failing to comply with a resolution of the Agency that resolves a data subject's claim on the exercise of their rights of access, rectification, erasure, opposition, portability, or temporary blocking.

j) Delivering, knowingly, false, incomplete, or manifestly erroneous information in the process of registration or certification of the infringement-prevention model.

k) Failing to comply with the obligation established in Article 15 ter, in cases where applicable.

### Original Spanish

> Artículo 34 quáter.- Infracciones gravísimas. Se
> consideran infracciones gravísimas, las siguientes:
> a) Efectuar tratamiento de datos personales en forma
> fraudulenta.
> b) Destinar maliciosamente los datos personales a una
> finalidad distinta de la consentida por el titular o
> prevista en la ley que autoriza su tratamiento.
> c) Comunicar o ceder, a sabiendas, información no
> veraz, incompleta, inexacta o desactualizada sobre el
> titular de datos.
> d) Vulnerar el deber de secreto o confidencialidad
> sobre los datos personales sensibles y datos personales
> relativos a la comisión y sanción de infracciones penales,
> civiles, administrativas y disciplinarias.
> e) Tratar, comunicar o ceder, a sabiendas, datos
> personales sensibles o datos personales de niños, niñas y
> adolescentes, en contravención a las normas de esta ley.
> f) Omitir en forma deliberada la comunicación de las
> vulneraciones a las medidas de seguridad que puedan afectar
> la confidencialidad, disponibilidad o integridad de los
> datos personales.
> g) Efectuar tratamiento masivo de datos personales
> contenidos en registros electrónicos de infracciones
> penales, civiles, administrativas y disciplinarias, que
> llevan los organismos públicos, sin contar con
> autorización legal para ello.
> h) Realizar, a sabiendas, operaciones de transferencia
> internacional de datos en contravención a las normas
> previstas en esta ley.
> i) Incumplir una resolución de la Agencia que resuelve
> la reclamación de un titular sobre el ejercicio de sus
> derechos de acceso, rectificación, supresión, oposición,
> portabilidad o bloqueo temporal.
> j) Entregar, a sabiendas, información falsa,
> incompleta o manifiestamente errónea en el proceso de
> registro o certificación del modelo de prevención de
> infracciones.
> k) Incumplir la obligación establecida en el artículo
> 15 ter, en los casos que corresponda.

> **Source:** Ley 19.628 Artículo 34 quáter as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 35 — Sanctions
**Spanish anchor:** Artículo 35

### Plain-English text

Article 35.- Sanctions. The sanctions for the infringements in which data controllers incur shall be the following:

a) Minor infringements shall be sanctioned with a written warning (amonestación escrita) or a fine of up to 5,000 monthly tax units (unidades tributarias mensuales — UTM).

b) Serious infringements shall be sanctioned with a fine of up to 10,000 monthly tax units.

c) Very serious infringements shall be sanctioned with a fine of up to 20,000 monthly tax units.

In each case, the Agency shall indicate the measures tending to remedy the causes that gave rise to the sanction, which must be adopted within a term not greater than sixty days; otherwise a 50% surcharge on the fine imposed shall be applied, without prejudice to the provisions of Article 49.

Where recurrence exists, in accordance with subparagraph a) of the second paragraph of Article 36, the Agency may apply a fine of up to three times the amount assigned to the infringement committed.

Where the infringer is an enterprise distinct from those defined as smaller enterprises in the second article of Law No. 20.416, that incurs in recurrence in a serious or very serious infringement in the terms of subparagraph a) of the second paragraph of Article 36, the fine may reach the more onerous of that indicated in the preceding paragraph or up to the amount corresponding to 2% or 4% of the annual income from sales and services and other activities of the trade in the last calendar year, according to whether the infringements are serious or very serious, respectively.

### Original Spanish

> Artículo 35.- Sanciones. Las sanciones a las
> infracciones en que incurran los responsables de datos
> serán las siguientes:
> a) Las infracciones leves serán sancionadas con
> amonestación escrita o multa de hasta 5.000 unidades
> tributarias mensuales.
> b) Las infracciones graves serán sancionadas con multa
> de hasta 10.000 unidades tributarias mensuales.
> c) Las infracciones gravísimas serán sancionadas con
> multa de hasta 20.000 unidades tributarias mensuales.
> En cada caso, la Agencia señalará las medidas
> tendientes a subsanar las causales que dieron motivo a la
> sanción, las que deberán ser adoptadas en un plazo no
> mayor a sesenta días, de lo contrario se impondrá un
> recargo de 50% a la multa cursada, sin perjuicio de lo
> establecido en el artículo 49.
> En caso de que exista reincidencia, de conformidad al
> literal a) del inciso segundo del artículo 36, la Agencia
> podrá aplicar una multa de hasta tres veces el monto
> asignado a la infracción cometida.
> En caso de que el infractor corresponda a una empresa
> distinta de aquéllas definidas como empresas de menor
> tamaño en el artículo segundo de la ley N° 20.416, que
> reincida en infracción de carácter grave o gravísima en
> los términos del literal a) del inciso segundo del
> artículo 36, la multa podrá alcanzar a la más gravosa
> entre la señalada en el inciso anterior o hasta el monto
> correspondiente al 2% o 4% de los ingresos anuales por
> ventas y servicios y otras actividades del giro en el
> último año calendario, según se trate de infracciones
> graves o gravísimas, respectivamente.

> **Source:** Ley 19.628 Artículo 35 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 36 — Mitigating and aggravating circumstances
**Spanish anchor:** Artículo 36

### Plain-English text

Article 36.- Mitigating and aggravating circumstances of liability. The following shall be considered mitigating circumstances:

1. The unilateral reparation actions taken by the controller and the reparatory agreements reached with the data subjects who were affected.

2. The cooperation that the infringer provides in the administrative investigation conducted by the Agency.

3. The absence of previous sanctions of the data controller.

4. Self-reporting (autodenuncia) before the Agency. Together with the self-report, the infringer must communicate the measures adopted for the cessation of the facts that gave rise to the infringement or the mitigation measures implemented, as appropriate.

5. Having diligently fulfilled its duties of direction and supervision for the protection of the personal data subject to processing, which shall be verified with the certificate issued in accordance with the provisions of Article 51.

The following shall be considered aggravating circumstances:

a) Recurrence (reincidencia). Recurrence exists when the controller has been sanctioned on two or more occasions, in the last thirty months, for infringement of this law. The resolutions imposing the respective sanctions must be final or enforceable.

b) The continuous character of the infringement.

c) Having put at risk the security of the rights and liberties of the data subjects in relation to their personal data.

### Original Spanish

> Artículo 36.- Circunstancias atenuantes y agravantes
> de responsabilidad. Se considerarán circunstancias
> atenuantes:
> 1. Las acciones unilaterales de reparación que realice
> el responsable y los acuerdos reparatorios convenidos con
> los titulares de datos que fueron afectados.
> 2. La colaboración que el infractor preste en la
> investigación administrativa practicada por la Agencia.
> 3. La ausencia de sanciones previas del responsable de
> datos.
> 4. La autodenuncia ante la Agencia. Junto con la
> autodenuncia, el infractor deberá comunicar las medidas
> adoptadas para el cese de los hechos que originaron la
> infracción o las medidas de mitigación implementadas,
> según corresponda.
> 5. El haber cumplido diligentemente sus deberes de
> dirección y supervisión para la protección de los datos
> personales sujetos a tratamiento, lo que se verificará con
> el certificado expedido de acuerdo a lo dispuesto en el
> artículo 51.
> Se considerarán circunstancias agravantes:
> a) La reincidencia. Existe reincidencia cuando el
> responsable ha sido sancionado en dos o más ocasiones, en
> los últimos treinta meses, por infracción a esta ley. Las
> resoluciones que aplican las sanciones respectivas deberán
> encontrarse firmes o ejecutoriadas.
> b) El carácter continuado de la infracción.
> c) El haber puesto en riesgo la seguridad de los
> derechos y libertades de los titulares en relación a sus
> datos personales.

> **Source:** Ley 19.628 Artículo 36 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 37 — Determination of fine amount
**Spanish anchor:** Artículo 37

### Plain-English text

Article 37.- Determination of the amount of fines. For the determination of the amount of the fines indicated in this law, the Agency must prudentially apply the following criteria:

1. The gravity of the conduct.

2. Whether the conduct was carried out with lack of diligence or care, in those cases in which these elements are not considered in the configuration of the infringement.

3. The harm produced by reason of the infringement, especially the number of data subjects who were affected.

4. The economic benefit obtained by reason of the infringement, if any.

5. Whether the processing carried out includes sensitive personal data or personal data of children and adolescents.

6. The economic capacity of the infringer.

7. The sanctions previously applied by the Agency in the same circumstances.

8. The mitigating and aggravating circumstances that concur.

Where one conduct gives rise to two or more infringements, or where one infringement is the means to commit another, a single fine shall be imposed, always considering the sanction of the most serious infringement. Where two or more infringing conducts are verified, independent of each other, the sanctions corresponding to each one of them shall be accumulated.

Fines must be paid at the General Treasury of the Republic (Tesorería General de la República), through the in-person or digital means that it provides, within the term of ten business days counted from the date on which the Agency's resolution becomes final. The corresponding proof of payment must be submitted to the Agency within the term of ten business days counted from the date on which the payment was made.

Where for the same facts and legal grounds, the infringer could be sanctioned in accordance with this law and with another or other laws, of the possible sanctions, that of greater gravity shall be imposed on him.

### Original Spanish

> Artículo 37.- Determinación del monto de las multas.
> Para la determinación del monto de las multas señaladas en
> esta ley, la Agencia deberá aplicar prudencialmente los
> siguientes criterios:
> 1. La gravedad de la conducta.
> 2. Si la conducta fue realizada con falta de diligencia
> o cuidado en aquellos casos que no se consideran estos
> elementos en la configuración de la infracción.
> 3. El perjuicio producido con motivo de la infracción,
> especialmente el número de titulares de datos que se vieron
> afectados.
> 4. El beneficio económico obtenido con motivo de la
> infracción, en caso de que lo hubiese.
> 5. Si el tratamiento realizado incluye datos personales
> sensibles o datos personales de niños, niñas y
> adolescentes.
> 6. La capacidad económica del infractor.
> 7. Las sanciones aplicadas con anterioridad por la
> Agencia en las mismas circunstancias.
> 8. Las circunstancias atenuantes y agravantes que
> concurran.
> En caso de que una conducta dé origen a dos o más
> infracciones, o cuando una infracción sea medio para
> cometer otra, se impondrá una sola multa, considerando
> siempre la sanción de la infracción más grave. En caso de
> que se verifiquen dos o más conductas infraccionales,
> independientes entre sí, se acumularán las sanciones
> correspondientes a cada una de ellas.
> Las multas deberán ser pagadas en la Tesorería
> General de la República, a través de los medios
> presenciales o digitales que ella disponga, dentro del plazo
> de diez días hábiles contado desde que la resolución de
> la Agencia se encuentre firme. El comprobante de pago
> correspondiente deberá ser presentado a la Agencia dentro
> del plazo de diez días hábiles contado desde que se
> hubiere efectuado el pago.
> Cuando por unos mismos hechos y fundamentos jurídicos,
> el infractor pudiese ser sancionado con arreglo a esta ley y
> a otra u otras leyes, de las sanciones posibles, se le
> impondrá la de mayor gravedad.

> **Source:** Ley 19.628 Artículo 37 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 38 — Accessory sanctions
**Spanish anchor:** Artículo 38

### Plain-English text

Article 38.- Accessory sanctions. Where fines are imposed for repeated very serious infringements (infracciones gravísimas reiteradas) within a period of twenty-four months, the Agency may order the suspension of the data-processing operations and activities carried out by the data controller, for a term of up to thirty days. This suspension shall not affect the storage of data by the controller.

The suspension that the Agency orders as an accessory sanction may be partial or total, and shall not be decreed where it would affect the rights of the data subjects.

During this period the controller must adopt the necessary measures with the purpose of adjusting its operations and activities to the requirements set out in the resolution that ordered the suspension.

If the controller does not comply with the provisions of the temporary-suspension resolution, this measure may be extended indefinitely, for successive periods of a maximum of thirty days, until the controller complies with what has been ordered.

Where the suspension affects an entity subject to supervision by a public body of a supervisory character, the Agency must previously bring the antecedents to the knowledge of the corresponding regulatory authority, for the effects of safeguarding the rights of the users of such entity.

### Original Spanish

> Artículo 38.- Sanciones accesorias. En caso que se
> impongan multas por infracciones gravísimas reiteradas, en
> un período de veinticuatro meses, la Agencia podrá
> disponer la suspensión de las operaciones y actividades de
> tratamiento de datos que realiza el responsable de datos,
> hasta por un término de treinta días. Esta suspensión no
> afectará el almacenamiento de datos por parte del
> responsable.
> La suspensión que disponga la Agencia como sanción
> accesoria podrá ser parcial o total, y no podrá decretarse
> cuando con ello se afecten los derechos de los titulares.
> Durante este período el responsable deberá adoptar
> las medidas necesarias con el objeto de adecuar sus
> operaciones y actividades a las exigencias dispuestas en la
> resolución que ordenó la suspensión.
> Si el responsable no da cumplimiento a lo dispuesto en
> la resolución de suspensión temporal, esta medida se
> podrá prorrogar indefinidamente, por períodos sucesivos de
> máximo treinta días, hasta que el responsable cumpla con
> lo ordenado.
> Cuando la suspensión afecte a una entidad sujeta a
> supervisión por parte de un organismo público de carácter
> fiscalizador, la Agencia deberá previamente poner los
> antecedentes en conocimiento de la autoridad regulatoria
> correspondiente, para los efectos de cautelar los derechos
> de los usuarios de dicha entidad.

> **Source:** Ley 19.628 Artículo 38 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 39 — National Registry of Sanctions and Compliance
**Spanish anchor:** Artículo 39

### Plain-English text

Article 39.- National Registry of Sanctions and Compliance. The National Registry of Sanctions and Compliance (Registro Nacional de Sanciones y Cumplimiento) is hereby created, administered by the Agency. The registry shall be public and free of access. It shall be consulted and kept in electronic form.

In it there must be recorded the data controllers that have been sanctioned for infringing the rights and obligations established in this law. A distinction must be made according to the gravity of the infringement.

Additionally, the conduct infringed, the mitigating and aggravating circumstances of liability, and the sanction imposed must be recorded. Likewise, the controllers that adopt certified infringement-prevention models, with current validity, must be recorded.

The entries in the registry shall be of public access for a period of five years, counted from the date on which the entry was made.

### Original Spanish

> Artículo 39.- Registro Nacional de Sanciones y
> Cumplimiento. Créase el Registro Nacional de Sanciones y
> Cumplimiento, administrado por la Agencia. El registro será
> público y su acceso gratuito. Se consultará y llevará en
> forma electrónica.
> En él se deberán consignar a los responsables de
> datos que hayan sido sancionados por infringir los derechos
> y obligaciones establecidos en esta ley. Deberá
> distinguirse según la gravedad de la infracción.
> Adicionalmente, se deberá consignar la conducta
> infraccionada, las circunstancias atenuantes y agravantes de
> responsabilidad y la sanción impuesta. También se deberán
> consignar los responsables que adopten modelos certificados
> de prevención de infracciones, con carácter vigente.
> Las anotaciones en el registro serán de acceso
> público por el período de cinco años, a contar de la
> fecha en que se practicó la anotación.

> **Source:** Ley 19.628 Artículo 39 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 40 — Prescription
**Spanish anchor:** Artículo 40

### Plain-English text

Article 40.- Prescription. The actions to pursue liability for the infringements provided in this law shall prescribe within the term of four years, counted from the occurrence of the fact that gave rise to the infringement.

In the case of continuous infringements, the term of prescription of the referred actions shall be counted from the day on which the infringement has ceased.

Prescription is interrupted by the notification of the commencement of the corresponding administrative procedure.

The sanctions imposed for an infringement of the present law shall prescribe within the term of three years, counted from the date on which the resolution imposing the sanction becomes enforceable.

Paragraph Two

On administrative procedures

### Original Spanish

> Artículo 40.- Prescripción. Las acciones para
> perseguir la responsabilidad por las infracciones previstas
> en esta ley prescriben en el plazo de cuatro años, contado
> desde la ocurrencia del hecho que originó la infracción.
> En caso de infracciones continuadas, el plazo de
> prescripción de las referidas acciones se contará desde el
> día en que la infracción haya cesado.
> Se interrumpe la prescripción con la notificación del
> inicio del procedimiento administrativo correspondiente.
> Las sanciones que se impongan por una infracción a la
> presente ley prescriben en el plazo de tres años, contado
> desde la fecha en que la resolución que impone la sanción
> quede ejecutoriada.
> Párrafo Segundo
> De los procedimientos administrativos

> **Source:** Ley 19.628 Artículo 40 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 41 — Administrative procedure for tutela of rights
**Spanish anchor:** Artículo 41

### Plain-English text

Article 41.- Administrative procedure for protection (tutela) of rights. The data subject may claim before the Agency where the controller has denied a request made in accordance with Article 11 of the present law, or has not given a response to such request within the legal term established in that article.

The claim presented shall be processed in accordance with the following rules:

a) It must be submitted in writing, in physical or electronic format, within the term of thirty business days counted from the receipt of the negative response from the data controller or from the expiration of the term that the controller had to respond to the requirement made by the data subject. The claim must indicate the contested decision in case of rejection or omission of response, and accompany all the antecedents on which it is founded, and indicate a postal address or an electronic-mail address or other equivalent electronic medium where the notifications shall be carried out.

b) Together with the filing of the claim, upon a well-founded petition of the data subject and only in justified cases, the Agency may suspend the processing of the personal data concerning the data subject which is the object of the claim, having previously heard the data controller.

c) Upon receiving the claim, the Agency, within the following ten business days, must determine whether it complies with the requirements established in letter a) to be admitted to processing. Where the claim is not admitted to processing, the Agency's resolution must be founded and shall be notified to the data subject. In any event, the claim shall be deemed admitted to processing if the Agency does not issue a pronouncement within the term indicated above.

d) Once the claim is admitted to processing, the Agency shall notify the data controller, who shall have a term of thirty consecutive days, extendable for the same term, to respond to the claim, accompanying all the antecedents that it deems pertinent. The notifications carried out on the controller shall be made at its postal address, electronic-mail address, or other equivalent electronic medium referred to in letter c) of Article 14 ter.

e) Once this term has expired, whether or not the data controller has replied, and only if there are substantial, pertinent, and disputed facts, the Agency may open an evidentiary term of ten business days, in which the parties may bring forward all the means of proof they deem appropriate.

f) The data controller may, in its response, acquiesce (allanarse) to the claim, in which case it must accompany the antecedents or testimonies that demonstrate this circumstance. Once the foregoing has been verified, the data subject shall be notified and shall have ten days to assert his rights. Once the term has been fulfilled, the Agency shall proceed to the filing of the antecedents, having previously applied the sanction or instruction to the data controller, where appropriate.

g) The Agency shall have broad powers to request antecedents or reports that contribute to its resolution. It may convene the parties to a hearing and urge them to reach an agreement. The opinions that the officials of the Agency may express at this hearing shall not disqualify them from continuing to hear the matter in case an agreement is not reached. Once the agreement has been reached, the antecedents shall be filed.

h) The resolution of the claim must be issued by the Agency and must be founded. The administrative procedure for protection of rights shall not exceed six months.

i) The Agency's resolution that does not admit a claim to processing, and the resolution that resolves the claim, may be judicially contested within the term of fifteen business days counted from its notification, through the procedure established in Article 43.

Claims and requests for suspension of processing made in the case of rejection of a request for temporary blocking must be resolved by the Agency within the maximum term of three business days, without the need to previously hear the parties.

### Original Spanish

> Artículo 41.- Procedimiento administrativo de tutela
> de derechos. El titular de datos podrá reclamar ante la
> Agencia cuando el responsable le haya denegado una solicitud
> realizada de conformidad al artículo 11 de la presente ley,
> o no hubiere dado respuesta a dicha solicitud dentro del
> plazo legal establecido en ese artículo.
> La reclamación presentada se tramitará conforme a las
> siguientes reglas:
> a) Deberá ser presentada por escrito, en formato
> físico o electrónico dentro del plazo de treinta días
> hábiles contado desde que reciba la respuesta negativa del
> responsable de datos o haya vencido el plazo que disponía
> el responsable para responder el requerimiento formulado por
> el titular. La reclamación deberá señalar la decisión
> impugnada en caso de rechazo u omisión de respuesta y
> acompañar todos los antecedentes en que aquélla se funda e
> indicar un domicilio postal o una dirección de correo
> electrónico u otro medio electrónico equivalente donde se
> practicarán las notificaciones.
> b) Junto con la interposición del reclamo, a petición
> fundada del titular y sólo en casos justificados, la
> Agencia podrá suspender el tratamiento de los datos
> personales que conciernen al titular y que son objeto de la
> reclamación, debiendo previamente oír al responsable de
> datos.
> c) Recibido el reclamo, la Agencia, dentro de los diez
> días hábiles siguientes, deberá determinar si éste
> cumple con los requisitos establecidos en la letra a) para
> ser acogido a tramitación. En caso de que no se acoja a
> trámite la reclamación, la resolución de la Agencia debe
> ser fundada y se notificará al titular. En todo caso, se
> entenderá acogido a tramitación el reclamo si la Agencia
> no se pronuncia en el término indicado precedentemente.
> d) Acogido el reclamo a tramitación, la Agencia
> notificará al responsable de datos, quien dispondrá de un
> plazo de treinta días corridos, prorrogables hasta por el
> mismo plazo, para responder la reclamación, acompañando
> todos los antecedentes que estime pertinentes. Las
> notificaciones que se practiquen al responsable se
> realizarán a su domicilio postal, dirección de correo
> electrónico u otro medio electrónico equivalente a que
> alude la letra c) del artículo 14 ter.
> e) Vencido este plazo, haya o no contestado el
> responsable de los datos y, sólo si existen hechos
> sustanciales, pertinentes y controvertidos, la Agencia
> podrá abrir un término probatorio de diez días hábiles
> en el cual las partes pueden hacer valer todos los medios de
> prueba que estimen convenientes.
> f) El responsable de datos en su respuesta podrá
> allanarse a la reclamación, en cuyo caso deberá acompañar
> los antecedentes o testimonios que acrediten esta
> circunstancia. Verificado lo anterior, será notificado el
> titular de datos quien tendrá diez días para hacer valer
> sus derechos. Cumplido el plazo, la Agencia procederá al
> archivo de los antecedentes, previa aplicación de la
> sanción o instrucción al responsable de datos, cuando
> corresponda.
> g) La Agencia tendrá amplias facultades para solicitar
> antecedentes o informes que contribuyan a su resolución.
> Podrá convocar a las partes a una audiencia e instarlas a
> alcanzar un acuerdo. Las opiniones que puedan expresar los
> funcionarios de la Agencia en esta audiencia, no los
> inhabilitará para seguir conociendo del asunto en caso de
> que no se alcance un acuerdo. Logrado el acuerdo se
> archivarán los antecedentes.
> h) La resolución del reclamo deberá dictarse por la
> Agencia y deberá ser fundada. El procedimiento
> administrativo de tutela de derechos no podrá superar los
> seis meses.
> i) La resolución de la Agencia que no acoge a
> tramitación un reclamo y la resolución que resuelve la
> reclamación, podrán ser impugnadas judicialmente dentro
> del plazo de quince días hábiles contado desde su
> notificación, a través del procedimiento establecido en el
> artículo 43.
> Las reclamaciones y las solicitudes de suspensión del
> tratamiento formuladas en caso de rechazo de una solicitud
> de bloqueo temporal, deberán ser resueltas por la Agencia
> en el plazo máximo de tres días hábiles, sin necesidad de
> oír previamente a las partes.

> **Source:** Ley 19.628 Artículo 41 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 42 — Administrative procedure for infringement of law
**Spanish anchor:** Artículo 42

### Plain-English text

Article 42.- Administrative procedure for infringement of law. The determination of the infringements that data controllers commit by failure to comply with or breach of the principles established in Article 3°, of the rights and obligations established in this law, and the application of the corresponding sanctions, shall be subject to the following special rules:

a) The sanctioning procedure shall be instructed by the Agency.

b) The Agency may initiate a sanctioning procedure, ex officio or upon petition of a party, as the result of a supervisory process or in consequence of a claim presented by a data subject, by virtue of the procedure established in Articles 23 and 41 of this law. In the latter case, the receipt of the claim must be certified. Together with the opening of the file, the Agency must designate an official responsible for the instruction of the procedure.

c) The Agency must submit a formulation of charges against the data controller in which it describes the facts that configure the infringement, the principles and obligations failed or breached by the controller, the legal rules infringed, and any other antecedent that serves to support the formulation.

d) The formulation of charges must be notified to the data controller at its postal address, electronic-mail address, or other equivalent electronic medium indicated in letter c) of Article 14 ter.

e) The data controller shall have a term of fifteen business days to submit its discharge. On that opportunity, the data controller may accompany all the antecedents that it deems pertinent to refute the imputed facts. Together with the discharge, the controller must set an electronic-mail address through which all subsequent communications and notifications shall be carried out.

f) Once the discharge is received or the term granted therefor has elapsed, the Agency may open an evidentiary term of ten days in case there exist substantial, pertinent, and disputed facts.

g) The Agency shall give place to the evidentiary measures or proceedings that the controller requests in its discharge, provided they are pertinent and necessary. In case of rejection, it must found its resolution.

h) The facts investigated and the responsibilities of the presumed infringers may be proven by any means of proof admissible in law, which shall be assessed according to the rules of sound criticism (sana crítica).

i) The Agency shall have broad powers to request antecedents or reports that contribute to its resolution.

j) The resolution that puts an end to the sanctioning procedure must be founded and resolve all the questions raised in the file, pronouncing on each one of the allegations and defences made by the data controller, and shall contain the declaration of having configured the failure or breach of the principles, rights, and obligations established in the law by the controller, or its absolution, as appropriate. Where the Agency considers that the infringement has been verified, in the same resolution it shall weigh the circumstances that aggravate or mitigate the infringer's liability, and shall impose the sanction, in accordance with the gravity of the infringement committed.

k) The resolution that establishes the failure or breach of the principles, rights, and obligations of this law and that applies the corresponding sanction must be founded. This resolution must indicate the administrative and judicial remedies that proceed against it in accordance with this law, the bodies before which they must be presented, and the terms for their interposition. The Agency's resolution that resolves the procedure for infringement of law shall be judicially contestable in accordance with the following article.

l) The administrative procedure for infringement of law shall not exceed six months. When more than six months have elapsed from the date of the certification indicated in letter b) of this article without the Agency having resolved the claim, the interested party may submit a claim of illegality (reclamo de ilegalidad) in the terms provided in the following article.

> **TN:** "Reclamo de ilegalidad" is a Chilean administrative-law remedy lodged before the Court of Appeals against unlawful administrative acts; it has no direct one-to-one English equivalent.

Paragraph Three

On the judicial-claim procedure

### Original Spanish

> Artículo 42.- Procedimiento administrativo por
> infracción de ley. La determinación de las infracciones
> que cometan los responsables de datos por incumplimiento o
> vulneración de los principios establecidos en el artículo
> 3°, de los derechos y obligaciones establecidos en esta ley
> y la aplicación de las sanciones correspondientes, se
> sujetará a las siguientes reglas especiales:
> a) El procedimiento sancionatorio será instruido por
> la Agencia.
> b) La Agencia podrá iniciar un procedimiento
> sancionatorio, de oficio o a petición de parte, como
> resultado de un proceso de fiscalización o a consecuencia
> de una reclamación presentada por un titular de datos, en
> virtud del procedimiento establecido en los artículos 23 y
> 41 de esta ley. En este último caso, se deberá certificar
> la recepción del reclamo. Junto con la apertura del
> expediente, la Agencia deberá designar un funcionario
> responsable de la instrucción del procedimiento.
> c) La Agencia deberá presentar una formulación de
> cargos en contra del responsable de datos en que describa
> los hechos que configuran la infracción, los principios y
> obligaciones incumplidos o vulnerados por el responsable,
> las normas legales infringidas y cualquier otro antecedente
> que sirva para sustentar la formulación.
> d) La formulación de cargos debe notificarse al
> responsable de datos a su domicilio postal, dirección de
> correo electrónico u otro medio electrónico equivalente
> señalado en la letra c) del artículo 14 ter.
> e) El responsable de datos tendrá un plazo de quince
> días hábiles para presentar sus descargos. En esa
> oportunidad, el responsable de datos puede acompañar todos
> los antecedentes que estime pertinentes para desacreditar
> los hechos imputados. Junto con los descargos, el
> responsable deberá fijar una dirección de correo
> electrónico a través de la cual se realizarán todas las
> demás comunicaciones y notificaciones.
> f) Recibidos los descargos o transcurrido el plazo
> otorgado para ello, la Agencia podrá abrir un término
> probatorio de diez días en el caso que existan hechos
> sustanciales, pertinentes y controvertidos.
> g) La Agencia dará lugar a las medidas o diligencias
> probatorias que solicite el responsable en sus descargos,
> siempre que sean pertinentes y necesarias. En caso de
> rechazo, deberá fundar su resolución.
> h) Los hechos investigados y las responsabilidades de
> los presuntos infractores pueden acreditarse mediante
> cualquier medio de prueba admisible en derecho, los que se
> apreciarán de acuerdo a las reglas de la sana crítica.
> i) La Agencia tendrá amplias facultades para solicitar
> antecedentes o informes que contribuyan a su resolución.
> j) La resolución que ponga fin al procedimiento
> sancionatorio debe ser fundada y resolver todas las
> cuestiones planteadas en el expediente, pronunciándose
> sobre cada una de las alegaciones y defensas formuladas por
> el responsable de datos y contendrá la declaración de
> haberse configurado el incumplimiento o vulneración de los
> principios, derechos y obligaciones establecidos en la ley
> por el responsable o su absolución, según corresponda. En
> caso que la Agencia considere que se ha verificado la
> infracción, en la misma resolución ponderará las
> circunstancias que agravan o atenúan la responsabilidad del
> infractor e impondrá la sanción, de acuerdo a la gravedad
> de la infracción cometida.
> k) La resolución que establezca el incumplimiento o
> vulneración a los principios, derechos y obligaciones de
> esta ley y aplique la sanción correspondiente deberá ser
> fundada. Esta resolución debe indicar los recursos
> administrativos y judiciales que procedan contra ella en
> conformidad a esta ley, los órganos ante los que deben
> presentarse y los plazos para su interposición. La
> resolución de la Agencia que resuelve el procedimiento por
> infracción de ley será reclamable judicialmente conforme
> al artículo siguiente.
> l) El procedimiento administrativo de infracción de
> ley no podrá superar los seis meses. Cuando hayan
> transcurrido más de seis meses desde la fecha de la
> certificación indicada en la letra b) de este artículo sin
> que la Agencia haya resuelto la reclamación, el interesado
> podrá presentar un reclamo de ilegalidad en los términos
> previstos en el siguiente artículo.
> Párrafo Tercero
> Del procedimiento de reclamación judicial

> **Source:** Ley 19.628 Artículo 42 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 43 — Judicial claim procedure
**Spanish anchor:** Artículo 43

### Plain-English text

Article 43.- Judicial-claim procedure. Interested natural or legal persons that consider that an administrative act that paralyzes the procedure, or a final or terminative resolution issued by the Agency, is unlawful, may file a claim of illegality (reclamo de ilegalidad) before the Court of Appeals of Santiago or that of the place where the claimant is domiciled, at the latter's election. The claim must be filed within the fifteen business days following the notification of the contested resolution, according to the following rules:

a) The claimant shall indicate in its written submission, with precision, the resolution that is the object of the claim, the legal rule or rules that are supposed to have been infringed, the form in which the infringement has been produced, and, where applicable, the reasons for which the act causes him grievance.

b) The Court may declare the claim inadmissible if the submission does not comply with the conditions indicated in letter a) above. Likewise, it may decree an order of no innovation (orden de no innovar) when the execution of the contested act would produce irreparable damage to the appellant.

c) Upon receiving the claim, the Court shall require a report from the Agency, granting it a term of ten days to that effect.

d) Once the transfer has been evacuated, or it is deemed evacuated in default (rebeldía), the Court may open an evidentiary term, if it deems it necessary, which shall be governed by the rules on incidents contemplated by the Code of Civil Procedure (Código de Procedimiento Civil).

e) Once the evidentiary term has expired, it shall be ordered that the records be brought for hearing (traer los autos en relación). The hearing of this case shall enjoy preference for its inclusion in the docket (tabla).

f) If the Court gives place to the claim, in its judgment it shall decide whether grievance existed and shall order, as appropriate, the rectification of the contested act and the issuance of the respective resolution, as appropriate.

g) In the case of claims against a resolution that resolves a sanctioning procedure, the Court may confirm or revoke the contested resolution, establish or dismiss the commission of the infringement, as appropriate, and maintain, render without effect, or modify the sanction imposed on the controller or its absolution, as the case may be.

h) In everything not regulated by the present article, the rules established in the Code of Judicial Organization (Código Orgánico de Tribunales) and in the Code of Civil Procedure shall govern, as appropriate.

Paragraph Four

On the liability of public bodies, of the authority or superior head of the body, and of its officers

### Original Spanish

> Artículo 43.- Procedimiento de reclamación judicial.
> Las personas naturales o jurídicas interesadas que estimen
> que un acto administrativo que paraliza el procedimiento, o
> una resolución final o de término emanado de la Agencia,
> sea ilegal, podrán deducir un reclamo de ilegalidad ante la
> Corte de Apelaciones de Santiago o la del lugar donde se
> encuentre domiciliado el reclamante, a elección de este
> último. El reclamo deberá interponerse dentro de los
> quince días hábiles siguientes a la notificación de la
> resolución impugnada, según las siguientes reglas:
> a) El reclamante señalará en su escrito, con
> precisión, la resolución objeto del reclamo, la o las
> normas legales que se suponen infringidas, la forma en que
> se ha producido la infracción, y cuando procediere, las
> razones por las cuales el acto le causa agravio.
> b) La Corte podrá declarar inadmisible la reclamación
> si el escrito no cumple con las condiciones señaladas en la
> letra a) anterior. Asimismo, podrá decretar orden de no
> innovar cuando la ejecución del acto impugnado le produzca
> un daño irreparable al recurrente.
> c) Recibida la reclamación, la Corte requerirá de
> informe de la Agencia, concediéndole un plazo de diez días
> al efecto.
> d) Evacuado el traslado o teniéndosele por evacuado en
> rebeldía, la Corte puede abrir un término de prueba, si
> así lo estima necesario, el que se regirá por las reglas
> de los incidentes que contempla el Código de Procedimiento
> Civil.
> e) Vencido el término de prueba, se ordenará traer
> los autos en relación. La vista de esta causa gozará de
> preferencia para su inclusión en la tabla.
> f) Si la Corte da lugar al reclamo, en su sentencia
> decidirá si existió agravio y ordenará, según sea
> procedente, la rectificación del acto impugnado y la
> dictación de la respectiva resolución, según corresponda.
> g) Tratándose de reclamaciones en contra de una
> resolución que resuelve un procedimiento sancionatorio, la
> Corte podrá confirmar o revocar la resolución impugnada,
> establecer o desechar la comisión de la infracción, según
> corresponda y, mantener, dejar sin efecto o modificar la
> sanción impuesta al responsable o su absolución, según
> sea el caso.
> h) En todo aquello no regulado por el presente
> artículo, regirán las normas establecidas en el Código
> Orgánico de Tribunales y en el Código de Procedimiento
> Civil, según corresponda.
> Párrafo Cuarto
> De la responsabilidad de los órganos públicos, de la
> autoridad o jefe superior del órgano y de sus funcionarios

> **Source:** Ley 19.628 Artículo 43 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 44 — Administrative liability of the head of public body
**Spanish anchor:** Artículo 44

### Plain-English text

Article 44.- Administrative liability of the superior head of the public body. The superior head of a public body must ensure that the respective body carries out its personal-data processing operations and activities in accordance with the principles, rights, and obligations established in Title IV of this law.

Likewise, public bodies must submit to the measures tending to remedy or prevent infringements indicated by the Agency, or to the compliance or infringement-prevention programs of Article 49.

The infringements of the principles established in Article 3°, and of the rights and obligations, in which public bodies may incur are typified in Articles 34 bis, 34 ter, and 34 quáter, and shall be sanctioned with a fine of twenty percent to fifty percent of the monthly remuneration of the superior head of the infringing public body. The amount of the fine shall be determined by considering the gravity of the infringement, the nature of the data processed, and the number of data subjects affected. In the determination of the sanction, the circumstances that mitigate the infringer's liability must also be considered.

If the public body persists in the infringement, the doubling of the originally imposed sanction shall be applied to the superior head of the public body, and suspension from the position for a period of five days.

In the case of sensitive personal data, the fine shall be fifty percent of the monthly remuneration of the superior head of the public body, and suspension from the position of up to thirty days shall proceed.

The infringements in which a public body incurs in the processing of personal data shall be determined by the Agency in accordance with the procedure established in Article 42.

Once the infringement has been configured, the administrative sanctions indicated in this article shall be applied by the Agency. Nevertheless, the General Comptrollership of the Republic (Contraloría General de la República), at the petition of the Agency, may, in accordance with the rules of its organic law, initiate the administrative procedures and propose the corresponding sanctions.

Against the resolutions of the Agency, the claim of illegality established in Article 43 may be filed.

The sanctions provided in this article must be published on the website of the Agency and of the respective body or service within the term of five business days counted from the date on which the respective resolution becomes final.

### Original Spanish

> Artículo 44.- Responsabilidad administrativa del jefe
> superior del órgano público. El jefe superior de un
> órgano público deberá velar por que el órgano respectivo
> realice sus operaciones y actividades de tratamiento de los
> datos personales con arreglo a los principios, derechos y
> obligaciones establecidos en el Título IV de esta ley.
> Asimismo, los órganos públicos deberán someterse a
> las medidas tendientes a subsanar o prevenir infracciones
> que indique la Agencia o a los programas de cumplimiento o
> de prevención de infracciones del artículo 49.
> Las infracciones a los principios establecidos en el
> artículo 3°, y a los derechos y obligaciones en que puedan
> incurrir los órganos públicos se tipifican en los
> artículos 34 bis, 34 ter y 34 quáter y serán sancionadas
> con multa de veinte por ciento a cincuenta por ciento de la
> remuneración mensual del jefe superior del órgano público
> infractor. La cuantía de la multa se determinará
> considerando la gravedad de la infracción, la naturaleza de
> los datos tratados y el número de titulares afectados. En
> la determinación de la sanción se deberán considerar
> también las circunstancias que atenúan la responsabilidad
> del infractor.
> Si el órgano público persiste en la infracción, se
> le aplicará al jefe superior del órgano público el duplo
> de la sanción originalmente impuesta y la suspensión en el
> cargo por un lapso de cinco días.
> Tratándose de datos personales sensibles, la multa
> será del cincuenta por ciento de la remuneración mensual
> del jefe superior del órgano público y procederá la
> suspensión en el cargo de hasta treinta días.
> Las infracciones en que incurra un órgano público en
> el tratamiento de los datos personales serán determinadas
> por la Agencia de acuerdo al procedimiento establecido en el
> artículo 42.
> Habiéndose configurado la infracción, las sanciones
> administrativas señaladas en este artículo serán
> aplicadas por la Agencia. Con todo, la Contraloría General
> de la República, a petición de la Agencia podrá, de
> acuerdo a las normas de su ley orgánica, incoar los
> procedimientos administrativos y proponer las sanciones que
> correspondan.
> En contra de las resoluciones de la Agencia se podrá
> deducir el reclamo de ilegalidad establecido en el artículo
> 43.
> Las sanciones previstas en este artículo deberán ser
> publicadas en el sitio web de la Agencia y del respectivo
> órgano o servicio dentro del plazo de cinco días hábiles
> contado desde que la respectiva resolución quede firme.

> **Source:** Ley 19.628 Artículo 44 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 45 — Liability of the infringing public officer
**Spanish anchor:** Artículo 45

### Plain-English text

Article 45.- Liability of the infringing officer. Without prejudice to the provisions of the preceding article, if in the corresponding administrative procedure it is determined that there are individual liabilities of one or more officers of the public body, the General Comptrollership of the Republic, at the petition of the Agency, shall initiate a summary investigation (investigación sumaria) to determine the liabilities of such officers, or shall do so within the administrative procedure already initiated, as appropriate. The sanctions on the infringing officers shall be determined in accordance with the provisions of the Administrative Statute (Estatuto Administrativo).

In the event that the corresponding administrative procedure determines that any of the officers involved is responsible for any of the very serious infringements indicated in Article 34 quáter of this law, this conduct shall be considered a serious contravention of administrative probity.

> **TN:** "Investigación sumaria" is a Chilean expedited administrative disciplinary inquiry under the Estatuto Administrativo; no direct one-to-one English equivalent.

### Original Spanish

> Artículo 45.- Responsabilidad del funcionario
> infractor. Sin perjuicio de lo dispuesto en el artículo
> anterior, si en el procedimiento administrativo
> correspondiente se determina que existen responsabilidades
> individuales de uno o más funcionarios del órgano
> público, la Contraloría General de la República, a
> petición de la Agencia, iniciará una investigación
> sumaria para determinar las responsabilidades de dichos
> funcionarios o lo hará en el procedimiento administrativo
> ya iniciado, en su caso. Las sanciones a los funcionarios
> infractores serán determinadas de conformidad a lo
> dispuesto en el Estatuto Administrativo.
> En caso de que el procedimiento administrativo
> correspondiente determine que cualquiera de los funcionarios
> involucrados es responsable de alguna de las infracciones
> gravísimas señaladas en el artículo 34 quáter de esta
> ley, esta conducta se considerará una contravención grave
> a la probidad administrativa.

> **Source:** Ley 19.628 Artículo 45 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 46 — Duty of officials of reserve and confidentiality
**Spanish anchor:** Artículo 46

### Plain-English text

Article 46.- Duty of officers of reserve and confidentiality. Officers of public bodies that process personal data, and especially when they refer to sensitive personal data or data relating to the commission and sanction of criminal, civil, administrative, and disciplinary infringements, must keep secret or confidentiality with respect to the information of which they take knowledge in the exercise of their positions, and refrain from using such information for a purpose distinct from that corresponding to the legal functions of the respective public body, or from using it for their own benefit or that of third parties.

For the effects of the provisions of the second paragraph of Article 125 of the Administrative Statute, it shall be deemed that the facts that configure infringements of this provision seriously breach the principle of administrative probity, without prejudice to the other sanctions and liabilities that may proceed.

When, in compliance with a legal obligation, a public body communicates or assigns to another public body data protected by rules of secrecy or confidentiality, the receiving public body and its officers must process them while maintaining the same obligation of secrecy or confidentiality.

Paragraph Five

On civil liability

### Original Spanish

> Artículo 46.- Deber de los funcionarios de reserva y
> confidencialidad. Los funcionarios de los órganos públicos
> que traten datos personales y especialmente, cuando se
> refieran a datos personales sensibles o datos relativos a la
> comisión y sanción de infracciones penales, civiles,
> administrativas y disciplinarias, deben guardar secreto o
> confidencialidad respecto de la información que tomen
> conocimiento en el ejercicio de sus cargos y abstenerse de
> usar dicha información con una finalidad distinta de la que
> corresponda a las funciones legales del órgano público
> respectivo o utilizarla en beneficio propio o de terceros.
> Para efectos de lo dispuesto en el inciso segundo del
> artículo 125 del Estatuto Administrativo, se estimará que
> los hechos que configuren infracciones a esta disposición
> vulneran gravemente el principio de probidad administrativa,
> sin perjuicio de las demás sanciones y responsabilidades
> que procedan.
> Cuando, en cumplimiento de una obligación legal, un
> órgano público comunica o cede a otro órgano público
> datos protegidos por normas de secreto o confidencialidad,
> el organismo público receptor y sus funcionarios deberán
> tratarlos manteniendo la misma obligación de secreto o
> confidencialidad.
> Párrafo Quinto
> De la responsabilidad civil

> **Source:** Ley 19.628 Artículo 46 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 47 — General rule (civil liability)
**Spanish anchor:** Artículo 47

### Plain-English text

Article 47.- General rule. The data controller must indemnify the patrimonial and extrapatrimonial damage that it causes to the data subject or subjects, when in its data-processing operations it infringes the principles established in Article 3°, the rights and obligations established in this law, and causes them harm. The foregoing does not preclude the exercise of the other rights that this law grants to the data subject or subjects.

The indemnification action indicated in the preceding paragraph may be filed once the resolution that resolved the claim filed before the Agency favourably becomes enforceable, or the judgment becomes final and enforceable, in case a claim of illegality has been filed, and shall be processed in accordance with the rules of the summary procedure (procedimiento sumario) established in Articles 680 and following of the Code of Civil Procedure.

The civil actions deriving from an infringement of the present law shall prescribe within the term of five years, counted from the date on which the administrative resolution or the judicial judgment, as the case may be, that imposes the respective fine, becomes enforceable.

### Original Spanish

> Artículo 47.- Norma general. El responsable de datos
> deberá indemnizar el daño patrimonial y extrapatrimonial
> que cause al o los titulares, cuando en sus operaciones de
> tratamiento de datos infrinja los principios establecidos en
> el artículo 3°, los derechos y obligaciones establecidos
> en esta ley y les cause perjuicio. Lo anterior no obsta al
> ejercicio de los demás derechos que concede esta ley al o
> los titulares de datos.
> La acción indemnizatoria señalada en el inciso
> anterior podrá interponerse una vez ejecutoriada la
> resolución que resolvió favorablemente el reclamo
> interpuesto ante la Agencia o la sentencia se encuentre
> firme y ejecutoriada, en caso de haber presentado un reclamo
> de ilegalidad, y se tramitará de conformidad a las normas
> del procedimiento sumario establecidas en los artículos 680
> y siguientes del Código de Procedimiento Civil.
> Las acciones civiles que deriven de una infracción a
> la presente ley prescribirán en el plazo de cinco años,
> contado desde que se encuentre ejecutoriada la resolución
> administrativa o la sentencia judicial, según sea el caso,
> que imponga la multa respectiva.

> **Source:** Ley 19.628 Artículo 47 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 48 — Prevention of infringements
**Spanish anchor:** Artículo 48

### Plain-English text

Article 48.- Prevention of infringements. Data controllers, whether natural or legal persons, public or private, must adopt actions destined to prevent the commission of the infringements established in Articles 34 bis, 34 ter, and 34 quáter.

### Original Spanish

> Artículo 48.- Prevención de infracciones. Los
> responsables de datos, sean personas naturales o jurídicas,
> públicas o privadas, deberán adoptar acciones destinadas a
> prevenir la comisión de las infracciones establecidas en
> los artículos 34 bis, 34 ter y 34 quáter.

> **Source:** Ley 19.628 Artículo 48 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 49 — Infringement prevention model
**Spanish anchor:** Artículo 49

### Plain-English text

Article 49.- Infringement-prevention model. Data controllers may voluntarily adopt an infringement-prevention model (modelo de prevención de infracciones) consisting of a compliance program.

The compliance program must contain, at minimum, the following elements:

a) The designation of a personal-data protection delegate (delegado de protección de datos personales).

b) The definition of the means and powers of the data-protection delegate.

c) The identification of the type of information that the entity processes, the territorial scope in which it operates, the category, class, or types of data or databases that it administers, and the characterization of the data subjects.

d) The identification of the activities or processes of the entity, whether habitual or sporadic, in whose context the risk of commission of the infringements indicated in Articles 34 bis, 34 ter, and 34 quáter is generated or increased.

e) The establishment of specific protocols, rules, and procedures that allow the persons who intervene in the activities or processes indicated in the preceding letter to program and execute their tasks or labours in a manner that prevents the commission of the said infringements.

f) The mechanisms for internal reporting on compliance with the provisions of the present law, and the mechanisms for reporting to the data-protection authority for the case of Article 14 sexies.

g) The existence of internal administrative sanctions, as well as procedures for complaint or sanction of liabilities of the persons who fail to comply with the infringement-prevention system.

The internal regulation to which the implementation of the program may give rise must, where applicable, be expressly incorporated as an obligation in the employment or service-provision contracts of all the workers, employees, and service providers of the entities that act as data controllers or the third parties that carry out the processing, including their senior executives; or alternatively, as an obligation of the internal regulations dealt with in Articles 153 and following of the Labour Code (Código del Trabajo). In this latter case, the publicity measures established in Article 156 of the same Code must be carried out.

### Original Spanish

> Artículo 49.- Modelo de prevención de infracciones.
> Los responsables de datos podrán voluntariamente adoptar un
> modelo de prevención de infracciones consistente en un
> programa de cumplimiento.
> El programa de cumplimiento deberá contener, al menos,
> los siguientes elementos:
> a) La designación de un delegado de protección de
> datos personales.
> b) La definición de medios y facultades del delegado
> de protección de datos.
> c) La identificación del tipo de información que la
> entidad trata, el ámbito territorial en que opera, la
> categoría, clase o tipos de datos o bases de datos que
> administra, y la caracterización de los titulares de datos.
> d) La identificación de las actividades o procesos de
> la entidad, sean habituales o esporádicos, en cuyo contexto
> se genere o incremente el riesgo de comisión de las
> infracciones señaladas en los artículos 34 bis, 34 ter y
> 34 quáter.
> e) El establecimiento de protocolos, reglas y
> procedimientos específicos que permitan a las personas que
> intervengan en las actividades o procesos indicados en la
> letra anterior, programar y ejecutar sus tareas o labores de
> una manera que prevenga la comisión de las referidas
> infracciones.
> f) Los mecanismos de reporte interno sobre el
> cumplimiento de lo dispuesto en la presente ley y los
> mecanismos de reporte a la autoridad de protección de datos
> para el caso del artículo 14 sexies.
> g) La existencia de sanciones administrativas internas,
> así como de procedimientos de denuncia o castigo de
> responsabilidades de las personas que incumplan el sistema
> de prevención de infracciones.
> La regulación interna a que dé lugar la
> implementación del programa, en su caso, deberá ser
> incorporada expresamente como una obligación en los
> contratos de trabajo o de prestación de servicios de todos
> los trabajadores, empleados y prestadores de servicios de
> las entidades que actúen como responsables de datos o los
> terceros que efectúen el tratamiento, incluidos los
> máximos ejecutivos de ellas, o bien, como una obligación
> del reglamento interno del que tratan los artículos 153 y
> siguientes del Código del Trabajo. En este último caso, se
> deben realizar las medidas de publicidad establecidas en el
> artículo 156 del mismo Código.

> **Source:** Ley 19.628 Artículo 49 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 50 — Powers of the delegate
**Spanish anchor:** Artículo 50

### Plain-English text

Article 50.- Powers of the delegate. The data controller may designate a personal-data protection delegate (delegado de protección de datos personales).

The data-protection delegate must be designated by the highest managerial or administrative authority of the data controller. The board of directors, an administering partner, or the highest authority of the enterprise or service, as appropriate, shall be considered the highest managerial or administrative authority.

The data-protection delegate must have autonomy with respect to the administration, in matters related to this law. In micro, small, and medium-sized enterprises, the owner or its highest authorities may personally assume the tasks of data-protection delegate.

The data-protection delegate may perform other functions and assignments, taking care to maintain independence in his function. The controller shall guarantee that such functions and assignments do not give rise to a conflict of interests.

The companies or entities that belong to a same business group, related enterprises, or those subject to a same controller in the terms provided in the Securities-Market Law (Ley de Mercado de Valores), may designate a single data-protection delegate, provided all of them operate under the same standards and policies on personal-data processing, and the delegate is accessible to all the entities and establishments.

The designation of the data-protection delegate must fall on a person who meets the requirements of suitability, capacity, and specific knowledge for the exercise of his functions.

Data subjects may contact the data-protection delegate with respect to all questions relating to the processing of their personal data and the exercise of their rights under this law.

The data-protection delegate shall be obliged to maintain strict secrecy or confidentiality of the personal data that he comes to know in the exercise of his position. Public officers who perform these functions and infringe this duty of secrecy or confidentiality shall be sanctioned in accordance with what is prescribed in Articles 246 to 247 bis of the Criminal Code (Código Penal). The controller shall be liable for the infringements of the duty of secrecy or confidentiality that should have been complied with by its prevention officer or protection delegate, without prejudice to the actions of recovery (acciones de repetición) that it may exercise against him.

The data controller must ensure that the delegate has the means and powers sufficient for the performance of his functions, and must grant him the material resources necessary to adequately carry out his labours, in consideration of the size and economic capacity of the entity.

Without prejudice to the other functions that may be assigned to him, the data-protection delegate shall have the following functions:

a) To inform and advise the data controller, the third parties charged with processing or mandataries, and the dependents of the controller, with respect to the legal and regulatory provisions relating to the right to the protection of personal data and the regulation of their processing.

b) To promote and participate in the policy that the data controller issues with respect to the protection and processing of personal data.

c) To supervise compliance with the present law and with the policy that the controller issues, within the scope of his competence.

d) To take care of the permanent training of the persons who participate in the data-processing operations.

e) To assist the members of the organization in the identification of the risks associated with the processing activity and the measures to adopt to safeguard the rights of personal-data subjects.

f) To develop an annual work plan and to render account of its results.

g) To resolve the consultations and requests of data subjects.

h) To cooperate and act as point of contact of the Agency.

### Original Spanish

> Artículo 50.- Atribuciones del delegado. El
> responsable de datos podrá designar un delegado de
> protección de datos personales.
> El delegado de protección de datos deberá ser
> designado por la máxima autoridad directiva o
> administrativa del responsable de datos. Se considerará
> como la máxima autoridad directiva o administrativa al
> directorio, un socio administrador o a la máxima autoridad
> de la empresa o servicio, según corresponda.
> El delegado de protección de datos deberá contar con
> autonomía respecto de la administración, en las materias
> relacionadas con esta ley. En las micro, pequeñas y
> medianas empresas, el dueño o sus máximas autoridades
> podrán asumir personalmente las tareas de delegado de
> protección de datos.
> El delegado de protección de datos podrá desempeñar
> otras funciones y cometidos, procurando mantener la
> independencia en su función. El responsable garantizará
> que dichas funciones y cometidos no den lugar a conflicto de
> intereses.
> Las sociedades o entidades que pertenezcan a un mismo
> grupo empresarial, empresas relacionadas o sujetas a un
> mismo controlador en los términos previstos en la Ley de
> Mercado de Valores, podrán designar un único delegado de
> protección de datos, siempre que todas ellas operen bajo
> los mismos estándares y políticas en materia de
> tratamiento de datos personales, y el delegado sea accesible
> para todas las entidades y establecimientos.
> La designación del delegado de protección de datos
> debe recaer en una persona que reúna los requisitos de
> idoneidad, capacidad y conocimientos específicos para el
> ejercicio de sus funciones.
> Los titulares de datos podrán ponerse en contacto con
> el delegado de protección de datos en lo que respecta a
> todas las cuestiones relativas al tratamiento de sus datos
> personales y al ejercicio de sus derechos al amparo de esta
> ley.
> El delegado de protección de datos estará obligado a
> mantener estricto secreto o confidencialidad de los datos
> personales que conociere en ejercicio de su cargo. Los
> funcionarios públicos que desempeñen estas funciones e
> infrinjan este deber de secreto o confidencialidad, serán
> sancionados de conformidad a lo que se prescribe en los
> artículos 246 a 247 bis del Código Penal. El responsable
> se hará cargo por las infracciones al deber de secreto o
> confidencialidad que debía cumplir su encargado de
> prevención o delegado de protección, sin perjuicio de las
> acciones de repetición que pueda ejercer contra éste.
> El responsable de datos deberá disponer que el
> delegado cuente con los medios y facultades suficientes para
> el desempeño de sus funciones, debiendo otorgarle los
> recursos materiales necesarios para realizar adecuadamente
> sus labores, en consideración al tamaño y capacidad
> económica de la entidad.
> Sin perjuicio de las demás funciones que se le puedan
> asignar, el delegado de protección de datos tendrá las
> siguientes funciones:
> a) Informar y asesorar al responsable de datos, a los
> terceros encargados o mandatarios y a los dependientes del
> responsable, respecto de las disposiciones legales y
> reglamentarias relativas al derecho a la protección de los
> datos personales y a la regulación de su tratamiento.
> b) Promover y participar en la política que dicte el
> responsable de datos respecto de la protección y el
> tratamiento de los datos personales.
> c) Supervisar el cumplimiento de la presente ley y de
> la política que dicte el responsable, dentro del ámbito de
> su competencia.
> d) Preocuparse de la formación permanente de las
> personas que participan en las operaciones de tratamiento de
> datos.
> e) Asistir a los miembros de la organización en la
> identificación de los riesgos asociados a la actividad de
> tratamiento y las medidas a adoptar para resguardar los
> derechos de los titulares de datos personales.
> f) Desarrollar un plan anual de trabajo y rendir cuenta
> de sus resultados.
> g) Absolver las consultas y solicitudes de los
> titulares de datos.
> h) Cooperar y actuar como punto de contacto de la
> Agencia.

> **Source:** Ley 19.628 Artículo 50 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 51 — Certification, registration, supervision of the prevention model and regulation
**Spanish anchor:** Artículo 51

### Plain-English text

Article 51.- Certification, registration, supervision of the infringement-prevention model, and regulation. The Agency shall be the entity charged with certifying that the infringement-prevention model meets the requirements and elements established in the law and its regulation, and with supervising them.

The Agency shall incorporate in the National Registry of Sanctions and Compliance the entities that hold a certification in force.

A regulation issued through the Ministry of Finance and signed by the Minister Secretary-General of the Presidency and by the Minister of Economy, Promotion, and Tourism shall establish the requirements, modalities, and procedures for the implementation, certification, registration, and supervision of the infringement-prevention models.

### Original Spanish

> Artículo 51.- Certificación, registro, supervisión
> del modelo de prevención de infracciones y reglamento. La
> Agencia será la entidad encargada de certificar que el
> modelo de prevención de infracciones reúna los requisitos
> y elementos establecidos en la ley y su reglamento y
> supervisarlos.
> La Agencia incorporará en el Registro Nacional de
> Sanciones y Cumplimiento a las entidades que posean una
> certificación vigente.
> Un reglamento expedido a través del Ministerio de
> Hacienda y suscrito por el Ministro Secretario General de la
> Presidencia y por el Ministro de Economía, Fomento y
> Turismo establecerá los requisitos, modalidades y
> procedimientos para la implementación, certificación,
> registro y supervisión de los modelos de prevención de
> infracciones.

> **Source:** Ley 19.628 Artículo 51 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 52 — Validity of certificates
**Spanish anchor:** Artículo 52

### Plain-English text

Article 52.- Validity of certificates. The certificates issued by the Agency shall have a validity of three years. Without prejudice to the foregoing, they shall be rendered without effect in the following cases:

a) By revocation effected by the Agency.

b) By death of the data controller in the case of natural persons.

c) By dissolution of the legal person.

d) By enforceable judicial resolution.

e) By voluntary cessation of the activity of the data controller.

The termination of the validity of a certificate by any of the causes indicated above shall not be opposable to third parties so long as it has not been eliminated from the registry.

### Original Spanish

> Artículo 52.- Vigencia de los certificados. Los
> certificados expedidos por la Agencia tendrán una vigencia
> de tres años. Sin perjuicio de lo anterior, quedarán sin
> efecto en los siguientes casos:
> a) Por revocación efectuada por la Agencia.
> b) Por fallecimiento del responsable de datos en los
> casos de personas naturales.
> c) Por disolución de la persona jurídica.
> d) Por resolución judicial ejecutoriada.
> e) Por cese voluntario de la actividad del responsable
> de datos.
> El término de vigencia de un certificado por alguna de
> las causales señaladas precedentemente será inoponible a
> terceros, mientras no sea eliminado del registro.

> **Source:** Ley 19.628 Artículo 52 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 53 — Revocation of certification
**Spanish anchor:** Artículo 53

### Plain-English text

Article 53.- Revocation of certification. The Agency may revoke the certification indicated in the preceding articles, if the controller fails to comply with what is established in this Paragraph. For this purpose, the Agency may require all such information as is necessary for the exercise of its functions.

Controllers may except themselves from delivering the requested information when it is covered by an obligation of secrecy or confidentiality, having to demonstrate such circumstance.

Failure to comply with the delivery of the required information, as well as the delivery of false, incomplete, or manifestly erroneous information, shall be sanctioned in accordance with this law.

When a certificate has been revoked by the Agency, in order to apply for it again the data controller must reliably demonstrate that the cause that gave rise to its revocation has been remedied.

Title VIII

On the processing of personal data by the National Congress, the Judicial Branch, and public bodies endowed with constitutional autonomy

### Original Spanish

> Artículo 53.- Revocación de la certificación. La
> Agencia puede revocar la certificación indicada en los
> artículos precedentes, si el responsable no da cumplimiento
> a lo establecido en este Párrafo. Con este objeto, la
> Agencia podrá requerir toda aquella información que fuere
> necesaria para el ejercicio de sus funciones.
> Los responsables pueden exceptuarse de entregar la
> información solicitada cuando la misma esté amparada por
> una obligación de secreto o confidencialidad, debiendo
> acreditar dicha circunstancia.
> El incumplimiento en la entrega de la información
> requerida, así como la entrega de información falsa,
> incompleta o manifiestamente errónea, será sancionado en
> conformidad con esta ley.
> Cuando un certificado ha sido revocado por la Agencia,
> para volver a solicitarlo el responsable de datos debe
> acreditar fehacientemente que la causal que dio origen a su
> revocación ha sido subsanada.
> Título VIII
> Del tratamiento de datos personales por el Congreso
> Nacional, el Poder Judicial y organismos públicos dotados
> de autonomía constitucional

> **Source:** Ley 19.628 Artículo 53 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

---

<!-- source: corpus/19628-data-protection-consolidated/titulo-08-organos-constitucionales.md -->
## FILE: corpus/19628-data-protection-consolidated/titulo-08-organos-constitucionales.md

# Ley 19.628 — Título VIII: Processing of Personal Data by the National Congress, the Judicial Branch, and Constitutionally Autonomous Public Bodies (Del tratamiento de datos personales por el Congreso Nacional, el Poder Judicial y organismos públicos dotados de autonomía constitucional — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** In force from 2026-12-01.

> **Title note:** New Title VIII inserted by Ley 21.719 Art. 1° item 14. Special framework for processing of personal data by the National Congress (Congreso Nacional), the Judicial Branch (Poder Judicial), and constitutionally autonomous public bodies (organismos públicos dotados de autonomía constitucional). Articles 54 and 55.

---

## Article 54 — General rule of processing of personal data (Title VIII bodies)
**Spanish anchor:** Artículo 54

### Plain-English text

**General rule of processing of personal data.** The processing of personal data (tratamiento de los datos personales) carried out by the National Congress (Congreso Nacional), the Judicial Branch (Poder Judicial), the Comptroller General of the Republic (Contraloría General de la República), the Public Prosecutor's Office (Ministerio Público), the Constitutional Court (Tribunal Constitucional), the Central Bank (Banco Central), the Electoral Service (Servicio Electoral) and the Electoral Justice (Justicia Electoral), and the other special tribunals created by law, is lawful when it is carried out for the fulfilment of their legal functions, within the scope of their competences, and in accordance with the special rules established in their respective organic laws and with the provisions of Title IV of this law applicable to public bodies (órganos públicos), with the exception of what is provided in Article 14 quinquies and in Articles 44 to 46, in so far as it refers to the intervention of the Comptroller General of the Republic in the determination of administrative liability (responsabilidad administrativa) and the application of Law No. 18.834. The civil servants (funcionarios) of these bodies must keep secrecy (guardar secreto) of such data. Under these conditions, these institutions and bodies have the status of data controllers (responsables de datos) and do not require the consent of the data subject (titular) to carry out the processing of their personal data.

The superior authorities of the internal organs of these institutions must issue the policies, rules, and instructions necessary to give effect to the principles and obligations established in this law, especially those that permit the exercise of the rights recognised to data subjects and those that fix the standards or minimum conditions of control, security, and safeguarding that must be observed in the processing of personal data, and may for that purpose request the technical assistance of the Agency. Likewise, the authorities of these bodies shall exercise disciplinary power (potestad disciplinaria) over their civil servants, in relation to the infringements that occur in the processing of personal data, particularly the infringements set out in Articles 34 bis, 34 ter, and 34 quáter.

> **TN:** The Spanish enumerates by name the constitutionally autonomous bodies (Contraloría, Ministerio Público, Tribunal Constitucional, Banco Central, Servicio Electoral, Justicia Electoral, and other special tribunals) rather than using a generic phrase. That enumeration is preserved literally here. "Funcionarios" is rendered as "civil servants" to capture the Chilean administrative-law meaning (career staff of a public body) without conflating it with private-sector "employees". "Guardar secreto" is rendered as "keep secrecy" to align with the secrecy-or-confidentiality framework of Art. 3(h). The cross-reference to Law N° 18.834 is to the Administrative Statute (Estatuto Administrativo) governing civil-service liability.

### Original Spanish

> Artículo 54.- Regla general del tratamiento de datos
> personales. Es lícito el tratamiento de los datos
> personales que efectúan el Congreso Nacional, el Poder
> Judicial, la Contraloría General de la República, el
> Ministerio Público, el Tribunal Constitucional, el Banco
> Central, el Servicio Electoral y la Justicia Electoral, y
> los demás tribunales especiales creados por ley, cuando se
> realiza para el cumplimiento de sus funciones legales,
> dentro del ámbito de sus competencias y, de conformidad a
> las normas especiales que se establecen en sus respectivas
> leyes orgánicas y a las disposiciones del Título IV de
> esta ley aplicables a los órganos públicos, con excepción
> de lo dispuesto en el artículo 14 quinquies y en los
> artículos 44 a 46, en lo referido a la intervención de la
> Contraloría General de la República en la determinación
> de la responsabilidad administrativa y la aplicación de la
> ley N° 18.834. Los funcionarios de estos organismos
> deberán guardar secreto de tales datos. En esas condiciones
> estas instituciones y organismos tienen la calidad de
> responsables de datos y no requieren el consentimiento del
> titular para efectuar el tratamiento de sus datos
> personales.
> Las autoridades superiores de los órganos internos de
> estas instituciones deberán dictar las políticas, normas e
> instrucciones necesarias para dar cumplimiento a los
> principios y obligaciones establecidos en esta ley,
> especialmente aquellas que permitan el ejercicio de los
> derechos que se reconocen a los titulares de datos y las que
> fijan los estándares o condiciones mínimas de control,
> seguridad y resguardo que se deben observar en el
> tratamiento de los datos personales, pudiendo requerir para
> ello la asistencia técnica de la Agencia. Asimismo, las
> autoridades de estos órganos ejercerán la potestad
> disciplinaria respecto de sus funcionarios, en relación a
> las infracciones que se produzcan en el tratamiento de los
> datos personales, particularmente las infracciones
> señaladas en los artículos 34 bis, 34 ter y 34 quáter.

> **Source:** Ley 19.628 Artículo 54 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

## Article 55 — Exercise of rights and claims (Title VIII bodies)
**Spanish anchor:** Artículo 55

### Plain-English text

**Exercise of rights and claims.** Data subjects (titulares de datos) shall exercise the rights recognised to them by this law before the National Congress, the Judicial Branch, the Comptroller General of the Republic, the Public Prosecutor's Office, the Constitutional Court, the Central Bank, the Electoral Service, the Electoral Justice, and the other special tribunals created by law, in accordance with rational and just procedures (procedimientos racionales y justos), and before the organs that these institutions designate, in conformity with what is set out in the preceding article.

In the event that the Comptroller General of the Republic, the Public Prosecutor's Office, the Central Bank, or the Electoral Service unjustifiedly or arbitrarily deny the exercise of a right recognised by this law to a data subject, or otherwise infringe any principle established in Article 3°, duty, or obligation established in it, causing the data subject prejudice, the data subject who is aggrieved or affected by the body's decision may file a claim before the Court of Appeals (Corte de Apelaciones), in accordance with the procedure provided in Article 43 of this law.

The superior authorities of the National Congress, the Judicial Branch, the Constitutional Court, the Electoral Justice, and the other special tribunals created by law, must ensure that, in the processing of personal data carried out by these institutions, the principles established in Article 3° and the duties are strictly complied with, and that the rights of the data subjects established in this law are respected, by adopting the supervisory and internal-control measures (medidas de fiscalización y control interno) that are necessary and adequate for that purpose.

> **TN:** Article 55 distinguishes between two groups of Title VIII bodies: (i) bodies whose data-subject-rights denials are judicially reviewable by the Court of Appeals under Art. 43 (Contraloría, Ministerio Público, Banco Central, and Servicio Electoral — listed in the second paragraph); and (ii) bodies whose superior authorities must instead self-supervise compliance (Congreso Nacional, Poder Judicial, Tribunal Constitucional, Justicia Electoral, and other special tribunals — listed in the third paragraph). The split reflects the constitutional separation of powers: Art. 43 judicial review is available against constitutionally autonomous administrative-style bodies, but not against the legislature or the judiciary themselves, which are subject only to internal supervisory mechanisms.

### Original Spanish

> Artículo 55.- Ejercicio de los derechos y
> reclamaciones. Los titulares de datos ejercerán los
> derechos que les reconoce esta ley ante el Congreso
> Nacional, el Poder Judicial, la Contraloría General de la
> República, el Ministerio Público, el Tribunal
> Constitucional, el Banco Central, el Servicio Electoral y la
> Justicia Electoral, y los demás tribunales especiales
> creados por ley, de acuerdo a procedimientos racionales y
> justos, y ante los organismos que dispongan estas
> instituciones, de conformidad a lo señalado en el artículo
> anterior.
> En caso que la Contraloría General de la República,
> el Ministerio Público, el Banco Central o el Servicio
> Electoral denieguen injustificada o arbitrariamente el
> ejercicio de un derecho reconocido por esta ley a un titular
> de datos, o bien infrinjan algún principio establecido en
> el artículo 3°, deber u obligación establecida en ella,
> causándole perjuicio, el titular que se vea agraviado o
> afectado por la decisión del organismo, podrá reclamar
> ante la Corte de Apelaciones, de acuerdo al procedimiento
> dispuesto en el artículo 43 de esta ley.
> Las autoridades superiores del Congreso Nacional, del
> Poder Judicial, del Tribunal Constitucional, de la Justicia
> Electoral y de los demás tribunales especiales creados por
> ley, deberán asegurarse que en el tratamiento de los datos
> personales que realizan estas instituciones se cumplen
> estrictamente con los principios establecidos en el
> artículo 3° y los deberes, y se respeten los derechos de
> los titulares establecidos en esta ley, adoptando las
> medidas de fiscalización y control interno que resulten
> necesarias y adecuadas para esta finalidad.

> **Source:** Ley 19.628 Artículo 55 as inserted by Ley 21.719 Art. 1° item 14 (in force 2026-12-01).

---

---

<!-- source: corpus/19628-data-protection-consolidated/titulo-final.md -->
## FILE: corpus/19628-data-protection-consolidated/titulo-final.md

# Ley 19.628 — Título Final: Repealed (Título Final — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** Título Final repealed (derogado) by Ley 21.719 Art. 1° item 15, in force 2026-12-01.

> **Title note:** Ley 21.719 Art. 1° item 15 expressly repealed (derogó) the entire Título Final of Ley 19.628 — which had consisted of Article 24, an amendment to Article 127 of the Health Code (Código Sanitario) creating a confidentiality rule for medical prescriptions, clinical-laboratory analyses, and pharmacy statistical disclosures.
>
> The Health Code amendment introduced by the original Art. 24 (1999) remains substantively in force within the Health Code itself; only its location as part of Ley 19.628 has been repealed. References to the Health Code's privacy rule should now be made directly to Article 127 of the Código Sanitario.

---

## Repealed — Former Article 24 (Health Code amendment)
**Spanish anchor:** Art. 24° (derogado)
**Tags:** repealed, derogated, Health-Code

### Plain-English text

**This article is repealed (derogado) as of 2026-12-01.** The original Article 24 of Ley 19.628 (1999) added new second and third paragraphs to Article 127 of the Health Code (Código Sanitario), establishing confidentiality of medical prescriptions, clinical-laboratory analyses, and related health services, and permitting pharmacies to disclose product-sales statistics provided no patient-identifying or prescribing-physician information was included.

The amendment to the Health Code introduced by the 1999 baseline Art. 24 remains substantively effective within the Health Code itself. Only its presence as a provision of Ley 19.628 has been repealed.

### Original Spanish (1999 baseline — repealed by Ley 21.719)

> Artículo 24.- Agrégase los siguientes incisos
> segundo y tercero, nuevos, al artículo 127 del Código
> Sanitario:
> ''Las recetas médicas y análisis o exámenes de
> laboratorios clínicos y servicios relacionados con la
> salud son reservados. Sólo podrá revelarse su contenido
> o darse copia de ellos con el consentimiento expreso del
> paciente, otorgado por escrito. Quien divulgare su
> contenido indebidamente, o infringiere las disposiciones
> del inciso siguiente, será castigado en la forma y con
> las sanciones establecidas en el Libro Décimo.
> Lo dispuesto en este artículo no obsta para que las
> farmacias puedan dar a conocer, para fines estadísticos,
> las ventas de productos farmacéuticos de cualquier
> naturaleza, incluyendo la denominación y cantidad de
> ellos. En ningún caso la información que proporcionen
> las farmacias consignará el nombre de los pacientes
> destinatarios de las recetas, ni el de los médicos que
> las expidieron, ni datos que sirvan para
> identificarlos.''.

### Cross-references
- Art. 127, Health Code (Código Sanitario) — the underlying provision that was amended by the original Art. 24; remains in force within the Health Code.

> **Source:** Ley 19.628 Título Final (Art. 24°) repealed in its entirety by Ley 21.719 Art. 1° item 15 (in force 2026-12-01).

---

---

<!-- source: corpus/19628-data-protection-consolidated/transitorios.md -->
## FILE: corpus/19628-data-protection-consolidated/transitorios.md

# Ley 19.628 — Disposiciones transitorias: Transitional Provisions (Disposiciones transitorias — consolidated, in force 2026-12-01)

**Law:** Ley 19.628 (consolidated, in force 2026-12-01)
_law:_ 19.628
**Status:** In force from 2026-12-01.

> **NOTE ON ARTICLE NUMBERING:** The three transitional articles are numbered 1°, 2°, and 3° within the transitional provisions section — independently of the main law's article numbering (Arts. 1–24). Because the extraction tool (`_extracted.json`) assigns `article_num` values of "1", "2", and "3" to these transitional articles — the same numbers as Arts. 1°, 2°, and 3° of Título Preliminar — there is a name collision in the extracted data. To avoid parity-check false positives, anchors in this file use the `Transitorio` prefix (e.g., `## Transitorio 1`) instead of `Article`, which distinguishes them from the main-law articles and prevents regex matching conflicts.

---

## Transitorio 1 — Entry into force; adjustment period for public-body databases
**Spanish anchor:** Art. 1° transitorio
**Tags:** transitional, entry-into-force, sixty-day-period, public-bodies, Article-22-deferred

### Plain-English text

The provisions of this law, with the exception of Article 22, shall enter into force within a period of sixty days counted from the date of its publication in the Official Gazette (Diario Oficial).

> **TN:** The 1999 baseline second and third paragraphs of this transitional Article 1° (concerning public-body database adjustment to the law and the deferred entry-into-force of Article 22) were eliminated by Ley 21.719 Art. 1° item 16. Only the first paragraph subsists. The deferred entry-into-force regime for Article 22 of the 1999 baseline is no longer operative under the consolidated law, since Art. 22 of the 1999 baseline (Civil Registry registration of public-body databases) has itself been superseded by the new Art. 22 of the consolidated law (inter-agency cession; entirely replaced by Ley 21.719 Art. 1° item 12).
>
> The sixty-day general period ran from the date of publication in the Diario Oficial (28 August 1999), placing the general entry into force of the original 1999 law on or around 27 October 1999. This historical first paragraph remains in the consolidated text but its operative period has long since elapsed; the consolidated law's own entry into force is 2026-12-01 per Ley 21.719's own transitional provisions.

### Original Spanish

> Artículo 1°.- Las disposiciones de esta ley, con
> excepción del artículo 22, entrarán en vigencia dentro
> del plazo de sesenta días, contados desde la fecha de su
> publicación en el Diario Oficial.

> **TN — eliminated 1999 baseline paragraphs (preserved for historical reference):** The second and third paragraphs of this transitorio in the 1999 baseline were eliminated by Ley 21.719 Art. 1° item 16. Their verbatim Spanish text was: "Los actuales registros o bancos de datos personales de organismos públicos se ajustarán a las disposiciones de este cuerpo legal, a contar de su entrada en vigencia. Lo dispuesto en el artículo 22 comenzará a regir un año después de la publicación de esta ley. Sin perjuicio de lo anterior, los organismos públicos que tuvieren a su cargo bancos de datos personales deberán remitir los antecedentes a que se refiere dicho precepto con anterioridad, dentro del plazo que fije el reglamento." Literal English: the existing registries or data banks of personal data of public bodies shall adjust to the provisions of this legal body, counted from its entry into force; what is provided in Article 22 shall begin to govern one year after the publication of this law; without prejudice to the foregoing, the public bodies that hold personal-data banks must remit the background information referred to in that precept beforehand, within the period fixed by the regulation. These paragraphs governed the original 1999 transition and are not operative under the consolidated law; the consolidated entry-into-force regime is set by Ley 21.719's own transitional articles (2026-12-01).

### Cross-references
- Art. 22 (consolidated — now covers inter-agency cession, not Civil Registry registration).
- Disposición transitoria Art. 3° (Transitorio 3 — transitional rule for the Commercial Bulletin regulations).

> **Source:** Disposición transitoria Art. 1° of Ley 19.628 as amended by Ley 21.719 Art. 1° item 16 (in force 2026-12-01). Item 16 eliminated the second and third paragraphs.

---

## Transitorio 2 — Rights of data subjects under pre-existing databases
**Spanish anchor:** Art. 2° transitorio
**Tags:** transitional, pre-existing-databases, data-subject-rights, retroactivity

### Plain-English text

Data subjects (titulares de los datos personales) whose personal data are recorded in data banks (bancos de datos) created before the entry into force of this law shall have the rights conferred on them by this law.

> **TN:** This transitional provision confirms that the rights granted by the law (Arts. 12–16) apply retroactively to data recorded in pre-existing databases, not only to data collected after entry into force. This is consistent with the purpose of data-subject rights as personal rights rather than rights conditioned on the date of data collection.

### Original Spanish

> Artículo 2°.- Los titulares de los datos personales
> registrados en bancos de datos creados con anterioridad a la
> entrada en vigencia de la presente ley tendrán los derechos
> que ésta les confiere.

### Cross-references
- Art. 12 (rights of access, modification, erasure, and blocking — conferred on pre-existing-database data subjects by this article).
- Art. 13 (non-waiver of data subject rights).
- Art. 16 (judicial remedy for enforcement of those rights).
- Disposición transitoria Art. 1° (Transitorio 1 — establishes when the law entered into force, i.e., sixty days after publication).

---

## Transitorio 3 — Continued application of the Commercial Bulletin regulations
**Spanish anchor:** Art. 3° transitorio
**Tags:** transitional, Commercial-Bulletin, Boletín-Informaciones-Comerciales, Supreme-Decree-950, continuity

### Plain-English text

The rules governing the Commercial Bulletin (Boletín de Informaciones Comerciales) established by Ministry of Finance Supreme Decree No. 950 of 1928 shall continue to apply in all respects that are not contrary to the provisions of this law.

> **TN:** The "Boletín de Informaciones Comerciales" is the commercial information bulletin created by Ministry of Finance Supreme Decree No. 950 of 1928. This transitional provision ensures legal continuity for the existing regulatory framework of the Bulletin, subject to conformity with Ley 19.628. See also Art. 17 (which regulates the types of data the Bulletin may communicate) and Disposición transitoria Art. 1° of Ley 19812 (which imposed additional restrictions on the Bulletin in relation to Art. 17 data).

### Original Spanish

> Artículo 3°.- Las normas que regulan el Boletín de
> Informaciones Comerciales creado por el decreto supremo de
> Hacienda N° 950, de 1928, seguirán aplicándose en todo lo
> que no sean contrarias a las disposiciones de esta ley.''.

### Cross-references
- Art. 17 (specific rules governing the types of data the Commercial Bulletin may communicate — primary substantive provision applicable to the Bulletin).
- Art. 18 (five-year time limit on communication of financial obligation data — applicable to the Bulletin).
- Art. 19 (update obligations upon payment — applicable to the Bulletin).
- Disposición transitoria Art. 1° (Transitorio 1 — general entry-into-force rule — the Commercial Bulletin's existing rules continue only from that date forward, subject to conformity with this law).

---

---
