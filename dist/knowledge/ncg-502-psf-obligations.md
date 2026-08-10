<!-- GENERATED — do not edit by hand. Source: corpus/_agent-policy.md + corpus/. Regenerate: python -m tools.build_dist -->
# ncg-502-psf-obligations

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

<!-- source: corpus/ncg/502-psf-obligations-consolidated/README.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/README.md

# NCG 502 — Registration, Authorization & Obligations of PSF (consolidated)

**Issued:** 2024-01-12 by the Comisión para el Mercado Financiero (CMF).
**Implements:** Ley 21.521 (Ley Fintec) Título II, arts. 4–13.
**Source PDF:** `sources/NCG 502.pdf` (baseline); `sources/ncg_524_2024.pdf` (amendments).

This is the core CMF regulation for every Financial-Service Provider (PSF)
under Ley 21.521 Título II. It governs the registration process, per-service
authorization requirements, disclosure obligations, corporate governance and
risk management, capital and guarantees, operational capacity, and reporting.

This corpus is **NCG 502 consolidated**: the baseline text published on
12-ene-2024 **with all 116 amendments from NCG 524 (02-dic-2024) applied**.
The amendments are no longer pending — they are integrated directly into the
section files below, and amended sections carry a `> **Source:**` footer naming
the 524 item(s). **Cite this as the current operative text.** The item→section
map for every amendment lives in `../524-amendments-changelog/changes.md`.

## Section layout
- `seccion-01-registro.md` — I. Registro de Prestadores de Servicios Financieros
- `seccion-02-autorizacion.md` — II. Autorización para la Prestación de Servicios
- `seccion-03-divulgacion.md` — III. Obligaciones de Divulgación y Entrega de Información
- `seccion-04a-gobierno-asesoria-inversion.md` — IV.A
- `seccion-04b-gobierno-asesoria-crediticia.md` — IV.B
- `seccion-04c-gobierno-plataformas-sat.md` — IV.C
- `seccion-04d-gobierno-enrutamiento.md` — IV.D
- `seccion-04e-gobierno-intermediacion-custodia.md` — IV.E
- `seccion-05-capital-garantias.md` — V. Capital y Garantías
- `seccion-06-09-disposiciones-finales.md` — VI–IX
- `anexo-01-definiciones.md`, `anexo-02-reporte-incidentes.md`, `anexo-03-reporte-perdidas.md`

## _law_ hint
_law:_ NCG-502

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/anexo-01-definiciones.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/anexo-01-definiciones.md

# NCG 502 — Anexo N°1: Definitions (Definiciones)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

## Anexo N°1 — Definitions (A–C)
**NCG anchor:** N° 502, Anexo N°1
**Implements:** Ley 21.521 (definitions used across NCG 502)
**Tags:** definitions, glossary

### Plain-English text

**Activos de información (information assets):** corresponds to information resources or elements related to the processing of information, which may be primary — such as information (physical and logical) and business processes and activities — or support, such as hardware; software; communications networks; personnel; among others.

**Amenaza (threat):** refers to any circumstance or event that could exploit a vulnerability.

**Análisis de impacto del negocio o BIA (business impact analysis or BIA):** is the procedure for analysing the effects that a business interruption may have on the entity's processes.

**Apetito por riesgo (risk appetite):** the aggregate level and types of risk that an entity is willing to assume, previously decided and within its risk capacity, in order to achieve its strategic objectives and business plan.

**Ataque (attack):** in the context of cybersecurity, refers to an event that has the intention to destroy, expose, alter, disable, steal, or obtain access to or make unauthorised use of an information asset.

**Ciberseguridad (cybersecurity):** corresponds to the set of actions carried out by the entity to mitigate risks and protect information and the infrastructure that supports it from cyberspace events, cyberspace being the resulting environment of the interaction of persons, software, and services on the Internet through technological devices connected to that network.

**Cliente activo (active client):** every person or entity that meets any of the following conditions and that does not have the status of qualified investor under subparagraph f) of Article 4° bis of Ley N° 18.045:

| Service type (Tipo de servicio) | Active clients (Clientes activos) |
|---|---|
| Investment advisory or credit advisory (Asesoría de inversión o crediticia) | Those who have received or requested a personalized advisory service during the last 3 months, that is, in the case of investment advisory, an evaluation or recommendation regarding the advisability of making a particular investment or transaction in publicly offered securities, financial instruments, or investment projects that responds to the particular request made by the person to the advisor; or, in the case of credit advisory, an evaluation or recommendation regarding the capacity or probability of payment, or of identity, for the purposes of obtaining, modifying, or renegotiating a credit or financing. |
| Order routing (Enrutamiento de órdenes) | Those who have submitted orders to be routed by the order router during the last 3 months. |
| Crowdfunding platform (Plataforma de financiamiento colectiva) | Those who have participated in the financing of an investment project or financing need during the last 3 months. |
| Alternative trading systems (Sistemas alternativos de transacción) | Those who have made a quotation, offer, or transaction on the alternative trading system during the last 3 months. |
| Intermediation of financial instruments (Intermediación de instrumentos financieros) | Those who have given a purchase-sale order to the intermediary during the last 3 months. Also, those who have acted as counterparty to the intermediary in transactions with financial instruments. |
| Custody of financial instruments (Custodia de instrumentos financieros) | Those who hold balances in custody of at least 100,000 pesos. |

**Cliente inactivo (inactive client):** an inactive client is defined as one who does not meet the conditions to be considered an active client.

**Inversionista institucional (institutional investor):** those referred to in subparagraph e) of Article 4 bis of Ley N° 18.045 on the Securities Market.

**Confidencialidad de la información (confidentiality of information):** protection of data against unauthorised access and disclosure, as defined by the board of directors or equivalent body. It includes the means to protect personal privacy and reserved information, especially that of the entity's clients.

### Original Spanish

> "ANEXO N° 1: DEFINICIONES
>
> Activos de información: corresponde a los recursos de información o elementos relacionados con el tratamiento de la información, los cuales pueden ser primarios como la información (física y lógica) y los procesos y actividades de negocio, o de soporte como hardware; software; redes de comunicación; personal; entre otros.
>
> Amenaza: se refiere a cualquiera circunstancia o evento que pudiera explotar una vulnerabilidad.
>
> Análisis de impacto del negocio o BIA: es el procedimiento de análisis de los efectos que puede tener en los procesos de la entidad una interrupción del negocio.
>
> Apetito por riesgo: nivel agregado y tipos de riesgo que una entidad está dispuesta a asumir, previamente decidido y dentro de su capacidad de riesgo, a fin de lograr sus objetivos estratégicos y plan de negocio.
>
> Ataque: en el contexto de ciberseguridad, se refiere a un evento que tuviera como intención destruir, exponer, alterar, deshabilitar, robar, u obtener acceso o hacer un uso no autorizado de un activo de información.
>
> Ciberseguridad: corresponde al conjunto de acciones que realiza la entidad para mitigar los riesgos y proteger la información e infraestructura que la soporta, de eventos del ciberespacio, siendo este último el entorno resultante de la interacción de personas, software y servicios en Internet a través de dispositivos tecnológicos conectados a dicha red.
>
> Cliente activo: toda persona o entidad que cumpla con alguna de las siguientes condiciones y que no tenga la calidad de inversionista calificado de la letra f) del artículo 4°bis de la Ley N°18.045: Asesoría de inversión o crediticia: Quienes hayan recibido o solicitado un servicio de asesoría personalizada durante los últimos 3 meses, esto es, en el caso de asesoría de inversión, una evaluación o recomendación respecto de la conveniencia de realizar una determinada inversión u operación en valores de oferta pública, instrumentos financieros o proyectos de inversión que responde a la petición particular efectuada por la persona al asesor; o, en el caso de asesoría crediticia, una evaluación o recomendación respecto de la capacidad o probabilidad de pago, o de la identidad, para fines de la obtención, modificación o renegociación de un crédito o financiamiento. Enrutamiento de órdenes: Quienes hayan ingresado órdenes para ser canalizadas por el enrutador durante los últimos 3 meses. Plataforma de financiamiento colectiva: Quienes hayan participado en el financiamiento de un proyecto de inversión o necesidad de financiamiento durante los últimos 3 meses. Sistemas alternativos de transacción: Quienes hayan realizado una cotización, oferta o transacción en el sistema alternativo de transacción en los últimos 3 meses. Intermediación de instrumentos financieros: Quienes hayan otorgado una orden de compraventa al intermediario durante los últimos 3 meses. Además, quienes hayan actuado como contraparte del intermediario en operaciones con instrumentos financieros. Custodia de instrumentos financieros: Quienes posean saldos en custodia por un monto de, al menos, 100.000 pesos.
>
> Cliente inactivo: se define como cliente inactivo aquel que no cumple con las condiciones para ser considerado cliente activo.
>
> Inversionista institucional: aquellos de la letra e) del artículo 4 bis de la Ley N°18.045 de Mercado de Valores.
>
> Confidencialidad de la información: protección de los datos contra el acceso y la divulgación no autorizados, definido por el directorio u órgano equivalente. Incluye los medios para proteger la privacidad personal y la información reservada, en especial de los clientes de la entidad."

### Cross-references
- NCG 502 §IV (Gobierno Corporativo y Gestión de Riesgos) — primary consumer of these definitions.
- NCG 502 §IV.A.5, §IV.B.5, §IV.C.7, §IV.D, §IV.E.8 — Información de Incidentes Operacionales sections use the definitions of incidente and riesgo operacional.
- Ley 18.045 Art. 4 bis(e) — definition of institutional investor referenced in Inversionista institucional.
- Ley 18.045 Art. 4 bis(f) — qualified-investor status excluded from Cliente activo.
- NCG 502 Anexo N°2 — operational-incident report that relies on the defined terms above.
- NCG 502 Anexo N°3 — operational-loss report that relies on the defined terms above.

> **TN:** NCG 524 spliced text into an existing sentence here; consolidated Spanish is faithful (verified against the 524 source PDF) but is not contiguous in either single source PDF. The amended "Cliente activo" definition is a two-column table in the 524 PDF that pdfplumber extracts in a column-interleaved order breaking the cell descriptions mid-sentence; it is transcribed here as flat prose. Individual cell passages match the 524 PDF, but this aggregated A–C definitions block reaches only ~0.51 chunk-coverage against either source PDF.

> **Source:** NCG 502 Anexo N°1 (12-ene-2024), as amended by NCG 524 items H.1, H.2, and H.3 (02-dic-2024).

---

## Anexo N°1 — Definitions (D–M)
**NCG anchor:** N° 502, Anexo N°1
**Implements:** Ley 21.521 (definitions used across NCG 502)
**Tags:** definitions, glossary

### Plain-English text

**Downtime:** the amount of time that a process or business is interrupted.

**Encargado del proceso (process owner):** corresponds to the person designated to be responsible for the administration of a process and to promote the improvements to be implemented in it.

**Externalización de servicios (outsourcing of services):** is the continuous or occasional execution by an external provider of services or activities that could normally be carried out by the contracting entity.

**Incidente (incident):** a single event or series of unexpected or undesired information-security events that result in an attempted unauthorised access, use, disclosure, modification, or destruction of information; an impediment to the normal operation of networks, systems, or IT resources; or a violation of the entity's information-security policy.

**Instancia (organisational instance):** refers to a level or degree of the entity's organisational structure; this includes committee, unit, division, department, or other equivalent.

**Malware:** software intended to carry out an unauthorised process that will have an adverse impact on the availability, confidentiality, and integrity of an information system. A virus, "worm," Trojan, or other code-based entity that infects a host. "Spyware" and some forms of adware are also examples of malicious code.

**Mecanismos de autenticación (authentication mechanisms):** mechanisms used to confirm the identity of a user. These mechanisms may use one or more authentication factors, for example, credentials, passwords, digital certificates, or biometric or biological characteristics. An authentication mechanism is multi-factor when it uses a combination of authentication factors to confirm identity.

**Mercado (market):** for the purpose of calculating the equity requirement for market risk for shares and share indices of derivative instruments and contracts for differences, "market" refers to all shares listed on securities markets located in the same national jurisdiction.

**Niveles mínimos aceptables de operación (minimum acceptable operating levels):** corresponds to the minimum level of services or products that are considered acceptable for the entity to meet its objectives during an interruption.

### Original Spanish

> "Downtime: la cantidad de tiempo que el proceso o negocio es interrumpido.
>
> Encargado del proceso: corresponde a aquella persona designada para hacerse responsable de la administración de un proceso y propiciar las mejoras a implementar en éste.
>
> Externalización de servicios: es la ejecución por un proveedor externo de servicios o actividades en forma continua u ocasional, las que normalmente podrían ser realizadas por la entidad contratante
>
> Incidente: evento único o serie de eventos de seguridad de la información inesperados o no deseados, que resultaren en un intento de acceso, uso, divulgación, modificación o destrucción no autorizada de información; un impedimento en la operación normal de las redes, sistemas o recursos informáticos; o una violación a la política de seguridad de la información de la entidad.
>
> Instancia: se refiere a un nivel o grado de la estructura organizacional de la entidad, esto incluye, comité, unidad, división, departamento u otro equivalente.
>
> Malware: software destinado a realizar un proceso no autorizado que tendrá un impacto adverso en la disponibilidad, confidencialidad e integridad de un sistema de información. Un virus, "worm", troyano u otra entidad basada en código que infecta un host. El "spyware" y algunas formas de adware también son ejemplos de código malicioso.
>
> Mecanismos de autenticación: mecanismos utilizados para confirmar la identidad de un usuario. Estos mecanismos pueden utilizar uno o más factores de autenticación, por ejemplo, credenciales, contraseñas, certificados digitales, o características biométricas o biológicas. El mecanismo de autenticación es multifactor cuando utiliza una combinación de factores de autenticación para confirmar la identidad.
>
> Mercado: para el cálculo del requisito de patrimonio por riesgo de mercado de acciones e índices accionarios de los instrumentos derivados y contratos por diferencias, mercado refiere a todas las acciones cotizadas en mercados de valores ubicados en la misma jurisdicción nacional.
>
> Niveles mínimos aceptables de operación: corresponde al mínimo nivel de servicios o productos que se consideran aceptables para que la entidad cumpla con sus objetivos durante una interrupción."

### Cross-references
- NCG 502 §IV — governance and risk management sections that use these terms operationally.
- NCG 502 Anexo N°2 — incidente definition governs what must be reported.

> **TN:** "Downtime" is retained in English as it appears verbatim in the Spanish source without a Spanish equivalent. "BIA" is likewise kept as the source uses the English acronym alongside the Spanish expansion.

> **Source:** NCG 502 Anexo N°1 (12-ene-2024).

---

## Anexo N°1 — Definitions (P–R)
**NCG anchor:** N° 502, Anexo N°1
**Implements:** Ley 21.521 (definitions used across NCG 502)
**Tags:** definitions, glossary

### Plain-English text

**Partes Interesadas (interested parties / stakeholders):** refers to the persons or organisations that interact with the activities and decisions of a company, such as employees, suppliers, clients, regulators, among others.

**Phishing:** a technique to attempt to acquire confidential data, such as bank account numbers, through a fraudulent request by email or on a website, in which the perpetrator impersonates a legitimate company or a trusted person.

**Procesamiento de datos (data processing):** electronic processing of data or of the basic elements of information, subjected to programmed operations.

**Proveedor de servicios (service provider):** an entity related or unrelated to the contracting institution that provides services or supplies goods and facilities to it.

**Punto objetivo de recuperación (RPO) (recovery point objective / RPO):** the maximum period of time before the data loss following an incident becomes unacceptable according to the entity's own quality standards.

**Riesgo aceptado (accepted risk):** corresponds to the level of risk that the entity is willing to accept in accordance with its risk management policy and its responsibilities established in the legal framework that governs it.

**Riesgo inherente (inherent risk):** corresponds to the risk that by its nature cannot be separated from the process or sub-process in which it occurs. It corresponds to the risk that each entity must assume in accordance with the scope of development of its activities established by law.

**Riesgo residual (residual risk):** the risk that persists after the entity adopts control and mitigation measures.

> **TN:** NCG 524 item H.4 deleted the Anexo N°1 definitions of Riesgo de crédito, Riesgo de contraparte, Riesgo crediticio del emisor, Riesgo de mercado, and Riesgo operacional (verified against the 524 source PDF — those five risk definitions no longer appear in Anexo N°1; the risk-category descriptions instead now live in the body of §IV). The cross-references below to §V.D.2 (Riesgo de mercado), §V.D.3 (Riesgo de crédito), and §IV (Riesgo operacional) are retained for navigation, but those terms are no longer defined in this Anexo following the deletion.

### Original Spanish

> "Partes Interesadas: refiere a las personas u organizaciones que se relacionan con las actividades y decisiones de una empresa, tales como empleados, proveedores, clientes, reguladores, entre otros.
>
> Phishing: una técnica para intentar adquirir datos confidenciales, como números de cuentas bancarias, a través de una solicitud fraudulenta por correo electrónico o en un sitio web, en la que el perpetrador se hace pasar por una empresa legítima o una persona de confianza.
>
> Procesamiento de datos: tratamiento electrónico de datos o de los elementos básicos de información, sometidos a operaciones programadas.
>
> Proveedor de servicios: entidad relacionada o no a la institución contratante, que preste servicios o provea bienes e instalaciones a éste.
>
> Punto objetivo de recuperación (RPO): período de tiempo máximo antes que la pérdida de datos que sigue a un incidente se vuelva inaceptable de acuerdo con los estándares de calidad de la propia entidad.
>
> Riesgo aceptado: corresponde al nivel de riesgo que la entidad está dispuesta a aceptar en concordancia con la política de gestión de riesgos y sus responsabilidades establecidas en el marco legal que las rige.
>
> Riesgo inherente: corresponde a aquel riesgo que por su naturaleza no puede ser separado del proceso o subproceso en que éste se presenta. Corresponde al riesgo que debe asumir cada entidad de acuerdo con el ámbito de desarrollo de sus actividades establecido por ley.
>
> Riesgo residual: aquel riesgo que persiste luego de adoptar las medidas de control y mitigación por parte de la entidad."

### Cross-references
- NCG 502 §V.D.2 — market risk capital requirement uses the Riesgo de mercado definition.
- NCG 502 §V.D.3 — credit risk capital requirement uses the Riesgo de crédito definition.
- NCG 502 §IV (all subsections) — operational risk governance uses the Riesgo operacional definition.

> **Source:** NCG 502 Anexo N°1 (12-ene-2024), as amended by NCG 524 item H.4 (02-dic-2024).

---

## Anexo N°1 — Definitions (S–V)
**NCG anchor:** N° 502, Anexo N°1
**Implements:** Ley 21.521 (definitions used across NCG 502)
**Tags:** definitions, glossary

### Plain-English text

**Servicios en la nube (cloud services):** services that provide infrastructure, platforms, or software that the client accesses through the network, without needing to install them on its own infrastructure, since they are located on a remote server of the service provider.

**Subcontratación en cadena de servicios externalizados (subcontracting chain of outsourced services):** those formed by third parties subcontracted by the initial service provider to carry out an important part of the activities contracted with it (subcontracting of other providers).

**Tiempos máximos tolerables de interrupción (maximum tolerable interruption times):** the maximum tolerable time during which a process could be interrupted without causing significant effects on operational continuity.

**Tiempo objetivo de recuperación (recovery time objective):** the period of time following an incident within which: a) a product, service, or activity must be resumed; or b) the resources must be recovered (resources being understood as assets, persons, skills, information, technology, facilities, supplies, and information necessary for business operations).

**Valor razonable (fair value):** the price that would be received for selling an asset or paid for transferring a liability in an orderly transaction in the principal (or most advantageous) market on the measurement date under current market conditions (i.e., an exit price), regardless of whether that price is directly observable or estimated using another valuation technique.

**Vulnerabilidad (vulnerability):** in the context of cybersecurity, refers to any weakness of an information asset or of a control mechanism that could be exploited by an attack; that is, it may be a flaw in a system that makes it accessible to attackers, or any type of weakness in the entity's own active assets in the procedures that leaves the entity's information security exposed to a threat.

### Original Spanish

> "Servicios en la nube: servicios que proveen infraestructura, plataformas o software a lo que el cliente accede a través de la red, sin la necesidad de instalarlos en su propia infraestructura, sino que están ubicados en un servidor remoto del proveedor del servicio.
>
> Subcontratación en cadena de servicios externalizados: las formadas por terceros subcontratados por el proveedor inicial de servicios para realizar parte importante de las actividades contratadas con éste (subcontrato de otros proveedores).
>
> Tiempos máximos tolerables de interrupción: tiempo máximo tolerable en que un proceso pudiera estar interrumpido sin provocar efectos relevantes en la continuidad operacional.
>
> Tiempo objetivo de recuperación: periodo de tiempo que sigue a un incidente dentro del cual: a) debe reanudarse un producto, servicio o actividad; o b) los recursos deben ser recuperados (entendiendo por recursos los activos, personas, habilidades, información, tecnología, instalaciones, suministros e información necesarios para las operaciones del negocio).
>
> Valor razonable: el precio que se recibiría por vender un activo o se pagaría por transferir un pasivo en una transacción ordenada en el mercado principal (o más ventajoso) en la fecha de medición en las condiciones actuales del mercado (es decir, un precio de salida) independientemente de si ese precio es directamente observable o estimado utilizando otra técnica de valoración.
>
> Vulnerabilidad: en el contexto de ciberseguridad, se refiere a cualquier debilidad de un activo de información o de un mecanismo de control que pudiera ser explotada por un ataque, es decir, puede ser un fallo en un sistema que lo torna accesible a los atacantes o cualquier tipo de debilidad en el propio activo en los procedimientos que deje la seguridad de la información de la entidad expuesta a una amenaza."

### Cross-references
- NCG 502 §IV.C.3.3 — externalización de servicios / subcontratación en cadena cross-referenced explicitly.
- NCG 502 §IV.C.3.2 and §IV.E.4.2 — continuidad del negocio sections use Tiempos máximos tolerables, Tiempo objetivo de recuperación, and Niveles mínimos aceptables.
- NCG 502 §V.C — Patrimonio Ajustado uses Valor razonable for asset valuation.
- NCG 502 §IV.A.2.2, §IV.C.3.1, §IV.E.4.1 — cybersecurity sections use Vulnerabilidad, Amenaza, Ataque, Malware.

> **Source:** NCG 502 Anexo N°1 (12-ene-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/anexo-02-reporte-incidentes.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/anexo-02-reporte-incidentes.md

# NCG 502 — Anexo N°2: Operational-Incident Report (Reporte de Incidentes Operacionales)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

## Anexo N°2 — Operational-Incident Report
**NCG anchor:** N° 502, Anexo N°2
**Implements:** Ley 21.521 (operational-incident reporting obligation; operationalises §IV reporting requirements)
**Tags:** operational-incident, reporting, template, cybersecurity, operational-risk

### Plain-English text

Through the "OPERATIONAL INCIDENTS AND LOSSES" (INCIDENTES Y PÉRDIDAS OPERACIONALES) menu of the official channel of communication and submission of information between the Commission (CMF) and its supervised entities, the entity must report the detail of each incident described in Section IV in accordance with the following scheme:

| Field (INFORMACION) | Detail (DETALLE) |
|---|---|
| Date and time of incident start | |
| Type of incident | |
| Detailed description of the incident | |
| Possible or identified causes | |
| Affected branches or assets | |
| Address of affected branches | |
| Affected channels | |
| Name of providers involved | |
| Type of provider involved | |
| Number of clients affected | |
| Type of clients affected | |
| Affected products or services | |
| Measures adopted and under way | |
| Other background information | |
| Names and positions of contact persons | |
| Contact telephone number | |
| Date and time of incident closure | |

For those fields for which the information is not available at the time of the report, the text "Under evaluation" ("En evaluación") must be entered; and for the case of numerical fields, if the figure is not available, those fields must be completed with a zero.

It shall be the entity's responsibility to update the foregoing information whenever new information becomes available and until the closure of the incident (incident closure date).

**FECHA Y HORA DEL INICIO DEL INCIDENTE — Date and time of incident start**
The date (DD/MM/YYYY) and time (HH:MM:SS) at which the incident began must be indicated.

**TIPO DE INCIDENTE — Type of incident**
This field must indicate the type of incident, choosing from the following options:
- Facility disruption (Afectación de instalaciones)
- Staff absence (Ausencia de Colaboradores)
- No access to branches and other specific areas (Sin acceso dependencias y otras áreas específicas)
- Base systems failure — OS, DB (Falla Sistemas Base (SO, BD))
- Application failure — business, web, batch (Falla aplicativos (negocio, web, batch))
- Communications failure (Falla de comunicaciones)
- Hardware failure (Falla Hardware)
- Basic-services failure — electricity/water (Falla en servicios básicos (electricidad/agua))
- Monetary-resource loss affecting the entity, its clients, and other interested parties (Pérdida de Recursos Monetarios de la entidad, sus clientes y otras partes interesadas)
- Information loss affecting the entity, its clients, and other interested parties (Pérdida de Información de la entidad, sus clientes y otras partes interesadas)
- Service interruption/latency (Interrupción/ latencia en servicios)
- Information-submission error (Error de envío de información)
- Others: specify (Otros: especificar)

**DESCRIPCIÓN DETALLADA DEL INCIDENTE — Detailed description of the incident**
This field must detail what the reported incident consists of.

**CAUSAS POSIBLES O IDENTIFICADAS — Possible or identified causes**
This field must provide an analysis of the causes of the incident and of the effectiveness of the measures adopted to resolve it.

**DEPENDENCIAS AFECTADAS — Affected branches**
This field must indicate the affected branches, choosing from the following options:
- Offices (Oficinas)
- Production site (Sitio Producción)
- Contingency site (Sitio Contingencia)
- Provider branches (Dependencias proveedor)
- Others: specify (Otros: especificar)

**DIRECCIÓN DEPENDENCIAS AFECTADAS (CALLE, COMUNA, REGIÓN) — Address of affected branches (street, municipality, region)**
This field must report the full address of the affected branch. If more than one branch is affected, the address of each must be indicated, separating them with a semicolon (;).

**CANALES AFECTADOS — Affected channels**
This field must select the channels affected by the incident (as applicable):
- Terminals (Terminales)
- Messaging (Mensajería)
- Custody services (Servicios de custodia)
- Branches (Sucursales)
- Others: specify (Otros: especificar)

**NOMBRE DE PROVEEDORES INVOLUCRADOS — Name of providers involved**
Corresponds to the name or corporate name (razón social) of the provider.

**TIPO DE PROVEEDOR INVOLUCRADO — Type of provider involved**
- Basic services (Servicios básicos)
- Telecommunications (Telecomunicaciones)
- Technological infrastructure (Infraestructura tecnológica)
- Processing (Procesamiento)
- Telephone service (Atención telefónica)
- Others: specify (Otros: especificar)

**NÚMERO DE CLIENTES AFECTADOS — Number of clients affected**
This field must be completed with the number of clients who were affected by the incident being reported.

**TIPO DE CLIENTES AFECTADOS — Type of clients affected**
This field must select the type of client affected, from the following options:
- Natural persons (Personas)
- Non-financial companies (Empresas no financieras)
- Financial companies — specify (Empresas financieras (Especificar))
- Clients (Clientes)
- Others: specify (Otros: Especificar)

**NÚMERO DE EMPLEADOS AFECTADOS — Number of employees affected**
This field must be completed with the number of employees who were affected by the incident being reported.

**SERVICIOS AFECTADOS — Affected services**
This field must report in detail the services affected by the incident.

**NÚMERO DE TRANSACCIONES AFECTADAS — Number of transactions affected**
This field must be completed with the number of transactions that were affected by the incident being reported.

**MEDIDAS ADOPTADAS — Measures adopted**
This field must report in detail the actions taken by the entity to overcome the incident.

**NOMBRE Y CARGO DE PERSONAS DE CONTACTO — Name and position of contact persons**
Corresponds to the persons who report the incident and their positions.

**TELÉFONO DE CONTACTO — Contact telephone number**
The mobile telephone number of the contact persons must be entered in this field.

**FECHA Y HORA DE TÉRMINO DEL INCIDENTE — Date and time of incident closure**
This field will be included when the incident is closed. The date (DD/MM/YYYY) and the time (HH:MM:SS) at which it ended must be completed.

### Original Spanish

> "ANEXO N° 2: REPORTE DE INCIDENTES OPERACIONALES
>
> A través del menú “INCIDENTES Y PÉRDIDAS OPERACIONALES” del canal oficial de comunicación y envío de información entre la Comisión y sus fiscalizados, la entidad deberá reportar el detalle de cada incidente descrito en la sección IV de acuerdo con el siguiente esquema:
>
> INFORMACION DETALLE Fecha y hora de inicio del incidente Tipo de incidente Descripción detallada del incidente Causas posibles o identificadas Dependencias o activos afectados Dirección dependencias afectadas Canales afectados Nombre de proveedores involucrados Tipo de proveedores involucrado Número de clientes afectados Tipo de clientes afectados Productos o servicios afectados Medidas adoptadas y en curso Otros antecedentes Nombres y cargos de las personas de contacto Teléfono de contacto Fecha y hora de cierre del incidente
>
> Para aquellos campos en los que al momento del reporte no se cuente con la información, se debe indicar con texto “En evaluación”, y para el caso de los campos numéricos, de no contarse con el dato, éstos deben completarse con un cero.
>
> Será responsabilidad de la entidad la actualización de los antecedentes mencionados cuando se disponga de nueva información y hasta el cierre del incidente (fecha de cierre del incidente).
>
> FECHA Y HORA DEL INICIO DEL INCIDENTE
> Se debe señalar la fecha (DD/MM/AAAA) y la hora (HH:MM:SS) en que comenzó el incidente.
>
> TIPO DE INCIDENTE
> En este campo se debe señalar el tipo de incidente, eligiendo entre las siguientes opciones:
>  Afectación de instalaciones  Ausencia de Colaboradores  Sin acceso dependencias y otras áreas específicas  Falla Sistemas Base (SO, BD)  Falla aplicativos (negocio, web, batch)  Falla de comunicaciones  Falla Hardware
>  Falla en servicios básicos (electricidad/agua)  Pérdida de Recursos Monetarios de la entidad, sus clientes y otras partes interesadas  Pérdida de Información de la entidad, sus clientes y otras partes interesadas  Interrupción/ latencia en servicios  Error de envío de información  Otros: especificar
>
> DESCRIPCIÓN DETALLADA DEL INCIDENTE
> En este campo se debe detallar en qué consiste el incidente reportado.
>
> CAUSAS POSIBLES O IDENTIFICADAS
> En este campo se debe realizar un análisis sobre las causas del incidente y sobre la efectividad de las medidas adoptadas para resolverlo.
>
> DEPENDENCIAS AFECTADAS
> En este campo se deben señalar las dependencias afectadas, eligiendo entre las siguientes opciones:
>  Oficinas  Sitio Producción  Sitio Contingencia  Dependencias proveedor  Otros: especificar
>
> DIRECCIÓN DEPENDENCIAS AFECTADAS (CALLE, COMUNA, REGIÓN)
> En este campo se debe informar la dirección completa de la dependencia afectada. Si existe más de una dependencia afectada, se debe indicar la dirección de cada una de ellas, separándolas con un punto y coma (;).
>
> CANALES AFECTADOS
> En este campo se deben seleccionar los canales afectados por el incidente (lo que sea aplicable):
>  Terminales  Mensajería  Servicios de custodia  Sucursales  Otros: especificar
>
> NOMBRE DE PROVEEDORES INVOLUCRADOS
> Corresponde al nombre o razón social del proveedor.
>
> TIPO DE PROVEEDOR INVOLUCRADO
>  Servicios básicos  Telecomunicaciones  Infraestructura tecnológica  Procesamiento  Atención telefónica  Otros: especificar
>
> NÚMERO DE CLIENTES AFECTADOS:
> En este campo se debe completar el número de clientes que fueron afectados por el incidente que se reporta.
>
> TIPO DE CLIENTES AFECTADOS:
> En este campo se debe seleccionar el tipo de cliente afectado, entre las siguientes opciones:
>  Personas  Empresas no financieras  Empresas financieras (Especificar)  Clientes  Otros: Especificar
>
> NÚMERO DE EMPLEADOS AFECTADOS
> En este campo se debe completar con el número de empleados que fueron afectados por el incidente que se reporta.
>
> SERVICIOS AFECTADOS
> En este campo se deben informar en detalle los servicios afectados por el incidente.
>
> NÚMERO DE TRANSACCIONES AFECTADAS
> En este campo se debe completar el número de transacciones que fueron afectadas por el incidente que se reporta.
>
> MEDIDAS ADOPTADAS
> En este campo se deben informar en detalle las acciones realizadas por la entidad para superar el incidente.
>
> NOMBRE Y CARGO DE PERSONAS DE CONTACTO
> Corresponden a las personas que informan el incidente y sus cargos.
>
> TELÉFONO DE CONTACTO
> Se debe señalar en este campo el teléfono celular de las personas de contacto.
>
> FECHA Y HORA DE TÉRMINO DEL INCIDENTE
> Este campo se incluirá cuando se cierra el incidente. Se debe completar la fecha (DD/MM/AAAA) y la hora (HH:MM:SS) en que éste finalizó."

### Cross-references
- NCG 502 §IV.A.5 — Información de Incidentes Operacionales (investment advisory): triggers this report.
- NCG 502 §IV.B.5 — Información de Incidentes Operacionales (credit advisory): triggers this report.
- NCG 502 §IV.C.7.1 — Registro y Comunicación de Incidentes Operacionales (crowdfunding / SAT): triggers this report.
- NCG 502 §IV.D — Enrutamiento de Órdenes: triggers this report.
- NCG 502 §IV.E.8.1 — Registro y Comunicación de Incidentes Operacionales (intermediation / custody): triggers this report.
- NCG 502 Anexo N°1 — definitions of incidente and riesgo operacional used in this template.
- NCG 502 Anexo N°3 — companion operational-loss report; the CMF-assigned incident ID generated here is used there.

> **TN:** The field heading "Dependencias o activos afectados" in the summary table is rendered "Affected branches or assets"; the field-instruction section heading is "DEPENDENCIAS AFECTADAS" only — both forms are preserved. "Colaboradores" (literally "collaborators") is rendered "Staff" in the incident-type list, tracking HR usage in Chilean entities. The table field "Productos o servicios afectados" has no standalone field-instruction paragraph in the PDF; the detailed-instructions section uses "SERVICIOS AFECTADOS" only — the table header appears to be broader. Rendered as found.

> **Source:** NCG 502 Anexo N°2 (12-ene-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/anexo-03-reporte-perdidas.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/anexo-03-reporte-perdidas.md

# NCG 502 — Anexo N°3: Operational-Loss Report (Reporte de Pérdidas Operacionales)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

## Anexo N°3 — Operational-Loss Report
**NCG anchor:** N° 502, Anexo N°3
**Implements:** Ley 21.521 (operational-loss reporting obligation; operationalises §IV.C.7.2 and §IV.E.8.2)
**Tags:** operational-loss, reporting, template, operational-risk

### Plain-English text

Through the "OPERATIONAL INCIDENTS AND LOSSES" (INCIDENTES Y PERDIDAS OPERACIONALES) menu of the official channel of communication and submission of information between the Commission (CMF) and its supervised entities, the entity must report, by the last business day of June and December of each year, the detail of all events that individually materialise in operational losses greater than 150 Unidades de Fomento. Additionally, the amounts of expenses and recoveries associated with operational losses linked to the same event must be reported.

| Field (INFORMACION) | Detail (DETALLE) |
|---|---|
| CMF-assigned incident identification number | |
| Discovery date | |
| Accounting date | |
| Amount type | |
| Expense type | |
| Recovery type | |
| Amount | |
| Name and position of the reporting person | |

**NUMERO DE IDENTIFICACIÓN DEL INCIDENTE ASIGNADO POR LA CMF — CMF-assigned incident identification number**
Corresponds to the code that uniquely identifies the reported incident, assigned by the Commission (CMF) when the start of the incident was reported through the "OPERATIONAL INCIDENTS AND LOSSES" (INCIDENTES Y PÉRDIDAS OPERACIONALES) menu of the official channel of communication and submission of information between the Commission (CMF) and its supervised entities.

**FECHA DE DESCUBRIMIENTO — Discovery date**
Select the day and time that will be displayed in this field corresponding to the date on which the loss event was identified.

**FECHA DE CONTABILIZACIÓN — Accounting date**
Select the day and time that will be displayed in this field corresponding to the date on which the loss or recovery is recorded in the financial statements.

**TIPO DE MONTO — Amount type**
Select the code that identifies the type of amount to be reported, in accordance with the following coding that will be displayed in this field:

| Code (CODIGO) | Amount type (TIPO DE MONTO) |
|---|---|
| 1 | Loss — direct charges in the income statement (Pérdida (cargos directos en los estados de resultados)) |
| 2 | Expenses — internal or external costs directly related to the operational event (Gastos (costos incurridos internos o externos con relación directa al evento operacional)) |
| 3 | Recovery (Recuperación) |

**TIPO DE GASTO — Expense type**
Select the code that identifies the primary type of expense associated with the loss event, whether internal or external directly attributable to the operational event, in accordance with the following coding that will be displayed in this field:

| Code (CODIGO) | Expense type (TIPO DE GASTO) |
|---|---|
| 1 | Legal (Legales) |
| 2 | Providers (Proveedores) |
| 3 | Advisory fees (Asesorías) |
| 4 | Internal (Internos) |
| 5 | Others (Otros) |
| 9 | Not applicable — must be reported when the "AMOUNT TYPE" field takes values 1 or 3 (No aplica (debe reportarse cuando el campo "TIPO DE MONTO" toma valores 1 o 3)) |

**TIPO DE RECUPERACIÓN — Recovery type**
Select the code associated with the causes of operational recovery, in accordance with the following coding that will be displayed in this field:

| Code (CODIGO) | Recovery type (TIPO DE RECUPERACIÓN) |
|---|---|
| 1 | Insurance companies (Compañías de seguros) |
| 2 | Legal actions (Acciones judiciales) |
| 3 | Others — provision reversal (Otros (liberación de provisión)) |
| 4 | Not applicable (No aplica) |

**MONTO — Amount**
Corresponds to the amount of losses, expenses, or recoveries that must be reported on the date on which they are recorded.

**NOMBRE Y CARGO DEL INFORMANTE — Name and position of the reporting person**
Corresponds to the person who reports the incident and their position.

### Original Spanish

> "ANEXO N° 3: REPORTE DE PÉRDIDAS OPERACIONALES
>
> A través del menú “INCIDENTES Y PERDIDAS OPERACIONALES” del canal oficial de comunicación y envío de información entre la Comisión y sus fiscalizados, la entidad deberá reportar al último día hábil de junio y diciembre de cada año el detalle de todos los eventos que materialicen individualmente en pérdidas operacionales mayores a 150 Unidades de Fomento. Además, se deberán reportar los montos de gastos y recuperaciones asociados a pérdidas operacionales asociados a un mismo evento.
>
> INFORMACION DETALLE Número de identificación del incidente asignado por la CMF Fecha de descubrimiento Fecha de contabilización Tipo de monto Tipo de gasto Tipo de recuperación Monto Nombre y cargo del informante
>
> NUMERO DE IDENTIFICACIÓN DEL INCIDENTE ASIGNADO POR LA CMF
> Corresponde al código que identifica en forma unívoca el incidente reportado, asignado por la CMF cuando se reportó el inicio del incidente a través del menú "INCIDENTES Y PÉRDIDAS OPERACIONALES" del canal oficial de comunicación y envío de información entre la Comisión y sus fiscalizados.
>
> FECHA DE DESCUBRIMIENTO
> Seleccionar el día y hora que se desplegará en este campo correspondiente a la fecha en la que se identificó el evento de pérdida.
>
> FECHA DE CONTABILIZACIÓN
> Seleccionar el día y hora que se desplegará en este campo correspondiente a la fecha en la que se imputa contablemente la pérdida o recupero en los estados financieros.
>
> TIPO DE MONTO
> Seleccionar el código que identifica el tipo de monto a reportar, de acuerdo con la siguiente codificación que se desplegará en este campo:
>
> CODIGO TIPO DE MONTO 1 Pérdida (cargos directos en los estados de resultados) 2 Gastos (costos incurridos internos o externos con relación directa al evento operacional) 3 Recuperación
>
> TIPO DE GASTO
> Seleccionar el código que identifica el principal tipo de gasto asociado al evento de pérdida, ya sea interno o externo directamente atribuible al evento operacional, de acuerdo con la siguiente codificación que se desplegará en este campo:
>
> CODIGO TIPO DE GASTO 1 Legales 2 Proveedores 3 Asesorías 4 Internos 5 Otros 9 No aplica (debe reportarse cuando el campo "TIPO DE MONTO" toma valores 1 o 3)
>
> TIPO DE RECUPERACIÓN
> Seleccione el código asociado a las causas de la recuperación operacional, de acuerdo con la siguiente codificación que se desplegará en este campo:
>
> CODIGO TIPO DE RECUPERACIÓN 1 Compañías de seguros 2 Acciones judiciales 3 Otros (liberación de provisión) 4 No aplica
>
> MONTO
> Corresponde al monto de las pérdidas, gastos o recuperaciones que deben reportarse en la fecha en la que se contabilicen.
>
> NOMBRE Y CARGO DEL INFORMANTE
> Corresponde a la persona que informa el incidente y su cargo."

### Cross-references
- NCG 502 §IV.C.7.2 — Registro y Comunicación de Pérdidas Operacionales (crowdfunding / SAT): triggers this report (150 UF threshold, June and December).
- NCG 502 §IV.E.8.2 — Registro y Comunicación de Pérdidas Operacionales (intermediation / custody): triggers this report.
- NCG 502 Anexo N°1 — definitions of riesgo operacional and pérdida operacional (operational loss) used in this template.
- NCG 502 Anexo N°2 — the CMF-assigned incident identification number in this report is generated when the incident is first reported via Anexo N°2.

> **TN:** "Unidades de Fomento" (UF) is the Chilean inflation-indexed unit of account; it is not translated. "recupero" (used in the accounting-date instruction) is rendered as "recovery" consistently with "recuperación" elsewhere in the document.

> **Source:** NCG 502 Anexo N°3 (12-ene-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/seccion-01-registro.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/seccion-01-registro.md

# NCG 502 — Sección I: Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

## I — Registry of Financial-Service Providers
**NCG anchor:** N° 502, Sección I
**Implements:** Ley 21.521 Art. 5 (registration obligation / Registry of Financial-Service Providers)
**Tags:** registration, psf, registry

### Plain-English text

This section governs the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) established by Article 5 of Ley 21.521. It comprises subsections A (registration application), B (cancellation of registration), and C (exceptions). It has no standalone body text of its own; the substantive rules begin at subsection A below.

### Original Spanish

> "I. REGISTRO DE PRESTADORES DE SERVICIOS FINANCIEROS"

### Cross-references
- Ley 21.521 Art. 5 — establishes the Registry of Financial-Service Providers, which this section implements.
- NCG 502 §I.A–§I.C — the subsections that make up this section.

> **Source:** NCG 502 §I (12-ene-2024).

---

## I.A — Registration Application
**NCG anchor:** N° 502, Sección I, A
**Implements:** Ley 21.521 Art. 5 (registration obligation) and Art. 6 (eligibility / ineligibility grounds, exclusive corporate purpose)
**Tags:** registration, psf, application, foreign-entity, exclusive-corporate-purpose

### Plain-English text

To provide the services regulated by Ley N° 21.521 in Chile, prior registration must be applied for in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) referred to in Article 5 of Ley N° 21.521. Those who materially carry out such services in the country — through the enabling or contracting of physical or electronic means to provide their services in the country — shall be understood to provide services in Chile, as shall those who employ any means of communication to direct the offering of their services to persons resident in Chile, regardless of the country of origin of those means.

For the purpose of applying for registration in the Registry, an application must be submitted through the specially enabled application (aplicación especialmente habilitada) on the Commission (CMF)'s website, which must be presented by the legal or conventional representative (representante legal o convencional) of the applicant, who shall be responsible for the truthfulness and integrity of all the information provided to the Commission (CMF).

Natural persons who carry out investment-advisory (asesoría de inversión) activity on behalf of and in representation of (i) a legal person registered in the Registry of Financial-Service Providers and authorized to provide the investment-advisory service, (ii) a bank, (iii) an insurance company, (iv) a securities broker-dealer (intermediario de valores), (v) a produce-exchange broker (corredor de bolsa de productos) under Ley N° 19.220, or (vi) a general fund manager (administradora general de fondos) or portfolio manager (administrador de carteras) under Ley N° 20.712, do not require registration or authorization for the provision of the investment-advisory service. The same applies to legal persons that carry out that activity on behalf of and in representation of those entities, provided that the natural persons from whom the recommendations issued by those legal persons emanate comply with the conditions established in NCG N° 503.

The said registration application must contain the following information:

a) Name or corporate name (razón social) of the person or entity and trade or commercial name (nombre de fantasía o comercial), where it has one.

b) National identity card (cédula de identidad) or passport number, or Unique Tax Roll (Rol Único Tributario).

c) Identification of the natural person (persona natural) empowered to act in conventional or legal representation in Chile of the person or entity: full name and national identity card or passport.

d) Telephone number.

e) Email address for the purposes of the notifications and communications made by this Commission (CMF).

f) Domicile (domicilio) in Chile, unless excepted from that requirement pursuant to this regulation.

g) URL of the website referred to in the first paragraph (inciso primero) of Article 5 of Ley N° 21.521.

In addition, the following supporting documents must accompany the application:

1. In the case of legal persons (personas jurídicas) incorporated in Chile (whether or not foreign-owned):

i. In the case of companies that are not subject to the simplified regime established in Ley N° 20.659 and registered in the Registry of Enterprises and Companies (Registro de Empresas y Sociedades) of the Ministry of Economy, Development and Tourism: a copy of the deed of incorporation and of the amending deeds of the last 10 years, of the registrations of the abstracts (extractos) of each of these, and of their publication in the Official Gazette (Diario Oficial), together with the company's certificate of good standing (certificado de vigencia) and a copy of the corporate registration evidencing the marginal annotations made, both no more than 15 days old counted from the date of the application. Where the company was incorporated less than 5 years ago and its founding shareholders are legal persons, the background documents evidencing their legal existence, corporate purpose, and capacity to form that company must be submitted. If any such document was granted abroad and is in a language other than Spanish, the applicant must accompany a translation duly certified by the legal or conventional representative. Where the applicant company was incorporated by virtue of a mandate granted by the founding shareholders, a copy of the public or private instrument evidencing the powers of the mandatary or mandataries to act in representation of those shareholders must be attached; if that instrument was granted abroad in a language other than Spanish, a duly certified translation must also be provided.

ii. In the case of companies subject to the simplified regime of Ley N° 20.659, it shall not be necessary to provide other supporting documents. Notwithstanding, where the company was incorporated less than 5 years ago and its founding shareholders are legal persons, the background documents evidencing their legal existence, corporate purpose, and capacity to form that company must be submitted. If any such document was granted abroad and is in a language other than Spanish, the applicant must accompany a translation duly certified by the legal or conventional representative. Where the applicant company was incorporated by virtue of a mandate granted by the founding shareholders, a copy of the public or private instrument evidencing the powers of the mandatary or mandataries to act in representation of those shareholders must be attached; if that instrument was granted abroad in a language other than Spanish, a duly certified translation must also be provided.

2. Entities incorporated abroad that will provide the services of Ley N° 21.521 without incorporating a company in Chile must establish an agency (agencia) and attach to the application a copy of the legalization, declaration, and abstract (extracto) referred to in Articles 121, 122, and 123 of Ley N° 18.046 or Articles 447, 448, and 449 of the Commercial Code (Código de Comercio), as applicable. Notwithstanding, where the exception contained in subparagraph C.3 below is relied upon, the declaration referred to in that subparagraph shall suffice.

3. Where the application is presented by a natural person (persona natural) acting as conventional representative of the person or entity giving rise to the application, a copy of the public or private document evidencing the corresponding power of attorney must accompany it. If that document was granted abroad and is in a language other than Spanish, the applicant must accompany a translation duly certified by the legal or conventional representative.

4. Declaration of not being subject to the disqualifications (inhabilidades) referred to in the second paragraph (inciso segundo) of Article 6 of Ley N° 21.521:

i. In the case of legal persons, when making the registration application, the natural person empowered to act on its behalf shall declare — identifying themselves by means of the electronic mechanism provided for those purposes on the Commission (CMF)'s website — that neither the entity nor its principal partners (socios principales), directors, or administrators are in any of the circumstances referred to in the second paragraph of Article 6 of Ley N° 21.521, in Chile or abroad.

ii. In the case of natural persons relying on the legal-personality exception (excepción de personalidad jurídica) contained in subparagraph C.1 of this section: a declaration made on the Commission (CMF)'s website, identifying themselves by means of the electronic mechanism provided for those purposes, that they are not in any of the circumstances referred to in the second paragraph of Article 6 of Ley N° 21.521, in Chile or abroad.

5. Certificate of Current Insolvency Proceedings / Bankruptcies (Certificado de Procedimientos Concursales Vigentes / Quiebras), issued by the Superintendency of Insolvency and Re-entrepreneurship (Superintendencia de Insolvencia y Reemprendimiento), evidencing that the person or entity whose registration is applied for is not in the bankruptcy registries, nor subject to an insolvency proceeding of liquidation, reorganization, or renegotiation, no more than 30 days old. In the case of agencies, this circumstance shall refer to the foreign entity and shall be declared on the same terms as those referred to in number 1) of number 4) above.

6. In the case of legal persons:

i. Identification of each principal partner, director, or administrator: full name, nationality, and identity card or passport number in the case of foreigners. By virtue of the provisions of the second paragraph of Article 6 of Ley N° 21.521, for these purposes a principal partner (socio principal) shall be understood to mean natural persons who directly or indirectly hold an interest equal to or greater than 10% of the capital, or who have the capacity to elect at least one member of the board of directors or management.

ii. Ownership structure of the business group (grupo empresarial) to which it belongs, indicating the principal businesses carried out by the companies of that group. For these purposes, the provisions of Article 96 of Ley N° 18.045 shall apply.

7. Summary of the business plan, expressly referring to the services of Title II of Ley N° 21.521, the inherent activities and the activities authorized by Commission (CMF) regulation that it intends to carry out, the expected income and expenditure, and the type of clients to whom the services it will provide are directed.

8. Organizational chart (organigrama), accompanied by a description of the principal functions of its areas, key positions, committees, and structure of responsibilities.

Once the application has been submitted and the completeness of the supporting documents required in this section has been verified, the entity will be registered in the Registry, subject to prior payment by the applicant of the fees established in Article 33 of D.L. N° 3.538. It should be noted that the foregoing does not entitle the entities to accompany graphic material owned by the Commission (CMF) in the dissemination of information, propaganda, or advertising that they carry out by any means, since this Commission (CMF) has registered the corresponding trademark and has the protection of Ley N° 19.039, in particular the provisions of Article 19 bis D, which empowers it to oppose the use that third parties may make of the said trademark.

Without prejudice to the foregoing, it is noted that, pursuant to Article 14(a) of Ley N° 21.521, it is a serious infringement (infracción grave) to provide the services regulated by that law without being registered in the registry or without having obtained the authorization to provide the services, and that among the aggravating circumstances referred to in Article 15 of the same law is feigning the status of being registered in the Registry or of being supervised by the Commission (CMF), which includes, among others, presenting oneself as regulated or giving the impression of being so by using graphic material owned by the Commission (CMF) in the dissemination of information, propaganda, or advertising that they carry out.

In the event that an application is incomplete or presented in such a way as to require a large number of corrections, the Commission (CMF) may request the entity to make a new submission.

In the event that, due to the applicant's inactivity, the procedure is halted for more than thirty days and action is taken in accordance with the provisions of Article 43 of Ley N° 19.880, which Establishes the Bases of the Administrative Procedures governing the acts of the organs of the State Administration, the registration application shall be deemed not to have been presented.

In the event that changes are made to the applicant's identification information referred to in subparagraphs a) and b) above, the communication through which such changes are reported to the Commission (CMF) must be accompanied by an application for annotation in the Registry, the fees established in Article 33 of D.L. N° 3.538 being payable. Consequently, together with registration in the Registry, the Commission (CMF) will grant the representative a username and password for the access and use of the system implemented by the Commission (CMF) for these purposes.

In accordance with the provisions of Article 6 of Ley N° 21.521, only the registration of legal persons whose exclusive corporate purpose (giro exclusivo) is the provision of one or more of the services regulated by Ley N° 21.521 and those activities that the Commission (CMF) has authorized by regulation shall proceed, which is why those who apply for their registration must have that sole corporate purpose (objeto social). The foregoing, with the exception of those who are in the circumstances and conditions established in subparagraph C of this section, for which they must accompany their registration application with the supporting documents required in that section.

> **TN:** NCG 524 inserted text mid-sentence here (an intercalación). The consolidated Spanish is faithful to NCG 502 as amended by NCG 524 (verified against the 524 source PDF), but its spliced wording does not appear as a contiguous passage in either single source PDF, so the automated dual-PDF round-trip cannot score it above threshold. This section is on the round-trip `--exclude` list and was verified manually.

### Original Spanish

> "A. SOLICITUD DE INSCRIPCIÓN
>
> Para prestar los servicios regulados por la Ley N°21.521 en Chile, se deberá solicitar la previa inscripción en el Registro de Prestadores de Servicios Financieros al que se refiere el artículo 5 de la Ley N° 21.521. Se entenderá que prestan servicios en Chile quienes materialmente los realicen en el país, a través de la habilitación o contratación de medios físicos o electrónicos para prestar sus servicios en el país, así como quienes empleen cualquier medio de comunicación para dirigir la oferta de sus servicios a personas residentes en Chile, independiente del país de origen de dichos medios.
>
> A efectos de solicitar la inscripción en el Registro, se deberá ingresar una solicitud a través de la aplicación especialmente habilitada en el sitio web de la Comisión, la que deberá ser presentada por el representante legal o convencional del solicitante, quien será el responsable de la veracidad e integridad de toda la información proporcionada a la Comisión.
>
> No requieren de inscripción ni autorización para la prestación del servicio de asesoría de inversión, las personas naturales que realicen dicha actividad por cuenta y en representación de (i) una persona jurídica inscrita en el Registro de Prestadores de Servicios Financieros y autorizada para prestar el servicio de asesoría de inversión, (ii) de un banco, (iii) de una compañía de seguros, (iv) de un intermediario de valores, (v) de un corredor de bolsa de productos de la Ley N°19.220, o (vi) de una administradora general de fondos o administradores de carteras de la ley N°20.712. Tampoco las personas jurídicas que realicen dicha actividad por cuenta y en representación de esas entidades y siempre que las personas naturales de las cuales emanen las recomendaciones que emitan esas personas jurídicas cumplan con las condiciones establecidas en la Norma de Carácter General N°503.
>
> La referida solicitud de inscripción deberá contener la siguiente información:
>
> a) Nombre o razón social de la persona o entidad y nombre de fantasía o comercial en caso de contar con uno.
>
> b) Número de cédula de identidad o pasaporte, o Rol Único Tributario.
>
> c) Identificación de la persona natural con poder para actuar en representación convencional o legal en Chile de la persona o entidad: nombre completo y cédula nacional de identidad o pasaporte.
>
> d) Número de Teléfono.
>
> e) Dirección de correo electrónico para efectos de las notificaciones y comunicaciones que practique esta Comisión.
>
> f) Domicilio en Chile, salvo que se haya exceptuada al efecto mediante esta norma.
>
> g) URL del sitio web al que se refiere el inciso primero del artículo 5 de la Ley N°21.521.
>
> Además, junto a la solicitud, se deberán acompañar los siguientes antecedentes:
>
> 1. Tratándose de personas jurídicas constituidas en Chile (sean o no de propiedad de extranjeros):
>
> i. En el caso de sociedades que no estén sometidas al régimen simplificado establecido en la Ley N°20.659 e inscritas en el Registro de Empresas y Sociedades del Ministerio de Economía, Fomento y Turismo, copia de la escritura de constitución y de las escrituras modificatorias de los últimos 10 años, de las inscripciones de los extractos de cada una de éstas, y de la publicación de éstos en el Diario Oficial, junto con el certificado de vigencia de la sociedad y una copia de la inscripción social con constancia de las anotaciones marginales practicadas, ambos de una antigüedad inferior a 15 días contados desde la fecha de la solicitud.
> En caso de sociedades cuya constitución sea menor a 5 años y en que los accionistas constituyentes sean personas jurídicas, deberán remitirse los antecedentes en que conste su vigencia, objeto, y capacidad para formar dicha sociedad. Para el caso en que el documento hubiese sido otorgado en el extranjero, y si este fuese extendido en un idioma distinto al español, el solicitante deberá acompañar una traducción debidamente certificada por el representante legal o convencional.
> Para el caso en que la sociedad solicitante hubiese sido constituida en virtud de un mandato otorgado por los socios o accionistas constituyentes, deberá acompañar copia del instrumento público o privado en que consten las facultades del o los mandatarios para actuar en representación de los primeros, y si este hubiese sido otorgado en el extranjero, en un idioma distinto al español, el solicitante deberá acompañar una traducción debidamente certificada por el representante legal o convencional.
>
> ii. En el caso de sociedades sometidas al régimen simplificado de la Ley N°20.659, no será necesario acompañar otros antecedentes.
> No obstante, en caso de sociedades cuya constitución sea menor a 5 años y en que los accionistas constituyentes sean personas jurídicas, deberán remitirse los antecedentes en que conste su vigencia, objeto, y capacidad para formar dicha sociedad. Para el caso en que el documento hubiese sido otorgado en el extranjero, y si este fuese extendido en un idioma distinto al español, el solicitante deberá acompañar una traducción debidamente certificada por el representante legal o convencional.
> Para el caso en que la sociedad solicitante hubiese sido constituida en virtud de un mandato otorgado por los socios o accionistas constituyentes, deberá acompañar copia del instrumento público o privado en que consten las facultades del o los mandatarios para actuar en representación de los primeros, y si este hubiese sido otorgado en el extranjero, en un idioma distinto al español, el solicitante deberá acompañar una traducción debidamente certificada por el representante legal o convencional.
>
> 2. Las entidades constituidas en el extranjero y que prestarán los servicios de la Ley N°21.521 sin constituir una sociedad en Chile, deberán establecer una agencia y adjuntar a la solicitud copia de la legalización, declaración y extracto a que se refieren los artículos 121, 122 y 123 de la Ley N°18.046 o los artículos 447, 448 y 449 del Código de Comercio según corresponda. No obstante, en el caso de acogerse a la excepción contenida en la letra C.3 siguiente, bastará con la declaración a la que se refiere esa letra.
>
> 3. En caso de que la solicitud la presente una persona natural en calidad de representante convencional de la persona o entidad que motiva la solicitud, deberá acompañar copia del documento público o privado en el que consta el poder correspondiente. Para el caso en que el documento hubiese sido otorgado en el extranjero, y si este fuese extendido en un idioma distinto al español, el solicitante deberá acompañar una traducción debidamente certificada por el representante legal o convencional.
>
> 4. Declaración de no estar afecto a las inhabilidades a que se refiere el inciso segundo del artículo 6 de la Ley N°21.521:
>
> i. En el caso de personas jurídicas, al efectuar la solicitud de inscripción la persona natural facultada para actuar por ésta declarará, identificándose mediante el mecanismo electrónico dispuesto para esos efectos en el sitio en Internet de la Comisión, que ni la entidad ni sus socios principales, directores o administradores se encuentran en alguna de las circunstancias a las que se refiere el inciso segundo del artículo 6 de la Ley N°21.521, en Chile ni en el extranjero.
>
> ii. En el caso de personas naturales que se acojan a la excepción de personalidad jurídica contenida en la letra C.1 de esta sección, declaración efectuada en el sitio en Internet de la Comisión, identificándose mediante el mecanismo electrónico dispuesto para esos efectos, respecto a que no se encuentra en alguna de las circunstancias a las que se refiere el inciso segundo del artículo 6 de la Ley N°21.521, en Chile ni en el extranjero.
>
> 5. Certificado de Procedimientos Concursales Vigentes / Quiebras, emitido por la Superintendencia de Insolvencia y Reemprendimiento, en el que conste que la persona o entidad cuya inscripción se solicita no se encuentra en los registros de quiebra, ni está sometida a un procedimiento concursal de liquidación, reorganización o renegociación, de una antigüedad igual o inferior a los 30 días. En el caso de agencias dicha circunstancia estará referida a la entidad extranjera y se declarará en los mismos términos al que se refiere el número 1) del número 4) anterior.
>
> 6. En el caso de personas jurídicas:
>
> i. Identificación de cada socio principal, director o administrador: nombre completo, nacionalidad, y cédula de identidad o número de pasaporte en caso de extranjeros. En virtud de lo señalado en el inciso segundo del artículo 6 de la Ley N°21.521, para estos efectos se entenderá como socio principal a las personas naturales que posean directa o indirectamente una participación igual o superior al 10% del capital o tengan la capacidad de elegir a lo menos un miembro del directorio o administración.
>
> ii. Estructura de propiedad del grupo empresarial al que pertenece, indicando los principales negocios que realizan las empresas de ese grupo. Para estos efectos, debe estarse a lo establecido en el artículo 96 de la Ley N°18.045.
>
> 7. Síntesis del plan de negocios, refiriéndose expresamente a los servicios del Título II de la Ley N°21.521, las actividades inherentes y las actividades autorizadas por normativa de la Comisión que pretende llevar a cabo, los ingresos y egresos esperados y tipo de clientes a los cuales se encuentran dirigidos los servicios que prestará.
>
> 8. Organigrama, acompañado con una descripción de las principales funciones de sus áreas, cargos claves, comités y estructura de responsabilidades.
>
> Ingresada la solicitud y verificada la completitud de los antecedentes requeridos en la presente sección, se procederá a la inscripción de la entidad en el Registro, previo pago por parte del solicitante de los derechos establecidos en el artículo 33 del D.L. N°3.538. Cabe señalar que lo anterior no habilita a las entidades a acompañar material gráfico de propiedad de la Comisión en la divulgación de información, propaganda o publicidad que efectuaren por cualquier medio, por cuanto esta Comisión ha registrado la marca comercial correspondiente y cuenta con la protección de la Ley N°19.039, en especial lo dispuesto en el artículo 19 bis D, que la faculta para oponerse al uso que puedan hacer terceros de la mencionada marca comercial.
>
> Sin perjuicio de lo anterior se hace presente que, conforme al artículo 14 letra a) de la Ley N°21.521, es una infracción grave el prestar los servicios regulados por esa Ley sin estar inscrito en el registro o sin haber obtenido la autorización para prestar los servicios y que entre los agravantes a los que se refiere el artículo 15 de la misma Ley se encuentra el fingir la calidad de inscrito en el Registro o de supervisado por la Comisión, lo cual incluye, entre otros, el presentarse como regulado o dar la impresión de serlo utilizando material gráfico de propiedad de la Comisión en la divulgación de información, propaganda o publicidad que realizaren.
>
> Para el evento que una solicitud se encuentre incompleta o presentada de tal forma que requiera un gran número de correcciones, la Comisión podrá solicitar a la entidad que efectúe una nueva presentación.
>
> En el evento de que por la inactividad del solicitante se produzca por más de treinta días la paralización del procedimiento y se proceda conforme a lo dispuesto en el artículo 43 de la Ley N°19.880 que Establece Bases de los Procedimientos Administrativos que rigen los actos de los órganos de la Administración del Estado, se entenderá por no presentada la solicitud de inscripción.
>
> En caso de que se efectúen cambios a la información de identificación del solicitante a que se refieren las letras a) y b) anteriores, la comunicación mediante la cual éstos se informen a la Comisión deberá ser acompañada de una solicitud de anotación en el Registro, debiéndose pagar los derechos establecidos en el artículo 33 del D.L. N°3.538. Por consiguiente, junto con la inscripción en el Registro, la Comisión otorgará al representante un nombre de usuario y contraseña para el acceso y utilización del sistema implementado por la Comisión para estos efectos.
>
> De conformidad con lo establecido en el artículo 6 de la Ley N°21.521, sólo procederá la inscripción de personas jurídicas cuyo giro exclusivo sea la prestación de uno o más los servicios regulados por la Ley N°21.521 y aquellas actividades que la Comisión haya autorizado por normativa, razón por la que quienes soliciten su inscripción deberán tener ese sólo objeto social. Lo anterior, con la excepción de quienes se encuentren en las circunstancias y condiciones establecidas en la letra C de esta sección, para lo cual deberán acompañar a su solicitud de inscripción los antecedentes exigidos en dicha sección."

> **TN:** "representante legal o convencional" is rendered "legal or conventional representative" — "conventional" (i.e., representation arising by agreement/power of attorney, as opposed to statutory/legal representation) tracks the Spanish civil-law distinction; the Spanish is preserved in parens on first use.

> **TN:** "infracción grave" is rendered "serious infringement" to match the Ley 21.521 sanctions terminology (Art. 14); the alternative "gross infringement" was not used.

### Cross-references
- Ley 21.521 Art. 5 — establishes the Registry of Financial-Service Providers and the registration obligation that this subsection operationalizes.
- Ley 21.521 Art. 6 — eligibility, the second-paragraph disqualifications declared under item 4, and the exclusive-corporate-purpose rule.
- Ley 21.521 Art. 13 — grounds the cancellation framework in §I.B (cross-referenced from the exclusive-purpose closing paragraph).
- Ley 21.521 Art. 14–15 — serious infringements and aggravating circumstances referenced in the trademark / feigned-status paragraph.
- NCG 502 §I.C (and §I.C.1, §I.C.2, §I.C.3) — the exceptions to the legal-person, exclusive-purpose, and Chilean-domicile requirements referenced in items 2, 4(ii), and the closing paragraph.

> **Source:** NCG 502 §I.A (12-ene-2024), as amended by NCG 524 items 1, 2, 3, 4, 5, 6, 7 (02-dic-2024).

---

## I.B — Cancellation of Registration
**NCG anchor:** N° 502, Sección I, B
**Implements:** Ley 21.521 Art. 5 (registration obligation) and Art. 13 (cancellation of registration)
**Tags:** cancellation, psf, registry, ex-officio, insolvency

### Plain-English text

For the purpose of requesting its cancellation from the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros), an application for cancellation signed by the representative of the entity must be sent to the Commission (CMF). In the case of legal persons (personas jurídicas), from that cancellation the corresponding amendment of the bylaws (reforma de estatutos) must be carried out in order to adapt the corporate purpose (objeto social) to services that are neither regulated nor subject to the registration obligation.

The foregoing is without prejudice that this Commission (CMF) may proceed with the ex-officio cancellation (cancelación de oficio) of the registration of those who, in accordance with the provisions of Article 13 of Ley N° 21.521, have not applied for the authorization to carry out any of the activities regulated by that law within the period of twelve months counted from the corresponding registration, as well as of those who, over a continuous period of 12 months, have not carried out the activities for which they were authorized.

Likewise, the Commission (CMF) will proceed with the cancellation of the registration in the Registry of those entities that come to have the status of debtor in an insolvency proceeding of liquidation (procedimiento concursal de liquidación), in accordance with the provisions of Article 13 of Ley N° 21.521, or in those cases in which the entity has been sanctioned for the serious infringements (infracciones graves) referred to in Article 14 of the same law; or of those that cease to comply with any of the requirements by virtue of which their registration was carried out.

### Original Spanish

> "B. CANCELACIÓN DE LA INSCRIPCIÓN
>
> Para efectos de requerir su cancelación del Registro de Prestadores de Servicios Financieros, se deberá remitir a la Comisión una solicitud de cancelación suscrita por el representante de la entidad. En el caso de personas jurídicas, a partir de dicha cancelación deberá procederse con la correspondiente reforma de estatutos para adecuar el objeto social a servicios que no estén regulados ni sometidos a obligación de inscripción.
>
> Lo anterior, sin perjuicio que esta Comisión pueda proceder a la cancelación de oficio de la inscripción de quienes, conforme a lo dispuesto en el artículo 13 de la Ley N° 21.521, no hubieren solicitado la autorización para realizar alguna de las actividades reguladas por dicha Ley dentro del plazo de doce meses contado desde la inscripción correspondiente, así como también de quienes en un periodo de 12 meses continuos no hubieren realizado las actividades que les fueron autorizadas.
>
> Asimismo, la Comisión procederá a la cancelación de la inscripción en el Registro de aquellas entidades que pasen a tener la calidad de deudor en un procedimiento concursal de liquidación, de conformidad a lo prescrito en el artículo 13 de la Ley N° 21.521, o en aquellos casos en que la entidad hubiere sido sancionada por las infracciones graves a que se refiere el artículo 14 de la misma Ley; o, de aquellas que dejen de cumplir con alguno de los requisitos en virtud de los cuales se procedió con su inscripción."

### Cross-references
- Ley 21.521 Art. 13 — the cancellation grounds (failure to obtain authorization within twelve months, twelve-month inactivity, insolvency-liquidation debtor status) that this subsection implements.
- Ley 21.521 Art. 14 — serious infringements whose sanction triggers cancellation.
- NCG 502 §I.A — registration whose conditions, once breached, ground cancellation; and §II (authorization to provide services) — the authorization whose non-request within twelve months grounds ex-officio cancellation.

> **Source:** NCG 502 §I.B (12-ene-2024).

---

## I.C — Exceptions
**NCG anchor:** N° 502, Sección I, C
**Implements:** Ley 21.521 Art. 4 (CMF power to grant exceptions) and Art. 6 (requirements being excepted)
**Tags:** exceptions, psf, registry

### Plain-English text

This subsection sets out the exceptions, granted under Article 4 of Ley N° 21.521, to certain registration requirements. It comprises subparagraph C.1 (exception to the legal-person requirement), C.2 (exception to the exclusive-corporate-purpose requirement, as amended by NCG 524), and C.3 (exception to the Chilean-domicile requirement, as amended by NCG 524). It has no standalone body text of its own; the exceptions begin at subparagraph C.1 below.

### Original Spanish

> "C. EXCEPCIONES"

### Cross-references
- Ley 21.521 Art. 4 — the power under which the Commission (CMF) grants these exceptions.
- NCG 502 §I.A — the registration requirements from which these exceptions derogate.
- NCG 502 §I.C.1, §I.C.2, §I.C.3 — the specific exceptions that make up this subparagraph.

> **Source:** NCG 502 §I.C (12-ene-2024).

---

## I.C.1 — On the Legal-Person Requirement
**NCG anchor:** N° 502, Sección I, C.1
**Implements:** Ley 21.521 Art. 4 (CMF exception) and Art. 6 (legal-person requirement)
**Tags:** exceptions, legal-person, investment-advisory, declaration

### Plain-English text

By virtue of the provisions of Article 4 of Ley N° 21.521, natural persons (personas naturales) who engage solely in the provision of the investment advisory (asesoría de inversión) service are excepted from the requirement of being incorporated as a legal person (persona jurídica) for the purpose of applying for their registration in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros), provided that they meet the following cumulative requirements (requisitos copulativos):

a) That they provide advisory services only to specific persons (personas determinadas); and

b) That the number of specific persons to whom they provided advisory services through any of the means it uses for that purpose, including social networks, in the last twelve months, does not exceed 100,000 persons.

To evidence this circumstance, it shall suffice for the person to make the declaration through the Commission (CMF)'s website, by means of the electronic mechanism provided for those purposes. Such declaration must be updated every 12 months from the date of registration.

### Original Spanish

> "C.1. DEL REQUISITO DE PERSONA JURÍDICA
>
> En virtud de lo establecido en el artículo 4° de la Ley N° 21.521, se exceptúa del requisito de constituirse como persona jurídica a efectos de solicitar su inscripción en el Registro de Prestadores de Servicios Financieros a las personas naturales que sólo se dediquen a la prestación del servicio de asesoría de inversión, y siempre que cumplan los siguientes requisitos copulativos:
>
> a) Que sólo efectúen asesorías a personas determinadas; y
>
> b) Que el número de personas determinadas a las que efectuaron asesorías por medio de cualesquiera de los medios que emplea para ese efecto, incluidas redes sociales, en los últimos doce meses, no supere las 100.000 personas.
>
> Para acreditar esta circunstancia, bastará con la declaración que efectúe la persona a través del sitio en Internet de la Comisión, mediante el mecanismo electrónico dispuesto para esos efectos. Dicha declaración deberá actualizarse cada 12 meses a partir de la fecha de inscripción."

### Cross-references
- Ley 21.521 Art. 4 — the exception power exercised here.
- Ley 21.521 Art. 6 — the legal-person requirement from which this subparagraph derogates.
- NCG 502 §I.A item 4(ii) — the disqualification declaration applicable to natural persons relying on this exception.

> **Source:** NCG 502 §I.C.1 (12-ene-2024).

---

## I.C.2 — On the Exclusive Corporate Purpose
**NCG anchor:** N° 502, Sección I, C.2
**Implements:** Ley 21.521 Art. 4 (CMF exception); relates to Art. 6 (exclusive corporate purpose)
**Tags:** exceptions, exclusive-corporate-purpose, qualified-investors, declaration

### Plain-English text

By virtue of the provisions of Article 4 of Ley N° 21.521, those who meet the following cumulative circumstances (circunstancias copulativas) are excepted from the exclusive-corporate-purpose (giro exclusivo) requirement for the purpose of applying for their registration in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros):

a) That, among the services regulated by Ley N° 21.521, they provide only the service of investment advisory (asesoría de inversión), credit advisory (asesoría crediticia), order routing (enrutadores de órdenes), alternative trading system (sistema alternativo de transacción), and crowdfunding platform (plataforma de financiamiento colectivo).

b) That the provision of the services regulated by this regulation be provided only to qualified investors (inversionistas calificados) referred to in subparagraph f) of Article 4 Bis of Ley N° 18.045.

To rely on this exception, the applicant must make a declaration regarding the fact that it will comply with the circumstances described above. Such declaration must be made through the electronic mechanism provided for the submission of the registration application, on the Commission (CMF)'s website. In addition, such declaration must be updated annually through the mechanism established for that purpose on the Commission (CMF)'s website.

Likewise, those who have availed themselves of the Chilean-domicile exception referred to in subparagraph C.3 below shall also be exempt from the exclusive-corporate-purpose requirement.

> **TN:** NCG 524 inserted text mid-sentence here (an intercalación). The consolidated Spanish is faithful to NCG 502 as amended by NCG 524 (verified against the 524 source PDF), but its spliced wording does not appear as a contiguous passage in either single source PDF, so the automated dual-PDF round-trip cannot score it above threshold. This section is on the round-trip `--exclude` list and was verified manually.

### Original Spanish

> "C.2. DEL GIRO EXCLUSIVO
>
> En virtud de lo establecido en el artículo 4° de la Ley N°21.521 se exceptúa del requisito de giro exclusivo a efectos de solicitar su inscripción en el Registro de Prestadores de Servicios Financieros, a quienes cumplan las siguientes circunstancias copulativas:
>
> a) Que, entre los servicios regulados por la Ley N°21.521, sólo presten el servicio de asesoría de inversión, asesoría crediticia, enrutadores de órdenes, sistema alternativo de transacción y plataforma de financiamiento colectivo.
>
> b) Que la prestación de los servicios regulados por esta normativa sólo sea provista a inversionistas calificados a los que se refiere la letra f) del artículo 4 Bis de la Ley N°18.045.
>
> Para acogerse a esta excepción, el solicitante deberá efectuar una declaración respecto del hecho que dará cumplimiento a las circunstancias antes descritas. Dicha declaración, deberá ser efectuada a través del mecanismo electrónico dispuesto para el ingreso de la solicitud de inscripción, en el sitio en Internet de la Comisión. Además, dicha declaración deberá ser actualizada anualmente a través del mecanismo establecido para ello en el sitio en Internet de la Comisión.
>
> A su vez, quedarán eximidos del requisito de giro exclusivo, quienes se hayan acogido a la excepción de domicilio en Chile a que se refiere la sección C.3 siguiente."

### Cross-references
- Ley 21.521 Art. 4 — the exception power exercised here.
- Ley 21.521 Art. 6 — the exclusive-corporate-purpose requirement from which this subparagraph derogates.
- Ley 18.045 Art. 4 Bis(f) — the definition of qualified investor (inversionista calificado) used in condition b).
- NCG 502 §I.C.3 — the parallel exception for foreign entities lacking Chilean domicile, on the same qualified-investor condition.

> **Source:** NCG 502 §I.C.2 (12-ene-2024), as amended by NCG 524 items b.1, b.2, b.3 (02-dic-2024).

---

## I.C.3 — On Chilean Domicile
**NCG anchor:** N° 502, Sección I, C.3
**Implements:** Ley 21.521 Art. 4 (CMF exception); relates to Art. 6 (domicile requirement)
**Tags:** exceptions, foreign-entity, domicile, qualified-investors, declaration

### Plain-English text

By virtue of the provisions of Article 4 of Ley N° 21.521, foreign entities are excepted from the requirement of having a domicile (domicilio) in Chile for the purpose of applying for their registration in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros), in the following cumulative circumstances (circunstancias copulativas):

a) That, in the last 10 years counted from the date of submission of the authorization application, those entities have not been sanctioned or do not have charges formulated against them for the serious infringements (infracciones graves) referred to in Article 14 of Ley N° 21.521, or abroad for equivalent conduct. In the case of a legal person, this requirement shall be considered with respect to the entities that form part of its business group (grupo empresarial) in the terms contemplated in Article 96 of Ley N° 18.045 on Securities Markets, as well as its controllers, principal shareholders or partners, directors, administrators, and managers, as at the date of the application; and

b) That the provision in Chile of the services regulated by this regulation be provided only to qualified investors (inversionistas calificados) referred to in subparagraph f) of Article 4 Bis of Ley N° 18.045.

To rely on this exception, the applicant must, at the time of applying for registration in the Registry, make a declaration regarding the fact that it will comply with the circumstances described above, and that, in the face of any modification to the same, it will cease to provide the services of Ley N° 21.521 while it has not obtained the corresponding authorization from this Commission (CMF). Such declaration must be made through the electronic mechanism provided for the submission of the registration application, on the Commission (CMF)'s website. In addition, such declaration must be updated annually through the mechanism established for that purpose on the Commission (CMF)'s website.

### Original Spanish

> "C.3. DEL DOMICILIO EN CHILE
>
> En virtud de lo establecido en el artículo 4° de la Ley N° 21.521 se exceptúa a las entidades extranjeras del requisito de contar con domicilio en Chile a efectos de solicitar su inscripción en el Registro de Prestadores de Servicios Financieros, en las siguientes circunstancias copulativas:
>
> a) Que, en los últimos 10 años desde la fecha de ingreso de la solicitud de autorización, esas entidades no hayan sido sancionadas o se encuentren formulados de cargos por las infracciones graves a que se refiere el artículo 14 de la Ley N°21.521, o en el extranjero por conductas equivalentes. Tratándose de una persona jurídica, este requisito se considerará respecto de las entidades que formen parte de su grupo empresarial en los términos contemplados en el artículo 96 de la Ley N°18.045 de Mercado de Valores, así como de sus controladores, socios o accionistas mayoritarios, directores, administradores y gerentes, a la fecha de la solicitud; y
>
> b) Que la prestación en Chile de los servicios regulados por esta normativa sólo sea provista a inversionistas calificados a los que se refiere la letra f) del artículo 4 Bis de la Ley N°18.045.
>
> Para acogerse a esta excepción el solicitante, al momento de solicitar la inscripción en el Registro, deberá efectuar una declaración respecto del hecho que cumple las circunstancias antes descritas y que, frente a cualquier modificación de las mismas, dejará de prestar los servicios de la Ley N°21.521 mientras no haya obtenido la autorización respectiva por parte de esta Comisión. Dicha declaración deberá ser efectuada a través del mecanismo electrónico dispuesto para el ingreso de la solicitud de inscripción, en el sitio en Internet de la Comisión. Además, dicha declaración deberá ser actualizada anualmente a través del mecanismo establecido para ello en el sitio en Internet de la Comisión."

### Cross-references
- Ley 21.521 Art. 4 — the exception power exercised here.
- Ley 18.045 Art. 4 Bis(f) — the definition of qualified investor (inversionista calificado) used in condition b).
- NCG 502 §I.A item 2 — the foreign-entity agency requirement, which this exception relieves (the C.3 declaration suffices in lieu of establishing an agency).
- NCG 502 §I.C.2 — the parallel exception to the exclusive-corporate-purpose requirement on the same qualified-investor condition.

> **Source:** NCG 502 §I.C.3 (12-ene-2024), as amended by NCG 524 items c.1, c.2 (02-dic-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/seccion-02-autorizacion.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/seccion-02-autorizacion.md

# NCG 502 — Sección II: Authorization for the Provision of Services (Autorización para la Prestación de Servicios)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

## II — Authorization for the Provision of Services
**NCG anchor:** N° 502, Sección II
**Implements:** Ley 21.521 Art. 7 (per-service authorization requirement)
**Tags:** authorization, psf, services

### Plain-English text

Prior to providing any of the services regulated by Title II of Ley N° 21.521, entities must apply to this Commission (CMF) for authorization, which may be submitted together with the application for registration in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) or once they are already registered therein. For these purposes, they must submit the relevant application through the specially enabled application (aplicación especialmente habilitada) on the Commission (CMF)'s website, which must be presented by the legal or conventional representative (representante legal o convencional) of the applicant, who shall be responsible for the truthfulness and integrity of all the information provided to the Commission (CMF).

Said application must expressly indicate the service or services for which authorization is sought and must be accompanied by the supporting documents indicated below according to the service in question. The manuals, descriptions, and internal regulations requested in this section must be submitted in Spanish or English, expressly indicating in them where applicable that they correspond to a translation of the original.

In the event that an application is incomplete or presented in such a way as to require a large number of corrections, the Commission (CMF) may require the applicant to make a new submission, treating the previously submitted application as not having been presented.

In the event that, due to the applicant's inactivity, the proceeding is halted for more than thirty days and action is taken in accordance with the provisions of Article 43 of Ley N° 19.880 which Establishes the Bases of the Administrative Procedures governing the acts of the organs of the State Administration, the authorization application shall be deemed not to have been presented.

In the event that, after processing the authorization application, it is rejected for all the services for which it was sought, the registration in the Registry of Financial-Service Providers of those who do not hold another authorization in force as of that date shall be cancelled.

This section comprises subsections A (investment advisory), B (credit advisory), C (crowdfunding platform), D (alternative trading system), E (order routing), F (intermediation and custody of financial instruments), and G (exception to the authorization requirement and compliance obligations).

### Original Spanish

> "II. AUTORIZACIÓN PARA LA PRESTACIÓN DE SERVICIOS
>
> Previo a prestar cualesquiera de los servicios regulados por el Título II de la Ley N°21.521, las entidades deberán solicitar la autorización de esta Comisión, la cual podrá ser presentada junto con la solicitud de inscripción en el Registro de Prestadores de Servicios Financieros o una vez inscritas en el mismo. Para estos efectos, deberán remitir la solicitud respectiva a través de la aplicación especialmente habilitada para ello en el sitio web de la Comisión, la que deberá ser presentada por el representante legal o convencional del solicitante, quien será el responsable de la veracidad e integridad de toda la información proporcionada a la Comisión.
>
> Dicha solicitud deberá señalar expresamente el o los servicios para los cuales solicita autorización y ser acompañada de los antecedentes que se indican más adelante según el servicio del que se trate. Los manuales, descripciones y reglamentación interna que se solicitan en esta Sección deberán ser presentados en idioma español o inglés, señalando expresamente en los mismos el caso que estos correspondan a una traducción del original.
>
> Para el evento que una solicitud se encuentre incompleta o presentada de tal forma que requiera un gran número de correcciones, la Comisión podrá requerir al solicitante que efectúe una nueva presentación, entendiendo como no presentada la ingresada con anterioridad.
>
> En el evento de que por la inactividad del solicitante se produzca por más de treinta días la paralización del procedimiento y se proceda conforme a lo dispuesto en el artículo 43 de la Ley N°19.880 que Establece Bases de los Procedimientos Administrativos que rigen los actos de los órganos de la Administración del Estado, se entenderá por no presentada la solicitud de autorización.
>
> En el caso que luego de tramitada la referida solicitud de autorización, la misma sea rechazada para todos los servicios que se hubiere solicitado, se procederá a la cancelación de la inscripción en el Registro de Prestadores de Servicios Financieros de quienes no tuvieren otra autorización vigente a esa fecha."

### Cross-references
- Ley 21.521 Art. 7 — per-service authorization mandate that this section operationalizes.
- Ley 21.521 Art. 13 — cancellation of registration upon rejection of all authorization applications.
- Ley N° 19.880 Art. 43 — administrative inactivity rule applied to halted authorization proceedings.
- NCG 502 §I — registration in the Registry of Financial-Service Providers, which may accompany or precede the authorization application.
- NCG 502 §II.A–§II.G — the subsections setting out per-service authorization requirements and the general exception.

> **Source:** NCG 502 §II (12-ene-2024), as amended by NCG 524 items B.1, B.2 (02-dic-2024).

---

## II.A — Investment Advisory
**NCG anchor:** N° 502, Sección II, A
**Implements:** Ley 21.521 Art. 7 (per-service authorization)
**Tags:** authorization, investment-advisory, psf

### Plain-English text

The authorization application for the investment advisory (asesoría de inversión) service must be accompanied by the following supporting documents:

a) Identification of the channels through which it will interact with clients or the public, indicating, as applicable:

1. The usernames or aliases (apodos) it uses to identify itself in those channels.

2. The applications that must be used to access those channels and on which platform they are supported.

3. In the case of physical channels, the address or addresses at which such interaction takes place.

4. Whether the provision of the investment advisory service will be directed to specific and determined clients (clientes específicos y determinados) and/or to the public in general.

5. The URL address or mechanism through which the information referred to in subparagraphs a) and b) of the first paragraph of Section III.A of this regulation can be accessed.

b) Document containing the policies referred to in subparagraph A of Section IV of this regulation that are applicable to it in accordance with what is established in subparagraph A.4 of that section. To rely on any of the exceptions referred to in subparagraph A.4, the applicant must declare the conditions that justify the exception.

c) Document with the general description of the procedure and manner in which the service will be provided, indicating those parts of the process that are carried out by natural persons or by computer algorithms, and which parts use the applicant's own resources, subcontracted resources, or resources acquired from third parties. When referring to the parts of the process carried out by such algorithms, it must describe in general terms the operation of the algorithm, clearly indicating the degree of automation and human intervention required.

d) In the case where investment recommendations (recomendaciones de inversión) emanate from a computer algorithm without human intervention, the certificate of knowledge accreditation (certificado de acreditación de conocimientos) of at least one person responsible for the verification and validation process of said algorithm must be attached — with respect to whether its design and execution comply with the standards of coherence, consistency, and objectivity between the data entered into the algorithm, the recommendations obtained from it, and the needs expressed by the clients who contract such services — in accordance with the requirements established in Norma de Carácter General N° 503.

e) In the case where investment recommendations emanate from natural persons, the certificate of knowledge accreditation of at least one such person must be attached, independently of the contractual relationship that such person maintains with the applicant entity, in accordance with the requirements established in Norma de Carácter General N° 503. In the case of natural persons who avail themselves of what is set out in Section I of Norma de Carácter General N° 503 — with respect to the conditions that allow them to exceptionally perform their functions on a temporary basis without having passed the knowledge accreditation examination — express mention of that fact must be made.

> **TN:** NCG 524 inserted text mid-sentence here (intercalación): "independiente de la relación contractual que mantenga con la entidad solicitante," was inserted in literal e) between the expressions "emanen de personas naturales," and "se deberá acompañar". The consolidated Spanish is faithful (verified against the 524 PDF) but its spliced wording is not a contiguous passage in either single source PDF, so this section is on the round-trip --exclude list and was verified manually.

The natural persons referred to in the preceding two subparagraphs — that is, those responsible for the verification and validation of the algorithms and those from whom investment recommendations emanate — prior to performing any of those functions must have passed a professional or technical academic program, whether national or foreign, in matters related to the financial market, its operation, legal framework, participants, or instruments, with a duration of at least 4 semesters. The foregoing must be accredited jointly and in the same terms established in subparagraphs d) and e), by attaching a document evidencing that the person on whom supporting documentation is requested in each of those subparagraphs has passed the said academic program.

### Original Spanish

> "A. ASESORÍA DE INVERSIÓN
>
> a) Identificación de los canales mediante los que interactuará con clientes o el público, indicando, en lo que corresponda:
>
> 1) Los nombres de usuario o apodos que emplea para identificarse en esos canales.
>
> 2) Las aplicaciones que se deben emplear para acceder a esos canales y en qué plataforma se soportan.
>
> 3) En caso de canales físicos, el o los domicilios en que se da esa interacción.
>
> 4) Si la prestación del servicio de asesoría de inversión estará dirigida a clientes específicos y determinados y/o al público en general.
>
> 5) La dirección URL o mecanismo en que se puede acceder a la información a que se refieren los literales a) y b) del primer párrafo de la sección III.A de esta normativa.
>
> b) Documento que contenga las políticas a que se refiere la letra A de la Sección IV de esta normativa que le resulten aplicables conforme a lo establecido en la letra A.4 de esa sección. Para acogerse a alguna de las excepciones a las que se refiere esa letra A.4 deberá declarar las condiciones que justifican la excepción.
>
> c) Documento con la descripción general del procedimiento y forma en que se prestará el servicio, indicando aquellas partes del proceso que son realizados por personas o por algoritmos informáticos, y cuáles con recursos propios, subcontratados o adquiridos a terceros. Al referirse a las partes del proceso que son realizadas por esos algoritmos, deberá describir en términos generales el funcionamiento del mismo, indicando claramente el grado de automatización e intervención humana requerido.
>
> d) En el caso de que las recomendaciones de inversión emanen de un algoritmo informático, sin intervención humana, se deberá acompañar el certificado de acreditación de conocimientos de al menos una persona responsable del proceso de verificación y validación de dicho algoritmo, en cuanto a que su diseño y ejecución cumpla con los estándares de coherencia, consistencia y objetividad entre los datos ingresados al algoritmo, las recomendaciones que se obtengan de este, y las necesidades manifestadas por los clientes que contratan dichos servicios, conforme a las exigencias establecidas en la Norma de Carácter General N°503.
>
> e) En el caso que las recomendaciones de inversión emanen de personas naturales, se deberá acompañar el certificado de acreditación de conocimientos de al menos una de esas personas, independiente de la relación contractual que mantenga con la entidad solicitante, conforme a las exigencias establecidas en la Norma de Carácter General N°503. Tratándose de personas naturales que se acojan a lo dispuesto en la sección I de la Norma de Carácter General N°503, respecto a las condiciones que le permitan desempeñarse excepcionalmente sus funciones de manera temporal sin haber aprobado el examen de acreditación de conocimientos, se deberá hacer expresa mención a ese hecho.
>
> Las personas naturales a las que se refieren las dos letras anteriores, es decir, las personas naturales responsables de la verificación y validación de los algoritmos y aquellas de las cuales emanan las recomendaciones de inversión, previo a desempeñar alguna de aquellas funciones deberán haber aprobado un programa académico de carácter profesional o técnico, nacional o extranjero, sobre materias relacionadas con el mercado financiero, su funcionamiento, marco jurídico, participantes o instrumentos, de una duración de al menos 4 semestres. Lo anterior deberá acreditarse en conjunto y en los mismos términos establecidos en las letras d) y e), acompañando un documento en que conste que la persona sobre la que se solicita antecedentes en cada una de esas letras ha aprobado el referido programa académico."

> **TN:** The heading reads "ASESORIA DE INVERSIÓN" (without accent on the first word) in the NCG 502 PDF; this appears to be a typographic omission — the full form is "asesoría de inversión". Rendered with correct accent in the English heading; the Spanish block reproduces the corrected form consistent with NCG 524's own heading "ASESORÍA DE INVERSIÓN".

> **TN:** "apodos" is rendered "aliases" in the parenthetical gloss and "usernames or aliases" in the English body, reflecting its meaning of informal identifiers or nicknames used in digital channels; "aliases" is more natural in a compliance context than the literal "nicknames".

### Cross-references
- Ley 21.521 Art. 7 — authorization mandate this section implements.
- Ley 18.045 Art. 4 Bis(f) — qualified investor definition; sole-declaration relief (removed by NCG 524) was conditioned on this class; now see §II.G.
- NCG 503 (Norma de Carácter General N° 503) — knowledge accreditation requirements for subparagraphs d) and e).
- NCG 502 §IV.A — governance and risk-management policies whose applicable subset must accompany this application (per item b).
- NCG 502 §III.A — disclosure obligations; URL/access mechanism for items a) and b) thereof now required under numeral 5) of literal a).
- NCG 502 §II.G — general exception to authorization requirement for entities serving only qualified investors.

> **Source:** NCG 502 §II.A (12-ene-2024), as amended by NCG 524 items a.1, a.2, a.3, a.4 (02-dic-2024).

---

## II.B — Credit Advisory
**NCG anchor:** N° 502, Sección II, B
**Implements:** Ley 21.521 Art. 7 (per-service authorization)
**Tags:** authorization, credit-advisory, psf

### Plain-English text

The authorization application for the credit advisory (asesoría crediticia) service must be accompanied by the following supporting documents:

a) Identification of the channels through which it will interact with clients or the public, indicating, as applicable:

1. The usernames or aliases it uses to identify itself in those channels.

2. The applications that must be used to access those channels and on which platform they are supported.

3. In the case of physical channels, the address or addresses at which such interaction takes place.

4. The URL address or mechanism through which the information referred to in subparagraphs a) and b) of the first paragraph of Section III.B of this regulation can be accessed.

> **TN:** NCG 524 amended this section: it added new numeral 4) to literal a) and replaced literal d) with substantively different text; the consolidated Spanish faithfully joins NCG 502 retained text (numerals 1–3 and literals b–c) with the NCG 524 amendments (numeral 4 and literal d). Verified against the 524 source PDF.

b) Document containing the policies referred to in subparagraph B of Section IV of this regulation that are applicable to it in accordance with what is established in subparagraph B.4 of that section. To rely on any of the exceptions referred to in subparagraph B.4, the applicant must declare the conditions that justify the exception.

c) Document with the general description of the procedure and manner in which the service will be provided, indicating those parts of the process that are carried out by natural persons or by computer algorithms, and which parts use the applicant's own resources, subcontracted resources, or resources acquired from third parties.

d) In the case where credit evaluations (evaluaciones crediticias) or identity verifications (verificaciones de identidad) emanate from a computer algorithm without human intervention, a person responsible for the verification and validation process of said algorithm must be designated — with respect to whether its design and execution comply with the standards of coherence, consistency, and objectivity between the data entered into the algorithm to perform the evaluation, the results it delivers, and the needs expressed by the clients who contract such services. The natural persons responsible for verifying the coherence of the algorithms and from whom the evaluations or identity verifications emanate, prior to performing any of those functions, must have passed a professional or technical academic program, whether national or foreign, in matters related to data analysis, statistics, finance, identity evaluation, or the payment capacity of natural or legal persons, with a duration of at least 4 semesters. For these purposes, a document must be attached evidencing that the natural person responsible for verifying the coherence of the algorithm or at least one natural person from whom the evaluations or identity verifications performed by the service provider emanate has passed the academic program referred to in the preceding paragraph.

### Original Spanish

> "B. ASESORÍA CREDITICIA
>
> a) Identificación de los canales mediante los que interactuará con clientes o el público, indicando, en lo que corresponda:
>
> 1) Los nombres de usuario o apodos que emplea para identificarse en esos canales.
>
> 2) Las aplicaciones que se deben emplear para acceder a esos canales y en qué plataforma se soportan.
>
> 3) En caso de canales físicos, el o los domicilios en que se da esa interacción.
>
> 4) La dirección URL o mecanismo en que se puede acceder a la información a que se refieren los literales a) y b) del primer párrafo de la sección III.B de esta normativa.
>
> b) Documento que contenga las políticas a que se refiere la letra B de la Sección IV de esta normativa que le resulten aplicables conforme a lo establecido en la letra B.4 de esa sección. Para acogerse a alguna de las excepciones a las que se refiere esa letra B.4 deberá declarar las condiciones que justifican la excepción.
>
> c) Documento con la descripción general del procedimiento y forma en que se prestará el servicio, indicando aquellas partes del proceso que son realizados por personas o por algoritmos informáticos y cuáles con recursos propios, subcontratados o adquiridos a terceros.
>
> d) En el caso de que las evaluaciones crediticias o verificaciones de identidad emanen de un algoritmo informático, sin intervención humana, se deberá designar a una persona responsable del proceso de verificación y validación de dicho algoritmo, en cuanto a que su diseño y ejecución cumpla con los estándares de coherencia, consistencia y objetividad entre datos ingresados al algoritmo para realizar la evaluación, los resultados que éste entrega y las necesidades manifestadas por los clientes que contratan dichos servicios. Las personas naturales responsables de verificar la coherencia de los algoritmos y de las cuales emanan las evaluaciones o las verificaciones de identidad, previo a desempeñar cualquiera de dichas funciones deberán haber aprobado un programa académico de carácter profesional o técnico, nacional o extranjero, sobre materias relacionadas con análisis de datos, estadísticas, finanzas, evaluación de la identidad o capacidad de pago de personas o entidades, de una duración de al menos 4 semestres. A estos efectos, se deberá acompañar un documento en que conste que la persona natural encargada de verificar la coherencia del algoritmo o al menos una persona natural de la cual emane las evaluaciones o las verificaciones de identidad realizadas por el prestador del servicio, ha aprobado el programa académico referido en el párrafo anterior."

### Cross-references
- Ley 21.521 Art. 7 — authorization mandate this section implements.
- Ley 18.045 Art. 4 Bis(f) — qualified investor definition; sole-declaration relief (removed by NCG 524) was conditioned on this class; now see §II.G.
- NCG 502 §IV.B — governance and risk-management policies whose applicable subset must accompany this application (per item b).
- NCG 502 §III.B — disclosure obligations; URL/access mechanism for items a) and b) thereof now required under numeral 4) of literal a).
- NCG 502 §II.G — general exception to authorization requirement for entities serving only qualified investors.

> **Source:** NCG 502 §II.B (12-ene-2024), as amended by NCG 524 items b.1, b.2, b.3 (02-dic-2024).

---

## II.C — Crowdfunding Platform
**NCG anchor:** N° 502, Sección II, C
**Implements:** Ley 21.521 Art. 7 (per-service authorization)
**Tags:** authorization, crowdfunding-platform, psf

### Plain-English text

The authorization application for the crowdfunding platform (plataforma de financiamiento colectivo) service must be accompanied by the following supporting documents:

a) Identification of the channels through which it will interact with clients or the public, indicating, as applicable:

1. The applications that must be used to access those channels and on which platform they are supported.

2. In the case of physical channels, the address or addresses at which such interaction takes place.

b) Identification of the block (bloque) referred to in subparagraph C.6 of Section IV of this regulation that is applicable to the applicant, accompanied by a declaration setting out in detail the conditions that justify the classification of the service provider in the relevant block.

c) Document containing the policies referred to in subparagraph C of Section IV, that are applicable to it in accordance with the block classification referred to in subparagraph C.6 of Section IV.

d) Document with the description of the procedures that will be carried out to prevent the investment projects or financing needs disseminated on the platform from being fraudulent, or that the resources come from or are destined for illicit activities.

e) Document with the description of the procedures that will be carried out, in addition to those referred to in subparagraph d) above, to analyze the economic, legal, and financial viability of those investment projects or financing needs disseminated on the platform with the aim of obtaining resources for amounts exceeding the equivalent of 20,000 Unidades de Fomento.

f) Document with the description of the mechanisms established to limit or adjust the degree of risk exposure that those who provide financing on the platform have in the projects, in accordance with the expectations or needs expressed by them.

> **TN:** NCG 524 amended this section: it deleted literal e)'s trailing sentence and deleted literal g) entirely (renumbering old g to f); the consolidated Spanish faithfully joins NCG 502 retained text with the new final paragraph from NCG 524. Verified against the 524 source PDF.

By virtue of the provisions of Article 5 second paragraph numeral 8 of Ley N° 21.521, stock exchanges (bolsas de valores) under Ley N° 18.045 may provide the crowdfunding platform service and operate such platforms without being registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros), provided that, prior to commencing the provision of such service, they communicate that fact to this Commission (CMF), together with the supporting documents required under subparagraphs d) to f) of this section.

### Original Spanish

> "C. PLATAFORMA DE FINANCIAMIENTO COLECTIVO
>
> a) Identificación de los canales mediante los que interactuará con clientes o el público, indicando, en lo que corresponda:
>
> 1) Las aplicaciones que se deben emplear para acceder a esos canales y en qué plataforma se soportan.
>
> 2) En caso de canales físicos, el o los domicilios en que se da esa interacción.
>
> b) Identificación del bloque al que se refiere la letra C.6 de la Sección IV de esta normativa que le resulta aplicable al solicitante, acompañando una declaración en que se detallen las condiciones que justifican la clasificación del prestador de servicios en determinado bloque.
>
> c) Documento que contenga las políticas a que se refieren la letra C de la Sección IV, que le resulten aplicables conforme a la clasificación de bloques a la que se refiere la letra C.6 de la Sección IV.
>
> d) Documento con la descripción de los procedimientos que se llevarán a cabo para prevenir que los proyectos o necesidades de financiamiento que se difundan en la plataforma resulten fraudulentos, o que los recursos provengan o estén destinados a actividades ilícitas.
>
> e) Documento con la descripción de los procedimientos que se llevarán a cabo, de forma adicional a aquellos referidos en la letra d) anterior, para analizar la viabilidad económica, jurídica y financiera de aquellos proyectos de inversión o necesidades de financiamiento que se difundan en la plataforma con el fin de obtener recursos por montos superiores al equivalente a 20.000 Unidades de Fomento.
>
> f) Documento con la descripción de los mecanismos establecidos para acotar o ajustar el grado de exposición al riesgo que tienen en los proyectos quienes entregan financiamiento en la plataforma, conforme a las expectativas o necesidades por ellos manifestadas.
>
> En virtud de lo establecido en el numeral 8 del segundo inciso del artículo 5 de la Ley N°21.521, las bolsas de valores de la Ley N°18.045 podrán prestar el servicio de Plataforma de Financiamiento Colectivo y operar tales plataformas, sin estar inscritas en el Registro de Prestadores de Servicios Financieros. Lo anterior, siempre que, previo al inicio de la prestación de dicho servicio comuniquen ese hecho a esta Comisión, junto a los antecedentes exigidos por las letras d) a la f) de esta sección."

### Cross-references
- Ley 21.521 Art. 7 — authorization mandate this section implements.
- Ley 21.521 Art. 5 second paragraph numeral 8 — stock-exchange exemption from registration for crowdfunding platform service.
- Ley 18.045 — governs stock exchanges that may rely on the numeral 8 exemption.
- NCG 502 §IV.C — governance and risk-management policies and block classification (C.6) whose applicable subset must accompany this application.
- NCG 502 §II.G — general exception to authorization requirement for entities serving only qualified investors.

> **Source:** NCG 502 §II.C (12-ene-2024), as amended by NCG 524 items c.1, c.2, c.3 (02-dic-2024).

---

## II.D — Alternative Trading System
**NCG anchor:** N° 502, Sección II, D
**Implements:** Ley 21.521 Art. 7 (per-service authorization)
**Tags:** authorization, alternative-trading-system, psf, crypto-assets

### Plain-English text

The authorization application for the alternative trading system (sistema alternativo de transacción) service must be accompanied by the following supporting documents:

a) Identification of the channels through which access to the transactional system will be obtained, indicating, as applicable:

1. The applications that must be used to access those channels and on which platform they are supported.

2. In the case of physical channels, the address or addresses at which such interaction takes place.

b) Identification of the block referred to in subparagraph C.6 of Section IV of this regulation that is applicable to the applicant, accompanied by a declaration setting out in detail the conditions that justify the classification of the service provider in the relevant block.

c) Document containing the policies referred to in subparagraph C of Section IV of this regulation, that are applicable to it in accordance with the block classification referred to in subparagraph C.6 of Section IV.

d) Document with the description of the mechanisms established to limit or adjust the degree of risk exposure that the system's participants have in the financial instruments, in accordance with the expectations or needs expressed by them.

e) Accreditation of operational capacity (capacidad operacional) in accordance with what is established in Section VI of this regulation.

f) Internal regulations (reglamentación interna) — applicable to Block 2 and Block 3 entities — which must at least address the following matters:

1. **Access Rules (Normas de Acceso):** what objective and non-discriminatory conditions will be required of participants to gain access to the systems and to be able to submit buy or sell offers for financial instruments, and how compliance with such conditions will be accredited. In addition, the circumstances under which participants could be suspended or expelled from the system.

2. **Instrument Admission Rules (Normas de admisión a negociación de instrumentos):** what characteristics or conditions the financial instruments, their issuers, represented assets, guarantors, guarantees, protocols, debtors, or custodians — as applicable — must meet to be admitted to trading on the system, and how compliance will be verified. For this purpose, it must distinguish between those instruments that, by their nature, require differentiated admission rules. In addition, with respect to virtual assets (activos virtuales), only crypto-assets that have a public document containing the technical specifications that allow knowledge of the technology and relevant aspects for those who acquire them — such as, for example, what assets are digitally represented, what rights the purchaser of the crypto-asset will have, regarding whom they will have those rights, and whether they are civil or natural rights — shall be admitted to trading. All of this in conformity with the minimum specifications established by the alternative system for those purposes. Such public document may be the translation into Spanish or English of its original or the one that the alternative system itself has prepared for that purpose.

3. **Price Formation Rules (Reglas de formación de precios):** what mechanisms for receiving offers or bids and for matching them will be used; that is, whether it will be by means of an open order book, an automatic compatible offers system, an open auction, or a tender, among others, and how competing offers will be prioritized.

4. **Settlement Rules (Reglas de liquidación):** how proceedings must be conducted subsequent to the close of the negotiation with the aim of effecting the physical, logical, or symbolic delivery of the financial instrument acquired and the payment for the purchase thereof, or of paying the balances in favor that are produced, as applicable, and what role the alternative system will play in that settlement process.

5. **Suspension Mechanisms (Mecanismos de suspensión):** rules establishing whether the system will have rules or criteria to suspend or cancel the quotation, offer, or transaction of financial instruments, due to significant price variation, cyber-attacks, fraud, or other relevant circumstances that warrant adopting such measure to prevent clients from being affected. In addition, the mechanism it will use to suspend or cancel the quotation of those instruments that cease to meet the characteristics or conditions by virtue of which they were admitted to the system, and to communicate that fact to its clients.

Without prejudice to the fact that the internal regulations are not subject to the approval of this Commission (CMF), any modification or update to them must be remitted to this Service no later than the day on which they come into force.

Those who provide the alternative trading system service shall in no case be authorized to admit to trading or to allow the entry of offers consisting of primary placements of securities (títulos valores) or crypto-assets (for example, "Initial Public Offering" or "Initial Coin Offering"), without having first obtained authorization to act as a crowdfunding platform and without complying with all the obligations applicable to such platforms in respect of this type of primary placement.

For the purposes of Ley N° 21.521, the mere making available to persons of a communication system (such as WhatsApp, IRC, Zoom, MS Teams, among others) shall not be considered to fall within the scope of the alternative trading system service, unless such system incorporates in its design mechanisms or tools whose purpose is to allow users to exchange or close offers, orders, or bids to buy or sell financial instruments or securities.

By virtue of the provisions of Article 5 second paragraph numeral 8 of Ley N° 21.521, stock exchanges (bolsas de valores) under Ley N° 18.045 may provide the alternative trading system service and operate such systems without being registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros), provided that, prior to commencing the provision of such service, they communicate that fact to this Commission (CMF), together with the supporting documents required under subparagraphs d) and f) of this section.

### Original Spanish

> "D. SISTEMA ALTERNATIVO DE TRANSACCIÓN
>
> a) Identificación de los canales a través de los cuales se accederá al sistema transaccional, indicando, en lo que corresponda:
>
> 1) Las aplicaciones que se deben emplear para acceder a esos canales y en qué plataforma se soportan.
>
> 2) En caso de canales físicos, el o los domicilios en que se da esa interacción.
>
> b) Identificación del bloque al que se refiere la letra C.6 de la Sección IV de esta normativa que resulta aplicable al solicitante, acompañando una declaración en que se detallen las condiciones que justifican la clasificación del prestador de servicios en determinado bloque.
>
> c) Documento que contenga las políticas a que se refiere la letra C de la Sección IV de esta normativa, que le resulten aplicables conforme a la clasificación de bloques a la que se refieren la letra C.6 de la Sección IV.
>
> d) Documento con la descripción de los mecanismos establecidos para acotar o ajustar el grado de exposición al riesgo que tienen en los instrumentos financieros los participantes del sistema, conforme a las expectativas o necesidades por ellos manifestadas.
>
> e) Acreditación de la capacidad operacional conforme a lo establecido en la Sección VI de esta normativa.
>
> f) Tratándose de entidades del Bloque 2 y 3, reglamentación interna, la que al menos deberá referirse a las siguientes materias:
>
> 1) Normas de Acceso: qué condiciones objetivas y no discriminatorias se exigirán a los participantes para tener acceso a los sistemas y poder ingresar ofertas de compraventa de instrumentos financieros, y cómo se acreditará el cumplimiento de las mismas. Además, las circunstancias en que los participantes pudieran ser suspendidos o expulsados del sistema.
>
> 2) Normas de admisión a negociación de instrumentos: qué características o condiciones deberán cumplir los instrumentos financieros, sus emisores, activos representados, garantes, garantías, protocolos, deudores o custodios, según corresponda, para ser admitidos a cotización en el sistema y cómo se verificará su cumplimiento. Para lo cual deberá distinguir entre aquellos instrumentos que, por su naturaleza, requieran reglas de admisión diferenciadas. Además, respecto de activos virtuales, sólo se admitirán a cotización criptoactivos que cuenten con un documento público que contenga las especificaciones técnicas que permitan conocer la tecnología y aspectos relevantes para quienes los adquieren como, por ejemplo, qué activos son representados digitalmente, qué derechos tendrá quien adquiere el criptoactivo, respecto de quién tendrá esos derechos, y si son civiles o naturales. Todo ello, de conformidad con las especificaciones mínimas que establezca el sistema alternativo para estos efectos. Dicho documento público podrá ser la traducción al español o inglés de su original o de aquel que el propio sistema alternativo haya elaborado para ese efecto.
>
> 3) Reglas de formación de precios: qué mecanismos de recepción de ofertas o posturas, y de calce de las mismas se emplearán; esto es, si será mediante un libro abierto de ofertas, un sistema de calce automático de ofertas compatibles, una subasta abierta o una licitación, entre otros, y cómo se priorizarán las ofertas que compiten entre sí.
>
> 4) Reglas de liquidación: cómo se deberá proceder con posterioridad al cierre de la negociación al objeto de materializar la entrega física, lógica o simbólica del instrumento financiero adquirido y el pago por la compra del mismo, o a pagar los saldos a favor que se produzcan, según corresponda, y qué rol tendrá en ese proceso el sistema alternativo.
>
> 5) Mecanismos de suspensión: normas que establezcan si el sistema contará con reglas o criterios para suspender o cancelar la cotización, oferta o transacción de los instrumentos financieros, por variación significativa de precios, ciberataques, fraudes u otras circunstancias relevantes que ameriten adoptar esa medida para prevenir que clientes se vean afectados. Además, el mecanismo que empleará para suspender o cancelar la cotización de aquellos instrumentos que dejen de cumplir las características o condiciones en virtud de las cuales se les admitió al sistema, y comunicar ese hecho a sus clientes.
>
> Sin perjuicio de que la reglamentación no queda sujeta a la aprobación de esta Comisión, toda modificación o actualización de ésta deberá ser remitida a este Servicio a más tardar el día en que entre en vigor.
>
> Quienes presten el servicio de sistema alternativo de transacción en ningún caso podrán admitir a cotización o permitir el ingreso de ofertas que consistan en colocaciones primarias de títulos valores o de criptoactivos (por ejemplo, "Initial Public Offering" o "Initial Coin Offering"), sin haber obtenido la autorización previa para actuar como plataforma de financiamiento colectivo y cumpliendo con todas las obligaciones exigibles a esas plataformas respecto de este tipo de colocaciones primarias.
>
> Para los efectos de la Ley N°21.521, no quedará comprendido dentro del servicio de sistema alternativo de transacción la mera puesta disposición a personas de un sistema de comunicación (como Whatsapp, IRC, Zoom, MS Teams, entre otros), salvo que éste contemple en su diseño mecanismos o herramientas que tienen por objeto permitir a los usuarios el intercambio o cierre de ofertas, órdenes o posturas de compra o venta de instrumentos financieros o títulos valores.
>
> En virtud de lo establecido en el numeral 8 del segundo inciso del artículo 5 de la Ley N°21.521, las bolsas de valores de la Ley N°18.045 podrán prestar el servicio de Sistemas Alternativos de Transacción y operar tales sistemas, sin estar inscritas en el Registro de Prestadores de Servicios Financieros. Lo anterior, siempre que, previo al inicio de la prestación de dicho servicio comuniquen ese hecho a esta Comisión, junto a los antecedentes exigidos por las letras d) y f) de esta sección."

> **TN:** "Normas de Acceso", "Normas de admisión a negociación de instrumentos", "Reglas de formación de precios", "Reglas de liquidación", and "Mecanismos de suspensión" appear in bold in the original PDF as defined sub-headings of the internal regulations requirement; they are rendered in bold in the English translation accordingly.

> **TN:** "títulos valores" is rendered "securities" as the standard Chilean securities-law equivalent; "criptoactivos" / "activos virtuales" are rendered "crypto-assets" / "virtual assets" following the Ley 21.521 regulatory vocabulary.

> **TN:** NCG 524 deleted former literal f) (the disclosure document, "Documento con la descripción de la información que será divulgada…") and renumbered former literal g) (internal regulations) to f), simultaneously narrowing its scope to Block 2 and Block 3 entities only. The disclosure-document requirement no longer appears as a standalone literal in the post-amendment text.

### Cross-references
- Ley 21.521 Art. 7 — authorization mandate this section implements.
- Ley 21.521 Art. 5 second paragraph numeral 8 — stock-exchange exemption from registration for alternative trading system service.
- Ley 18.045 — governs stock exchanges that may rely on the numeral 8 exemption.
- NCG 502 §IV.C — governance policies and block classification (C.6) whose applicable subset must accompany this application.
- NCG 502 §VI — operational capacity accreditation required under item e).
- NCG 502 §II.C — crowdfunding platform authorization; prior authorization required before admitting primary placements.
- NCG 502 §II.G — general exception to authorization requirement for entities serving only qualified investors.

> **Source:** NCG 502 §II.D (12-ene-2024), as amended by NCG 524 items d.1, d.2, d.3 (02-dic-2024).

---

## II.E — Order Routing
**NCG anchor:** N° 502, Sección II, E
**Implements:** Ley 21.521 Art. 7 (per-service authorization)
**Tags:** authorization, order-routing, psf, guarantee

### Plain-English text

The authorization application for the order routing (enrutamiento de órdenes) service must be accompanied by the following supporting documents:

a) Identification of the channels through which access to the services will be obtained, indicating, as applicable:

1. The applications that must be used to access those channels and on which platform they are supported.

2. In the case of physical channels, the address or addresses at which such interaction takes place.

b) Document containing the policies referred to in subparagraph D of Section IV of this regulation that are applicable to it in accordance with what is established in subparagraph D.4 of that Section. To rely on any of the exceptions referred to in subparagraph D.4, the applicant must attach a declaration setting out in detail the conditions that justify the exception.

c) Document accrediting the establishment of the guarantee (garantía) under Article 10 of Ley N° 21.521, in accordance with what is established in Section V of this regulation, that is applicable to it in accordance with subparagraph A of that Section.

d) Accreditation of operational capacity in accordance with what is established in Section VI of this regulation.

> **TN:** NCG 524 deleted former literal d) ("Documento con la descripción de la información que será divulgada…") and renumbered former literal e) (operational capacity) to d). The disclosure-document requirement no longer appears as a standalone literal in the post-amendment text for this service.

### Original Spanish

> "E. ENRUTAMIENTO DE ÓRDENES
>
> a) Identificación de los canales a través de los cuales se accederá a los servicios, indicando, en lo que corresponda:
>
> 1) Las aplicaciones que se deben emplear para acceder a esos canales y en qué plataforma se soportan.
>
> 2) En caso de canales físicos, el o los domicilios en que se da esa interacción.
>
> b) Documento que contenga las políticas a que se refiere la letra D de la Sección IV de esta normativa que le resulten aplicables conforme a lo establecido en la letra D.4 de esa Sección. Para acogerse a alguna de las excepciones a las que se refiere esa letra D.4 deberá acompañar una declaración en que se detallen las condiciones que justifican la excepción.
>
> c) Documento que acredite la constitución de la garantía del artículo 10° de la Ley N°21.521, de conformidad a lo establecido en la Sección V de esta normativa, que le resulte aplicable conforme a lo establecido en la letra A. de esa Sección.
>
> d) Acreditación de la capacidad operacional conforme a lo establecido en la Sección VI de esta normativa."

### Cross-references
- Ley 21.521 Art. 7 — authorization mandate this section implements.
- Ley 21.521 Art. 10 — guarantee requirement whose accreditation is required under item c).
- NCG 502 §IV.D — governance policies whose applicable subset must accompany this application (per item b).
- NCG 502 §V — capital and guarantees section; subparagraph A governs which guarantee tier is applicable.
- NCG 502 §VI — operational capacity accreditation required under item d).
- NCG 502 §II.G — general exception to authorization requirement for entities serving only qualified investors.

> **Source:** NCG 502 §II.E (12-ene-2024), as amended by NCG 524 item e.1 (02-dic-2024).

---

## II.F — Intermediation and Custody of Financial Instruments
**NCG anchor:** N° 502, Sección II, F
**Implements:** Ley 21.521 Art. 7 (per-service authorization)
**Tags:** authorization, intermediation, custody, financial-instruments, psf

### Plain-English text

The authorization application for the intermediation and custody of financial instruments (intermediación y custodia de instrumentos financieros) service must be accompanied by the following supporting documents:

a) Identification of the channels through which access to the services will be obtained, indicating, as applicable:

1. The applications that must be used to access those channels and on which platform they are supported.

2. In the case of physical channels, the address or addresses at which such interaction takes place.

b) Identification of the block referred to in subparagraph E.6 of Section IV of this regulation that is applicable to the applicant, accompanied by a declaration setting out in detail the conditions that justify the classification of the service provider in the relevant block.

c) Document containing the policies and procedures referred to in subparagraph E of Section IV of this regulation, that are applicable to it in accordance with the block classification referred to in subparagraph E.6 of Section IV.

d) Document accrediting the establishment of the guarantee under Article 10 of Ley N° 21.521, in accordance with what is established in Section V of this regulation, that is applicable to it in accordance with subparagraph A of that Section.

e) Annual financial statements of the entity audited by an external audit firm without qualifications (sin salvedades), no more than 12 months old, and additionally financial statements for the immediately preceding quarter when the audited financial statements are more than 6 months old as of the date of the application. In addition, a declaration must be attached setting out the calculation of the adjusted net worth (patrimonio ajustado).

f) In the case of those applying for authorization to provide the custody of financial instruments service, in the event that they hold instruments in custody at the time of making the application, they must submit a summary of the number of clients they have and the aggregate amount in custody per financial instrument as of the date of application.

g) Accreditation of operational capacity in accordance with what is established in Section VI of this regulation.

> **TN:** NCG 524 replaced literal e) with substantively different text (adding the "sin salvedades" requirement and removing the annual-update obligation via the official channel), deleted literal g) (renumbering old h to g), and added a new final paragraph. The consolidated Spanish faithfully joins NCG 502 retained text with NCG 524 amendments. The 100-character sliding-window chunks that straddle those NCG 502/NCG 524 text boundaries are not contiguous passages in either single source PDF. This section is on the round-trip --exclude list and was verified manually.

For the purposes of Ley N° 21.521, the prior intent to sell financial instruments shall not be considered as prior intent (ánimo previo) for the intermediation of financial instruments when such sale has the sole purpose of delivering in pledge (prenda), guarantee (garantía), custody (custodia), or collection (cobranza) the financial instrument that will be acquired.

> **TN:** NCG 524 deleted former literal g) ("Documento con la descripción de la información que será divulgada…") and renumbered former literal h) (operational capacity) to g). The disclosure-document requirement no longer appears as a standalone literal in the post-amendment text for this service.

### Original Spanish

> "F. INTERMEDIACIÓN Y CUSTODIA DE INSTRUMENTOS FINANCIEROS
>
> a) Identificación de los canales a través de los cuales se accederá a los servicios, indicando, en lo que corresponda:
>
> 1) Las aplicaciones que se deben emplear para acceder a esos canales y en qué plataforma se soportan.
>
> 2) En caso de canales físicos, el o los domicilios en que se da esa interacción.
>
> b) Identificación del bloque al que se refiere la letra E.6 de la Sección IV de esta normativa que resulta aplicable al solicitante, acompañando una declaración en que se detallen las condiciones que justifican la clasificación del prestador de servicios en determinado bloque.
>
> c) Documento que contenga las políticas y procedimientos a que se refiere la letra E de la Sección IV de esta normativa, que le resulten aplicables conforme a la clasificación de bloques a la que se refieren la letra E.6 de la Sección IV.
>
> d) Documento que acredite la constitución de la garantía del artículo 10° de la Ley N°21.521, de conformidad a lo establecido en la Sección V de esta normativa, que le resulte aplicable conforme a lo establecido en la letra A de esa Sección.
>
> e) Estados financieros de la entidad auditados por una empresa de auditoría externa sin salvedades y con una antigüedad no mayor a 12 meses. Adicionalmente, estados financieros del trimestre inmediatamente anterior a la solicitud cuando los estados financieros auditados sean de una antigüedad superior a 6 meses a la fecha de la solicitud. Además, deberán acompañar una declaración en la cual se detalle el cálculo del patrimonio ajustado.
>
> f) Tratándose de quienes soliciten autorización para prestar el servicio de custodia de instrumentos financieros, en el evento que mantengan instrumentos custodiados al momento de realizar la solicitud, deberán remitir un resumen de la cantidad de clientes que poseen y el monto agregado en custodia por instrumento financiero a la fecha de solicitud.
>
> g) Acreditación de la capacidad operacional conforme a lo establecido en la Sección VI de esta normativa.
>
> Para efectos de lo establecido en la Ley N°21.521, no se considerará como ánimo previo para la intermediación de instrumentos financieros la intención anterior de enajenar los instrumentos cuando esta enajenación tiene la sola finalidad de entregar en prenda, garantía, custodia o cobranza el instrumento financiero que será adquirido."

> **TN:** "patrimonio ajustado" is rendered "adjusted net worth" — the term refers to a regulatory capital measure computed by adjusting equity for specific add-backs and deductions defined in §V.C of this regulation. "Adjusted equity" would also be acceptable; "adjusted net worth" is preferred here to signal the prudential (rather than purely accounting) nature of the measure.

> **TN:** "fiscalizados" (present in former item e)) has been removed by NCG 524's replacement of that literal; the new literal e) no longer contains that term. The new text requires audited financial statements "sin salvedades" (without qualifications) — a material new requirement not present in the NCG 502 baseline.

### Cross-references
- Ley 21.521 Art. 7 — authorization mandate this section implements.
- Ley 21.521 Art. 10 — guarantee requirement whose accreditation is required under item d).
- NCG 502 §IV.E — governance policies and block classification (E.6) whose applicable subset must accompany this application.
- NCG 502 §V — capital and guarantees; subparagraph A governs which guarantee tier is applicable; §V.C defines adjusted net worth.
- NCG 502 §VI — operational capacity accreditation required under item g).
- NCG 502 §II.G — general exception to authorization requirement for entities serving only qualified investors.

> **Source:** NCG 502 §II.F (12-ene-2024), as amended by NCG 524 items f.1, f.2, f.3 (02-dic-2024).

---

## II.G — Exception to the Authorization Requirement and Compliance with the Provisions of This Regulation
**NCG anchor:** N° 502, Sección II, G
**Implements:** Ley 21.521 Art. 4 (CMF power to grant exceptions); Art. 7 (per-service authorization requirement)
**Tags:** authorization, exception, qualified-investors, psf

### Plain-English text

By virtue of the provisions of Article 4 of Ley N° 21.521, those who, being registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros), meet the following cumulative circumstances (circunstancias copulativas) are excepted from the requirement to apply for authorization to provide the investment advisory (asesoría de inversión), credit advisory (asesoría crediticia), crowdfunding platform (plataforma de financiamiento colectivo), order routing (enrutamiento de órdenes), and alternative trading system (sistema alternativo de transacción) services, and from compliance with the provisions of this regulation:

a) That, in the last 10 years counted from the date of submission of the authorization application, they have not been sanctioned or do not have charges formulated against them for the serious infringements (infracciones graves) referred to in Article 14 of the provisions of Ley N° 21.521, or abroad for equivalent conduct. In the case of a legal person, this requirement shall be considered with respect to the entities that form part of its business group (grupo empresarial) in the terms contemplated in Article 96 of Ley N° 18.045 on Securities Markets, as well as its controllers, principal shareholders or partners, directors, administrators, and managers, as at the date of the application; and

b) That the provision in Chile of the services regulated by this regulation be provided only to qualified investors (inversionistas calificados) referred to in subparagraph f) of Article 4 Bis of Ley N° 18.045.

To rely on this exception, the applicant must, at the time of applying for registration in the Registry, make a declaration regarding the fact that it complies with the circumstances described above, and that, in the face of any modification to the same, it will cease to provide the services of Ley N° 21.521 while it has not obtained the corresponding authorization from this Commission (CMF). Such declaration must be made through the electronic mechanism provided for the submission of the registration application, on the Commission (CMF)'s website. In addition, such declaration must be updated annually through the mechanism established for that purpose on the Commission (CMF)'s website.

### Original Spanish

> "G. EXCEPCIÓN A LA SOLICITUD DE AUTORIZACIÓN Y CUMPLIMIENTO DE LAS DISPOSICIONES CONTENIDAS EN ESTA NORMATIVA
>
> En virtud de lo establecido en el artículo 4° de la Ley N°21.521 se exceptúa del requisito de solicitar autorización para prestar los servicios de asesoría de inversión, asesoría crediticia, plataforma de financiamiento colectivo, enrutamiento de órdenes y sistema alternativo de transacción, y del cumplimiento de las disposiciones contenidas en la presente normativa, a quienes, estando inscritos en el Registro de Prestadores de Servicios Financieros, cumplan las siguientes circunstancias copulativas:
>
> a) Que, en los últimos 10 años desde la fecha de ingreso de la solicitud de autorización, no hayan sido sancionadas o se encuentren formulados de cargos por las infracciones graves a que se refiere el artículo 14 a las disposiciones de la Ley N°21.521, o en el extranjero por conductas equivalentes. Tratándose de una persona jurídica, este requisito se considerará respecto de las entidades que formen parte de su grupo empresarial en los términos contemplados en el artículo 96 de la Ley N°18.045 de Mercado de Valores, así como de sus controladores, socios o accionistas mayoritarios, directores, administradores y gerentes, a la fecha de la solicitud; y
>
> b) Que la prestación en Chile de los servicios regulados por esta normativa sólo sea provista a inversionistas calificados a los que se refiere la letra f) del artículo 4 Bis de la Ley N°18.045.
>
> Para acogerse a esta excepción el solicitante, al momento de solicitar la inscripción en el Registro, deberá efectuar una declaración respecto del hecho que cumple las circunstancias antes descritas y que, frente a cualquier modificación de las mismas, dejará de prestar los servicios de la Ley N°21.521 mientras no haya obtenido la autorización respectiva por parte de esta Comisión. Dicha declaración deberá ser efectuada a través del mecanismo electrónico dispuesto para el ingreso de la solicitud de inscripción, en el sitio en Internet de la Comisión. Además, dicha declaración deberá ser actualizada anualmente a través del mecanismo establecido para ello en el sitio en Internet de la Comisión."

### Cross-references
- Ley 21.521 Art. 4 — the exception power exercised here.
- Ley 21.521 Art. 14 — the serious infringements whose sanction or charge disqualifies reliance on this exception.
- Ley 18.045 Art. 4 Bis(f) — the definition of qualified investor (inversionista calificado) used in condition b).
- Ley 18.045 Art. 96 — business group definition used in the condition a) assessment for legal persons.
- NCG 502 §I.C.2 — the parallel exception to the exclusive-corporate-purpose registration requirement on the same qualified-investor condition.
- NCG 502 §I.C.3 — the parallel exception to the Chilean-domicile registration requirement on the same qualified-investor condition.

> **Source:** NCG 502 §II.G (added by NCG 524 item g, 02-dic-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/seccion-03-divulgacion.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/seccion-03-divulgacion.md

# NCG 502 — Sección III: Disclosure and Information-Delivery Obligations (Obligaciones de Divulgación y Entrega de Información)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

## III — Disclosure and Information-Delivery Obligations
**NCG anchor:** N° 502, Sección III
**Implements:** Ley 21.521 Art. 12 (disclosure / information obligations)
**Tags:** disclosure, information, psf

### Plain-English text

Financial-Service Providers (PSFs), regardless of the activities for which they have been authorized, must implement policies, procedures, and controls to comply with the information obligations referred to in this section.

In particular, all information that is prepared, delivered, or made available to clients or the public must be:

a) Expressed in terms appropriate to the characteristics and conditions of the person who receives it, using plain language and avoiding technical terms, except where strictly necessary, and in that case explaining them clearly. Special consideration must be given to persons with disabilities — for example, visual or auditory disabilities — so that the information is delivered or made available to them in a manner appropriate to their disability.

b) Communicated through interactive and didactic tools, formats, resources, or media that facilitate its comprehension. In addition, relevant information must be communicated in a question-and-answer format.

c) Improved on the basis of an analysis conducted at least annually by the entity itself or by an external party, to determine, among other matters, whether the information made available is being read and understood by those who receive it.

d) Communicated in a timely manner and through appropriate channels or media to inform the client and the general public.

Those who provide the services of investment advisory (asesoría de inversión), credit advisory (asesoría crediticia), crowdfunding platform (plataforma de financiamiento colectivo), and alternative trading system (sistema alternativo de transacción) exclusively to Qualified Investors (Inversionistas Calificados) referred to in subparagraph f) of Article 4 Bis of Ley N° 18.045 shall be exempt from all requirements of this Section III.

### Original Spanish

> "III. OBLIGACIONES DE DIVULGACIÓN Y ENTREGA DE INFORMACIÓN
>
> Los proveedores de servicios financieros, independiente de las actividades que les hayan sido autorizadas, deberán implementar políticas, procedimientos y controles para cumplir con las obligaciones de información a las que se refiere la presente sección.
>
> En particular, toda información que se elabore, entregue, o ponga a disposición de clientes o el público, deberá ser:
>
> a) Expresada en términos acorde a las características y condiciones de quien la recibe, empleando un lenguaje sencillo y evitando tecnicismos, salvo en los casos en que resulte estrictamente necesario, debiendo explicarlos claramente. Deberá tener especial consideración con las personas en situación de discapacidad como, por ejemplo, visual o auditiva, de manera que la información se les entregue o ponga a disposición de una forma que resulte acorde a su situación de discapacidad.
>
> b) Comunicada mediante herramientas, formatos, recursos o medios interactivos y didácticos que faciliten su comprensión. Además, deberá comunicar la información relevante mediante la modalidad de preguntas y respuestas.
>
> c) Perfeccionada sobre la base del análisis que se realice al menos anualmente por la propia entidad o un externo para determinar, entre otras materias, si la información puesta a disposición está siendo leída y comprendida por quienes la recibieron.
>
> d) Comunicada de manera oportuna y mediante canales o medios idóneos para informar al cliente y público en general.
>
> Quienes presten los servicios de asesoría de inversión, asesoría crediticia, plataforma de financiamiento colectivo y sistema alternativo de transacción exclusivamente a inversionistas calificados a los que se refiere la letra f) del artículo 4 Bis de la Ley N°18.045 quedarán exceptuados de todas las exigencias de esta Sección III."

### Cross-references
- Ley 21.521 Art. 12 — disclosure mandate this section implements.
- Ley 18.045 Art. 4 Bis(f) — qualified investor definition; exemption applies when the four listed services are provided exclusively to this class.
- NCG 502 §III.A–§III.G — per-service subsections setting out specific disclosure and information-delivery obligations.

> **Source:** NCG 502 §III (12-ene-2024).

---

## III.A — Investment Advisory
**NCG anchor:** N° 502, Sección III, A
**Implements:** Ley 21.521 Art. 12 (disclosure / information obligations)
**Tags:** disclosure, information, investment-advisory

### Plain-English text

The following information must be made available to the public at all times, duly updated:

a) General description of the commission or remuneration structure received by the adviser — that is, indicating whether it charges a fixed or variable commission to clients; whether it receives a fee from those who issue, intermediate, channel, or place the instruments acquired or held by the adviser's clients; or whether it receives a fee for referring clients to another service provider; among others.

b) Description of the advisory model used — that is, whether the recommendation emanates from natural persons, computer algorithms, or a combination of both; and, in general terms, on the basis of what elements the recommendation is made — for example, whether it emanates from a fundamental analysis that takes as its basis financial statements or financial position, or whether it is a type of technical or statistical analysis based on the historical behaviour of the instrument, or on the expert judgement of an individual, among others. In describing the model, the entity must avoid generating mistaken perceptions in the public regarding the degree of sophistication of the computer algorithm used. For example, the fact that the recommendation emanates from simple mathematical and logical operations carried out in a spreadsheet must not be presented as if it emanated from a computer algorithm.

c) The existence of conflicts of interest that emanate from the business model or its revenue sources, and how they are managed.

d) In the event that it has disclosed target prices or recommendations to buy, sell, or hold securities (valores), financial instruments, or investment projects to unidentified persons in the last 3 months, briefly describe the recommendation made and its outcome — that is, whether the target price was reached during the relevant period, or whether, for that period, had a transaction been carried out in line with the recommendation, it would have generated a gain or loss for the client who had followed such recommendation. For the purposes of the supervision of this obligation, the entity must maintain a record of recommendations made to unidentified persons, evidencing the recommendation and the date on which it was disclosed.

At the time of making the recommendation, the following information must be delivered to the client:

a) The principal financial, economic, tax, and legal characteristics of the recommended financial instrument, with special emphasis on the risks entailed by investing in that instrument and how those characteristics are suited to the client's needs.

b) The conflicts of interest arising between the service provider and the client in particular, how they will be managed, and how they may affect the client if not adequately resolved.

c) In the case of investment advisory services directed to the public in general, through social media and/or communications media, that have as consideration a fee from those who issue, intermediate, channel, or place the instruments or investment projects that are the subject of the communicated recommendation, the investment adviser must inform of this circumstance in an unequivocal and express manner at the time of communicating the content that is disseminated. The same shall apply in the event that the investment advisory service communicated has as consideration a fee for referring clients to other service providers.

It shall not be necessary to deliver the information referred to in subparagraphs a) and b) of the preceding paragraph in the case of clients with the status of Institutional Investor (Inversionista Institucional), and of Qualified Investor (Inversionista Calificado) from among those indicated in items 2, 3, and 4 of Section II of Norma de Carácter General N° 216.

### Original Spanish

> "A. ASESORÍA DE INVERSIÓN
>
> La siguiente información deberá ser puesta a disposición del público en todo momento, debidamente actualizada:
>
> a) Descripción general de la estructura de comisiones o remuneraciones que recibe el asesor, esto es, señalar si cobra una comisión fija o variable a clientes; recibe una retribución de quienes emiten, intermedian, canalizan o colocan los instrumentos adquiridos o mantenidos por los clientes del asesor; o recibe una retribución por referir clientes a otro prestador de servicios; entre otros.
>
> b) Descripción del modelo de asesoría utilizado, esto es, si la recomendación emana de personas, algoritmos informáticos o una combinación de ambos; y, en términos generales, sobre la base de qué elementos se efectúa la recomendación, por ejemplo, si emana de un análisis fundamental que toma como base los estados financieros o situación financiera, o si es un tipo de análisis técnico o estadístico sobre la base del comportamiento histórico del instrumento, o del juicio experto de un individuo, entre otros. En la descripción del modelo la entidad deberá evitar generar percepciones erradas en el público respecto al grado de sofisticación del algoritmo informático utilizado. Por ejemplo, que la recomendación emane de operaciones matemáticas y lógicas simples realizadas en una planilla de cálculo, no debe presentarse como que emana de un algoritmo informático.
>
> c) La existencia de conflictos de intereses que emanen del modelo de negocios o sus fuentes de ingresos, y cómo los gestiona.
>
> d) En caso que hubiere difundido precios objetivo o recomendaciones para comprar, enajenar o mantener valores, instrumentos financieros o proyectos de inversión a personas indeterminadas en los últimos 3 meses, describir brevemente la recomendación efectuada y su resultado, esto es, si se alcanzó dicho precio en el período respectivo o si, para dicho período, de haberse realizado una operación en línea con la recomendación se habría generado una ganancia o no para aquel cliente que hubiere seguido tal recomendación. Para efectos de la fiscalización de esta obligación, la entidad deberá mantener un registro de las recomendaciones a personas indeterminadas dejando constancia de la recomendación y la fecha en que fue difundida.
>
> Al momento de efectuar la recomendación, deberá entregar al cliente la siguiente información:
>
> a) Las principales características financieras, económicas, tributarias y jurídicas del instrumento financiero recomendado, poniendo especial énfasis en los riesgos que conllevan la inversión en ese instrumento y cómo esas características se adecúan a las necesidades del cliente.
>
> b) Los conflictos de intereses que se susciten entre el prestador del servicio y el cliente en particular, cómo se gestionarán y cómo pueden afectar al cliente si no se resolvieren adecuadamente.
>
> c) En caso de asesorías de inversión dirigidas al público en general, a través de medios sociales y/o de comunicación, que tengan como contraprestación una retribución de parte de quienes emiten, intermedian, canalizan o colocan los instrumentos o proyectos de inversión objetos de la recomendación comunicada, el asesor de inversión deberá informar de esta circunstancia de manera inequívoca y expresa al momento de comunicar el contenido que se difunde. Lo mismo aplicará para el caso en que la asesoría de inversión que se comunica tenga como contraprestación una retribución por referir clientes a otros prestadores de servicios.
>
> No será necesario entregar la información a que se refieren las letras a) y b) del párrafo anterior, en caso de clientes que tengan la calidad de Inversionista Institucional, y de Inversionista Calificado de entre los señalados en los números 2, 3 y 4 de la Sección II de la Norma de Carácter General N°216."

### Cross-references
- Ley 21.521 Art. 12 — disclosure mandate this section implements.
- Ley 18.045 Art. 4 Bis(f) — qualified investor definition; exemption from entire Section III applies when service is provided exclusively to this class.
- NCG 216 §II (items 2, 3, 4) — qualified investor sub-categories exempt from at-recommendation disclosures in this section.
- NCG 502 §III — general information-quality requirements applicable to all disclosures under this subsection.

> **Source:** NCG 502 §III.A (12-ene-2024), as amended by NCG 524 item C.a.1 (02-dic-2024).

---

## III.B — Credit Advisory
**NCG anchor:** N° 502, Sección III, B
**Implements:** Ley 21.521 Art. 12 (disclosure / information obligations)
**Tags:** disclosure, information, credit-advisory

### Plain-English text

The following information must be made available to the public at all times, duly updated:

a) General description of the commission or remuneration structure received by the adviser — that is, indicating whether it charges a fixed or variable commission to clients; whether it receives a fee for referring clients to another service provider; or whether it receives a fee based on the amount of credit placed; among others.

b) Description of the advisory model used — that is, whether the evaluation emanates from natural persons, computer algorithms, or a combination of both; and, in general terms, on the basis of what elements the evaluation is made — for example, whether it emanates from a fundamental analysis that takes as its basis financial statements or financial position, or whether it is a type of technical or statistical analysis based on the historical behaviour of the person or entity being evaluated, or on the expert judgement of an individual, among others. In describing the model, the entity must avoid generating mistaken perceptions in the public regarding the degree of sophistication of the computer algorithm used. For example, the fact that the recommendation emanates from simple mathematical and logical operations carried out in a spreadsheet must not be presented as if it emanated from a computer algorithm.

c) The existence of conflicts of interest that emanate from the business model or its revenue sources, and how they are managed.

In addition, this information must be submitted to the Commission (CMF) no later than the fifth business day following the Commission's authorization of the provision of this service. Modifications to that information must be submitted to the Commission within five business days following the respective modification.

At the time of carrying out the evaluation, the following information must be delivered to the client:

a) If the person requesting the credit evaluation is the same natural person requiring the financing, the credit adviser must inform that person of the economic, financial, and legal consequences of over-indebtedness.

b) The conflicts of interest arising between the service provider and the client in particular, and how they may affect the client if not adequately resolved.

It shall not be necessary to deliver the information referred to in subparagraphs a) and b) of the preceding paragraph in the case of clients with the status of Institutional Investor, and of Qualified Investor from among those indicated in items 2, 3, and 4 of Section II of Norma de Carácter General N° 216.

### Original Spanish

> "B. ASESORÍA CREDITICIA
>
> La siguiente información deberá ser puesta a disposición del público en todo momento, debidamente actualizada:
>
> a) Descripción general de la estructura de comisiones o remuneraciones que recibe el asesor, esto es, señalar si cobra una comisión fija o variable a clientes; recibe una retribución por referir clientes a otro prestador de servicios; o recibe una retribución por el monto del crédito colocado; entre otros.
>
> b) Descripción del modelo de asesoría utilizado, esto es, si la evaluación emana de personas, algoritmos informáticos o una combinación de ambos; y, en términos generales, sobre la base de qué elementos se efectúa la evaluación, por ejemplo, si emana de un análisis fundamental que toma como base los estados financieros o situación financiera, o si es un tipo de análisis técnico o estadístico sobre la base del comportamiento histórico de la persona o entidad evaluada, o del juicio experto de un individuo, entre otros. En la descripción del modelo la entidad deberá evitar generar percepciones erradas en el público respecto al grado de sofisticación del algoritmo informático utilizado. Por ejemplo, que la recomendación emane de operaciones matemáticas y lógicas simples realizadas en una planilla de cálculo, no debe presentarse como que emana de un algoritmo informático.
>
> c) La existencia de conflictos de intereses que emanen del modelo de negocios o sus fuentes de ingresos, y cómo los gestiona.
>
> Además, dicha información deberá ser remitida a la Comisión a más tardar al quinto día hábil de autorizada la prestación de este servicio por la Comisión. Las modificaciones a esa información deberán ser remitidas a la Comisión, dentro de los cinco días hábiles siguientes a la modificación respectiva.
>
> Al momento de efectuar la evaluación, deberá entregar al cliente la siguiente información:
>
> a) Si quien solicita la evaluación crediticia es la propia persona natural que requiere el financiamiento, el asesor crediticio deberá informar a esa persona respecto de las consecuencias económicas, financieras y jurídicas que tiene el sobre endeudamiento.
>
> b) Los conflictos de intereses que se susciten entre el prestador del servicio y el cliente en particular y cómo pueden afectar al cliente si no se resolvieren adecuadamente.
>
> No será necesario entregar la información a que se refieren las letras a) y b) del párrafo anterior, en caso de clientes que tengan la calidad de Inversionista Institucional, y de Inversionista Calificado de entre los señalados en los números 2, 3 y 4 de la Sección II de la Norma de Carácter General N°216."

> **TN:** NCG 524 amended this section by inserting a new paragraph between the public-disclosure block and the at-evaluation block ("Además, dicha información deberá ser remitida…"); the consolidated Spanish combines the retained NCG 502 text with that inserted paragraph. Verified against the 524 source PDF.

> **TN:** "sobre endeudamiento" (§III.B) and related concepts: the PDF renders the word as two words in §III.B ("sobre endeudamiento") but as a single compound in context; "over-indebtedness" is the standard English regulatory rendering and is used throughout.

### Cross-references
- Ley 21.521 Art. 12 — disclosure mandate this section implements.
- NCG 216 §II (items 2, 3, 4) — qualified investor sub-categories exempt from at-evaluation disclosures in this section.
- NCG 502 §III — general information-quality requirements applicable to all disclosures under this subsection.

> **Source:** NCG 502 §III.B (12-ene-2024), as amended by NCG 524 item C.b.1 (02-dic-2024).

---

## III.C — Crowdfunding Platform
**NCG anchor:** N° 502, Sección III, C
**Implements:** Ley 21.521 Art. 12 (disclosure / information obligations)
**Tags:** disclosure, information, crowdfunding-platform

### Plain-English text

The crowdfunding platform service provider must make available to the public at all times the following information, which must be kept duly updated:

a) General description of the commission or remuneration structure received by the platform — that is, indicating whether it charges a commission or fee to those who provide financing, to those who obtain financing, or to both, and the method for determining such commission or fee.

b) The existence of conflicts of interest that emanate from the business model or its revenue sources, and how they are managed.

c) Description of the mechanisms the platform has established to prevent the financing of fraudulent projects, money laundering, terrorism financing, proliferation of weapons of mass destruction, or the commission of other types of illicit activities through it.

d) Description of the mechanisms the platform has established to limit or adjust the degree of risk exposure that those who provide financing through it have in the projects, in accordance with the expectations or needs expressed by them.

e) Description of the processes the platform has established to analyse the economic, financial, and legal viability of the projects or of those who obtain financing through it as an intermediary, specifying the limit referred to in subparagraph d) of letter C of the preceding Section II, or, in the alternative, the specific circumstances or parameters by virtue of which they have been exempted from the processes mentioned therein.

In addition, this information must be submitted to the Commission (CMF) no later than the fifth business day following the Commission's authorization of the provision of this service. Modifications to that information must be submitted to the Commission within five business days following the respective modification.

At the time of disseminating a particular project or financing need, the following information must be delivered to those clients who will potentially provide the financing:

a) Information about the person who has the investment project or financing need, or who will be obligated to pay the obligation or will act as guarantor thereof, depending on the nature of the financing or investment.

1. In the case of natural persons, their identification data and the background information that is relevant to understanding their capacity to manage the investment project or to fulfil the obligations they will incur in connection with the financing obtained for the relevant financing need.

2. In the case of legal persons, their identification, their majority partners or shareholders and legal representative must be provided; the most relevant milestones that have materially affected them patrimonially in the last 2 years, if that had occurred; and a brief summary of the businesses, products, and services they currently develop and, in that context, a brief description of the industrial or economic sectors in which they operate, including, where applicable, a reference to the legal or regulatory framework that regulates or affects the industry in which it participates.

b) An explanation of the use to be made of the resources obtained through the financing, including the amount expected to be raised and the total amount of resources to be allocated to the same objective — that is, whether the financing obtained through the platform will be supplemented with other resources, indicating where they come from.

c) Mechanisms or tools that the platform will provide so that those providing the financing may monitor and verify the progress of the project and, where applicable, the payment of the debt as planned; keep informed of the status of the obligation owed to them; or channel concerns or problems arising in connection with the investment, financing, or payment of the obligation.

d) Description of the legal nature of the instrument through which the financing will be effected — that is, whether it is by means of shares in stock corporations or companies limited by shares, credit instruments, fund units or community interests, mutual loan agreements, crypto-assets, etc. Special emphasis must be placed on the rights, preferences, obligations, and means of exercising corporate rights, the supporting technology and protocols, and the risks associated therewith, specifying whether civil or natural rights are being acquired.

e) An explanation of how the financing round will be closed — whether in the event the requested financing is completed or not — indicating how the contribution and the consideration for the financing will be effected. For example, whether the financier will be put in direct contact with the person who holds the project or financing need, or whether it will be delivered to a third party.

f) Recommended level of exposure to financing risk — that is, for what types of risk-return-investment horizon needs the project is advisable. It shall not be necessary to deliver this information in the case of clients with the status of Institutional Investor, and of Qualified Investor from among those indicated in items 2, 3, and 4 of Section II of Norma de Carácter General N° 216.

In any event, entities may substitute the information obligations referred to in subparagraphs a) to f) of the preceding paragraph with other information that the platform itself defines, to the extent that the following cumulative conditions are met:

1) That the information provided in replacement of those established in this regulation fulfils the purpose of adequately protecting and informing the financing users of the platform of the risks, costs, and benefits of the project or need;

2) That the projects or financing needs have a maximum period of 12 months to pay the amounts owed in respect of the same users, including reprogrammings or refinancings; and

3) That the amounts financed for the person or entity obtaining the financing within 12 months do not exceed in total 100,000 UF, or that no person providing financing contributes more than 10 UF to the relevant project or need.

### Original Spanish

> "C. PLATAFORMA DE FINANCIAMIENTO COLECTIVO
>
> El prestador de servicios de plataformas de financiamiento colectivo deberá poner a disposición del público en todo momento, la siguiente información, que deberá mantenerse debidamente actualizada:
>
> a) Descripción general de la estructura de comisiones o remuneraciones que recibe la plataforma, esto es, señalar si cobra una comisión o remuneración a quienes financian, a quienes obtienen financiamiento, o a ambos, y el método de determinación de esa comisión o remuneración.
>
> b) La existencia de conflictos de intereses que emanen del modelo de negocios o sus fuentes de ingresos y cómo se gestionan.
>
> c) Descripción de los mecanismos que la plataforma ha establecido para prevenir que mediante ella se financien proyectos fraudulentos, lavado de activos, financiamiento del terrorismo, la proliferación de armas de destrucción masiva o la comisión de otro tipo de ilícitos.
>
> d) Descripción de los mecanismos que la plataforma ha establecido para acotar o ajustar el grado de exposición al riesgo que tienen en los proyectos quienes entregan financiamiento a través de ella, conforme a las expectativas o necesidades por ellos manifestadas.
>
> e) Descripción de los procesos que la plataforma ha establecido para analizar la viabilidad económica, financiera y jurídica de los proyectos o de quienes obtienen financiamiento por su intermedio, especificando el límite al que se refiere el literal d) de la letra C de la Sección II anterior, o bien, las circunstancias o parámetros específicos por las cuales se han eximido de los procesos mencionados.
>
> Además, dicha información deberá ser remitida a la Comisión a más tardar al quinto día hábil de autorizada la prestación de este servicio por la Comisión. Las modificaciones a esa información deberán ser remitidas a la Comisión, dentro de los cinco días hábiles siguientes a la modificación respectiva.
>
> El prestador de servicios de plataforma de financiamiento colectivo, respecto a un proyecto o necesidad de financiamiento en particular, deberá entregar a los clientes que potencialmente realizarán el financiamiento, la siguiente información:
>
> a) Información sobre quien tiene el proyecto de inversión o necesidad de financiamiento, o quien estará obligado al pago de la obligación o será garante de la misma, según la naturaleza del financiamiento o inversión.
>
> 1) Tratándose de personas naturales, los datos de identificación de las mismas y los antecedentes que resulten relevantes para comprender su capacidad para gestionar el proyecto de inversión o cumplir con las obligaciones que contrajere con el financiamiento que obtenga para la necesidad de financiamiento respectiva.
>
> 2) Tratándose de personas jurídicas, se deberá entregar su identificación, los socios o accionistas mayoritarios y representante legal; los hitos más relevantes que la hubieren afectado patrimonialmente en los últimos 2 años, en caso de que aquello hubiere ocurrido; y una breve reseña respecto a los negocios, productos y servicios que desarrolla en la actualidad y, en tal contexto, proveer una breve descripción de él o los sectores industriales o económicos en que se desarrollan, incluyendo, en caso de que corresponda, una referencia al marco legal o normativo que regule o que afecte la industria en la cual participa.
>
> b) Una explicación sobre el uso que se dará a los recursos que se obtengan con el financiamiento, incluyendo el monto que se espera recaudar y el monto total de recursos que se destinarán al mismo objetivo, esto es, si el financiamiento obtenido a través de la plataforma será complementado con otros recursos, señalando de donde provienen los mismos.
>
> c) Mecanismos o herramientas que la plataforma entregará para que los financistas puedan monitorear y verificar el desarrollo del proyecto y, cuando corresponda, el pago de la deuda conforme a lo planificado; interiorizarse del estado de la obligación que se le adeuda; o canalizar las inquietudes o problemas que se susciten con motivo de la inversión, financiamiento o pago de la obligación.
>
> d) Descripción de la naturaleza jurídica del instrumento a través del cual se concretará el financiamiento, esto es, si es mediante acciones de sociedades anónimas o de sociedades por acciones, títulos de crédito, cuotas de fondos o comunidades, contratos de mutuo, criptoactivos, etc. Se deberá hacer especial énfasis en los derechos, preferencias, obligaciones, formas de ejercer derechos societarios, tecnología y protocolos de soporte, y riesgos asociados al mismo, especificando si se adquieren obligaciones civiles o naturales.
>
> e) Una explicación de cómo se procederá al momento de cerrar la ronda de financiamiento, ya sea en el caso que se complete el financiamiento solicitado o no, indicando cómo se deberá proceder para materializar el aporte y la contraprestación al financiamiento. Por ejemplo, si el financista quedará en contacto directo con quien tiene el proyecto o necesidad de financiamiento, o si se deberá entregar a un tercero.
>
> f) Nivel recomendado de exposición al riesgo de financiamiento, esto es, para qué tipos de necesidades de riesgo-retorno-horizonte de inversión el proyecto es aconsejable. No será necesario entregar esta información, en caso de clientes que tengan la calidad de Inversionista Institucional, y de Inversionista Calificado de entre los señalados en los números 2, 3 y 4 de la Sección II de la Norma de Carácter General N°216.
>
> Con todo, las entidades podrán sustituir las obligaciones de información a que se refieren las letras a) a la f) del párrafo anterior, por otras que la propia plataforma defina, en la medida que se cumplan las siguientes condiciones copulativas:
>
> 1) Que la información que provean en reemplazo de las establecidas en esta normativa cumpla el objeto de proteger e informar adecuadamente a los financistas usuarios de la plataforma los riesgos, costos y beneficios del proyecto o necesidad;
>
> 2) Que los proyectos o necesidades de financiamiento que se financien tengan un plazo máximo para pagar lo adeudado de 12 meses respecto de los mismos usuarios, incluidas las reprogramaciones o refinanciamientos; y
>
> 3) Que los montos financiados para la persona o entidad que obtiene el financiamiento dentro de 12 meses no supere en total las 100.000 UF, o que ninguna persona que entrega financiamiento aporte más de 10UF para el proyecto o necesidad respectiva."

> **TN:** NCG 524 (item C.c.3) spliced text into this section: it inserted a new paragraph between the public-disclosure block and the at-dissemination block ("Además, dicha información deberá ser remitida…"). The consolidated Spanish is faithful to NCG 502 as amended by NCG 524 (verified against the 524 source PDF), but is not a contiguous passage in either single source PDF, so the dual-PDF round-trip excludes this section and it was verified manually.

> **TN:** "contratos de mutuo" in item d) is rendered "mutual loan agreements" — in Chilean civil law, a "mutuo" is a loan contract under which the borrower receives fungible assets and must return equivalents; "mutual loan" is the established English rendition in Chilean financial regulatory texts.

> **TN:** "obligaciones civiles o naturales" in item d) refers to the Chilean civil law distinction between enforceable obligations (civiles) and unenforceable natural obligations (naturales); rendered literally as "civil or natural rights/obligations" with the parenthetical clarification in the English body.

### Cross-references
- Ley 21.521 Art. 12 — disclosure mandate this section implements.
- Ley 18.045 Art. 4 Bis(f) — qualified investor definition; exemption from entire Section III applies when service is provided exclusively to this class.
- NCG 502 §II.C(d) — viability-analysis threshold (20,000 UF) whose exemption must be disclosed under item e) of the public-disclosure block (cross-reference updated from e) to d) by NCG 524 item C.c.2).
- NCG 216 §II (items 2, 3, 4) — qualified investor sub-categories exempt from delivery of item f) of the at-dissemination block.
- NCG 502 §III — general information-quality requirements applicable to all disclosures under this subsection.

> **Source:** NCG 502 §III.C (12-ene-2024), as amended by NCG 524 items C.c.1–C.c.9 (02-dic-2024).

---

## III.D — Alternative Trading System
**NCG anchor:** N° 502, Sección III, D
**Implements:** Ley 21.521 Art. 12 (disclosure / information obligations)
**Tags:** disclosure, information, alternative-trading-system

### Plain-English text

The following information must be made available to the public at all times, duly updated:

a) The internal regulations referred to in subparagraph d) of numeral 2 of Article 7 of Ley N° 21.521.

b) General description of the commission or remuneration structure received by the system — that is, indicating whether it charges a fixed or variable commission or fee, the amount or percentage, and the method for its determination.

c) The existence of conflicts of interest that emanate from the business model or its revenue sources, and how they are managed.

d) Description of the instrument admission rules (normas de admisión de los instrumentos financieros), highlighting the mechanisms established to prevent financial instruments that are fraudulent or serve a fraudulent purpose from being traded on the system.

e) Description of the principal characteristics of the instruments admitted to trading, as well as the recommended level of risk exposure — that is, for what types of risk-return-investment horizon needs the instrument is advisable. In the case of virtual assets (activos virtuales), access must also be facilitated to the public document that has been prepared to refer to the technical specifications regarding the technology and relevant aspects underlying the instrument.

f) Quotation prices, units, and amounts per transaction, with a lag of less than 5 minutes from the time the quotation or negotiation was effected.

g) Closing prices, units, and total daily amounts traded for each instrument, at the close of the trading day or at 00:00 of the following day if the system has no closing time.

h) Identification of instruments that have been cancelled or suspended from trading and the reasons therefor, in accordance with the rules established for those purposes.

i) Description of operational risk management policies and the service levels committed in terms of availability, performance, and continuity, as well as the manner and timing in which incidents that compromise the availability and security of information will be reported. In addition, how proceedings will be conducted in the event such incidents occur for entities of Block 3 in accordance with Section IV.C.3.

In addition, the information referred to in subparagraphs b) and c) must be submitted to the Commission (CMF) no later than the fifth business day following the Commission's authorization of the provision of this service. Modifications to that information must be submitted to the Commission within five business days following the respective modification.

The following information must be made available to the client at the time of the negotiation:

a) The terms agreed upon in the negotiation — that is, instrument, counterparty, price, units, and amount, with a clear indication of the currency in which those terms were agreed.

b) The terms, date, and settlement procedure for the transactions and, in the event that the instruments traded are held in custody, that fact together with the identification of the entity responsible for such custody.

It shall not be necessary to deliver the information referred to in subparagraphs a) and b) of the preceding paragraph in the case of clients with the status of Institutional Investor, and of Qualified Investor from among those indicated in items 2, 3, and 4 of Section II of Norma de Carácter General N° 216.

### Original Spanish

> "D. SISTEMA ALTERNATIVO DE TRANSACCIÓN
>
> La siguiente información deberá ser puesta a disposición del público en todo momento, debidamente actualizada:
>
> a) Reglamentación interna a que se refiere el literal d) del numeral 2 del artículo 7 de la Ley N°21.521.
>
> b) Descripción general de la estructura de comisiones o remuneraciones que recibe el sistema, esto es, señalar si cobra una comisión o remuneración fija o variable, el monto o porcentaje, y la forma de su determinación.
>
> c) La existencia de conflictos de intereses que emanen del modelo de negocios o sus fuentes de ingresos y cómo se gestionan.
>
> d) Descripción de las normas de admisión de los instrumentos financieros, destacando los mecanismos establecidos para prevenir que en el sistema se negocien instrumentos financieros que resulten o tengan un fin fraudulento.
>
> e) Descripción de las principales características de los instrumentos admitidos a cotización, así como el nivel recomendado de exposición al riesgo, esto es, para qué tipos de necesidades de riesgo-retorno-horizonte de inversión el instrumento es aconsejable. Tratándose de activos virtuales, además se deberá facilitar el acceso al documento público que se hubiere elaborado para referirse a las especificaciones técnicas respecto de la tecnología y aspectos relevantes que subyacen al instrumento.
>
> f) Precios de cotización, unidades y montos por transacción, con un desfase inferior a los 5 minutos de efectuada la cotización o negociación.
>
> g) Precios de cierre, unidades y montos totales diarios negociados de cada instrumento, al cierre del día o a las 00:00 del día siguiente si el sistema no tuviere horario de cierre.
>
> h) Identificación de los instrumentos que hubieren sido cancelados o suspendidos de negociación y las razones de aquello, conforme a las reglas establecidas para esos efectos.
>
> i) Descripción de las políticas de gestión de riesgo operacional y los niveles de servicio comprometidos en cuanto a disponibilidad, desempeño y continuidad, así como la forma y oportunidad en que serán informados los incidentes que comprometan la disponibilidad y seguridad de la información. A su vez, la forma en que se procederá en caso de que aquéllos se produzcan para las entidades del Bloque 3 de acuerdo con la Sección IV.C.3.
>
> Además, la información a que se refieren las letras b) y c) deberá ser remitida a la Comisión a más tardar al quinto día hábil de autorizada la prestación de este servicio. Las modificaciones a esa información deberán ser remitidas a la Comisión, dentro de los cinco días hábiles siguientes a la modificación respectiva.
>
> La siguiente información deberá ser puesta a disposición del cliente al momento de la negociación:
>
> a) Condiciones pactadas en la negociación, esto es, instrumento, contraparte, precio, unidades y monto, con indicación clara de la moneda en la que se acordaron esas condiciones.
>
> b) Condiciones, fecha y procedimiento de liquidación de las operaciones y, en caso de que los instrumentos negociados queden en custodia, ese hecho junto a la identificación de la entidad encargada de la misma.
>
> No será necesario entregar la información a que se refieren las letras a) y b) del párrafo anterior, en caso de clientes que tengan la calidad de Inversionista Institucional, y de Inversionista Calificado de entre los señalados en los números 2, 3 y 4 de la Sección II de la Norma de Carácter General N°216."

> **TN:** NCG 524 (item C.d.3) amended this section by inserting a new paragraph between the public-disclosure block and the at-negotiation block ("Además, la información a que se refieren las letras b) y c)…"); the consolidated Spanish combines the retained NCG 502 text with that inserted paragraph. Verified against the 524 source PDF.

### Cross-references
- Ley 21.521 Art. 12 — disclosure mandate this section implements.
- Ley 21.521 Art. 7 numeral 2 literal d) — the statutory provision for internal regulations, now cited directly in item a) per NCG 524 amendment C.d.1.
- Ley 18.045 Art. 4 Bis(f) — qualified investor definition; exemption from entire Section III applies when service is provided exclusively to this class.
- NCG 216 §II (items 2, 3, 4) — qualified investor sub-categories exempt from at-negotiation disclosures in this section.
- NCG 502 §II.D(f) — internal regulations whose disclosure is required under item a) of the public-disclosure block.
- NCG 502 §IV.C.3 — Block 3 operational risk framework referenced in item i) (reference updated from IV.C to IV.C.3 by NCG 524 item C.d.2).
- NCG 502 §III — general information-quality requirements applicable to all disclosures under this subsection.

> **Source:** NCG 502 §III.D (12-ene-2024), as amended by NCG 524 items C.d.1–C.d.3 (02-dic-2024).

---

## III.E — Order Routing
**NCG anchor:** N° 502, Sección III, E
**Implements:** Ley 21.521 Art. 12 (disclosure / information obligations)
**Tags:** disclosure, information, order-routing

### Plain-English text

The following information must be made available to the public at all times, duly updated:

a) General description of the commission or remuneration structure received by the router (enrutador) — that is, indicating whether it charges clients for channelling orders or receives a fee from the intermediary or system to which it channels the order, or from the placer or issuer of the instruments that are the subject of the order; and whether that commission or fee is fixed or variable, the amount or percentage, and the method for its determination.

b) The existence of conflicts of interest that emanate from the business model or its revenue sources, and how they are managed.

c) Description of operational risk management policies and the service levels committed in terms of availability, performance, and continuity.

d) The manner and timing in which incidents that compromise the availability and security of information will be reported.

e) Identification of the guarantees the entity has established to indemnify the losses that may be caused to clients, as well as the description of the manner or mechanisms for executing and assigning those guarantees.

Prior to channelling the order, the client must be informed of the conflicts of interest arising between the service provider and the client in particular and how they may affect the client if not adequately resolved. Once the order has been channelled, the fact that it was received and channelled must be communicated, as well as the confirmation of its receipt and eventual execution by the intermediary, alternative system, or third party to which that order was routed.

It shall not be necessary to deliver the information referred to in the two preceding paragraphs in the case of clients with the status of Institutional Investor, and of Qualified Investor from among those indicated in items 2, 3, and 4 of Section II of Norma de Carácter General N° 216.

### Original Spanish

> "E. ENRUTAMIENTO DE ÓRDENES
>
> La siguiente información deberá ser puesta a disposición del público en todo momento, debidamente actualizada:
>
> a) Descripción general de la estructura de comisiones o remuneraciones que recibe el enrutador, esto es, señalar si cobra a los clientes por canalizar órdenes o percibe una retribución del intermediario o sistema al que canaliza la orden, o del colocador o emisor de los instrumentos objeto de la orden; y si esa comisión o remuneración es fija o variable, el monto o porcentaje, y la forma de su determinación.
>
> b) La existencia de conflictos de intereses que emanen del modelo de negocios o sus fuentes de ingresos y cómo los gestiona.
>
> c) Descripción de las políticas de gestión de riesgo operacional y los niveles de servicio comprometidos en cuanto a disponibilidad, desempeño y continuidad.
>
> d) Forma y oportunidad en que serán informados los incidentes que comprometan la disponibilidad y seguridad de la información.
>
> e) Identificación de las garantías que la entidad haya constituido para indemnizar los perjuicios que se puedan producir a clientes, así como la descripción de la forma o mecanismos de ejecución y asignación de esas garantías.
>
> Previo a canalizar la orden se deberá informar al cliente los conflictos de intereses que se susciten entre el prestador del servicio y el cliente en particular y cómo pueden afectar al cliente si no se resolvieren adecuadamente. Una vez que sea canalizada, se deberá comunicar el hecho de que se recibió y canalizó la orden, así como la confirmación de su recepción y eventual ejecución por parte del intermediario, sistema alternativo o tercero al que se hubiere derivado esa orden.
>
> No será necesario entregar la información a que se refieren los dos párrafos anteriores, en caso de clientes que tengan la calidad de Inversionista Institucional, y de Inversionista Calificado, de entre los señalados en los números 2, 3 y 4 de la Sección II de la Norma de Carácter General N°216."

> **TN:** NCG 524 item C.e.1 replaced the last two paragraphs of §III.E with the new text above. The old structure had a two-letter (a/b) at-order block and a separate exemption sentence; the new structure collapses those into two prose paragraphs (the at-order obligation and the exemption). The old anchors for "La siguiente información deberá ser puesta a disposición del cliente al momento de, o previo a, canalizar la orden" and letters a) and b) thereunder have been superseded and are deleted.

> **TN:** "enrutador" is rendered "router" in the parenthetical gloss and "the router" in the English body — it refers to the PSF providing the order routing service, not a network device.

### Cross-references
- Ley 21.521 Art. 12 — disclosure mandate this section implements.
- NCG 216 §II (items 2, 3, 4) — qualified investor sub-categories exempt from the at-order-routing disclosures in this section.
- NCG 502 §V — guarantee framework; the guarantees identified under item e) are constituted pursuant to §V.
- NCG 502 §III — general information-quality requirements applicable to all disclosures under this subsection.

> **Source:** NCG 502 §III.E (12-ene-2024), as amended by NCG 524 item C.e.1 (02-dic-2024).

---

## III.F — Intermediation of Financial Instruments
**NCG anchor:** N° 502, Sección III, F
**Implements:** Ley 21.521 Art. 12 (disclosure / information obligations)
**Tags:** disclosure, information, intermediation, financial-instruments

### Plain-English text

The following information must be made available to the public at all times, duly updated:

a) General description of the commission or remuneration structure received by the entity — that is, indicating whether it charges clients for executing orders; whether it receives a fee from the issuer of the instruments that are the subject of the order or from third parties; and whether that commission or fee is fixed or variable, the amount or percentage, and the method for its determination.

b) The existence of conflicts of interest that emanate from the business model or its revenue sources, and how they are managed.

c) Description of operational risk management policies and the service levels committed in terms of availability, performance, and continuity.

d) The manner and timing in which incidents that compromise the availability and security of information will be reported.

e) Identification of the guarantees the entity has established to indemnify the losses that may be caused to clients, as well as the description of the manner or mechanisms for executing and assigning those guarantees.

f) Description of the principal policies, procedures, mechanisms, and controls implemented by the entity with the aim of preserving its solvency and liquidity.

g) Situations that are pending resolution and that may materially compromise its solvency, liquidity, or capacity to fulfil its obligations.

The following information must be made available to the client prior to receiving and executing the order:

a) The conflicts of interest arising between the service provider and the client in particular, how they will be managed, and how they may affect the client if not adequately resolved.

b) Any material situation of which the entity is aware that relates to the instrument that is the subject of the order and that, for a person with average economic and financial knowledge, is relevant to their investment decisions.

Once the order is executed, the client must be informed of the fact that it was received and executed, as well as the conditions under which it was executed.

It shall not be necessary to deliver the information referred to in subparagraphs a) and b) of the second paragraph above in the case of clients with the status of Institutional Investor, and of Qualified Investor from among those indicated in items 2, 3, and 4 of Section II of Norma de Carácter General N° 216.

### Original Spanish

> "F. INTERMEDIACIÓN DE INSTRUMENTOS FINANCIEROS
>
> La siguiente información deberá ser puesta a disposición del público en todo momento, debidamente actualizada:
>
> a) Descripción general de la estructura de comisiones o remuneraciones que recibe la entidad, esto es, señalar si cobra a los clientes por ejecutar órdenes; si percibe una retribución del emisor de los instrumentos objeto de la orden o de terceros; y si esa comisión o remuneración es fija o variable, el monto o porcentaje, y la forma de su determinación.
>
> b) La existencia de conflictos de intereses que emanen del modelo de negocios o sus fuentes de ingresos y cómo los gestiona.
>
> c) Descripción de las políticas de gestión de riesgo operacional y los niveles de servicio comprometidos en cuanto a disponibilidad, desempeño y continuidad.
>
> d) Forma y oportunidad en que serán informados los incidentes que comprometan la disponibilidad y seguridad de la información.
>
> e) Identificación de las garantías que la entidad haya constituido para indemnizar los perjuicios que se puedan producir a clientes, así como la descripción de la forma o mecanismos de ejecución y asignación de esas garantías.
>
> f) Descripción de las principales políticas, procedimientos, mecanismos y controles que ha implementado la entidad con el objeto de preservar su solvencia y liquidez.
>
> g) Situaciones que están pendientes de resolución y que pueden comprometer de manera relevante su solvencia, liquidez o capacidad de cumplir sus obligaciones.
>
> La siguiente información deberá ser puesta a disposición del cliente previo a recibir y ejecutar la orden:
>
> a) Los conflictos de intereses que se susciten entre el prestador del servicio y el cliente en particular, cómo se gestionarán y cómo pueden afectar al cliente si no se resolvieren adecuadamente.
>
> b) Cualquier situación material que esté en conocimiento de la entidad que diga relación con el instrumento objeto de la orden y que, para una persona con conocimientos económicos financieros promedio, sea relevante para sus decisiones de inversión.
>
> Una vez que se ejecute la orden, se le deberá comunicar el hecho de que se recibió y ejecutó la orden, así como las condiciones en las que fue ejecutada.
>
> No será necesario entregar la información a que se refieren las letras a) y b) del segundo inciso, en caso de clientes que tengan la calidad de Inversionista Institucional, y de Inversionista Calificado de entre los señalados en los números 2, 3 y 4 de la Sección II de la Norma de Carácter General N°216."

> **TN:** NCG 524 item C.f.1 replaced the two last paragraphs of §III.F with three new paragraphs. The old structure had a three-letter (a/b/c) at-execution block with a/b subject to the qualified-investor exemption; the new structure has a two-letter (a/b) pre-execution disclosure block, a separate sentence for post-execution confirmation, and an exemption covering only letters a) and b) of the second paragraph (the pre-execution block). Old letter a) ("El hecho de que se recibió y ejecutó la orden…") is now a standalone paragraph; old letter c) has been deleted and the substance of former c) (conflicts of interest) moved to new letter a). The old anchor for the three-letter at-execution block (a/b/c) and the old exemption referencing "letras b) y c)" are superseded.

### Cross-references
- Ley 21.521 Art. 12 — disclosure mandate this section implements.
- NCG 216 §II (items 2, 3, 4) — qualified investor sub-categories exempt from pre-execution disclosures a) and b) in this section.
- NCG 502 §V — guarantee framework; the guarantees identified under item e) are constituted pursuant to §V.
- NCG 502 §III — general information-quality requirements applicable to all disclosures under this subsection.

> **Source:** NCG 502 §III.F (12-ene-2024), as amended by NCG 524 item C.f.1 (02-dic-2024).

---

## III.G — Custody of Financial Instruments
**NCG anchor:** N° 502, Sección III, G
**Implements:** Ley 21.521 Art. 12 (disclosure / information obligations)
**Tags:** disclosure, information, custody, financial-instruments

### Plain-English text

The following information must be made available to the public at all times, duly updated:

a) General description of the commission or remuneration structure received by the entity — that is, indicating whether it charges clients for storing keys, documentation, or instruments; whether that fee is fixed or variable; and the amount or percentage, and the method for its determination.

b) The existence of conflicts of interest that emanate from the business model or its revenue sources, and how they are managed.

c) Description of operational risk management policies and the service levels committed in terms of availability, performance, and continuity.

d) The manner and timing in which incidents that compromise the availability and security of information will be reported.

e) Identification of the guarantees the entity has established to indemnify the losses that may be caused to clients, as well as the description of the manner or mechanisms for executing and assigning those guarantees.

f) Situations that are pending resolution and that may materially compromise its solvency, liquidity, or capacity to fulfil its obligations.

The following information must be made available to the client prior to receiving the instruments in custody:

a) The conflicts of interest arising between the service provider and the client in particular, and how they may affect the client if not adequately resolved.

b) Any situation that may materially affect the entity's capacity to adequately safeguard the instruments in custody or to return them to their owners.

c) Any material situation of which the entity is aware that relates to the instruments in custody and that is relevant for the client to adequately safeguard their interests.

d) Whether or not the entity will be responsible for exercising the corporate rights (derechos societarios) inherent in the financial instruments, and, if so, the policies for exercising such rights.

Once the instruments are received in custody, the client must be informed of that fact.

It shall not be necessary to deliver the information referred to in subparagraphs a) to d) of the preceding paragraph in the case of clients with the status of Institutional Investor, or of Qualified Investor from among those indicated in items 2, 3, and 4 of Section II of Norma de Carácter General N° 216.

### Original Spanish

> "G. CUSTODIA DE INSTRUMENTOS FINANCIEROS
>
> La siguiente información deberá ser puesta a disposición del público en todo momento, debidamente actualizada:
>
> a) Descripción general de la estructura de comisiones o remuneraciones que recibe la entidad, esto es, señalar si cobra a los clientes por almacenar claves, documentación o instrumentos; si esa retribución es fija o variable, y el monto o porcentaje, y la forma de su determinación.
>
> b) La existencia de conflictos de intereses que emanen del modelo de negocios o sus fuentes de ingresos y cómo los gestiona.
>
> c) Descripción de las políticas de gestión de riesgo operacional y los niveles de servicio comprometidos en cuanto a disponibilidad, desempeño y continuidad.
>
> d) Forma y oportunidad en que serán informados los incidentes que comprometan la disponibilidad y seguridad de la información.
>
> e) Identificación de las garantías que la entidad haya constituido para indemnizar los perjuicios que se puedan producir a clientes, así como la descripción de la forma o mecanismos de ejecución y asignación de esas garantías.
>
> f) Situaciones que están pendientes de resolución y que pueden comprometer de manera relevante su solvencia, liquidez o capacidad de cumplir sus obligaciones.
>
> La siguiente información deberá ser puesta a disposición del cliente previo a recibir los instrumentos en custodia:
>
> a) Los conflictos de intereses que se susciten entre el prestador del servicio y el cliente en particular y cómo pueden afectar al cliente si no se resolvieren adecuadamente.
>
> b) Cualquier situación que pueda afectar de manera material la capacidad de la entidad de resguardar adecuadamente los instrumentos en custodia o de restituirlos a sus dueños.
>
> c) Cualquier situación material que esté en conocimiento de la entidad que diga relación con los instrumentos en custodia y que sea relevante para que el cliente pueda resguardar adecuadamente sus intereses.
>
> d) Si la entidad quedará o no a cargo de ejercer los derechos societarios inherentes a los instrumentos financieros y, en caso afirmativo, las políticas de ejercicio de tales derechos.
>
> Una vez que se reciban en custodia los instrumentos, se deberá comunicar al cliente ese hecho.
>
> No será necesario entregar la información a que se refieren las letras a) a la d) del párrafo anterior, en caso de clientes que tengan la calidad de Inversionista Institucional, o de Inversionista Calificado de entre los señalados en los números 2, 3 y 4 de la Sección II de la Norma de Carácter General N°216."

> **TN:** NCG 524 item C.g.1 replaced the heading of the second paragraph and deleted old letter a) ("El hecho de que se recibió el instrumento en custodia"), renumbering old b)–e) to a)–d). The deletion of old letter a) and the renumbering of old letters b)–e) to a)–d) are reflected above. The post-custody notification ("Una vez que se reciban en custodia los instrumentos…") was added as a standalone sentence by NCG 524 item C.g.2, which also replaced the old last paragraph (the exemption referencing "letras b) a la e)") with two new final paragraphs: the notification sentence and the updated exemption covering "letras a) a la d)".

> **TN:** "derechos societarios" is rendered "corporate rights" — in the context of financial instruments held in custody (shares, fund units, etc.), these are the rights attaching to the instrument as a corporate or participatory right (voting, dividend, redemption), as distinguished from mere contractual or property rights. "Shareholder rights" would be narrower and less accurate given that the instruments include fund units and other non-share instruments.

### Cross-references
- Ley 21.521 Art. 12 — disclosure mandate this section implements.
- NCG 216 §II (items 2, 3, 4) — qualified investor sub-categories exempt from pre-custody disclosures a) through d) in this section (updated from b)–e) per NCG 524 item C.g.1/g.2).
- NCG 502 §V — guarantee framework; the guarantees identified under item e) are constituted pursuant to §V.
- NCG 502 §III — general information-quality requirements applicable to all disclosures under this subsection.

> **Source:** NCG 502 §III.G (12-ene-2024), as amended by NCG 524 items C.g.1–C.g.2 (02-dic-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/seccion-04a-gobierno-asesoria-inversion.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/seccion-04a-gobierno-asesoria-inversion.md

# NCG 502 — Sección IV.A: Corporate Governance & Risk Management — Investment Advisory (Gobierno Corporativo y Gestión de Riesgos — Asesoría de Inversión)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

## IV — Corporate Governance and Risk Management
**NCG anchor:** N° 502, Sección IV
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, psf

### Plain-English text

Section IV sets corporate-governance and risk-management obligations by service type (A–E). The provisions of this section must be observed proportionally, having regard to the nature of the entity, its business model, and organisational structure, in a manner that renders it capable of having strategic responses appropriate to the risks inherent in its lines of business, and consistent with the economic and financial viability of the entity.

Where a PSF provides more than one of the services regulated by Title II of Ley N° 21.521, the entity must comply with the corporate-governance and risk-management requirements applicable to each of them. The policies that the entity must establish by virtue of this section may be contained in a single document or manual. Likewise, the entity must establish the procedures for implementing the policies defined and approved by the board of directors or equivalent body.

Notwithstanding the foregoing, all entities subject to this regulation shall not be exempt from complying with the obligations regarding personal data established by Ley N° 21.521.

### Original Spanish

> "IV. GOBIERNO CORPORATIVO Y GESTIÓN DE RIESGOS
>
> Las disposiciones expuestas en la presente sección deben observarse de manera proporcional, atendiendo a la naturaleza de la entidad, su modelo de negocios y estructura organizacional; de manera de compatibilizar la capacidad de contar con respuestas estratégicas idóneas para los riesgos inherentes a las líneas de negocios, con la viabilidad económica y financiera de la entidad.
>
> En caso de prestar más de un servicio de los regulados por el Título II de la ley N° 21.521, la entidad deberá cumplir los requisitos de gobierno corporativo y gestión de riesgos aplicables a cada uno de ellos. Las políticas que la entidad deba establecer en virtud de esta sección podrán estar contenidas en un mismo documento o manual. Asimismo, la entidad deberá establecer los procedimientos para la implementación de las políticas definidas y aprobadas por el directorio.
>
> Sin perjuicio de lo anterior, todas las entidades objeto de la presente normativa no podrán exceptuarse del cumplimiento de las obligaciones que en materia de datos personales establece la ley N° 21.521."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.A–§IV.E — per-service subsections setting out specific governance and risk-management obligations.

> **Source:** NCG 502 §IV (12-ene-2024).

---

## IV.A — Investment Advisory
**NCG anchor:** N° 502, Sección IV, A
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, investment-advisory

### Plain-English text

This subsection sets out the corporate-governance and risk-management obligations applicable to Financial-Service Providers (PSFs) that provide the investment advisory service.

### Original Spanish

> "A. ASESORÍA DE INVERSIÓN"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this subsection implements.
- NCG 502 §IV — general proportionality framework applicable to all subsections of Section IV.

> **Source:** NCG 502 §IV.A (12-ene-2024).

---

## IV.A.1 — Responsibility of the Board of Directors or Equivalent Body
**NCG anchor:** N° 502, Sección IV, A.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, board, investment-advisory

### Plain-English text

The Board of Directors or Equivalent Body (Directorio u Órgano Equivalente) of the entity is the body responsible for approving and authorising risk-management and internal-control policies, at least once a year or with the frequency necessary in the event of significant changes to the established policies, leaving evidence thereof. For these purposes, the board of directors or equivalent body must comply with the following risk-management requirements:

a) Establish the mission, vision, and strategic objectives, taking into account the responsibilities that the applicable regulatory framework imposes on the entity.

b) Approve risk-management policies that are consistent with the strategic objectives and the regulatory framework.

c) Periodically evaluate the adequacy of the resources of the bodies responsible for risk management.

d) Approve the code of conduct, which must reflect the organisational values and principles and establish guidelines for the conduct of the entity's personnel.

e) Establish an adequate organisational structure for the entity's risk management, taking into account the following:

1) The administration and control of all relevant risks arising from the development of its activities. In this regard, the organisational structure must be appropriate in relation to the volume of business; the number and type of clients of the entity; the complexity of its relationships with other entities; among other aspects.

2) The definition of roles, competencies, and responsibilities that enable the entity to carry out its activities and adequately manage the risks it faces. This includes the appropriate segregation of duties and functions — especially those which, if performed by the same person, could give rise to errors that go undetected or that expose the entity or its participants to undue risks — and between risk-generating areas and the areas that control them.

3) The implementation of the risk-management function, in accordance with what is described in subparagraph A.3 of this Section.

f) Establish personnel-hiring policies that ensure the entity has staff with the appropriate experience to carry out their functions, and ensure that it has qualified human resources for risk management. In the case of personnel who provide advisory services to clients, they must comply with the requirements established in the authorisation requirements for the provision of services.

g) Implement remuneration and compensation policies for those who provide services to the entity, which must consider at least the manner or mechanism by which it will be prevented and verified that the remunerations and compensations do not give rise to or exacerbate conflicts of interest on the part of those who manage the resources of the entity itself and of those who advise or maintain commercial relationships with clients.

h) The board of directors or equivalent body must evaluate the appropriateness of forming a Risk Management Committee or a similar body that allows it to address and monitor relevant business matters, relating to matters such as conflicts of interest, information security, among others. The grounds considered by the board of directors or equivalent body for evaluating the formation of committees or similar bodies must be duly documented.

i) Ensure that the minutes or equivalent documentation reflect the principal matters addressed in the sessions of the board of directors or equivalent body and the committees, as well as the policies referred to above. All material prepared or presented to the board of directors or equivalent body or the committees must be duly documented and archived in accordance with the applicable general regulations on the matter, and must be permanently available for examination at the request of the Commission (CMF).

### Original Spanish

> "A.1. RESPONSABILIDAD DEL DIRECTORIO U ÓRGANO EQUIVALENTE
>
> El Directorio u órgano equivalente de la entidad es la instancia responsable de aprobar y autorizar las políticas de gestión de riesgos y control interno, como mínimo una vez al año o con la frecuencia necesaria en caso de que se produzcan cambios significativos en las políticas establecidas, dejando evidencia de ello. Para esos efectos, el directorio u órgano equivalente deberá dar cumplimiento a los requisitos de gestión de riesgos que se señalan a continuación:
>
> a) Establecer la misión, visión y objetivos estratégicos, teniendo en consideración las responsabilidades que el marco regulatorio vigente establece para la entidad.
>
> b) Aprobar políticas de gestión de riesgos que sean coherentes con los objetivos estratégicos y el marco regulatorio.
>
> c) Evaluar periódicamente la suficiencia de recursos de las instancias encargadas de la gestión de riesgos.
>
> d) Aprobar el código de conducta, que dé cuenta de los valores y principios organizacionales y establezca directrices en el actuar del personal de la entidad.
>
> e) Establecer una estructura organizacional adecuada para la gestión de riesgos de la entidad, que considere lo siguiente:
>
> 1) La administración y el control de todos los riesgos pertinentes derivados del desarrollo de sus actividades. En ese tenor, la estructura organizacional debe ser la adecuada en relación con el volumen de negocios; el número y tipo de clientes de la entidad; la complejidad de las relaciones con otras entidades, entre otros aspectos.
>
> 2) La definición de los roles, competencias y responsabilidades que permitan realizar sus actividades y gestionar adecuadamente los riesgos que enfrenta la entidad. Lo anterior involucra la segregación apropiada de los deberes y las funciones claves, especialmente aquéllas que, si fueran realizadas por una misma persona, puedan dar lugar a errores que no se detecten o que expongan a la entidad o sus participantes a riesgos indebidos; y entre las áreas generadoras de riesgo y de control de los mismos.
>
> 3) La implementación de la función de gestión de riesgos, de conformidad con lo descrito en el literal A.3. de esta Sección.
>
> f) Establecer políticas de contratación de empleados que aseguren que la entidad disponga de personal con la debida experiencia para desempeñar sus funciones, y velar porque se cuente con el recurso humano calificado para la gestión de riesgos. En el caso del personal que efectúe asesorías a los clientes, deberá cumplir con lo establecido en los requisitos de autorización para la prestación de servicios.
>
> g) Implementar políticas de remuneración y compensación para quienes presten servicios a la entidad, las cuales considerarán al menos la forma o mecanismo mediante el que se prevendrá y verificará que con las remuneraciones y compensaciones no se produzcan o exacerben conflictos de intereses por parte de quienes gestionan recursos de la propia entidad y de quienes asesoran o mantienen relaciones comerciales con clientes.
>
> h) El directorio u órgano equivalente deberá evaluar la pertinencia de conformar un Comité de Gestión de Riesgos o una instancia similar que le permitan tratar y monitorear aspectos relevantes de los negocios, referidos a materias tales como conflictos de intereses, seguridad de la información, entre otros. Los fundamentos considerados por el directorio u órgano equivalente para evaluar la conformación de comités o instancias similares deberán estar debidamente documentados.
>
> i) Asegurar que las actas o documentación equivalente den cuenta de las principales temáticas tratadas en las sesiones del directorio u órgano equivalente y los comités, así como las políticas mencionadas previamente. Todo el material que se elabore o presente al directorio u órgano equivalente o los comités, deberá estar debidamente documentado y archivado de conformidad a las normas generales aplicables en la materia, y estar permanentemente disponible para su examen a solicitud de esta Comisión."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.A.3 — risk-management function whose implementation the board must establish under item e)(3).
- NCG 502 §II.A — authorisation requirements for the provision of services referenced in item f).

> **Source:** NCG 502 §IV.A.1 (12-ene-2024).

---

## IV.A.2 — Policies and Procedures
**NCG anchor:** N° 502, Sección IV, A.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, policies-and-procedures, investment-advisory

### Plain-English text

Entities must formally develop and implement risk-management and internal-control policies and procedures that address the risks associated with investment advisory.

The risk-management function shall be responsible for ensuring that all policies and procedures are prepared by those in charge of the various risk-generating areas, and for their accuracy, integrity, and currency.

The established policies and procedures must comply with the following general requirements:

a) They must relate to the number or type of clients, and to the volume of transactions carried out, in respect of each of the businesses or activities developed.

b) Policies must set out the general principles and guidelines established by the board of directors or equivalent body to guide the activities of the organisation.

c) Procedures must define how to carry out a process, with the aim of ensuring compliance with the policies approved by the board of directors or equivalent body, incorporating at least: the description of the principal activities that compose it and the identification of those responsible; the determination of those responsible for supervising and controlling the outcome of the activities carried out; documentation evidencing the execution of the activities that make up the procedures; the definition and description of the controls associated with those activities. In the case of outsourced activities, there must always be a person responsible within the organisation for the control of those activities.

d) Policies, procedures, and control mechanisms must be formally established and documented.

### Original Spanish

> "A.2. POLÍTICAS Y PROCEDIMIENTOS
>
> Las entidades deberán elaborar y poner en práctica de manera formal, políticas y procedimientos de gestión de riesgos y control interno que contemplen los riesgos asociados a la asesoría de inversión.
>
> La función de gestión de riesgos será la responsable de asegurar la elaboración de la totalidad de las políticas y los procedimientos por parte de los encargados de las distintas áreas generadoras de riesgos; y de la exactitud, integridad y actualización de tales políticas y procedimientos.
>
> Las políticas y procedimientos establecidas deberán cumplir con los siguientes aspectos generales:
>
> a) Deberán guardar relación con el número o tipo de clientes, y al volumen de operaciones efectuadas, y respecto de cada uno de los negocios o actividades que se desarrolle.
>
> b) Las políticas deberán exponer los principios generales y directrices establecidas por el directorio u órgano equivalente para orientar las actividades de la organización.
>
> c) Los procedimientos deberán definir cómo llevar a cabo un proceso, con el fin de asegurar el cumplimiento de las políticas aprobadas por el directorio u órgano equivalente incorporando, al menos: la descripción de las actividades principales que lo componen y la identificación de sus responsables; determinación de los responsables de supervisar y controlar el resultado de las actividades ejecutadas; documentación que evidencie la ejecución de las actividades que conforman los procedimientos; definición y descripción de los controles asociados a dichas actividades. En el caso de actividades externalizadas, siempre deberá existir una persona responsable dentro de la organización respecto al control de estas.
>
> d) Las políticas, procedimientos y mecanismos de control deberán estar formalmente establecidos y documentados."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.A.2.1 — specific minimum content requirements for risk-management and internal-control policies and procedures.
- NCG 502 §IV.A.2.2 — specific requirements for operational risk.
- NCG 502 §IV.A.3 — risk-management function responsible for ensuring policy accuracy and currency.

> **Source:** NCG 502 §IV.A.2 (12-ene-2024), as amended by NCG 524 item 1 (02-dic-2024).

---

## IV.A.2.1 — Risk-Management and Internal-Control Policies and Procedures
**NCG anchor:** N° 502, Sección IV, A.2.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, internal-control, policies-and-procedures, investment-advisory

### Plain-English text

Without prejudice to the foregoing, the policies and procedures must address at least the following matters:

**a) Conflicts of interest**

Entities must define policies and procedures that specify the methods by which all potential conflicts of interest inherent in the services it offers will be identified, managed, and monitored. The policies and procedures must address the identification, prevention, and monitoring of conflicts that may arise between the investment advisory service and its clients, as well as those arising from other products offered by the entity, as permitted by applicable legislation and regulations.

**b) Confidentiality of information**

Entities must define policies and procedures aimed at safeguarding the confidential nature of the information delivered by their clients for the purposes of the investment advisory service, and must comply with all applicable legal provisions to that effect, in particular those established by Ley N° 19.628 on the protection of private life.

The policies and procedures must include consent for the use of information by clients, in accordance with Ley N° 19.628 on the protection of private life, ensuring the protection of data against unauthorised access and disclosure, and the means for protecting personal privacy and reserved information.

**c) Offering of products in line with the investor's needs, expectations, and risk tolerance**

Entities must define policies and procedures aimed at ensuring that investors invest their resources in financial instruments with knowledge of the information that enables them to understand and accept the risk they are assuming, and at avoiding the offering of products that are not in line with their needs, expectations, and risk tolerance, as provided in Article 28 of Ley N° 21.521.

Entities must have procedures to ensure compliance with this obligation. In cases where a client decides to invest in a financial instrument that, in the opinion of the entity, is not in line with the needs, expectations, or risks the entity has communicated to it, the entity must be able to certify that this was duly warned, in the event that such certification is requested by the Commission (CMF). For these purposes, the procedures may include requiring prospective clients to provide background information such as data on their knowledge and experience as an investor, their financial situation, and their investment or savings objectives, and other information of this nature that the entity considers relevant.

The entity may establish exceptions to this policy in the case of offerings of products directed at clients with the status of institutional investor or of qualified investor from among those indicated in items 2, 3, and 4 of Section II of Norma de Carácter General N° 216.

**d) Information to the investor**

The entity must define policies and procedures that determine how it will ensure that clients have truthful, sufficient, and timely information relating to the products or services offered, as provided in Article 28 of Ley N° 21.521.

These policies must specify, at a minimum, the information that must be known by clients in accordance with Section III of this regulation, and any additional information the entity considers necessary to be known, as well as the frequency established for that purpose. For its part, the procedures must relate to how the entity will monitor compliance with these provisions.

**e) Algorithm approval, evaluation, and control methodology**

Where applicable, entities must have policies and procedures for the approval, evaluation, and control of algorithms that ensure their adequate operation when providing the investment advisory service. These policies and procedures must ensure that the algorithms used guarantee that advisory services are carried out in the interest of and for the protection of clients, in accordance with their needs, expectations, and risk tolerance that they have previously communicated.

Entities must have trained personnel who understand the operation of the algorithms and the continuous verification of the correct operation of their algorithms, including what is established in subparagraph d) of Section II.A of this regulation.

**f) Compliance with legal and regulatory operating requirements**

Policies and procedures must be defined that specify how compliance with the applicable legal and regulatory requirements for the entity will be monitored and ensured.

In addition, procedures must be defined for the event of non-compliance with the legal operating requirements occurring, which must be reported promptly to the Commission (CMF).

### Original Spanish

> "A.2.1. POLÍTICAS Y PROCEDIMIENTOS DE GESTIÓN DE RIESGOS Y CONTROL INTERNO
>
> Sin perjuicio de lo anterior, las políticas y procedimientos deberán abordar como mínimo los siguientes aspectos:
>
> a) Conflictos de intereses
>
> Las entidades deberán definir políticas y procedimientos que especifiquen los métodos según los cuales se identificarán, manejarán y vigilarán todos los potenciales conflictos de intereses inherentes a los servicios ofrecidos por ella. Las políticas y procedimientos deberán considerar la identificación, la prevención y monitoreo de los conflictos que puedan surgir entre el servicio de asesoría de inversión y sus clientes, así como de otros productos ofrecidos por la entidad, según le permita la legislación y normativa vigente.
>
> b) Confidencialidad de la información
>
> Las entidades deberán definir políticas y procedimientos destinados a resguardar la naturaleza confidencial de la información entregada por sus clientes para efectos del servicio de asesoría de inversión, debiendo cumplir con todas las disposiciones legales al efecto, en particular, aquellas que establece la ley N°19.628 sobre protección de la vida privada.
>
> Las políticas y procedimientos deberán incluir el consentimiento para el uso de la información por parte de los clientes, de acuerdo con la ley N°19.628 sobre protección de la vida privada, asegurando la protección de los datos contra el acceso y la divulgación no autorizados y los medios para proteger la privacidad personal y la información reservada.
>
> c) Oferta de productos acorde a las necesidades, expectativas y disposición al riesgo del inversionista
>
> Las entidades deberán definir políticas y procedimientos tendientes a que los inversionistas inviertan sus recursos en instrumentos financieros, conociendo la información que les permita entender y aceptar el riesgo que están asumiendo, y a evitar ofrecer productos que no sean acordes a sus las necesidades, expectativas y disposición al riesgo de los inversionistas, según lo dispuesto en el artículo 28 de la ley N°21.521.
>
> Las entidades deberán contar con procedimientos para asegurar el cumplimiento de la citada obligación. En aquellos casos en que un cliente decida invertir en un instrumento financiero que, en opinión de la entidad, no es acorde a las necesidades, expectativas o riesgos que este le ha comunicado la entidad deberá poder acreditar que aquello fue debidamente advertido, en caso de que le sea solicitado por la Comisión. Para estos efectos, los procedimientos podrán considerar el requerir a sus potenciales clientes antecedentes tales como información sobre sus conocimientos y experiencia como inversionista, su situación financiera, y objetivos de inversión o ahorro, y otra información de esta naturaleza que la entidad considere relevante.
>
> La entidad podrá establecer excepciones en esta política, en caso de que la oferta de productos esté dirigida a clientes que tengan la calidad de inversionista institucional o inversionista calificado de entre los señalados en los números 2, 3 y 4 de la Sección II de la Norma de Carácter General N°216.
>
> d) Información al inversionista
>
> La entidad deberá definir políticas y procedimientos que determinen la forma en que se garantizará que los clientes cuenten con información veraz, suficiente y oportuna, relativa a los productos o servicios ofrecidos, según lo dispuesto en el artículo 28 de la ley N°21.521.
>
> Estas políticas deberán especificar, al menos, la información que debe ser conocida por los clientes de acuerdo con la Sección III de esta normativa, y aquella que adicionalmente la entidad estime necesaria que se conozca, así como también la periodicidad establecida para ello. Por su parte, los procedimientos deberán estar referidos a la forma en que la entidad controlará el cumplimiento de estas disposiciones.
>
> e) Metodología de aprobación, evaluación y control de algoritmos
>
> En caso de corresponder, las entidades deberán contar con políticas y procedimientos de aprobación, evaluación y control de algoritmos que garanticen su adecuado funcionamiento al otorgar el servicio de asesoría de inversión. Estas políticas y procedimientos deberán velar porque los algoritmos empleados garanticen que las asesorías se realicen en el interés y la protección de los clientes, acorde con las necesidades, expectativas y disposición al riesgo que éstos les hayan comunicado previamente.
>
> Las entidades deberán contar con personal capacitado que comprenda el funcionamiento de los algoritmos y la verificación continua de su correcto funcionamiento de sus algoritmos, incluyendo lo establecido en la letra d) de la Sección II.A de esta normativa.
>
> f) Cumplimiento de requisitos legales y normativos de funcionamiento
>
> Se deberán definir políticas y procedimientos que especifiquen la forma en que se monitoreará y garantizará el debido cumplimiento de los requisitos legales y normativos aplicables a la entidad.
>
> Además, se deberá definir procedimientos en caso de presentarse eventos de incumplimiento de los requisitos legales de funcionamiento, los cuales deberán ser informados oportunamente a esta Comisión."

> **TN:** Item c) contains a typographical duplicate in the source — "acordes a sus las necesidades" — which has been rendered as "in line with their needs" in the English without replication of the error.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- Ley 21.521 Art. 28 — investor information and suitability obligation, referenced in items c) and d).
- Ley N° 19.628 — personal data protection law referenced in items b) and c).
- NCG 216 §II (items 2, 3, 4) — qualified investor sub-categories that may be exempted from the product-suitability policy under item c).
- NCG 502 §II.A(d) — algorithm-related authorisation requirements referenced in item e).
- NCG 502 §III — client-information obligations the policies under item d) must reference.
- NCG 502 §IV.A.2 — general policies-and-procedures framework of which this is a minimum-content specification.

> **Source:** NCG 502 §IV.A.2.1 (12-ene-2024).

---

## IV.A.2.2 — Operational Risk
**NCG anchor:** N° 502, Sección IV, A.2.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, operational-risk, information-security, cybersecurity, investment-advisory

### Plain-English text

Without prejudice to the minimum policies and procedures that entities must implement by virtue of the preceding section, entities must observe the following guidelines in terms of information security and cybersecurity. It is important to note that entities must adapt these requirements taking into account especially their business model, volume of transactions, and number and type of clients:

a) Periodic training of personnel on the matter, so that they are aware of information security and cybersecurity risks and contribute to their adequate management.

b) Safeguarding of client information:

1) Implement an inventory of information assets, including a classification of these. This classification must take into account dimensions such as the availability, confidentiality, and integrity of information assets.

2) Implement an inventory of services related to information assets.

3) Implement access controls for facilities, business infrastructure, and information systems.

4) Implement tools for recording, controlling, and monitoring the activity of system users.

c) Implement controls to mitigate risks arising from the use of mobile devices and remote access by personnel, and cybersecurity management tools such as, for example, software and firmware patch management programmes, network protection against attacks through firewalls, intrusion prevention systems, privilege escalation, identity and physical and logical access management, identity control mechanisms to prevent impersonation of third parties, among others.

d) Manage environmental conditions for the secure location of the entity's equipment and tools.

e) Procedures for the identification of cybersecurity threats such as phishing, malware, malicious code injection, among others.

### Original Spanish

> "A.2.2. RIESGO OPERACIONAL
>
> Sin perjuicio de las políticas y procedimientos mínimos que deban implementar las entidades en virtud de la sección anterior, éstas deberán observar los siguientes lineamientos en términos de seguridad de la información y ciberseguridad. Resulta relevante destacar que las entidades deberán adaptar estas exigencias considerando especialmente su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) La capacitación periódica del personal en la materia, de manera que sea consciente de los riesgos de seguridad de la información y ciberseguridad y contribuya a una adecuada gestión de éstos.
>
> b) Resguardo de la información de sus clientes:
>
> 1) Implementar un inventario de los activos de información, incluyendo una clasificación de estos. Esta clasificación deberá considerar dimensiones tales como disponibilidad, confidencialidad e integridad de los activos de información.
>
> 2) Implementar un inventario de servicios relacionados con los activos de información.
>
> 3) Implementar controles de acceso a las instalaciones, infraestructuras de negocios y sistemas de información.
>
> 4) Implementar herramientas de registro, control y monitoreo de la actividad de los usuarios de sistemas.
>
> c) Implementar controles que permitan mitigar los riesgos derivados del uso de dispositivos móviles y del acceso remoto realizado por el personal, y herramientas de gestión de la ciberseguridad como, por ejemplo, programas de gestión de parches de software y firmware, protección de redes ante ataques por medio de firewalls, sistemas de prevención de intrusos, elevación de privilegios, gestión de identidades y acceso físico y lógico, mecanismos de control de identidad para evitar suplantación de terceros entre otras.
>
> d) Gestionar las condiciones ambientales para la localización segura de los equipos y herramientas de la entidad.
>
> e) Procedimientos de identificación de amenazas de ciberseguridad tales como phishing, malware, inyección de código malicioso, entre otros."

> **TN:** Item c) lists "elevación de privilegios" as a standalone item in the enumeration of cybersecurity tools alongside firewalls and intrusion prevention systems. In context the phrase describes privilege-escalation controls (i.e., mechanisms to prevent or manage escalation of access rights), rendered as "privilege escalation" in the English list. This reading follows the CMF's consistent framing of the item as a control against misuse of elevated access.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.A.2 — general policies-and-procedures framework of which this is a supplementary specification.
- NCG 502 §IV.A.5 — operational-incident reporting obligation triggered when incidents affecting information security or client personal data occur.

> **Source:** NCG 502 §IV.A.2.2 (12-ene-2024), as amended by NCG 524 item 2 (02-dic-2024).

---

## IV.A.3 — Risk Management
**NCG anchor:** N° 502, Sección IV, A.3
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, investment-advisory

### Plain-English text

This subsection establishes the requirements for the risk-management function and risk-management plan applicable to entities providing investment advisory services.

### Original Spanish

> "A.3. GESTIÓN DE RIESGOS"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this subsection implements.
- NCG 502 §IV.A.3.1 — risk-management function requirements.
- NCG 502 §IV.A.3.2 — risk-management plan requirements.

> **Source:** NCG 502 §IV.A.3 (12-ene-2024).

---

## IV.A.3.1 — Risk-Management Function
**NCG anchor:** N° 502, Sección IV, A.3.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, risk-management-function, investment-advisory

### Plain-English text

The risk-management function is the body responsible for monitoring the controls defined in the entity's risk-management and internal-control policies and procedures. This function must report directly to the board of directors or equivalent body.

In accordance with subparagraph A.4 of this Section, the risk-management function may be carried out by a person, an internal unit, or by the senior management (alta administración) of the entity. If the function is exercised by a corporate risk-management unit in the case where the entity belongs to a business group, it shall be considered as carried out by an internal unit.

Without prejudice to the foregoing, the entity shall always be responsible for the risk-management function even when it is carried out by a body belonging to the business group, and must review and approve the reports produced in that regard, for which it must retain all relevant documentation.

Likewise, the risk-management function shall be responsible for carrying out activities to monitor compliance with the policies defined by the entity.

In order to implement the foregoing, the risk-management function must:

a) Verify the existence of the minimum policies and procedures described in subparagraph A.2 above.

b) Issue a report, at least on a semi-annual basis, to the board of directors or equivalent body documenting the instances of non-compliance detected, the causes that gave rise to them, the measures adopted, and the effectiveness of those measures.

c) Propose changes to risk-management policies and procedures based on the deficiencies found in its control activities.

d) Prepare an annual plan addressing the nature, scope, and timing of the activities that the risk-management function will carry out. This plan must be approved by the board of directors or equivalent body. In any event, the plan must be updated whenever significant changes occur, such as changes in the economic environment and markets in which the entity operates, the introduction of new products or services, or changes in the regulations applicable to the entity.

### Original Spanish

> "A.3.1. FUNCIÓN DE GESTIÓN DE RIESGOS
>
> La función de gestión de riesgos es la instancia responsable del monitoreo de los controles definidos en las políticas y los procedimientos de gestión de riesgos y control interno de la entidad. Esta función deberá reportar directamente al directorio u órgano equivalente.
>
> De acuerdo con el literal A.4. de esta Sección, la función de gestión de riesgos podrá ser realizada por una persona, unidad interna o por la alta administración de la entidad. Si la función es ejercida por una unidad de gestión de riesgos corporativa en caso de que la entidad pertenezca a un grupo empresarial, se considerará realizada por una unidad interna.
>
> Sin perjuicio de lo anterior, la entidad será siempre responsable de la función de gestión de riesgos aun cuando ésta sea realizada por una instancia perteneciente al grupo empresarial, debiendo revisar y aprobar los informes realizados al respecto, para lo cual deberá hacerse de toda la documentación relevante.
>
> Asimismo, la función de gestión de riesgos será responsable de la realización de actividades para monitorear el cumplimiento de las políticas definidas por la entidad.
>
> Con objeto de implementar lo anteriormente señalado, la función de gestión de riesgos deberá:
>
> a) Verificar la existencia de las políticas y procedimientos mínimos descritos en el literal A.2 anterior.
>
> b) Emitir un informe, al menos con una periodicidad semestral, al directorio u órgano equivalente para documentar las instancias de incumplimientos detectados, causas que los originaron, medidas adoptadas y efectividad de dichas medidas.
>
> c) Proponer cambios en las políticas y en los procedimientos de gestión de riesgos en función de las deficiencias encontradas en sus actividades de control.
>
> d) Elaborar un plan anual que se refiera a la naturaleza, el alcance y oportunidad de las actividades que la función de gestión de riesgos desarrollará. Este plan deberá ser aprobado por el directorio u órgano equivalente. En todo caso, dicho plan deberá ser actualizado cada vez que se produzcan cambios significativos tales como cambios en condiciones del entorno económico y mercados en que opera la entidad, introducción de nuevos productos o servicios, o cambios en la regulación aplicable a la entidad."

> **TN:** "alta administración" in the second paragraph is rendered "senior management" — the lexicon renders "alta gerencia" as "senior management"; "alta administración" is a near-synonym used in this context with equivalent meaning; the same rendering is applied and noted here.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.A.4 — proportionality provisions that determine whether the risk-management function may be exercised by senior management or must be specialised.
- NCG 502 §IV.A.2 — minimum policies and procedures the risk-management function must verify.

> **Source:** NCG 502 §IV.A.3.1 (12-ene-2024), as amended by NCG 524 item 3 (02-dic-2024).

---

## IV.A.3.2 — Risk-Management Plan
**NCG anchor:** N° 502, Sección IV, A.3.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, risk-management-plan, investment-advisory

### Plain-English text

The risk-management function shall be responsible for preparing a risk-management plan that will include risk-mitigation strategies and contingency planning in relation to the principal risks, which must at a minimum address risks arising from conflicts of interest and information security and cybersecurity risks.

The board of directors or equivalent body must approve the risk-management plan at least annually, with the aim of reflecting significant changes in the entity's business strategy or changes in market conditions. The risk-management function shall monitor compliance with the risk-management plan and its respective procedures.

The preparation of risk-mitigation strategies and contingency planning shall take into account the following:

a) Identification of the processes into which the activities carried out by the entity are broken down, and the respective persons responsible for those processes (process map). The risk-management function, together with those in charge of the principal processes, must formally identify the risks inherent in those to which the entity is exposed in the development of its activities.

b) Measurement of the inherent risks identified in the activities carried out by the entity.

c) Definition of the control mechanisms to mitigate the inherent risks identified. In this regard, such control mechanisms must address:

1) Description of each control and its objective.

2) Identification of those formally designated as responsible for the control for these purposes.

3) Assessment of the effectiveness of the controls in mitigating the inherent risks, by a body independent of those responsible for them.

d) Information and communication procedures for risk management that ensure that relevant information about the effectiveness of the mitigating controls and compliance with risk-appetite levels reaches the board of directors or equivalent body and all interested parties.

e) A continuous risk-management improvement programme, with the aim of evaluating the need to make changes in response to new economic and financial scenarios facing the entity, changes in the risk profile, and as a result of the implementation or changes in international standards or best practices.

f) Where the entity belongs to a business group, operational-risk management may be performed by a person of that group, provided that such person maintains its independence from the group's internal-audit areas.

### Original Spanish

> "A.3.2. PLAN DE GESTIÓN DE RIESGOS
>
> La función de gestión de riesgos estará a cargo de la elaboración de un plan de gestión de riesgos que incluirá las estrategias de mitigación de riesgos y la planificación de contingencias en relación con los principales riesgos, los que, como mínimo deben contemplar los riesgos provenientes de conflictos de intereses y los riesgos de seguridad de la información y ciberseguridad.
>
> El directorio u órgano equivalente deberá aprobar el plan de gestión de riesgos al menos anualmente, con el fin de reflejar cambios significativos experimentados en la estrategia de negocios de la entidad o cambios en las condiciones de mercado. La función de gestión de riesgos controlará que se dé cumplimiento al plan de gestión de riesgos y a sus respectivos procedimientos.
>
> La elaboración de estrategias de mitigación de riesgos y planificación de contingencias considerará lo siguiente:
>
> a) Identificación de procesos en los que se descomponen las actividades efectuadas por la entidad, y los respectivos responsables de dichos procesos (mapa de procesos).
>
> La función de gestión de riesgos, en conjunto con los encargados de los procesos principales, deberá identificar formalmente los riesgos inherentes a los que se expone la entidad en el desarrollo de sus actividades.
>
> b) Medición de los riesgos inherentes identificados en las actividades efectuadas por la entidad.
>
> c) Definición de los mecanismos de control para mitigar los riesgos inherentes identificados. Al respecto, dichos mecanismos de control deberán considerar:
>
> 1) Descripción de cada control y su objetivo.
>
> 2) Identificación de los responsables del control formalmente designados para esos efectos.
>
> 3) Calificación de la efectividad de los controles para la mitigación de los riesgos inherentes, por una instancia independiente del responsable de los mismos.
>
> d) Procedimientos de información y comunicación de la gestión de riesgos que asegure que la información relevante acerca de la efectividad de los controles mitigantes y el cumplimiento de los niveles de apetito por riesgo llegue al directorio u órgano equivalente y a todas las partes interesadas.
>
> e) Programa de mejoramiento continuo de la gestión de riesgos, con el objeto de evaluar la necesidad de realizar cambios frente a nuevos escenarios económicos y financieros que vaya enfrentando la entidad, cambios del perfil de riesgo y producto de la implementación o cambios en los estándares o mejores prácticas internacionales.
>
> f) En el caso que la entidad pertenezca a un grupo empresarial, la gestión de riesgo operacional podrá ser desempeñada por una persona de dicho grupo, siempre que aquella mantenga su independencia de las áreas de auditoría interna del grupo."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.A.3.1 — risk-management function responsible for preparing and monitoring the plan.
- NCG 502 §IV.A.2.1 — conflict-of-interest and information-security policies that the plan's risk-mitigation strategies must at minimum address.

> **Source:** NCG 502 §IV.A.3.2 (12-ene-2024), as amended by NCG 524 item 4 (02-dic-2024).

---

## IV.A.4 — Proportionality
**NCG anchor:** N° 502, Sección IV, A.4
**Implements:** Ley 21.521 Arts. 1 and 12 (proportionality; governance & risk management)
**Tags:** governance, risk-management, proportionality, investment-advisory

### Plain-English text

In line with the provisions of Articles 1 and 12 of Ley N° 21.521, entities may adapt the provisions of this Section IV.A to their size, volume, and the nature of their businesses and risks.

Without prejudice to the foregoing, Table 1 describes the proportional requirements that entities providing the investment advisory service must comply with.

Proportionality shall be applied depending on whether the investment advisers have fewer or more than 100 active clients in Chile or 100,000 followers:

**Table 1. Proportionality for the provision of the investment advisory service**

| Characteristics of the investment advisory provider | Policies | Risk-management function |
|---|---|---|
| Fewer than 100 active clients in Chile or fewer than 100,000 followers | Exempt | Exempt |
| More than 100 active clients in Chile or 100,000 followers | CI, CINF, OP, II, RLN, ALG, RO | Non-specialised |

Where:

a) CI: Conflicts of interest.
b) CINF: Confidentiality of information.
c) OP: Offering of products in line with the investor's needs, expectations, and risk tolerance.
d) II: Information to the investor.
e) ALG: Algorithm approval, evaluation, and control methodology.
f) RLN: Compliance with legal and regulatory operating requirements.
g) RO: Operational risk.
h) Non-specialised: The risk-management function may be exercised by a member of the senior management of the entity.

When an entity reaches 100 active clients in Chile or 100,000 followers on social media, it shall have a maximum period of 9 months to comply with the corresponding corporate-governance and comprehensive risk-management requirements. Once that number of clients is reached, they must report that fact to the Commission within the 5 business days following the occurrence of the event. To revert to being exempt from the requirements, entities must remain below the client threshold indicated for more than 6 months and request authorisation from the Commission (CMF).

### Original Spanish

> "A.4. PROPORCIONALIDAD
>
> En línea con lo establecido en los artículos 1 y 12 de la ley N°21.521, las entidades podrán adaptar las disposiciones de esta Sección IV.A, conforme a su tamaño, volumen y naturaleza de sus negocios y riesgos.
>
> Sin perjuicio de lo anterior, la Tabla 1 describe los requisitos proporcionales que deberán cumplir las entidades que presten el servicio de asesoría de inversión.
>
> La proporcionalidad se aplicará dependiendo de si los asesores de inversión tienen menos o más de 100 clientes activos en Chile o 100.000 seguidores:
>
> Tabla 1. Proporcionalidad para la prestación del servicio de asesoría de inversión Características del prestador de asesoría de inversión Políticas Función de gestión de riesgos Menos de 100 clientes activos en Chile o menos de 100.000 seguidores Se exime Se exime Más de 100 clientes activos en Chile o 100.000 seguidores CI, CINF, OP, II, RLN, ALG, RO No especializada
>
> Donde,
>
> a) CI: Conflictos de intereses.
>
> b) CINF: Confidencialidad de la información.
>
> c) OP: Oferta de productos acorde a las necesidades, expectativas y disposición al riesgo del inversionista.
>
> d) II: Información al inversionista.
>
> e) ALG: Metodología de aprobación, evaluación y control de algoritmos.
>
> f) RLN: Cumplimiento de requisitos legales y normativos de funcionamiento.
>
> g) RO: Riesgo operacional.
>
> h) No especializada: La función de gestión de riesgos podrá ser ejercida por algún integrante de la alta administración de la entidad.
>
> Cuando una entidad alcance los 100 clientes activos en Chile o 100.000 seguidores en redes sociales, dispondrá de un plazo máximo de 9 meses para dar cumplimiento a los requisitos de gobierno corporativo y gestión integral de riesgos correspondientes. Una vez alcanzado ese número de clientes, deberán avisar ese hecho a la Comisión dentro de los 5 días hábiles siguientes de ocurrido el hecho. Para volver a estar exentas de los requerimientos, las entidades deberán mantenerse por más de 6 meses bajo el umbral de clientes señalado y solicitar autorización de la Comisión."

> **TN:** Table 1 is a structured table in the PDF source. The Original Spanish above transcribes the table cells in the PDF's column-first reading order; the English rendering presents the same content as a row-first Markdown table. The amended threshold combines active-client count (100) and follower count (100,000) and removes the prior natural-/legal-person and personal-data distinctions.

### Cross-references
- Ley 21.521 Arts. 1 and 12 — proportionality and governance mandate this section implements.
- NCG 502 §IV.A.3.1 — risk-management function requirements, including the specialised vs. non-specialised distinction.

> **Source:** NCG 502 §IV.A.4 (12-ene-2024), as amended by NCG 524 item 5 (02-dic-2024).

---

## IV.A.5 — Reporting of Operational Incidents
**NCG anchor:** N° 502, Sección IV, A.5
**Implements:** Ley 21.521 Art. 8 (governance & risk management; operational incident reporting)
**Tags:** governance, risk-management, operational-incidents, information-security, investment-advisory

### Plain-English text

Investment advisory entities that have more than 100 active clients in Chile or more than 100,000 followers must notify the Commission (CMF) of operational incidents affecting the entity's information or the personal data of their clients, such as technology problems affecting information security; viruses or malware detected in critical information assets; loss or leakage of information belonging to the entity or its clients; among others.

For these purposes, entities must use the format of the Operational Incident Report (Reporte de Incidentes Operacionales — RIO) in Annex N° 2 of this regulation, and shall have a period of 2 hours from the time the entity became aware of the event. The period indicated is solely for the purpose of notifying the Commission (CMF) of the occurrence of the incident with the information available at that time and does not imply that the entity must have resolved the problem, taken specific actions, or clarified the causes of the incident, which may be the subject of follow-up reports on the incident sent to the CMF subsequently.

The board of directors or equivalent body must designate an officer in charge and an alternate for the preparation of reports and the sending of information on operational incidents, as well as to keep the board of directors or equivalent body informed in a timely manner about the incident and the measures adopted to resolve it.

### Original Spanish

> "A.5. INFORMACIÓN DE INCIDENTES OPERACIONALES
>
> Las entidades de asesoría de inversión que tengan más de 100 clientes activos en Chile o más de 100.000 seguidores deberán comunicar a esta Comisión los incidentes operacionales que afecten la información de la entidad o los datos personales de sus clientes, tales como, problemas tecnológicos que afecten la seguridad de la información; virus o malware detectados en los activos de información críticos; pérdidas o fugas de información de la entidad o sus clientes, entre otros.
>
> Para estos efectos, las entidades deberán usar el formato del Reporte de Incidentes Operacionales (RIO) del Anexo N°2 de esta normativa, y dispondrán de un plazo de 2 horas transcurridas desde que la entidad tomó conocimiento del hecho. El plazo señalado es solo para efectos de notificar a la Comisión de la ocurrencia del incidente con la información disponible en ese momento y no implica que la entidad deba tener resuelto el problema, haber tomado determinadas acciones o tener aclarada las causas del incidente, lo que podría ser materia de reportes de seguimiento del incidente enviados la CMF, posteriormente.
>
> El directorio u órgano equivalente deberá definir un funcionario encargado y un suplente para la realización de reportes y envío de información de incidentes operacionales, así como para mantener informado en forma oportuna al directorio u órgano equivalente respecto al incidente y las medidas adoptadas para resolverlo."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate; operational incident reporting is part of the entity's risk-management obligations.
- NCG 502 Annex N° 2 — Operational Incident Report (RIO) form required for incident notifications.
- NCG 502 §IV.A.4 — proportionality table establishing the 100-active-client and 100,000-follower thresholds that trigger the reporting obligation.
- NCG 502 §IV.A.2.2 — cybersecurity guidelines whose breach events (malware, phishing, etc.) are typical triggers for reporting under this section.

> **Source:** NCG 502 §IV.A.5 (12-ene-2024), as amended by NCG 524 item 6 (02-dic-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/seccion-04b-gobierno-asesoria-crediticia.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/seccion-04b-gobierno-asesoria-crediticia.md

# NCG 502 — Sección IV.B: Corporate Governance & Risk Management — Credit Advisory (Gobierno Corporativo y Gestión de Riesgos — Asesoría Crediticia)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

---

## IV.B — Credit Advisory
**NCG anchor:** N° 502, Sección IV, B
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, credit-advisory

### Plain-English text

This subsection sets out the corporate-governance and risk-management obligations applicable to Financial-Service Providers (PSFs) that provide the credit advisory service.

### Original Spanish

> "B. ASESORÍA CREDITICIA"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this subsection implements.
- NCG 502 §IV — general proportionality framework applicable to all subsections of Section IV.

> **Source:** NCG 502 §IV.B (12-ene-2024).

---

## IV.B.1 — Responsibility of the Board of Directors or Equivalent Body
**NCG anchor:** N° 502, Sección IV, B.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, board, credit-advisory

### Plain-English text

The Board of Directors or Equivalent Body (Directorio u Órgano Equivalente) of the entity is the body responsible for approving and authorising risk-management and internal-control policies, at least once a year or with the frequency necessary in the event of significant changes to the established policies, leaving evidence thereof. For these purposes, the board of directors or equivalent body must comply with the following risk-management requirements:

a) Establish the mission, vision, and strategic objectives, taking into account the responsibilities that the applicable regulatory framework imposes on the entity.

b) Approve risk-appetite levels, verifying that those definitions enable the entity to comply with its legal obligations, strategic objectives, and be sustainable over time.

c) Approve risk-management policies that are consistent with the strategic objectives, the regulatory framework, the organisational values, and the risk-appetite levels defined, establishing an adequate process for disseminating a risk-management culture throughout the organisation.

d) Review the policies at least annually, and update them in the event of significant changes such as the introduction of new services, or changes in the regulation applicable to the entity.

e) Approve the code of conduct, which must reflect the organisational values and principles and establish guidelines for the conduct of the entity's personnel.

f) Approve the plans of the risk-management function and the internal-audit function. Likewise, take note of the reports issued by those responsible for those functions in a timely manner.

g) Periodically evaluate the adequacy of the resources of the bodies responsible for risk management and internal audit to carry out their work, for which purpose it must take into account the coverage of the work of those functions, approving the allocation of the necessary resources to those units and monitoring the degree of compliance with the budget assigned for that purpose.

h) Have adequate technology and information systems to support the development of the entity's activities, and which in turn enable the continuity of the implementation of risk-management and internal-control policies and procedures.

i) Establish an adequate organisational structure for the entity's risk management, taking into account the following:

1) The administration and control of all relevant risks arising from the development of its activities. In this regard, the organisational structure must be appropriate in relation to the volume of business; the number and type of clients of the entity; and the complexity of its relationships with other entities.

2) The definition of roles, competencies, and responsibilities that enable the entity to carry out its activities and adequately manage the risks it faces. This includes the appropriate segregation of key duties and functions — especially those which, if performed by the same person, could give rise to errors that go undetected or that expose the entity or its participants to undue risks — and between risk-generating areas and the areas that control them.

3) The implementation of the risk-management function, in accordance with what is described in subparagraph B.3.1 of this Section.

4) The implementation of the internal-audit function, in accordance with what is described in subparagraph B.3.3 of this Section.

5) That the board of directors or equivalent body oversees compliance with the segregation of functions and the independence of the risk-management and internal-audit functions.

j) Establish personnel-hiring policies that ensure the entity has staff with the appropriate experience to carry out their functions, and ensure that it has qualified human resources for risk management.

k) Implement remuneration and compensation policies for those who provide services to the entity, which must consider at least the manner or mechanism by which it will be prevented and verified that the remunerations and compensations do not give rise to or exacerbate conflicts of interest on the part of those who manage the resources of the entity itself and of those who advise or maintain commercial relationships with clients.

l) The board of directors or equivalent body must evaluate the appropriateness of forming a Risk Management Committee or a similar body that allows it to address and monitor relevant business matters, relating to matters such as audit, information security, among others. The grounds considered by the board of directors or equivalent body for evaluating the formation of committees or similar bodies must be duly documented.

Without prejudice to the foregoing, the following committees, if constituted, must be composed of at least one member of the board of directors or equivalent body: the Risk Management Committee and the Audit Committee. In the case of entities whose direction rests with a collegiate body, no director may be a member of both the Risk Management Committee and the Audit Committee at the same time.

m) Ensure that the minutes or equivalent documentation reflect the principal matters addressed in the sessions of the board of directors or equivalent body and the committees. All material prepared or presented to the board of directors or equivalent body or the committees must be duly documented and archived in accordance with the applicable general regulations on the matter, and must be permanently available for examination at the request of the Commission (CMF).

### Original Spanish

> "B.1. RESPONSABILIDAD DEL DIRECTORIO U ÓRGANO EQUIVALENTE
>
> El Directorio u órgano equivalente de la entidad es la instancia responsable de aprobar y autorizar las políticas de gestión de riesgos y control interno, como mínimo una vez al año o con la frecuencia necesaria en caso de que se produzcan cambios significativos en las políticas establecidas, dejando evidencia de ello. Para esos efectos, el directorio u órgano equivalente deberá dar cumplimiento a los requisitos de gestión de riesgos que se señalan a continuación:
>
> a) Establecer la misión, visión y objetivos estratégicos, teniendo en consideración las responsabilidades que el marco regulatorio vigente establece para la entidad.
>
> b) Aprobar los niveles de apetito por riesgo, verificando que aquellas definiciones permitan a la entidad cumplir con sus obligaciones legales, objetivos estratégicos y ser sostenible en el tiempo.
>
> c) Aprobar políticas de gestión de riesgos que sean coherentes con los objetivos estratégicos, el marco regulatorio, los valores organizacionales y los niveles de apetito por riesgo definidos, estableciendo un proceso adecuado de difusión de una cultura de gestión de riesgos en toda la organización.
>
> d) Revisar las políticas, al menos anualmente, y actualizarlas en caso de que se produzcan cambios significativos tales como introducción de nuevos servicios, o cambios en la regulación aplicable a la entidad.
>
> e) Aprobar el código de conducta, que dé cuenta de los valores y principios organizacionales y establezca directrices en el actuar del personal de la entidad.
>
> f) Aprobar los planes de la función de gestión de riesgos y la función de auditoría interna. Asimismo, tomar conocimiento de los reportes emitidos por los encargados de dichas funciones en forma oportuna.
>
> g) Evaluar periódicamente la suficiencia de recursos de las instancias encargadas de la gestión de riesgos y auditoría interna para efectuar sus labores, para lo cual deberá tener en consideración la cobertura del trabajo de dichas funciones, aprobando la asignación de los recursos necesarios para dichas unidades y monitoreando el grado de cumplimiento del presupuesto asignado a tal fin.
>
> h) Disponer de sistemas de tecnología e información adecuados que apoyen el desarrollo de las actividades de la entidad, y que a su vez permitan la continuidad de la implementación de las políticas y los procedimientos de gestión de riesgos y control interno.
>
> i) Establecer una estructura organizacional adecuada para la gestión de riesgos de la entidad, que considere lo siguiente:
>
> 1) La administración y el control de todos los riesgos pertinentes derivados del desarrollo de sus actividades. En ese tenor, la estructura organizacional debe ser la adecuada en relación con el volumen de negocios; el número y tipo de clientes de la entidad; y la complejidad de las relaciones con otras entidades.
>
> 2) La definición de los roles, competencias y responsabilidades que permitan realizar sus actividades y gestionar adecuadamente los riesgos que enfrenta la entidad. Lo anterior involucra la segregación apropiada de los deberes y las funciones claves, especialmente aquéllas que, si fueran realizadas por una misma persona, puedan dar lugar a errores que no se detecten o que expongan a la entidad o sus participantes a riesgos indebidos; y entre las áreas generadoras de riesgo y de control de estos.
>
> 3) La implementación de la función de gestión de riesgo, de conformidad con lo descrito en el literal B.3.1 de esta Sección.
>
> 4) La implementación de la función de auditoría interna, de conformidad con lo descrito en el literal B.3.3 de esta Sección.
>
> 5) Que el directorio u órgano equivalente vele por el cumplimiento de la segregación de funciones y la independencia de las funciones de gestión de riesgos y de auditoría interna.
>
> j) Establecer políticas de contratación de empleados que aseguren que la entidad disponga de personal con la debida experiencia para desempeñar sus funciones, y velar porque se cuente con el recurso humano calificado para la gestión de riesgos.
>
> k) Implementar políticas de remuneración y compensación para quienes presten servicios a la entidad, las cuales considerarán al menos la forma o mecanismo mediante el que se prevendrá y verificará que con las remuneraciones y compensaciones no se produzcan o exacerben conflictos de intereses por parte de quienes gestionan recursos de la propia entidad y de quienes asesoran o mantienen relaciones comerciales con clientes.
>
> l) El directorio u órgano equivalente deberá evaluar la pertinencia de conformar un Comité de Gestión de Riesgos o una instancia similar que le permitan tratar y monitorear aspectos relevantes de los negocios, referidos a materias tales como auditoría, seguridad de la información, entre otros. Los fundamentos considerados por el directorio u órgano equivalente para evaluar la conformación de comités o instancias similares deberán están debidamente documentados.
>
> Sin perjuicio de ello, los siguientes comités, en caso de ser constituidos, deberán estar integrados al menos por un integrante del directorio u órgano equivalente: Comité de Gestión de Riesgos y Comité de Auditoría. Tratándose de entidades cuya dirección recae en un órgano colegiado, ningún director (o miembro del órgano equivalente) podrá ser parte del Comité de Gestión de Riesgos y de Auditoría al mismo tiempo.
>
> m) Asegurar que las actas o documentación equivalente den cuenta de las principales temáticas tratadas en las sesiones del directorio u órgano equivalente y los comités. Todo el material que se elabore o presente al directorio u órgano equivalente o los comités, deberá estar debidamente documentado y archivado de conformidad a las normas generales aplicables en la materia, y estar permanentemente disponible para su examen a solicitud de esta Comisión."

> **TN:** Item l) contains a grammatical irregularity in the source — "deberán están debidamente documentados" — which has been rendered idiomatically in English ("must be duly documented") without replication of the error.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.B.3.1 — risk-management function whose implementation the board must establish under item i)(3).
- NCG 502 §IV.B.3.3 — internal-audit function whose implementation the board must establish under item i)(4).

> **Source:** NCG 502 §IV.B.1 (12-ene-2024), as amended by NCG 524 item 7 (02-dic-2024).

---

## IV.B.2 — Policies, Procedures, and Control Mechanisms
**NCG anchor:** N° 502, Sección IV, B.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, policies-and-procedures, credit-advisory

### Plain-English text

Entities must formally develop and implement risk-management and internal-control policies and procedures that address the risks associated with credit advisory. Such risk-management and internal-control policies and procedures have the purpose of effectively controlling the risks faced by the entity's business, while at the same time contributing to minimising the risks associated with this Commission's supervisory objectives.

The body responsible for the risk-management function shall be responsible for ensuring that all policies and procedures are prepared by those in charge of the various risk-generating areas, and for their accuracy, integrity, and currency.

The established policies and procedures must comply with the following general requirements:

a) They must relate to the number or type of clients, and to the volume of transactions carried out, in respect of each of the businesses or activities developed.

b) Policies must set out the general principles and guidelines established by the board of directors or equivalent body to guide the activities of the organisation.

c) Procedures must define how to carry out a process, with the aim of ensuring compliance with the policies approved by the board of directors or equivalent body, incorporating at least: the description of the principal activities that compose it and the identification of those responsible; the determination of those responsible for supervising and controlling the outcome of the activities carried out; documentation evidencing the execution of the activities that make up the procedures; the definition and description of the controls associated with those activities. In the case of outsourced activities, there must always be a person responsible within the organisation for the control of those activities.

d) Policies, procedures, and control mechanisms must be formally established and documented, being consistent with the risk-appetite levels defined by the entity.

e) Operational risk-management policies and procedures must form part of the entity's risk-management policies and procedures, in accordance with subparagraph B.2.2 of this Section.

### Original Spanish

> "B.2. POLÍTICAS, PROCEDIMIENTOS Y MECANISMOS DE CONTROL
>
> Las entidades deberán elaborar y poner en práctica de manera formal, políticas y procedimientos de gestión de riesgos y control interno que contemplen los riesgos asociados a la asesoría crediticia. Tales políticas y procedimientos de gestión de riesgos y control interno tienen como propósito controlar con eficacia los riesgos a que se enfrenta el negocio de la entidad, a la vez que contribuyen a que se minimicen los riesgos asociados a los objetivos de supervisión de esta Comisión.
>
> La instancia encargada de la función de gestión de riesgos será la responsable de asegurar la elaboración de la totalidad de las políticas y los procedimientos por parte de los encargados de las distintas áreas generadoras de riesgos; y de la exactitud, integridad y actualización de tales políticas y procedimientos.
>
> Las políticas y procedimientos establecidas deberán cumplir con los siguientes aspectos generales:
>
> a) Deberán guardar relación con el número o tipo de clientes, y al volumen de operaciones efectuadas, y respecto de cada uno de los negocios o actividades que se desarrolle.
>
> b) Las políticas deberán exponer los principios generales y directrices establecidas por el directorio u órgano equivalente para orientar las actividades de la organización.
>
> c) Los procedimientos deberán definir cómo llevar a cabo un proceso, con el fin de asegurar el cumplimiento de las políticas aprobadas por el directorio u órgano equivalente, incorporando, al menos: la descripción de las actividades principales que lo componen y la identificación de sus responsables; determinación de los responsables de supervisar y controlar el resultado de las actividades ejecutadas; documentación que evidencie la ejecución de las actividades que conforman los procedimientos; definición y descripción de los controles asociados a dichas actividades. En el caso de actividades externalizadas, siempre deberá existir una persona responsable dentro de la organización respecto al control de estas.
>
> d) Las políticas, procedimientos y mecanismos de control deberán estar formalmente establecidos y documentados, siendo consistentes con los niveles de apetito por riesgo que haya definido la entidad.
>
> e) Las políticas y procedimientos de gestión de riesgo operacional deberán formar parte de las políticas y procedimientos de gestión de riesgos de la entidad, de acuerdo con el literal B.2.2 de esta Sección."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.B.2.1 — specific minimum content requirements for risk-management and internal-control policies and procedures.
- NCG 502 §IV.B.2.2 — specific requirements for operational risk, information security, and cybersecurity.
- NCG 502 §IV.B.3.1 — risk-management function responsible for ensuring policy accuracy and currency.

> **TN:** NCG 524 item 25 (literal y) restates verbatim the same instruction as item 8 (literal h): insert "u órgano equivalente" in B.2 literal c) between "por el directorio" and "incorporando, al menos". The insertion is applied once (see literal c) above, "aprobadas por el directorio u órgano equivalente, incorporando, al menos"); item 25 is therefore a redundant duplicate amendment and is a no-op in the consolidated text. Both items are listed in the Source footer for traceability.

> **Source:** NCG 502 §IV.B.2 (12-ene-2024), as amended by NCG 524 items 8 and 25 (02-dic-2024).

---

## IV.B.2.1 — Risk-Management and Internal-Control Policies and Procedures
**NCG anchor:** N° 502, Sección IV, B.2.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, internal-control, policies-and-procedures, credit-advisory

### Plain-English text

Without prejudice to the foregoing, the policies and procedures must address at least the following matters:

**a) Conflicts of interest**

Entities must define policies and procedures that specify the methods by which all potential conflicts of interest inherent in the services it offers will be identified, managed, and monitored. The policies and procedures must address the identification, prevention, and monitoring of conflicts that may arise between the credit advisory service and its clients, as well as those arising from other services offered by the entity, as permitted by applicable legislation and regulations.

**b) Confidentiality of information**

Entities must define policies aimed at safeguarding the confidential nature of the information delivered by their clients for the purposes of the credit advisory service, and must comply with all applicable legal provisions to that effect, in particular those established by Ley N° 19.628 on the protection of private life.

The policies and procedures must include consent for the use of information by clients, in accordance with Ley N° 19.628 on the protection of private life, ensuring the protection of data against unauthorised access and disclosure, and the means for protecting personal privacy and reserved information.

**c) Management of queries, complaints, and claims**

Entities must define policies and procedures that enable them to manage and resolve queries, claims, and complaints from their clients, workers, and the general public. For that purpose, they must consider, at a minimum, a manual that establishes, in simple terms, the minimum background information that will be required in order to make a query, complaint, or claim, and that describes how to use the specialised channels arranged for those purposes.

**d) Marketing and advertising**

Entities must define policies and procedures that, in addition to complying with applicable legal provisions, have as an objective that the services offered to clients are understood by them, in particular in aspects such as the associated costs and the purpose of the credit advisory service.

**e) Information to the client**

The entity must define policies and procedures that determine how it will ensure that clients have truthful, sufficient, and timely information relating to the services offered, as provided in Article 28 of Ley N° 21.521.

These policies and procedures must specify, at a minimum, the information that must be known by clients in accordance with Section III of this regulation and any additional information the entity considers necessary to be known, as well as the frequency established for that purpose. For its part, the procedures must relate to how the entity will monitor compliance with the policies and procedures defined.

**f) Algorithm approval, evaluation, and control methodology**

Where applicable, entities must have policies and procedures for the approval, evaluation, and control of algorithms that ensure their adequate operation when providing the credit advisory service. These policies and procedures must ensure that the algorithms used guarantee that advisory services are carried out in the interest of and for the protection of clients, in accordance with their needs, expectations, and risk tolerance that they have previously communicated.

The policies and procedures must consider, at a minimum, that the entity has trained personnel who understand the operation of the algorithms and the continuous verification of the correct operation of its algorithms.

**g) Compliance with legal and regulatory operating requirements**

Policies and procedures must be defined that specify how compliance with the applicable legal and regulatory requirements for the entity will be monitored and ensured.

In addition, procedures must be defined for the event of non-compliance with the legal operating requirements occurring, which must be reported promptly to the Commission (CMF).

### Original Spanish

> "B.2.1. POLÍTICAS Y PROCEDIMIENTOS DE GESTIÓN DE RIESGOS Y CONTROL INTERNO
>
> Sin perjuicio de lo anterior, las políticas y procedimientos deberán abordar como mínimo los siguientes aspectos:
>
> a) Conflictos de intereses
>
> Las entidades deberán definir políticas y procedimientos que especifiquen los métodos según los cuales se identificarán, manejarán y vigilarán todos los potenciales conflictos de intereses inherentes a los servicios ofrecidos por ella. Las políticas y procedimientos deberán considerar la identificación, la prevención y monitoreo de los conflictos que puedan surgir entre el servicio de asesoría crediticia y sus clientes, así como de otros servicios ofrecidos por la entidad según le permita la legislación y normativa vigente.
>
> b) Confidencialidad de la información
>
> Las entidades deberán definir políticas destinadas a resguardar la naturaleza confidencial de la información entregada por sus clientes para efectos del servicio de asesoría crediticia, debiendo cumplir con todas las disposiciones legales al efecto, en particular, aquellas que establece la ley N°19.628 sobre la protección de la vida privada.
>
> Las políticas y procedimientos deberán incluir el consentimiento para el uso de la información por parte de los clientes, de acuerdo con la ley N°19.628 sobre protección de la vida privada, asegurando la protección de los datos contra el acceso y la divulgación no autorizados, y los medios para proteger la privacidad personal y la información reservada.
>
> c) Gestión de consultas, reclamos y denuncias
>
> Las entidades deberán definir políticas y procedimientos que les permitan gestionar y resolver las consultas, denuncias y reclamos de sus clientes, trabajadores y el público general. Para ello deberán considerar, al menos, un manual que establezca, en términos simples, los antecedentes mínimos que se requerirán para efectuar una consulta, denuncia o reclamo, y que describa cómo utilizar los canales especializados que se hubieren dispuesto para esos efectos.
>
> d) Comercialización y publicidad
>
> Las entidades deberán definir políticas y procedimientos que, además de cumplir las disposiciones legales, tengan como un objetivo que los servicios ofrecidos al cliente sean entendidos por él, en particular, en aspectos como los costos asociados y la finalidad del servicio de asesoría crediticia.
>
> e) Información al cliente
>
> La entidad deberá definir políticas y procedimientos que determinen la forma en que se garantizará que los clientes cuenten con información veraz, suficiente y oportuna, relativa a los servicios ofrecidos, según lo dispuesto en el artículo 28 de la Ley N°21.521.
>
> Estas políticas y procedimientos deberán especificar, al menos, la información que debe ser conocida por los clientes de acuerdo con la Sección III de esta normativa y aquella que adicionalmente la entidad estime necesaria que se conozca, así como también la periodicidad establecida para ello. Por su parte, los procedimientos deberán estar referidos a la forma en que la entidad controlará el cumplimiento de las políticas y procedimientos definidos.
>
> f) Metodología de aprobación, evaluación y control de algoritmos
>
> En caso de corresponder, las entidades deberán contar con políticas y procedimientos de aprobación, evaluación y control de algoritmos que garanticen su adecuado funcionamiento al otorgar el servicio de asesoría crediticia. Estas políticas y procedimientos deberán velar porque los algoritmos empleados garanticen que las asesorías se realicen en el interés y la protección de los clientes, acorde con las necesidades, expectativas y disposición al riesgo que éstos les hayan comunicado previamente.
>
> Las políticas y procedimientos deben considerar, al menos, que la entidad cuente con personal capacitado que comprenda el funcionamiento de los algoritmos y la verificación continua del correcto funcionamiento de sus algoritmos.
>
> g) Cumplimiento de requisitos legales y normativos de funcionamiento
>
> Se deberán definir políticas y procedimientos que especifiquen la forma en que se monitoreará y garantizará el debido cumplimiento de los requisitos legales y normativos aplicables a la entidad.
>
> Además, se deberá definir procedimientos en caso de presentarse eventos de incumplimiento de los requisitos legales de funcionamiento, los cuales deberán ser informados oportunamente a esta Comisión."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- Ley 21.521 Art. 28 — client information obligation, referenced in item e).
- Ley N° 19.628 — personal data protection law referenced in items b) and c).
- NCG 502 §III — client-information obligations the policies under item e) must reference.
- NCG 502 §IV.B.2 — general policies-and-procedures framework of which this is a minimum-content specification.

> **Source:** NCG 502 §IV.B.2.1 (12-ene-2024).

---

## IV.B.2.2 — Operational Risk
**NCG anchor:** N° 502, Sección IV, B.2.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, operational-risk, information-security, cybersecurity, credit-advisory

### Plain-English text

Without prejudice to the minimum policies and procedures that entities must implement by virtue of the preceding section, they must observe the following guidelines in terms of information security and cybersecurity, adapting them on the basis of their business model, volume of transactions, and number and type of clients:

a) Training of personnel on the matter, so that they are aware of information security and cybersecurity risks and contribute to their adequate management.

b) Safeguarding of client information:

1) Implement an inventory of those information assets, including a classification of these. This classification must take into account dimensions such as the availability, confidentiality, and integrity of information assets.

2) Implement an inventory of services related to information assets.

3) Implement access controls for facilities, business infrastructure, and information systems.

4) Implement tools for recording, controlling, and monitoring the activity of system users.

c) Implement controls to mitigate risks arising from the use of mobile devices and remote access by personnel, and cybersecurity management tools such as, for example, software and firmware patch management programmes, network protection against attacks through firewalls, intrusion prevention systems, privilege escalation, identity and physical and logical access management, identity control mechanisms to prevent impersonation of third parties, among others.

d) Manage environmental conditions for the secure location of the entity's equipment and tools.

e) Procedures for the identification of cybersecurity threats such as phishing, malware, malicious code injection, among others.

### Original Spanish

> "B.2.2. RIESGO OPERACIONAL
>
> Sin perjuicio de las políticas y procedimientos mínimos que deban implementar las entidades en virtud de la sección anterior, éstas deberán observar los siguientes lineamientos en términos de seguridad de la información y ciberseguridad, adaptándolas en base a su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) La capacitación del personal en la materia, de manera que sea consciente de los riesgos de seguridad de la información y ciberseguridad y contribuya a una adecuada gestión de éstos.
>
> b) Resguardo de la información de sus clientes:
>
> 1) Implementar un inventario de esos activos de información, incluyendo una clasificación de estos. Esta clasificación deberá considerar dimensiones tales como disponibilidad, confidencialidad e integridad de los activos de información.
>
> 2) Implementar un inventario de servicios relacionados con los activos de información.
>
> 3) Implementar controles de acceso a las instalaciones, infraestructuras de negocios y sistemas de información.
>
> 4) Implementar herramientas de registro, control y monitoreo de la actividad de los usuarios de sistemas.
>
> c) Implementar controles que permitan mitigar los riesgos derivados del uso de dispositivos móviles y del acceso remoto realizado por el personal, y herramientas de gestión de la ciberseguridad como, por ejemplo, programas de gestión de parches de software y firmware, protección de redes ante ataques por medio de firewalls, sistemas de prevención de intrusos, elevación de privilegios, gestión de identidades y acceso físico y lógico, mecanismos de control de identidad para evitar suplantación de terceros, entre otras.
>
> d) Gestionar las condiciones ambientales para la localización segura de los equipos y herramientas.
>
> e) Procedimientos de identificación de amenazas de ciberseguridad tales como phishing, malware, inyección de código malicioso, entre otros."

> **TN:** Item c) lists "elevación de privilegios" as a standalone item in the enumeration of cybersecurity tools alongside firewalls and intrusion prevention systems. In context the phrase describes privilege-escalation controls (i.e., mechanisms to prevent or manage escalation of access rights), rendered as "privilege escalation" in the English list. This reading follows the CMF's consistent framing of the item as a control against misuse of elevated access (same convention as §IV.A.2.2).

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.B.2 — general policies-and-procedures framework of which this is a supplementary specification.
- NCG 502 §IV.B.5 — operational-incident reporting obligation triggered when incidents affecting information security or client personal data occur.

> **Source:** NCG 502 §IV.B.2.2 (12-ene-2024).

---

## IV.B.3 — Risk Management, Control, and Internal Audit Programme
**NCG anchor:** N° 502, Sección IV, B.3
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, internal-audit, credit-advisory

### Plain-English text

This subsection establishes the requirements for the risk-management function, the risk-management plan, and the internal-audit function applicable to entities providing credit advisory services.

### Original Spanish

> "B.3. PROGRAMA DE GESTIÓN DE RIESGOS, CONTROL Y AUDITORÍA INTERNA"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this subsection implements.
- NCG 502 §IV.B.3.1 — risk-management function requirements.
- NCG 502 §IV.B.3.2 — risk-management plan requirements.
- NCG 502 §IV.B.3.3 — internal-audit function requirements.

> **Source:** NCG 502 §IV.B.3 (12-ene-2024).

---

## IV.B.3.1 — Risk-Management Function
**NCG anchor:** N° 502, Sección IV, B.3.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, risk-management-function, credit-advisory

### Plain-English text

The risk-management function is the body responsible for monitoring the controls defined in the entity's risk-management and internal-control policies and procedures. This function must be independent of the risk-generating units and of the internal-audit function, and must report directly to the board of directors or equivalent body.

The risk-management function may be carried out by a natural person or internal unit or, in certain cases, by the senior management (alta administración) of the entity.

Where the entity belongs to a business group, the risk-management function of the entity may be exercised by the corporate risk-management unit, to the extent that it has thorough knowledge of the risk-management framework and control environment of the entity and complies with the requirements established in this regulation, which must be agreed by the board of directors or equivalent body. The appropriateness of the respective unit of the business group that will exercise the risk-management function must be considered, in relation to compliance with the requirements established in this regulation and any conflicts of interest that may arise and, if applicable, their mitigation and/or elimination. For all purposes, if the function is exercised by a corporate risk-management unit in the case where the entity belongs to a business group, it shall be considered as carried out by an internal unit.

Without prejudice to the foregoing, the entity shall always be responsible for the risk-management function even when it is carried out by a body belonging to the business group, and must review and approve the reports produced in that regard, for which it must retain all relevant documentation.

Likewise, the risk-management function shall be responsible for carrying out activities to monitor compliance with the policies, procedures, and controls for the areas defined by the entity.

Additionally, it must adopt the measures that enable it to guarantee due compliance with the provisions contained in laws and regulations, and specifically in relation to due handling of matters such as prohibited activities, conflicts of interest, the possibility of fraud, and other offences or violations.

In order to implement the foregoing, the risk-management function must:

a) Verify the existence of the minimum policies and procedures described in subparagraph B.2 above.

b) Have methodologies and tools to quantify, aggregate, and manage the risks faced by the entity, which must be evaluated at least annually and prospectively, including scenarios such as changes in economic conditions and crisis situations. Furthermore, it must have methodologies and tools that enable it to verify compliance with the policies, procedures, and control mechanisms.

c) Issue a report, at least on a semi-annual basis, to the board of directors or equivalent body documenting the instances of non-compliance detected, the causes that gave rise to them, the measures adopted, and the effectiveness of those measures.

d) Propose changes to risk-management policies and procedures based on the deficiencies found in its control activities.

e) Promote a responsible organisational culture in the area of risk management, which includes periodic awareness, sensitisation, and training programmes that contribute to ensuring that the entity's personnel, including the board of directors or equivalent body and external personnel performing critical functions for the entity, understand the risks relevant to their functions and their contribution to the effectiveness of the management of those risks.

f) The nature, scope, and timing of the activities that the risk-management function will carry out must be contained in an annual plan, which must be approved by the board of directors or equivalent body. In any event, that plan must be updated whenever significant changes occur, such as changes in economic environment and market conditions in which the entity operates, the introduction of new services, or changes in the regulation applicable to the entity.

### Original Spanish

> "B.3.1. FUNCIÓN DE GESTIÓN DE RIESGOS
>
> La función de gestión de riesgos es la instancia responsable del monitoreo de los controles definidos en las políticas y los procedimientos de gestión de riesgos y control interno de la entidad. Esta función deberá ser independiente de las unidades generadoras de riesgos y de la función de auditoría interna, y reportar directamente al directorio u órgano equivalente.
>
> La función de gestión de riesgos podrá ser realizada por una persona o unidad interna o, en ciertos casos, por la alta administración de la entidad.
>
> En el caso que la entidad pertenezca a un grupo empresarial la función de gestión de riesgos de la entidad podrá ser ejercida por la unidad de riesgos corporativa, en la medida que ésta tenga un conocimiento acabado del marco de gestión de riesgos y ambiente de control de la entidad y que cumpla con los requisitos establecidos en la presente normativa, lo cual deberá ser acordado por el directorio u órgano equivalente. Se deberá considerar la pertinencia respecto a la idoneidad de la unidad respectiva del grupo empresarial que ejercerá la función de riesgos, en relación con el cumplimiento de los requisitos establecidos en esta norma y los conflictos de intereses que pudieran generarse y, de ser el caso, su mitigación y/o eliminación. Para todos los efectos, si la función es ejercida por una unidad de gestión de riesgos corporativa en caso de que la entidad pertenezca a un grupo empresarial se considerará realizada por una unidad interna.
>
> Sin perjuicio de lo anterior, la entidad será siempre responsable de la función de gestión de riesgos aun cuando ésta sea realizada por una instancia perteneciente al grupo empresarial, debiendo revisar y aprobar los informes realizados al respecto, para lo cual deberá hacerse de toda la documentación relevante.
>
> Asimismo, la función de gestión de riesgos será responsable de la realización de actividades para monitorear el cumplimiento de las políticas, procedimientos y controles para las áreas que la entidad defina.
>
> Adicionalmente, deberá adoptar las medidas que permitan garantizar el debido cumplimiento de las disposiciones contenidas en las leyes y normativas, y en lo específico, en lo relativo al debido manejo de materias tales como, actividades prohibidas, conflictos de intereses, eventualidad de fraude, y otros delitos o infracciones.
>
> Con objeto de implementar lo anteriormente señalado, la función de gestión de riesgos deberá:
>
> a) Verificar la existencia de las políticas y procedimientos mínimos descritos en el literal B.2 anterior.
>
> b) Contar con metodologías y herramientas para cuantificar, agregar y gestionar los riesgos que enfrenta la entidad, los cuales deberán evaluarse al menos anualmente y en forma prospectiva, incluyendo escenarios tales como cambios en las condiciones de la economía y situaciones de crisis. Además, deberá contar con metodologías y herramientas que le permita verificar el cumplimiento de las políticas, procedimientos y mecanismos de control.
>
> c) Emitir un informe, al menos con una periodicidad semestral al directorio u órgano equivalente para documentar las instancias de incumplimientos detectados, causas que los originaron, medidas adoptadas y efectividad de dichas medidas.
>
> d) Proponer cambios en las políticas y en los procedimientos de gestión de riesgos en función de las deficiencias encontradas en sus actividades de control.
>
> e) Promover una cultura organizacional responsable en el ámbito de gestión de riesgo, que comprenda programas periódicos de difusión, concientización y capacitación, que contribuyan a que el personal de la entidad, incluyendo el directorio u órgano equivalente y el personal externo que realice funciones críticas para la entidad, comprenda los riesgos atingentes a sus funciones, y cuál es su contribución a la efectividad de la gestión de dichos riesgos.
>
> f) La naturaleza, el alcance y oportunidad de las actividades que desarrollará la función de gestión de riesgos deberán estar contenidos en un plan anual, el que deberá ser aprobado por el directorio u órgano equivalente. En todo caso, dicho plan deberá ser actualizado cada vez que se produzcan cambios significativos tales como cambios en condiciones del entorno económico y mercados en que opera la entidad, introducción de nuevos servicios, o cambios en la regulación aplicable a la entidad."

> **TN:** "alta administración" is rendered "senior management" — the lexicon renders "alta gerencia" as "senior management"; "alta administración" is a near-synonym used in this context with equivalent meaning; the same rendering is applied (same convention as §IV.A.3.1).

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.B.4 — proportionality provisions that determine whether the risk-management function may be exercised by senior management or must be specialised.
- NCG 502 §IV.B.2 — minimum policies and procedures the risk-management function must verify.

> **Source:** NCG 502 §IV.B.3.1 (12-ene-2024).

---

## IV.B.3.2 — Risk-Management Plan
**NCG anchor:** N° 502, Sección IV, B.3.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, risk-management-plan, credit-advisory

### Plain-English text

The risk-management function shall be responsible for preparing a risk-management plan that will include risk-mitigation strategies and contingency planning in relation to the principal risks arising from the entity's activities.

The board of directors or equivalent body must approve the risk-management plan at least annually, with the aim of reflecting significant changes in the entity's business strategy or changes in market conditions. The risk-management function shall monitor compliance with the risk-management plan and its respective procedures.

The preparation of risk-mitigation strategies and contingency planning shall take into account the following:

a) Identification of the processes into which the activities carried out by the entity are broken down, and the respective persons responsible for those processes (process map).

The risk-management function, together with those in charge of the principal processes, must formally identify the risks inherent in those to which the entity is exposed in the development of its activities.

b) Measurement of the inherent risks identified in the activities carried out by the entity.

c) Definition of the control mechanisms to mitigate the inherent risks identified. In this regard, such control mechanisms must address:

1) Description of each control and its objective.

2) Identification of those formally designated as responsible for the control for these purposes.

3) Assessment of the effectiveness of the controls in mitigating the inherent risks, by a body independent of those responsible for them.

d) Information and communication procedures for risk management that ensure that relevant information about the effectiveness of the mitigating controls and compliance with risk-appetite levels reaches the board of directors or equivalent body and all interested parties.

e) A continuous risk-management improvement programme, with the aim of evaluating the need to make changes in response to new economic and financial scenarios facing the entity, changes in the risk profile, and as a result of the implementation or changes in international standards or best practices. Where the entity belongs to a business group, operational-risk management may be performed by a person of that group, provided that such person maintains its independence from the group's internal-audit areas.

### Original Spanish

> "B.3.2. PLAN DE GESTIÓN DE RIESGOS
>
> La función de gestión de riesgos estará a cargo de la elaboración de un plan de gestión de riesgos que incluirá las estrategias de mitigación de riesgos y la planificación de contingencias en relación con los principales riesgos que surjan de las actividades de la entidad.
>
> El directorio u órgano equivalente deberá aprobar el plan de gestión de riesgos al menos anualmente, con el fin de reflejar cambios significativos experimentados en la estrategia de negocios de la entidad o cambios en las condiciones de mercado. La función de gestión de riesgos controlará que se dé cumplimiento al plan de gestión de riesgos y a sus respectivos procedimientos.
>
> La elaboración de estrategias de mitigación de riesgos y planificación de contingencias considerará lo siguiente:
>
> a) Identificación de procesos en los que se descomponen las actividades efectuadas por la entidad, y los respectivos responsables de dichos procesos (mapa de procesos).
>
> La función de gestión de riesgos, en conjunto con los encargados de los procesos principales, deberá identificar formalmente los riesgos inherentes a los que se expone la entidad en el desarrollo de sus actividades.
>
> b) Medición de los riesgos inherentes identificados en las actividades efectuadas por la entidad.
>
> c) Definición de los mecanismos de control para mitigar los riesgos inherentes identificados. Al respecto, dichos mecanismos de control deberán considerar:
>
> 1) Descripción de cada control y su objetivo.
>
> 2) Identificación de los responsables del control formalmente designados para esos efectos.
>
> 3) Calificación de la efectividad de los controles para la mitigación de los riesgos inherentes, por una instancia independiente del responsable de los mismos.
>
> d) Procedimientos de información y comunicación de la gestión de riesgos que asegure que la información relevante acerca de la efectividad de los controles mitigantes y el cumplimiento de los niveles de apetito por riesgo llegue al directorio u órgano equivalente y a todas las partes interesadas.
>
> e) Programa de mejoramiento continuo de la gestión de riesgos, con el objeto de evaluar la necesidad de realizar cambios frente a nuevos escenarios económicos y financieros que vaya enfrentando la entidad, cambios del perfil de riesgo y producto de la implementación o cambios en los estándares o mejores prácticas internacionales. En el caso que la entidad pertenezca a un grupo empresarial, la gestión de riesgo operacional podrá ser desempeñada por una persona de dicho grupo, siempre que aquella mantenga su independencia de las áreas de auditoría interna del grupo."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.B.3.1 — risk-management function responsible for preparing and monitoring the plan.

> **Source:** NCG 502 §IV.B.3.2 (12-ene-2024), as amended by NCG 524 item 9 (02-dic-2024).

---

## IV.B.3.3 — Internal-Audit Function
**NCG anchor:** N° 502, Sección IV, B.3.3
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, internal-audit, internal-audit-function, credit-advisory

### Plain-English text

The internal-audit function is the body responsible for verifying the correct functioning of the entity's internal-control system and risk-management system. This function must be independent of the risk-generating units and of the risk-management function, and must report directly to the board of directors or equivalent body.

The internal-audit function may be carried out by a natural person or internal unit, or outsourced to a third party. Where the entity belongs to a business group, the internal-audit function may be exercised by the corporate internal-audit unit, to the extent that it has thorough knowledge of the entity's risk-management framework and control environment and complies with the requirements established in this regulation, which must be agreed by the board of directors or equivalent body. The appropriateness of the respective unit of the business group that will carry out the activity must be considered, in relation to compliance with the requirements established in this regulation and any conflicts of interest that may arise and, if applicable, their mitigation and/or elimination.

For all purposes, if the internal-audit function is exercised by a corporate unit of the business group to which the entity belongs, it shall be understood that it is exercised by an internal unit. Without prejudice to the foregoing, the entity shall always be responsible for the internal-audit function even when it is carried out by a body belonging to the business group, and must review and approve the reports produced in that regard, for which it must retain all relevant documentation.

In order for the entity to develop an adequate internal-audit function, it must comply, at a minimum, with the following principles and elements:

a) The internal-audit function must be carried out by personnel with verifiable experience and knowledge of risk-management frameworks specific to the functions that function must audit.

b) The internal-audit function must be developed on the basis of a methodology that considers at least the following aspects:

1) The nature, scope, and timing of the audits that could be carried out.

2) Audit work programmes.

3) The follow-up to be conducted on the observations identified.

4) How significant deficiencies will be reported to the board of directors or equivalent body.

5) The preparation and structure of the reports produced by this function.

6) The existence and execution of an annual audit plan that includes the nature, scope, and timing of the activities to be developed, and that considers:

i) That the most relevant areas, processes, business lines, or risks are audited periodically, including the risk-management function.

ii) Follow-up on compliance with the commitments made by the audited areas in previous reviews.

c) The internal-audit function must issue a semi-annual report to the board of directors or equivalent body that considers:

1) In respect of the areas, processes, business lines, or risks audited during the period:

i) The quality and effectiveness of the policies, procedures, and control mechanisms.

ii) The result of the audits carried out with their respective rating.

iii) The actions or measures proposed to address the observations raised and the estimated timeframe for their implementation.

iv) The date of the last audit carried out for each auditable unit.

2) In respect of the risk-management function:

i) The effectiveness of the risk-management system.

ii) Non-compliance with risk-management policies and procedures detected in the audits, the causes that gave rise to them, and the corrective actions adopted to prevent their recurrence.

3) The result of the follow-up on the correction of the situations identified in the audits carried out.

The report must be submitted to the board of directors or equivalent body within no more than 30 calendar days after the end of the period to which it refers.

### Original Spanish

> "B.3.3. FUNCIÓN DE AUDITORÍA INTERNA
>
> La función de auditoría interna es la instancia responsable de verificar el correcto funcionamiento del sistema de control interno y de gestión de riesgos de la entidad. Esta función deberá ser independiente de las unidades generadoras de riesgos y de la función de gestión de riesgos, debiendo reportar directamente al directorio u órgano equivalente.
>
> La función de auditoría interna podrá ser realizada por una persona o unidad interna, o externalizada a un tercero. En el caso que la entidad pertenezca a un grupo empresarial, la función de auditoría interna podrá ser ejercida por la unidad de auditoría interna corporativa, en la medida que ésta tenga un conocimiento acabado del marco de gestión de riesgos y ambiente de control de la entidad y que cumpla con los requisitos establecidos en la presente normativa, lo cual deberá ser acordado por el directorio u órgano equivalente. Se deberá considerar la pertinencia respecto a la idoneidad de la unidad respectiva del grupo empresarial que se encargará de la actividad, en relación con el cumplimiento de los requisitos establecidos en esta norma y los conflictos de intereses que pudieran generarse y, de ser el caso, su mitigación y/o eliminación.
>
> Para todos los efectos, si la función de auditoría interna es ejercida por una unidad corporativa del grupo empresarial al que pertenece la empresa, se entenderá que es ejercida por una unidad interna. Sin perjuicio de lo anterior, la entidad será siempre responsable de la función de auditoría interna aun cuando ésta sea realizada por una instancia perteneciente al grupo empresarial, debiendo revisar y aprobar los informes realizados al respecto, para lo cual deberá hacerse de toda la documentación relevante.
>
> Con el objeto de que la entidad desarrolle una adecuada función de auditoría interna se deberá dar cumplimiento, al menos, a los principios y elementos que se señalan a continuación:
>
> a) La función de auditoría interna deberá ser desarrollada por personal con experiencia y conocimientos comprobables en marcos de gestión de los riesgos específicos que dicha función deberá auditar.
>
> b) La función de auditoría interna deberá ser desarrollada sobre la base de una metodología que considere al menos los siguientes aspectos:
>
> 1) La naturaleza, alcance y oportunidad de las auditorías que podrían ser efectuadas.
>
> 2) Programas de trabajo de auditoría.
>
> 3) El seguimiento que se efectuará a las observaciones detectadas.
>
> 4) La forma en que se reportarán las deficiencias significativas al directorio u órgano equivalente.
>
> 5) La elaboración y estructura de los informes que esta función realice.
>
> 6) La existencia y ejecución de un plan anual de auditoría que incluya la naturaleza, alcance y oportunidad de las actividades que se desarrollarán, y considerar:
>
> i) Que las áreas, procesos, líneas de negocio o riesgos más relevantes sean auditados periódicamente, incluyendo la función de gestión de riesgos.
>
> ii) El seguimiento al cumplimiento de los compromisos adquiridos por las áreas auditadas en revisiones anteriores.
>
> c) La función de auditoría interna deberá emitir un informe semestral al directorio u órgano equivalente que considere:
>
> 1) Respecto de las áreas, procesos, líneas de negocio o riesgos auditados durante el periodo:
>
> i) La calidad y efectividad de las políticas, procedimientos y mecanismos de control.
>
> ii) El resultado de las auditorías efectuadas con su respectiva calificación.
>
> iii) Las acciones o medidas propuestas para subsanar las observaciones levantadas y el plazo estimado para su implementación.
>
> iv) Fecha de la última auditoría realizada a cada unidad auditable.
>
> 2) Respecto de la función de gestión de riesgos:
>
> i) La efectividad del sistema de gestión de riesgos.
>
> ii) Los incumplimientos de políticas y procedimientos de gestión de riesgos detectados en las auditorías, las causas que los originaron y las acciones correctivas adoptadas para evitar su reiteración.
>
> 3) El resultado del seguimiento de la corrección de las situaciones detectadas en las auditorías realizadas.
>
> El informe deberá ser remitido al directorio u órgano equivalente en un plazo no superior a 30 días corridos de finalizado el periodo al cual se refiere."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.B.3.1 — risk-management function whose independence from the internal-audit function is required.
- NCG 502 §IV.B.4 — proportionality provisions that determine whether the internal-audit function must be specialised.

> **Source:** NCG 502 §IV.B.3.3 (12-ene-2024).

---

## IV.B.4 — Proportionality
**NCG anchor:** N° 502, Sección IV, B.4
**Implements:** Ley 21.521 Arts. 1 and 12 (proportionality; governance & risk management)
**Tags:** governance, risk-management, proportionality, credit-advisory

### Plain-English text

In line with the provisions of Articles 1 and 12 of Ley N° 21.521, entities may adapt the provisions of this Section IV.B to their size, volume, and the nature of their businesses and risks.

Without prejudice to the foregoing, Table 2 describes the proportional requirements that entities providing the credit advisory service must comply with.

Proportionality for credit advisers shall be applied depending on whether they have fewer or more than 100 active clients in Chile.

**Table 2. Proportionality for the provision of the credit advisory service**

| Characteristics of the credit advisory provider | Policies | Risk-management function | Internal-audit function |
|---|---|---|---|
| Fewer than 100 active clients in Chile | Exempt from all requirements of this Section IV.B | Exempt | Exempt |
| 100 or more active clients in Chile | CI, CINF, GCR, CP, IC, ALG, RLN, RO | Non-specialised | Specialised |

Where:

a) CI: Conflicts of interest.
b) CINF: Confidentiality of information.
c) GCR: Management of queries, complaints, and claims.
d) CP: Marketing and advertising.
e) IC: Information to the client.
f) ALG: Algorithm approval, evaluation, and control methodology.
g) RLN: Compliance with legal and regulatory operating requirements.
h) RO: Operational risk.
i) Non-specialised: The risk-management function may be exercised by a member of the senior management of the entity.

In the case of entities providing the credit advisory service whose requirement is that the risk-management and internal-audit function be specialised, this function shall not be exercised by the senior management (alta administración), and must report directly to the board of directors or equivalent body.

Where the internal-audit function is carried out by an external third party, in no case may that third party exercise the external audit function for the entity, and the entity must ensure the adequate segregation of both functions.

When a credit adviser reaches 100 active clients in Chile, it shall have a maximum period of 9 months to comply with the corresponding corporate-governance and comprehensive risk-management requirements. Once that number of clients is reached, credit advisers must report that fact to the Commission within the 5 business days following the occurrence of the event. To revert to being exempt from the requirements, entities must remain below the indicated client threshold for more than 6 months and request authorisation from the Commission (CMF).

### Original Spanish

> "B.4. PROPORCIONALIDAD
>
> En línea con lo establecido en los artículos 1 y 12 de la ley N°21.521, las entidades podrán adaptar las disposiciones de esta Sección IV.B, conforme a su tamaño, volumen y naturaleza de sus negocios y riesgos.
>
> Sin perjuicio de lo anterior, la Tabla 2 describe los requisitos proporcionales que deberán cumplir las entidades que presten el servicio de asesoría crediticia.
>
> La proporcionalidad para asesores crediticios se aplicará dependiendo si tienen menos o más de 100 clientes activos en Chile.
>
> Tabla 2. Proporcionalidad para la prestación del servicio de asesoría crediticia Características del prestador de asesoría crediticia Políticas Función de gestión de riesgos Función de auditoría interna Menos de 100 clientes activos en Chile 100 o más clientes activos en Chile Se exime de todos los requisitos de esta Sección IV.B CI, CINF, GCR, CP, IC, ALG, RLN, RO Se exime No especializada Se exime Especializada
>
> Donde,
>
> a) CI: Conflictos de intereses.
>
> b) CINF: Confidencialidad de la información.
>
> c) GCR: Gestión de consultas, reclamos y denuncias.
>
> d) CP: Comercialización y publicidad.
>
> e) IC: Información al cliente.
>
> f) ALG: Metodología de aprobación, evaluación y control de algoritmos.
>
> g) RLN: Cumplimiento de requisitos legales y normativos de funcionamiento.
>
> h) RO: Riesgo operacional.
>
> i) No especializada: La función de gestión de riesgos podrá ser ejercida por algún integrante de la alta administración de la entidad.
>
> En el caso de las entidades que presten el servicio de asesoría crediticia y cuyo requisito sea que la función de gestión de riesgos y auditoría interna sea especializada, esta función no podrá ser ejercida por la alta administración, debiendo reportar directamente al directorio u órgano equivalente.
>
> En caso de que la función de auditoría interna sea realizada por un tercero externo, en ningún caso dicho tercero podrá ejercer la función de auditoría externa en la entidad, debiendo la entidad velar por la adecuada segregación de ambas funciones.
>
> En caso de que un asesor crediticio alcance los 100 clientes activos en Chile, dispondrá de un plazo máximo de 9 meses para dar cumplimiento a los requisitos de gobierno corporativo y gestión integral de riesgos correspondientes. Una vez alcanzado ese número de clientes, los asesores crediticios deberán avisar ese hecho a la Comisión dentro de los 5 días hábiles siguientes de ocurrido el hecho. Para volver a estar exentas de los requerimientos, las entidades deberán mantenerse por más de 6 meses bajo el umbral de clientes señalado y solicitar autorización de la Comisión."

> **TN:** Table 2 is a structured table in the PDF source. The Original Spanish above transcribes the table cells in the PDF's column-first reading order (header labels, then the two client-threshold rows, then the Políticas column, then the Función de gestión de riesgos column, then the Función de auditoría interna column); the English rendering presents the same content as a row-first Markdown table. As amended by NCG 524, Table 2 removes the prior personal-data-processing dimension entirely and splits the former combined "risk-management and internal-audit function" column into two separate columns (risk-management function and internal-audit function).

### Cross-references
- Ley 21.521 Arts. 1 and 12 — proportionality and governance mandate this section implements.
- NCG 502 §IV.B.3.1 — risk-management function requirements, including the specialised vs. non-specialised distinction.
- NCG 502 §IV.B.3.3 — internal-audit function requirements subject to the same specialised/non-specialised threshold.

> **Source:** NCG 502 §IV.B.4 (12-ene-2024), as amended by NCG 524 item 10 (02-dic-2024).

---

## IV.B.5 — Reporting of Operational Incidents
**NCG anchor:** N° 502, Sección IV, B.5
**Implements:** Ley 21.521 Art. 8 (governance & risk management; operational incident reporting)
**Tags:** governance, risk-management, operational-incidents, information-security, credit-advisory

### Plain-English text

Credit advisory entities that have more than 100 active clients in Chile must notify the Commission (CMF) of operational incidents affecting the entity's information or the personal data of their clients, such as technology problems affecting information security; viruses or malware detected in critical information assets; loss or leakage of information belonging to the entity or its clients, among others.

For these purposes, entities may use the format of the Operational Incident Report (Reporte de Incidentes Operacionales — RIO) in Annex N° 2 of this regulation, and shall have a period of 2 hours from the time the entity became aware of the event. The period indicated is solely for the purpose of notifying the Commission (CMF) of the occurrence of the incident with the information available at that time and does not imply that the entity must have resolved the problem, taken specific actions, or clarified the causes of the incident, which may be the subject of follow-up reports on the incident sent to the CMF subsequently.

The board of directors or equivalent body must designate an officer in charge and an alternate for the preparation of reports and the sending of information on operational incidents, as well as to keep the board of directors or equivalent body informed in a timely manner about the incident and the measures adopted to resolve it.

### Original Spanish

> "B.5. INFORMACIÓN DE INCIDENTES OPERACIONALES
>
> Las entidades de asesoría crediticia que tengan más de 100 clientes activos en Chile deberán comunicar a esta Comisión los incidentes operacionales que afecten la información de la entidad o los datos personales de sus clientes, tales como, problemas tecnológicos que afecten la seguridad de la información; virus o malware detectados en los activos de información críticos; pérdidas o fugas de información de la entidad o sus clientes, entre otros.
>
> Para estos efectos, las entidades podrán usar el formato del Reporte de Incidentes Operacionales (RIO) del Anexo N°2 de esta normativa, y dispondrán de un plazo de 2 horas transcurridas desde que la entidad tomó conocimiento del hecho. El plazo señalado es solo para efectos de notificar a la Comisión de la ocurrencia del incidente con la información disponible en ese momento y no implica que la entidad deba tener resuelto el problema, haber tomado determinadas acciones o tener aclarada las causas del incidente, lo que podría ser materia de reportes de seguimiento del incidente enviados la CMF, posteriormente.
>
> El directorio u órgano equivalente deberá definir un funcionario encargado y un suplente para la realización de reportes y envío de información, así como para mantener informado en forma oportuna al directorio u órgano equivalente respecto al incidente y las medidas adoptadas para resolverlo."

> **TN:** B.5 uses "podrán usar" (may use) for the RIO format, whereas the parallel provision in §IV.A.5 uses "deberán usar" (must use). The difference is preserved faithfully: the English renders "podrán" as "may" per lexicon convention. The substantive obligation to notify (deberán comunicar) remains mandatory.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate; operational incident reporting is part of the entity's risk-management obligations.
- NCG 502 Annex N° 2 — Operational Incident Report (RIO) form available for incident notifications.
- NCG 502 §IV.B.4 — proportionality table establishing the 100-active-client threshold that triggers the reporting obligation.
- NCG 502 §IV.B.2.2 — cybersecurity guidelines whose breach events (malware, phishing, etc.) are typical triggers for reporting under this section.

> **Source:** NCG 502 §IV.B.5 (12-ene-2024), as amended by NCG 524 item 11 (02-dic-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/seccion-04c-gobierno-plataformas-sat.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/seccion-04c-gobierno-plataformas-sat.md

# NCG 502 — Sección IV.C: Corporate Governance & Risk Management — Crowdfunding Platforms & Alternative Trading Systems (Gobierno Corporativo y Gestión de Riesgos — Plataformas de Financiamiento Colectivo y Sistemas Alternativos de Transacción)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

---

## IV.C — Crowdfunding Platforms and Alternative Trading Systems
**NCG anchor:** N° 502, Sección IV, C
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, crowdfunding, alternative-trading

### Plain-English text

This subsection sets out the corporate-governance and risk-management obligations applicable to Financial-Service Providers (PSFs) that operate crowdfunding platforms (plataformas de financiamiento colectivo) and alternative trading systems (sistemas alternativos de transacción).

### Original Spanish

> "C. PLATAFORMAS DE FINANCIAMIENTO COLECTIVO Y SISTEMAS ALTERNATIVOS DE TRANSACCIÓN"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this subsection implements.
- NCG 502 §IV — general proportionality framework applicable to all subsections of Section IV.

> **Source:** NCG 502 §IV.C (12-ene-2024).

---

## IV.C.1 — Role of the Board of Directors or Equivalent Body
**NCG anchor:** N° 502, Sección IV, C.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, board, crowdfunding, alternative-trading

### Plain-English text

The Board of Directors or Equivalent Body (Directorio u Órgano Equivalente) is responsible for establishing the organisational structure, objectives, and policies that enable adequate management of the risks that may affect the entity (risk-management framework), and must ensure that it has an appropriate risk-management culture, understood as the adequate understanding of corporate governance and risks inherent to the entity. The members of the board of directors or equivalent body must have the appropriate knowledge, experience, and dedication in this regard.

The board of directors or equivalent body must comply, at a minimum, with the following principles and elements:

a) Approve the risk-appetite levels of those risks previously identified. An effective definition should quantify the level of risk that the board of directors or equivalent body wishes to accept in consideration of the entity's strategic objectives and the responsibilities applicable to it under the regulatory framework. In addition, it must continuously be informed of compliance with the risk appetite.

b) Approve the policies set out in subparagraphs C.2 to C.5 of this Section, taking into account for that purpose:

1) That the policies implemented to manage risks are consistent with the mission, vision, strategic objectives, risk-appetite levels, and the regulatory framework applicable to the entity.

2) That the policies are reviewed and updated at least annually or with the frequency necessary in the event of significant changes such as the introduction of new products or services, or changes in the regulation applicable to the entity.

c) Establish an adequate organisational structure for the entity's risk management, taking into account the following:

1) The definition of roles, competencies, and responsibilities that enable the entity to carry out its activities and adequately manage the risks it faces. This involves the appropriate segregation of key duties and functions — especially those which, if performed by the same person, could give rise to errors that go undetected or that expose the entity or its participants to undesired or unmitigated and uncontrolled risks — and between risk-generating areas and the areas that control them.

2) The implementation of the risk-management function, in accordance with what is described in C.4 and C.6 below.

3) The implementation of the internal-audit function, in accordance with what is described in sections C.5 and C.6 below.

4) That the board of directors or equivalent body oversees compliance with the segregation of functions and the independence of the risk-management and internal-audit functions.

5) Have a Risk Management Committee or a similar body. Without prejudice thereto, the board of directors or equivalent body must evaluate the appropriateness of forming other committees or similar bodies that allow it to address and monitor relevant business matters and risk management, relating to matters such as, for example: Internal Audit; Prevention of Money Laundering, Financing of Terrorism, and Financing of Weapons of Mass Destruction; Investments; New Services or Products; Business Continuity; Information Security and Cybersecurity. The board of directors or equivalent body must establish the procedures for the formation and operation of the committees or similar bodies, which must be duly documented, as must their actions, which must be reported to the board on a continuous basis. Without prejudice to the foregoing, the Risk Management and Internal Audit Committees (the latter, if constituted) must be composed of at least one member of the board of directors or equivalent body. In the case of entities whose direction lies with a collegiate body, no director (or member of the equivalent body) may be a member of both the Risk Management Committee and the Internal Audit Committee at the same time. The actions of the committees constituted, in the matters mentioned above, must be recorded in writing in minutes, which must clearly reflect the matters addressed.

d) Approve the annual plans of the risk-management and internal-audit functions and be aware, in a timely manner, of their compliance and of the reports they produce.

e) Establish a policy for the hiring and training of the entity's personnel, in order to have qualified human resources. This policy and programme must consider:

1) The adequate dissemination of the entity's values, organisational principles, and risk-management framework.

2) Continuous training in relation to the activities carried out by the entity's personnel.

f) Implement remuneration and compensation policies for those who provide services to the entity, which must consider at least the manner or mechanism by which it will be prevented and verified that the remunerations and compensations do not give rise to or exacerbate conflicts of interest on the part of those who manage the resources of the entity itself and of those who advise or maintain commercial relationships with clients.

g) Establish information recording and processing systems with adequate protection and security measures that enable:

1) The board of directors or equivalent body to have timely access to information related to the development of the business, risk management, and any other information relevant to the performance of its functions.

2) The business areas and the risk-management and internal-audit functions to have access to information relevant to the performance of their functions.

3) The entity to comply with the disclosure of information required by the regulatory framework.

h) Periodically evaluate the adequacy of the resources of the risk-management and internal-audit functions to carry out their work, approve the allocation of the necessary resources to those functions, and monitor the degree of compliance with the budget assigned for that purpose.

i) Ensure that the minutes or equivalent documentation reflect the principal matters addressed in the sessions of the board of directors or equivalent body and the committees. All material prepared or presented to the board of directors or equivalent body or the committees must be duly documented and archived in accordance with the applicable general regulations on the matter, and must be permanently available for examination at the request of the Commission (CMF).

### Original Spanish

> "C.1. ROL DEL DIRECTORIO U ÓRGANO EQUIVALENTE
>
> El Directorio u órgano equivalente es el responsable de establecer la estructura organizacional, objetivos, políticas que permitan gestionar adecuadamente los riesgos que pueden afectar las actividades que desarrolle la entidad (marco de gestión de riesgos), debiendo asegurarse de contar con una apropiada cultura de gestión de riesgos, entendida como la adecuada comprensión del gobierno corporativo y riesgos inherentes a la entidad. Los miembros del directorio u órgano equivalente deberán contar con los conocimientos, experiencia y dedicación adecuados a este respecto.
>
> El directorio u órgano equivalente deberá dar cumplimiento, al menos, a los principios y elementos que se señalan a continuación:
>
> a) Aprobar los niveles de apetito por riesgo de aquellos previamente identificados. Una efectiva definición debiera cuantificar el nivel de riesgo que el directorio u órgano equivalente desee aceptar en consideración a los objetivos estratégicos de la entidad y las responsabilidades que le son aplicables por el marco regulatorio. Además, deberá informarse continuamente del cumplimiento del apetito por riesgo.
>
> b) Aprobar las políticas que se señalan en los literales C.2 al C.5 de esta Sección, considerando para ello:
>
> 1) Que las políticas implementadas para gestionar los riesgos sean coherentes con la misión, visión, objetivos estratégicos, los niveles de apetito por riesgo y el marco regulatorio que le es aplicable a la entidad.
>
> 2) Que las políticas se revisen y actualicen al menos anualmente o con la frecuencia necesaria en caso de que se produzcan cambios significativos tales como introducción de nuevos productos o servicios, o cambios en la regulación aplicable a la entidad.
>
> c) Establecer una estructura organizacional adecuada para la gestión de riesgos de la entidad, que considere lo siguiente:
>
> 1) La definición de los roles, competencias y responsabilidades que permitan realizar sus actividades y gestionar adecuadamente los riesgos que enfrenta la entidad. Lo anterior involucra la segregación apropiada de los deberes y las funciones claves, especialmente aquéllas que, si fueran realizadas por una misma persona, puedan dar lugar a errores que no se detecten o que expongan a la entidad o sus participantes a riesgos no deseados o no mitigados y controlados; y entre las áreas generadoras de riesgo y de control de estos.
>
> 2) La implementación de la función de gestión de riesgos, de conformidad con lo descrito en las C.4 y C.6 siguientes.
>
> 3) La implementación de la función de auditoría interna, de conformidad con lo descrito en las secciones C.5 y C.6 siguientes.
>
> 4) Que el directorio u órgano equivalente vele por el cumplimiento de la segregación de funciones y la independencia de las funciones de gestión de riesgos y de auditoría interna.
>
> 5) Contar con un Comité de Gestión de Riesgos o una instancia similar. Sin perjuicio de ello, el directorio u órgano equivalente deberá evaluar la pertinencia de conformar otros comités o instancias similares que le permitan tratar y monitorear aspectos relevantes de los negocios y la gestión de los riesgos, referidos a materias tales como, por ejemplo: Auditoría Interna; Prevención del Lavado de Activos, Financiamiento del Terrorismo y Financiamiento de Armas de Destrucción Masiva; Inversiones; Nuevos Servicios o Productos; Continuidad del Negocio; Seguridad de la Información y Ciberseguridad. El directorio u órgano equivalente deberá establecer los procedimientos para la conformación y funcionamiento de los comités o instancias similares, los cuales deberán quedar debidamente documentados, como también sus actuaciones, las que deberán ser reportadas al directorio en forma continua. Sin perjuicio de lo anterior, los Comités de Gestión de Riesgos y de Auditoría Interna (éste último, en caso de ser constituido) deberán estar integrados al menos por un miembro del directorio u órgano equivalente. Tratándose de entidades cuya dirección recae en un órgano colegiado, ningún director (o miembro del órgano equivalente) podrá ser parte del Comité de Gestión de Riesgos y del Comité de Auditoría Interna al mismo tiempo. La actuación de los comités que se conformen, en las materias antes mencionadas, deberá constar por escrito en actas, las que deberán reflejar con claridad los asuntos tratados.
>
> d) Aprobar los planes anuales de las funciones de gestión de riesgos y de auditoría interna y estar en conocimiento, en forma oportuna, de su cumplimiento y de los informes que elabore.
>
> e) Establecer una política de contratación y capacitación del personal de la entidad, de forma de contar con recursos humanos calificados. Esta política y programa deberá considerar:
>
> 1) La adecuada difusión de los valores, principios organizacionales y marco de gestión de riesgos de la entidad.
>
> 2) Capacitación continua en relación con las actividades que realiza el personal de la entidad.
>
> f) Implementar políticas de remuneración y compensación para quienes presten servicios a la entidad, las cuales considerarán al menos la forma o mecanismo mediante el que se prevendrá y verificará que con las remuneraciones y compensaciones no se produzcan o exacerben conflictos de intereses por parte de quienes gestionan recursos de la propia entidad y de quienes asesoran o mantienen relaciones comerciales con clientes.
>
> g) Establecer sistemas de registro y procesamiento de información con medidas de protección y seguridad adecuadas que permitan que:
>
> 1) El directorio u órgano equivalente tenga acceso oportuno a información relacionada con el desarrollo del negocio, la gestión de riesgos, y toda otra información relevante para el cumplimiento de sus funciones.
>
> 2) Las áreas de negocio y las funciones de gestión de riesgos y auditoría interna tengan acceso a información relevante para el cumplimiento de sus funciones.
>
> 3) La entidad dé cumplimiento a la divulgación de información que el marco regulatorio le exige.
>
> h) Evaluar periódicamente la suficiencia de recursos de las funciones de gestión de riesgos y auditoría interna para efectuar su labor, aprobar la asignación de los recursos necesarios para dichas funciones y monitorear el grado de cumplimiento del presupuesto asignado a tal fin.
>
> i) Asegurar que las actas o documentación equivalente den cuenta de las principales temáticas tratadas en las sesiones del directorio u órgano equivalente y los comités. Todo el material que se elabore o presente al directorio u órgano equivalente o los comités, deberá estar debidamente documentado y archivado de conformidad a las normas generales aplicables en la materia, y estar permanentemente disponible para su examen a solicitud de esta Comisión."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.2 to §IV.C.5 — policies the board must approve under item b).
- NCG 502 §IV.C.4 and §IV.C.6 — risk-management function and proportionality whose implementation the board must establish under item c)(2).
- NCG 502 §IV.C.5 and §IV.C.6 — internal-audit function and proportionality whose implementation the board must establish under item c)(3).

> **Source:** NCG 502 §IV.C.1 (12-ene-2024), as amended by NCG 524 item 29 (02-dic-2024).

---

## IV.C.2 — Policies, Procedures, and Control Mechanisms
**NCG anchor:** N° 502, Sección IV, C.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, policies-and-procedures, crowdfunding, alternative-trading

### Plain-English text

This subsection establishes the general principles applicable to the entity's policies, procedures, and control mechanisms, and the minimum policies and procedures the entity must implement.

### Original Spanish

> "C.2. POLÍTICAS, PROCEDIMIENTOS Y MECANISMOS DE CONTROL"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.2.1 — general principles applicable to the policies, procedures, and control mechanisms.
- NCG 502 §IV.C.2.2 — minimum policies and procedures the entity must implement.

> **Source:** NCG 502 §IV.C.2 (12-ene-2024).

---

## IV.C.2.1 — General Aspects
**NCG anchor:** N° 502, Sección IV, C.2.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, internal-control, policies-and-procedures, crowdfunding, alternative-trading

### Plain-English text

The entity's policies, procedures, and control mechanisms must take into account the following principles:

a) Effective operating policies, procedures, and controls must be established that relate to the number or type of participants; volume of transactions; investment projects, financing needs, or financial instruments traded, quoted, or offered; and in respect of each of the businesses or activities developed.

b) Policies must set out the general principles and guidelines established by the board of directors or equivalent body to guide the activities of the organisation.

c) With the aim of ensuring compliance with the policies approved by the board of directors or equivalent body, a procedure must be defined that incorporates at a minimum: the description of the principal activities that compose it and the identification of those responsible; the determination of those responsible for supervising and controlling the outcome of the activities carried out; documentation evidencing the execution of the activities that make up the procedures; the definition and description of the controls associated with those activities. In the case of outsourced activities, there must always be a person responsible within the organisation for the control of those activities.

d) Policies, procedures, and control mechanisms must be formally established and documented, being consistent with the risk-appetite levels defined by the entity.

### Original Spanish

> "C.2.1. ASPECTOS GENERALES
>
> Las políticas, procedimientos y mecanismos de control de la entidad, deberán tener en cuenta los siguientes principios:
>
> a) Se deberán establecer políticas, procedimientos y controles operativos efectivos que guarden relación con el número o tipo de participantes; volumen de operaciones; proyectos de inversión, necesidades de financiamiento o instrumentos financieros negociados, cotizados u ofertados; y respecto de cada uno de los negocios o actividades que se desarrolle.
>
> b) Las políticas deberán exponer los principios generales y directrices establecidas por el directorio u órgano equivalente para orientar las actividades de la organización.
>
> c) Con el fin de asegurar el cumplimiento de las políticas aprobadas por el directorio u órgano equivalente, se deberá definir un procedimiento que incorpore al menos: la descripción de las actividades principales que lo componen y la identificación de sus responsables; determinación de los responsables de supervisar y controlar el resultado de las actividades ejecutadas; documentación que evidencia la ejecución de las actividades que conforman los procedimientos; definición y descripción de los controles asociados a dichas actividades. En el caso de actividades externalizadas, siempre deberá existir una persona responsable dentro de la organización respecto al control de estas.
>
> d) Las políticas, procedimientos y mecanismos de control deberán estar formalmente establecidos y documentados, siendo consistentes con los niveles de apetito por riesgo que haya definido la entidad."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.2.2 — minimum policies and procedures supplementing these general aspects.

> **Source:** NCG 502 §IV.C.2.1 (12-ene-2024), as amended by NCG 524 item 30 (02-dic-2024).

---

## IV.C.2.2 — Minimum Policies and Procedures to Implement
**NCG anchor:** N° 502, Sección IV, C.2.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, policies-and-procedures, conflicts-of-interest, aml, crowdfunding, alternative-trading

### Plain-English text

The entity must have, at a minimum, the policies and procedures detailed below.

**a) Eligibility of financial instruments, investment projects, or financing needs eligible to be traded or offered**

Policies must be defined to prevent that instruments subject to trading in alternative trading systems, or the investment projects or financing needs offered on crowdfunding platforms, as applicable, result in a fraudulent purpose. For these purposes, alternative trading systems and crowdfunding platforms must establish the procedures referred to in Sections II.D and II.C, respectively, as regards the access and approval requirements and processes that apply before admitting financial instruments or investment projects or financing needs, as applicable.

**b) Conflicts of interest**

Entities must define policies and procedures that specify the methods by which all potential conflicts of interest inherent in the services it offers will be identified, managed, and monitored. The policies and procedures must address the identification, prevention, and monitoring of conflicts that may arise between the crowdfunding platform and the published investment projects or financing needs, or between the alternative trading system and the issuers of financial instruments admitted to trading, as applicable to the type of service provided.

**c) Offer of products consistent with the investor's needs, expectations, and risk tolerance**

Entities must define policies and procedures aimed at offering investors financial instruments, investment projects, or financing needs consistent with their needs, expectations, and risk tolerance, providing them with information that enables them to understand and accept the risk they are assuming, avoiding offering products that are not consistent with their needs, expectations, and risk tolerance, as provided in Article 28 of Ley N° 21.521.

Entities must have procedures to ensure compliance with the aforementioned obligation. In those cases where a client decides to contract a service that, in the entity's opinion, is not consistent with the needs, expectations, or risks that the client has communicated, the entity must be able to evidence that it was duly warned, if requested by the Commission. For these purposes, the procedures may consider requiring from potential investors information such as their knowledge and experience as an investor, their financial situation, and investment or savings objectives, and other information of this nature that the entity considers relevant.

The entity must establish procedures that enable it to monitor compliance with the product-offering policy on a periodic basis, including a description of the procedures for detecting needs, expectations, and risk tolerance associated with each investor. The entity may establish exceptions to this policy, in the event that the product offering is directed at clients that qualify as institutional investors or qualified investors among those indicated in numbers 2, 3, and 4 of Section II of General Regulation N° 216.

**d) Prevention of money laundering and financing of terrorism**

Entities must have policies and procedures for compliance with the legal and regulatory provisions relating to the prevention of money laundering, financing of terrorism, and financing of weapons of mass destruction, as provided in Ley N° 19.913 and in the regulations issued by the Financial Analysis Unit.

**e) Information to the investor**

The entity must define policies and procedures that determine how it will ensure that clients have truthful, sufficient, and timely information relating to the products or services offered, as provided in Article 28 of Ley N° 21.521.

These policies and procedures must specify, at a minimum, the information that must be known by clients in accordance with Section III of this regulation and any additional information the entity considers necessary to be known, as well as the frequency established for that purpose. For their part, the procedures must relate to how the entity will monitor compliance with these provisions.

**f) Compliance with legal and regulatory operating requirements**

Policies and procedures must be defined that specify how compliance with the applicable legal and regulatory requirements for the entity will be monitored and ensured.

In addition, procedures must be defined for the event of non-compliance with the legal operating requirements occurring, which must be reported promptly to the Commission (CMF).

**g) Management of queries, complaints, and claims**

Entities must define policies and procedures that enable them to manage and resolve queries, claims, and complaints from their clients, workers, and the general public. For that purpose, they must consider, at a minimum, a manual that establishes, in simple terms, the minimum background information that will be required in order to make a query, complaint, or claim, and that describes how to use the specialised channels arranged for those purposes. The manual must establish:

1) A procedure for resolving queries from the public that considers the different channels arranged for these purposes. The mechanism must allow the queries made to be followed up.

2) Procedures that enable the confidentiality of the person who makes the claim or complaint to be safeguarded.

3) Clearly defining how the seriousness or relevance of the complaint or claim will be rated, and how it will be communicated to the appropriate bodies, including the board of directors or equivalent body in the case of the most relevant ones.

4) The bodies that will participate in the management of the queries, complaints, or claims according to the relevance or seriousness defined for each case. In any event, the management of claims must be carried out by a unit independent of the area in which they originated.

5) The maximum times established for managing and responding to each query, complaint, or claim according to its seriousness or relevance.

6) A register of the queries, complaints, and claims together with the seriousness or relevance assigned and the solution implemented.

7) Defining a body responsible for analysing, monitoring, and proposing measures to prevent the situations that gave rise to the queries, complaints, or claims from recurring.

### Original Spanish

> "C.2.2. POLÍTICAS Y PROCEDIMIENTOS A IMPLEMENTAR
>
> La entidad deberá contar, al menos, con las políticas y procedimientos que se detallan a continuación.
>
> a) Admisibilidad de instrumentos financieros, proyectos de inversión o necesidades de financiamiento elegibles para transar u ofertar
>
> Se deberán definir políticas que permitan prevenir que los instrumentos sujetos a negociación en los sistemas alternativos de transacción, o los proyectos de inversión o necesidades de financiamiento que se oferten en plataformas de financiamiento colectivo, según corresponda, resulten en una finalidad fraudulenta. Para estos efectos, los sistemas alternativos de transacción y las plataformas de financiamiento colectivo deberán establecer los procedimientos a los que se refiere la Sección II.D y II.C, respectivamente, en cuanto a requisitos y procesos de acceso y de aprobación que se aplican antes de admitir instrumentos financieros o proyectos de inversión o necesidades de financiamiento, según corresponda.
>
> b) Conflictos de intereses
>
> Las entidades deberán definir políticas y procedimientos que especifiquen los métodos según los cuales se identificarán, manejarán y vigilarán todos los potenciales conflictos de intereses inherentes a los servicios ofrecidos por ella. Las políticas y procedimientos deberán considerar la identificación, prevención y monitoreo de los conflictos que puedan surgir entre la plataforma de financiamiento colectivo con los proyectos de inversión o necesidades de financiamiento publicados, o entre el sistema alternativo de transacción con los emisores de instrumentos financieros admitidos a transacción, según corresponda al tipo de servicio prestado.
>
> c) Oferta de productos acorde a las necesidades, expectativas y disposición al riesgo del inversionista
>
> Las entidades deberán definir políticas y procedimientos tendientes a que se ofrezcan a los inversionistas instrumentos financieros proyectos de inversión o necesidades de financiamiento acordes a sus necesidades, expectativas y disposición al riesgo, entregándoles información que les permita entender y aceptar el riesgo que están asumiendo, evitando ofrecer productos que no sean acordes a sus necesidades, expectativas y disposición al riesgo, según lo dispuesto en el artículo 28 de la ley N°21.521.
>
> Las entidades deberán contar con procedimientos para asegurar el cumplimiento de la citada obligación. En aquellos casos en que un cliente decida contratar un servicio que en opinión de la entidad no sea acorde a las necesidades, expectativas o riesgos que este le haya comunicado la entidad deberá poder acreditar que aquello fue debidamente advertido, en caso de que le sea solicitado por la Comisión. Para estos efectos, los procedimientos podrán considerar el requerir a sus potenciales inversionistas antecedentes tales como información sobre sus conocimientos y experiencia como inversionista, su situación financiera y objetivos de inversión o ahorro, y otra información de esta naturaleza que la entidad considere relevante.
>
> La entidad deberá establecer procedimientos que permitan monitorear el cumplimiento de la política de oferta de productos en forma periódica, incluyendo una descripción de los procedimientos de detección de necesidades, expectativas y disposición al riesgo asociadas a cada inversionista. La entidad podrá establecer excepciones en esta política, en caso de que la oferta de productos esté dirigida a clientes que tengan la calidad de inversionista institucional o inversionista calificado de entre los señalados en los números 2, 3 y 4 de la Sección II de la Norma de Carácter General N°216.
>
> d) Prevención del lavado de activos y financiamiento del terrorismo
>
> Las entidades deberán contar con políticas y procedimientos para el cumplimiento de las disposiciones legales y normativas relativas a la prevención del lavado de activos, financiamiento del terrorismo y financiamiento de armas de destrucción masiva, según lo dispuesto en la ley N°19.913 y en la normativa dictada por la Unidad de Análisis Financiero.
>
> e) Información al inversionista
>
> La entidad deberá definir políticas y procedimientos que determinen la forma en que se garantizará que los clientes cuenten con información veraz, suficiente y oportuna, relativa a los productos o servicios ofrecidos, según lo dispuesto en el artículo 28 de la ley N°21.521.
>
> Estas políticas deberán especificar, al menos, la información que debe ser conocida por los clientes de acuerdo con la Sección III de esta normativa, y aquella que adicionalmente la entidad estime necesaria que se conozca, así como también la periodicidad establecida para ello. Por su parte, los procedimientos deberán estar referidos a la forma en que la entidad controlará el cumplimiento de estas disposiciones.
>
> f) Cumplimiento de requisitos legales y normativos de funcionamiento
>
> Se deberán definir políticas y procedimientos que especifiquen la forma en que se monitoreará y garantizará el debido cumplimiento de los requisitos legales y normativos aplicables a la entidad.
>
> Además, se deberá definir procedimientos en caso de presentarse eventos de incumplimiento de los requisitos legales de funcionamiento, los cuales deberán ser informados oportunamente a esta Comisión.
>
> g) Gestión de consultas, reclamos y denuncias
>
> Las entidades deberán definir políticas y procedimientos que le permita gestionar y resolver las consultas, denuncias y reclamos de sus clientes, trabajadores y el público general. Para ello deberá considerar, al menos, un manual que establezca, en términos simples, los antecedentes mínimos que se requerirán para efectuar una consulta, denuncia o reclamo, y que describa cómo utilizar los canales especializados que se hubieren dispuesto para esos efectos. El manual deberá establecer:
>
> 1) Procedimiento para resolver las consultas del público que considere los diferentes canales que se disponga para estos efectos. El mecanismo deberá permitir hacer un seguimiento de las consultas efectuadas.
>
> 2) Procedimientos que permitan resguardar la reserva de quien formula el reclamo o denuncia.
>
> 3) Definir claramente cómo se calificará la gravedad o relevancia de la denuncia o reclamo, y cómo se comunicará a las instancias que corresponda, incluyendo al directorio u órgano equivalente en el caso de aquellas más relevantes.
>
> 4) Las instancias que participarán en la gestión de las consultas, denuncias o reclamos de acuerdo con la relevancia o la gravedad que se hubiere definido para cada caso. Con todo, la gestión de los reclamos deberá ser efectuada por una unidad independiente del área donde se originaron los mismos.
>
> 5) Los tiempos máximos establecidos para gestionar y responder cada consulta, denuncia o reclamo de acuerdo con su gravedad o relevancia.
>
> 6) Un registro de las consultas, denuncias y reclamos junto con la gravedad o relevancia asignada y la solución implementada.
>
> 7) Definir una instancia encargada de analizar, monitorear y proponer medidas para evitar que las situaciones que generaron las consultas, denuncias o reclamos se repitan."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- Ley 21.521 Art. 28 — investor information obligation, referenced in items c) and e).
- Ley N° 19.913 — money-laundering prevention law referenced in item d).
- NCG 216 §II Nos. 2, 3, 4 — institutional/qualified investor definitions referenced in item c).
- NCG 502 §II.C and §II.D — access and approval procedures for crowdfunding platforms and alternative trading systems referenced in item a).
- NCG 502 §III — investor-information obligations the policies under item e) must reference.
- NCG 502 §IV.C.2.1 — general aspects framework of which this is a minimum-content specification.

> **Source:** NCG 502 §IV.C.2.2 (12-ene-2024), as amended by NCG 524 item 31 (02-dic-2024).

---

## IV.C.3 — Operational Risk
**NCG anchor:** N° 502, Sección IV, C.3
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, operational-risk, crowdfunding, alternative-trading

### Plain-English text

Crowdfunding platforms and alternative trading systems, in order for the entity to develop adequate operational-risk management, must consider the elements set out below, adapting them on the basis of their business model, volume of transactions, and number and type of clients:

a) Establish operational risk-management policies and procedures, which must include, at a minimum, the following areas, described in the following sections: information security and cybersecurity; business continuity; and outsourcing of services. The areas mentioned must be considered by the entity in the reports produced by the bodies responsible for risk management and internal audit, as applicable. The operational risk-management policies and procedures must be designed to provide reasonable assurance that the entity can carry out the business operations in a continuous and efficient manner, even in the presence of disruptive events, safeguarding its services, processes, and information assets. These policies and procedures must be established and approved by the board of directors or equivalent body, and disseminated to all personnel within the organisation. In addition, those policies and procedures must establish the risk-appetite levels defined by the board of directors or equivalent body, which will determine the need to avoid, reduce, transfer, or accept risks, and accordingly, design mitigating controls.

b) Have key operational-risk measurement indicators consistent with the entity's comprehensive risk evaluation and monitoring methodology, while at the same time enabling alert levels to be established and the effectiveness of the controls adopted to be evaluated. The detail of the calculation of these indicators must be expressly included in the entity's operational risk-management policies and procedures.

Where the entity belongs to a business group, the operational risk-management may be carried out by a person of that group, provided that such person maintains independence from the group's internal audit.

### Original Spanish

> "C.3. RIESGO OPERACIONAL
>
> Las plataformas de financiamiento colectivo y los sistemas alternativos de transacción, con el objeto de que la entidad desarrolle una adecuada gestión de riesgo operacional, deberán dar considerar los elementos que se señalan a continuación, adaptándolos de acuerdo con su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Establecer políticas y procedimientos de gestión de riesgo operacional, las que deberán incluir, al menos, los siguientes ámbitos relacionados, descritos en las próximas secciones: seguridad de la información y ciberseguridad; continuidad de negocio; y externalización de servicios. Los ámbitos mencionados deberán ser considerados por la entidad en los informes que realicen las instancias encargadas de la gestión de riesgos y la auditoría interna, según corresponda. Las políticas y procedimientos de gestión de riesgo operacional deben estar diseñadas para brindar una seguridad razonable que la entidad pueda desarrollar las operaciones del negocio en forma continua y eficiente, incluso ante la presencia de eventos disruptivos, salvaguardando sus servicios, procesos y activos de información. Estas políticas y procedimientos deben ser establecidas y aprobadas por el directorio u órgano equivalente, y ser difundidas a todo el personal dentro de la organización. Además, dichas políticas y procedimientos deben establecer los niveles de apetito por riesgo definidos por el directorio u órgano equivalente, que determinará la necesidad de evitar, reducir, transferir o aceptar los riesgos, y acorde con ello, diseñar controles mitigantes.
>
> b) Contar con indicadores claves de medición del riesgo operacional consistentes con la metodología de evaluación y monitoreo de riesgos integrales de la entidad, permitiendo al mismo tiempo establecer niveles de alerta y evaluar la eficacia de los controles adoptados. El detalle de cálculo de estos indicadores deberá ser incluido expresamente en las políticas y procedimientos de gestión de riesgo operacional de misma la entidad.
>
> En el caso que la entidad pertenezca a un grupo empresarial, la gestión de riesgo operacional podrá ser desempeñada por una persona de dicho grupo, siempre que mantenga su independencia de la auditoría interna del grupo."

> **TN:** Item a) reads "deberán dar considerar los elementos" in the source — an apparent drafting slip ("dar" interpolated before "considerar"); rendered idiomatically as "must consider the elements". Item b) closes with "de misma la entidad" (word order inversion of "de la misma entidad"); rendered as "the entity's" without replicating the inversion.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.3.1 — information security and cybersecurity area.
- NCG 502 §IV.C.3.2 — business continuity area.
- NCG 502 §IV.C.3.3 — outsourcing of services area.

> **Source:** NCG 502 §IV.C.3 (12-ene-2024), as amended by NCG 524 item 32 (02-dic-2024).

---

## IV.C.3.1 — Information Security and Cybersecurity
**NCG anchor:** N° 502, Sección IV, C.3.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, information-security, cybersecurity, crowdfunding, alternative-trading

### Plain-English text

This subsection establishes the information-security and cybersecurity obligations within operational-risk management. It comprises general provisions (C.3.1.1, below) and the procedures for managing information security and cybersecurity (C.3.1.2, reproduced in this block).

The entity must consider the following procedures, and adapt them in relation to its business model, volume of transactions, and number and type of clients (C.3.1.2 — Procedures for the management of information security and cybersecurity):

**a) Identification**

1) Have a clear definition of information assets that is sufficient for the adequate management of the associated risks.

2) Classify information, taking into account the dimensions of availability, confidentiality, and integrity.

3) Define critical information assets, which are those considered indispensable for the operation of the business, with a level of detail sufficient to enable their management, classified from the perspective of availability, confidentiality, and integrity.

4) Implement an inventory of information assets that enables the principal characteristics of the asset to be known, considering at least: hardware, software, applications, devices, systems, data, personnel, external information systems, processes, facilities, workstations, servers, storage media, and physical documentation.

5) Update the information-asset inventory on a continuous basis, for which purpose the various operational risk-management processes must report the information that may have an effect on that inventory.

**b) Protection and Detection**

1) Access controls for facilities and business, operational infrastructure, and technical units, among which are data centres, alternative power sources, and backups of data and applications.

2) Access controls for systems, so as to mitigate the risks of impersonation or improper use by third parties. In the case of critical facilities, infrastructure, and systems, the use of multifactor authentication mechanisms must be favoured.

3) Implementation of tools for recording, controlling, and monitoring the activities carried out by users and administrators of systems and information assets, including high-privilege users.

4) Procedures to grant, revoke, or modify the privileges granted to system users, network services, operating systems, databases, and business applications on the basis of personnel roles and responsibilities and only to the extent strictly necessary for the performance of their current functions.

5) Controls that enable the mitigation of risks arising from the use of mobile devices and remote access by internal or external personnel, as well as Internet of Things (IoT) devices.

6) Mechanisms for controlling and monitoring environmental conditions for the secure location of equipment and tools, taking into account humidity and temperature conditions and the possibility of fires and natural disasters.

7) Procedures for the security of the entity's operations and communications, through the implementation of:

i) Tools and controls for the proactive detection and protection against cyberattacks and other anomalous activities. For example, the use of web application firewalls, intrusion prevention systems, data loss prevention systems, denial-of-service prevention systems, email filtering, antivirus, anti-spyware, and anti-malware, among others.

ii) A process for managing the configuration of systems and information assets.

iii) Tools and procedures for the backup, transfer, restoration, and secure deletion of information, within the organisation and with third parties, including physical and electronic media. For this purpose, the following must be considered:

a) The provisions relating to the backup, transfer, restoration, and deletion of information in the regulations that safeguard the protection of data and the rights of investors, including non-disclosure agreements.

b) The backup management processes that ensure the availability, confidentiality, and integrity of information upon the occurrence of an incident, which must be consistent with the analysis of risks for the management of business continuity in accordance with the provisions of section C.3.2.2 below. Backups of information should, as far as possible, be kept in environments free of malicious code and in facilities distinct from the production sites. In addition, periodic backup-restoration tests must be carried out, at least annually, in order to verify that critical information can be recovered in the event that the original data are lost or damaged.

c) Tools and procedures for the identification, authentication, and access control for the digital channels through which the entity interacts with its clients.

d) Tools and procedures so that information that the entity decides to store or process through cloud services retains its characteristics of availability, confidentiality, and integrity.

**c) Response and Recovery**

1) The entity must have procedures for the management of information-security and cybersecurity incidents, considering:

i) A high-level body defined by the board of directors or equivalent body responsible for the management of information-security and cybersecurity incidents.

ii) Incident response and recovery procedures, approved by the board of directors or equivalent body, that consider the timely recovery of critical functions, backup and support processes, critical information assets, and interdependencies with third parties in the event of incidents. Those procedures must consider the provisions relating to the recording, reporting, and communication of incidents of section IV.C.7 of this regulation. Likewise, depending on the severity of the incident, the situation must be escalated to the board of directors or equivalent body for decision-making. The incident response and recovery procedures must be updated at least annually, whenever changes are recorded in information assets or incidents occur that threaten their security.

iii) Communication procedures to keep the board of directors or equivalent body, other interested parties (both internal and external), the relevant authorities on information-security and cybersecurity matters, and this Commission informed in a timely manner about the occurrence of an incident and the measures adopted to resolve it. Those procedures must consider the provisions relating to the recording, reporting, and communication of incidents of section IV.C.7 of this regulation. Likewise, in the case of incidents affecting the quality or continuity of services to clients or a publicly known event, the institution will be responsible for informing users in a timely manner about the occurrence of that event, and must update the available information until the conclusions on the causes of the incident and the measures adopted to resolve it are known, including compliance with the regulations safeguarding the protection of personal data and the rights of investors.

2) Procedures for the development, acquisition, and updating of the entity's technological infrastructure, that consider:

i) The entity's technological infrastructure needs.

ii) Implementation of a change-management process, so as to ensure that the modifications made to information assets resulting from the introduction of new products, systems, and activities are carried out and monitored in a secure and controlled manner.

As part of this process, prior to the production deployment of a service or information asset, functional, integral, security, cybersecurity, continuity, and regulatory tests must be carried out, with the aim of ensuring that there is no adverse impact on information security and on business operations.

iii) Implementation of a technological-obsolescence management process, that enables software and hardware to be maintained with support, except for duly substantiated exceptions that do not generate adverse effects on the operation of the entity's services. The use of unauthorised or non-commercially licensed software must be prevented.

iv) Implementation of a software security-update (patch) management process.

3) The entity must have a procedure for the continuous improvement of information-security and cybersecurity tools, procedures, and controls that considers:

i) Collecting and analysing information on the functioning of information assets.

ii) Analysing information-security and cybersecurity incidents and the effectiveness of the measures adopted to resolve them.

iii) Carrying out tests to identify threats and vulnerabilities in information security:

a) The tests must be carried out with a frequency no greater than one year, and be supervised by the body responsible for the entity's Risk Management.

The tests must be based on planned and designed risk scenarios in order to demonstrate that the mechanisms and tools implemented to preserve information security adequately comply with their objective, including cyberattacks.

b) The results of the tests carried out must be reported to the board of directors or equivalent body, including recommendations for improvement of the tools, procedures, and controls.

### Original Spanish

> "C.3.1. SEGURIDAD DE LA INFORMACIÓN Y CIBERSEGURIDAD
>
> C.3.1.2 PROCEDIMIENTOS PARA LA GESTIÓN DE SEGURIDAD DE LA INFORMACIÓN Y CIBERSEGURIDAD
>
> La entidad deberá considerar los siguientes procedimientos, y adaptarlos en relación con su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Identificación
>
> 1) Contar con una definición clara de activos de información que sea suficiente para la adecuada gestión de los riesgos asociados.
>
> 2) Clasificar la información, teniendo en consideración las dimensiones de disponibilidad, confidencialidad e integridad.
>
> 3) Definir los activos de información críticos, que son los activos considerados como indispensables para el funcionamiento del negocio, con un nivel suficiente de detalle que permita su gestión, clasificados desde una perspectiva de disponibilidad, confidencialidad e integridad.
>
> 4) Implementar un inventario de activos de información que permita conocer las principales características del activo, considerando al menos: hardware, software, aplicaciones, dispositivos, sistemas, datos, personal, sistemas de información externos, procesos, instalaciones, estaciones de trabajo, servidores, medios de almacenamiento y documentación física.
>
> 5) Actualizar el inventario de activos de información en forma continua, para lo cual los distintos procesos de gestión de riesgo operacional deberán reportar la información que pueda tener efecto en dicho inventario.
>
> b) Protección y Detección
>
> 1) Controles de acceso a las instalaciones e infraestructuras de negocios, operativas y dependencias técnicas, dentro de las que se encuentran los centros de datos, fuentes de energía alternativa y respaldos de datos y aplicativos.
>
> 2) Controles de acceso a los sistemas, de manera de mitigar los riesgos de suplantación o uso indebido por parte de terceros. En el caso de instalaciones, infraestructuras y sistemas críticos, se deberá privilegiar el uso de mecanismos de autenticación multifactor.
>
> 3) Implementación de herramientas de registro, control y monitoreo de las actividades realizadas por los usuarios y administradores de sistemas y activos de información, incluyendo usuarios de alto privilegio.
>
> 4) Procedimientos para otorgar, revocar o modificar los privilegios otorgados a los usuarios de los sistemas, servicios de red, sistemas operativos, bases de datos y aplicaciones de negocios en función de los roles y responsabilidades del personal y sólo lo estrictamente necesario para que éste cumpla sus funciones actuales.
>
> 5) Controles que permitan mitigar los riesgos derivados del uso de dispositivos móviles y del acceso remoto realizado por personal interno o externo, así como también los dispositivos Internet de las Cosas (IoT).
>
> 6) Mecanismos de control y monitoreo de las condiciones ambientales para la localización segura para los equipos y herramientas, teniendo en consideración las condiciones de humedad, temperatura y la posibilidad de incendios y desastres naturales.
>
> 7) Procedimientos de seguridad de las operaciones y comunicaciones de la entidad, mediante la implementación de:
>
> i) Herramientas y controles para la detección y protección proactiva de ataques cibernéticos y otras actividades anómalas. Por ejemplo, el uso de firewalls de aplicaciones web, sistemas de prevención de intrusos, sistemas de prevención de pérdida de datos, sistemas anti-denegación de servicios, filtrado de correo electrónico, antivirus, anti-spyware y anti-malware, entre otros.
>
> ii) Un proceso de gestión de la configuración de los sistemas y activos de información.
>
> iii) Herramientas y procedimientos para el respaldo, transferencia, restauración y eliminación segura de la información, al interior de la organización y con terceros, incluyendo medios físicos y electrónicos. Para ello se deberá considerar:
>
> a) Las disposiciones relativas al respaldo, transferencia, restauración y eliminación de información en las normas que resguardan la protección de datos y los derechos de los inversionistas, incluyendo acuerdos de no divulgación.
>
> b) Los procesos de administración de respaldos que aseguren la disponibilidad, confidencialidad e integridad de la información ante la ocurrencia de un incidente, el que debe ser concordante con el análisis de los riesgos para la gestión de la continuidad del negocio de acuerdo con lo dispuesto en la sección C.3.2.2 siguiente. Los respaldos de la información se debiesen mantener en lo posible en ambientes libres de códigos maliciosos y en instalaciones distintas a los sitios de producción. Además, se deben realizar pruebas de restauración de respaldos periódicas, al menos anuales, con el fin de verificar que la información crítica puede ser recuperada en caso de que los datos originales se pierdan o se dañen.
>
> c) Herramientas y procedimientos de identificación, autenticación y control de acceso para los canales digitales a través de los cuales la entidad interactúa con sus clientes.
>
> d) Herramientas y procedimientos para que la información que la entidad decidiere almacenar o procesar mediante servicios en la nube conserve sus características de disponibilidad, confidencialidad e integridad.
>
> c) Respuesta y Recuperación
>
> 1) La entidad deberá contar con procedimientos para la gestión de incidentes de seguridad de la información y ciberseguridad, considerando:
>
> i) Una instancia de alto nivel definida por el directorio u órgano equivalente encargada de la gestión de incidentes de seguridad de la información y ciberseguridad.
>
> ii) Procedimientos de respuesta y recuperación ante incidentes, aprobados por el directorio u órgano equivalente, que consideren la recuperación oportuna de las funciones críticas, los procesos de respaldo y soporte, los activos de información críticos y las interdependencias con terceros en caso de incidentes. Dichos procedimientos deberán considerar las disposiciones relativas al registro, reporte y comunicación de incidentes de la sección IV.C.7. de esta normativa. Asimismo, dependiendo de la severidad del incidente, corresponderá escalar la situación al directorio u órgano equivalente para la toma de decisiones. Los procedimientos de respuesta y recuperación ante incidentes deberán actualizarse al menos anualmente, cada vez que se registran cambios en los activos de información o se produzcan incidentes que amenacen la seguridad de estos.
>
> iii) Procedimientos de comunicaciones para mantener informado en forma oportuna al directorio u órgano equivalente, a otras partes interesadas (tanto internas como externas), a las autoridades pertinentes en materia de seguridad de la información y ciberseguridad, y a esta Comisión, de la ocurrencia de un incidente y las medidas adoptadas para resolverlo. Estos procedimientos deberán considerar las disposiciones relativas al registro, reporte y comunicación de incidentes de la sección IV.C.7. de esta normativa. Asimismo, tratándose de incidentes que afecten la calidad o continuidad de los servicios a los clientes o de un hecho de público conocimiento, la institución será responsable de informar oportunamente a los usuarios sobre la ocurrencia de dicho evento, debiendo actualizar la información disponible hasta que se conozcan las conclusiones sobre las causas del incidente y las medidas adoptadas para resolverlo, incluyendo el cumplimiento de las normas que resguardan la protección de datos personales y los derechos de los inversionistas.
>
> 2) Procedimientos para el desarrollo, adquisición y actualización de la infraestructura tecnológica de la entidad, que consideren:
>
> i) Las necesidades de infraestructura tecnológica de la entidad.
>
> ii) Implementación de un proceso de gestión de cambio, de forma de asegurar que las modificaciones realizadas a los activos de información producto de la introducción de nuevos productos, sistemas y actividades sean efectuadas y monitoreadas de manera segura y controlada.
>
> Como parte de este proceso, previo al paso de producción de un servicio o activo de información se deben realizar pruebas de carácter funcional, integral, de seguridad, de ciberseguridad, de continuidad y normativas, con el propósito de asegurar que no hubiere un impacto adverso en la seguridad de la información y en las operaciones del negocio.
>
> iii) Implementación de un proceso de gestión de obsolescencia tecnológica, que permita mantener el software y hardware con soporte, salvo las excepciones debidamente fundamentadas que no generen efectos adversos para la operación de los servicios de la entidad. Se deberá prevenir el uso de software no autorizado o sin licenciamiento comercial
>
> iv) Implementación de un proceso de gestión de actualizaciones de seguridad de software (parches).
>
> 3) La entidad deberá contar con un procedimiento para el mejoramiento continuo de las herramientas, procedimientos y controles de seguridad de la información y ciberseguridad que considere:
>
> i) Recolectar y analizar información sobre el funcionamiento de activos de información.
>
> ii) Analizar los incidentes de seguridad de la información y ciberseguridad y la efectividad de las medidas adoptadas para resolverlo.
>
> iii) Ejecutar pruebas para identificar amenazas y vulnerabilidades en la seguridad de la información:
>
> a) Las pruebas deberán ser realizadas con una periodicidad no mayor a un año, y ser supervisadas por la instancia responsable de la Gestión de Riesgos de la entidad.
>
> Las pruebas deberán estar basadas en escenarios de riesgo planificados y diseñados para demostrar que los mecanismos y herramientas implementados para preservar la seguridad de la información cumplen adecuadamente con su objetivo, incluyendo ataques cibernéticos.
>
> b) Los resultados de las pruebas realizadas deberán ser reportados al directorio u órgano equivalente, incluyendo recomendaciones de mejora en las herramientas, procedimientos y controles."

> **TN:** The PDF subdivides §IV.C.3.1 into two headed parts — C.3.1.1 (Disposiciones Generales) and C.3.1.2 (Procedimientos para la Gestión de Seguridad de la Información y Ciberseguridad). The regulation's table of contents lists only C.3.1.1 as a nested entry under C.3.1; there is no separate C.3.1.2 anchor. To preserve all source text under the contracted anchor set, the C.3.1.2 "Procedimientos" content is reproduced verbatim within this C.3.1 parent block, and the C.3.1.1 "Disposiciones Generales" content appears in the C.3.1.1 block below.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.3.1.1 — general provisions on information security and cybersecurity.
- NCG 502 §IV.C.3.2.2 — business-continuity procedures with which backup management must be consistent (item b)(7)(iii)(b)).
- NCG 502 §IV.C.7 — recording, reporting, and communication of incidents referenced in the response and recovery procedures.

> **Source:** NCG 502 §IV.C.3.1 (12-ene-2024), as amended by NCG 524 item 34 (02-dic-2024).

---

## IV.C.3.1.1 — General Provisions
**NCG anchor:** N° 502, Sección IV, C.3.1.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, information-security, cybersecurity, crowdfunding, alternative-trading

### Plain-English text

In the area of information security and cybersecurity, operational-risk management must include the following elements, adapting them on the basis of their business model, volume of transactions, and number and type of clients:

a) Have an information-security and cybersecurity policy that considers at least the following:

1) Procedures for the implementation and maintenance of an information-security and cybersecurity management system, so as to safeguard the availability, confidentiality, and integrity of information assets.

2) Risk-appetite levels in relation to information security and cybersecurity.

3) Principal functions and responsibilities on the matter.

4) Procedures for the evaluation of information-security and cybersecurity risks that could be assumed when introducing new products, services, systems, undertaking new activities, or defining new processes.

5) The information-security and cybersecurity policies will form part of the entity's risk-management policies, and must be updated and approved at least annually by the board of directors or equivalent body, or with a greater frequency in the event of significant changes.

b) Have an information and communication technology (ICT) policy that considers at least the following:

1) Definition of the lines of responsibility for the management of the entity's information assets.

2) Definition of the ICT processes that ensure an adequate design, transition, service operation, and management through its information assets.

3) Definition of the procedures that must be followed for the adequate management of ICT processes.

c) Definition of the necessary number of persons with verifiable knowledge or experience in information-security and cybersecurity standards.

d) Establishment of the procedures so that the entity's personnel, including the board of directors or equivalent body, contribute to an adequate management of information-security and cybersecurity risks, in accordance with their roles and responsibilities, through the implementation of:

1) Dissemination, training, and awareness procedures that address information-security risks, vulnerabilities, and threats, the management of these, and the lessons learned with respect to incidents on this matter, in order to ensure that the entity's personnel are duly prepared to face the contingency scenarios defined and that they understand their responsibilities in the management of those risks.

2) Contractual agreements with employees that establish their responsibilities and those of the entity on information-security and cybersecurity matters, including sanctions.

e) Generation of contractual agreements for the revocation of information-access rights and destruction of information assets as part of the process of position change or termination of an employee.

f) Audit of the information-security and cybersecurity management processes, with the depth and scope necessary, that considers aspects such as compliance with the policies and the effectiveness of the procedures and controls defined on these matters.

g) Provision of procedures that enable the board of directors or equivalent body to be kept informed in a timely and periodic manner about the information-security and cybersecurity management system. The reporting of information on these matters must be recorded.

### Original Spanish

> "C.3.1.1 DISPOSICIONES GENERALES
>
> En el ámbito de seguridad de la información y ciberseguridad, la gestión de riesgo operacional deberá incluir los siguientes elementos, adaptándolos de acuerdo a su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Contar con una política de seguridad de la información y ciberseguridad que considere al menos lo siguiente:
>
> 1) Procedimientos para la implementación y mantención de un sistema de gestión de seguridad de la información y ciberseguridad, de forma de resguardar la disponibilidad, confidencialidad e integridad de los activos de información.
>
> 2) Niveles de apetito por riesgo en materia de seguridad de la información y ciberseguridad.
>
> 3) Principales funciones y responsabilidades sobre la materia.
>
> 4) Procedimientos para la evaluación de los riesgos de seguridad de la información y ciberseguridad que se podrían estar asumiendo al introducir nuevos productos, servicios, sistemas, emprender nuevas actividades o definir nuevos procesos.
>
> 5) Las políticas de seguridad de la información y ciberseguridad formarán parte de las políticas de gestión de riesgos de la entidad, debiendo ser actualizadas y aprobadas al menos anualmente por el directorio, u órgano equivalente, o con una periodicidad mayor en caso de cambios significativos.
>
> b) Contar con una política de tecnologías de información y comunicación (TIC), que considere al menos lo siguiente:
>
> 1) Definición de las líneas de responsabilidad en cuanto a la gestión de los activos de información en la entidad.
>
> 2) Definición de los procesos TIC que aseguren un adecuado diseño, transición, operación de servicio y gestión a través de sus activos de información.
>
> 3) Definición de los procedimientos que se deberán seguir para la adecuada gestión de los procesos TIC.
>
> c) Definición del número necesario de personas con conocimientos o experiencia comprobables en estándares de seguridad de la información y ciberseguridad.
>
> d) Establecimiento de los procedimientos para que el personal de la entidad, incluyendo el directorio u órgano equivalente, contribuya a una adecuada gestión de los riesgos de seguridad de la información y ciberseguridad, de conformidad con sus roles y responsabilidades, mediante la implementación de:
>
> 1) Procedimientos de difusión, capacitación y concientización que traten sobre los riesgos, vulnerabilidades y amenazas a la seguridad de la información, la gestión de estos, y las lecciones aprendidas respecto de los incidentes en esta materia, para garantizar que el personal de la entidad esté debidamente preparado para enfrentar los escenarios de contingencia definidos y que comprendan sus responsabilidades en la gestión de dichos riesgos.
>
> 2) Acuerdos contractuales con los empleados que establezcan sus responsabilidades y las de la entidad en materia de seguridad de la información y ciberseguridad, incluyendo sanciones.
>
> e) Generación de acuerdos contractuales para la revocación de derechos de acceso a información y destrucción de activos de información como parte del proceso de cambio de posición o desvinculación de un empleado.
>
> f) Auditoría de los procesos de gestión de la seguridad de la información y ciberseguridad, con la profundidad y alcance necesario, que considere aspectos tales como el cumplimiento de las políticas y la eficacia de los procedimientos y controles definidos en estas materias.
>
> g) Disposición de procedimientos que le permitan al directorio u órgano equivalente mantenerse informado en forma oportuna y periódica sobre el sistema de gestión de la seguridad de la información y ciberseguridad. Deberá dejarse constancia del reporte de la información de estas materias."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.3.1 — information-security and cybersecurity subsection of which these are the general provisions (and which reproduces the C.3.1.2 procedures).

> **Source:** NCG 502 §IV.C.3.1.1 (12-ene-2024), as amended by NCG 524 item 33 (02-dic-2024).

---

## IV.C.3.2 — Business Continuity
**NCG anchor:** N° 502, Sección IV, C.3.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, business-continuity, crowdfunding, alternative-trading

### Plain-English text

This subsection establishes the business-continuity obligations within operational-risk management. It comprises general provisions (C.3.2.1) and the procedures for the management of business continuity (C.3.2.2).

### Original Spanish

> "C.3.2. CONTINUIDAD DEL NEGOCIO"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.3.2.1 — general provisions on business continuity.
- NCG 502 §IV.C.3.2.2 — procedures for the management of business continuity.

> **Source:** NCG 502 §IV.C.3.2 (12-ene-2024).

---

## IV.C.3.2.1 — General Provisions
**NCG anchor:** N° 502, Sección IV, C.3.2.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, business-continuity, crowdfunding, alternative-trading

### Plain-English text

In the area of business continuity, operational-risk management must take into account the following elements and adapt them on the basis of the business model, volume of transactions, and number and type of clients:

a) Have a business-continuity policy that considers at least the following:

1) Response procedures upon the occurrence of internal or external events that could create an interruption in the continuity of business operations. For entities classified in Block 3, these procedures must relate at least to the carrying out of a Business Impact Analysis (BIA, by its initials in English) and a Risk Impact Analysis (RIA, by its initials in English).

2) Establish the principal functions and responsibilities on the matter, in particular which bodies will be responsible for defining, designing, executing, and improving the procedures and methodologies for business-continuity management. The business-continuity policies will form part of the entity's risk-management policies, and must be updated and approved at least annually by the board of directors or equivalent body or with a lesser frequency in the event of significant changes.

b) For entities belonging to Block 3, have persons with verifiable knowledge or experience in business-continuity standards and experience in the management of the associated risks, whose principal activities will be the development and improvement of the policies, procedures, and controls for business-continuity management. In the case of Block 1 and Block 2 entities, the person in charge of those matters must at least have completed an academic programme related to them.

c) Establish training and awareness policies and procedures to ensure that the entity's personnel are duly prepared to face the contingency scenarios defined and that they understand their responsibilities in the management of the risks of the business-continuity system.

d) The board of directors or equivalent body must be kept informed about business-continuity management, for which purpose it must have procedures that enable it to be informed in a timely and periodic manner. The reporting of information on these matters must be recorded.

### Original Spanish

> "C.3.2.1 DISPOSICIONES GENERALES
>
> En el ámbito de continuidad de negocio, la gestión de riesgo operacional deberá tomar en cuenta los siguientes elementos y adaptarlos de acuerdo con el modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Contar con una política de continuidad de negocio que considere a lo menos lo siguiente:
>
> 1) Procedimientos de respuesta ante la ocurrencia de eventos internos o externos que pudieran crear una interrupción en la continuidad de las operaciones del negocio. Para las entidades clasificadas en el Bloque 3, estos procedimientos se deberán referir al menos a la ejecución de un Análisis de Impacto del Negocio (BIA, por su sigla en inglés) y un Análisis de Impacto de Riesgo (RIA, por su sigla en inglés).
>
> 2) Establecer las principales funciones y responsabilidades sobre la materia, en especial, cuáles serán las instancias encargadas de definir, diseñar, ejecutar y mejorar los procedimientos y metodologías para la gestión de continuidad de negocio. Las políticas de continuidad del negocio formarán parte de las políticas de gestión de riesgos de la entidad, debiendo ser actualizada y aprobada al menos anualmente por el directorio u órgano equivalente o con una periodicidad menor en caso de cambios significativos.
>
> b) Para las entidades pertenecientes al Bloque 3, contar con personas con conocimientos o experiencia comprobables en estándares de continuidad de negocio y experiencia en la gestión de los riesgos asociados, cuyas actividades principales serán el desarrollo y mejora de las políticas, procedimientos y controles para la gestión de continuidad de negocio. En caso de entidades del Bloque 1 y Bloque 2, la persona a cargo de esas materias deberá al menos haber cursado un programa académico relacionado a éstas.
>
> c) Establecer políticas y procedimientos de capacitación y concientización para garantizar que el personal de la entidad esté debidamente preparado para enfrentar los escenarios de contingencia definidos y que comprendan sus responsabilidades en la gestión de los riesgos del sistema de continuidad de negocio.
>
> d) El directorio u órgano equivalente deberá mantenerse informado sobre la gestión de continuidad de negocio, para lo cual deberá disponer de procedimientos que le permitan informarse de manera oportuna y periódica. Deberá dejarse constancia del reporte de la información en estas materias."

> **TN:** Item a)(2) states the business-continuity policies must be updated and approved "al menos anualmente ... o con una periodicidad menor en caso de cambios significativos" (literally "at least annually ... or with a lesser frequency in the event of significant changes"). In context "periodicidad menor" denotes a shorter interval (i.e., more frequent updates) when significant changes occur; rendered literally as "with a lesser frequency" to preserve the source wording, noting the intended meaning is more-frequent updating. The parallel C.3.1.1.a)(5) uses "periodicidad mayor" for the same notion.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.3.2.2 — procedures for the management of business continuity supplementing these general provisions.
- NCG 502 §IV.C.6 — proportionality classification defining Block 3 entities subject to BIA and RIA obligations.

> **Source:** NCG 502 §IV.C.3.2.1 (12-ene-2024), as amended by NCG 524 item 35 (02-dic-2024).

---

## IV.C.3.2.2 — Procedures for the Management of Business Continuity
**NCG anchor:** N° 502, Sección IV, C.3.2.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, business-continuity, crowdfunding, alternative-trading

### Plain-English text

Entities must implement the following elements for the management of business continuity, adapting them in relation to the business model, volume of transactions, and number and type of clients:

a) Have a Business Continuity and Disaster Recovery Plan, approved annually by the board of directors or equivalent body, that contains:

1) The procedures for the management of continuity events, with a level of detail that enables the various affected bodies to determine the activities to be developed in each defined scenario.

2) The criteria for the activation of the Plan and for the return to normality. This includes evaluating in a timely manner the business-continuity risks that could be assumed when introducing new products, systems, undertaking new activities, or defining new processes.

3) Roles and responsibilities of personnel.

The frequency of updating of this Plan could be greater depending on the entity's own regulations, or at the request of this Commission.

b) Entities classified in Block 3, described below, must carry out or update, at least annually, in the event of events that threaten the continuity of business operations, a BIA in order to identify the processes of greatest relevance for business continuity, the impact that an interruption of those processes would have, and the times and resources necessary for their continuity and recovery. The BIA must be carried out at the strategic, tactical, and operational level. From those processes, and taking into account the risk-appetite levels defined, the following must be determined:

1) The maximum tolerable periods of disruption (MTPD by its initials in English);

2) The recovery time objectives (RTO by its initials in English);

3) The recovery point objectives (RPO by its initials in English);

4) The minimum acceptable levels of operation; and

5) The human, technological, infrastructure, and information resources necessary for their continuity and recovery.

The results of the BIA must be approved by the board of directors or equivalent body.

c) In the case of alternative trading systems, they must have a secondary physical site or a site in the cloud that enables the entity to resume operation in the event that it is interrupted at the principal site, allowing the most relevant business processes to be restored, such as platforms, infrastructure, systems, and data processing.

d) Entities classified in Block 3 must carry out or update, at least annually, a risk impact analysis (RIA) that enables the business-continuity risks that, if materialised, would cause an interruption in the most relevant processes of the entity to be identified and analysed. For the foregoing, internal and external scenarios must be considered, contemplating, among others, the total and partial failure of technological systems; malicious attacks affecting cybersecurity; the absence of critical personnel; the impossibility of accessing or using physical facilities; and the failure to provide critical services contracted to suppliers.

e) Entities classified in Block 3, in consideration of the results of the BIA and the RIA, must define a business-continuity strategy that has as its objective maintaining the continuity of the most relevant processes, considering preventive measures to reduce the probability of materialisation of damage, minimise the recovery time, and limit the impact on the entity's business operations.

f) The Crisis Plan must be tested annually, in which the escalation, communication, management, and reporting procedures for operational-continuity events are determined, in order to keep the board of directors or equivalent body, all interested parties, and this Commission informed in a timely manner about relevant information regarding the continuity event, the measures adopted to resolve it, and to coordinate an adequate response within the recovery point and time objectives provided for in the BIA (entities classified in Block 3 referred to in the preceding sections).

g) Have a procedure for the continuous improvement of the policies, plans, and procedures of business continuity with the aim of reducing the response times when an identical or similar incident recurs; identifying possible improvements in the processes; facilitating the exchange of knowledge; and having information available that enables decision-making to be supported in the event of new incidents materialising.

h) Test annually the Business Continuity and Disaster Recovery Plan, so as to ensure that it is adequate and effective, without prejudice to the fact that this Commission may request a different frequency for entities classified in Block 3. These tests must consider at least the following:

1) They must be supervised by the body responsible for the entity's Risk Management.

2) Being based on risk scenarios that resemble real events, including severe but plausible scenarios. The foregoing, in order to demonstrate that the business-continuity procedures will function if necessary, including cyberattacks, natural disasters, and health contingencies.

3) Block 1 and 2 entities may use business-continuity indicators different from those established in preceding item b).

Reports of the results of the tests carried out must be issued to the board of directors or equivalent body, containing recommendations and actions to implement improvements to the Business Continuity and Disaster Recovery Plan.

### Original Spanish

> "C.3.2.2 PROCEDIMIENTOS PARA LA GESTIÓN DE LA CONTINUIDAD DE NEGOCIOS
>
> Las entidades deberán implementar los siguientes elementos para la gestión de la continuidad de negocios, adaptándolos en relación con el modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Contar con un Plan de Continuidad de Negocio y Recuperación de Desastres, aprobado anualmente por el directorio u órgano equivalente, que contenga:
>
> 1) Los procedimientos para la gestión de eventos de continuidad, con un nivel de detalle que permita a las distintas instancias afectadas determinar las actividades a desarrollar en cada escenario definido.
>
> 2) Los criterios para la activación del Plan y para la vuelta a la normalidad. Esto incluye evaluar oportunamente los riesgos asociados a la continuidad de negocios que se podrían estar asumiendo al introducir nuevos productos, sistemas, emprender nuevas actividades o definir nuevos procesos.
>
> 3) Roles y responsabilidades del personal.
>
> La periodicidad de actualización de este Plan podría ser mayor dependiendo de la normativa propia de la entidad, o a requerimiento de esta Comisión.
>
> b) Las entidades clasificadas en el Bloque 3, descrito más abajo, deberán realizar o actualizar, al menos anualmente, ante eventos que amenacen la continuidad de las operaciones del negocio, un BIA con el objeto de identificar los procesos de mayor relevancia para la continuidad de negocio, el impacto que tendría una interrupción de esos procesos, y los tiempos y recursos necesarios para la continuidad y recuperación de estos. El BIA deberá realizarse a nivel estratégico, táctico y operativo. De esos procesos, y considerando los niveles de apetito por riesgo definidos, se deberá determinar:
>
> 1) Los tiempos máximos tolerables de interrupción (MTPD por sus siglas en inglés);
>
> 2) Los tiempos objetivos de recuperación (RTO por sus siglas en inglés);
>
> 3) Los puntos objetivos de recuperación (RPO por sus siglas en inglés);
>
> 4) Los niveles mínimos aceptables de operación; y
>
> 5) Los recursos humanos, tecnológicos y de infraestructura e información necesarios para su continuidad y recuperación.
>
> Los resultados del BIA deberán ser aprobados por el directorio u órgano equivalente.
>
> c) En el caso de sistemas alternativos de transacción deben disponer de un sitio secundario físico o en la nube que permita a la entidad reanudar la operación en caso de que esta se vea interrumpida en el sitio principal, permitiendo restablecer los procesos de mayor relevancia del negocio, tales como plataformas, infraestructura, sistemas y procesamiento de datos.
>
> d) Las entidades clasificadas en el Bloque 3 deberán realizar o actualizar, al menos anualmente, una evaluación de impacto de riesgos (RIA) que permita identificar y analizar los riesgos de continuidad de negocio que, de materializarse, provocarían una interrupción en los procesos de mayor relevancia de la entidad. Para lo anterior, se deberá considerar escenarios internos y externos, contemplando, entre otros, la falta total y parcial de los sistemas tecnológicos; ataques maliciosos que afecten la ciberseguridad; la ausencia de personal crítico; la imposibilidad de acceder o utilizar las instalaciones físicas; y la falta de provisión de los servicios críticos contratados a proveedores.
>
> e) Las entidades clasificadas en el Bloque 3, en consideración de los resultados del BIA y el RIA, deberán definir una estrategia de continuidad de negocio que tenga por objetivo mantener la continuidad de los procesos de mayor relevancia, considerando medidas preventivas para reducir la probabilidad de materialización de daños, minimizar el tiempo de recuperación y limitar el impacto en las operaciones del negocio de la entidad.
>
> f) Probar anualmente el Plan de Crisis en el que se determine los procedimientos de escalamiento, comunicaciones, gestión y reporte de eventos de continuidad operacional para mantener informado en forma oportuna al directorio u órgano equivalente, a todas las partes interesadas y a esta Comisión, respecto de información relevante respecto del evento de continuidad, las medidas adoptadas para resolverlo y para coordinar una respuesta adecuada dentro de los puntos objetivos y tiempos objetivos de recuperación previstos en el BIA (entidades clasificadas en el Bloque 3 al que se refieren las secciones anteriores).
>
> g) Contar con un procedimiento para el mejoramiento continuo de las políticas, planes y procedimientos de continuidad del negocio con el objeto de disminuir los tiempos de respuesta cuando se repita un incidente igual o similar; identificar posibles mejoras en los procesos; facilitar el intercambio de conocimientos; y disponer de información que permita apoyar la toma de decisiones en caso de materializarse nuevos incidentes.
>
> h) Probar anualmente el Plan de Continuidad de Negocio y Recuperación de Desastres, de forma de asegurar que es adecuado y efectivo, sin perjuicio de que esta Comisión pueda solicitar una periodicidad diferente para las entidades clasificadas en el Bloque 3. Estas pruebas deberán considerar a lo menos lo siguiente:
>
> 1) Deberán ser supervisadas por la instancia responsable de la Gestión de Riesgos de la entidad.
>
> 2) Estar basadas en escenarios de riesgo que se asimilen a eventos reales incluyendo escenarios severos pero plausibles. Lo anterior, para demostrar que los procedimientos de continuidad de negocio funcionarán en caso de ser necesarios, incluyendo ataques cibernéticos, desastres naturales y contingencias sanitarias.
>
> 3) Las entidades del Bloque 1 y 2, podrán utilizar indicadores de continuidad del negocio distintos de los establecidos en el literal b) precedente.
>
> Se deberán emitir reportes de los resultados de las pruebas realizadas al directorio u órgano equivalente, que contengan recomendaciones y acciones para implementar mejoras al Plan de Continuidad de Negocio y Recuperación ante Desastres."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.3.2.1 — general provisions on business continuity these procedures supplement.
- NCG 502 §IV.C.6 — proportionality classification defining the Block 1, 2, and 3 thresholds referenced throughout.
- NCG 502 §IV.C.3.1 — backup management (§IV.C.3.1.2.b)(7)(iii)(b)) that must be consistent with this continuity analysis.

> **Source:** NCG 502 §IV.C.3.2.2 (12-ene-2024), as amended by NCG 524 item 36 (02-dic-2024).

---

## IV.C.3.3 — Outsourcing of Services
**NCG anchor:** N° 502, Sección IV, C.3.3
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, outsourcing, crowdfunding, alternative-trading

### Plain-English text

This subsection establishes the obligations relating to the outsourcing of services within operational-risk management. It comprises the outsourcing risks (C.3.3.1) and the procedures for the management of outsourced services (C.3.3.2).

### Original Spanish

> "C.3.3. EXTERNALIZACIÓN DE SERVICIOS"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.3.3.1 — outsourcing risks.
- NCG 502 §IV.C.3.3.2 — procedures for the management of outsourced services.

> **Source:** NCG 502 §IV.C.3.3 (12-ene-2024).

---

## IV.C.3.3.1 — Outsourcing Risks
**NCG anchor:** N° 502, Sección IV, C.3.3.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, outsourcing, crowdfunding, alternative-trading

### Plain-English text

The services provided by suppliers, relating to regulatory compliance, business continuity, information security, and the quality of the services, products, information, and image of the contracting entity, must be considered in the operational risk-management processes of the entity. In that regard, for the evaluation of supplier-contracting risks, the following risks, among others, must be considered:

1) Substitution risk: the possibility of substituting or not a supplier within a determined period that guarantees the continuity of the contracted service.

2) Intervention risk: the possibility that the entity has to take over the contracted function.

3) Subcontracting risk: the possibility that the supplier in turn subcontracts all or part of the service, reducing the entity's capacity to supervise the subcontracted function.

4) Concentration risk: the possibility that an entity contracts one or several services with the same supplier that is difficult to substitute, increasing the possibility of prolonged failures or interruptions.

### Original Spanish

> "C.3.3.1 RIESGOS DE EXTERNALIZACIÓN
>
> Los servicios prestados por proveedores, relacionados con el cumplimiento normativo, la continuidad del negocio, la seguridad de la información y la calidad de los servicios, productos, información e imagen de la entidad contratante, deberán ser considerados en los procesos de gestión de riesgo operacional de la entidad. En tal sentido, para la evaluación de riesgos de contratación de proveedores, se deberán considerar, entre otros, los siguientes riesgos:
>
> 1) Riesgo de sustitución: la posibilidad de sustituir o no a un proveedor dentro de un plazo determinado que garantice la continuidad del servicio contratado.
>
> 2) Riesgo de intervención: la posibilidad de que la entidad tenga que hacerse cargo de la función contratada.
>
> 3) Riesgo de subcontratación: la posibilidad de que el proveedor subcontrate a su vez todo o parte del servicio, reduciendo la capacidad de la entidad de supervisar la función subcontratada.
>
> 4) Riesgo de concentración: la posibilidad que una entidad contrate uno o varios servicios a un mismo proveedor que sea difícil de sustituir, incrementando la posibilidad de fallas o interrupciones prolongadas."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.3.3.2 — procedures for the management of outsourced services that address these risks.

> **Source:** NCG 502 §IV.C.3.3.1 (12-ene-2024), as amended by NCG 524 item 37 (02-dic-2024).

---

## IV.C.3.3.2 — Procedures for the Management of Outsourced Services
**NCG anchor:** N° 502, Sección IV, C.3.3.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, outsourcing, cloud, crowdfunding, alternative-trading

### Plain-English text

In the area of outsourcing of services, operational-risk management must consider the following elements and adapt them on the basis of the business model, volume of transactions, and number and type of clients:

a) Have a policy for the outsourcing of services that considers at least the following:

1) Define the governance structure and the procedures to be followed to authorise and manage the outsourcing of services to third parties, including the reporting and responsibility lines.

2) Establish the objectives in relation to the outsourcing of services.

3) Establish the risk-appetite levels in the outsourcing of services and the mitigation strategies.

4) Comply with the provisions on information security, cybersecurity, and business continuity.

5) Establish the procedures for the determination of critical services. In that regard, in order to understand a service as critical, the following considerations must be taken into account:

i) The effect that a weakness or failure in the provision or execution of the service has on regulatory compliance, business continuity, information security, and the quality of the services, products, information, and image of the contracting entity.

ii) The complexity of the associated commercial functions.

iii) The degree to which the service can be transferred quickly to another supplier, considering the costs and the time to do so.

6) Define the services that can only be outsourced with the prior approval of the board of directors or equivalent body.

7) Define the minimum elements that the service-provision contract must incorporate.

8) Define the risk-management elements that will not be applied to activities that, by their nature, do not have a relevant impact on the provision of the services.

9) Include the outsourcing policies as part of the entity's risk-management policies, which must be approved and updated at least annually by the board of directors or equivalent body, or with a greater frequency in the event of significant internal or external changes.

10) Consider the substitution, intervention, subcontracting, and concentration risks of the preceding section.

b) Establish procedures for the selection, contracting, and monitoring of suppliers that consider:

1) A definition of the particular contracting criteria, when the supplier is a related entity. These criteria must be aimed at avoiding the conflicts of interest that may arise.

2) The incorporation into the analysis of elements that enable a due-diligence process to be carried out, so as to ensure that the suppliers have an adequate commercial reputation, financial solvency, experience, and sufficient resources to guarantee the quality of the provision of the service. In the case of services in which full compliance with the aforementioned conditions cannot be guaranteed, as may be the case of data-processing services carried out abroad, the entity's board of directors or equivalent body must review and evaluate background information supporting the quality of the service provided, the financial soundness of the supplier, and the existence of adequate personal-data protection legislation in the applicable jurisdiction, taking responsibility for the availability, confidentiality, and integrity of the information delivered to the contracted supplier.

c) Contemplate in the contracts with the suppliers of outsourced services the following minimum contents:

1) A clear description of the contracted service and the term of validity.

2) The service-provision obligations of the supplier, defining agreed service levels. The entity must define the situations that will be considered serious contractual breaches and grounds for early termination of the contract.

3) The obligation to communicate any event that may have a material impact on the capacity to carry out the outsourced service.

4) The information-security, cybersecurity, and business-continuity requirements that the supplier must comply with, which must be consistent with the provisions established on this matter by the entity. The suppliers must have incident-management and business-continuity procedures that enable them to continue providing the services in the event that disruptive situations arise.

5) The documentation of the operational, administrative, and technological procedures specific to the contracted service. In the case of the existence of chain subcontracting, the entity must verify compliance with the conditions agreed with the initial service supplier and the entities subcontracted by the latter.

6) The procedures for the periodic evaluation and monitoring of the quality of the provision of the outsourced service. The entity may agree with the supplier the carrying out of audits by designated third parties or by the entity itself, which will be responsible in the last instance for guaranteeing the quality of the provision of the outsourced service.

7) The strategies for the termination of the provision of outsourced services without prejudice to the entity's operations, considering those situations in the Business Continuity and Disaster Recovery Plan.

d) Have a register of outsourced services, in order to manage the subcontracting risks, which must include at least the following information:

1) Identification of the outsourced service, including a brief description of it and of the data involved if it is a critical service, whether there is chain subcontracting, and whether it is carried out in the cloud.

2) Identification of the supplier, including whether or not it is a related entity.

3) Start, renewal, and termination date of the service.

4) In the case of data-processing services, a description of the data and processing that are subcontracted, the security measures adopted, and the geographic location of the supplier.

5) In the case of chain subcontracting, the entities to which the supplier subcontracts the service must be detailed, a description of the associated risks and whether the supplier carries out a control of the quality of the provision of the service subcontracted in chain.

e) Periodically monitor that the suppliers comply with the conditions agreed in order to guarantee the quality of the provision of the service. The entity will be responsible for the quality of the outsourced services.

f) In the event that the entity decides to contract services for accessing and processing information in the cloud, or that the supplier as part of the chain subcontracting considers cloud services, a reinforced analysis of the risks inherent in those services must be carried out, analysing in particular how it could affect the availability, confidentiality, and integrity of the information, and the business continuity of the entity. That analysis must take into account factors such as:

1) The independent certifications regarding the management of information security and the quality of the provision of the supplier's service.

2) The execution of the outsourcing-of-services contract directly between the entity and the supplier, with the aim of minimising the risks in this type of service.

3) The processing or storage of information in other jurisdictions, and in that case the existence of regulations safeguarding the protection of personal data, the availability, confidentiality, and integrity of information, and the resolution of legal contingencies.

4) The existence of adequate security mechanisms of the supplier, both physical and logical, that enable the components of the infrastructure in the cloud that the entity shares with other clients of the supplier to be isolated, so as to prevent leaks of information or events that may affect the availability, confidentiality, and integrity of the entity's data.

5) The use of encryption techniques for the data that the entity establishes, in accordance with their nature and sensitivity.

g) Evaluate that the supplier of the contracted services possesses adequate knowledge and experience.

h) Maintain personnel with the due knowledge and experience to carry out the control of the provision of services performed by its suppliers. Likewise, it must also oversee due compliance with those regulatory and legal aspects that could affect the provision of the contracted services.

The board of directors or equivalent body must be kept informed about the matters relating to the outsourcing of services, for which purpose it must have procedures that enable it to be informed in a timely and periodic manner. The reporting of information on these matters must be recorded.

### Original Spanish

> "C.3.3.2 PROCEDIMIENTOS PARA LA GESTIÓN DE SERVICIOS EXTERNALIZADOS
>
> En el ámbito de externalización de servicios, la gestión de riesgo operacional deberá considerar los siguientes elementos y adaptarlos de acuerdo con el modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Contar con una política para la externalización de servicios que considere a lo menos lo siguiente:
>
> 1) Definir la estructura de gobierno y de los procedimientos a seguir para autorizar y gestionar la externalización de servicios por terceros, incluyendo las líneas de reporte y de responsabilidad.
>
> 2) Establecer los objetivos en materia de externalización de servicios.
>
> 3) Establecer los niveles de apetito por riesgo en la externalización de servicios y las estrategias de mitigación.
>
> 4) Cumplir con las disposiciones en materia de seguridad de la información, ciberseguridad y continuidad de negocios.
>
> 5) Establecer los procedimientos para la determinación de los servicios críticos. En tal sentido, para entender como crítico un servicio se deberán tener en cuenta las siguientes consideraciones:
>
> i) El efecto que una debilidad o falla en la provisión o ejecución del servicio tenga sobre el cumplimiento normativo, continuidad del negocio, seguridad de la información y la calidad de los servicios, productos, información e imagen de la entidad contratante.
>
> ii) La complejidad de las funciones comerciales asociadas.
>
> iii) El grado en que el servicio puede transferirse rápidamente a otro proveedor, considerando los costos y el tiempo para hacerlo.
>
> 6) Definir los servicios que solo pueden ser externalizados con la aprobación previa del directorio u órgano equivalente.
>
> 7) Definir los elementos mínimos que deberá incorporar el contrato de prestación de servicios.
>
> 8) Definir los elementos de la gestión de riesgos que no serán aplicados a actividades que por su naturaleza no tengan impacto relevante en la prestación de los servicios.
>
> 9) Incluir a las políticas de externalización de servicios como parte de las políticas de gestión de riesgos de la entidad, debiendo ser aprobada y actualizada al menos anualmente por el directorio u órgano equivalente, o con una frecuencia mayor en caso de cambios internos o externos significativos.
>
> 10) Considerar los riesgos de sustitución, intervención, subcontratación y concentración de la sección anterior.
>
> b) Establecer procedimientos para la selección, contratación y monitoreo de proveedores que consideren:
>
> 1) Una definición de los criterios particulares de contratación, cuando el proveedor se trate de una entidad relacionada. Estos criterios deberán estar destinados a evitar los conflictos de intereses que se pueden presentar.
>
> 2) La incorporación al análisis de elementos que permitan llevar a cabo un proceso de debida diligencia, de forma de asegurar que los proveedores tengan una adecuada reputación comercial, solvencia financiera, experiencia y recursos suficientes para garantizar la calidad de la provisión del servicio. En el caso de servicios en los que no se pueda garantizar el pleno cumplimiento de las condiciones mencionadas, como puede ser el caso de servicios de procesamiento de datos realizados en el extranjero, el directorio u órgano equivalente de la entidad deberá revisar y evaluar antecedentes que respalden la calidad del servicio prestado, la solidez financiera del proveedor y la existencia de una adecuada legislación de protección de datos personales en la jurisdicción aplicable, haciéndose responsable por la disponibilidad, confidencialidad e integridad de la información entregada al proveedor contratado.
>
> c) Contemplar en los contratos con los proveedores de servicios externalizados los siguientes contenidos mínimos:
>
> 1) Una descripción clara del servicio contratado y el plazo de vigencia.
>
> 2) Las obligaciones de prestación del servicio por parte del proveedor, definiendo niveles de servicio acordados. La entidad deberá definir las situaciones que se considerarán graves incumplimientos contractuales y causales de término anticipado del contrato.
>
> 3) La obligación de comunicar cualquier acontecimiento que pueda tener un impacto material en la capacidad para llevar a cabo el servicio externalizado.
>
> 4) Los requisitos de seguridad de la información, ciberseguridad y continuidad de negocios que deberá cumplir el proveedor, que deben ser concordantes con las disposiciones establecidas en esta materia por la entidad. Los proveedores deberán contar con procedimientos de gestión de incidentes y continuidad de negocios que le permitan seguir brindando los servicios en el evento que se presenten situaciones disruptivas.
>
> 5) La documentación de los procedimientos operacionales, administrativos y tecnológicos propios del servicio contratado. En el caso de existir subcontratación en cadena, la entidad deberá verificar el cumplimiento de las condiciones pactadas con el proveedor de servicios inicial y las entidades subcontratadas por este último.
>
> 6) Los procedimientos para la evaluación y monitoreo periódico de la calidad de la provisión del servicio externalizado. La entidad podrá pactar con el proveedor la realización de auditorías por terceros designados o por la propia entidad, quien será responsable en última instancia por garantizar la calidad de la provisión del servicio externalizado.
>
> 7) Las estrategias para el término de la prestación de servicios externalizados sin perjudicar las operaciones de la entidad, considerando esas situaciones en el Plan de Continuidad del Negocio y Recuperación ante Desastres.
>
> d) Contar con un registro de servicios externalizados, para gestionar los riesgos de subcontratación, que deberá incluir al menos la siguiente información:
>
> 1) Identificación del servicio externalizado, incluyendo una breve descripción del mismo y de los datos involucrados si corresponde a un servicio crítico, si existe subcontratación en cadena, y si se lleva a cabo en la nube.
>
> 2) Identificación del proveedor, incluyendo si corresponde a una entidad relacionada o no.
>
> 3) Fecha de inicio, renovación y término del servicio.
>
> 4) En el caso de servicios de procesamiento de datos, una descripción de los datos y tratamientos que se subcontratan, las medidas de seguridad adoptadas, y la ubicación geográfica del proveedor.
>
> 5) En caso de subcontratación en cadena, se deberá detallar cuáles son las entidades a las que el proveedor subcontrata el servicio, una descripción de los riesgos asociados y si el proveedor realiza un control de la calidad de la provisión del servicio subcontratado en cadena.
>
> e) Monitorear periódicamente que los proveedores cumplen con las condiciones pactadas para garantizar la calidad de la provisión del servicio. La entidad será responsable de la calidad de los servicios externalizados.
>
> f) En el caso que la entidad decida contratar servicios de acceso y tratamiento de información en la nube, o que el proveedor como parte de la subcontratación en cadena considere los servicios en la nube, se deberá realizar un análisis reforzado de los riesgos inherentes a esos servicios, analizando en particular cómo podría afectarse la disponibilidad, confidencialidad e integridad de la información, y la continuidad de negocio de la entidad. Ese análisis deberá tener en consideración factores tales como:
>
> 1) Las certificaciones independientes respecto a la gestión de la seguridad de la información y la calidad de la prestación del servicio del proveedor.
>
> 2) La celebración del contrato de externalización de servicios directamente entre la entidad y el proveedor, con la finalidad de minimizar los riesgos en este tipo de servicios.
>
> 3) El procesamiento o almacenamiento de información en otras jurisdicciones, y en ese caso la existencia de normas que resguarden la protección de datos personales, la disponibilidad, confidencialidad e integridad de la información y la resolución de contingencias legales.
>
> 4) La existencia de adecuados mecanismos de seguridad del proveedor, tanto físicos como lógicos, que permitan aislar los componentes de la infraestructura en la nube que la entidad comparte con otros clientes del proveedor, de manera de prevenir fugas de información o eventos que puedan afectar la disponibilidad, confidencialidad e integridad de los datos de la entidad.
>
> 5) La utilización de técnicas de encriptación para los datos que la entidad establezca, de acuerdo con su naturaleza y sensibilidad
>
> g) Evaluar que el proveedor de los servicios contratados posea adecuados conocimientos y experiencia.
>
> h) Mantener personal con el debido conocimiento y experiencia para efectuar el control de la prestación de servicios efectuada por sus proveedores. Asimismo, también deberá vigilar el debido cumplimiento de aquellos aspectos regulatorios y legales que pudiesen afectar la provisión de los servicios contratados.
>
> El directorio u órgano equivalente deberá mantenerse informado sobre las materias referidas a la externalización de servicios, para lo cual deberá disponer de procedimientos que le permitan informarse de manera oportuna y periódica. Deberá dejarse constancia del reporte de la información en estas materias."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.3.3.1 — outsourcing risks (substitution, intervention, subcontracting, concentration) referenced in items a)(10).
- NCG 502 §IV.C.3.2.2 — Business Continuity and Disaster Recovery Plan referenced in item c)(7).

> **Source:** NCG 502 §IV.C.3.3.2 (12-ene-2024), as amended by NCG 524 item 38 (02-dic-2024).

---

## IV.C.4 — Risk-Management Function
**NCG anchor:** N° 502, Sección IV, C.4
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, risk-management-function, crowdfunding, alternative-trading

### Plain-English text

This subsection establishes the requirements for the risk-management function applicable to crowdfunding platforms and alternative trading systems. It comprises general provisions (C.4.1) and the risk-management process (C.4.2).

### Original Spanish

> "C.4. FUNCIÓN DE GESTIÓN DE RIESGOS"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.4.1 — general provisions on the risk-management function.
- NCG 502 §IV.C.4.2 — risk-management process.

> **Source:** NCG 502 §IV.C.4 (12-ene-2024).

---

## IV.C.4.1 — General Provisions
**NCG anchor:** N° 502, Sección IV, C.4.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, risk-management-function, crowdfunding, alternative-trading

### Plain-English text

The body responsible for the risk-management function has the purpose of ensuring that the activities of the risk-management process are adequately developed in the entity (risk-management framework), in accordance with the policies and procedures established for that purpose.

The risk-management function may be carried out by a natural person or internal unit, in accordance with Section C.6 below. That function, in the case of Blocks 2 and 3, must be independent of the operational and business areas of the entity and of the body responsible for the internal-audit function, with direct reporting to the board of directors or equivalent body.

Where the entity belongs to a business group, the risk-management function of the entity may be exercised by the corporate risk-management unit, to the extent that it has thorough knowledge of the entity's risk-management framework and control environment and complies with the requirements established in this regulation, which must be agreed by the board of directors or equivalent body. The appropriateness of the respective unit of the business group that will exercise the risk-management function must be considered, in relation to compliance with the requirements established in this regulation and any conflicts of interest that may arise and, if applicable, their mitigation and/or elimination. For all purposes, if the function is exercised by a corporate risk-management unit in the case where the entity belongs to a business group, it shall be considered as carried out by an internal unit.

Without prejudice to the foregoing, the entity shall always be responsible for the risk-management function even when it is carried out by a body belonging to the business group, and must review and approve the reports produced in that regard, for which it must retain all relevant documentation.

The risk-management framework must have as its purpose the effective management of the risks that arise in the development of its business, such as, for example, general business risk, operational risk, and reputational risk, among others. The risk-management policies, procedures, and systems must also safeguard compliance with the requirements established in the applicable laws and regulations.

For the development of its activities, compliance must be given, at a minimum, to the following principles and elements:

a) The risk-management function must be independent of the risk-generating areas and of the internal-audit function, with a direct responsibility line to the board of directors or equivalent body.

b) The personnel responsible must have verifiable experience and knowledge of commonly accepted standards or best practices for risk management and of the specific risks it must manage in accordance with the risk-management framework.

c) The risk-management function must propose risk-management policies and procedures to the board of directors or equivalent body, consistent with the mission, vision, strategic objectives, and the responsibilities assigned to it by the regulatory framework.

d) The risk-management function must have methodologies and tools to quantify, aggregate, and manage the risks faced by the entity, which must be evaluated at least annually and prospectively, including scenarios such as changes in economic conditions and crisis situations. In addition, it must have methodologies and tools that enable it to verify compliance with the policies, procedures, and control mechanisms.

e) The nature, scope, and timing of the activities that the risk-management function will carry out must be contained in an annual plan, which must be approved by the board of directors or equivalent body. In any event, that plan must be updated whenever significant changes occur, such as changes in economic environment and market conditions in which the entity operates, the introduction of new products or services, or changes in the regulation applicable to the entity.

The risk-management function must promote a responsible organisational culture in the area of risk management, which includes periodic awareness, sensitisation, and training programmes that contribute to ensuring that the entity's personnel, including the board of directors or equivalent body and external personnel performing critical functions for the organisation, understand the risks relevant to their functions and their contribution to the effectiveness of the management of those risks.

### Original Spanish

> "C.4.1. DISPOSICIONES GENERALES
>
> La instancia encargada de la función de gestión de riesgos tiene por objeto que las actividades del proceso de gestión de riesgos sean desarrolladas adecuadamente en la entidad (marco de gestión de riesgo), conforme a las políticas y procedimientos establecidos para dicho efecto.
>
> La función de gestión de riesgos podrá ser realizada por una persona o unidad interna, de acuerdo con la Sección C.6 siguiente. Dicha función, para el caso de los Bloques 2 y 3, deberá ser independiente de las áreas operativas y de negocios de la entidad y de la instancia encargada de la función de auditoría interna, con reporte directo al directorio u órgano equivalente.
>
> En el caso que la entidad pertenezca a un grupo empresarial, la función de gestión de riesgos de la entidad podrá ser ejercida por la unidad de riesgos corporativa, en la medida que ésta tenga un conocimiento acabado del marco de gestión de riesgos y ambiente de control de la entidad y que cumpla con los requisitos establecidos en la presente normativa, lo cual deberá ser acordado por el directorio u órgano equivalente. Se deberá considerar la pertinencia respecto a la idoneidad de la unidad respectiva del grupo empresarial que ejercerá la función de riesgos, en relación con el cumplimiento de los requisitos establecidos en esta norma y los conflictos de intereses que pudieran generarse y, de ser el caso, su mitigación y/o eliminación. Para todos los efectos, si la función es ejercida por una unidad de gestión de riesgos corporativa, en el caso de que la entidad pertenezca a un grupo empresarial se considerará realizada por una unidad interna.
>
> Sin perjuicio de lo anterior, la entidad será siempre responsable de la función de gestión de riesgos aun cuando ésta sea realizada por una instancia perteneciente al grupo empresarial, debiendo revisar y aprobar los informes realizados al respecto, para lo cual deberá hacerse de toda la documentación relevante.
>
> El marco de gestión de riesgos deberá tener como propósito gestionar eficazmente los riesgos que se presentan en el desarrollo de su negocio, como por ejemplo el riesgo general del negocio, riesgo operacional y riesgo reputacional, entre otros. Las políticas, procedimientos y sistemas de gestión de riesgos deberán cautelar además el cumplimiento de los requisitos establecidos en las leyes y la normativa aplicable.
>
> Para el desarrollo de sus actividades, se deberá dar cumplimiento, al menos, a los principios y elementos que se señalan a continuación:
>
> a) La función de gestión de riesgos deberá ser independiente de las áreas generadoras de riesgos y de la función de auditoría interna, con línea de responsabilidad directa al directorio u órgano equivalente.
>
> b) El personal encargado deberá contar con experiencia y conocimientos comprobables en estándares o mejores prácticas de común aceptación para la gestión de riesgos y de los riesgos específicos que debe gestionar de acuerdo con el marco de gestión de riesgos.
>
> c) La función de gestión de riesgos deberá proponer políticas y procedimientos para la gestión de riesgos al directorio u órgano equivalente, consistentes con la misión, visión, objetivos estratégicos y las responsabilidades que el marco regulatorio le asigna.
>
> d) La función de gestión de riesgos deberá contar con metodologías y herramientas para cuantificar, agregar y gestionar los riesgos que enfrenta la entidad, los cuales deberán evaluarse al menos anualmente y en forma prospectiva, incluyendo escenarios tales como cambios en las condiciones de la economía y situaciones de crisis. Además, deberá contar con metodologías y herramientas que le permita verificar el cumplimiento de las políticas, procedimientos y mecanismos de control.
>
> e) La naturaleza, el alcance y oportunidad de las actividades que la función de gestión de riesgos desarrollará deberá estar contenido en un plan anual, el que deberá ser aprobado por el directorio u órgano equivalente. En todo caso, dicho plan deberá ser actualizado cada vez que se produzcan cambios significativos tales como cambios en condiciones del entorno económico y mercados en que opera la entidad, introducción de nuevos productos o servicios, o cambios en la regulación aplicable a la entidad.
>
> La función de gestión de riesgos deberá promover una cultura organizacional responsable en el ámbito de gestión de riesgo, que comprenda programas periódicos de difusión, concientización y capacitación, que contribuyan a que el personal de la entidad, incluyendo directorio u órgano equivalente y personal externo que realice funciones críticas para la organización, comprenda los riesgos atingentes a sus funciones, y cuál es su contribución a la efectividad de la gestión de dichos riesgos."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.4.2 — risk-management process the function must carry out.
- NCG 502 §IV.C.6 — proportionality provisions governing how the function may be exercised.
- NCG 502 §IV.C.5 — internal-audit function whose independence from the risk-management function is required.

> **Source:** NCG 502 §IV.C.4.1 (12-ene-2024), as amended by NCG 524 item 39 (02-dic-2024).

---

## IV.C.4.2 — Risk-Management Process
**NCG anchor:** N° 502, Sección IV, C.4.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, risk-management-process, crowdfunding, alternative-trading

### Plain-English text

The risk-management process will consider the following principal activities:

a) Identification of the processes into which the activities carried out by the entity are broken down, and the respective persons responsible for those processes (process map).

The risk-management function, together with those in charge of the principal processes, must formally identify the risks inherent in those to which the entity is exposed in the development of its activities.

b) Measurement of the inherent risks identified in the activities carried out by the entity. For this purpose, a risk matrix must be prepared that enables a probability of occurrence and impact of the risks to be estimated, as well as rating their severity considering these factors.

c) Definition of the control mechanisms to mitigate the inherent risks identified. In this regard, such control mechanisms must consider:

1) Description of each control and its objective.

2) Identification of those responsible for the control formally designated for these purposes.

3) Rating of the effectiveness of the controls for the mitigation of the inherent risks, by a body independent of those responsible for them.

d) Quantification of the residual risks, which will be determined on the basis of the inherent risks considering the rating of the effectiveness of the controls.

e) Definition of the treatment of the residual risks, for which purpose the risk-appetite levels must be taken into account.

f) Procedure for monitoring the risks and controls established, considering at least:

1) Definition and measurement of key risk-evaluation indicators.

2) Continuous risk-monitoring procedures that enable a possible materialisation of risks above the defined risk-appetite levels to be identified in a timely manner. For this purpose, the entity must implement an alert mechanism based on the key risk indicators.

3) Timely communication of the deficiencies of the controls and the deviation of the residual risk with respect to the defined risk-appetite levels to those responsible for applying the corrective measures, including the committees referred to in this regulation and the board of directors or equivalent body in the case of significant deficiencies.

4) Continuous follow-up of the corrective measures that have been defined for the deficiencies identified in the risk-monitoring process, so that these are effectively implemented within the established periods.

g) Information and communication procedures for risk management that ensure that relevant information about the effectiveness of the mitigating controls and compliance with the risk-appetite levels reaches the board of directors or equivalent body and all interested parties.

h) A continuous risk-management improvement programme, with the aim of evaluating the need to make changes in response to new economic and financial scenarios facing the entity, changes in the risk profile, and as a result of the implementation or changes in international standards or best practices.

### Original Spanish

> "C.4.2. PROCESO DE GESTIÓN DE RIESGOS
>
> El proceso de gestión de riesgos considerará las siguientes actividades principales:
>
> a) Identificación de procesos en los que se descomponen las actividades efectuadas por la entidad, y los respectivos responsables de dichos procesos (mapa de procesos).
>
> La función de gestión de riesgos, en conjunto con los encargados de los procesos principales, deberá identificar formalmente los riesgos inherentes a los que se expone la entidad en el desarrollo de sus actividades.
>
> b) Medición de los riesgos inherentes identificados en las actividades efectuadas por la entidad. Para ello deberá elaborarse una matriz de riesgo que permita estimar una probabilidad de ocurrencia e impacto de los riesgos, como también calificar su severidad considerando estos factores.
>
> c) Definición de los mecanismos de control para mitigar los riesgos inherentes identificados. Al respecto, dichos mecanismos de control deberán considerar:
>
> 1) Descripción de cada control y su objetivo.
>
> 2) Identificación de los responsables del control formalmente designados para esos efectos.
>
> 3) Calificación de la efectividad de los controles para la mitigación de los riesgos inherentes, por una instancia independiente del responsable de estos.
>
> d) Cuantificación de los riesgos residuales, los que serán determinados a partir de los riesgos inherentes considerando la calificación de la efectividad de los controles.
>
> e) Definición del tratamiento de los riesgos residuales, para lo cual se deberá tener en consideración los niveles de apetito por riesgo.
>
> f) Procedimiento de monitoreo de los riesgos y controles establecidos, considerando al menos:
>
> 1) Definición y medición de indicadores clave de evaluación de riesgos.
>
> 2) Procedimientos de monitoreo continuo de riesgos que permitan identificar oportunamente una posible materialización de riesgos por encima de los niveles de apetito por riesgo definidos. Para ello, la entidad deberá implementar un mecanismo de alertas basado en los indicadores clave de riesgos.
>
> 3) Comunicación oportuna de las deficiencias de los controles y la desviación del riesgo residual respecto a los niveles de apetito por riesgo definidos a los responsables de aplicar las medidas correctivas, incluyendo los comités a los que se refiere esta normativa y al directorio u órgano equivalente en el caso de deficiencias significativas.
>
> 4) Seguimiento continuo de las medidas correctivas que se hubieren definido para las deficiencias identificadas en el proceso de monitoreo de riesgos, para que éstas sean efectivamente implementadas en los plazos establecidos.
>
> g) Procedimientos de información y comunicación de la gestión de riesgos que asegure que la información relevante acerca de la efectividad de los controles mitigantes y el cumplimiento de los niveles de apetito por riesgo llegue al directorio u órgano equivalente y a todas las partes interesadas.
>
> h) Programa de mejoramiento continuo de la gestión de riesgos, con el objeto de evaluar la necesidad de realizar cambios frente a nuevos escenarios económicos y financieros que vaya enfrentando la entidad, cambios del perfil de riesgo y producto de la implementación o cambios en los estándares o mejores prácticas internacionales."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.4.1 — general provisions on the risk-management function carrying out this process.

> **Source:** NCG 502 §IV.C.4.2 (12-ene-2024).

---

## IV.C.5 — Internal-Audit Function
**NCG anchor:** N° 502, Sección IV, C.5
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, internal-audit, internal-audit-function, crowdfunding, alternative-trading

### Plain-English text

The body responsible for the internal-audit function has the purpose of verifying the correct functioning of the risk-management system and its consistency with the objectives and policies of the organisation, as well as compliance with the legal and regulatory provisions applicable to the entity.

The internal-audit function may be carried out by a natural person or internal unit or outsourced to a third party, in accordance with Section C.6 below.

Where the entity belongs to a business group, the internal-audit function may be exercised by the corporate internal-audit unit, to the extent that it has thorough knowledge of the entity's risk-management framework and control environment and complies with the requirements established in this regulation, which must be agreed by the board of directors or equivalent body. The appropriateness of the respective unit of the business group that will carry out the activity must be considered, in relation to compliance with the requirements established in this regulation and any conflicts of interest that may arise and, if applicable, their mitigation and/or elimination. For all purposes, if the internal-audit function is exercised by a corporate unit of the business group to which the entity belongs, it shall be understood that it is exercised by an internal unit.

Without prejudice to the foregoing, the entity shall always be responsible even when it is carried out by a body belonging to the business group, and must review and approve the reports produced in that regard, for which it must retain all relevant documentation.

For the development of its activities, compliance must be given, at a minimum, to the following principles and elements:

a) The internal-audit function must be independent of the risk-generating areas and of the risk-management function, with a direct responsibility line to the board of directors or equivalent body.

b) The personnel responsible must have verifiable experience and knowledge of risk-management frameworks specific to the functions that it must audit.

c) The internal audit must be developed on the basis of a methodology that considers at least the following aspects:

1) The nature, scope, and timing of the audits.

2) Audit work programmes.

3) The categories used to rate the observations detected.

4) The follow-up to be conducted on the observations detected.

5) How significant deficiencies will be reported to the board of directors.

6) The preparation and structure of the reports produced by the internal-audit function.

d) The existence and execution of an annual audit plan that includes the nature, scope, and timing of the activities to be developed by the internal-audit function, and that considers:

1) That the most relevant areas, processes, business lines, or risks are audited periodically, including the risk-management function.

2) Follow-up on compliance with the commitments made by the audited areas in previous reviews.

e) The internal-audit function must issue a semi-annual report to the board of directors or equivalent body that considers:

1) In respect of the areas, processes, business lines, or risks audited during the period:

i) The quality and effectiveness of the policies, procedures, and control mechanisms.

ii) The result of the audits carried out with their respective rating.

iii) The actions or measures proposed to address the observations raised and the estimated timeframe for their implementation.

iv) The date of the last audit carried out for each auditable unit.

2) In respect of the risk-management function:

i) The effectiveness of the risk-management system.

ii) Non-compliance with risk-management policies and procedures detected in the audits, the causes that gave rise to them, and the corrective actions adopted to prevent their recurrence.

3) The result of the follow-up on the correction of the situations identified in the audits carried out.

The report must be submitted to the board of directors or equivalent body within no more than 30 calendar days after the end of the period to which it refers. The foregoing is without prejudice to the monthly information that the internal-audit function may provide to the board of directors or equivalent body, so as to keep it informed of the work of this function.

### Original Spanish

> "C.5. FUNCIÓN DE AUDITORÍA INTERNA
>
> La instancia encargada de la función de auditoría interna tiene por objeto verificar el correcto funcionamiento del sistema de gestión de riesgos y su consistencia con los objetivos y políticas de la organización, como también del cumplimiento de las disposiciones legales y normativas que le son aplicables a la entidad.
>
> La función de auditoría interna podrá ser realizada por una persona o unidad interna o externalizada a un tercero, de acuerdo con la Sección C.6 siguiente.
>
> En el caso que la entidad pertenezca a un grupo empresarial, la función de auditoría interna podrá ser ejercida por la unidad de auditoría interna corporativa, en la medida que ésta tenga un conocimiento acabado del marco de gestión de riesgos y ambiente de control de la entidad y que cumpla con los requisitos establecidos en la presente normativa, lo cual deberá ser acordado por el directorio u órgano equivalente. Se deberá considerar la pertinencia respecto a la idoneidad de la unidad respectiva del grupo empresarial que se encargará de la actividad, en relación con el cumplimiento de los requisitos establecidos en esta norma y los conflictos de intereses que pudieran generarse y, de ser el caso, su mitigación y/o eliminación. Para todos los efectos, si la función de auditoría interna es ejercida por una unidad corporativa del grupo empresarial al que pertenece la empresa, se entenderá que es ejercida por una unidad interna.
>
> Sin perjuicio de lo anterior, la entidad será siempre responsable aun cuando ésta sea realizada por una instancia perteneciente al grupo empresarial, debiendo revisar y aprobar los informes realizados al respecto, para lo cual deberá hacerse de toda la documentación relevante.
>
> Para el desarrollo de sus actividades, se deberá dar cumplimiento, al menos, a los principios y elementos que se señalan a continuación:
>
> a) La función de auditoría interna deberá ser independiente de las áreas generadoras de riesgos y de la función de gestión de riesgos, con línea de responsabilidad directa al directorio u órgano equivalente.
>
> b) El personal encargado deberá tener experiencia y conocimientos comprobables en marcos de gestión de los riesgos específicos que deberá auditar.
>
> c) La auditoría interna deberá ser desarrollada sobre la base de una metodología que considere al menos los siguientes aspectos:
>
> 1) La naturaleza, alcance y oportunidad de las auditorías.
>
> 2) Programas de trabajo de auditoría.
>
> 3) Las categorías utilizadas para calificar las observaciones detectadas.
>
> 4) El seguimiento que se efectuará a las observaciones detectadas.
>
> 5) La forma en que se reportarán las deficiencias significativas al directorio.
>
> 6) La elaboración y estructura de los informes que la función de auditoría interna realice.
>
> d) La existencia y ejecución de un plan anual de auditoría que incluya la naturaleza, alcance y oportunidad de las actividades que la función de auditoría interna desarrollará, y considerar:
>
> 1) Que las áreas, procesos, líneas de negocio o riesgos más relevantes sean auditados periódicamente, incluyendo la función de gestión de riesgos.
>
> 2) El seguimiento al cumplimiento de los compromisos adquiridos por las áreas auditadas en revisiones anteriores.
>
> e) La función de auditoría interna deberá emitir un informe semestral al directorio u órgano equivalente que considere:
>
> 1) Respecto de las áreas, procesos, líneas de negocio o riesgos auditados durante el periodo:
>
> i) La calidad y efectividad de las políticas, procedimientos y mecanismos de control.
>
> ii) El resultado de las auditorías efectuadas con su respectiva calificación.
>
> iii) Las acciones o medidas propuestas para subsanar las observaciones levantadas y el plazo estimado para su implementación.
>
> iv) Fecha de la última auditoría realizada a cada unidad auditable.
>
> 2) Respecto de la función de gestión de riesgos:
>
> i) La efectividad del sistema de gestión de riesgos.
>
> ii) Los incumplimientos de políticas y procedimientos de gestión de riesgos detectados en las auditorías, las causas que los originaron y las acciones correctivas adoptadas para evitar su reiteración.
>
> 3) El resultado del seguimiento de la corrección de las situaciones detectadas en las auditorías realizadas.
>
> El informe deberá ser remitido al directorio u órgano equivalente en un plazo no superior a 30 días corridos de finalizado el periodo al cual se refiere. Lo anterior, sin perjuicio de la información mensual que la función de auditoría interna le pueda proporcionar al directorio u órgano equivalente, de forma de mantenerlo informado de la labor de esta función."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.C.4.1 — risk-management function whose independence from the internal-audit function is required.
- NCG 502 §IV.C.6 — proportionality provisions governing how the function may be exercised, including outsourcing to a third party.

> **Source:** NCG 502 §IV.C.5 (12-ene-2024).

---

## IV.C.6 — Proportionality
**NCG anchor:** N° 502, Sección IV, C.6
**Implements:** Ley 21.521 Arts. 1 and 12 (proportionality; governance & risk management)
**Tags:** governance, risk-management, proportionality, crowdfunding, alternative-trading

### Plain-English text

In accordance with the provisions of Articles 1 and 12 of Ley N° 21.521, in addition to the proportionality considerations based on the size, volume, and nature of the entity's businesses and risks in Section IV.C, the following blocks will be defined, according to the following classification:

1) **Block 1**: entities that do not meet any of the business-volume metrics of Block 2 or 3 entities. Active clients shall be considered to be those that meet the conditions defined in Annex N° 1 of this regulation.

2) **Block 2**: entities that meet any of the following conditions:

i) Have a number of active clients in Chile, for the crowdfunding platform service or alternative trading system service as applicable, between 500 and 5,000.

ii) Average daily transactions carried out in Chile in the last 12 months between UF 100,000 and UF 500,000 in the case of alternative trading systems, or amounts financed through the crowdfunding platform in the last 12 months of between UF 300,000 and UF 1,000,000 monthly average.

iii) Income from the crowdfunding platform service or alternative trading system service in Chile, as applicable, in the last 12 months between UF 25,000 and UF 50,000.

3) **Block 3**: entities that meet any of the following conditions:

i) More than 5,000 active clients in Chile for the crowdfunding platform service or alternative trading system service, as applicable.

ii) More than UF 500,000 in average daily transactions carried out in Chile in the last 12 months in the case of alternative trading systems, or amounts financed through the crowdfunding platform in the last 12 months over UF 1,000,000 monthly average.

iii) Income in the last 12 months over UF 50,000, from the crowdfunding platform service or alternative trading system service in Chile, as applicable.

When an entity meets one of the conditions that classifies it in a different block for more than 6 months, it must notify this fact to the Commission within the 5 business days following the occurrence of the event and shall have a maximum period of 9 months to comply with the corporate-governance and comprehensive risk-management requirements corresponding to that block. Entities may be reclassified to lower blocks after ceasing to meet the respective conditions of the higher block for a minimum of 6 months and with the authorisation of the Commission.

Entities that classify within Block 3 may not outsource the internal-audit function.

Entities that classify within Blocks 1 or 2 may develop the internal-audit function through a natural person or internal unit or through an external third party, always ensuring compliance with segregation from, and independence of, the risk-management function.

In the event that the internal-audit function is carried out by an external third party, in no case may that third party exercise the external audit function for the entity, and the entity must ensure the adequate segregation of both functions.

Entities that classify within Block 3 must develop the internal-audit function through a natural person or internal unit, always ensuring compliance with segregation from, and independence of, the risk-management function.

**Table 3. Proportionality for the provision of the alternative trading system or crowdfunding platform services**

| Block | Policies | Risk-management function | Internal-audit function |
|---|---|---|---|
| 1 | MIF, CI, OP, PLAFT, II, RO | Natural person or internal unit | Natural person or internal unit or carried out by a third party |
| 2 | MIF, CI, OP, PLAFT, II, RO | Natural person or internal unit | Natural person or internal unit or carried out by a third party |
| 3 | MIF, CI, OP, PLAFT, II, RLN, GCR, RO | Natural person or internal unit | Natural person or internal unit |

Where:

- MIF: Maintenance of financial instruments in alternative trading systems, or dissemination of investment projects or financing needs on crowdfunding platforms.
- CI: Conflicts of interest.
- OP: Offer of products consistent with the investor's needs, expectations, and risk tolerance.
- PLAFT: Prevention of money laundering and financing of terrorism.
- II: Information to the investor.
- RLN: Compliance with legal and regulatory operating requirements.
- GCR: Management of queries, complaints, and claims.
- RO: Operational risk defined in section IV.C.3.

### Original Spanish

> "C.6. PROPORCIONALIDAD
>
> De acuerdo con lo establecido en los artículos 1 y 12 de la ley N°21.521, además de las consideraciones de proporcionalidad, conforme al tamaño, volumen y naturaleza de los negocios y riesgos de la entidad en la Sección IV.C, se definirán los siguientes bloques, de acuerdo con la siguiente clasificación:
>
> 1) Bloque 1: entidades que no cumplan ninguna de las métricas de volumen de negocio de las entidades de los Bloques 2 o 3. Se considerarán clientes activos aquellos que cumplan con las condiciones definidas en el Anexo N°1 de esta normativa.
>
> 2) Bloque 2: entidades que cumplan alguna de las siguientes condiciones:
>
> i) Tengan un número de clientes activos en Chile por el servicio de plataforma de financiamiento colectivo o sistema alternativo de transacción, según corresponda, entre 500 y 5.000.
>
> ii) Transacciones promedio diarias efectuadas en Chile en los últimos 12 meses entre UF 100.000 y UF 500.000 en caso de sistemas alternativos de transacción, o montos financiados a través de la plataforma de financiamiento colectivo en los últimos 12 meses de entre UF 300.000 y UF 1.000.000 promedio mensual.
>
> iii) Ingresos por el servicio de plataforma de financiamiento colectivo o sistema alternativo de transacción en Chile, según corresponda, en los últimos 12 meses entre UF 25.000 y UF 50.000.
>
> 3) Bloque 3: entidades que cumplan alguna de las siguientes condiciones:
>
> i) Más de 5.000 clientes activos en Chile por el servicio de plataforma de financiamiento colectivo o sistema alternativo de transacción, según corresponda.
>
> ii) Más de UF 500.000 en transacciones promedio diarias efectuadas en Chile en los últimos 12 meses en caso de sistemas alternativos de transacción, o montos financiados a través de la plataforma de financiamiento colectivo en los últimos 12 meses superiores a las UF 1.000.000 promedio mensual.
>
> iii) Ingresos en los últimos 12 meses sobre UF 50.000, por el servicio de plataforma de financiamiento colectivo o sistema alternativo de transacción en Chile, según corresponda.
>
> Cuando una entidad alcance una de las condiciones que lo clasifique en un bloque diferente por más de 6 meses, deberá avisar este hecho a la Comisión dentro de los 5 días hábiles siguientes de ocurrido el hecho y dispondrá de un plazo máximo de 9 meses para dar cumplimiento a los requisitos de gobierno corporativo y gestión integral de riesgos correspondientes a dicho bloque. Las entidades podrán ser reclasificadas a bloques inferiores después de dejar de cumplir las condiciones respectivas al bloque superior por un mínimo de 6 meses y con autorización de la Comisión.
>
> Las entidades que clasifiquen dentro del Bloque 3 no podrán externalizar la función de auditoría interna.
>
> Las entidades que clasifiquen dentro de los Bloques 1 o 2 podrán desarrollar la función de auditoría interna por una persona o unidad interna o por un tercero externo, velando siempre por el cumplimiento de la segregación e independencia con la función de gestión de riesgos.
>
> En caso de que la función de auditoría interna sea realizada por un tercero externo, en ningún caso dicho tercero podrá ejercer la función de auditoría externa en la entidad, debiendo la entidad velar por la adecuada segregación de ambas funciones.
>
> Las entidades que clasifiquen dentro del Bloque 3 deberán desarrollar la función de auditoría interna por una persona o unidad interna, velando siempre por el cumplimiento de la segregación e independencia con la función de gestión de riesgos.
>
> Tabla 3. Proporcionalidad para la prestación de los servicios de sistema alternativo de transacción o plataforma de financiamiento colectivo
>
> Bloque Políticas Función de gestión de riesgos Función de auditoría interna 1 MIF, CI, OP, PLAFT, II, RO Persona o unidad interna Persona o unidad interna o ser realizadas por un tercero 2 MIF, CI, OP, PLAFT, II, RO Persona o unidad interna o ser realizadas por un tercero 3 MIF, CI, OP, PLAFT, II, RLN, GCR, RO Persona o unidad interna
>
> Donde,
>
> - MIF: Mantención de instrumentos financieros en sistemas alternativos de transacción, o difusión de proyectos de inversión o necesidades de financiamiento en plataformas de financiamiento colectivo.
>
> - CI: Conflictos de intereses.
>
> - OP: Oferta de productos acorde a las necesidades, expectativas y disposición al riesgo del inversionista.
>
> - PLAFT: Prevención del lavado de activos y financiamiento del terrorismo.
>
> - II: Información al inversionista.
>
> - RLN: Cumplimiento de requisitos legales y normativos de funcionamiento.
>
> - GCR: Gestión de consultas, reclamos y denuncias.
>
> - RO: Riesgo operacional definido en la sección IV.C.3."

> **TN:** Table 3 is a structured table in the PDF source. The English rendering above presents it as a Markdown table with equivalent informational content (the "Risk-management function" column is merged across all three blocks in the PDF — "Persona o unidad interna" — and the "Internal-audit function" column is merged across Blocks 1 and 2). The Original Spanish blockquote reproduces the PDF's column-first extraction sequence for the table chunk.

> **TN:** NCG 524 item 40 replaced the first three paragraphs of this section (the block-classification chapeau and the Block 1/2/3 definitions and reclassification rule), while the proportionality Table 3 and its key remain from the NCG 502 baseline. The consolidated Spanish is therefore faithful (the replaced paragraphs verified against the NCG 524 source PDF, coverage 0.97; the table and key verified against the NCG 502 source PDF) but is not contiguous in either single source PDF — best single-PDF coverage of the combined block is 0.59.

### Cross-references
- Ley 21.521 Arts. 1 and 12 — proportionality and governance mandate this section implements.
- NCG 502 Annex N° 1 — conditions defining "active clients" referenced in the Block 1 definition.
- NCG 502 §IV.C.2.2 — policies (MIF, CI, OP, PLAFT, II, RLN, GCR) referenced in the table key.
- NCG 502 §IV.C.3 — operational risk (RO) referenced in the table key.
- NCG 502 §IV.C.4 and §IV.C.5 — risk-management and internal-audit functions subject to the block thresholds.

> **Source:** NCG 502 §IV.C.6 (12-ene-2024), as amended by NCG 524 item 40 (02-dic-2024).

---

## IV.C.7 — Reporting of Operational Incidents
**NCG anchor:** N° 502, Sección IV, C.7
**Implements:** Ley 21.521 Art. 8 (governance & risk management; operational incident reporting)
**Tags:** governance, risk-management, operational-incidents, crowdfunding, alternative-trading

### Plain-English text

This subsection establishes the obligations relating to the recording and communication of operational incidents (C.7.1) and operational losses (C.7.2).

### Original Spanish

> "C.7. INFORMACIÓN DE INCIDENTES OPERACIONALES"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate; operational incident reporting is part of the entity's risk-management obligations.
- NCG 502 §IV.C.7.1 — recording and communication of operational incidents.
- NCG 502 §IV.C.7.2 — recording and communication of operational losses.
- NCG 502 Annex N° 2 — Operational Incident Report (RIO) form.
- NCG 502 Annex N° 3 — operational-loss reporting instructions.

> **Source:** NCG 502 §IV.C.7 (12-ene-2024).

---

## IV.C.7.1 — Recording and Communication of Operational Incidents
**NCG anchor:** N° 502, Sección IV, C.7.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management; operational incident reporting)
**Tags:** governance, risk-management, operational-incidents, information-security, crowdfunding, alternative-trading

### Plain-English text

a) Crowdfunding platforms and alternative trading systems belonging to Block 3 must communicate to this Commission the operational incidents that affect the continuity of the business, the resources and information of the entity or its clients, and the quality of the services. By way of example, and without being exhaustive or limiting, the following must be reported: failures in services important for business operations; technological problems affecting information security; cyberspace attacks; viruses or malware detected in critical information assets; events of unavailability or interruption of any service or product affecting clients, on any channel; losses or leakage of information of the entity or of clients; incidents affecting the entity's assets resulting from internal or external fraud; problems affecting the continuity of critical service suppliers; among others. This information must be maintained by the entity in an incident database and another operational-loss database for the continuous improvement of the operational risk-management process.

b) The occurrence of an operational incident of those mentioned in the preceding numeral must be reported to this Commission within a maximum period of 2 hours elapsed from the time the entity became aware of the event. The period indicated is solely for the purpose of notifying the Commission of the occurrence of the incident with the information available at that time and does not imply that the entity must have resolved the problem, taken specific actions, or clarified the causes of the incident, which may be the subject of follow-up reports on the incident sent to the CMF subsequently. The instructions for reporting operational incidents to this Commission are found in Annex N° 2 of this regulation.

c) For these purposes, the board of directors or equivalent body must designate an officer in charge and an alternate for the preparation of reports and the sending of information in accordance with what is indicated in this section. Both persons must have an executive level and be designated by the entity, both for this purpose and to respond to any queries on the part of this Commission.

d) Likewise, in cases where this Commission considers it necessary, it may require the entity to prepare an internal report containing at least: the analysis of the causes of the incident; the generation of documentation and investigation reports; an analysis of the impact generated on the services; the procedure to prevent, with a high degree of certainty, its recurrence; and the additional matters that this Commission may require.

e) Without prejudice to the foregoing, the entity must keep the board of directors or equivalent body informed in a timely manner about the updates of all relevant operational incidents and the measures adopted to resolve them.

### Original Spanish

> "C.7.1. REGISTRO Y COMUNICACIÓN DE INCIDENTES OPERACIONALES
>
> a) Las plataformas de financiamiento colectivo y los sistemas alternativos de transacción, pertenecientes al Bloque 3, deberán comunicar a esta Comisión los incidentes operacionales que afecten la continuidad del negocio, los recursos e información de la entidad o de sus clientes y la calidad de los servicios. A modo de ejemplo, y sin el objeto de ser exhaustivos ni taxativos, deberán ser reportadas las fallas en servicios importantes para las operaciones del negocio; problemas tecnológicos que afecten la seguridad de la información; ataques del ciberespacio; virus o malware detectados en los activos de información críticos; eventos de indisponibilidad o interrupción de algún servicio o producto que afecte a los clientes, en cualquier canal; pérdidas o fugas de información de la entidad o de clientes; los incidentes que afecten el patrimonio de la entidad producto de fraudes internos o externos; problemas que afecten la continuidad de proveedores de servicios críticos; entre otros. Esta información deberá ser mantenida por la entidad en una base de datos de incidentes y otra base de datos de pérdidas operacionales para el mejoramiento continuo del proceso de gestión de riesgo operacional.
>
> b) La ocurrencia de un incidente operacional de aquéllos mencionados en el numeral anterior deberá ser informada a esta Comisión en un plazo máximo de 2 horas transcurridas desde que la entidad tomó conocimiento del hecho. El plazo señalado es solo para efectos de notificar a la Comisión de la ocurrencia del incidente con la información disponible en ese momento y no implica que la entidad deba tener resuelto el problema, haber tomado determinadas acciones o tener aclarada las causas del incidente, lo que podría ser materia de reportes de seguimiento del incidente enviados la CMF, posteriormente. Las instrucciones para reportar los incidentes operacionales a esta Comisión se encuentran en el Anexo N° 2 de esta normativa.
>
> c) Para estos efectos, el directorio u órgano equivalente deberá definir un funcionario encargado y un suplente para la realización de reportes y envío de información según lo indicado en esta sección. Ambas personas deberán tener un nivel ejecutivo y ser designados por la entidad, tanto para este efecto como para responder eventuales consultas por parte de esta Comisión.
>
> d) Asimismo, en los casos en que esta Comisión lo estime necesario, podrá requerir a la entidad la elaboración de un informe interno que contenga al menos: el análisis de las causas del incidente; la generación de documentación e informes de investigación; un análisis del impacto generado en los servicios; y el procedimiento para evitar con alto grado de seguridad que se vuelva a presentar; y las materias adicionales que esta Comisión pueda requerir.
>
> e) Sin perjuicio de lo anterior, la entidad deberá mantener informado en forma oportuna al directorio u órgano equivalente sobre las actualizaciones de todos los incidentes operacionales relevantes y las medidas adoptadas para resolverlo."

> **TN:** As amended by NCG 524 item 41, the deadline now reads "2 horas transcurridas desde que la entidad tomó conocimiento del hecho" (the pre-amendment baseline truncated the clause at "la entidad tomó"). The 2-hour reporting obligation here is mandatory ("deberá ser informada"), unlike the optional RIO-format wording in §IV.B.5.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate; operational incident reporting is part of the entity's risk-management obligations.
- NCG 502 Annex N° 2 — instructions for reporting operational incidents (RIO) referenced in item b).
- NCG 502 §IV.C.6 — proportionality classification defining the Block 3 entities subject to this reporting obligation.
- NCG 502 §IV.C.3.1 — information-security and cybersecurity guidelines whose breach events are typical triggers for reporting.

> **Source:** NCG 502 §IV.C.7.1 (12-ene-2024), as amended by NCG 524 item 41 (02-dic-2024).

---

## IV.C.7.2 — Recording and Communication of Operational Losses
**NCG anchor:** N° 502, Sección IV, C.7.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management; operational loss reporting)
**Tags:** governance, risk-management, operational-losses, crowdfunding, alternative-trading

### Plain-English text

a) An operational loss is understood to be any financial loss resulting from the materialisation of operational risk in accordance with what was defined above. This includes financial losses due to legal or regulatory changes affecting the entity's operations, or resulting from non-compliance with current regulation.

b) The information on all incidents that materialise individually in operational losses greater than 150 Unidades de Fomento must be sent to this Commission in accordance with the instructions of Annex N° 3 of this regulation, 15 business days after the close of June and December of each year.

c) The criteria for the preparation of the operational-loss register are the following:

1) The entity must have documented processes and procedures for the identification, collection, use, and communication of the operational-loss records. This Commission may require that compliance with such requirements be validated through a pronouncement issued by external audit firms, among those registered in the Registry of External Audit Firms of this Commission, that have units specialised in the evaluation of operational risk-management procedures and mechanisms, with experience of no less than 5 years in those matters.

2) The entity's internal records on operational losses must be comprehensive and include all the relevant activities and exposures, in all systems and in all relevant geographic locations.

3) The entity must collect information on the gross amounts of the losses, and on the reference dates of the operational-risk events. In addition, the entity must collect information on recoveries of gross amounts of losses, and descriptive information on the determining factors or the causes of the loss event. The degree of detail of the descriptive information must be in proportion to the gross amount of the loss.

4) The entity must use the accounting date of the event to construct the set of loss records. In the case of legal events, the accounting date refers to when a provision for this legal contingency is constituted in the statement of financial position, with the corresponding reflection in the income statement.

5) Losses caused by a common operational-risk event or by several related operational-risk events over time, but recorded over the course of several years, must be assigned to the corresponding years in the loss database, consistent with their accounting treatment.

d) Gross loss is understood to be a loss before recoveries of any type.

1) The following items must be included in the calculations of the gross losses for the loss database:

i) Direct charges in the entity's Income Statement accounts and amortisations due to operational-risk events of the period. For example, costs incurred as a consequence of an event, including external expenses with a direct relationship to the operational-risk event (e.g., legal expenses directly related to the event and commissions paid to advisers, lawyers, or suppliers) and repair or replacement costs incurred to restore the position that prevailed before the operational-risk event.

ii) Direct charges in the entity's Income Statement accounts and amortisations due to operational-risk events of previous accounting periods that affect the entity's financial statements in the present period.

2) The following items must be excluded from the gross losses recorded in the loss database:

i) Costs for general maintenance contracts of property, plant, or equipment.

ii) Internal or external expenses with the aim of improving the business after the losses due to operational risk: updates, improvements, risk-management initiatives, and improvements thereto.

iii) Insurance premiums.

e) Net loss is understood to be the loss after taking into account the effects of recoveries. The recovery is an independent event, related to the initial loss event, that is not necessarily carried out in the same period in which the respective funds are received.

The entity must be able to identify recoveries not arising from insurance and recoveries originating from the payment of insurance indemnities for all operational-loss events. Likewise, it must use the net losses of recoveries (including those arising from insurance) in the set of operational-loss records, although recoveries may only be used to reduce the losses when the payment has been received.

Entities classified in Blocks 1 and 2 are exempt from the operational-loss report referred to in Annex N° 3 of this regulation.

### Original Spanish

> "C.7.2. REGISTRO Y COMUNICACIÓN DE PÉRDIDAS OPERACIONALES
>
> a) Se entiende por pérdida operacional toda pérdida financiera resultante de la materialización del riesgo operacional de acuerdo con lo definido anteriormente. Esto incluye las pérdidas financieras debido a cambios legales o regulatorios que afecten las operaciones de la entidad, o producto de incumplimientos con la regulación vigente.
>
> b) La información de todos los incidentes que se materialicen individualmente en pérdidas operacionales mayores a 150 Unidades de Fomento este deberá ser enviada a esta Comisión de acuerdo con las instrucciones del Anexo N° 3 de la presente norma, 15 días hábiles después del cierre de junio y diciembre de cada año.
>
> c) Los criterios para la confección del registro de pérdidas operacionales son los siguientes:
>
> 1) La entidad deberá contar con procesos y procedimientos documentados para la identificación, recopilación, uso y comunicación de los registros de pérdida operacional. Esta Comisión podrá exigir que el cumplimiento de tales requisitos sea validado a través de un pronunciamiento emitido por empresas de auditoría externa, de aquellos inscritos en el Registro de Empresas de Auditoría Externa de esta Comisión, que cuenten con unidades especializadas en la evaluación de procedimientos y mecanismos de gestión de riesgo operacional, con una experiencia no inferior a 5 años en dichas materias.
>
> 2) Los registros internos sobre pérdidas operacionales de la entidad deberán ser integrales e incluir la totalidad de las actividades y exposiciones relevantes, en todos los sistemas y en todas las ubicaciones geográficas pertinentes.
>
> 3) La entidad deberá recopilar información sobre los importes brutos de las pérdidas, y sobre las fechas de referencia de los eventos de riesgo operacional. Además, la entidad deberá recoger información sobre recuperaciones de importes brutos de pérdidas, e información descriptiva sobre los factores determinantes o las causas del evento de pérdida. El grado de detalle de la información descriptiva deberá estar en proporción al importe bruto de la pérdida.
>
> 4) La entidad deberá utilizar la fecha de contabilización del evento para construir el conjunto de registros sobre pérdidas. En el caso de eventos legales, la fecha de contabilización se refiere a cuando se constituye una provisión para esta contingencia legal en el estado de situación financiera, con su reflejo correspondiente en el estado de resultados.
>
> 5) Las pérdidas causadas por un evento de riesgo operacional común o por varios eventos de riesgo operacional relacionados a lo largo del tiempo, pero contabilizadas en el transcurso de varios años, deberán asignarse a los años correspondientes en la base de datos de pérdidas, en consonancia con su tratamiento contable.
>
> d) Por pérdida bruta se entiende una pérdida antes de recuperaciones de cualquier tipo.
>
> 1) Los siguientes ítems deben ser incluidos en los cálculos de las pérdidas brutas para la base de datos de pérdidas:
>
> i) Cargos directos en las cuentas de Estados de Resultados de la entidad y amortizaciones debido a eventos de riesgo operacional del período. Por ej. Costos incurridos como consecuencia de un evento, incluyendo gastos externos con una relación directa al evento por riesgo operacional (ej. Gastos legales directamente relacionados al evento y comisiones pagadas a los asesores, abogados o proveedores) y costos de reparación o reemplazo incurridos para restaurar la posición que prevalecía antes del evento de riesgo operacional.
>
> ii) Cargos directos en las cuentas de Estados de Resultados de la entidad y amortizaciones debido a eventos por riesgo operacional de ejercicios contables previos que afecten los estados financieros de la entidad en el presente período.
>
> 2) Los siguientes ítems deben ser excluidos de las pérdidas brutas registradas en la base de datos de pérdidas:
>
> i) Costos por contratos de mantenimientos generales de la propiedad, planta o equipos.
>
> ii) Gastos internos o externos con el fin de mejorar el negocio después de las pérdidas por riesgo operacional: actualizaciones, mejoras, iniciativas de gestión del riesgo y mejoras en ellas.
>
> iii) Primas de seguro.
>
> e) Por pérdida neta se entiende la pérdida después de tener en consideración los efectos de las recuperaciones. La recuperación es un hecho independiente, relacionado con el evento de pérdida inicial, que no necesariamente se efectúa en el mismo periodo en el que se perciben los fondos respectivos.
>
> La entidad deberá ser capaz de identificar las recuperaciones no procedentes de seguros y las recuperaciones originadas por el pago de indemnizaciones de seguros para todos los eventos de pérdidas operacionales. Asimismo, deberá utilizar las pérdidas netas de recuperaciones (incluidas las procedentes de seguros) en el conjunto de registros sobre pérdidas operacionales, aunque las recuperaciones sólo podrán utilizarse para reducir las pérdidas cuando se haya recibido el pago.
>
> Las entidades clasificadas en los Bloques 1 y 2 quedan eximidas del reporte de pérdidas operacionales al que se refiere el Anexo N°3 de la presente normativa."

> **TN:** Item b) contains "este deberá ser enviada" — a redundant/misplaced pronoun "este" in the source; rendered idiomatically as "must be sent" without replicating the pronoun. "Unidades de Fomento" (UF) is Chile's inflation-indexed accounting unit; retained as "Unidades de Fomento" / "UF" per source.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate; operational loss reporting is part of the entity's risk-management obligations.
- NCG 502 Annex N° 3 — instructions for reporting operational losses referenced in items b) and e).
- NCG 502 §IV.C.6 — proportionality classification exempting Blocks 1 and 2 from operational-loss reporting.
- NCG 502 §IV.C.7.1 — operational-incident reporting that feeds the incident and operational-loss databases.

> **Source:** NCG 502 §IV.C.7.2 (12-ene-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/seccion-04d-gobierno-enrutamiento.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/seccion-04d-gobierno-enrutamiento.md

# NCG 502 — Sección IV.D: Corporate Governance & Risk Management — Order Routing (Gobierno Corporativo y Gestión de Riesgos — Enrutamiento de Órdenes)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

---

## IV.D — Order Routing
**NCG anchor:** N° 502, Sección IV, D
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, order-routing

### Plain-English text

This subsection sets out the corporate-governance and risk-management obligations applicable to Financial-Service Providers (PSFs) that provide the order routing service.

### Original Spanish

> "D. ENRUTAMIENTO DE ÓRDENES"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this subsection implements.
- NCG 502 §IV — general proportionality framework applicable to all subsections of Section IV.

> **Source:** NCG 502 §IV.D (12-ene-2024).

---

## IV.D.1 — Responsibility of the Board of Directors or Equivalent Body
**NCG anchor:** N° 502, Sección IV, D.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, board, order-routing

### Plain-English text

The Board of Directors or Equivalent Body (Directorio u Órgano Equivalente) of the entity is the body responsible for approving and authorising risk-management and internal-control policies, at least once a year or with the frequency necessary in the event of significant changes to the established policies, leaving evidence thereof. For those purposes, the board of directors or equivalent body must comply with the risk-management principles and elements set out below:

a) Establish the mission, vision, and strategic objectives, taking into account the responsibilities that the applicable regulatory framework imposes on the entity.

b) Approve risk-management policies that are consistent with the strategic objectives and the regulatory framework.

c) Review the policies at least annually, and update them in the event of significant changes such as the introduction of new products or services, or changes in the regulation applicable to the entity.

d) Periodically evaluate the adequacy of the resources of the bodies responsible for risk management.

e) Establish an adequate organisational structure for the entity's risk management, taking into account the following:

1) The identification and management of all relevant risks arising from the development of its activities. In this regard, the organisational structure must be appropriate in relation to the volume of business; the number and type of clients of the entity; the complexity of its relationships with other entities, among other aspects.

2) The definition of roles, competencies, and responsibilities that enable the entity to carry out its activities and adequately manage the risks it faces. The foregoing involves the appropriate segregation of key duties and functions — especially those which, if performed by the same person, could give rise to errors that go undetected or that expose the entity or its participants to undue risks — and between risk-generating areas and the areas that control them.

3) The implementation of the risk-management function, in accordance with what is described in subparagraph D.3 of this Section.

f) Establish personnel-hiring policies that ensure the entity has staff with the appropriate experience to carry out their functions, and ensure that it has qualified human resources for risk management.

g) Implement remuneration and compensation policies for those who provide services to the entity, which must consider at least the manner or mechanism by which it will be prevented and verified that the remunerations and compensations do not give rise to or exacerbate conflicts of interest on the part of those who manage the resources of the entity itself and of those who advise or maintain commercial relationships with clients.

h) The board of directors or equivalent body must evaluate the appropriateness of forming a Risk Management Committee or a similar body that allows it to address and monitor relevant business matters, relating to matters such as conflicts of interest, information security, among others. The grounds considered by the board of directors or equivalent body for evaluating the formation of committees or similar bodies must be duly documented.

i) Ensure that the minutes or equivalent documentation reflect the principal matters addressed in the sessions of the board of directors or equivalent body and the committees, as well as the policies and procedures mentioned above. All material prepared or presented to the board of directors or equivalent body or the committees must be duly documented and archived in accordance with the applicable general regulations on the matter, and must be permanently available for examination at the request of this Commission (CMF).

### Original Spanish

> "D.1. RESPONSABILIDAD DEL DIRECTORIO U ÓRGANO EQUIVALENTE
>
> El Directorio u órgano equivalente de la entidad es la instancia responsable de aprobar y autorizar las políticas de gestión de riesgos y control interno, como mínimo una vez al año o con la frecuencia necesaria en caso de que se produzcan cambios significativos en las políticas establecidas, dejando evidencia de ello. Para esos efectos, el directorio u órgano equivalente deberá dar cumplimiento a los principios y elementos de gestión de riesgos que se señalan a continuación:
>
> a) Establecer la misión, visión y objetivos estratégicos, teniendo en consideración las responsabilidades que el marco regulatorio vigente establece para la entidad.
>
> b) Aprobar políticas de gestión de riesgos que sean coherentes con los objetivos estratégicos y el marco regulatorio.
>
> c) Revisar las políticas, al menos anualmente, y actualizarlas en caso de que se produzcan cambios significativos tales como introducción de nuevos productos o servicios, o cambios en la regulación aplicable a la entidad.
>
> d) Evaluar periódicamente la suficiencia de recursos de las instancias encargadas de la gestión de riesgos.
>
> e) Establecer una estructura organizacional adecuada para la gestión de riesgos de la entidad, que considere lo siguiente:
>
> 1) La identificación y gestión de todos los riesgos pertinentes derivados del desarrollo de sus actividades. En ese tenor, la estructura organizacional debe ser la adecuada en relación con el volumen de negocios; el número y tipo de clientes de la entidad; la complejidad de las relaciones con otras entidades, entre otros aspectos.
>
> 2) La definición de los roles, competencias y responsabilidades que permitan realizar sus actividades y gestionar adecuadamente los riesgos que enfrenta la entidad. Lo anterior involucra la segregación apropiada de los deberes y las funciones claves, especialmente aquéllas que, si fueran realizadas por una misma persona, puedan dar lugar a errores que no se detecten o que expongan a la entidad o sus participantes a riesgos indebidos; y entre las áreas generadoras de riesgo y de control de estos.
>
> 3) La implementación de la función de gestión de riesgos, de conformidad con lo descrito en el literal D.3. de esta Sección.
>
> f) Establecer políticas de contratación de empleados que aseguren que la entidad disponga de personal con la debida experiencia para desempeñar sus funciones, y velar porque se cuente con el recurso humano calificado para la gestión de riesgos.
>
> g) Implementar políticas de remuneración y compensación para quienes presten servicios a la entidad, las cuales considerarán al menos la forma o mecanismo mediante el que se prevendrá y verificará que con las remuneraciones y compensaciones no se produzcan o exacerben conflictos de intereses por parte de quienes gestionan recursos de la propia entidad y de quienes asesoran o mantienen relaciones comerciales con clientes.
>
> h) El directorio u órgano equivalente deberá evaluar la pertinencia de conformar un Comité de Gestión de Riesgos o una instancia similar que le permitan tratar y monitorear aspectos relevantes de los negocios, referidos a materias tales como conflictos de intereses, seguridad de la información, entre otros. Los fundamentos considerados por el directorio u órgano equivalente para evaluar la conformación de comités o instancias similares deberán están debidamente documentados.
>
> i) Asegurar que las actas o documentación equivalente den cuenta de las principales temáticas tratadas en las sesiones del directorio u órgano equivalente y los comités, así como las políticas y los procedimientos mencionados previamente. Todo el material que se elabore o presente al directorio u órgano equivalente o los comités, deberá estar debidamente documentado y archivado de conformidad a las normas generales aplicables en la materia, y estar permanentemente disponible para su examen a solicitud de esta Comisión."

> **TN:** Item h) contains the same grammatical irregularity as the parallel provision in §IV.B.1(l) — "deberán están debidamente documentados" — rendered idiomatically in English ("must be duly documented") without replication of the error.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.D.3 — risk-management function whose implementation the board must establish under item e)(3).

> **Source:** NCG 502 §IV.D.1 (12-ene-2024).

---

## IV.D.2 — Policies and Procedures
**NCG anchor:** N° 502, Sección IV, D.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, policies-and-procedures, order-routing

### Plain-English text

Entities must formally develop and implement risk-management and internal-control policies and procedures that address the risks associated with order routing.

The body responsible for the risk-management function shall be responsible for ensuring that all policies and procedures are prepared by those in charge of the various risk-generating areas, and for their accuracy, integrity, and currency.

The established policies and procedures must comply with the following general requirements:

a) They must relate to the number or type of clients, and to the volume of transactions carried out, in respect of each of the businesses or activities developed.

b) Policies must set out the general principles and guidelines established by the board of directors or equivalent body to guide the activities of the organisation.

c) Procedures must define how to carry out a process, with the aim of ensuring compliance with the policies approved by the board of directors, incorporating at least: the description of the principal activities that compose it and the identification of those responsible; the determination of those responsible for supervising and controlling the outcome of the activities carried out; documentation evidencing the execution of the activities that make up the procedures; the definition and description of the controls associated with those activities. In the case of outsourced activities, there must always be a person responsible within the organisation for the control of those activities.

d) Policies, procedures, and control mechanisms must be formally established and documented.

### Original Spanish

> "D.2. POLÍTICAS Y PROCEDIMIENTOS
>
> Las entidades deberán elaborar y poner en práctica de manera formal, políticas y procedimientos de gestión de riesgos y control interno que contemplen los riesgos asociados al enrutamiento de órdenes.
>
> La función de gestión de riesgos será la responsable de asegurar la elaboración de la totalidad de las políticas y los procedimientos por parte de los encargados de las distintas áreas generadoras de riesgos; y de la exactitud, integridad y actualización de tales políticas y procedimientos.
>
> Las políticas y procedimientos establecidas deberán cumplir con los siguientes aspectos generales:
>
> a) Deberán guardar relación con el número o tipo de clientes, y el volumen de operaciones efectuadas, y respecto de cada uno de los negocios o actividades que se desarrolle.
>
> b) Las políticas deberán exponer los principios generales y directrices establecidas por el directorio u órgano equivalente para orientar las actividades de la organización.
>
> c) Los procedimientos deberán definir cómo llevar a cabo un proceso, con el fin de asegurar el cumplimiento de las políticas aprobadas por el directorio, incorporando, al menos: la descripción de las actividades principales que lo componen y la identificación de sus responsables; determinación de los responsables de supervisar y controlar el resultado de las actividades ejecutadas; documentación que evidencie la ejecución de las actividades que conforman los procedimientos; definición y descripción de los controles asociados a dichas actividades. En el caso de actividades externalizadas, siempre deberá existir una persona responsable dentro de la organización respecto al control de estas.
>
> d) Las políticas, procedimientos y mecanismos de control deberán estar formalmente establecidos y documentados."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.D.2.1 — specific minimum content requirements for risk-management and internal-control policies and procedures.
- NCG 502 §IV.D.2.2 — specific requirements for operational risk, information security, and cybersecurity.
- NCG 502 §IV.D.3.1 — risk-management function responsible for ensuring policy accuracy and currency.

> **Source:** NCG 502 §IV.D.2 (12-ene-2024).

---

## IV.D.2.1 — Risk-Management and Internal-Control Policies and Procedures
**NCG anchor:** N° 502, Sección IV, D.2.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, internal-control, policies-and-procedures, order-routing

### Plain-English text

Without prejudice to the foregoing, the policies and procedures must address at least the following matters:

**a) Conflicts of interest**

Entities must define policies and procedures that specify the methods by which all potential conflicts of interest inherent in the services it offers will be identified, managed, and monitored. The policies and procedures must address the identification, prevention, and monitoring of conflicts that may arise between the order routing service and its clients, as well as those arising from other products offered by the entity, as permitted by applicable legislation and regulations.

**b) Confidentiality of information**

Entities must define policies aimed at safeguarding the confidential nature of the pending orders of clients, and must comply with all applicable legal provisions to that effect, in particular those established by Ley N° 19.628 on the protection of private life.

The policies must include consent for the use of information by clients, in accordance with Ley N° 19.628 on the protection of private life, ensuring the protection of data against unauthorised access and disclosure, and the means for protecting personal privacy and reserved information.

**c) Information to the investor**

The entity must define policies and procedures that determine how it will ensure that clients have truthful, sufficient, and timely information relating to the products or services offered, as provided in Article 28 of Ley N° 21.521.

These policies must specify, at a minimum, the information that must be known by clients in accordance with Section III of this regulation and any additional information the entity considers necessary to be known, as well as the frequency established for that purpose. For its part, the procedures must relate to how the entity will monitor compliance with these provisions.

**d) Compliance with legal and regulatory operating requirements**

Policies and procedures must be defined that specify how compliance with the applicable legal and regulatory requirements for the entity will be monitored and ensured.

In addition, procedures must be defined for the event of non-compliance with the legal operating requirements occurring, which must be reported promptly to the Commission (CMF).

### Original Spanish

> "D.2.1. POLÍTICAS Y PROCEDIMIENTOS DE GESTIÓN DE RIESGOS Y CONTROL INTERNO
>
> Sin perjuicio de lo anterior, las políticas y procedimientos deberán abordar como mínimo los siguientes aspectos:
>
> a) Conflictos de intereses
>
> Las entidades deberán definir políticas y procedimientos que especifiquen los métodos según los cuales se identificarán, manejarán y vigilarán todos los potenciales conflictos de intereses inherentes a los servicios ofrecidos por ella. Las políticas y procedimientos deberán considerar la identificación, la prevención y monitoreo de los conflictos que puedan surgir entre el servicio de enrutamiento de órdenes y sus clientes, así como de otros productos ofrecidos por la entidad, según le permita la legislación y normativa vigente.
>
> b) Confidencialidad de la información
>
> Las entidades deberán definir políticas destinadas a resguardar la naturaleza confidencial de las órdenes pendientes de ejecución de los clientes, debiendo cumplir con todas las disposiciones legales al efecto, en particular, aquellas que establece la ley N°19.628 sobre la protección de la vida privada.
>
> Las políticas deberán incluir el consentimiento para el uso de la información por parte de los clientes, de acuerdo con la ley N°19.628 sobre protección de la vida privada, asegurando la protección de los datos contra el acceso y la divulgación no autorizados y los medios para proteger la privacidad personal y la información reservada.
>
> c) Información al inversionista
>
> La entidad deberá definir políticas y procedimientos que determinen la forma en que se garantizará que los clientes cuenten con información veraz, suficiente y oportuna, relativa a los productos o servicios ofrecidos, según lo dispuesto en el artículo 28 de la ley N°21.521.
>
> Estas políticas deberán especificar, al menos, la información que debe ser conocida por los clientes de acuerdo con la Sección III de esta normativa y aquella que adicionalmente la entidad estime necesaria que se conozca, así como también la periodicidad establecida para ello. Por su parte, los procedimientos deberán estar referidos a la forma en que la entidad controlará el cumplimiento de estas disposiciones.
>
> d) Cumplimiento de requisitos legales y normativos de funcionamiento
>
> Se deberán definir políticas y procedimientos que especifiquen la forma en que se monitoreará y garantizará el debido cumplimiento de los requisitos legales y normativos aplicables a la entidad.
>
> Además, se deberá definir procedimientos en caso de presentarse eventos de incumplimiento de los requisitos legales de funcionamiento, los cuales deberán ser informados oportunamente a esta Comisión."

> **TN:** Item c) is headed "Información al inversionista" (information to the investor), reflecting that order routing clients are investors rather than credit-advisory clients; the English rendering uses "investor" accordingly rather than the generic "client" used in the heading of parallel provisions in §IV.B.2.1(e).

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- Ley 21.521 Art. 28 — client information obligation, referenced in item c).
- Ley N° 19.628 — personal data protection law referenced in items b) and c).
- NCG 502 §III — client-information obligations the policies under item c) must reference.
- NCG 502 §IV.D.2 — general policies-and-procedures framework of which this is a minimum-content specification.

> **Source:** NCG 502 §IV.D.2.1 (12-ene-2024).

---

## IV.D.2.2 — Operational Risk
**NCG anchor:** N° 502, Sección IV, D.2.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, operational-risk, information-security, cybersecurity, order-routing

### Plain-English text

Without prejudice to the minimum policies and procedures that entities must implement by virtue of the preceding section, they must observe the following guidelines in terms of information security and cybersecurity, adapting them on the basis of their business model, volume of transactions, and number and type of clients:

a) Training of personnel on the matter, so that they are aware of information security and cybersecurity risks and contribute to their adequate management.

b) The safeguarding of the information of its clients, for which it must:

1) Implement an inventory of those information assets, including a classification of these. This classification must take into account dimensions such as the availability, confidentiality, and integrity of information assets.

2) Implement an inventory of services related to information assets.

3) Implement access controls for facilities, business infrastructure, and information systems.

4) Implement tools for recording, controlling, and monitoring the activity of system users.

c) Implement controls to mitigate risks arising from the use of mobile devices and remote access by personnel, and cybersecurity management tools such as software and firmware patch management programmes, network protection against attacks through firewalls, intrusion prevention systems, privilege escalation, identity and physical and logical access management, identity control mechanisms to prevent impersonation of third parties, among others.

d) Manage environmental conditions for the secure location of the entity's equipment and tools.

e) Procedures for the identification of cybersecurity threats such as phishing, malware, malicious code injection, among others.

f) Procedures for response and recovery in the face of operational incidents, which must consider the timely recovery of critical functions; backup and support processes; previously defined critical information assets; and interdependency with third parties.

### Original Spanish

> "D.2.2. RIESGO OPERACIONAL
>
> Sin perjuicio de las políticas mínimas que deban implementar las entidades en virtud de la sección anterior, éstas deberán observar los siguientes lineamientos en términos de seguridad de la información y ciberseguridad, adaptándolas según su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) La capacitación del personal en la materia, de manera que sea consciente de los riesgos de seguridad de la información y ciberseguridad y contribuya a una adecuada gestión de éstos.
>
> b) El resguardo de la información de sus clientes, para lo cual se deberá:
>
> 1) Implementar un inventario de esos activos de información, incluyendo una clasificación de estos. Esta clasificación deberá considerar dimensiones tales como disponibilidad, confidencialidad e integridad de los activos de información.
>
> 2) Implementar un inventario de servicios relacionados con los activos de información.
>
> 3) Implementar controles de acceso a las instalaciones, infraestructuras de negocios y sistemas de información.
>
> 4) Implementar herramientas de registro, control y monitoreo de la actividad de los usuarios de sistemas.
>
> c) Implementar controles que permitan mitigar los riesgos derivados del uso de dispositivos móviles y del acceso remoto realizado por el personal, y  herramientas de gestión de la ciberseguridad tales como programas de gestión de parches de software y firmware, protección de redes ante ataques por medio de firewalls, sistemas de prevención de intrusos, elevación de privilegios, gestión de identidades y acceso físico y lógico, mecanismos de control de identidad para evitar suplantación de terceros, entre otras.
>
> d) Gestionar las condiciones ambientales para la localización segura de los equipos y herramientas de la entidad.
>
> e) Procedimientos de identificación de amenazas de ciberseguridad tales como phishing, malware, inyección de código malicioso, entre otros.
>
> f) Procedimientos de respuesta y recuperación ante incidentes operacionales, los que deberán considerar la recuperación oportuna de funciones críticas; los procesos de respaldo y soporte; los activos críticos de información previamente definidos; y la interdependencia con terceros."

> **TN:** Item c) lists "elevación de privilegios" as a standalone item in the enumeration of cybersecurity tools alongside firewalls and intrusion prevention systems. In context the phrase describes privilege-escalation controls (i.e., mechanisms to prevent or manage escalation of access rights), rendered as "privilege escalation" in the English list. This reading follows the CMF's consistent framing of the item as a control against misuse of elevated access (same convention as §IV.A.2.2 and §IV.B.2.2). Section D.2.2 adds item f) on operational incident response and recovery procedures, which does not appear in the parallel §IV.B.2.2.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.D.2 — general policies-and-procedures framework of which this is a supplementary specification.

> **Source:** NCG 502 §IV.D.2.2 (12-ene-2024), as amended by NCG 524 item 2 (02-dic-2024).

---

## IV.D.3 — Risk Management
**NCG anchor:** N° 502, Sección IV, D.3
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, order-routing

### Plain-English text

This subsection establishes the requirements for the risk-management function and the risk-management plan applicable to entities providing order routing services.

### Original Spanish

> "D.3. GESTIÓN DE RIESGOS"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this subsection implements.
- NCG 502 §IV.D.3.1 — risk-management function requirements.
- NCG 502 §IV.D.3.2 — risk-management plan requirements.

> **Source:** NCG 502 §IV.D.3 (12-ene-2024).

---

## IV.D.3.1 — Risk-Management Function
**NCG anchor:** N° 502, Sección IV, D.3.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, risk-management-function, order-routing

### Plain-English text

The risk-management function is the body responsible for monitoring the controls defined in the entity's risk-management and internal-control policies and procedures. This function must report directly to the board of directors or equivalent body.

In accordance with subparagraph D.4 of this Section, the risk-management function may be carried out by a natural person or internal unit or by the senior management (alta administración) of the entity. It may also be exercised by a corporate risk-management unit in the event that the entity belongs to a business group. For all purposes, if the function is exercised by a corporate risk-management unit in the case where the entity belongs to a business group, it shall be considered as carried out by an internal unit.

Without prejudice to the foregoing, the entity shall always be responsible for the risk-management function even when it is carried out by a body belonging to the business group, and must review and approve the reports produced in that regard, for which it must retain all relevant documentation.

Likewise, the risk-management function shall be responsible for carrying out activities to monitor compliance with the policies defined by the entity.

Additionally, it must adopt the measures that enable it to guarantee due compliance with the provisions contained in laws and regulations, and specifically in relation to due handling of matters such as prohibited activities, conflicts of interest, the possibility of fraud, and other offences or violations.

In order to implement the foregoing, the risk-management function must:

a) Verify the existence of the minimum policies and procedures described in subparagraph D.2 above.

b) Issue a report, at least on a semi-annual basis, to the board of directors or equivalent body documenting the instances of non-compliance detected, the causes that gave rise to them, the measures adopted, and the effectiveness of those measures.

c) Propose changes to risk-management policies and procedures based on the deficiencies found in its control activities.

d) Prepare an annual plan setting out the nature, scope, and timing of the activities that the risk-management function will carry out. That plan must be approved by the board of directors or equivalent body. In any event, that plan must be updated whenever significant changes occur, such as changes in economic environment and market conditions in which the entity operates, the introduction of new products or services, or changes in the regulation applicable to the entity.

### Original Spanish

> "D.3.1. FUNCIÓN DE GESTIÓN DE RIESGOS
>
> La función de gestión de riesgos es la instancia responsable del monitoreo de los controles definidos en las políticas y los procedimientos de gestión de riesgos y control interno de la entidad. Esta función deberá reportar directamente al directorio u órgano equivalente.
>
> De acuerdo con el literal D.4. de esta Sección, la función de gestión de riesgos podrá ser realizada por una persona o unidad interna o por la alta administración de la entidad. También podrá ser ejercida por una unidad de gestión de riesgos corporativa en caso de que la entidad pertenezca a un grupo empresarial. Para todos los efectos, si la función es ejercida por una unidad de gestión de riesgos corporativa, en caso de que la entidad pertenezca a un grupo empresarial, se considerará realizada por una unidad interna.
>
> Sin perjuicio de lo anterior, la entidad será siempre responsable de la función de gestión de riesgos aun cuando ésta sea realizada por una instancia perteneciente al grupo empresarial, debiendo revisar y aprobar los informes realizados al respecto, para lo cual deberá hacerse de toda la documentación relevante.
>
> Asimismo, la función de gestión de riesgos será responsable de la realización de actividades para monitorear el cumplimiento de las políticas definidas por la entidad.
>
> Adicionalmente, deberá adoptar las medidas que permitan garantizar el debido cumplimiento de las disposiciones contenidas en las leyes y normativas, y en lo específico, en lo relativo al debido manejo de materias tales como actividades prohibidas, conflictos de intereses, eventualidad de fraude, y otros delitos o infracciones.
>
> Con objeto de implementar lo anteriormente señalado, la función de gestión de riesgos deberá:
>
> a) Verificar la existencia de las políticas y procedimientos mínimos descritos en el literal D.2 anterior.
>
> b) Emitir un informe, al menos con una periodicidad semestral, al directorio u órgano equivalente para documentar las instancias de incumplimientos detectados, causas que los originaron, medidas adoptadas y efectividad de dichas medidas.
>
> c) Proponer cambios en las políticas y en los procedimientos de gestión de riesgos en función de las deficiencias encontradas en sus actividades de control.
>
> d) Elaborar un plan anual que se refiera a la naturaleza, el alcance y oportunidad de las actividades que la función de gestión de riesgos desarrollará. Este plan deberá ser aprobado por el directorio u órgano equivalente. En todo caso, dicho plan deberá ser actualizado cada vez que se produzcan cambios significativos tales como cambios en condiciones del entorno económico y mercados en que opera la entidad, introducción de nuevos productos o servicios, o cambios en la regulación aplicable a la entidad."

> **TN:** "alta administración" is rendered "senior management" — the lexicon renders "alta gerencia" as "senior management"; "alta administración" is a near-synonym used in this context with equivalent meaning; the same rendering is applied (same convention as §IV.A.3.1 and §IV.B.3.1). Unlike the parallel §IV.B.3.1, §IV.D.3.1 does not include items on methodologies and tools (§IV.B.3.1(b)), promotion of risk culture (§IV.B.3.1(e)), or the annual plan as a lettered sub-item with the same detail; §IV.D.3.1 instead consolidates the annual plan into item d) with a more streamlined scope.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.D.4 — proportionality provisions that determine whether the risk-management function may be exercised by senior management or must be independent.
- NCG 502 §IV.D.2 — minimum policies and procedures the risk-management function must verify.

> **Source:** NCG 502 §IV.D.3.1 (12-ene-2024), as amended by NCG 524 item 1 (02-dic-2024).

---

## IV.D.3.2 — Risk-Management Plan
**NCG anchor:** N° 502, Sección IV, D.3.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, risk-management-plan, order-routing

### Plain-English text

The risk-management function shall be responsible for preparing a risk-management plan that will include risk-mitigation strategies and contingency planning in relation to the principal risks, which must at a minimum address risks arising from conflicts of interest and information security and cybersecurity risks.

The board of directors or equivalent body must approve the risk-management plan at least annually, with the aim of reflecting significant changes experienced in the entity's business strategy or changes in market conditions. The risk-management function shall monitor compliance with the risk-management plan and its respective procedures.

The preparation of risk-mitigation strategies and contingency planning shall take into account the following:

a) Identification of the processes into which the activities carried out by the entity are broken down, and the respective persons responsible for those processes (process map).

The risk-management function, together with those in charge of the principal processes, must formally identify the risks inherent in those to which the entity is exposed in the development of its activities.

b) Measurement of the inherent risks identified in the activities carried out by the entity.

c) Definition of the control mechanisms to mitigate the inherent risks identified. In this regard, such control mechanisms must address:

1) Description of each control and its objective.

2) Identification of those formally designated as responsible for the control for these purposes.

3) Assessment of the effectiveness of the controls in mitigating the inherent risks, by a body independent of those responsible for them.

d) Information and communication procedures for risk management that ensure that relevant information about the effectiveness of the mitigating controls and compliance with risk-appetite levels reaches the board of directors or equivalent body and all interested parties.

e) A continuous risk-management improvement programme, with the aim of evaluating the need to make changes in response to new economic and financial scenarios facing the entity, changes in the risk profile, and as a result of the implementation or changes in international standards or best practices.

### Original Spanish

> "D.3.2. PLAN DE GESTIÓN DE RIESGOS
>
> La función de gestión de riesgos estará a cargo de la elaboración de un plan de gestión de riesgos que incluirá las estrategias de mitigación de riesgos y la planificación de contingencias en relación con los principales riesgos, los que, como mínimo deben contemplar los riesgos provenientes de conflictos de intereses y los riesgos de seguridad de la información y ciberseguridad.
>
> El directorio u órgano equivalente deberá aprobar el plan de gestión de riesgos al menos anualmente, con el fin de reflejar cambios significativos experimentados en la estrategia de negocios de la entidad o cambios en las condiciones de mercado. La función de gestión de riesgos controlará que se dé cumplimiento al plan de gestión de riesgos y a sus respectivos procedimientos.
>
> La elaboración de estrategias de mitigación de riesgos y planificación de contingencias considerará lo siguiente:
>
> a) Identificación de procesos en los que se descomponen las actividades efectuadas por la entidad, y los respectivos responsables de dichos procesos (mapa de procesos).
>
> La función de gestión de riesgos, en conjunto con los encargados de los procesos principales, deberá identificar formalmente los riesgos inherentes a los que se expone la entidad en el desarrollo de sus actividades.
>
> b) Medición de los riesgos inherentes identificados en las actividades efectuadas por la entidad.
>
> c) Definición de los mecanismos de control para mitigar los riesgos inherentes identificados. Al respecto, dichos mecanismos de control deberán considerar:
>
> 1) Descripción de cada control y su objetivo.
>
> 2) Identificación de los responsables del control formalmente designados para esos efectos.
>
> 3) Calificación de la efectividad de los controles para la mitigación de los riesgos inherentes, por una instancia independiente del responsable de estos.
>
> d) Procedimientos de información y comunicación de la gestión de riesgos que asegure que la información relevante acerca de la efectividad de los controles mitigantes y el cumplimiento de los niveles de apetito por riesgo llegue al directorio u órgano equivalente y a todas las partes interesadas.
>
> e) Programa de mejoramiento continuo de la gestión de riesgos, con el objeto de evaluar la necesidad de realizar cambios frente a nuevos escenarios económicos y financieros que vaya enfrentando la entidad, cambios del perfil de riesgo y producto de la implementación o cambios en los estándares o mejores prácticas internacionales."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.D.3.1 — risk-management function responsible for preparing and monitoring the plan.

> **Source:** NCG 502 §IV.D.3.2 (12-ene-2024).

---

## IV.D.4 — Proportionality
**NCG anchor:** N° 502, Sección IV, D.4
**Implements:** Ley 21.521 Arts. 1 and 12 (proportionality; governance & risk management)
**Tags:** governance, risk-management, proportionality, order-routing

### Plain-English text

In line with the provisions of Articles 1 and 12 of Ley N° 21.521, entities may adapt the provisions of this Section IV.D to their size, volume, and the nature of their businesses and risks.

Without prejudice to the foregoing, Table 4 describes the specific requirements for entities providing the order routing service.

Proportionality shall be applied depending on whether entities have fewer or more than 100 active clients in Chile.

**Table 4. Proportionality for the provision of the order routing service**

| Block | Characteristics of the order routing provider | Policies | Risk-management function |
|---|---|---|---|
| 1 | Fewer than 100 active clients in Chile | Exempt from all requirements of this Section IV.D | — |
| 2 | 100 or more active clients in Chile | CI, CINF, II, RLN, RO | Non-specialised |

Where:

a) CI: Conflicts of interest.
b) CINF: Confidentiality of information.
c) II: Information to the investor.
d) RLN: Compliance with legal and regulatory operating requirements.
e) RO: Operational risk.
f) Non-specialised: The risk-management function may be exercised by a member of the senior management of the entity.

The risk-management function may be non-specialised — that is, it may be exercised by the senior management, and must report directly to the board of directors or equivalent body.

When an entity reaches 100 active clients in Chile, it shall have a maximum period of 9 months to comply with the corresponding corporate-governance and comprehensive risk-management requirements. In turn, it must notify that fact to the Commission within the 5 business days following its occurrence.

Once that number is reached, entities must comply with the corporate-governance and comprehensive risk-management requirements. To revert to being exempt from the requirements, entities must remain below the indicated client threshold for more than 6 months and request authorisation from the Commission (CMF).

### Original Spanish

> "D.4. PROPORCIONALIDAD
>
> En línea con lo establecido en los artículos 1 y 12 de la ley N°21.521, las entidades podrán adaptar las disposiciones de esta Sección IV.D, conforme a su tamaño, volumen y naturaleza de sus negocios y riesgos.
>
> Sin perjuicio de lo señalado anteriormente, la Tabla 4 describe los requisitos específicos para las entidades que presten el servicio de enrutamiento de órdenes.
>
> La proporcionalidad se aplicará en función de si tienen menos o más de 100 clientes activos en Chile.
>
> Tabla 4. Proporcionalidad para la prestación del servicio de enrutamiento de
> órdenes
>
> Características del
> prestador de
> Bloque Políticas
> enrutamiento de órde- Función de ges-
> nes tión de riesgos
> Se exime de todos los requisitos de
> Menos de 100 clientes ac-
> 1 esta
> tivos en Chile
> Sección IV.D
> 100 o más clientes acti- CI, CINF, II, RLN,
> 2
> vos en Chile RO. No especializada
>
> Donde,
>
> a) CI: Conflictos de intereses.
>
> b) CINF: Confidencialidad de la información.
>
> c) II: Información al inversionista.
>
> d) RLN: Cumplimiento de requisitos legales y normativos de funcionamiento.
>
> e) RO: Riesgo operacional.
>
> f) No especializada: La función de gestión de riesgos podrá ser ejercida por algún integrante de la alta administración de la entidad.
>
> La función de gestión de riesgos podrá ser no especializada, es decir, podrá ser ejercida por la alta administración, debiendo reportar directamente al directorio u órgano equivalente
>
> Cuando una entidad alcance los 100 clientes activos en Chile, dispondrá de un plazo máximo de 9 meses para dar cumplimiento a los requisitos de gobierno corporativo y gestión integral de riesgos correspondientes. A su vez, deberá avisar ese hecho a la Comisión dentro de los 5 días hábiles siguientes de ocurrido el mismo.
>
> Una vez alcanzado ese número, las entidades deberán cumplir con las exigencias de gobierno corporativo y gestión integral de riesgos. Para volver a estar exentas de los requerimientos, las entidades deberán mantenerse por más de 6 meses bajo el umbral de clientes señalado y solicitar autorización de la Comisión."

> **TN:** Table 4 is a structured table in the PDF source. The English rendering above presents it as a Markdown table with equivalent informational content. As amended by NCG 524 (item 1), Table 4 now carries an explicit "Bloque"/"Block" column (Block 1 = fewer than 100 active clients in Chile; Block 2 = 100 or more active clients in Chile) and adds "RO" (operational risk) to the policies applicable to Block 2 (NCG 524 items 1–2), with a corresponding new defined term "e) RO: Riesgo operacional" and the renumbering of the former letter e) to f) (NCG 524 item 3). The table's extraction order in the Original Spanish blockquote preserves the NCG 524 PDF's extraction sequence, consistent with the convention established for §IV.B.4 and §IV.A.4. Table 4 still has only two data rows (a single active-client threshold, with no personal-data-processing dimension), reflecting the simpler proportionality regime applicable to order routing providers.

> **TN:** NCG 524 spliced text into an existing sentence here; consolidated Spanish is faithful (verified against the 524 source PDF) but is not contiguous in either single source PDF.

### Cross-references
- Ley 21.521 Arts. 1 and 12 — proportionality and governance mandate this section implements.
- NCG 502 §IV.D.3.1 — risk-management function requirements, including the non-specialised option available under the proportionality threshold.

> **Source:** NCG 502 §IV.D.4 (12-ene-2024), as amended by NCG 524 items 1–4 (02-dic-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/seccion-04e-gobierno-intermediacion-custodia.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/seccion-04e-gobierno-intermediacion-custodia.md

# NCG 502 — Sección IV.E: Corporate Governance & Risk Management — Intermediation & Custody of Financial Instruments (Gobierno Corporativo y Gestión de Riesgos — Intermediación y Custodia de Instrumentos Financieros)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

---

## IV.E — Intermediation and Custody of Financial Instruments
**NCG anchor:** N° 502, Sección IV, E
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, intermediation, custody

### Plain-English text

This subsection sets out the corporate-governance and risk-management obligations applicable to Financial-Service Providers (PSFs) that provide intermediation services and custody of financial instruments (intermediación y custodia de instrumentos financieros).

### Original Spanish

> "E. INTERMEDIACIÓN Y CUSTODIA DE INSTRUMENTOS FINANCIEROS"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this subsection implements.
- NCG 502 §IV — general proportionality framework applicable to all subsections of Section IV.

> **Source:** NCG 502 §IV.E (12-ene-2024).

---

## IV.E.1 — Responsibility of the Board of Directors or Equivalent Body
**NCG anchor:** N° 502, Sección IV, E.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, board, intermediation, custody

### Plain-English text

The Board of Directors or Equivalent Body (Directorio u Órgano Equivalente) is the party principally responsible for ensuring that the entity is adequately organised, and for the implementation and functioning of the entity's internal-control and risk-management system. It must also promote that both the entity and its officers adhere to the defined procedures and standards.

For those purposes, the board of directors or equivalent body must comply, at a minimum, with the risk-management principles and elements set out below:

a) Approve the appetite for the identified risks, verifying that the relevant definitions enable the entity to comply with its legal responsibilities and strategic objectives and to be sustainable over time.

b) Approve risk-management policies that are consistent with the strategic objectives, the regulatory framework, the organisational values, and the defined risk appetite, and with the use of good practices in the area of risk management associated with the entities that provide intermediation and/or custody services for financial instruments.

c) Approve the code of ethics, which sets out the organisational values and principles and establishes guidelines for the conduct of the entity's personnel.

d) Have a Risk Management Committee or another similar body. Without prejudice thereto, the board of directors or equivalent body must evaluate the appropriateness of forming committees or other bodies that allow it to address and monitor relevant business matters, relating to matters such as Audit, Money Laundering, Investments, New Products, Business Continuity, Information Security, and Cybersecurity, among others. The grounds for the actions considered by the board of directors or equivalent body to evaluate the formation of committees or similar bodies must be duly documented.

e) The board of directors or equivalent body shall establish the procedures for the formation and operation of the committees or similar bodies, which must be duly documented, as must their actions. Notwithstanding, without prejudice thereto, the Risk Management and Audit Committees (the latter, if constituted) must be composed of at least one member of the board of directors or equivalent body. In the case of entities whose management rests with a collegiate body, no director (or member of the equivalent body) may be a member of both the Risk Management Committee and the Audit Committee at the same time.

f) Ensure that the minutes or equivalent documentation reflect the principal matters addressed in the sessions of the board of directors or equivalent body and the committees, as well as the policies mentioned previously. All material prepared or presented to the board of directors or equivalent body or the committees must be duly documented and archived in accordance with the applicable general regulations on the matter, and must be permanently available for examination at the request of this Commission.

g) Approve the annual plans of the risk-management and internal-audit functions, and be aware, in a timely manner, of their compliance and of the reports they produce.

h) Periodically evaluate the adequacy of the resources of the risk-management and internal-audit functions, for which purpose it must take into consideration the coverage of the work of those functions, approving the allocation of the necessary resources and monitoring the degree of compliance with the budget assigned for that purpose.

i) Know and understand the risks inherent in the businesses and activities the entity develops.

j) Establish an adequate organisational structure, consistent with the volume and complexity of the operations and which contemplates an appropriate segregation of functions.

k) Approve and review, at least once a year, or with a greater frequency if necessary, the internal-control and risk-management policies.

l) Ensure the existence of an adequate design, implementation, and documentation of policies for:

1) The different types of operations and activities the entity carries out in the development of its business.

2) The management of confidential information.

3) The resolution of conflicts of interest between the entity, or its employees, and its clients.

4) For providers of the intermediation service for financial instruments, the knowledge of clients, of their needs and investment objectives, and the delivery of periodic information to them, with the aim of not recommending or offering them investments in instruments or assets that do not correspond to the needs, expectations, and risk tolerance expressed by them, in accordance with the provisions established in Article 28 of Ley N° 21.521.

5) Provide for controls that prevent the carrying out of prohibited activities or operations.

6) Prevent, detect, and avoid the carrying out of operations linked to money laundering, financing of terrorism, and financing of weapons of mass destruction, in accordance with the legal provisions established in Ley N° 19.913.

7) Incorporate a new product or service.

m) Approve the systems and methodologies for measuring and controlling the different types of risks the entity faces.

n) Approve policies for the treatment of exceptions to the limits of exposure to the various risks.

o) Approve a document in which the risk-management policies are recorded, and ensure their permanent review and updating.

p) Ensure the existence of a body responsible for the risk-management function and ensure its independence and adequate functioning.

q) Ensure the existence of a body responsible for the internal-audit function and ensure its independence and adequate functioning.

r) Ensure that the entity has qualified human resources, with the aim that the intermediation and/or custody activities for financial instruments are developed under high standards of professionalism and suitability, in compliance with the legal and regulatory provisions in force.

s) Implement remuneration and compensation policies for those who provide services to the entity, which must consider at least the manner or mechanism by which it will be prevented and verified that the remunerations and compensations do not give rise to or exacerbate conflicts of interest on the part of those who manage the resources of the entity itself and of those who advise or maintain commercial relationships with clients.

t) Ensure the implementation of an information system for the development of the entity's activities, risk control, and risk management.

u) Define an adequate process for disseminating a risk-management culture throughout the organisation.

v) Establish an effective mechanism for the receipt, management, and resolution of internal or external claims and reports of non-compliance with the code of ethics, in such a way as to enable the confidentiality of the person who makes them to be safeguarded. The board of directors or equivalent body must keep itself informed of relevant reports and claims.

w) Take note of the reports or accounts issued by the risk-management and internal-audit functions.

x) Have a programme for the continuous improvement of the internal-control and risk-management system, including training programmes for the entity's personnel, in order to manage with greater effectiveness the risks that arise in the development of the entity's activities.

### Original Spanish

> "E.1. RESPONSABILIDAD DEL DIRECTORIO U ÓRGANO EQUIVALENTE
>
> El Directorio u órgano equivalente es el principal responsable de que la entidad esté adecuadamente organizada, y de la implementación y funcionamiento del sistema de control interno y gestión de riesgos de la entidad. También deberá promover que tanto la entidad como sus funcionarios se atengan a los procedimientos y normas definidos.
>
> Para esos efectos, el directorio u órgano equivalente deberá dar cumplimiento, al menos, a los principios y elementos de gestión de riesgos que se señalan a continuación:
>
> a) Aprobar el apetito a los riesgos identificados, verificando que las definiciones pertinentes permitan a la entidad cumplir con sus responsabilidades legales, objetivos estratégicos y ser sostenible en el tiempo.
>
> b) Aprobar políticas de gestión de riesgos que sean coherentes con los objetivos estratégicos, el marco regulatorio, los valores organizacionales y el apetito al riesgo definido y la utilización de buenas prácticas en materia de gestión de riesgos asociados a las entidades que prestan servicios de intermediación y/o custodia de instrumentos financieros.
>
> c) Aprobar el código de ética, que dé cuenta de los valores y principios organizacionales y establezca directrices en el actuar del personal de la entidad.
>
> d) Contar con un Comité de Gestión de Riesgos u otra instancia similar. Sin perjuicio de ello, el directorio u órgano equivalente deberá evaluar la pertinencia de conformar comités u otras instancias, que le permitan tratar y monitorear aspectos relevantes de los negocios, referidos a materias tales como Auditoría, Lavado de Activos, Inversiones, Nuevos Productos, Continuidad del Negocio, Seguridad de la Información y Ciberseguridad, entre otros. Los fundamentos de las actuaciones consideradas por el directorio u órgano equivalente para evaluar la conformación de comités o instancias similares deberán estar debidamente documentados.
>
> e) El directorio u órgano equivalente establecerá los procedimientos para la conformación y funcionamiento de los comités o instancias similares, los cuales deberán quedar debidamente documentados, como también sus actuaciones. No obstante. Sin perjuicio de ello, los Comités de Gestión de Riesgos y de Auditoría (éste último, en caso de ser constituido) deberán estar integrados al menos por un integrante del directorio u órgano equivalente. Tratándose de entidades cuya dirección recae en un órgano colegiado, ningún director (o miembro del órgano equivalente) podrá ser parte del Comité de Gestión de Riesgos y del Comité de Auditoría al mismo tiempo.
>
> f) Asegurar que las actas o documentación equivalente den cuenta de las principales temáticas tratadas en las sesiones del directorio u órgano equivalente y los comités, así como las políticas mencionadas previamente. Todo el material que se elabore o presente al directorio u órgano equivalente o los comités, deberá estar debidamente documentado y archivado de conformidad a las normas generales aplicables en la materia, y estar permanentemente disponible para su examen a solicitud de esta Comisión.
>
> g) Aprobar los planes anuales de las funciones de gestión de riesgos y de auditoría interna, y estar en conocimiento, en forma oportuna, de su cumplimiento y de los informes que elabore.
>
> h) Evaluar periódicamente la suficiencia de recursos de las funciones de gestión de riesgos y de auditoría interna, para lo cual deberá tener en consideración de la cobertura del trabajo de ellas, aprobando la asignación de los recursos necesarios y monitoreando el grado de cumplimiento del presupuesto asignado a tal fin.
>
> i) Conocer y comprender los riesgos inherentes a los negocios y actividades que desarrolla la entidad.
>
> j) Establecer una estructura organizacional adecuada, consistente con el volumen y complejidad de las operaciones y que contemple una apropiada segregación de funciones.
>
> k) Aprobar y revisar al menos una vez al año, o con una mayor frecuencia si es necesario, las políticas de control interno y gestión de riesgos.
>
> l) Velar por la existencia de un adecuado diseño, implementación y documentación de políticas para:
>
> 1) Los distintos tipos de operaciones y actividades que realiza la entidad en el desarrollo de su giro.
>
> 2) El manejo de información confidencial.
>
> 3) La resolución de conflictos de intereses entre la entidad, o sus empleados, y sus clientes.
>
> 4) Para los prestadores del servicio de intermediación de instrumentos financieros, el conocimiento de los clientes, de sus necesidades y objetivos de inversión, y la entrega de información periódica a los mismos, al objeto de no recomendarles u ofrecerles inversiones en instrumentos o activos que no correspondan a las necesidades, expectativas y disposición al riesgo manifestadas por ellos, en conformidad a las disposiciones establecidas en el artículo 28 de la ley N°21.521.
>
> 5) Disponer de controles que eviten la realización de actividades u operaciones prohibidas.
>
> 6) Prevenir, detectar y evitar la realización de operaciones vinculadas al lavado de activos, financiamiento del terrorismo y financiamiento de armas de destrucción masiva, de acuerdo con las disposiciones legales establecidas en la ley N°19.913.
>
> 7) Incorporar un nuevo producto o servicio.
>
> m) Aprobar los sistemas y metodologías de medición y control de los distintos tipos de riesgos que enfrenta la entidad.
>
> n) Aprobar políticas para el tratamiento de excepciones a los límites de exposición a los diversos riesgos.
>
> o) Aprobar un documento donde consten las políticas de gestión de riesgos y asegurarse de su permanente revisión y actualización.
>
> p) Velar por la existencia de una instancia encargada de la función de gestión de riesgos y asegurarse de su independencia y adecuado funcionamiento.
>
> q) Velar por la existencia de una instancia encargada de la función de auditoría interna y asegurarse de su independencia y adecuado funcionamiento.
>
> r) Velar porque la entidad cuente con el recurso humano calificado, con el fin de que las actividades de intermediación y/o custodia de instrumentos financieros se desarrolle bajo altos estándares de profesionalismo e idoneidad, con apego a las disposiciones legales y normativas vigentes.
>
> s) Implementar políticas de remuneración y compensación para quienes presten servicios a la entidad, las cuales considerarán al menos la forma o mecanismo mediante el que se prevendrá y verificará que con las remuneraciones y compensaciones no se produzcan o exacerben conflictos de intereses por parte de quienes gestionan recursos de la propia entidad y de quienes asesoran o mantienen relaciones comerciales con clientes.
>
> t) Velar por la implementación de un sistema de información para el desarrollo de las actividades de la entidad, el control y gestión de riesgo.
>
> u) Definir un proceso adecuado de difusión de una cultura de gestión de riesgos en toda la organización.
>
> v) Establecer un mecanismo efectivo para la recepción, gestión y resolución de reclamos internos o externos y denuncias de incumplimiento al código de ética, de manera que permitan resguardar la reserva de quien lo formula. El directorio u órgano equivalente deberá mantenerse informado de las denuncias y reclamos relevantes.
>
> w) Tomar conocimiento de los reportes o informes emitidos por las funciones de gestión de riesgos y de auditoría interna.
>
> x) Contar con un programa de mejoramiento continuo del sistema de control interno y gestión de riesgos, incluyendo programas de capacitación al personal de la entidad, a objeto de gestionar con mayor eficacia los riesgos que se presentan en el desarrollo de las actividades de la entidad."

> **TN:** Item e) contains "No obstante. Sin perjuicio de ello, …" in the source — an apparent drafting artefact (a stray "No obstante." sentence fragment followed by "Sin perjuicio de ello"); reproduced verbatim in the Original Spanish, and rendered in English as "Notwithstanding, without prejudice thereto, …" without inventing additional content.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- Ley 21.521 Art. 28 — investor-information obligation referenced in item l)(4).
- Ley N° 19.913 — money-laundering prevention law referenced in item l)(6).
- NCG 502 §IV.E.2 — risk-management system the board oversees.
- NCG 502 §IV.E.5 — internal-audit function whose existence and independence the board must ensure.

> **Source:** NCG 502 §IV.E.1 (12-ene-2024), as amended by NCG 524 item cc (02-dic-2024).

---

## IV.E.2 — Risk Management
**NCG anchor:** N° 502, Sección IV, E.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, intermediation, custody

### Plain-English text

Entities must implement a risk-management system adequate to the nature, volume, and complexity of their operations. The referred system must have as its purpose the effective management of the financial, operational, and regulatory-compliance risks that arise in the businesses and activities they carry out in the development of their business, as well as those that may affect the interests and assets of clients.

Consequently, the risk-management system must consider at least the following activities:

a) Identification of the processes into which the activities carried out by the entity are broken down (process map), by means of:

1) A description of the principal activities and businesses;

2) Identification of those responsible for carrying out those activities, as well as for their supervision; and

3) The documentation evidencing that execution and supervision.

b) Formally identify the risks to which it is exposed in the development of its businesses and activities, in the processes and systems it uses.

c) Determine the risk-appetite levels in relation to its objectives and to the protection of the assets and interests of the investors.

d) Establish controls aimed at mitigating the identified risks.

e) Monitor the defined alerts, compliance with the established limits and controls, or whether the formal exception procedures have been followed.

f) Establish an effective communications system that ensures that the information relevant to risk management and control reaches the board of directors or equivalent body and other responsible bodies in a truthful, sufficient, and timely manner.

### Original Spanish

> "E.2. GESTIÓN DE RIESGOS
>
> Las entidades deberán implementar un sistema de gestión de riesgos adecuado a la naturaleza, volumen y complejidad de sus operaciones. El referido sistema debe tener como propósito gestionar eficazmente los riesgos financieros, operacionales y de cumplimiento normativo que se presentan en los negocios y actividades que realizan en el desarrollo de su giro, como también aquéllos que pueden afectar los intereses y activos de los clientes.
>
> En consecuencia, el sistema de gestión de riesgos debe considerar al menos las siguientes actividades:
>
> a) Identificación de procesos en los que se descomponen las actividades efectuadas por la entidad (mapa de procesos) a través de:
>
> 1) Una descripción de las actividades y negocios principales;
>
> 2) Identificación de los responsables de efectuar dichas actividades, así como de su supervisión; y
>
> 3) La documentación que evidencia dicha ejecución y supervisión.
>
> b) Identificar formalmente los riesgos a los que se expone en el desarrollo de sus negocios y actividades, en los procesos y sistemas que utiliza.
>
> c) Determinar los niveles de apetito al riesgo en relación con sus objetivos y a la protección de los activos e intereses de los inversionistas.
>
> d) Establecer controles tendientes a mitigar los riesgos identificados.
>
> e) Monitorear las alertas definidas, el cumplimiento de los límites y controles establecidos o si se han seguido los procedimientos formales de excepción.
>
> f) Establecer un sistema eficaz de comunicaciones que asegure que la información relevante para la gestión y control de riesgos llega en forma veraz, suficiente y oportuna al directorio u órgano equivalente y otras instancias responsables."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.2.1 — risk-management function.
- NCG 502 §IV.E.2.2 — risk-management policies and procedures.

> **Source:** NCG 502 §IV.E.2 (12-ene-2024).

---

## IV.E.2.1 — Risk-Management Function
**NCG anchor:** N° 502, Sección IV, E.2.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, risk-management-function, intermediation, custody

### Plain-English text

The body responsible for the risk-management function must be adequately segregated from the risk-generating areas and from internal audit, being responsible to the board of directors or equivalent body. The risk-management function must be carried out by personnel with verifiable experience and knowledge of reference frameworks or standards for risk management and of the specific risks the entity faces in the development of its business.

The risk-management function may be carried out by a natural person or internal unit in accordance with Section E.6 below. That function must be independent of the operational and business areas of the entity and of the body responsible for the internal-audit function, with direct reporting to the board of directors or equivalent body.

Where the entity belongs to a business group, the risk-management function of the entity may be exercised by the corporate risk-management unit, to the extent that it has thorough knowledge of the entity's risk-management framework and control environment and complies with the requirements established in this regulation, which must be agreed by the board of directors or equivalent body. The appropriateness of the respective unit of the business group that will exercise the risk function must be considered, in relation to compliance with the requirements established in this regulation and any conflicts of interest that may arise and, if applicable, their mitigation and/or elimination. For all purposes, if the function is exercised by a corporate risk-management unit, in the case where the entity belongs to a business group, it shall be considered as carried out by an internal unit.

Without prejudice to the foregoing, the entity shall always be responsible for the risk-management function even when it is carried out by a body belonging to the business group, and must review and approve the reports produced in that regard, for which it must retain all relevant documentation.

The body responsible for the risk-management function must, at a minimum:

a) Develop the activities indicated in subparagraphs E.2 and E.3 below.

b) Propose risk-management policies and procedures to the board of directors or equivalent body, consistent with the business strategy and the protection of the assets and interests of clients.

c) Analyse the risks associated with changes in the conditions of the economic environment, of the industry, and of the markets in which the entity operates, and their effects on the risk position.

d) Permanently evaluate whether the entity's policies and procedures for managing its risks are up to date, whether they are adequate for the entity, and whether they are appropriately reflected in the document that contains the risk-management policies and procedures.

e) Establish procedures so that personnel are aware of the risks, the mitigation mechanisms, and the implications of non-compliance with the control policies and procedures.

f) Carry out permanent follow-up on compliance with the risk-exposure limits and on the corrective measures that have been defined for the deficiencies identified.

g) Issue a report to the board of directors or equivalent body, at least quarterly, on the non-compliances detected in the risk-management policies and procedures, the causes that gave rise to them, measures adopted, and the entity's risk-exposure levels.

h) Issue a report at the close of each annual financial year, intended for the board of directors or equivalent body, on the functioning of the risk-management system in respect of the financial year reported, in which it gives an opinion on the functioning of the alerts and indicators; on the timely identification of relevant events of the period; weaknesses detected; and improvements applied to the system, among other aspects.

i) Propose an annual plan of activities for the following financial year, which must be approved by the board of directors or equivalent body.

j) Monitor the timely correction of the observations arising from weaknesses or deficiencies detected, both internally and externally, that have implications for the entity's risk management.

The grounds supporting any of the measures of this numeral must be duly documented.

Where the entity belongs to a business group, operational-risk management may be performed by a person of that group, provided that it maintains its independence from the group's internal audit.

### Original Spanish

> "E.2.1. FUNCIÓN DE GESTIÓN DE RIESGOS
>
> La instancia encargada de la función de gestión de riesgos deberá estar adecuadamente segregada de las áreas generadoras de riesgos y de auditoría interna, siendo responsables ante directorio u órgano equivalente. La función de gestión de riesgos deberá ser desarrollada por personal con experiencia y conocimientos comprobables en marcos de referencia o estándares de gestión de riesgos y de los riesgos específicos que la entidad enfrenta en el desarrollo de su negocio.
>
> La función de gestión de riesgos podrá ser realizada por una persona o unidad interna de acuerdo con la sección E.6 siguiente. Dicha función deberá ser independiente de las áreas operativas y de negocios de la entidad y de la instancia encargada de la función de auditoría interna, con reporte directo al directorio u órgano equivalente.
>
> En el caso que la entidad pertenezca a un grupo empresarial, la función de gestión de riesgos podrá ser ejercida por la unidad de riesgos corporativa, en la medida que ésta tenga un conocimiento acabado del marco de gestión de riesgos y ambiente de control de la entidad y que cumpla con los requisitos establecidos en la presente normativa, lo cual deberá ser acordado por el directorio u órgano equivalente. Se deberá considerar la pertinencia respecto a la idoneidad de la unidad respectiva del grupo empresarial que ejercerá la función de riesgos, en relación con el cumplimiento de los requisitos establecidos en esta norma y los conflictos de intereses que pudieran generarse y, de ser el caso, su mitigación y/o eliminación. Para todos los efectos, si la función es ejercida por una unidad de gestión de riesgos corporativa, en caso de que la entidad pertenezca a un grupo empresarial, se considerará realizada por una unidad interna.
>
> Sin perjuicio de lo anterior, la entidad será siempre responsable de la función de gestión de riesgos aun cuando ésta sea realizada por una instancia perteneciente al grupo empresarial, debiendo revisar y aprobar los informes realizados al respecto, para lo cual deberá hacerse de toda la documentación relevante.
>
> La instancia encargada de la función de gestión de riesgos al menos deberá:
>
> a) Desarrollar las actividades señaladas en los literales E.2 y E.3 siguientes.
>
> b) Proponer políticas y procedimientos para la gestión de riesgos al directorio u órgano equivalente, consistentes con la estrategia de negocios y la protección de los activos e intereses de los clientes.
>
> c) Analizar los riesgos asociados a los cambios en las condiciones del entorno económico, de la industria y de los mercados en los que opera la entidad y sus efectos en la posición de riesgos.
>
> d) Evaluar permanentemente si las políticas y procedimientos de la entidad para gestionar sus riesgos se encuentran actualizados, si son adecuados para la entidad y si éstos se recogen apropiadamente en el documento que contiene las políticas y procedimientos de gestión de riesgos.
>
> e) Establecer procedimientos para que el personal esté en conocimiento de los riesgos, los mecanismos de mitigación y las implicancias del incumplimiento de las políticas y procedimientos de control.
>
> f) Efectuar seguimiento permanente al cumplimiento de los límites de exposición al riesgo y de las medidas correctivas que se hubieren definido para las deficiencias identificadas.
>
> g) Emitir un informe al directorio u órgano equivalente, al menos con una periodicidad trimestral, sobre los incumplimientos detectados en las políticas y procedimientos de gestión de riesgos, causas que los originaron, medidas adoptadas y niveles de exposición al riesgo de la entidad.
>
> h) Emitir un informe al cierre de cada ejercicio anual, destinado al directorio u órgano equivalente, sobre el funcionamiento del sistema de gestión de riesgos respecto del ejercicio que se informa, en el que se pronuncie acerca del funcionamiento de las alertas e indicadores; de la oportuna identificación de eventos relevantes del periodo, debilidades detectadas y mejoras aplicadas al sistema, entre otros aspectos.
>
> i) Proponer un plan anual de actividades para el ejercicio siguiente, el cual debe ser aprobado por el directorio u órgano equivalente.
>
> j) Monitorear la oportuna corrección de las observaciones por falencias o deficiencias detectadas, tanto interna como externamente, que tengan implicancias en la gestión de riesgos de la entidad.
>
> Los fundamentos que sustenten cualquiera de las medidas de este numeral, deberán quedar debidamente documentados.
>
> En el caso que la entidad pertenezca a un grupo empresarial, la gestión de riesgo operacional podrá ser desempeñada por una persona de dicho grupo, siempre que mantenga su independencia de auditoría interna del grupo."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.2.2 — risk-management policies and procedures the function proposes.
- NCG 502 §IV.E.5 — internal-audit function whose independence from the risk-management function is required.
- NCG 502 §IV.E.6 — proportionality provisions governing how the function may be exercised.

> **Source:** NCG 502 §IV.E.2.1 (12-ene-2024), as amended by NCG 524 items dd.1 and dd.2 (02-dic-2024).

---

## IV.E.2.2 — Risk-Management Policies and Procedures
**NCG anchor:** N° 502, Sección IV, E.2.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, policies-and-procedures, intermediation, custody

### Plain-English text

The entities that provide intermediation and/or custody services for financial instruments must have the risk-management policies and procedures, duly documented, which must be reviewed at least once a year and updated whenever a significant change occurs, and must incorporate the following minimum contents:

a) The entity's risk matrix, in which, for each of the business lines or activities it develops, the processes that comprise it, the inherent risks associated with those processes, their relative importance in relation to the entity's objectives and the protection of the interests and assets of clients, an evaluation of the probability of occurrence and impact of those risks, and the associated mitigating controls are identified. The design of mitigating controls must consider:

1) A description of each control and its objective.

2) The identification of those responsible for the control formally designated for those purposes and the timing in which it is applied.

3) The rating of the effectiveness of the controls.

4) The residual risks, that is, that part of the inherent risks that cannot be mitigated by the corresponding controls, whether due to the type of control or its quality or effectiveness. On the basis of the residual risks, their treatment must be defined, taking into consideration the risk-appetite levels.

b) Key risk indicators, which must be monitored periodically to evaluate the exposure to the defined risk-appetite levels. For each indicator, the following must be defined and documented:

1) Its formal calculation methodology.

2) Those responsible for its generation, monitoring, and reporting.

3) Thresholds and risk-appetite levels for each indicator.

c) Alert mechanisms that enable any deficiency in the mitigating controls that gives rise to or may give rise to a significant deviation of the residual risks above the defined risk-appetite levels to be communicated in a timely manner to the responsible persons.

d) Information and communication procedures for risk management that ensure that the information relevant to the effectiveness of the mitigating controls and compliance with the risk-appetite levels reaches the board of directors or equivalent body and all relevant bodies.

e) The identification of the personnel responsible for the application of the policies and procedures, their positions, and a description of these.

f) The identification of the personnel responsible for the supervision of the persons referred to in the preceding subparagraph, whose objective is to verify that the policies and procedures are being carried out in accordance with what was defined.

g) In the event that exception situations are defined in certain procedures, the identification of the persons responsible for authorising such exceptions.

h) The description of the process for monitoring, documentation, and reporting of compliance/non-compliance with the risk-management procedures.

i) The description of the process by which the procedures and controls are approved, reviewed, and updated, and the periodicity of these activities.

### Original Spanish

> "E.2.2. POLÍTICAS Y PROCEDIMIENTOS DE GESTIÓN DE RIESGOS
>
> Las entidades que presten los servicios de intermediación y/o custodia de instrumentos financieros deberán contar con las políticas y procedimientos de gestión de riesgos, debidamente documentados, los cuales deben ser revisados al menos una vez al año y actualizados cada vez que exista un cambio significativo, y deben incorporar los siguientes contenidos mínimos:
>
> a) La matriz de riesgo de la entidad, en la que se identifiquen, para cada una de las líneas de negocio o actividades que desarrolla, los procesos que la integran, los riesgos inherentes asociados a dichos procesos, su importancia relativa en relación con los objetivos de la entidad y la protección de los intereses y activos de los clientes, una evaluación sobre la probabilidad de ocurrencia e impacto de dichos riesgos y los controles mitigantes asociados. El diseño de controles mitigantes deberá considerar:
>
> 1) Una descripción de cada control y de su objetivo.
>
> 2) La identificación de los responsables del control formalmente designados para esos efectos y la oportunidad en que se aplica.
>
> 3) La calificación de la efectividad de los controles.
>
> 4) Los riesgos residuales, esto es, aquella parte de los riesgos inherentes que no puede ser mitigada por los controles correspondientes, ya sea por el tipo de control, la calidad o efectividad del mismo. A partir de los riesgos residuales, se deberá definir su tratamiento teniendo en consideración los niveles de apetito al riesgo.
>
> b) Indicadores claves de riesgos, los que deben ser monitoreados periódicamente para evaluar la exposición a los niveles de apetito al riesgo definidos. Para cada indicador se deberá definir y documentar:
>
> 1) Su metodología de cálculo formal.
>
> 2) Los responsables de su generación, monitoreo y reporte.
>
> 3) Umbrales y niveles de apetito al riesgo para cada indicador
>
> c) Mecanismos de alerta que permitan comunicar oportunamente a las personas responsables toda deficiencia en los controles mitigantes que lleve o pueda llevar a una desviación significativa de los riesgos residuales por encima de los niveles de apetito al riesgo definidos.
>
> d) Procedimientos de información y comunicación de la gestión de riesgos que asegure que la información relevante acerca de la efectividad de los controles mitigantes y el cumplimiento de los niveles de apetito al riesgo llegue a directorio u órgano equivalente y a todas las instancias pertinentes.
>
> e) La identificación del personal responsable de la aplicación de las políticas y procedimientos, sus cargos y descripción de éstos.
>
> f) La identificación del personal responsable de la supervisión de las personas referidas en el literal precedente, cuyo objetivo es verificar que las políticas y procedimientos se están llevando a cabo de acuerdo con lo definido.
>
> g) En el evento que se definan situaciones de excepción en determinados procedimientos, la identificación de las personas responsables de autorizar tales excepciones.
>
> h) La descripción del proceso de monitoreo, documentación e informe de cumplimiento/incumplimiento de los procedimientos de gestión de riesgo.
>
> i) La descripción del proceso mediante el cual se aprueban, revisan y actualizan los procedimientos y controles y la periodicidad de estas gestiones."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.2.1 — risk-management function that proposes and applies these policies and procedures.

> **Source:** NCG 502 §IV.E.2.2 (12-ene-2024).

---

## IV.E.3 — Organization and Internal Control
**NCG anchor:** N° 502, Sección IV, E.3
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, organization, internal-control, intermediation, custody

### Plain-English text

The internal organisation of the entities will depend on the nature, size, and complexity of the businesses they carry out and of the risks they face, among other variables. Notwithstanding, in its design, the board of directors or equivalent body must consider at least the following aspects:

### Original Spanish

> "E.3. ORGANIZACIÓN Y CONTROL INTERNO
>
> La organización interna de las entidades dependerá de la naturaleza, tamaño y complejidad de los negocios que realizan y de los riesgos que enfrentan, entre otras variables. No obstante, en su diseño el directorio u órgano equivalente deberá considerar al menos los siguientes aspectos:"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.3.1 — policies and procedures the board's organisational design must establish.

> **Source:** NCG 502 §IV.E.3 (12-ene-2024).

---

## IV.E.3.1 — Policies and Procedures
**NCG anchor:** N° 502, Sección IV, E.3.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, internal-control, policies-and-procedures, conflicts-of-interest, aml, custody, intermediation

### Plain-English text

The entities that provide intermediation and/or custody services for financial instruments must establish and maintain effective operating policies, procedures, and controls in relation to their daily activity and in respect of each of the businesses or activities they develop. These policies, procedures, and controls must be formally documented and must relate at least to the following:

**a) Conflicts of interest**

Entities must define policies and procedures that specify the methods by which all potential conflicts of interest inherent in the services it offers will be identified, managed, and monitored. The policies and procedures must consider the identification, prevention, and monitoring of the conflicts of interest that may arise and that may affect its clients.

**b) Offer of products consistent with the investor's needs, expectations, and risk tolerance**

Entities must define policies and procedures aimed at investors investing their resources in financial instruments, being aware of the information that enables them to understand and accept the risk they are assuming and avoiding offering products that are not consistent with their needs, expectations, and risk tolerance, as provided in Article 28 of Ley N° 21.521.

Entities must have procedures to ensure compliance with the aforementioned obligation. In those cases where a client decides to invest in a financial instrument that, in the entity's opinion, is not consistent with the needs, expectations, or risks that the client has communicated, the entity must be able to evidence that it was duly warned, if requested by this Commission. For these purposes, those procedures may consider requiring from potential clients information such as their knowledge and experience as an investor, their financial situation, and investment or savings objectives, and other information of this nature that the entity considers relevant.

The entity must establish procedures that enable it to monitor compliance with the product-offering policy on a periodic basis, including a description of the procedures for detecting needs, expectations, and risk tolerance associated with each investor. The entity may establish exceptions to this policy, in the event that the product offering is directed at clients that qualify as institutional investors or qualified investors among those indicated in numbers 2, 3, and 4 of Section II of General Regulation N° 216.

**c) Information to the investor**

The entity must define policies and procedures that determine the way in which it will be ensured that clients have truthful, sufficient, and timely information relating to the products or services offered, as provided in Article 28 of Ley N° 21.521.

These policies must specify, at a minimum, the information that must be known by clients in accordance with Section III of this regulation, and that which the entity additionally considers necessary to be known, as well as the periodicity established for that purpose. For their part, the procedures must relate to the way in which the entity will monitor compliance with these provisions.

**d) Methodology for the approval, evaluation, and control of algorithms**

Where applicable, entities must have mechanisms for the approval, evaluation, and control of algorithms that guarantee their adequate functioning in providing the intermediation service for financial instruments. These mechanisms must ensure that the algorithms used guarantee that the transactions are carried out in the interest and protection of clients, consistent with the needs, expectations, and risk tolerance that they have previously communicated.

The entity must have trained personnel who understand the functioning of the algorithms and the continuous verification of their correct functioning.

**e) Guarantees**

In the event that the entities require guarantees from investors in order to carry out operations, they must establish:

1) The methodology for the valuation of the instruments delivered as a guarantee.

2) The eligibility of the instruments to be delivered as guarantees.

3) The periodic review of the methodologies.

4) The back-testing to determine the sufficiency of the guarantees.

**f) Prevention of money laundering and financing of terrorism**

Entities must have policies and procedures for compliance with the legal and regulatory provisions relating to the prevention of money laundering, financing of terrorism, and financing of weapons of mass destruction, as provided in Ley N° 19.913 and in the regulations issued by the Financial Analysis Unit.

**g) Compliance with legal and regulatory operating requirements**

Policies and procedures must be defined that specify the way in which compliance with the applicable legal and regulatory requirements for the entity will be monitored and ensured.

In addition, procedures must be defined for the event of non-compliance with the legal operating requirements occurring, which must be reported promptly to this Commission.

**h) Management of queries, complaints, and reports**

Entities must define policies and procedures that enable them to manage and resolve queries, reports, and complaints from their clients, workers, and the general public. For that purpose, they must consider, at a minimum, a manual that establishes, in simple terms, the minimum background information that will be required in order to make a query, report, or complaint, and that describes how to use the specialised channels arranged for those purposes. In that regard, that manual must contain:

1) The procedures for resolving queries from the public that consider the different channels arranged for these purposes and a mechanism that enables the queries made to be followed up.

2) The procedures that enable the confidentiality of the person who makes the complaint or report to be safeguarded.

3) The definition of how the seriousness or relevance of the report or complaint will be rated, and how it will be communicated to the appropriate bodies, including the board of directors or equivalent body, which must be kept informed of relevant complaints and reports.

4) The bodies that will participate in the management of the queries, reports, or complaints according to the relevance or seriousness defined for each case. In any event, the management of complaints must be carried out by a unit independent of the area in which they originated.

5) The maximum times established for managing and responding to each query, report, or complaint according to its seriousness or relevance.

6) A register of the queries, reports, and complaints together with the seriousness or relevance assigned and the solution implemented.

7) The definition of a body responsible for analysing, monitoring, and proposing measures to prevent the situations that gave rise to the queries, reports, or complaints from recurring.

**i) Integrity in custody practices**

Providers of the custody service for financial instruments must implement policies and procedures that consider:

1) The means of access of the client to the financial instruments and private cryptographic keys.

2) The maintenance of a custody register with information on operations carried out on financial instruments, including: transactions carried out by the client, positions held by the client, transfers and reconciliations of financial instruments carried out by the entity, changes in the custody of private cryptographic keys, among others. This information must be made available to the client in a truthful, sufficient, and timely manner, in such a way that the client knows how its assets are kept and the safeguard measures for them and for its private cryptographic keys.

3) The segregation of the accounts and assets of clients from the assets of the entity, in such a way that the assets of clients are clearly identified and cannot be reused or lent without their consent.

### Original Spanish

> "E.3.1. POLÍTICAS Y PROCEDIMIENTOS
>
> Las entidades que presten los servicios de intermediación y/o custodia de instrumentos financieros deberán establecer y mantener políticas, procedimientos y controles operativos efectivos en relación con su actividad diaria y respecto de cada uno de los negocios o actividades que desarrollan. Estas políticas, procedimientos y controles deben estar formalmente documentados y deberán referirse al menos a lo siguiente:
>
> a) Conflictos de intereses
>
> Las entidades deberán definir políticas y procedimientos que especifiquen los métodos según los cuales se identificarán, manejarán y vigilarán todos los potenciales conflictos de intereses inherentes a los servicios ofrecidos por ella. Las políticas y procedimientos deberán considerar la identificación, la prevención y monitoreo de los conflictos de intereses que puedan surgir y que puedan afectar a sus clientes.
>
> b) Oferta de productos acorde necesidades, expectativas y disposición al riesgo del inversionista
>
> Las entidades deberán definir políticas y procedimientos tendientes a que los inversionistas inviertan sus recursos en instrumentos financieros, conociendo la información que les permita entender y aceptar el riesgo que están asumiendo y evitando ofrecer productos que no sean acordes a sus necesidades, expectativas y disposición al riesgo, según lo dispuesto en el artículo 28 de la ley N°21.521.
>
> Las entidades deberán contar con procedimientos para asegurar el cumplimiento de la citada obligación. En aquellos casos en que un cliente decida invertir en un instrumento financiero que en opinión de la entidad no sea acorde a las necesidades, expectativas o riesgos que este le haya comunicado, la entidad deberá poder acreditar que aquello fue debidamente advertido, en caso de que le sea solicitado por esta Comisión. Para estos efectos, estos procedimientos podrán considerar el requerir a sus potenciales clientes antecedentes tales como, información sobre sus conocimientos y experiencia como inversionista, su situación financiera y objetivos de inversión o ahorro y otra información de esta naturaleza que la entidad considere relevante.
>
> La entidad deberá establecer procedimientos que permitan monitorear el cumplimiento de la política de oferta de productos en forma periódica, incluyendo una descripción de los procedimientos de detección de necesidades, expectativas y disposición al riesgo asociadas a cada inversionista. La entidad podrá establecer excepciones en esta política, en caso de que la oferta de productos esté dirigida a clientes que tengan la calidad de inversionista institucional o inversionista calificado de entre los señalados en los números 2, 3 y 4 de la Sección II de la Norma de Carácter General N°216.
>
> c) Información al inversionista
>
> La entidad deberá definir políticas y procedimientos que determinen la forma en que se garantizará que los clientes cuenten con información veraz, suficiente y oportuna, relativa a los productos o servicios ofrecidos, según lo dispuesto en el artículo 28 de la ley N°21.521.
>
> Estas políticas deberán especificar, al menos, la información que debe ser conocida por los clientes de acuerdo con la Sección III de esta normativa, y aquella que adicionalmente la entidad estime necesaria que se conozca, así como también la periodicidad establecida para ello. Por su parte, los procedimientos deberán estar referidos a la forma en que la entidad controlará el cumplimiento de estas disposiciones.
>
> d) Metodología de aprobación, evaluación y control de algoritmos
>
> En caso de corresponder, las entidades deberán contar con mecanismos de aprobación, evaluación y control de algoritmos que garanticen su adecuado funcionamiento al otorgar el servicio de intermediación de instrumentos financieros. Estos mecanismos deberán velar porque los algoritmos empleados garanticen que las transacciones se realicen en el interés y la protección de los clientes, acorde con las necesidades, expectativas y disposición al riesgo que éstos les hayan comunicado previamente.
>
> La entidad debe contar con personal capacitado que comprenda el funcionamiento de los algoritmos y la verificación continua de su correcto funcionamiento de sus algoritmos.
>
> e) Garantías
>
> En caso de que las entidades requieran garantías por parte de los inversionistas para realizar operaciones, deberá establecer:
>
> 1) La metodología para la valorización de los instrumentos entregados en garantía.
>
> 2) La elegibilidad de los instrumentos a entregar en garantías.
>
> 3) La revisión periódica de las metodologías.
>
> 4) Las pruebas retrospectivas para determinar la suficiencia de las garantías.
>
> f) Prevención de lavado de activos y financiamiento del terrorismo
>
> Las entidades deberán contar con políticas y procedimientos para el cumplimiento de las disposiciones legales y normativas relativas a la prevención del lavado de activos, financiamiento del terrorismo y financiamiento de armas de destrucción masiva, según lo dispuesto en la ley N°19.913 y en la normativa dictada por la Unidad de Análisis Financiero.
>
> g) Cumplimiento de requisitos legales y normativos de funcionamiento
>
> Se deberán definir políticas y procedimientos que especifiquen la forma en que se monitoreará y garantizará el debido cumplimiento de los requisitos legales y normativos aplicables a la entidad.
>
> Además, se deberá definir procedimientos en caso de presentarse eventos de incumplimiento de los requisitos legales de funcionamiento, los cuales deberán ser informados oportunamente a esta Comisión.
>
> h) Gestión de consultas, reclamos y denuncias
>
> Las entidades deberán definir políticas y procedimientos que les permita gestionar y resolver las consultas, denuncias y reclamos de sus clientes, trabajadores y el público general. Para ello deberá considerar, al menos, un manual que establezca, en términos simples, los antecedentes mínimos que se requerirán para efectuar una consulta, denuncia o reclamo, y que describa cómo utilizar los canales especializados que se hubieren dispuesto para esos efectos. Al respecto, dicho manual deberá contener:
>
> 1) Los procedimientos para resolver las consultas del público, que consideren los diferentes canales que se disponga para estos efectos y un mecanismo que permita hacer un seguimiento de las consultas efectuadas.
>
> 2) Los procedimientos que permitan resguardar la reserva de quien formula el reclamo o denuncia.
>
> 3) La definición de cómo se calificará la gravedad o relevancia de la denuncia o reclamo, y cómo se comunicará a las instancias que corresponda, incluyendo al directorio u órgano equivalente, el cual deberá mantenerse informado de los reclamos y denuncias relevantes.
>
> 4) Las instancias que participarán en la gestión de las consultas, denuncias o reclamos de acuerdo con la relevancia o la gravedad que se hubiere definido para cada caso. Con todo, la gestión de los reclamos deberá ser efectuada por una unidad independiente del área que dio origen a los mismos.
>
> 5) Los tiempos máximos establecidos para gestionar y responder cada consulta, denuncia o reclamo de acuerdo con su gravedad o relevancia.
>
> 6) Un registro de las consultas, denuncias y reclamos junto con la gravedad o relevancia asignada y la solución implementada.
>
> 7) La definición de una instancia encargada de analizar, monitorear y proponer medidas para evitar que las situaciones que generaron las consultas, denuncias o reclamos se repitan.
>
> i) Integridad en las prácticas de custodia
>
> Los prestadores del servicio de custodia de instrumentos financieros deberán implementar políticas y procedimientos que consideren:
>
> 1) Los medios de acceso del cliente a los instrumentos financieros y claves criptográficas privadas.
>
> 2) El mantenimiento de un registro de custodia con información de operaciones realizadas sobre instrumentos financieros, incluyendo: transacciones efectuadas por el cliente, posiciones mantenidas por el cliente, transferencias y conciliaciones de instrumentos financieros efectuadas por la entidad, cambios en la custodia de claves criptográficas privadas, entre otros. Esta información debe ponerse a disposición del cliente en forma veraz, suficiente y oportuna, de forma tal que el cliente conozca cómo se conservan sus activos y las medidas de salvaguarda de los mismos y de sus claves criptográficas privadas.
>
> 3) La segregación de las cuentas y activos de los clientes de los activos de la entidad, de manera que los activos de los clientes estén claramente identificados y no puedan ser reutilizados o prestados sin su consentimiento."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- Ley 21.521 Art. 28 — investor-information obligation, referenced in items b) and c).
- Ley N° 19.913 — money-laundering prevention law referenced in item f).
- NCG 216 §II Nos. 2, 3, 4 — institutional/qualified investor definitions referenced in item b).
- NCG 502 §III — investor-information obligations the policies under item c) must reference.
- NCG 502 §IV.E.3 — organisation and internal-control framework of which these policies are a minimum-content specification.

> **Source:** NCG 502 §IV.E.3.1 (12-ene-2024), as amended by NCG 524 items ee.1 and ee.2 (02-dic-2024).

---

## IV.E.4 — Operational Risk
**NCG anchor:** N° 502, Sección IV, E.4
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, operational-risk, intermediation, custody

### Plain-English text

Intermediaries and custodians of financial instruments, in order for the entity to develop adequate operational-risk management, must consider the elements set out below, adapting them on the basis of their business model, volume of transactions, and number and type of clients:

a) Establish operational risk-management policies and procedures, which must include, at a minimum, the following related areas, described in the following sections: information security and cybersecurity, business continuity; and outsourcing of services. The areas mentioned must be considered by the entity in the reports produced by the bodies responsible for risk management and internal audit, as applicable. The operational risk-management policies and procedures must be designed to provide reasonable assurance that the entity can carry out the business operations in a continuous and efficient manner, even in the presence of disruptive events, safeguarding its services, processes, and information assets. These policies and procedures must be established and approved by the board of directors or equivalent body, and disseminated to all personnel within the organisation. In addition, those policies and procedures must establish the risk-appetite levels defined by the board of directors or equivalent body, which will determine the need to avoid, reduce, transfer, or accept risks, and accordingly, design mitigating controls.

b) Have key operational-risk measurement indicators consistent with the entity's comprehensive risk evaluation and monitoring methodology, while at the same time enabling alert levels to be established and the effectiveness of the controls adopted to be evaluated. The detail of the calculation of these indicators must be expressly included in the entity's operational risk-management policies and procedures.

### Original Spanish

> "E.4. RIESGO OPERACIONAL
>
> Los intermediarios y custodios de instrumentos financieros, con el objeto de que la entidad desarrolle una adecuada gestión de riesgo operacional, deberán considerar los elementos que se señalan a continuación, adaptándolos de acuerdo a su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Establecer políticas y procedimientos de gestión de riesgo operacional, las que deberán incluir, al menos, los siguientes ámbitos relacionados, descritos en las próximas secciones: seguridad de la información y ciberseguridad, continuidad de negocio; y externalización de servicios. Los ámbitos mencionados deberán ser considerados por la entidad en los informes que realicen las instancias encargadas de la gestión de riesgos y la auditoría interna, según corresponda. Las políticas y procedimientos de gestión de riesgo operacional deben estar diseñadas para brindar una seguridad razonable que la entidad pueda desarrollar las operaciones del negocio en forma continua y eficiente, incluso ante la presencia de eventos disruptivos, salvaguardando sus servicios, procesos y activos de información. Estas políticas y procedimientos deben ser establecidas y aprobadas por el directorio, u órgano equivalente, y ser difundidas a todo el personal dentro de la organización. Además, dichas políticas y procedimientos deben establecer los niveles de apetito por riesgo definidos por el directorio u órgano equivalente, que determinará la necesidad de evitar, reducir, transferir o aceptar los riesgos, y acorde con ello, diseñar controles mitigantes.
>
> b) Contar con indicadores claves de medición del riesgo operacional consistentes con la metodología de evaluación y monitoreo de riesgos integrales de la entidad, permitiendo al mismo tiempo establecer niveles de alerta y evaluar la eficacia de los controles adoptados. El detalle de cálculo de estos indicadores deberá ser incluido expresamente en las políticas y procedimientos de gestión de riesgo operacional de misma la entidad."

> **TN:** Item b) closes with "de misma la entidad" (word-order inversion of "de la misma entidad"); rendered as "the entity's" without replicating the inversion, consistent with the parallel provision in §IV.C.3.b).

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.4.1 — information security and cybersecurity area.
- NCG 502 §IV.E.4.2 — business continuity area.
- NCG 502 §IV.E.4.3 — outsourcing of services area.

> **Source:** NCG 502 §IV.E.4 (12-ene-2024), as amended by NCG 524 item ff (02-dic-2024).

---

## IV.E.4.1 — Information Security and Cybersecurity
**NCG anchor:** N° 502, Sección IV, E.4.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, information-security, cybersecurity, intermediation, custody

### Plain-English text

This subsection establishes the information-security and cybersecurity obligations within operational-risk management. It comprises general provisions (E.4.1.1, below) and the procedures for managing information security and cybersecurity (E.4.1.2, reproduced in this block).

The entity must consider the following procedures, and adapt them in relation to its business model, volume of transactions, and number and type of clients (E.4.1.2 — Procedures for the management of information security and cybersecurity):

**a) Identification**

1) Have a clear definition of information assets that is sufficient for the adequate management of the associated risks.

2) Classify information, taking into account the dimensions of availability, confidentiality, and integrity.

3) Define critical information assets, which are those considered indispensable for the operation of the business, with a level of detail sufficient to enable their management, classified from the perspective of availability, confidentiality, and integrity.

4) Implement an inventory of information assets that enables the principal characteristics of the asset to be known, considering at least: hardware, software, applications, devices, systems, data, personnel, external information systems, processes, facilities, workstations, servers, storage media, and physical documentation.

5) Update the information-asset inventory on a continuous basis, for which purpose the various operational risk-management processes must report the information that may have an effect on that inventory.

**b) Protection and Detection**

1) Access controls for facilities and business, operational infrastructure, and technical units, among which are data centres, alternative power sources, and backups of data and applications.

2) Access controls for systems, so as to mitigate the risks of impersonation or improper use by third parties. In the case of critical facilities, infrastructure, and systems, the use of multifactor authentication mechanisms must be favoured.

3) Implementation of tools for recording, controlling, and monitoring the activities carried out by users and administrators of systems and information assets, including high-privilege users.

4) Procedures to grant, revoke, or modify the privileges granted to system users, network services, operating systems, databases, and business applications on the basis of personnel roles and responsibilities and only to the extent strictly necessary for the performance of their current functions.

5) Controls that enable the mitigation of risks arising from the use of mobile devices and remote access by internal or external personnel, as well as Internet of Things (IoT) devices.

6) Mechanisms for controlling and monitoring environmental conditions for the secure location of equipment and tools, taking into account humidity and temperature conditions and the possibility of fires and natural disasters.

7) Procedures for the security of the entity's operations and communications, through the implementation of:

i) Tools and controls for the proactive detection and protection against cyberattacks and other anomalous activities. For example, the use of web application firewalls, intrusion prevention systems, data loss prevention systems, denial-of-service prevention systems, email filtering, antivirus, anti-spyware, and anti-malware, among others.

ii) A process for managing the configuration of systems and information assets.

iii) Tools and procedures for the backup, transfer, restoration, and secure deletion of information, within the organisation and with third parties, including physical and electronic media. For this purpose, the following must be considered:

a) The provisions relating to the backup, transfer, restoration, and deletion of information in the regulations that safeguard the protection of data and the rights of investors, including non-disclosure agreements.

b) The backup management processes that ensure the availability, confidentiality, and integrity of information upon the occurrence of an incident, which must be consistent with the analysis of risks for the management of business continuity in accordance with the provisions of section E.4.2 below. Backups of information should, as far as possible, be kept in environments free of malicious code and in facilities distinct from the production sites. In addition, periodic backup-restoration tests must be carried out, at least annually, in order to verify that critical information can be recovered in the event that the original data are lost or damaged.

c) Tools and procedures for the identification, authentication, and access control for the digital channels through which the entity interacts with its clients.

d) Tools and procedures so that information that the entity decides to store or process through cloud services retains its characteristics of availability, confidentiality, and integrity.

**c) Response and Recovery**

1) The entity must have procedures for the management of information-security and cybersecurity incidents, considering:

i) A high-level body defined by the board of directors or equivalent body responsible for the management of information-security and cybersecurity incidents.

ii) Incident response and recovery procedures, approved by the board of directors or equivalent body, that consider the timely recovery of critical functions, backup and support processes, critical information assets, and interdependencies with third parties in the event of incidents. Those procedures must consider the provisions relating to the recording, reporting, and communication of incidents of section IV.E.8 of this regulation. Likewise, depending on the severity of the incident, the situation must be escalated to the board of directors or equivalent body for decision-making. The incident response and recovery procedures must be updated at least annually, whenever changes are recorded in information assets or incidents occur that threaten their security.

iii) Communication procedures to keep the board of directors or equivalent body, other interested parties (both internal and external), the relevant authorities on information-security and cybersecurity matters, and this Commission informed in a timely manner about the occurrence of an incident and the measures adopted to resolve it. Those procedures must consider the provisions relating to the recording, reporting, and communication of incidents of section IV.E.8 of this regulation. Likewise, in the case of incidents affecting the quality or continuity of services to clients or a publicly known event, the institution will be responsible for informing users in a timely manner about the occurrence of that event, and must update the available information until the conclusions on the causes of the incident and the measures adopted to resolve it are known, including compliance with the regulations safeguarding the protection of personal data and the rights of investors.

2) Procedures for the development, acquisition, and updating of the entity's technological infrastructure, that consider:

i) The entity's technological infrastructure needs.

ii) Implementation of a change-management process, so as to ensure that the modifications made to information assets resulting from the introduction of new products, systems, and activities are carried out and monitored in a secure and controlled manner.

As part of this process, prior to the production deployment of a service or information asset, functional, integral, security, cybersecurity, continuity, and regulatory tests must be carried out, with the aim of ensuring that there is no adverse impact on information security and on business operations.

iii) Implementation of a technological-obsolescence management process, that enables software and hardware to be maintained with support, except for duly substantiated exceptions that do not generate adverse effects on the operation of the entity's services. The use of unauthorised or non-commercially licensed software must be prevented.

iv) Implementation of a software security-update (patch) management process.

3) The entity must have a procedure for the continuous improvement of information-security and cybersecurity tools, procedures, and controls that considers:

i) Collecting and analysing information on the functioning of information assets.

ii) Analysing information-security and cybersecurity incidents and the effectiveness of the measures adopted to resolve them.

iii) Carrying out tests to identify threats and vulnerabilities in information security:

a) The tests must be carried out with a frequency no greater than one year, and be supervised by the body responsible for the entity's Risk Management.

The tests must be based on planned and designed risk scenarios in order to demonstrate that the mechanisms and tools implemented to preserve information security adequately comply with their objective, including cyberattacks.

b) The results of the tests carried out must be reported to the board of directors or equivalent body, including recommendations for improvement of the tools, procedures, and controls.

### Original Spanish

> "E.4.1. SEGURIDAD DE LA INFORMACIÓN Y CIBERSEGURIDAD
>
> E.4.1.2 PROCEDIMIENTOS PARA LA GESTIÓN DE SEGURIDAD DE LA INFORMACIÓN Y CIBERSEGURIDAD
>
> La entidad deberá considerar los siguientes procedimientos, y adaptarlos en relación con su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Identificación
>
> 1) Contar con una definición clara de activos de información que sea suficiente para la adecuada gestión de los riesgos asociados.
>
> 2) Clasificar la información, teniendo en consideración las dimensiones de disponibilidad, confidencialidad e integridad.
>
> 3) Definir los activos de información críticos, que son los activos considerados como indispensables para el funcionamiento del negocio, con un nivel suficiente de detalle que permita su gestión, clasificados desde una perspectiva de disponibilidad, confidencialidad e integridad.
>
> 4) Implementar un inventario de activos de información que permita conocer las principales características del activo, considerando al menos: hardware, software, aplicaciones, dispositivos, sistemas, datos, personal, sistemas de información externos, procesos, instalaciones, estaciones de trabajo, servidores, medios de almacenamiento y documentación física.
>
> 5) Actualizar el inventario de activos de información en forma continua, para lo cual los distintos procesos de gestión de riesgo operacional deberán reportar la información que pueda tener efecto en dicho inventario.
>
> b) Protección y Detección
>
> 1) Controles de acceso a las instalaciones e infraestructuras de negocios, operativas y dependencias técnicas, dentro de las que se encuentran los centros de datos, fuentes de energía alternativa y respaldos de datos y aplicativos.
>
> 2) Controles de acceso a los sistemas, de manera de mitigar los riesgos de suplantación o uso indebido por parte de terceros. En el caso de instalaciones, infraestructuras y sistemas críticos, se deberá privilegiar el uso de mecanismos de autenticación multifactor.
>
> 3) Implementación de herramientas de registro, control y monitoreo de las actividades realizadas por los usuarios y administradores de sistemas y activos de información, incluyendo usuarios de alto privilegio.
>
> 4) Procedimientos para otorgar, revocar o modificar los privilegios otorgados a los usuarios de los sistemas, servicios de red, sistemas operativos, bases de datos y aplicaciones de negocios en función de los roles y responsabilidades del personal y sólo lo estrictamente necesario para que éste cumpla sus funciones actuales.
>
> 5) Controles que permitan mitigar los riesgos derivados del uso de dispositivos móviles y del acceso remoto realizado por personal interno o externo, así como también los dispositivos Internet de las Cosas (IoT).
>
> 6) Mecanismos de control y monitoreo de las condiciones ambientales para la localización segura para los equipos y herramientas, teniendo en consideración las condiciones de humedad, temperatura y la posibilidad de incendios y desastres naturales.
>
> 7) Procedimientos de seguridad de las operaciones y comunicaciones de la entidad, mediante la implementación de:
>
> i) Herramientas y controles para la detección y protección proactiva de ataques cibernéticos y otras actividades anómalas. Por ejemplo, el uso de firewalls de aplicaciones web, sistemas de prevención de intrusos, sistemas de prevención de pérdida de datos, sistemas anti-denegación de servicios, filtrado de correo electrónico, antivirus, anti-spyware y anti-malware, entre otros.
>
> ii) Un proceso de gestión de la configuración de los sistemas y activos de información.
>
> iii) Herramientas y procedimientos para el respaldo, transferencia, restauración y eliminación segura de la información, al interior de la organización y con terceros, incluyendo medios físicos y electrónicos. Para ello se deberá considerar:
>
> a) Las disposiciones relativas al respaldo, transferencia, restauración y eliminación de información en las normas que resguardan la protección de datos y los derechos de los inversionistas, incluyendo acuerdos de no divulgación.
>
> b) Los procesos de administración de respaldos que aseguren la disponibilidad, confidencialidad e integridad de la información ante la ocurrencia de un incidente, el que debe ser concordante con el análisis de los riesgos para la gestión de la continuidad del negocio de acuerdo con lo dispuesto en la sección E.4.2 siguiente. Los respaldos de la información se debiesen mantener en lo posible en ambientes libres de códigos maliciosos y en instalaciones distintas a los sitios de producción. Además, se deben realizar pruebas de restauración de respaldos periódicas, al menos anuales, con el fin de verificar que la información crítica puede ser recuperada en caso de que los datos originales se pierdan o se dañen.
>
> c) Herramientas y procedimientos de identificación, autenticación y control de acceso para los canales digitales a través de los cuales la entidad interactúa con sus clientes.
>
> d) Herramientas y procedimientos para que la información que la entidad decidiere almacenar o procesar mediante servicios en la nube conserve sus características de disponibilidad, confidencialidad e integridad.
>
> c) Respuesta y Recuperación
>
> 1) La entidad deberá contar con procedimientos para la gestión de incidentes de seguridad de la información y ciberseguridad, considerando:
>
> i) Una instancia de alto nivel definida por el directorio u órgano equivalente encargada de la gestión de incidentes de seguridad de la información y ciberseguridad.
>
> ii) Procedimientos de respuesta y recuperación ante incidentes, aprobados por el directorio u órgano equivalente, que consideren la recuperación oportuna de las funciones críticas, los procesos de respaldo y soporte, los activos de información críticos y las interdependencias con terceros en caso de incidentes. Dichos procedimientos deberán considerar las disposiciones relativas al registro, reporte y comunicación de incidentes de la sección IV.E.8 de esta norma. Asimismo, dependiendo de la severidad del incidente, corresponderá escalar la situación al directorio u órgano equivalente para la toma de decisiones. Los procedimientos de respuesta y recuperación ante incidentes deberán actualizarse al menos anualmente, cada vez que se registran cambios en los activos de información o se produzcan incidentes que amenacen la seguridad de estos.
>
> iii) Procedimientos de comunicaciones para mantener informado en forma oportuna al directorio u órgano equivalente, a otras partes interesadas (tanto internas como externas), a las autoridades pertinentes en materia de seguridad de la información y ciberseguridad, y a esta Comisión, de la ocurrencia de un incidente y las medidas adoptadas para resolverlo. Estos procedimientos deberán considerar las disposiciones relativas al registro, reporte y comunicación de incidentes de la sección IV.E.8 de esta norma. Asimismo, tratándose de incidentes que afecten la calidad o continuidad de los servicios a los clientes o de un hecho de público conocimiento, la institución será responsable de informar oportunamente a los usuarios sobre la ocurrencia de dicho evento, debiendo actualizar la información disponible hasta que se conozcan las conclusiones sobre las causas del incidente y las medidas adoptadas para resolverlo, incluyendo el cumplimiento de las normas que resguardan la protección de datos personales y los derechos de los inversionistas.
>
> 2) Procedimientos para el desarrollo, adquisición y actualización de la infraestructura tecnológica de la entidad, que consideren:
>
> i) Las necesidades de infraestructura tecnológica de la entidad.
>
> ii) Implementación de un proceso de gestión de cambio, de forma de asegurar que las modificaciones realizadas a los activos de información producto de la introducción de nuevos productos, sistemas y actividades sean efectuadas y monitoreadas de manera segura y controlada.
>
> Como parte de este proceso, previo al paso de producción de un servicio o activo de información se deben realizar pruebas de carácter funcional, integral, de seguridad, de ciberseguridad, de continuidad y normativas, con el propósito de asegurar que no hubiere un impacto adverso en la seguridad de la información y en las operaciones del negocio.
>
> iii) Implementación de un proceso de gestión de obsolescencia tecnológica, que permita mantener el software y hardware con soporte, salvo las excepciones debidamente fundamentadas que no generen efectos adversos para la operación de los servicios de la entidad. Se deberá prevenir el uso de software no autorizado o sin licenciamiento comercial
>
> iv) Implementación de un proceso de gestión de actualizaciones de seguridad de software (parches).
>
> 3) La entidad deberá contar con un procedimiento para el mejoramiento continuo de las herramientas, procedimientos y controles de seguridad de la información y ciberseguridad que considere:
>
> i) Recolectar y analizar información sobre el funcionamiento de activos de información.
>
> ii) Analizar los incidentes de seguridad de la información y ciberseguridad y la efectividad de las medidas adoptadas para resolverlo.
>
> iii) Ejecutar pruebas para identificar amenazas y vulnerabilidades en la seguridad de la información:
>
> a) Las pruebas deberán ser realizadas con una periodicidad no mayor a un año, y ser supervisadas por la instancia responsable de la Gestión de Riesgos de la entidad.
>
> Las pruebas deberán estar basadas en escenarios de riesgo planificados y diseñados para demostrar que los mecanismos y herramientas implementados para preservar la seguridad de la información cumplen adecuadamente con su objetivo, incluyendo ataques cibernéticos.
>
> b) Los resultados de las pruebas realizadas deberán ser reportados al directorio u órgano equivalente, incluyendo recomendaciones de mejora en las herramientas, procedimientos y controles."

> **TN:** The PDF subdivides §IV.E.4.1 into two headed parts — E.4.1.1 (Disposiciones Generales) and E.4.1.2 (Procedimientos para la Gestión de Seguridad de la Información y Ciberseguridad). The regulation's table of contents lists only E.4.1.1 as a nested entry under E.4.1; there is no separate E.4.1.2 anchor. To preserve all source text under the contracted anchor set, the E.4.1.2 "Procedimientos" content is reproduced verbatim within this E.4.1 parent block, and the E.4.1.1 "Disposiciones Generales" content appears in the E.4.1.1 block below. In the original 12-ene-2024 text the E.4.1.2 list items were lettered d), e), f) (a drafting carry-over from the preceding E.4.1.1 list, which runs a)–g)); NCG 524 item hh.1 re-lettered them to a), b), c) respectively, as reflected here. NCG 524 item hh.2 corrected the cross-references in numbers ii) and iii) of numeral 1) of the now-c) "Respuesta y Recuperación" letter — the original "IV.E" and "V.E" references (the latter an apparent source error) were both replaced with "IV.E.8" (the recording/reporting-of-incidents provisions).

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.4.1.1 — general provisions on information security and cybersecurity.
- NCG 502 §IV.E.4.2.2 — business-continuity procedures with which backup management must be consistent (item e)(7)(iii)(b)).
- NCG 502 §IV.E.8 — recording, reporting, and communication of incidents referenced in the response and recovery procedures.

> **Source:** NCG 502 §IV.E.4.1 (12-ene-2024), as amended by NCG 524 items hh.1 and hh.2 (02-dic-2024).

---

## IV.E.4.1.1 — General Provisions
**NCG anchor:** N° 502, Sección IV, E.4.1.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, information-security, cybersecurity, intermediation, custody

### Plain-English text

In the area of information security and cybersecurity, operational-risk management must include the following elements, adapting them on the basis of their business model, volume of transactions, and number and type of clients:

a) Have an information-security and cybersecurity policy that considers at least the following:

1) Procedures for the implementation and maintenance of an information-security and cybersecurity management system, so as to safeguard the availability, confidentiality, and integrity of information assets.

2) Risk-appetite levels in relation to information security and cybersecurity.

3) Principal functions and responsibilities on the matter.

4) Procedures for the evaluation of information-security and cybersecurity risks that could be assumed when introducing new products, services, systems, undertaking new activities, or defining new processes.

5) The information-security and cybersecurity policies will form part of the entity's risk-management policies, and must be updated and approved at least annually by the board of directors or equivalent body, or with a greater frequency in the event of significant changes.

b) Have an information and communication technology (ICT) policy that considers at least the following:

1) Definition of the lines of responsibility for the management of the entity's information assets.

2) Definition of the ICT processes that ensure an adequate design, transition, service operation, and management through its information assets.

3) Definition of the procedures that must be followed for the adequate management of ICT processes.

c) Definition of the necessary number of persons with verifiable knowledge or experience in information-security and cybersecurity standards.

d) Establishment of the procedures so that the entity's personnel, including the board of directors or equivalent body, contribute to an adequate management of information-security and cybersecurity risks, in accordance with their roles and responsibilities, through the implementation of:

1) Dissemination, training, and awareness procedures that address information-security risks, vulnerabilities, and threats, the management of these, and the lessons learned with respect to incidents on this matter, in order to ensure that the entity's personnel are duly prepared to face the contingency scenarios defined and that they understand their responsibilities in the management of those risks.

2) Contractual agreements with employees that establish their responsibilities and those of the entity on information-security and cybersecurity matters, including sanctions.

e) Generation of contractual agreements for the revocation of information-access rights and destruction of information assets as part of the process of position change or termination of an employee.

f) Audit of the information-security and cybersecurity management processes, with the depth and scope necessary, that considers aspects such as compliance with the policies and the effectiveness of the procedures and controls defined on these matters.

g) Provision of procedures that enable the board of directors or equivalent body to be kept informed in a timely and periodic manner about the information-security and cybersecurity management system. The reporting of information on these matters must be recorded these matters.

### Original Spanish

> "E.4.1.1 DISPOSICIONES GENERALES
>
> En el ámbito de seguridad de la información y ciberseguridad, la gestión de riesgo operacional deberá incluir los siguientes elementos, adaptándolos de acuerdo a su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Contar con una política de seguridad de la información y ciberseguridad que considere al menos lo siguiente:
>
> 1) Procedimientos para la implementación y mantención de un sistema de gestión de seguridad de la información y ciberseguridad, de forma resguardar la disponibilidad, confidencialidad e integridad de los activos de información.
>
> 2) Niveles de apetito por riesgo en materia de seguridad de la información y ciberseguridad.
>
> 3) Principales funciones y responsabilidades sobre la materia.
>
> 4) Procedimientos para la evaluación de los riesgos de seguridad de la información y ciberseguridad que se podrían estar asumiendo al introducir nuevos productos, servicios, sistemas, emprender nuevas actividades o definir nuevos procesos.
>
> 5) Las políticas de seguridad de la información y ciberseguridad formarán parte de las políticas de gestión de riesgos de la entidad, debiendo ser actualizadas y aprobadas al menos anualmente por el directorio, u órgano equivalente, o con una periodicidad mayor en caso de cambios significativos.
>
> b) Contar con una política de tecnologías de información y comunicación (TIC), que considere al menos lo siguiente:
>
> 1) Definición de las líneas de responsabilidad en cuanto a la gestión de los activos de información en la entidad.
>
> 2) Definición de los procesos TIC que aseguren un adecuado diseño, transición, operación de servicio y gestión a través de sus activos de información.
>
> 3) Definición de los procedimientos que se deberán seguir para la adecuada gestión de los procesos TIC.
>
> c) Definición del número necesario de personas con conocimientos o experiencia comprobables en estándares de seguridad de la información y ciberseguridad.
>
> d) Establecimiento de los procedimientos para que el personal de la entidad, incluyendo el directorio u órgano equivalente, contribuya a una adecuada gestión de los riesgos de seguridad de la información y ciberseguridad, de conformidad con sus roles y responsabilidades, mediante la implementación de:
>
> 1) Procedimientos de difusión, capacitación y concientización que traten sobre los riesgos, vulnerabilidades y amenazas a la seguridad de la información, la gestión de estos, y las lecciones aprendidas respecto de los incidentes en esta materia, para garantizar que el personal de la entidad esté debidamente preparado para enfrentar los escenarios de contingencia definidos y que comprendan sus responsabilidades en la gestión de dichos riesgos.
>
> 2) Acuerdos contractuales con los empleados que establezcan sus responsabilidades y las de la entidad en materia de seguridad de la información y ciberseguridad, incluyendo sanciones.
>
> e) Generación de acuerdos contractuales para la revocación de derechos de acceso a información y destrucción de activos de información como parte del proceso de cambio de posición o desvinculación de un empleado.
>
> f) Auditoría de los procesos de gestión de la seguridad de la información y ciberseguridad, con la profundidad y alcance necesario, que considere aspectos tales como el cumplimiento de las políticas y la eficacia de los procedimientos y controles definidos en estas materias.
>
> g) Disposición de procedimientos que le permitan al directorio u órgano equivalente mantenerse informado en forma oportuna y periódica sobre el sistema de gestión de la seguridad de la información y ciberseguridad. Deberá dejarse constancia del reporte de la información de estas materias estas materias."

> **TN:** NCG 524 item gg.3 eliminated the phrase "en las respectivas actas del directorio u órgano equivalente y los comités que se conformen para revisar" from letter g). After the elimination, the source sentence reads "Deberá dejarse constancia del reporte de la información de estas materias estas materias." — i.e., the trailing "estas materias" is duplicated; the consolidated Spanish reproduces this verbatim per the amending instruction, and the English mirrors it ("must be recorded these matters").

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.4.1 — information-security and cybersecurity subsection of which these are the general provisions (and which reproduces the E.4.1.2 procedures).

> **Source:** NCG 502 §IV.E.4.1.1 (12-ene-2024), as amended by NCG 524 items gg.1, gg.2 and gg.3 (02-dic-2024).

---

## IV.E.4.2 — Business Continuity
**NCG anchor:** N° 502, Sección IV, E.4.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, business-continuity, intermediation, custody

### Plain-English text

This subsection establishes the business-continuity obligations within operational-risk management. It comprises general provisions (E.4.2.1) and the procedures for the management of business continuity (E.4.2.2).

### Original Spanish

> "E.4.2. CONTINUIDAD DEL NEGOCIO"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.4.2.1 — general provisions on business continuity.
- NCG 502 §IV.E.4.2.2 — procedures for the management of business continuity.

> **Source:** NCG 502 §IV.E.4.2 (12-ene-2024).

---

## IV.E.4.2.1 — General Provisions
**NCG anchor:** N° 502, Sección IV, E.4.2.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, business-continuity, intermediation, custody

### Plain-English text

In the area of business continuity, operational-risk management must take into account the following elements and adapt them on the basis of the business model, volume of transactions, and number and type of clients:

a) Have a business-continuity policy that considers at least the following:

1) Response procedures upon the occurrence of internal or external events that could create an interruption in the continuity of business operations. For entities classified in Block 3, these procedures must relate at least to the carrying out of a Business Impact Analysis (BIA, by its initials in English) and a Risk Impact Analysis (RIA, by its initials in English).

2) For entities belonging to Block 3, the principal functions and responsibilities on the matter, in particular which bodies will be responsible for defining, designing, executing, and improving the procedures and methodologies for business-continuity management. The business-continuity policies will form part of the entity's risk-management policies, and must be updated and approved at least annually by the board of directors or equivalent body or with a lesser frequency in the event of significant changes.

b) For entities belonging to Block 3, have persons with verifiable knowledge or experience in business-continuity standards and experience in the management of the associated risks, whose principal activities will be the development and improvement of the policies, procedures, and controls for business-continuity management. In the case of Block 1 and 2 entities, the person in charge of these matters must at least have completed an academic programme related to them.

c) Establish training and awareness policies and procedures to ensure that the entity's personnel are duly prepared to face the contingency scenarios defined and that they understand their responsibilities in the management of the risks of the business-continuity system.

d) The board of directors or equivalent body must be kept informed about business-continuity management, for which purpose it must have procedures that enable it to be informed in a timely and periodic manner. The reporting of information on these matters must be recorded.

### Original Spanish

> "E.4.2.1 DISPOSICIONES GENERALES
>
> En el ámbito de continuidad de negocio, la gestión de riesgo operacional deberá tomar en cuenta los siguientes elementos y adaptarlos de acuerdo con el modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Contar con una política de continuidad de negocio que considere a lo menos lo siguiente:
>
> 1) Procedimientos de respuesta ante la ocurrencia de eventos internos o externos que pudieran crear una interrupción en la continuidad de las operaciones del negocio. Para las entidades clasificadas en el Bloque 3, estos procedimientos se deberán referir al menos a la ejecución de un Análisis de Impacto de Negocio (BIA, por su sigla en inglés) y un Análisis de Impacto de Riesgo (RIA, por su sigla en inglés).
>
> 2) Para entidades que pertenezcan al Bloque 3, las principales funciones y responsabilidades sobre la materia, en especial, cuáles serán las instancias encargadas de definir, diseñar, ejecutar y mejorar los procedimientos y metodologías para la gestión de continuidad de negocio. Las políticas de continuidad del negocio formarán parte de las políticas de gestión de riesgos de la entidad, debiendo ser actualizada y aprobada al menos anualmente por el directorio u órgano equivalente o con una periodicidad menor en caso de cambios significativos.
>
> b) Para entidades que pertenezcan al Bloque 3, contar con personas con conocimientos o experiencia comprobables en estándares de continuidad de negocio y experiencia en la gestión de los riesgos asociados, cuyas actividades principales serán el desarrollo y mejora de las políticas, procedimientos y controles para la gestión de continuidad de negocio. En caso de las entidades del Bloque 1 y 2, la persona a cargo de estas materias deberá al menos haber cursado un programa académico relacionado con éstas.
>
> c) Establecer políticas y procedimientos de capacitación y concientización para garantizar que el personal de la entidad esté debidamente preparado para enfrentar los escenarios de contingencia definidos y que comprendan sus responsabilidades en la gestión de los riesgos del sistema de continuidad de negocio.
>
> d) El directorio u órgano equivalente deberá mantenerse informado sobre la gestión de continuidad de negocio, para lo cual deberá disponer de procedimientos que le permitan informarse de manera oportuna y periódica. Deberá dejarse constancia del reporte de la información en estas materias."

> **TN:** Item a)(2) states the business-continuity policies must be updated and approved "al menos anualmente ... o con una periodicidad menor en caso de cambios significativos" (literally "at least annually ... or with a lesser frequency in the event of significant changes"). In context "periodicidad menor" denotes a shorter interval (i.e., more frequent updates) when significant changes occur; rendered literally as "with a lesser frequency" to preserve the source wording, noting the intended meaning is more-frequent updating. The parallel E.4.1.1.a)(5) uses "periodicidad mayor" for the same notion.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.4.2.2 — procedures for the management of business continuity supplementing these general provisions.
- NCG 502 §IV.E.6 — proportionality classification defining Block 3 entities subject to BIA and RIA obligations.

> **Source:** NCG 502 §IV.E.4.2.1 (12-ene-2024), as amended by NCG 524 items ii.1, ii.2, ii.3, ii.4 and ii.5 (02-dic-2024).

---

## IV.E.4.2.2 — Procedures for the Management of Business Continuity
**NCG anchor:** N° 502, Sección IV, E.4.2.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, business-continuity, intermediation, custody

### Plain-English text

The entities that provide the services considered in this letter E must implement the following elements for the management of business continuity, adapting them in relation to the business model, volume of transactions, and number and type of clients:

a) Have a secondary physical site or a site in the cloud that enables the entity to resume operation in the event that it is interrupted at the principal site, allowing the most relevant business processes to be restored, such as platforms, infrastructure, systems, and data processing.

b) Have a Business Continuity and Disaster Recovery Plan, approved annually by the board of directors or equivalent body, that contains:

1) The procedures for the management of continuity events, with a level of detail that enables the various affected bodies to determine the activities to be developed in each defined scenario.

2) The criteria for the activation of the Plan and for the return to normality. This includes evaluating in a timely manner the business-continuity risks that could be assumed when introducing new products, systems, undertaking new activities, or defining new processes.

3) Roles and responsibilities of personnel.

The frequency of updating of this Plan could be greater depending on the entity's own regulations, or at the request of this Commission.

c) Entities classified in Block 3 must carry out or update, at least annually, in the event of events that threaten the continuity of business operations, a BIA in order to identify the processes of greatest relevance for business continuity, the impact that an interruption of those processes would have, and the times and resources necessary for their continuity and recovery. The BIA must be carried out at the strategic, tactical, and operational level. From those processes, and taking into account the risk-appetite levels defined, the following must be determined:

1) The maximum tolerable periods of disruption (MTPD by its initials in English);

2) The recovery time objectives (RTO by its initials in English);

3) The recovery point objectives (RPO by its initials in English);

4) The minimum acceptable levels of operation; and

5) The human, technological, infrastructure, and information resources necessary for their continuity and recovery.

The results of the BIA must be approved by the board of directors or equivalent body.

d) Entities classified in Block 3, defined below, must carry out or update, at least annually, a risk impact analysis (RIA) that enables the business-continuity risks that, if materialised, would cause an interruption in the most relevant processes of the entity to be identified and analysed. For the foregoing, internal and external scenarios must be considered, contemplating, among others, the total and partial failure of technological systems; malicious attacks affecting cybersecurity; the absence of critical personnel; the impossibility of accessing or using physical facilities; and the failure to provide critical services contracted to suppliers.

e) Entities classified in Block 3, in consideration of the results of the BIA and the RIA, must define a business-continuity strategy that has as its objective maintaining the continuity of the most relevant processes, considering preventive measures to reduce the probability of materialisation of damage, minimise the recovery time, and limit the impact on the entity's business operations.

f) A Crisis Plan must be implemented in which the escalation, communication, management, and reporting procedures for operational-continuity events are determined, in order to keep the board of directors or equivalent body, all interested parties, and this Commission informed in a timely manner about relevant information regarding the continuity event, the measures adopted to resolve it, and to coordinate an adequate response within the recovery point and time objectives provided for in the BIA (entities classified in Block 3 referred to in the preceding sections).

g) Have a procedure for the continuous improvement of the policies, plans, and procedures of business continuity with the aim of reducing the response times when an identical or similar incident recurs; identifying possible improvements in the processes; facilitating the exchange of knowledge; and having information available that enables decision-making to be supported in the event of new incidents materialising.

h) Test annually the Business Continuity and Disaster Recovery Plan, so as to ensure that it is adequate and effective, without prejudice to the fact that this Commission may request a different frequency for entities classified in Block 3. These tests must consider at least the following:

1) They must be supervised by the body responsible for the entity's Risk Management.

2) Being based on risk scenarios that resemble real events, including severe but plausible scenarios. The foregoing, in order to demonstrate that the business-continuity procedures will function if necessary, including cyberattacks, natural disasters, and health contingencies.

3) Block 1 and 2 entities, defined in Section E.6 below, may use business-continuity indicators different from those established in the preceding letter c).

### Original Spanish

> "E.4.2.2 PROCEDIMIENTOS PARA LA GESTIÓN DE LA CONTINUIDAD DE NEGOCIOS
>
> Las entidades que presten los servicios considerados en esta letra E deberán implementar los siguientes elementos para la gestión de la continuidad de negocios, adaptándolos en relación con el modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Disponer de un sitio secundario físico o en la nube que permita a la entidad reanudar la operación en caso de que esta se vea interrumpida en el sitio principal, permitiendo restablecer los procesos de mayor relevancia del negocio, tales como plataformas, infraestructura, sistemas y procesamiento de datos.
>
> b) Contar con un Plan de Continuidad de Negocio y Recuperación de Desastres, aprobado anualmente por el directorio u órgano equivalente, que contenga:
>
> 1) Los procedimientos para la gestión de eventos de continuidad, con un nivel de detalle que permita a las distintas instancias afectadas determinar las actividades a desarrollar en cada escenario definido.
>
> 2) Los criterios para la activación del Plan y para la vuelta a la normalidad. Esto incluye evaluar oportunamente los riesgos asociados a la continuidad de negocios que se podrían estar asumiendo al introducir nuevos productos, sistemas, emprender nuevas actividades o definir nuevos procesos.
>
> 3) Roles y responsabilidades del personal.
>
> La periodicidad de actualización de este Plan podría ser mayor dependiendo de la normativa propia de la entidad, o a requerimiento de esta Comisión.
>
> c) Las entidades clasificadas en el Bloque 3 deberán realizar o actualizar, al menos anualmente, ante eventos que amenacen la continuidad de las operaciones del negocio, un BIA con el objeto de identificar los procesos de mayor relevancia para la continuidad de negocio, el impacto que tendría una interrupción de esos procesos, y los tiempos y recursos necesarios para la continuidad y recuperación de estos. El BIA deberá realizarse a nivel estratégico, táctico y operativo. De esos procesos, y considerando los niveles de apetito por riesgo definidos, se deberá determinar:
>
> 1) Los tiempos máximos tolerables de interrupción (MTPD por sus siglas en inglés);
>
> 2) Los tiempos objetivos de recuperación (RTO por sus siglas en inglés);
>
> 3) Los puntos objetivos de recuperación (RPO por sus siglas en inglés);
>
> 4) Los niveles mínimos aceptables de operación; y
>
> 5) Los recursos humanos, tecnológicos y de infraestructura e información necesarios para su continuidad y recuperación.
>
> Los resultados del BIA deberán ser aprobados por el directorio u órgano equivalente.
>
> d) Las entidades clasificadas en el Bloque 3, definido más abajo, deberán realizar o actualizar, al menos anualmente, una evaluación de impacto de riesgos (RIA) que permita identificar y analizar los riesgos de continuidad de negocio que, de materializarse, provocarían una interrupción en los procesos de mayor relevancia de la entidad. Para lo anterior, se deberá considerar escenarios internos y externos, contemplando, entre otros, la falta total y parcial de los sistemas tecnológicos; ataques maliciosos que afecten la ciberseguridad; la ausencia de personal crítico; la imposibilidad de acceder o utilizar las instalaciones físicas; y la falta de provisión de los servicios críticos contratados a proveedores.
>
> e) Las entidades clasificadas en el Bloque 3, en consideración de los resultados del BIA y el RIA, deberán definir una estrategia de continuidad de negocio que tenga por objetivo mantener la continuidad de los procesos de mayor relevancia, considerando medidas preventivas para reducir la probabilidad de materialización de daños, minimizar el tiempo de recuperación y limitar el impacto en las operaciones del negocio de la entidad.
>
> f) Se deberá implementar un Plan de Crisis en el que se determine los procedimientos de escalamiento, comunicaciones, gestión y reporte de eventos de continuidad operacional para mantener informado en forma oportuna al directorio u órgano equivalente, a todas las partes interesadas y a esta Comisión, respecto de información relevante respecto del evento de continuidad, las medidas adoptadas para resolverlo y para coordinar una respuesta adecuada dentro de los puntos objetivos y tiempos objetivos de recuperación previstos en el BIA (entidades clasificadas en el Bloque 3 al que se refieren las secciones anteriores).
>
> g) Contar con un procedimiento para el mejoramiento continuo de las políticas, planes y procedimientos de continuidad del negocio con el objeto de disminuir los tiempos de respuesta cuando se repita un incidente igual o similar; identificar posibles mejoras en los procesos; facilitar el intercambio de conocimientos; y disponer de información que permita apoyar la toma de decisiones en caso de materializarse nuevos incidentes.
>
> h) Probar anualmente el Plan de Continuidad de Negocio y Recuperación de Desastres, de forma de asegurar que es adecuado y efectivo, sin perjuicio de que esta Comisión pueda solicitar una periodicidad diferente para las entidades clasificadas en el Bloque 3. Estas pruebas deberán considerar a lo menos lo siguiente:
>
> 1) Deberán ser supervisadas por la instancia responsable de la Gestión de Riesgos de la entidad.
>
> 2) Estar basadas en escenarios de riesgo que se asimilen a eventos reales incluyendo escenarios severos pero plausibles. Lo anterior, para demostrar que los procedimientos de continuidad de negocio funcionarán en caso de ser necesarios, incluyendo ataques cibernéticos, desastres naturales y contingencias sanitarias.
>
> 3) Las entidades del Bloque 1 y 2, definidas en la sección E.6 siguiente, podrán utilizar indicadores de continuidad del negocio distintos de los establecidos en el literal c) precedente."

> **TN:** In the original 12-ene-2024 text, item h)(3) cross-referred to "las secciones anteriores" and to "la Sección B.2.c". NCG 524 item jj replaced the whole literal h), correcting these to "la sección E.6 siguiente" and to "el literal c) precedente" respectively, and removing the original trailing reporting paragraph of h); the consolidated text reflects the amended h).

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.4.2.1 — general provisions on business continuity these procedures supplement.
- NCG 502 §IV.E.6 — proportionality classification defining the Block 1, 2, and 3 thresholds referenced throughout.
- NCG 502 §IV.E.4.1 — backup management (§IV.E.4.1.2.e)(7)(iii)(b)) that must be consistent with this continuity analysis.

> **Source:** NCG 502 §IV.E.4.2.2 (12-ene-2024), as amended by NCG 524 item jj (02-dic-2024).

---

## IV.E.4.3 — Outsourcing of Services
**NCG anchor:** N° 502, Sección IV, E.4.3
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, outsourcing, intermediation, custody

### Plain-English text

This subsection establishes the obligations relating to the outsourcing of services within operational-risk management. It comprises the outsourcing risks (E.4.3.1) and the procedures for the management of outsourced services (E.4.3.2).

### Original Spanish

> "E.4.3. EXTERNALIZACIÓN DE SERVICIOS"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.4.3.1 — outsourcing risks.
- NCG 502 §IV.E.4.3.2 — procedures for the management of outsourced services.

> **Source:** NCG 502 §IV.E.4.3 (12-ene-2024).

---

## IV.E.4.3.1 — Outsourcing Risks
**NCG anchor:** N° 502, Sección IV, E.4.3.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, outsourcing, intermediation, custody

### Plain-English text

The services provided by suppliers, relating to regulatory compliance, business continuity, information security, and the quality of the services, products, information, and image of the contracting entity, must be considered in the operational risk-management processes of the entity. In that regard, for the evaluation of supplier-contracting risks, the following risks, among others, must be considered:

1) Substitution risk: the possibility of substituting or not a supplier within a determined period that guarantees the continuity of the contracted service.

2) Intervention risk: the possibility that the entity has to take over the contracted function.

3) Subcontracting risk: the possibility that the supplier in turn subcontracts all or part of the service, reducing the entity's capacity to supervise the subcontracted function.

4) Concentration risk: the possibility that an entity contracts one or several services with the same supplier that is difficult to substitute, increasing the possibility of prolonged failures or interruptions.

### Original Spanish

> "E.4.3.1 RIESGOS DE EXTERNALIZACIÓN
>
> Los servicios prestados por proveedores, relacionados con el cumplimiento normativo, la continuidad del negocio, la seguridad de la información y la calidad de los servicios, productos, información e imagen de la entidad contratante, deberán ser considerados en los procesos de gestión de riesgo operacional de la entidad. En tal sentido, para la evaluación de riesgos de contratación de proveedores, se deberán considerar, entre otros, los siguientes riesgos:
>
> 1) Riesgo de sustitución: la posibilidad de sustituir o no a un proveedor dentro de un plazo determinado que garantice la continuidad del servicio contratado.
>
> 2) Riesgo de intervención: la posibilidad de que la entidad tenga que hacerse cargo de la función contratada.
>
> 3) Riesgo de subcontratación: la posibilidad de que el proveedor subcontrate a su vez todo o parte del servicio, reduciendo la capacidad de la entidad de supervisar la función subcontratada.
>
> 4) Riesgo de concentración: la posibilidad que una entidad contrate uno o varios servicios en un mismo proveedor que sea difícil de sustituir, incrementando la posibilidad de fallas o interrupciones prolongadas."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.4.3.2 — procedures for the management of outsourced services that address these risks.

> **Source:** NCG 502 §IV.E.4.3.1 (12-ene-2024), as amended by NCG 524 item kk (02-dic-2024).

---

## IV.E.4.3.2 — Procedures for the Management of Outsourced Services
**NCG anchor:** N° 502, Sección IV, E.4.3.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, operational-risk, outsourcing, cloud, intermediation, custody

### Plain-English text

In the area of outsourcing of services, operational-risk management must consider the following elements and adapt them on the basis of the business model, volume of transactions, and number and type of clients:

a) Have a policy for the outsourcing of services that considers at least the following:

1) Define the governance structure and the procedures to be followed to authorise and manage the outsourcing of services to third parties, including the reporting and responsibility lines.

2) Establish the objectives in relation to the outsourcing of services.

3) Establish the risk-appetite levels in the outsourcing of services and the mitigation strategies.

4) Comply with the provisions on information security, cybersecurity, and business continuity.

5) Establish the procedures for the determination of critical services. In that regard, in order to understand a service as critical, the following considerations must be taken into account:

i) The effect that a weakness or failure in the provision or execution of the service has on regulatory compliance, business continuity, information security, and the quality of the services, products, information, and image of the contracting entity.

ii) The complexity of the associated commercial functions.

iii) The degree to which the service can be transferred quickly to another supplier, considering the costs and the time to do so.

6) Define the services that can only be outsourced with the prior approval of the board of directors or equivalent body.

7) Define the minimum elements that the service-provision contract must incorporate.

8) Define the risk-management elements that will not be applied to activities that, by their nature, do not have a relevant impact on the provision of the services.

9) Include the outsourcing-of-services policies as part of the entity's risk-management policies, which must be approved and updated at least annually by the board of directors or equivalent body, or with a greater frequency in the event of significant internal or external changes.

10) Consider the substitution, intervention, subcontracting, and concentration risks of the preceding section.

b) Establish procedures for the selection, contracting, and monitoring of suppliers that consider:

1) A definition of the particular contracting criteria, when the supplier is a related entity. These criteria must be aimed at avoiding the conflicts of interest that may arise.

2) The incorporation into the analysis of elements that enable a due-diligence process to be carried out, so as to ensure that the suppliers have an adequate commercial reputation, financial solvency, experience, and sufficient resources to guarantee the quality of the provision of the service. In the case of services in which full compliance with the aforementioned conditions cannot be guaranteed, as may be the case of data-processing services carried out abroad, the entity's board of directors or equivalent body must review and evaluate background information supporting the quality of the service provided, the financial soundness of the supplier, and the existence of adequate personal-data protection legislation in the applicable jurisdiction, taking responsibility for the availability, confidentiality, and integrity of the information delivered to the contracted supplier.

c) Contemplate in the contracts with the suppliers of outsourced services the following minimum contents:

1) A clear description of the contracted service and the term of validity.

2) The service-provision obligations of the supplier, defining agreed service levels. The entity must define the situations that will be considered serious contractual breaches and grounds for early termination of the contract.

3) The obligation to communicate any event that may have a material impact on the capacity to carry out the outsourced service.

4) The information-security, cybersecurity, and business-continuity requirements that the supplier must comply with, which must be consistent with the provisions established on this matter by the entity. The suppliers must have incident-management and business-continuity procedures that enable them to continue providing the services in the event that disruptive situations arise.

5) The documentation of the operational, administrative, and technological procedures specific to the contracted service. In the case of the existence of chain subcontracting, the entity must verify compliance with the conditions agreed with the initial service supplier and the entities subcontracted by the latter.

6) The procedures for the periodic evaluation and monitoring of the quality of the provision of the outsourced service. The entity may agree with the supplier the carrying out of audits by designated third parties or by the entity itself, which will be responsible in the last instance for guaranteeing the quality of the provision of the outsourced service.

7) The strategies for the termination of the provision of outsourced services without prejudice to the entity's operations, considering those situations in the Business Continuity and Disaster Recovery Plan.

d) Have a register of outsourced services, in order to manage the subcontracting risks, which must include at least the following information:

1) Identification of the outsourced service, including a brief description of it and of the data involved if it is a critical service, whether there is chain subcontracting, and whether it is carried out in the cloud.

2) Identification of the supplier, including whether or not it is a related entity.

3) Start, renewal, and termination date of the service.

4) In the case of data-processing services, a description of the data and processing that are subcontracted, the security measures adopted, and the geographic location of the supplier.

5) In the case of chain subcontracting, the entities to which the supplier subcontracts the service must be detailed, a description of the associated risks and whether the supplier carries out a control of the quality of the provision of the service subcontracted in chain.

e) Periodically monitor that the suppliers comply with the conditions agreed in order to guarantee the quality of the provision of the service. The entity will be responsible for the quality of the outsourced services.

f) In the event that the entity decides to contract services for accessing and processing information in the cloud, or that the supplier as part of the chain subcontracting considers cloud services, a reinforced analysis of the risks inherent in those services must be carried out, analysing in particular how it could affect the availability, confidentiality, and integrity of the information, and the business continuity of the entity. That analysis must take into account factors such as:

1) The independent certifications regarding the management of information security and the quality of the provision of the supplier's service.

2) The execution of the outsourcing-of-services contract directly between the entity and the supplier, with the aim of minimising the risks in this type of service.

3) The processing or storage of information in other jurisdictions, and in that case the existence of regulations safeguarding the protection of personal data, the availability, confidentiality, and integrity of information, and the resolution of legal contingencies.

4) The existence of adequate security mechanisms of the supplier, both physical and logical, that enable the components of the infrastructure in the cloud that the entity shares with other clients of the supplier to be isolated, so as to prevent leaks of information or events that may affect the availability, confidentiality, and integrity of the entity's data.

5) The use of encryption techniques for the data that the entity establishes, in accordance with their nature and sensitivity.

g) Evaluate that the supplier of the contracted services possesses adequate knowledge and experience.

h) Maintain personnel with the due knowledge and experience to carry out the control of the provision of services performed by its suppliers. Likewise, it must also oversee due compliance with those regulatory and legal aspects that could affect the provision of the contracted services.

i) The board of directors or equivalent body must be kept informed about the matters relating to the outsourcing of services, for which purpose it must have procedures that enable it to be informed in a timely and periodic manner. The reporting of information on these matters must be recorded.

### Original Spanish

> "E.4.3.2 PROCEDIMIENTOS PARA LA GESTIÓN DE SERVICIOS EXTERNALIZADOS
>
> En el ámbito de externalización de servicios, la gestión de riesgo operacional deberá considerar los siguientes elementos y adaptarlos de acuerdo con el modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Contar con una política para la externalización de servicios que considere a lo menos lo siguiente:
>
> 1) Definir la estructura de gobierno y de los procedimientos a seguir para autorizar y gestionar la externalización de servicios por terceros, incluyendo las líneas de reporte y de responsabilidad.
>
> 2) Establecer los objetivos en materia de externalización de servicios.
>
> 3) Establecer los niveles de apetito por riesgo en la externalización de servicios y las estrategias de mitigación.
>
> 4) Cumplir con las disposiciones en materia de seguridad de la información, ciberseguridad y continuidad de negocios.
>
> 5) Establecer los procedimientos para la determinación de los servicios críticos. En tal sentido, para entender como crítico un servicio se deberán tener en cuenta las siguientes consideraciones:
>
> i) El efecto que una debilidad o falla en la provisión o ejecución del servicio tenga sobre el cumplimiento normativo, continuidad del negocio, seguridad de la información y la calidad de los servicios, productos, información e imagen de la entidad contratante.
>
> ii) La complejidad de las funciones comerciales asociadas.
>
> iii) El grado en que el servicio puede transferirse rápidamente a otro proveedor, considerando los costos y el tiempo para hacerlo.
>
> 6) Definir los servicios que solo pueden ser externalizados con la aprobación previa del directorio u órgano equivalente.
>
> 7) Definir los elementos mínimos que deberá incorporar el contrato de prestación de servicios.
>
> 8) Definir los elementos de la gestión de riesgos que no serán aplicados a actividades que por su naturaleza no tengan impacto relevante en la prestación de los servicios.
>
> 9) Incluir a las políticas de externalización de servicios como parte de las políticas de gestión de riesgos de la entidad, debiendo ser aprobada y actualizada al menos anualmente por el directorio u órgano equivalente, o con una frecuencia mayor en caso de cambios internos o externos significativos.
>
> 10) Considerar los riesgos de sustitución, intervención, subcontratación y concentración de la sección anterior.
>
> b) Establecer procedimientos para la selección, contratación y monitoreo de proveedores que consideren:
>
> 1) Una definición de los criterios particulares de contratación, cuando el proveedor se trate de una entidad relacionada. Estos criterios deberán estar destinados a evitar los conflictos de intereses que se pueden presentar.
>
> 2) La incorporación al análisis de elementos que permitan llevar a cabo un proceso de debida diligencia, de forma de asegurar que los proveedores tengan una adecuada reputación comercial, solvencia financiera, experiencia y recursos suficientes para garantizar la calidad de la provisión del servicio. En el caso de servicios en los que no se pueda garantizar el pleno cumplimiento de las condiciones mencionadas, como puede ser el caso de servicios de procesamiento de datos realizados en el extranjero, el directorio u órgano equivalente de la entidad deberá revisar y evaluar antecedentes que respalden la calidad del servicio prestado, la solidez financiera del proveedor y la existencia de una adecuada legislación de protección de datos personales en la jurisdicción aplicable, haciéndose responsable por la disponibilidad, confidencialidad e integridad de la información entregada al proveedor contratado.
>
> c) Contemplar en los contratos con los proveedores de servicios externalizados los siguientes contenidos mínimos:
>
> 1) Una descripción clara del servicio contratado y el plazo de vigencia.
>
> 2) Las obligaciones de prestación del servicio por parte del proveedor, definiendo niveles de servicio acordados. La entidad deberá definir las situaciones que se considerarán graves incumplimientos contractuales y causales de término anticipado del contrato.
>
> 3) La obligación de comunicar cualquier acontecimiento que pueda tener un impacto material en la capacidad para llevar a cabo el servicio externalizado.
>
> 4) Los requisitos de seguridad de la información, ciberseguridad y continuidad de negocios que deberá cumplir el proveedor, que deben ser concordantes con las disposiciones establecidas en esta materia por la entidad. Los proveedores deberán contar con procedimientos de gestión de incidentes y continuidad de negocios que le permitan seguir brindando los servicios en el evento que se presenten situaciones disruptivas.
>
> 5) La documentación de los procedimientos operacionales, administrativos y tecnológicos propios del servicio contratado. En el caso de existir subcontratación en cadena, la entidad deberá verificar el cumplimiento de las condiciones pactadas con el proveedor de servicios inicial y las entidades subcontratadas por este último.
>
> 6) Los procedimientos para la evaluación y monitoreo periódico de la calidad de la provisión del servicio externalizado. La entidad podrá pactar con el proveedor la realización de auditorías por terceros designados o por la propia entidad, quien será responsable en última instancia por garantizar la calidad de la provisión del servicio externalizado.
>
> 7) Las estrategias para el término de la prestación de servicios externalizados sin perjudicar las operaciones de la entidad, considerando esas situaciones en el Plan de Continuidad del Negocio y Recuperación ante Desastres.
>
> d) Contar con un registro de servicios externalizados, para gestionar los riesgos de subcontratación, que deberá incluir al menos la siguiente información:
>
> 1) Identificación del servicio externalizado, incluyendo una breve descripción del mismo y de los datos involucrados si corresponde a un servicio crítico, si existe subcontratación en cadena, y si se lleva a cabo en la nube.
>
> 2) Identificación del proveedor, incluyendo si corresponde a una entidad relacionada o no.
>
> 3) Fecha de inicio, renovación y término del servicio.
>
> 4) En el caso de servicios de procesamiento de datos, una descripción de los datos y tratamientos que se subcontratan, las medidas de seguridad adoptadas, y la ubicación geográfica del proveedor.
>
> 5) En caso de subcontratación en cadena, se deberá detallar cuáles son las entidades a las que el proveedor subcontrata el servicio, una descripción de los riesgos asociados y si el proveedor realiza un control de la calidad de la provisión del servicio subcontratado en cadena.
>
> e) Monitorear periódicamente que los proveedores cumplen con las condiciones pactadas para garantizar la calidad de la provisión del servicio. La entidad será responsable de la calidad de los servicios externalizados.
>
> f) En el caso de que la entidad decida contratar servicios de acceso y tratamiento de información en la nube, o que el proveedor como parte de la subcontratación en cadena considere los servicios en la nube, se deberá realizar un análisis reforzado de los riesgos inherentes a esos servicios, analizando en particular cómo podría afectarse la disponibilidad, confidencialidad e integridad de la información, y la continuidad de negocio de la entidad. Ese análisis deberá tener en consideración factores tales como:
>
> 1) Las certificaciones independientes respecto a la gestión de la seguridad de la información y la calidad de la prestación del servicio del proveedor.
>
> 2) La celebración del contrato de externalización de servicios directamente entre la entidad y el proveedor, con la finalidad de minimizar los riesgos en este tipo de servicios.
>
> 3) El procesamiento o almacenamiento de información en otras jurisdicciones, y en ese caso la existencia de normas que resguardan la protección de datos personales, la disponibilidad, confidencialidad e integridad de la información y la resolución de contingencias legales.
>
> 4) La existencia de adecuados mecanismos de seguridad del proveedor, tanto físicos como lógicos, que permitan aislar los componentes de la infraestructura en la nube que la entidad comparte con otros clientes del proveedor, de manera de prevenir fugas de información o eventos que puedan afectar la disponibilidad, confidencialidad e integridad de los datos de la entidad.
>
> 5) La utilización de técnicas de encriptación para los datos que la entidad establezca, de acuerdo con su naturaleza y sensibilidad
>
> g) Evaluar que el proveedor de los servicios contratados posea adecuados conocimientos y experiencia.
>
> h) Mantener personal con el debido conocimiento y experiencia para efectuar el control de la prestación de servicios efectuada por sus proveedores. Asimismo, también deberá vigilar el debido cumplimiento de aquellos aspectos regulatorios y legales que pudiesen afectar la provisión de los servicios contratados.
>
> i) El directorio u órgano equivalente deberá mantenerse informado sobre las materias referidas a la externalización de servicios, para lo cual deberá disponer de procedimientos que le permitan informarse de manera oportuna y periódica. Deberá dejarse constancia del reporte de la información en estas materias."

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.4.3.1 — outsourcing risks (substitution, intervention, subcontracting, concentration) referenced in item a)(10).
- NCG 502 §IV.E.4.2.2 — Business Continuity and Disaster Recovery Plan referenced in item c)(7).

> **Source:** NCG 502 §IV.E.4.3.2 (12-ene-2024), as amended by NCG 524 item ll (02-dic-2024).

---

## IV.E.5 — Internal-Audit Function
**NCG anchor:** N° 502, Sección IV, E.5
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, internal-audit, internal-audit-function, intermediation, custody

### Plain-English text

The internal-audit function must have persons with experience and knowledge to develop appropriately, at a minimum, the following activities:

a) Evaluate adherence to the objectives, policies, and procedures on internal-control matters of the different units or areas of the entity.

b) Evaluate the effectiveness of and compliance with the policies, procedures, and controls implemented that are conducive to the protection of its own assets and those of its clients, to the execution of orders in the interest of clients, to the detection of illicit operations, to guaranteeing information security, to the protection of the integrity of the information systems, to guaranteeing the confidential handling of information relating to its clients, to the adequate handling of conflicts of interest with clients, among others.

c) Evaluate the functioning of the body responsible for the risk-management function developed in the entity.

d) Evaluate that the financial information used for the conduct of the businesses and that used for the purposes of risk control is reliable, timely, complete, and accurate.

e) Review the organisational structure to verify the adequate segregation of functions.

f) Verify compliance with the legal and regulatory provisions applicable to the entities, their directors, and employees, as well as all internal documentation such as codes of ethics and operating manuals.

g) Monitor the timely correction of the observations arising from weaknesses or deficiencies detected on internal-control and risk-management matters.

To carry out these tasks, the internal-audit function must have an annual review plan, duly approved by the board of directors or equivalent body, and documented procedures for the development of these reviews.

The internal-audit function must report in writing to the board of directors or equivalent body on a periodic basis, at least semi-annually, on the performance of the tasks described and on compliance with its annual review plan. The internal-audit function must be independent of the operational and business areas of the entity and of the body responsible for the risk-management function, with direct reporting to the board of directors or equivalent body, and may be carried out by a natural person or internal unit or outsourced to a third party, in accordance with Section E.6 below.

Where the entity belongs to a business group, the internal-audit function may be exercised by the corporate internal-audit unit, to the extent that it has thorough knowledge of the entity's risk-management framework and control environment and complies with the requirements established in this regulation, which must be agreed by the board of directors or equivalent body. The appropriateness of the respective unit of the business group that will carry out the activity must be considered, in relation to compliance with the requirements established in this regulation and any conflicts of interest that may arise and, if applicable, their mitigation and/or elimination. For all purposes, if the internal-audit function is exercised by a corporate unit of the business group to which the company belongs, on the conditions indicated, it shall be understood that it is exercised by an internal unit.

Without prejudice to the foregoing, the entity shall always be responsible for the internal-audit function even when it is carried out by a body belonging to the business group, and must review and approve the reports produced in that regard, for which it must retain all relevant documentation.

The reports generated as a result of the annual review plan must be addressed to the board of directors or equivalent body and contain, at a minimum, the objective, the scope, the situations detected, their relative importance, and the corresponding conclusions. Likewise, they must indicate the comments of the areas that have been the subject of the review, the corrective measures to be adopted, and the estimated timeframes for that purpose.

### Original Spanish

> "E.5. FUNCIÓN DE AUDITORÍA INTERNA
>
> La función de auditoría interna deberá contar con personas con experiencia y conocimientos para desarrollar apropiadamente, al menos, las siguientes actividades:
>
> a) Evaluar la adhesión a los objetivos, políticas y procedimientos en materia de control interno de las distintas unidades o áreas de la entidad.
>
> b) Evaluar la efectividad y el cumplimiento de las políticas, procedimientos y controles implementados conducentes a la protección de activos propios y de sus clientes, a la ejecución de órdenes en el interés de los clientes, a la detección de operaciones ilícitas, a garantizar la seguridad de la información, a la protección de la integridad de los sistemas de información, a garantizar el manejo confidencial de la información relativa a sus clientes, al adecuado manejo de los conflictos de intereses con los clientes, entre otros.
>
> c) Evaluar el funcionamiento de la instancia encargada de la función de gestión de riesgos desarrollada en la entidad.
>
> d) Evaluar que la información financiera utilizada para la conducción de los negocios y aquélla utilizada para efectos de control de los riesgos, sea confiable, oportuna, completa e íntegra.
>
> e) Revisar la estructura organizacional para verificar la adecuada segregación de funciones.
>
> f) Verificar el cumplimiento de las disposiciones legales y normativas que le son aplicables a las entidades, sus directivos y empleados, como así también toda documentación interna tal como códigos de ética y manuales operativos
>
> g) Monitorear la oportuna corrección de las observaciones por falencias o deficiencias detectadas en materia de control interno y gestión de riesgo.
>
> Para llevar a cabo estas labores, la función de auditoría interna deberá contar con un plan de revisión anual, debidamente aprobado por el directorio u órgano equivalente y con procedimientos documentados para el desarrollo de estas revisiones.
>
> La función de auditoría interna deberá informar por escrito al directorio u órgano equivalente en forma periódica, al menos semestral, sobre el desempeño de las labores descritas y sobre el cumplimiento de su plan de revisión anual. La función de auditoría deberá ser independiente de las áreas operativas y de negocios de la entidad y de la instancia encargada de la función de gestión de riesgos, con reporte directo al directorio u órgano equivalente y podrá ser realizada por una persona o unidad interna o externalizada a un tercero, de acuerdo con la Sección E.6 siguiente.
>
> En el caso que la entidad pertenezca a un grupo empresarial, la función de auditoría interna podrá ser ejercida por la unidad de auditoría interna corporativa, en la medida que ésta tenga un conocimiento acabado del marco de gestión de riesgos y ambiente de control de la entidad y que cumpla con los requisitos establecidos en la presente normativa, lo cual deberá ser acordado por el directorio u órgano equivalente. Se deberá considerar la pertinencia respecto a la idoneidad de la unidad respectiva del grupo empresarial que se encargará de la actividad, en relación con el cumplimiento de los requisitos establecidos en esta norma y los conflictos de intereses que pudieran generarse y, de ser el caso, su mitigación y/o eliminación. Para todos los efectos, si la función de auditoría interna es ejercida por una unidad corporativa del grupo empresarial al que pertenece la empresa, con las condiciones señaladas, se entenderá que es ejercida por una unidad interna.
>
> Sin perjuicio de lo anterior, la entidad será la entidad será siempre responsable de la función de auditoría interna aun cuando ésta sea realizada por una instancia perteneciente al grupo empresarial, debiendo revisar y aprobar los informes realizados al respecto, para lo cual deberá hacerse de toda la documentación relevante.
>
> Los informes que se generen producto del plan de revisión anual deberán dirigirse al directorio u órgano equivalente y contener como mínimo el objetivo, el alcance, las situaciones detectadas, la importancia relativa de las mismas y las conclusiones correspondientes. Asimismo, deberán señalar los comentarios de las áreas que han sido objeto de la revisión, las medidas correctivas que se adoptarán y los plazos estimados para ello."

> **TN:** The penultimate paragraph contains "la entidad será la entidad será siempre responsable" — a duplicated subject/verb phrase in the source ("la entidad será" repeated); reproduced verbatim in the Original Spanish and rendered once ("the entity shall always be responsible") in the English.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.2.1 — risk-management function whose functioning the internal-audit function evaluates and from which it must be independent.
- NCG 502 §IV.E.6 — proportionality provisions governing how the function may be exercised, including outsourcing to a third party.

> **Source:** NCG 502 §IV.E.5 (12-ene-2024).

---

## IV.E.6 — Proportionality
**NCG anchor:** N° 502, Sección IV, E.6
**Implements:** Ley 21.521 Arts. 1 and 12 (proportionality; governance & risk management)
**Tags:** governance, risk-management, proportionality, intermediation, custody

### Plain-English text

In line with the provisions of Articles 1 and 12 of Ley N° 21.521, the entities may adapt the provisions of this Section IV.E, in accordance with their size, volume, and the nature of their businesses and risks, according to the following classification:

**Intermediation:**

a) **Block 1**: entities that do not meet any of the business-volume metrics of Block 2 or 3 entities. Active clients shall be considered to be those that meet the conditions defined in Annex N° 1 of this regulation.

b) **Block 2**: entities that meet any of the following conditions:

i) Have a number of active clients in Chile for the intermediation service between 500 and 5,000.

ii) Average daily transactions carried out in Chile in the last 12 months between UF 100,000 and UF 500,000, for the intermediation service.

iii) Income in Chile in the last 12 months between UF 25,000 and UF 50,000, for the intermediation service.

c) **Block 3**: entities that meet any of the following conditions:

i) More than 5,000 active clients in Chile for the intermediation service.

ii) More than UF 500,000 in average daily transactions carried out in Chile in the last 12 months, for the intermediation service.

iii) Income in Chile in the last 12 months over UF 50,000, for the intermediation service.

**Custody:**

a) **Block 1**: entities that do not meet any of the business-volume metrics of Block 2 or 3 entities. Active clients shall be considered to be those that meet the conditions defined in Annex N° 1 of this regulation.

b) **Block 2**: entities that meet any of the following conditions:

i) Have a number of active clients in Chile for the custody service between 1,000 and 5,000.

ii) Average daily custodied assets in Chile in the last 12 months between UF 10,000 and UF 100,000.

c) **Block 3**: entities that meet any of the following conditions:

i) More than 5,000 active clients in Chile for the custody service.

ii) Average daily custodied assets in Chile in the last 12 months, over UF 100,000.

When an entity reaches one of the conditions that classifies it in a different block for more than 6 months, it must give notice of that fact to the Commission within the following 5 business days of the occurrence of the fact and shall have a maximum period of 9 months to comply with the corporate-governance and comprehensive risk-management requirements corresponding to that block. Entities may be reclassified to lower blocks when they cease to meet the conditions of the higher block for a minimum of 6 months and with the authorisation of the Commission.

Entities that classify within Blocks 1 or 2 may develop the internal-audit function through a natural person or internal unit, or through an external third party.

In the event that the internal-audit function is carried out by an external third party, in no case may that third party exercise the external audit function for the entity, and the entity must ensure the adequate segregation of both functions.

Entities that classify within Block 3 must develop the internal-audit function through a natural person or internal unit.

For the purposes of the determination of the conditions described above, the operations in invoices that have been executed through brokers, on the product exchanges of Ley N° 19.220, and those invoices of clients that are custodied in their entirety in those brokers or in those exchanges, shall not be considered.

**Table 5. Proportionality for the provision of the intermediation and/or custody services for financial instruments**

| Block | Policies | Risk-management function | Internal-audit function |
|---|---|---|---|
| 1 | CI, OP, II, ALG, GAR, PLAFT, CUST, RO | Natural person or internal unit | Natural person or internal unit or carried out by a third party |
| 2 | CI, OP, II, ALG, GAR, PLAFT, CUST, RO | Natural person or internal unit | Natural person or internal unit or carried out by a third party |
| 3 | CI, OP, II, ALG, GAR, PLAFT, RLN, GCR, CUST, RO | Natural person or internal unit | Natural person or internal unit |

Where:

- CI: Conflicts of interest.
- OP: Offer of products consistent with the investor's needs, expectations, and risk tolerance.
- II: Information to the investor.
- ALG: Methodology for the approval, evaluation, and control of algorithms.
- GAR: Guarantees.
- PLAFT: Prevention of money laundering and financing of terrorism.
- RLN: Compliance with legal and regulatory operating requirements.
- GCR: Management of queries, complaints, and reports.
- CUST: Integrity in custody practices.
- RO: Operational risk.

### Original Spanish

> "E.6. PROPORCIONALIDAD
>
> En línea con lo establecido en los artículos 1 y 12 de la ley N°21.521, las entidades podrán adaptar las disposiciones de esta Sección IV.E, conforme a su tamaño, volumen y naturaleza de sus negocios y riesgos, de acuerdo con la siguiente clasificación:
>
> Intermediación:
>
> a) Bloque 1: entidades que no cumplan ninguna de las métricas de volumen de negocio de las entidades de los Bloques 2 o 3. Se considerarán clientes activos aquellos que cumplan con las condiciones definidas en el Anexo N°1 de esta normativa.
>
> b) Bloque 2: entidades que cumplan alguna de las siguientes condiciones:
>
> i) Tengan un número de clientes activos en Chile por el servicio de intermediación entre 500 y 5.000.
>
> ii) Transacciones promedio diarias efectuadas en Chile en los últimos 12 meses entre UF 100.000 y UF 500.000, para el servicio de intermediación.
>
> iii) Ingresos en Chile en los últimos 12 meses entre UF 25.000 y UF 50.000, por el servicio de intermediación.
>
> c) Bloque 3: entidades que cumplan alguna de las siguientes condiciones:
>
> i) Más de 5.000 clientes activos en Chile por el servicio de intermediación.
>
> ii) Más de UF 500.000 en transacciones promedio diarias efectuadas en Chile en los últimos 12 meses, para el servicio de intermediación.
>
> iii) Ingresos en Chile en los últimos 12 meses sobre UF 50.000, por el servicio de intermediación.
>
> Custodia:
>
> a) Bloque 1: entidades que no cumplan ninguna de las métricas de volumen de negocio de las entidades de los Bloques 2 o 3. Se considerarán clientes activos aquellos que cumplan con las condiciones definidas en el Anexo N°1 de esta normativa.
>
> b) Bloque 2: entidades que cumplan alguna de las siguientes condiciones
>
> i) Tengan un número de clientes activos en Chile por el servicio de custodia entre 1.000 y 5.000.
>
> ii) Activos custodiados en Chile promedio diarios en los últimos 12 meses entre UF 10.000 y UF 100.000.
>
> c) Bloque 3: entidades que cumplan alguna de las siguientes condiciones:
>
> i) Más de 5.000 clientes activos en Chile por el servicio de custodia.
>
> ii) Activos custodiados en Chile promedio diarios en los últimos 12 meses, sobre UF 100.000.
>
> Cuando una entidad alcance una de las condiciones que la clasifique en un bloque diferente por más de 6 meses deberá dar aviso de este hecho a la Comisión dentro de los próximos 5 días hábiles de ocurrido este hecho y dispondrá de un plazo máximo de 9 meses para dar cumplimiento a los requisitos de gobierno corporativo y gestión integral de riesgos correspondientes a dicho bloque. Las entidades podrán ser reclasificadas a bloques inferiores cuando dejen de cumplir las condiciones del bloque superior por un mínimo de 6 meses y con autorización de la Comisión.
>
> Las entidades que clasifiquen dentro de los Bloques 1 o 2 podrán desarrollar la función de auditoría interna por una persona o unidad interna, o por un tercero externo.
>
> En caso de que la función de auditoría interna sea realizada por un tercero externo, en ningún caso dicho tercero podrá ejercer la función de auditoría externa en la entidad, debiendo la entidad velar por la adecuada segregación de ambas funciones.
>
> Las entidades que clasifiquen dentro del Bloque 3 deberán desarrollar la función de auditoría interna por una persona o unidad interna.
>
> Para efectos de la determinación de las condiciones antes descritas, no se considerarán las operaciones en facturas que hayan sido ejecutadas a través de corredores, en las bolsas de productos de la Ley N°19.220, y de aquellas facturas de clientes que estén custodiadas en su totalidad en esas corredoras o en dichas bolsas.
>
> Tabla 5. Proporcionalidad para la prestación de los servicios de intermediación y/o custodia de instrumentos financieros.
>
> Bloque Políticas Función de gestión de riesgos Función de auditoría interna 1 CI, OP, II, ALG, GAR, PLAFT, CUST, RO Persona o unidad interna Persona o unidad interna o ser realizadas por un tercero 2 CI, OP, II, ALG, GAR, PLAFT, CUST, RO 3 CI, OP, II, ALG, GAR, PLAFT, RLN, GCR, CUST, RO Persona o unidad interna
>
> Donde,
>
> - CI: Conflictos de intereses.
>
> - OP: Oferta de productos acorde a las necesidades, expectativas y disposición al riesgo del inversionista.
>
> - II: Información al inversionista.
>
> - ALG: Metodología de aprobación, evaluación y control de algoritmos.
>
> - GAR: Garantías.
>
> - PLAFT: Prevención de lavado de activos y financiamiento del terrorismo.
>
> - RLN: Cumplimiento de requisitos legales y normativos de funcionamiento.
>
> - GCR: Gestión de consultas, reclamos y denuncias.
>
> - CUST: Integridad en las prácticas de custodia.
>
> - RO: Riesgo operacional."

> **TN:** NCG 524 item mm replaced the whole Títulos E.6 and E.7. The amended E.6 restates the proportionality classification with separate metric sets for Intermediación and Custodia (the original 12-ene-2024 E.6 used a single combined set), changes the reclassification regime (9-month compliance period plus a 5-business-day notice requirement; reclassification to lower blocks "cuando dejen de cumplir las condiciones del bloque superior"), adds the conjunction "o por un tercero externo" in the internal-audit paragraph, and adds the closing paragraph excluding factoring operations executed through brokers on the Ley N° 19.220 product exchanges. Table 5 is a structured table in the PDF source; the English rendering presents it as a Markdown table with equivalent informational content (the "Risk-management function" column is merged across all three blocks — "Persona o unidad interna" — and the "Internal-audit function" column is merged across Blocks 1 and 2 — "Persona o unidad interna o ser realizadas por un tercero"). The Original Spanish blockquote reproduces the PDF's row-first sequence for the table chunk.

### Cross-references
- Ley 21.521 Arts. 1 and 12 — proportionality and governance mandate this section implements.
- Ley N° 19.220 — law on product exchanges referenced in the closing exclusion paragraph.
- NCG 502 Annex N° 1 — conditions defining "active clients" referenced in the Block 1 definition.
- NCG 502 §IV.E.3.1 — policies (CI, OP, II, ALG, GAR, PLAFT, RLN, GCR, CUST) referenced in the table key.
- NCG 502 §IV.E.4 — operational risk (RO) referenced in the table key.
- NCG 502 §IV.E.2.1 and §IV.E.5 — risk-management and internal-audit functions subject to the block thresholds.

> **Source:** NCG 502 §IV.E.6 (12-ene-2024), as amended by NCG 524 item mm (02-dic-2024).

---

## IV.E.7 — Evaluation of the Quality of Risk Management
**NCG anchor:** N° 502, Sección IV, E.7
**Implements:** Ley 21.521 Art. 8 (governance & risk management)
**Tags:** governance, risk-management, supervisory-evaluation, intermediation, custody

### Plain-English text

The Commission will evaluate the manner in which the board of directors or equivalent body and the risk-management system comply with the provisions of the preceding sections.

The Commission will inform the entities of the result of that evaluation, with the aim that the measures necessary to strengthen the entity's governance and overall risk-management system are adopted, where necessary.

The principal elements of the evaluation process are described below:

**E.7.1. Role of the Board of Directors or Equivalent Body**

The evaluation must consider the degree of compliance with the provisions established in the preceding literal E.1 Responsibility of the Board of Directors or Equivalent Body. In particular, the action of the board of directors or equivalent body in relation to the adequate management of risks will be evaluated, including the effectiveness of the controls established, compliance with the policies and procedures established, and the organisational structure and strength of the lines of defence that it has defined for the management of risks, having regard to the nature, volume, and complexity of its activities.

Additionally, the evaluation in this matter will consider the manner in which the governance body ensures the independence in the exercise of the control function that corresponds to it. The foregoing, having regard to the complexity of the operations and risks assumed by the entity.

**E.7.2. Risk-Management System**

The evaluation must consider the degree of compliance with the provisions established in the preceding literals E.2 Risk Management, E.3 Organisation and Internal Control, E.4 Operational Risk, and E.5 Internal-Audit Function. As an input for the evaluation, the identification, evaluation, and appropriate mitigation of the risks described below will be considered, having regard to the nature, volume, and complexity of the activities it carries out:

Credit risk: refers to a potential exposure to economic losses due to non-compliance by a third party with the terms and conditions stipulated in the respective contract, agreement, or legal act. This risk is divided into the following subcategories:

- Counterparty risk: exposure to potential losses as a result of the contractual non-compliance of the counterparty in a financial transaction.

- Issuer credit risk: exposure to potential bankruptcies or deterioration of solvency in publicly offered securities or financial instruments of an entity.

Market risk: refers to a potential loss caused by changes in market prices, which could generate adverse effects on the financial situation of the own portfolio or that of third parties managed by the entity. It covers interest-rate risk, exchange-rate risk, and price risk associated with the entity's own portfolio.

Liquidity risk: exposure of the entity to a potential loss as a result of the need to obtain funds for the fulfilment of its financial commitments in an immediate manner. This risk is divided into the following subcategories:

- Funding liquidity risk: exposure to a potential loss as a result of the inability to obtain resources, secure or refinance loans at a convenient rate, or comply with the requirements of the projected cash flows.

- Market liquidity risk: exposure to a potential loss due to the inability to liquidate a financial instrument or security in portfolio without adversely affecting the price of the asset, given the shallow depth of the market for that asset.

Operational risk: corresponds to the risk that the deficiencies that may occur in the information systems, internal processes or in personnel, or the disruptions caused by external events, cause the reduction, deterioration, or interruption of the services the entity provides and eventually give rise to financial losses. It includes the areas of information security and cybersecurity, business continuity, outsourcing of services, as well as the risk of losses arising from regulatory changes affecting the entity's operations, and also losses arising from non-compliance with or lack of adherence to current regulation.

Custody risk: exposure to potential losses due to negligence, misappropriation of funds, theft, loss, or errors in the recording of transactions carried out with financial instruments of third parties held in custody.

Risk of money laundering, financing of terrorism, and financing of the proliferation of weapons of mass destruction: refers to the possibility of loss or damage that the entities may suffer due to their propensity to be used as an instrument for the channelling of resources towards the carrying out of terrorist activities or the financing of weapons of mass destruction, or when it is intended to conceal or disguise the illicit origin of goods or resources that come from criminal activities. This risk is associated with the businesses of the entities, the type of clients, and the amounts traded or custodied.

Conduct risk: refers to the risks associated with compliance with the following principles: i) fair treatment of the clients of financial entities; ii) adequate management of conflicts of interest; iii) protection of clients' information; iv) transparency in the commercialisation and advertising of financial products; and v) diligent management of complaints and submissions.

Others: other risks that the entities have identified as relevant for their operation and that are not considered in the risks defined above.

The Commission may specifically evaluate the matters it considers necessary, on the basis of the information it periodically requires from its supervised entities or any additional information it may require for the purposes of the evaluation.

To rate the matters associated with the risks previously defined, the following scale will be used:

| Risk-management rating | Meaning |
|---|---|
| Compliance | The entity complies comprehensively with the best practices and application of sound principles that characterise an adequate management. There are no appreciable deficiencies. |
| Material compliance | The entity complies significantly with the best practices and application of sound principles that characterise an adequate management. Even when some weaknesses are identified in specific processes of some function, they may be considered limited, without prejudice to which their correction must be addressed by the entity in order to reach the highest standards of risk management. |
| Unsatisfactory compliance | The entity does not comply reasonably with the best practices and application of sound principles that characterise an adequate management. Weaknesses are identified in the processes that make up various functions, among which are some relevant ones. The correction of these weaknesses must be carried out with the greatest promptness. |
| Non-compliance | The entity materially fails to comply with the best practices and application of sound principles that characterise an adequate management. The solution of its weaknesses is considered indispensable. |

**E.7.3. Global Rating of the Quality of Risk Management**

As a result of the evaluation process of one or more risks as regards the role of the board of directors and the risk-management system, this Commission will determine the global rating of the quality of the risk management of the evaluated entity on the basis of the following evaluation scale:

| Global rating of the quality of risk management | Meaning |
|---|---|
| A | The entity complies satisfactorily with high standards of risk management, for which reason it does not present the characteristics of levels B, C, or D. |
| B | Entity that, in the supervision process or in the process of monitoring its information, reflects weaknesses related to the matters defined in the applicable regulation, especially in its corporate governance, internal controls, quality of the information reported, information systems for decision-making, timely follow-up of the various risks, and capacity to face contingency scenarios, but that these do not expose it to significant risks. |
| C | Entity that in the supervision process or in the process of monitoring its information presents significant deficiencies in any of the factors indicated in the preceding classification, the correction of which must be carried out promptly in order to avoid an impairment to it. |
| D | Entity that presents serious weaknesses in the management of any of the risks evaluated or that presents regulatory non-compliances of relevance, the correction of which must be carried out immediately in order to avoid a relevant impairment to its stability or to the interests of clients. |

In the case of the entities belonging to Blocks 1 and 2, in accordance with the considerations of literal E.6 Proportionality, ratings C and D may determine the requirement of corporate-governance and risk-management requirements corresponding to Block 3. In that case, the entity shall have a maximum period of 9 months from the communication by the Commission of the rating assigned, to comply with those additional requirements.

The foregoing is without prejudice to the requirements of capital or guarantees that may be required for the entity on the basis of its global rating, in accordance with Section V of this regulation.

### Original Spanish

> "E.7. EVALUACIÓN DE LA CALIDAD DE GESTIÓN DE RIESGOS
>
> La Comisión evaluará la forma en que el directorio u órgano equivalente y el sistema de gestión de riesgos cumplen con lo dispuesto en las secciones precedentes.
>
> La Comisión informará a las entidades respecto al resultado de dicha evaluación, con el objeto de que se adopten las medidas necesarias para fortalecer la gobernanza y el sistema global de gestión de riesgos de la entidad, en caso de ser necesario.
>
> A continuación, se describen los principales elementos del proceso de evaluación:
>
> E.7.1. ROL DEL DIRECTORIO U ÓRGANO EQUIVALENTE
>
> La evaluación deberá considerar el grado de cumplimiento de las disposiciones establecidas en el literal E.1 RESPONSABILIDAD DEL DIRECTORIO U ÓRGANO EQUIVALENTE precedente. En particular, se evaluará la actuación del directorio u órgano equivalente en relación a la adecuada gestión de los riesgos, incluyendo la efectividad de los controles establecidos, el cumplimiento de las políticas y procedimientos establecidos, y la estructura organizacional y fortaleza de las líneas de defensa que haya definido para la gestión de los riesgos, atendiendo a la naturaleza, volumen y complejidad de sus actividades.
>
> Adicionalmente, la evaluación en esta materia considerará la forma en que la instancia de gobierno asegure la independencia en el ejercicio de la función de control que le corresponde. Lo anterior, en atención a la complejidad de las operaciones y riesgos que asume la entidad.
>
> E.7.2. SISTEMA DE GESTIÓN DE RIESGOS
>
> La evaluación deberá considerar el grado de cumplimiento de las disposiciones establecidas en los literales E.2. GESTIÓN DE RIESGOS, E.3 ORGANIZACIÓN Y CONTROL INTERNO, E.4. RIESGO OPERACIONAL y E.5 FUNCION DE AUDITORIA INTERNA precedentes. Como insumo para la evaluación, se considerará la identificación, evaluación y mitigación apropiada de los riesgos que se describen a continuación, en atención a la naturaleza, volumen y complejidad de las actividades que realiza:
>
> Riesgo de crédito: se refiere a una potencial exposición a pérdidas económicas debido al incumplimiento por parte de un tercero de los términos y las condiciones estipuladas en el respectivo contrato, convención o acto jurídico. Este riesgo se divide en las siguientes subcategorías:
>
> • Riesgo de contraparte: exposición a potenciales pérdidas como resultado del incumplimiento contractual de la contraparte en una transacción financiera.
>
> • Riesgo crediticio del emisor: exposición a potenciales quiebras o deterioro de solvencia en los valores de oferta pública o instrumentos financieros de una entidad.
>
> Riesgo de mercado: se refiere a una potencial pérdida causada por cambios en los precios del mercado, que podría generar efectos adversos en la situación financiera de la cartera propia o de terceros que maneja la entidad. Abarca el riesgo de tasas de interés, el riesgo cambiario y el riesgo de precios asociados a la cartera propia de la entidad.
>
> Riesgo de liquidez: exposición de la entidad a una potencial pérdida como resultado de la necesidad de obtener fondos para el cumplimiento de sus compromisos financieros de manera inmediata. Este riesgo se divide en las siguientes subcategorías:
>
> • Riesgo de liquidez de financiamiento: exposición a una pérdida potencial como resultado de la incapacidad de obtener recursos, conseguir o refundir préstamos a una tasa conveniente o cumplir con las exigencias de los flujos de caja proyectados.
>
> • Riesgo de liquidez de mercado: exposición a una pérdida potencial debido a la incapacidad de liquidar un instrumento financiero o valor en cartera sin afectar de manera adversa el precio del activo, dada la escasa profundidad del mercado de ese activo.
>
> Riesgo operacional: corresponde al riesgo de que las deficiencias que puedan producirse en los sistemas de información, los procesos internos o en el personal, o las perturbaciones ocasionadas por acontecimientos externos, provoquen la reducción, el deterioro o la interrupción de los servicios que presta la entidad y eventualmente le originen pérdidas financieras. Incluye los ámbitos de seguridad de la información y ciberseguridad, continuidad de negocio, externalización de servicios, así como el riesgo de pérdidas ante cambios regulatorios que afecten las operaciones de la entidad, como también pérdidas derivadas de incumplimiento o falta de apego a la regulación vigente.
>
> Riesgo de custodia: exposición a pérdidas potenciales debido a negligencia, malversación de fondos, robo, pérdida o errores en el registro de transacciones efectuadas con instrumentos financieros de terceros mantenidos en custodia.
>
> Riesgo de lavado de activos, financiamiento del terrorismo y financiamiento de la proliferación de armas de destrucción masiva: se refiere a la posibilidad de pérdida o daño que pueden sufrir las entidades por su propensión a ser utilizadas como instrumento para la canalización de recursos hacia la realización de actividades terroristas o financiamiento de armas de destrucción masiva, o cuando se pretende ocultar o disfrazar el origen ilícito de bienes o recursos que provienen de actividades delictivas. Este riesgo está asociado a los negocios de las entidades, el tipo de clientes, y los montos transados o custodiados.
>
> Riesgo de conducta: se refiere a los riesgos asociados al cumplimiento de los siguientes principios: i) trato justo a los clientes de entidades financieras; ii) adecuada gestión de conflictos de intereses; iii) protección de la información de los clientes; iv) transparencia en la comercialización y publicidad de productos financieros; y v) gestión diligente de reclamos y presentaciones.
>
> Otros: otros riesgos que las entidades hayan identificado como relevantes para su operación y que no estén considerados en los riesgos definidos anteriormente.
>
> La Comisión podrá evaluar específicamente las materias que estime necesarias, sobre la base de la información que periódicamente requiere a sus fiscalizados o aquella adicional que pudiera requerir para efectos de la evaluación.
>
> Para calificar las materias asociadas a los riesgos previamente definidos se utilizará la siguiente escala:
>
> Calificación de la gestión del riesgo | Significado
> Cumplimiento | La entidad cumple integralmente con las mejores prácticas y aplicación de sanos principios que caracterizan una adecuada gestión. No existen deficiencias apreciables.
> Cumplimiento material | La entidad cumple en forma significativa con las mejores prácticas y aplicación de sanos principios que caracterizan una adecuada gestión. Aun cuando se identifican algunas debilidades en procesos específicos de alguna función, ellas se pueden considerar acotadas, sin perjuicio de lo cual su corrección debe ser atendida por la entidad a objeto de alcanzar los más altos estándares de gestión de riesgos.
> Cumplimiento insatisfactorio | La entidad no cumple en forma razonable con las mejores prácticas y aplicación de sanos principios que caracterizan una adecuada gestión. Se identifican debilidades en los procesos que componen diversas funciones, entre las que se encuentran algunas relevantes. La corrección de estas debilidades debe ser efectuada con la mayor prontitud.
> Incumplimiento | La entidad incumple materialmente con las mejores prácticas y aplicación de sanos principios que caracterizan una adecuada gestión. La solución de sus debilidades se considera indispensable.
>
> E.7.3. CALIFICACIÓN GLOBAL DE LA CALIDAD DE GESTIÓN DE RIESGOS
>
> Como resultado del proceso de evaluación de uno o más riesgos en cuanto al rol del directorio y del sistema de gestión de riesgos, esta Comisión determinará la calificación global de la calidad de la gestión de riesgos de la entidad evaluada a partir de la siguiente escala de evaluación:
>
> Calificación global de la calidad de gestión de riesgos | Significado
> A | La entidad cumple satisfactoriamente con altos estándares de gestión de riesgos, por lo que no presenta las características de los niveles B, C o D.
> B | Entidad que en el proceso de supervisión o que, en el proceso de monitoreo de su información, refleja debilidades relacionadas con las materias definidas en la normativa aplicable, especialmente en su gobierno corporativo, controles internos, calidad de la información reportada, sistemas de información para la toma de decisiones, seguimiento oportuno de los distintos riesgos, y capacidad para enfrentar escenarios de contingencia, pero que éstas no la exponen a riesgos significativos.
> C | Entidad que en el proceso de supervisión o que en el proceso de monitoreo de su información presente deficiencias significativas en alguno de los factores señalados en la clasificación anterior, cuya corrección debe ser efectuada con prontitud para evitarle un menoscabo.
> D | Entidad que presente debilidades graves en la gestión de alguno de los riesgos evaluados o que presente incumplimientos normativos de relevancia, cuya corrección debe ser efectuada de inmediato para evitar un menoscabo relevante en su estabilidad o en los intereses de los clientes.
>
> En el caso de las entidades pertenecientes a los Bloques 1 y 2, de acuerdo a las consideraciones del literal E.6. PROPORCIONALIDAD, las calificaciones C y D podrán determinar la exigencia de requisitos de gobierno corporativo y gestión de riesgos correspondientes al Bloque 3. En tal caso, la entidad dispondrá de un plazo máximo de 9 meses desde la comunicación por parte de la Comisión de la calificación asignada, para dar cumplimiento a estos requisitos adicionales.
>
> Lo anterior, es sin perjuicio de los requisitos de patrimonio o garantías que puedan ser requeridos para la entidad en base a su calificación global, según la sección V de esta normativa."

> **TN:** NCG 524 item mm replaced the original §IV.E.7 "OTRAS DISPOSICIONES" (a single paragraph on agreed-upon procedures reports) with the new §IV.E.7 "EVALUACIÓN DE LA CALIDAD DE GESTIÓN DE RIESGOS", which in the source PDF is subdivided into three headed parts: E.7.1 (Rol del Directorio u Órgano Equivalente), E.7.2 (Sistema de Gestión de Riesgos), and E.7.3 (Calificación Global de la Calidad de Gestión de Riesgos). The regulation's contracted anchor set for this file has no separate E.7.1/E.7.2/E.7.3 anchors; the three parts are reproduced verbatim within this single E.7 parent block. The two rating tables (risk-management rating scale and global-rating scale) are structured tables in the PDF; the English rendering presents them as Markdown tables and the Original Spanish blockquote reproduces them as row-wise "header | header" / "row | row" sequences.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate this section implements.
- NCG 502 §IV.E.1 — Responsibility of the Board (basis for the E.7.1 evaluation).
- NCG 502 §IV.E.2, §IV.E.3, §IV.E.4, §IV.E.5 — risk-management system provisions whose compliance is evaluated under E.7.2.
- NCG 502 §IV.E.6 — proportionality classification referenced in the E.7.3 escalation of Block 1 and 2 entities rated C or D.
- NCG 502 §V — capital and guarantees requirements referenced in the closing paragraph.

> **Source:** NCG 502 §IV.E.7 (12-ene-2024), as amended by NCG 524 item mm (02-dic-2024).

---

## IV.E.8 — Reporting of Operational Incidents
**NCG anchor:** N° 502, Sección IV, E.8
**Implements:** Ley 21.521 Art. 8 (governance & risk management; operational incident reporting)
**Tags:** governance, risk-management, operational-incidents, intermediation, custody

### Plain-English text

This subsection establishes the obligations relating to the recording and communication of operational incidents (E.8.1) and operational losses (E.8.2).

### Original Spanish

> "E.8. INFORMACIÓN DE INCIDENTES OPERACIONALES"

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate; operational incident reporting is part of the entity's risk-management obligations.
- NCG 502 §IV.E.8.1 — recording and communication of operational incidents.
- NCG 502 §IV.E.8.2 — recording and communication of operational losses.
- NCG 502 Annex N° 2 — Operational Incident Report (RIO) form.
- NCG 502 Annex N° 3 — operational-loss reporting instructions.

> **Source:** NCG 502 §IV.E.8 (12-ene-2024).

---

## IV.E.8.1 — Recording and Communication of Operational Incidents
**NCG anchor:** N° 502, Sección IV, E.8.1
**Implements:** Ley 21.521 Art. 8 (governance & risk management; operational incident reporting)
**Tags:** governance, risk-management, operational-incidents, information-security, intermediation, custody

### Plain-English text

a) Intermediaries and custodians of financial instruments belonging to Block 3 must communicate to this Commission the operational incidents that affect the continuity of the business, the resources and information of the entity or its clients, and the quality of the services. By way of example, and without being exhaustive or limiting, the following must be reported: failures in services important for business operations; technological problems affecting information security; cyberspace attacks; viruses or malware detected in critical information assets; events of unavailability or interruption of any service or product affecting clients, on any channel; losses or leakage of information of the entity or of clients; incidents affecting the entity's assets resulting from internal or external fraud; problems affecting the continuity of critical service suppliers; among others. This information must be maintained by the entity in an incident database and another operational-loss database for the continuous improvement of the operational risk-management process.

b) The occurrence of an operational incident of those mentioned in the preceding numeral must be reported to this Commission within a maximum period of 2 hours elapsed from the time the entity became aware of the event. The period indicated is solely for the purpose of notifying the Commission of the occurrence of the incident with the information available at that time and does not imply that the entity must have resolved the problem, taken specific actions, or clarified the causes of the incident, which may be the subject of follow-up reports on the incident sent to the CMF subsequently. The instructions for reporting operational incidents to this Commission are found in Annex N° 2 of this regulation.

c) For these purposes, the board of directors or equivalent body must designate an officer in charge and an alternate for the preparation of reports and the sending of information in accordance with what is indicated in this section. Both persons must have an executive level and be designated by the entity, both for this purpose and to respond to any queries on the part of this Commission.

d) Likewise, in cases where this Commission considers it necessary, it may require the entity to prepare an internal report containing at least: the analysis of the causes of the incident; the generation of documentation and investigation reports; an analysis of the impact generated on the services; and the procedure to prevent, with a high degree of certainty, its recurrence; and the additional matters that this Commission may require.

e) Without prejudice to the foregoing, the entity must keep the board of directors or equivalent body informed in a timely manner about the updates of all relevant operational incidents and the measures adopted to resolve them.

### Original Spanish

> "E.8.1. REGISTRO Y COMUNICACIÓN DE INCIDENTES OPERACIONALES
>
> a) Los intermediarios y custodios de instrumentos financieros, pertenecientes al Bloque 3, deberán comunicar a esta Comisión los incidentes operacionales que afecten la continuidad del negocio, los recursos e información de la entidad o de sus clientes y la calidad de los servicios. A modo de ejemplo, y sin el objeto de ser exhaustivos ni taxativos, deberán ser reportadas las fallas en servicios importantes para las operaciones del negocio; problemas tecnológicos que afecten la seguridad de la información; ataques del ciberespacio; virus o malware detectados en los activos de información críticos; eventos de indisponibilidad o interrupción de algún servicio o producto que afecte a los clientes, en cualquier canal; pérdidas o fugas de información de la entidad o de clientes; los incidentes que afecten el patrimonio de la entidad producto de fraudes internos o externos; problemas que afecten la continuidad de proveedores de servicios críticos; entre otros. Esta información deberá ser mantenida por la entidad en una base de datos de incidentes y otra base de datos de pérdidas operacionales para el mejoramiento continuo del proceso de gestión de riesgo operacional.
>
> b) La ocurrencia de un incidente operacional de aquéllos mencionados en el numeral anterior deberá ser informada a esta Comisión en un plazo máximo de 2 horas transcurridas desde que la entidad tomó conocimiento del hecho. El plazo señalado es solo para efectos de notificar a la Comisión de la ocurrencia del incidente con la información disponible en ese momento y no implica que la entidad deba tener resuelto el problema, haber tomado determinadas acciones o tener aclarada las causas del incidente, lo que podría ser materia de reportes de seguimiento del incidente enviados la CMF, posteriormente. Las instrucciones para reportar los incidentes operacionales a esta Comisión se encuentran en el Anexo N° 2 de esta normativa.
>
> c) Para estos efectos, el directorio u órgano equivalente deberá definir un funcionario encargado y un suplente para la realización de reportes y envío de información según lo indicado en esta sección. Ambas personas deberán tener un nivel ejecutivo y ser designados por la entidad, tanto para este efecto como para responder eventuales consultas por parte de esta Comisión.
>
> d) Asimismo, en los casos en que esta Comisión lo estime necesario, podrá requerir a la entidad la elaboración de un informe interno que contenga al menos: el análisis de las causas del incidente; la generación de documentación e informes de investigación; un análisis del impacto generado en los servicios; y el procedimiento para evitar con alto grado de seguridad que se vuelva a presentar; y las materias adicionales que esta Comisión pueda requerir.
>
> e) Sin perjuicio de lo anterior, la entidad deberá mantener informado en forma oportuna al directorio u órgano equivalente sobre las actualizaciones de todos los incidentes operacionales relevantes y las medidas adoptadas para resolverlo."

> **TN:** In the original 12-ene-2024 text, item b) read "en un plazo máximo de 2 horas desde que la entidad tomó" — omitting the object of "tomó". NCG 524 item nn replaced that expression with "2 horas transcurridas desde que la entidad tomó conocimiento del hecho", as reflected here. Separately, "enviados la CMF" omits a preposition ("enviados a la CMF"); rendered idiomatically as "sent to the CMF".

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate; operational incident reporting is part of the entity's risk-management obligations.
- NCG 502 Annex N° 2 — instructions for reporting operational incidents (RIO) referenced in item b).
- NCG 502 §IV.E.6 — proportionality classification defining the Block 3 entities subject to this reporting obligation.
- NCG 502 §IV.E.4.1 — information-security and cybersecurity guidelines whose breach events are typical triggers for reporting.

> **Source:** NCG 502 §IV.E.8.1 (12-ene-2024), as amended by NCG 524 item nn (02-dic-2024).

---

## IV.E.8.2 — Recording and Communication of Operational Losses
**NCG anchor:** N° 502, Sección IV, E.8.2
**Implements:** Ley 21.521 Art. 8 (governance & risk management; operational loss reporting)
**Tags:** governance, risk-management, operational-losses, intermediation, custody

### Plain-English text

a) An operational loss is understood to be any financial loss resulting from the materialisation of operational risk in accordance with what was defined above. This includes financial losses due to legal or regulatory changes affecting the entity's operations, or resulting from non-compliance with current regulation.

b) The information on all incidents that materialise individually in operational losses greater than 150 Unidades de Fomento must be sent to this Commission in accordance with the instructions of Annex N° 3 of this regulation, 15 business days after the close of June and December of each year.

c) The criteria for the preparation of the operational-loss register are the following:

1) The entity must have documented processes and procedures for the identification, collection, use, and communication of the operational-loss records. This Commission may require that compliance with such requirements be validated through a pronouncement issued by external audit firms, among those registered in the Registry of External Audit Firms of this Commission, that have units specialised in the evaluation of operational risk-management procedures and mechanisms, with experience of no less than 5 years in those matters.

2) The entity's internal records on operational losses must be comprehensive and include all the relevant activities and exposures, in all systems and in all relevant geographic locations.

3) The entity must collect information on the gross amounts of the losses, and on the reference dates of the operational-risk events. In addition, the entity must collect information on recoveries of gross amounts of losses, and descriptive information on the determining factors or the causes of the loss event. The degree of detail of the descriptive information must be in proportion to the gross amount of the loss.

4) The entity must use the accounting date of the event to construct the set of loss records. In the case of legal events, the accounting date refers to when a provision for this legal contingency is constituted in the statement of financial position, with the corresponding reflection in the income statement.

5) Losses caused by a common operational-risk event or by several related operational-risk events over time, but recorded over the course of several years, must be assigned to the corresponding years in the loss database, consistent with their accounting treatment.

d) Gross loss is understood to be a loss before recoveries of any type.

1) The following items must be included in the calculations of the gross losses for the loss database:

i) Direct charges in the entity's Income Statement accounts and amortisations due to operational-risk events of the period. For example, costs incurred as a consequence of an event, including external expenses with a direct relationship to the operational-risk event (e.g., legal expenses directly related to the event and commissions paid to advisers, lawyers, or suppliers) and repair or replacement costs incurred to restore the position that prevailed before the operational-risk event.

ii) Direct charges in the entity's Income Statement accounts and amortisations due to operational-risk events of previous accounting periods that affect the entity's financial statements in the present period.

2) The following items must be excluded from the gross losses recorded in the loss database:

i) Costs for general maintenance contracts of property, plant, or equipment.

ii) Internal or external expenses with the aim of improving the business after the losses due to operational risk: updates, improvements, risk-management initiatives, and improvements thereto.

iii) Insurance premiums.

e) Net loss is understood to be the loss after taking into account the effects of recoveries. The recovery is an independent event, related to the initial loss event, that is not necessarily carried out in the same period in which the respective funds are received.

The entity must be able to identify recoveries not arising from insurance and recoveries originating from the payment of insurance indemnities for all operational-loss events. Likewise, it must use the net losses of recoveries (including those arising from insurance) in the set of operational-loss records, although recoveries may only be used to reduce the losses when the payment has been received.

Entities classified in Blocks 1 and 2 are exempt from the operational-loss report referred to in Annex N° 3 of this regulation.

### Original Spanish

> "E.8.2. REGISTRO Y COMUNICACIÓN DE PÉRDIDAS OPERACIONALES
>
> a) Se entiende por pérdida operacional toda pérdida financiera resultante de la materialización del riesgo operacional de acuerdo con lo definido anteriormente. Esto incluye las pérdidas financieras debido a cambios legales o regulatorios que afecten las operaciones de la entidad, o producto de incumplimientos con la regulación vigente.
>
> b) La información de todos los incidentes que se materialicen individualmente en pérdidas operacionales mayores a 150 Unidades de Fomento deberá ser enviada a esta Comisión de acuerdo con las instrucciones del Anexo N° 3 de la presente norma, 15 días hábiles después del cierre de junio y diciembre de cada año.
>
> c) Los criterios para la confección del registro de pérdidas operacionales son los siguientes:
>
> 1) La entidad deberá contar con procesos y procedimientos documentados para la identificación, recopilación, uso y comunicación de los registros de pérdida operacional. Esta Comisión podrá exigir que el cumplimiento de tales requisitos sea validado a través de un pronunciamiento emitido por empresas de auditoría externa, de aquellos inscritos en el Registro de Empresas de Auditoría Externa de esta Comisión, que cuenten con unidades especializadas en la evaluación de procedimientos y mecanismos de gestión de riesgo operacional, con una experiencia no inferior a 5 años en dichas materias.
>
> 2) Los registros internos sobre pérdidas operacionales de la entidad deberán ser integrales e incluir la totalidad de las actividades y exposiciones relevantes, en todos los sistemas y en todas las ubicaciones geográficas pertinentes.
>
> 3) La entidad deberá recopilar información sobre los importes brutos de las pérdidas, y sobre las fechas de referencia de los eventos de riesgo operacional. Además, la entidad deberá recoger información sobre recuperaciones de importes brutos de pérdidas, e información descriptiva sobre los factores determinantes o las causas del evento de pérdida. El grado de detalle de la información descriptiva deberá estar en proporción al importe bruto de la pérdida.
>
> 4) La entidad deberá utilizar la fecha de contabilización del evento para construir el conjunto de registros sobre pérdidas. En el caso de eventos legales, la fecha de contabilización se refiere a cuando se constituye una provisión para esta contingencia legal en el estado de situación financiera, con su reflejo correspondiente en el estado de resultados.
>
> 5) Las pérdidas causadas por un evento de riesgo operacional común o por varios eventos de riesgo operacional relacionados a lo largo del tiempo, pero contabilizadas en el transcurso de varios años, deberán asignarse a los años correspondientes en la base de datos de pérdidas, en consonancia con su tratamiento contable.
>
> d) Por pérdida bruta se entiende una pérdida antes de recuperaciones de cualquier tipo.
>
> 1) Los siguientes ítems deben ser incluidos en los cálculos de las pérdidas brutas para la base de datos de pérdidas:
>
> i) Cargos directos en las cuentas de Estados de Resultados de la entidad y amortizaciones debido a eventos de riesgo operacional del período. Por ej. Costos incurridos como consecuencia de un evento, incluyendo gastos externos con una relación directa al evento por riesgo operacional (ej. Gastos legales directamente relacionados al evento y comisiones pagadas a los asesores, abogados o proveedores) y costos de reparación o reemplazo incurridos para restaurar la posición que prevalecía antes del evento de riesgo operacional.
>
> ii) Cargos directos en las cuentas de Estados de Resultados de la entidad y amortizaciones debido a eventos por riesgo operacional de ejercicios contables previos que afecten los estados financieros de la entidad en el presente período.
>
> 2) Los siguientes ítems deben ser excluidos de las pérdidas brutas registradas en la base de datos de pérdidas:
>
> i) Costos por contratos de mantenimientos generales de la propiedad, planta o equipos.
>
> ii) Gastos internos o externos con el fin de mejorar el negocio después de las pérdidas por riesgo operacional: actualizaciones, mejoras, iniciativas de gestión del riesgo y mejoras en ellas.
>
> iii) Primas de seguro.
>
> e) Por pérdida neta se entiende la pérdida después de tener en consideración los efectos de las recuperaciones. La recuperación es un hecho independiente, relacionado con el evento de pérdida inicial, que no necesariamente se efectúa en el mismo periodo en el que se perciben los fondos respectivos.
>
> La entidad deberá ser capaz de identificar las recuperaciones no procedentes de seguros y las recuperaciones originadas por el pago de indemnizaciones de seguros para todos los eventos de pérdidas operacionales. Asimismo, deberá utilizar las pérdidas netas de recuperaciones (incluidas las procedentes de seguros) en el conjunto de registros sobre pérdidas operacionales, aunque las recuperaciones sólo podrán utilizarse para reducir las pérdidas cuando se haya recibido el pago.
>
> Las entidades clasificadas en los Bloques 1 y 2 quedan eximidas del reporte de pérdidas operacionales al que se refiere el Anexo N°3 de la presente normativa."

> **TN:** "Unidades de Fomento" (UF) is Chile's inflation-indexed accounting unit; retained as "Unidades de Fomento" / "UF" per source.

### Cross-references
- Ley 21.521 Art. 8 — governance and risk-management mandate; operational loss reporting is part of the entity's risk-management obligations.
- NCG 502 Annex N° 3 — instructions for reporting operational losses referenced in items b) and e).
- NCG 502 §IV.E.6 — proportionality classification exempting Blocks 1 and 2 from operational-loss reporting.
- NCG 502 §IV.E.8.1 — operational-incident reporting that feeds the incident and operational-loss databases.

> **Source:** NCG 502 §IV.E.8.2 (12-ene-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/seccion-05-capital-garantias.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/seccion-05-capital-garantias.md

# NCG 502 — Sección V: Capital and Guarantees (Capital y Garantías)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

---

## V — Capital and Guarantees
**NCG anchor:** N° 502, Sección V
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, guarantees, minimum-equity, risk-weighted-assets

### Plain-English text

This Section establishes the minimum-equity and guarantee requirements for entities that provide the services of intermediation of financial instruments and custody of financial instruments, as well as guarantee requirements for entities that provide the order-routing service, in accordance with Articles 7, 10, and 11 of Ley N° 21.521.

> **TN:** "patrimonio" is rendered throughout as "equity" in the sense of regulatory equity / net worth (the entity's own funds available to meet regulatory capital requirements), not share capital alone.

### Original Spanish

> "V. CAPITAL Y GARANTÍAS
>
> En esta sección se establecen los requisitos de patrimonio mínimo y garantías para las entidades que presten los servicios de intermediación de instrumentos financieros y custodia de instrumentos financieros, así como requisitos de garantías a las entidades que presten el servicio de enrutamiento de órdenes, conforme lo establecido en los artículos 7, 10 y 11 de la Ley N°21.521."

### Cross-references
- Ley 21.521 Arts. 7, 10, 11 — service-accumulation rule and capital/guarantee requirements this Section implements.
- NCG 502 §V.A to §V.D — classification, minimum-equity/guarantee requirements, adjusted equity, and risk-weighting methodology developed in this Section.

> **Source:** NCG 502 §V (12-ene-2024).

---

## V.A — Classification According to Business Volume
**NCG anchor:** N° 502, Sección V, A
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, guarantees, business-volume, classification, blocks

### Plain-English text

Three blocks of entities are defined according to their business volume, with the aim of establishing proportional minimum-equity and guarantee requirements for each of them.

a) Block 1: entities that have a number of active clients below 500, and that do not meet any of the business-volume metrics of the Block 2 or 3 entities. Active clients are considered to be those that meet the conditions defined in Annex N° 1 of this regulation.

b) Block 2: entities that meet any of the following conditions:

i) Have a number of active clients between 500 and 5,000.

ii) Average daily transactions over the last three months (moving average) between UF 100,000 and UF 500,000.

iii) Average daily assets in custody over the last three months (moving average) between UF 20,000 and UF 100,000.

iv) Revenue over the last 12 months (moving average) between UF 25,000 and UF 50,000.

c) Block 3: entities that meet any of the following conditions:

i) More than 5,000 active clients.

ii) More than UF 500,000 in average daily transactions over the last three months (moving average).

iii) Average daily assets in custody over the last three months (moving average) above UF 100,000.

iv) Revenue over the last 12 months (moving average) above UF 50,000.

In the event that the entity is reclassified to a higher block, it shall have a maximum period of 6 months to comply with the minimum-equity and guarantee requirements corresponding to that block.

Entities may be reclassified to lower blocks after a minimum of 6 months and with the authorisation of the Commission (CMF).

### Original Spanish

> "A. CLASIFICACIÓN DE ACUERDO CON EL VOLUMEN DE NEGOCIOS
>
> Se definen tres bloques de entidades de acuerdo con su volumen de negocios, con el objetivo de establecer requisitos de patrimonio mínimo y garantías proporcionales para cada una de ellas.
>
> a) Bloque 1: entidades que tengan un número de clientes activos menor a 500, y no cumplan ninguna de las métricas de volumen de negocio de las entidades del Bloque 2 o 3. Se considerarán clientes activos aquellos que cumplan con las condiciones definidas en el Anexo N°1 de esta normativa.
>
> b) Bloque 2: entidades que cumplan alguna de las siguientes condiciones:
>
> i) Tengan un número de clientes activos entre 500 y 5.000.
>
> ii) Transacciones promedio diarias en los últimos tres meses (media móvil) entre UF 100.000 y UF 500.000.
>
> iii) Activos custodiados promedio diarios en los últimos tres meses (media móvil) entre UF 20.000 y UF 100.000.
>
> iv) Ingresos en los últimos 12 meses (media móvil) entre UF 25.000 y UF 50.000.
>
> c) Bloque 3: entidades que cumplan alguna de las siguientes condiciones:
>
> i) Más de 5.000 clientes activos.
>
> ii) Más de UF 500.000 en transacciones promedio diarias en los últimos tres meses (media móvil).
>
> iii) Activos custodiados promedio diarios en los últimos tres meses (media móvil) sobre UF 100.000.
>
> iv) Ingresos en los últimos 12 meses (media móvil) sobre UF 50.000.
>
> En caso de que la entidad sea reclasificada a un bloque superior, dispondrá de un plazo máximo de 6 meses para dar cumplimiento a los requisitos de patrimonio mínimo y garantías correspondiente a dicho bloque.
>
> Las entidades podrán ser reclasificadas a bloques inferiores después de un mínimo de 6 meses y con autorización de la Comisión."

### Cross-references
- Ley 21.521 Art. 11 — capital/guarantee requirements that the block classification calibrates.
- NCG 502 Anexo N° 1 — definition of "active clients" referenced in item a).
- NCG 502 §V.B — minimum-equity and guarantee requirements assigned to each block.

> **Source:** NCG 502 §V.A (12-ene-2024).

---

## V.B — Minimum-Equity and Guarantee Requirement
**NCG anchor:** N° 502, Sección V, B
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, guarantees, minimum-equity, insurance-policy, bank-guarantee

### Plain-English text

In accordance with Article 7 of the Fintech Law, in the event that an entity provides simultaneously two or more of the services covered by this regulation, it must demonstrate that it complies with each and every one of the requirements applicable to each of the services, without this implying the need to accumulate compliance with the minimum-equity and guarantee requirements of Articles 10 and 11. Accordingly:

a) Block 1 entities that provide the services of intermediation of financial instruments, custody of financial instruments, or order routing are exempt from minimum-equity and guarantee requirements.

b) Block 2 entities that provide the services of intermediation and/or custody of financial instruments must permanently maintain adjusted equity and/or guarantees equal to or greater than UF 1,000, in accordance with the calculation methodology set out in Section C. If the entity described also provides the order-routing service, it shall not additionally comply with the UF 500 guarantee requirement described below.

c) Block 3 entities that provide the services of intermediation and/or custody of financial instruments must permanently maintain adjusted equity and/or guarantees equal to or greater than the higher of:

1) UF 5,000.

2) 3% (or up to 6%) of the entity's risk-weighted assets for financial and operational risk, in accordance with the provisions of letter D below.

d) The equity requirements for financial risks (market and credit) shall be met exclusively by means of adjusted equity. The equity requirement for operational risk may be met by adjusted equity and/or guarantees.

e) Block 2 or 3 entities that provide the order-routing service must permanently maintain adjusted equity and/or guarantees equal to or greater than UF 500.

f) Block 3 entities that provide the services of intermediation and/or custody of financial instruments that meet the requirements mentioned in subparagraph c), and that also provide the order-routing service, shall not additionally comply with the UF 500 guarantee requirement.

g) The entity may constitute a guarantee by means of an insurance policy or bank-guarantee certificate (boleta de garantía bancaria) for compliance with the requirements established in this regulation.

1) In the case of the insurance policy, it must cover the damages and losses caused to third parties for which the entity is civilly liable, resulting from the provision of the services proper to the intermediation of financial instruments, order routing, or custody of financial instruments, for acts, errors, or omissions occurring during the term of the policy and affecting third parties professionally served by the insured. It must likewise cover the civil liability of its dependents, of its administrators, representatives, attorneys-in-fact, or of any person who participates in the advisory functions on its account, and in general, that of any person for which it is civilly liable in the exercise of the activity of intermediation of financial instruments, order routing, or custody of financial instruments. The coverage must comprise both the damages and losses caused to third parties and the costs and expenses of the proceedings that these third parties or their successors-in-title bring against the insured.

The expenses of the insured's defence, including the respective fees, must also be borne by the insurance company, even where the claims are unfounded.

Finally, the insurance must state that the payment of the indemnity to the injured third party will be made by virtue of a final enforceable judgment, or of a judicial or extrajudicial settlement entered into by the insured with the consent of the company.

2) In the case where the guarantee is constituted by means of a bank-guarantee certificate, it must be taken out at a bank authorised to operate in the national market. The document must state that it is taken out in favour of the beneficiaries of the guarantee — that is, the present or future creditors that the entity may come to have by reason of its operations of intermediation of financial instruments, order routing, or custody of financial instruments — and for the exclusive purpose of being used under the terms of Ley N° 21.521, and that it is payable on demand.

The amount of the bank-guarantee certificate shall be that determined by application of the provisions of this regulation.

The entity must designate a bank as representative of the possible beneficiaries of the bank-guarantee certificate, which shall be the holder thereof.

The representative of the beneficiaries of the bank-guarantee certificate, in order to enforce it and without it being necessary to prove this to the issuing entity, must be judicially notified of the fact that a lawsuit has been filed against the guaranteed entity.

The bank-guarantee certificate must be capable of being enforced up to 30 days after its expiry, but only for events occurring during the period of its validity.

The money proceeding from the realisation of the bank-guarantee certificate shall remain pledged by operation of law in substitution of the guarantee, kept in adjustable deposits by the representative, until the obligation to maintain the guarantee ceases.

h) As regards the validity of the guarantee, entities must always keep the guarantee in force on the terms and for the amounts established in this regulation in order to be able to act in the development of their business (to the extent that it has not been covered by equity in accordance with what is set out in this Section).

In the event that the guarantee is enforced, the entity shall be obliged to present a new guarantee, in accordance with what is established in this regulation, in order to be able to continue developing the activities inherent to its business.

In the case of insurance policies, upon any indemnity paid by the insurer under such policies — which reduces the insured amount by an equal sum — the affected entity must reinstate the original insured amount of the policy, simultaneously with the payment of the loss by the company. Such reinstatement must be evidenced before the Commission (CMF), on the same day on which the payment of the indemnity was made.

An entity that does not give timely compliance with the foregoing obligations may not enter into new contracts inherent to the development of its business, without prejudice to the measures that the Commission (CMF) may order for that purpose.

**Table 6. Minimum-equity and guarantee requirements for the provision of intermediation and/or custody of financial instruments, and order-routing services.**

| Service | Block | Equity requirement by risk | Regulation section |
|---|---|---|---|
| EO | 1 | Exempt | V.B.(a) |
| EO | 2 | Minimum-equity requirement or guarantees of UF 500 | V.B.(e) |
| EO | 3 | Minimum-equity requirement or guarantees of UF 500 | V.B.(e) |
| Custody — With and without IIF | 1 | Exempt | V.B.(a) |
| Custody — With and without IIF | 2 | Minimum-equity requirement or guarantees of UF 1,000 | V.B.(b) |
| Custody — Without IIF | 3 | Operational | V.D.1.(b.2) |
| Custody — With IIF | 3 | Operational | V.D.1.(b.1) |
| IIF — Own and third-party account | 1 | Exempt | V.B.(a) |
| IIF — Own and third-party account | 2 | Minimum-equity requirement or guarantees of UF 1,000 | V.B.(b) |
| IIF — Own and third-party account | 3 | Operational | V.D.1.(a) |
| IIF — Own account — Market | 3 | Interest rates | V.D.2.1 |
| IIF — Own account — Market | 3 | Commodities | V.D.2.2 |
| IIF — Own account — Market | 3 | Foreign currency | V.D.2.3 |
| IIF — Own account — Market | 3 | Equities and equity indices | V.D.2.4 |
| IIF — Own account — Credit | 3 | Credit | V.D.3 |
| IIF — Own account — Credit | 3 | Counterparty | V.D.3.1 |
| IIF — Own account — Crypto | 3 | Type A | V.D.4.(d) |
| IIF — Own account — Crypto | 3 | Type B | V.D.4.(e) |

Where:
- IIF: Intermediation of financial instruments.
- EO: Order routing.
- Custody: Custody of financial instruments.
- Without IIF: Entity provides only the custody service, without the intermediation of financial instruments.
- With IIF: the entity provides the custody service jointly with the intermediation-of-financial-instruments service.
- Own account: Intermediation of financial instruments for own account.
- Third parties: Intermediation of financial instruments for the account of third parties.

### Original Spanish

> "B. REQUISITO DE PATRIMONIO MÍNIMO Y GARANTÍAS
>
> De acuerdo con el artículo 7 de la Ley Fintec, en el caso de que una entidad preste de manera simultánea dos o más de los servicios comprendidos en esta norma, deberá acreditar que cumple todos y cada uno de los requisitos aplicables a cada uno de los servicios sin entenderse por este motivo, la necesidad de acumular el cumplimiento de los requisitos de patrimonio mínimo y garantías de los artículos 10 y 11. De este modo:
>
> a) Las entidades del Bloque 1 que presten los servicios de intermediación de instrumentos financieros, custodia de instrumentos financieros o enrutamiento de órdenes se encuentran exentas de requisitos de patrimonio mínimo y de garantías.
>
> b) Las entidades del Bloque 2 que presten los servicios de intermediación y/o custodia de instrumentos financieros deberán disponer permanentemente de un patrimonio ajustado y/o garantías igual o superior a UF 1.000 de acuerdo con la metodología de cálculo indicada en la sección C. Si la entidad descrita también presta el servicio de enrutamiento de órdenes, no deberá cumplir adicionalmente el requisito de garantías por UF 500 descrito más adelante.
>
> c) Las entidades del Bloque 3 que presten los servicios de intermediación y/o custodia de instrumentos financieros, deberán contar permanentemente con un patrimonio ajustado) y/o garantías que sea igual o superior al mayor entre:
>
> 1) UF 5.000.
>
> 2) El 3% (o hasta 6%) de los activos ponderados por riesgo financiero y operacional de la entidad, de acuerdo con lo dispuesto en la letra D siguiente.
>
> d) Los requisitos de patrimonio por riesgos financieros (mercado y crédito) serán cumplidos exclusivamente por medio del patrimonio ajustado. El requisito de patrimonio por riesgo operacional podrá ser cumplido por patrimonio ajustado y/o garantías.
>
> e) Las entidades del Bloque 2 o 3 que presten el servicio de enrutamiento de órdenes, deberán contar permanentemente con patrimonio ajustado y/o garantías igual o superior a UF 500.
>
> f) Las entidades del Bloque 3 que presten los servicios de intermediación y/o custodia de instrumentos financieros que cumplan con los requisitos mencionados en el literal c), y que también presten el servicio de enrutamiento de órdenes no deberán cumplir adicionalmente el requisito de garantías por UF 500.
>
> g) La entidad podrá constituir una garantía mediante una póliza de seguro o boleta de garantía bancaria para el cumplimiento de los requisitos establecidos en esta norma.
>
> 1) En caso de la póliza de seguro, esta deberá cubrir los daños y perjuicios causados a terceros, de los cuales sea civilmente responsable, que resulten de la prestación de los servicios propios de intermediación de instrumentos financieros, enrutamiento de órdenes o custodia de instrumentos financieros, por actos, errores u omisiones ocurridos durante la vigencia de la póliza y que afecten a los terceros atendidas profesionalmente por el asegurado. Deberá cubrir, asimismo, la responsabilidad civil de sus dependientes, de sus administradores, representantes, apoderados o de cualquier persona que participe en las funciones de asesoría por su cuenta, y en general, la de toda persona por la cual sea civilmente responsable en el ejercicio de la actividad de intermediación de instrumentos financieros, enrutamiento de órdenes o custodia de instrumentos financieros. La cobertura deberá comprender tanto los daños y perjuicios causados a terceros, como los gastos y costas del proceso que éstos o sus causahabientes promuevan en contra del asegurado.
>
> También deberá ser de cargo de la compañía aseguradora los gastos de defensa del asegurado, incluso los honorarios respectivos, aun cuando se trate de reclamaciones infundadas.
>
> Por último, el seguro deberá indicar que el pago de la indemnización al tercero perjudicado se efectuará en virtud de sentencia ejecutoriada, o de transacción judicial o extrajudicial celebrada por el asegurado con el consentimiento de la compañía.
>
> 2) En el caso de constituirse la garantía mediante boleta bancaria, ella deberá ser tomada en un banco autorizado para operar en el mercado nacional. El documento deberá señalar que es tomada a favor de los beneficiarios de la garantía, esto es, los acreedores presentes o futuros que llegare a tener en razón de sus operaciones de intermediación de instrumentos financieros, enrutamiento de órdenes o custodia de instrumentos financieros, y con el exclusivo objeto de ser usada en los términos de la Ley N°21.521, y ser pagadera a simple requerimiento.
>
> El monto de la boleta bancaria será el que se determine por aplicación de lo dispuesto en esta norma.
>
> La entidad deberá designar a un banco como representante de los posibles beneficiarios de la boleta bancaria, quien será el tenedor de esta.
>
> El representante de los beneficiarios de la boleta bancaria, para hacerla efectiva y sin que sea necesario acreditarlo a la entidad otorgante, deberá ser notificado judicialmente del hecho de haberse interpuesto demanda en contra de la entidad caucionada.
>
> La boleta bancaria deberá poder hacerse efectiva hasta 30 días después de su vencimiento, pero sólo por hechos ocurridos durante el período de su vigencia.
>
> El dinero proveniente de la realización de la boleta bancaria quedará en prenda de pleno derecho en sustitución de la garantía, manteniéndose en depósitos reajustables por el representante, hasta que cese la obligación de mantener la garantía.
>
> h) En lo referente a la vigencia de la garantía, las entidades deberán mantener siempre vigente la garantía en los términos y por los montos establecidos en la presente norma para poder actuar en el desarrollo de su giro (en la medida que no haya sido cubierto por patrimonio de acuerdo a lo señalado en esta sección).
>
> En caso de hacerse efectiva la garantía, la entidad estará obligada a la presentación de una nueva garantía, conforme a lo establecido en esta norma, para poder continuar desarrollando las actividades inherentes a su giro.
>
> Tratándose de pólizas de seguros, ante cualquier indemnización pagada por el asegurador con cargo a dichas pólizas -que reduzca el monto asegurado en igual cantidad- la entidad afectada deberá rehabilitar el monto asegurado original de la póliza, simultáneamente con el pago del siniestro por parte de la compañía. Se deberá acreditar dicha rehabilitación ante la Comisión, el mismo día en que se haya efectuado el pago de la indemnización.
>
> La entidad que no diere cumplimiento oportuno a las obligaciones anteriores no podrá celebrar nuevos contratos inherentes al desarrollo de su giro, sin perjuicio de las medidas que al efecto disponga la Comisión.
>
> Tabla 6. Requisitos de patrimonio mínimo y garantías para la prestación de servicios de intermediación y/o custodia de instrumentos financieros, y enrutamiento de órdenes.
>
> Requisito de patrimonio por Sección
> Servicio Bloque
> riesgo norma
> 1 Exento V.B.(a)
> EO 2 Requisito de patrimonio mínimo
> V.B.(e)
> 3 o garantías de UF 500
> 1 Exento V.B.(a)
> Con y sin
> Requisito de patrimonio mínimo
> IIF 2 V.B.(b)
> Custodia o garantías de UF 1.000
> Sin IIF V.D.1.(b.2)
> 3 Operacional
> Con IIF V.D.1.(b.1)
> 1 Exento V.B.(a)
> Cuenta
> Requisito de patrimonio mínimo
> propia y 2 V.B.(b)
> o garantías de UF 1.000
> terceros
> 3 Operacional V.D.1.(a)
> Tasas de interés V.D.2.1
> Materias primas V.D.2.2
> IIF Mercado
> Moneda extranjera V.D.2.3
> Cuenta Acciones e índices V.D.2.4
> 3
> propia Crédito V.D.3
> Crédito
> Contraparte V.D.3.1
> Tipo A V.D.4.(d)
> Cripto
> Tipo B V.D.4.(e)
> Donde:
> IIF: Intermediación de instrumentos financieros.
> EO: Enrutamiento de órdenes.
> Custodia: Custodia de instrumentos financieros.
> Sin IIF: Entidad presta solamente el servicio de custodia, sin la intermediación de instrumentos financieros.
> Con IIF: la entidad presta el servicio de custodia de forma conjunta con el servicio de intermediación de instrumentos financieros.
> Cuenta propia: Intermediación de instrumentos financieros por cuenta propia.
> Terceros: Intermediación de instrumentos financieros por cuenta de terceros."

> **TN:** Item c) reads "patrimonio ajustado)" in the source — a stray closing parenthesis (drafting artifact); rendered without it as "adjusted equity". Table 6 is reproduced in the Original Spanish blockquote in pdfplumber's column-first extraction order (which interleaves the Block column and merged cells); the English table above is realigned row-first for readability.

### Cross-references
- Ley 21.521 Art. 7 — service-accumulation rule (no cumulative stacking of requirements) referenced in the opening paragraph.
- Ley 21.521 Arts. 10, 11 — minimum-equity and guarantee requirements referenced in the opening paragraph.
- NCG 502 §V.A — block classification that determines which requirement applies.
- NCG 502 §V.C — adjusted-equity calculation methodology referenced in item b).
- NCG 502 §V.D — risk-weighted-assets methodology referenced in item c)(2).
- NCG 502 §V.D.1 to §V.D.4 — risk-specific requirement sections referenced in Table 6.

> **Source:** NCG 502 §V.B (12-ene-2024).

---

## V.C — Adjusted Equity
**NCG anchor:** N° 502, Sección V, C
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, adjusted-equity, deductions, unpaid-assets, appraisal

### Plain-English text

The entity's adjusted equity may not be lower than the minimum-equity requirement established in letter B above.

a) For the calculation of adjusted equity, the following shall be deducted from accounting equity:

1) Intangible assets.

2) The debit balance of the accounts with natural or legal persons related to the financial-service provider.

3) Assets used to guarantee the obligations of third parties.

4) Assets delivered to other entities to cover the operations carried out for own account in derivatives or contracts for differences.

5) The debit balance of the receivable accounts with related parties.

6) The amount recorded under prepaid expenses.

7) The net balance of deferred assets.

b) In the determination of adjusted equity, if there are assets that remain unpaid, the value to be considered for those assets shall be the lower value resulting from applying one of the following methods:

1) Deduct from the value of the assets the provisions that have been constituted for the concept of uncollectible debts, in accordance with the International Financial Reporting Standards (IFRS) and with the rules of this Commission.

2) Depending on the period during which it has remained unpaid, or the number of times it has been rescheduled:

i) Consider at 60% of their value the assets that remain unpaid for a period exceeding 2 days after their maturity, or whose maturity has been scheduled for the first time.

ii) Consider at 30% of their value the assets that remained unpaid for a period exceeding 10 days, or whose maturity has been rescheduled for the second time.

iii) Do not consider those assets that remained unpaid for a period exceeding 30 days after their maturity, or whose maturity has been rescheduled more than twice.

c) In the event that properties represent more than 40% of total assets, an independent commercial appraisal not more than two years old must be available. For these purposes, they shall have to engage a commercial appraisal with suitable, independent professionals, not related to the entity nor to one another, these appraisers being bank appraisers, architects, civil engineers, or civil constructors of recognised prestige. The appraisers must have the highest professional qualification in consideration of the characteristics, use, and intended purpose of the appraised assets. Entities must ensure that the persons engaged to appraise the real-estate assets of their property do not have interests that compromise their independence with respect to the entity and to those who have an economic interest or could be affected by the appraisal.

### Original Spanish

> "C. PATRIMONIO AJUSTADO
>
> El patrimonio ajustado de la entidad no podrá ser inferior al requisito de patrimonio mínimo establecido en la letra B anterior.
>
> a) Para el cálculo del patrimonio ajustado se rebajará del patrimonio contable:
>
> 1) Los activos intangibles.
>
> 2) El saldo deudor de las cuentas con personas naturales o jurídicas relacionadas al prestador de servicios financieros.
>
> 3) Los activos utilizados para garantizar obligaciones de terceros.
>
> 4) Los activos entregados a otras entidades para cubrir las operaciones efectuadas por cuenta propia en derivados o contratos por diferencias.
>
> 5) El saldo deudor de las cuentas por cobrar con relacionados.
>
> 6) El monto registrado por concepto de gastos anticipados.
>
> 7) El saldo neto de activos diferidos.
>
> b) En la determinación del patrimonio ajustado, si existieren activos que permanecieren impagos, se deberá considerar como valor de dichos activos el menor valor que resulte de aplicar uno de los siguientes métodos.
>
> 1) Rebajar del valor de los activos las provisiones que se hubieren constituido por concepto de deudas incobrables, de acuerdo con las Normas Internacionales de Información Financiera (NIIF, IFRS en su sigla en inglés) y a las normas de esta Comisión.
>
> 2) Según sea el período en que ha permanecido impago, o las veces que ha sido reprogramado:
>
> i) Considerar en un 60% de su valor los activos que permanecieren impagos por un plazo superior a 2 días con posterioridad a su vencimiento o cuyo vencimiento hubiere sido programado por primera vez.
>
> ii) Considerar en un 30% de su valor los activos que permanecieron impagos por un plazo superior a 10 días o cuyo vencimiento hubiere sido reprogramado por segunda vez.
>
> iii) No considerar aquellos activos que permanecieron impagos por un plazo superior a 30 días con posterioridad a su vencimiento o cuyo vencimiento hubiere sido reprogramado más de dos veces.
>
> c) En caso de que las propiedades representen más del 40% del total de activos, se deberá disponer de una tasación comercial independiente con una antigüedad no mayor a dos años. Para estos efectos, tendrán que contratar una tasación comercial con profesionales idóneos, independientes, no relacionados con la entidad ni entre sí, siendo estos tasadores de bancos, arquitectos, ingenieros civiles o constructores civiles de reconocido prestigio. Los tasadores deberán tener la más alta calificación profesional en consideración a las características, uso y destino de los bienes tasados. Las entidades deberán velar por que las personas contratadas para tasar los bienes raíces de su propiedad, no tengan intereses que comprometan su independencia respecto la entidad y de quienes tengan interés económico o puedan ser afectados por la tasación."

### Cross-references
- Ley 21.521 Art. 11 — capital requirement that adjusted equity serves.
- NCG 502 §V.B — minimum-equity requirement that adjusted equity may not fall below.
- NCG 502 §V.D — risk-weighted-assets methodology against which adjusted equity is measured.

> **Source:** NCG 502 §V.C (12-ene-2024).

---

## V.D — Methodology for Computing Risk-Weighted Assets for Financial and Operational Risk
**NCG anchor:** N° 502, Sección V, D
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, risk-weighted-assets, operational-risk, market-risk, credit-risk, crypto-assets

### Plain-English text

a) The adjusted-equity requirement for the provision of the services of intermediation and/or custody of financial instruments shall be calculated by means of the sum of the following amounts:

1) An amount referring to the equity requirement for operational risk calculated in accordance with the provisions of Section D.1 below.

2) An amount referring to the equity requirement for market risk in accordance with the provisions of Section D.2 below.

3) An amount referring to the equity requirement for credit risk in accordance with the provisions of Section D.3 below.

4) An amount referring to the credit- and market-risk equity requirement for crypto-assets in Section D.4 below.

b) The total value of the risk-weighted assets for financial and operational risk shall correspond to 33.3 times the equity requirement of preceding letter a).

### Original Spanish

> "D. METODOLOGÍA DE CÓMPUTO DE LOS ACTIVOS PONDERADOS POR RIESGO FINANCIERO Y OPERACIONAL
>
> a) El requerimiento de patrimonio ajustado para la prestación de los servicios de intermediación y/o custodia de instrumentos financieros será calculado por medio de la suma de las siguientes cantidades:
>
> 1) Un monto referido al requerimiento de patrimonio por riesgo operacional calculado según lo dispuesto la sección D.1 siguiente.
>
> 2) Un monto referido al requerimiento de patrimonio por riesgo de mercado según lo dispuesto en la sección D.2 siguiente.
>
> 3) Un monto referido al requerimiento de patrimonio por riesgo de crédito según lo dispuesto en la sección D.3 siguiente.
>
> 4) Un monto referido al requerimiento de patrimonio de riesgo de crédito y mercado para criptoactivos en la sección D.4. siguiente.
>
> b) El valor total de los activos ponderados por riesgo financiero y operacional corresponderá a 33,3 veces el requerimiento de patrimonio de la letra a) precedente."

> **TN:** Item a)(1) reads "calculado según lo dispuesto la sección D.1" in the source — the preposition "en" appears to be omitted before "la sección"; rendered idiomatically as "in accordance with the provisions of Section D.1".

### Cross-references
- Ley 21.521 Art. 11 — capital requirement implemented by this methodology.
- NCG 502 §V.B.c)(2) — 3%-to-6% requirement applied to the risk-weighted assets computed here.
- NCG 502 §V.D.1 to §V.D.4 — operational, market, credit, and crypto-asset risk requirement sub-sections.

> **Source:** NCG 502 §V.D (12-ene-2024).

---

## V.D.1 — Equity (or Guarantee) Requirement for Operational Risk
**NCG anchor:** N° 502, Sección V, D.1
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, operational-risk, intermediation, custody, exposure-weighting

### Plain-English text

a) The equity requirement for operational risk for the intermediation-of-financial-instruments service corresponds to a percentage of the amount of the total average daily transactions of the last three months. The total of transactions includes those of purchase and sale, both for own account and for the account of third parties. For this purpose, the following must be summed:

1) 0.1% of the transactions that do not correspond to derivatives or contracts for differences, average daily over the last three months.

2) 0.01% of the notional amounts of the derivative contracts or contracts for differences, average daily over the last three months.

b) The equity requirement for operational risk for the custody-of-financial-instruments service corresponds to a percentage of the amount of the average assets in custody of the last three months.

1) In the case where the intermediation and custody of financial instruments services are provided jointly, this amount shall be 0.4% of the average daily assets in custody of the last three months.

2) In the case where the custody service is provided exclusively, this amount shall be 0.1% of the average daily assets in custody of the last three months.

c) Table 7 shows the methodology for calculating the equity requirement for operational risk when the provision of the intermediation service is carried out jointly with the custody service. Table 8 corresponds to the case where the custody service is provided exclusively, without considering the intermediation service.

**Table 7. Calculation of the operational-risk equity requirement for the joint provision of intermediation and custody services.**

| Service | Exposure (E) | Weight (P) | Equity requirement |
|---|---|---|---|
| Custody | Assets in custody | 0.4% | ∑E*P |
| Intermediation — transactions not corresponding to derivatives or CFD | Average daily amount of the value of transactions | 0.1% | ∑E*P |
| Intermediation — transactions in derivatives and CFD | Average daily amount of the notional amount of transactions | 0.01% | ∑E*P |

**Table 8. Calculation of the operational-risk equity requirement for the provision of the custody service on an exclusive basis (without intermediation).**

| Service | Exposure (E) | Weight (P) | Equity requirement |
|---|---|---|---|
| Custody | Assets in custody | 0.1% | ∑E*P |

### Original Spanish

> "D.1. REQUISITO DE PATRIMONIO (O GARANTÍAS) POR RIESGO OPERACIONAL
>
> a) El requisito de patrimonio por riesgo operacional para el servicio de intermediación de instrumentos financieros corresponde a un porcentaje del monto de las transacciones totales promedio diarias de los últimos tres meses. El total de transacciones incluye aquellas de compra y venta, tanto por cuenta propia como por cuenta de terceros. Para ello se deberán sumar:
>
> 1) El 0,1% de las transacciones que no correspondan a derivados o contratos por diferencias promedio diarias de los últimos tres meses.
>
> 2) El 0,01% de los montos nocionales de los contratos derivados o contratos por diferencias promedio diario de los últimos tres meses.
>
> b) El requerimiento de patrimonio de riesgo operacional para el servicio de custodia de instrumentos financieros corresponde a un porcentaje del monto de los activos custodiados promedio de los últimos tres meses.
>
> 1) En el caso que los servicios de intermediación y custodia de instrumentos financieros sean prestados de forma conjunta, este monto será el 0,4% de los activos custodiados promedio diario de los últimos tres meses.
>
> 2) En el caso que el servicio de custodia sea prestado de forma exclusiva, este monto será 0,1% de los activos custodiados promedio diario de los últimos tres meses.
>
> c) La Tabla 7 muestra la metodología de cálculo del requisito de patrimonio por riesgo operacional cuando la prestación del servicio de intermediación se realiza en forma conjunta con el servicio de custodia. La Tabla 8 corresponde al caso en que el servicio de custodia se presta de forma exclusiva, sin considerar el servicio de intermediación.
>
> Tabla 7. Cálculo del requisito de patrimonio por riesgo operacional para la prestación conjunta de servicios de intermediación y custodia.
>
> Ponderador Requisito de
> Servicio Exposición (E)
> (P) patrimonio
> Custodia Activos custodiados 0,4%
> Intermediación
> transacciones
> Monto promedio
> que no
> diario del valor de 0,1%
> corresponden a ∑E*P
> las transacciones
> derivados o
> CFD
> Intermediación Monto promedio
> transacciones diario del monto
> 0,01%
> en derivados y nocional de las
> CFD transacciones
>
> Tabla 8. Cálculo del requisito de patrimonio por riesgo operacional para la prestación del servicio de custodia de forma exclusiva (sin intermediación).
>
> Ponderador Requisito de
> Servicio Exposición (E)
> (P) patrimonio
> Custodia Activos custodiados 0,1% ∑E*P"

> **TN:** Tables 7 and 8 are reproduced in the Original Spanish blockquote in pdfplumber's column-first/line-wrapped extraction order; the English tables above are realigned row-first.

### Cross-references
- Ley 21.521 Art. 11 — capital/guarantee requirement implemented.
- NCG 502 §V.B.d) — operational-risk requirement may be met by adjusted equity and/or guarantees.
- NCG 502 §V.D.a)(1) — operational-risk amount as a component of the total adjusted-equity requirement.

> **Source:** NCG 502 §V.D.1 (12-ene-2024).

---

## V.D.2 — Equity Requirement for Market Risk
**NCG anchor:** N° 502, Sección V, D.2
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, market-risk, own-portfolio, risk-factors

### Plain-English text

This requirement applies to the providers of intermediation-of-financial-instruments services that hold an own portfolio in financial instruments. The total equity requirement for market risk shall be equal to the sum of the amounts required by the exposures to the following risk factors:

1. Interest rate
2. Commodities
3. Exchange rate
4. Equities and equity indices

### Original Spanish

> "D.2. REQUISITO DE PATRIMONIO POR RIESGO DE MERCADO
>
> Este requisito aplica a los prestadores de servicios de intermediación de instrumentos financieros que dispongan una cartera propia en instrumentos financieros. El requisito total de patrimonio por riesgo de mercado será igual a la suma de los montos requeridos por las exposiciones a los siguientes factores de riesgo:
>
> 1. Tasa de interés
>
> 2. Materias primas
>
> 3. Tipo de cambio
>
> 4. Acciones e índices accionarios"

### Cross-references
- Ley 21.521 Art. 11 — capital requirement implemented.
- NCG 502 §V.B.d) — market-risk requirement met exclusively by adjusted equity.
- NCG 502 §V.D.2.1 to §V.D.2.4 — the four market-risk factor sub-sections.

> **Source:** NCG 502 §V.D.2 (12-ene-2024).

---

## V.D.2.1 — Interest Rate
**NCG anchor:** N° 502, Sección V, D.2.1
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, market-risk, interest-rate, debt-instruments, derivatives

### Plain-English text

a) **Debt-representative instruments.** The equity requirement for market risk corresponds to an amount referring to the positions in debt-representative financial instruments that the intermediation-service provider considers in the calculation of its minimum equity.

1) Each of the financial instruments must be classified in accordance with Table 9, referring to the maturity term.

2) Once this classification has been carried out, the percentages set out in Table 9 must be applied to the market value of the financial instruments.

3) For the case of instruments for which, in accordance with IFRS, provisions must be constituted, the equity requirement shall be calculated on the net-of-provision asset multiplied by the corresponding weight.

b) **Interest-rate derivatives.** The equity requirement for market risk corresponds to an amount referring to the rights and obligations of the intermediation-service provider whose value is adjusted in accordance with the variation of market interest rates. In the case of derivatives or contracts for differences, their notional value must be considered.

1) Each of the financial instruments must be classified in accordance with Table 9, referring to the residual term to maturity of the instrument.

2) Once this classification has been carried out, the percentages set out in Table 9 must be applied to the notional value of the financial instruments.

**Table 9. Percentages according to term to maturity — interest-rate market risk**

| Term to maturity | % |
|---|---|
| <91 days | 2 |
| 90 days< and <1 year | 5 |
| 1 year < and <5 years | 8 |
| 5 years< and <12 years | 12 |
| >12 years | 20 |

### Original Spanish

> "D.2.1. TASA DE INTERÉS
>
> a) Instrumentos representativos de deuda. El requisito de patrimonio por riesgo de mercado corresponde a un monto referido a las posiciones en instrumentos financieros representativos de deuda que el prestador de servicios de intermediación considere en el cálculo de su patrimonio mínimo.
>
> 1) Se deberá clasificar cada uno de los instrumentos financieros de acuerdo con la Tabla 9 referida al plazo de vencimiento.
>
> 2) Una vez efectuada esta clasificación se deberán aplicar los porcentajes dispuestos en la Tabla 9, sobre el valor de mercado de los instrumentos financieros.
>
> 3) Para el caso de los instrumentos que, de acuerdo con IFRS, se deban constituir provisiones, el requerimiento patrimonial se calculará sobre el activo neto de provisión multiplicado por el ponderador correspondiente.
>
> b) Derivados de tasas de interés. El requisito de patrimonio por riesgo de mercado corresponde a un monto referido a los derechos y obligaciones del prestador de servicios de intermediación cuyo valor se reajuste de acuerdo con la variación de tasas de interés del mercado. En el caso de derivados o contratos por diferencias se deberá considerar su valor nocional.
>
> 1) Se deberá clasificar cada uno de los instrumentos financieros de acuerdo con la Tabla 9 referida al plazo residual al vencimiento del instrumento.
>
> 2) Una vez efectuada esta clasificación se deberán aplicar los porcentajes dispuestos en la Tabla 9, sobre el valor nocional de los instrumentos financieros.
>
> Tabla 9. Porcentajes según plazo al vencimiento riesgo de mercado tasas de interés
>
> Plazo al vencimiento %
> <91 días 2
> 90 días< y <1 año 5
> 1 año < y <5 años 8
> 5 años< y <12 años 12
> >12 años 20"

### Cross-references
- Ley 21.521 Art. 11 — capital requirement implemented.
- NCG 502 §V.D.2 — market-risk requirement of which interest rate is the first factor.

> **Source:** NCG 502 §V.D.2.1 (12-ene-2024).

---

## V.D.2.2 — Commodities
**NCG anchor:** N° 502, Sección V, D.2.2
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, market-risk, commodities, derivatives, net-position

### Plain-English text

a) For the calculation of the equity requirement for market risk, all positions in financial instruments in derivatives and contracts for differences on commodities or indices on commodities must be included.

b) For each commodity, expressed in its standard unit of measurement and then converted to local currency by means of the spot rates, the net position is calculated as the difference between long and short positions. To this resulting position a charge of 15% is applied. In addition, an additional charge of 3% is applied to the gross position in each commodity — that is, to the sum of long and short positions (in absolute value).

c) The foregoing is expressed in the following formula. Where `Aᵢ` corresponds to the value of the long positions in commodity "i", `Pᵢ` corresponds to the value of the short positions in commodity "i", and "N" corresponds to the number of commodities in which the intermediation-service provider maintains positions:

`∑ᵢ₌₁ᴺ (|Aᵢ − Pᵢ|) * 15% + ∑ᵢ₌₁ᴺ (Aᵢ + |Pᵢ|) * 3%`

### Original Spanish

> "D.2.2. MATERIAS PRIMAS
>
> a) Para el cálculo del requisito de patrimonio por riesgo de mercado, se deben incluir todas las posiciones en instrumentos financieros en derivados y contratos por diferencias sobre materias primas o índices sobre materias primas.
>
> b) Para cada materia prima expresada en su unidad estándar de medición y luego convertida a moneda local mediante las tasas spot, se calcula la posición neta como la diferencia entre posiciones activas y pasivas. A esta posición resultante se le aplica un cargo de 15%. Además, se aplica un cargo adicional de 3% sobre la posición bruta en cada materia prima, es decir, sobre la suma de posiciones activas y pasivas (en valor absoluto).
>
> c) Lo anterior se expresa en la siguiente fórmula. Donde 𝐴𝑖 corresponde al valor de las posiciones activas en la materia prima “i”, 𝑃𝑖 corresponde al valor de las posiciones pasivas en la materia prima “i” y “N” corresponde al número de materias primas en las que el prestador de servicios de intermediación mantiene posiciones.
>
> 𝐍 𝐍
> ∑ (|𝐀 −𝐏|)∗𝟏𝟓%+∑ (𝐀 +|𝐏|)∗𝟑%
> 𝐢 𝐢 𝐢 𝐢
> 𝐢=𝟏 𝐢=𝟏"

> **TN:** The formula is reproduced in the Original Spanish blockquote in pdfplumber's extraction order, in which the summation symbols, the body of the expression, and the subscript/limit characters extract on separate lines; the English text presents the same formula linearised.

> **TN:** This block's `--mode ncg` round-trip coverage is ~0.84 (the CI gate runs at 0.80). The shortfall is a pdfplumber page-break artifact, not a fidelity gap: at the foot of p.117 the running header ("V. CAPITAL Y GARANTÍAS / D. METODOLOGÍA…") is extracted between item b) and item c), so the sliding-window chunks straddling that boundary fail to match even though every word is transcribed verbatim. The Spanish is faithful to the PDF.


### Cross-references
- Ley 21.521 Art. 11 — capital requirement implemented.
- NCG 502 §V.D.2 — market-risk requirement of which commodities is the second factor.

> **Source:** NCG 502 §V.D.2.2 (12-ene-2024).

---

## V.D.2.3 — Foreign Currency
**NCG anchor:** N° 502, Sección V, D.2.3
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, market-risk, foreign-currency, exchange-rate, net-position

### Plain-English text

a) For the calculation of the equity requirement for market risk, the net positions in currencies across the entire balance sheet must be considered. The net position in each currency must be calculated by summing:

1) The effective or spot net position.

2) The net position in derivatives or contracts for differences, which includes all amounts to be received less all amounts to be paid.

3) Guarantees in foreign currency.

4) Any other position on the balance sheet that may generate gains or losses in foreign currencies.

b) For the calculation of the equity requirement for market risk, the net position in each currency must be weighted by the market-risk weight (PRM) corresponding to it, by means of the following formula:

`max( ∑ᵢ₌₁ᴺ (PNAᵢ * PRMᵢ), ∑ᵢ₌₁ᴺ (|PNPᵢ * PRMᵢ|) )`

c) Where `PNAᵢ` and `PNPᵢ` correspond to the long net position and short net position, respectively, for each currency "i"; `PRMᵢ` corresponds to the market-risk weight associated with currency "i", which is determined in accordance with Table 10.

**Table 10. Exchange-rate risk weights**

| Risks | Currencies | Weight |
|---|---|---|
| Basket 1 | USD, EUR, EAU, AUD, CAD, CHF, CNY, CZK, DKK, GBP, HKD, ILS, JPY, KRW, NOK, NZD, SAR, SGD, SKK, SEK, TWD | 8% |
| Basket 2 | Rest of currencies | 12% |

### Original Spanish

> "D.2.3. MONEDA EXTRANJERA.
>
> a) Para el cálculo del requisito de patrimonio por riesgo de mercado, se deben considerar las posiciones netas en monedas en todo el balance. La posición neta en cada moneda debe calcularse sumando:
>
> 1) La posición neta efectiva o spot.
>
> 2) La posición neta en derivados o contratos por diferencias, que incluye todos los montos a recibir menos todos los montos a pagar.
>
> 3) Garantías en moneda extranjera.
>
> 4) Cualquier otra posición del balance que pueda generar ganancias o pérdidas en monedas extranjeras.
>
> b) Para el cálculo del requisito de patrimonio por riesgo de mercado, se debe ponderar la posición neta en cada moneda por el ponderador de riesgo de mercado (PRM) que le corresponda, mediante la siguiente fórmula.
>
> 𝐍 𝐍
> 𝐦𝐚𝐱(∑ (𝐏𝐍𝐀 ∗𝐏𝐑𝐌),∑ (|𝐏𝐍𝐏 ∗𝐏𝐑𝐌|))
> 𝐢 𝐢 𝐢 𝐢
> 𝐢=𝟏 𝐢=𝟏
>
> c) Donde 𝑃𝑁𝐴𝑖 y 𝑃𝑁𝑃𝑖 corresponden a la posición neta activa y pasiva, respectivamente para cada moneda “i”; 𝑃𝑅𝑀𝑖 corresponde al ponderador de riesgo de mercado, asociado a la moneda “i”, que se determina de acuerdo con la Tabla 10.
>
> Tabla 10. Ponderadores de riesgo de tipo de cambio
>
> Riesgos Monedas Ponderador
> USD, EUR, EAU, AUD, CAD, CHF,
> CNY, CZK, DKK, GBP, HKD, ILS, JPY,
> Canasta 1 8%
> KRW, NOK, NZD, SAR, SGD, SKK,
> SEK, TWD
> Canasta 2 Resto de monedas 12%"

> **TN:** "posición neta activa / pasiva" is rendered as "long net position / short net position" (the active/passive position dichotomy used elsewhere in this Section). The formula and Table 10 are reproduced in the Original Spanish blockquote in pdfplumber's line-wrapped extraction order (summation body and subscripts split across lines; the Basket 1 currency list wrapped over multiple lines); the English presents them linearised and row-first.

### Cross-references
- Ley 21.521 Art. 11 — capital requirement implemented.
- NCG 502 §V.D.2 — market-risk requirement of which foreign currency is the third factor.

> **Source:** NCG 502 §V.D.2.3 (12-ene-2024).

---

## V.D.2.4 — Equities and Equity Indices
**NCG anchor:** N° 502, Sección V, D.2.4
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, market-risk, equities, equity-indices, specific-risk, general-risk

### Plain-English text

The equity requirement for market risk of stock-exchange quotations applies to all derivatives and contracts for differences that have as underlyings positions in shares and indices on shares, which must be separated into the respective underlyings. They must be calculated in accordance with each market of the respective underlying and considering the specific risk and general risk set out below.

a) **Specific risk.** Where "`Aᵢ`" corresponds to the value of the long positions in stock-exchange market "i", "`Pᵢ`" corresponds to the value of the short positions in stock-exchange market "i", and "N" corresponds to the number of stock-exchange markets in which the intermediation-service provider maintains positions:

`∑ᵢ₌₁ᴺ (Aᵢ + |Pᵢ|) * 11%`

b) **General risk.** The equity requirement for general risk is calculated as the net exposure of derivative instruments or contracts for difference — that is, the sum of the long positions less the short positions, multiplied by a single market-risk weight (PRM) of 11%. In addition to the foregoing, an additional charge of 2% is added to the net positions in indices on shares. Where "`Aᵢ`" corresponds to the value of the long positions in stock-exchange market "i" (excludes indices and arbitrage strategies), "`Pᵢ`" corresponds to the value of the short positions in stock-exchange market "i" (excludes indices and arbitrage strategies), "`AIᵢ`" corresponds to the value of the long positions in indices and arbitrage strategies in stock-exchange market "i", "`PIᵢ`" corresponds to the value of the short positions in indices and arbitrage strategies in stock-exchange market "i", and "N" corresponds to the number of stock-exchange markets in which the intermediation-service provider maintains positions:

`∑ᵢ₌₁ᴺ (|Aᵢ − Pᵢ|) * 11% + ∑ᵢ₌₁ᴺ (|AIᵢ − PIᵢ|) * 13%`

### Original Spanish

> "D.2.4. ACCIONES E ÍNDICES ACCIONARIOS
>
> El requisito de patrimonio por riesgo de mercado de cotizaciones bursátiles se aplica a todos los derivados y contratos por diferencias que tengan como subyacentes posiciones en acciones e índices sobre acciones, los que deben ser separados en los subyacentes respectivos. Se deberán calcular de acuerdo con cada mercado del respectivo subyacente y considerar el riesgo específico y riesgo general señalado a continuación.
>
> a) Riesgo específico. Donde “𝐴𝑖” corresponde al valor de las posiciones activas en el mercado bursátil “i”, “𝑃𝑖” corresponde al valor de las posiciones pasivas en el mercado bursátil “i” y “N” corresponde al número de mercados bursátiles en los que el prestador de servicios de intermediación mantiene posiciones.
>
> 𝐍
> ∑ (𝐀 +|𝐏|)∗𝟏𝟏%
> 𝐢 𝐢
> 𝐢=𝟏
>
> b) Riesgo general. El requisito de patrimonio por riesgo general se calcula como la exposición neta de instrumentos derivados o contratos por diferencia, es decir, la suma de las posiciones activas menos las posiciones pasivas, multiplicado por un ponderador de riesgo de mercado (PRM) único de 11%. Además de lo anterior, se agrega un cargo adicional de 2% a las posiciones netas en índices sobre acciones. Donde “𝐴𝑖” corresponde al valor de las posiciones activas en el mercado bursátil “i” (excluye índices y estrategias de arbitraje), “𝑃𝑖” corresponde al valor de las posiciones pasivas en el mercado bursátil “i” (excluye índices y estrategias de arbitraje), “𝐴𝐼𝑖” corresponde al valor de las posiciones activas en índices y estrategias de arbitraje en el mercado bursátil “i”, “𝑃𝐼𝑖” corresponde al valor de las posiciones pasivas en índices y estrategias de arbitraje en el mercado bursátil “i” y “N” corresponde al número de mercados bursátiles en los que el prestador de servicios de intermediación mantiene posiciones.
>
> 𝐍 𝐍
> ∑ (|𝐀 −𝐏|)∗𝟏𝟏%+∑ (|𝐀𝐈 −𝐏𝐈|)∗𝟏𝟑%
> 𝐢 𝐢 𝐢 𝐢
> 𝐢=𝟏 𝐢=𝟏"

> **TN:** "posiciones activas / pasivas" are rendered as "long positions / short positions". Both formulas are reproduced in the Original Spanish blockquote in pdfplumber's extraction order, in which the summation symbol, expression body, and subscript/limit characters each occupy separate lines; the English presents them linearised.

### Cross-references
- Ley 21.521 Art. 11 — capital requirement implemented.
- NCG 502 §V.D.2 — market-risk requirement of which equities and equity indices is the fourth factor.

> **Source:** NCG 502 §V.D.2.4 (12-ene-2024).

---

## V.D.3 — Equity Requirement for Credit Risk
**NCG anchor:** N° 502, Sección V, D.3
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, credit-risk, debt-instruments, credit-rating, counterparty

### Plain-English text

a) The equity requirement for credit risk corresponds to an amount referring to debt-representative instruments that the intermediation-of-financial-instruments-service provider considers in the calculation of its minimum equity. The balance of the cash and cash-equivalents account shall be exempt from the application of that percentage.

1) Each of the financial instruments must be classified in accordance with the credit rating and counterparty type of Table 11.

2) Once this classification has been carried out, the percentages set out in Table 11 must be applied to the value of the financial instruments.

b) The intermediation-financial-service provider must maintain a register in which it shall record all that information which makes it possible to clearly determine the assets that have remained unpaid, the period during which they were in that condition, the number and date on which reschedulings were made, and the identification of the corresponding debtors. This register must be maintained on a medium and systems that guarantee its reliability and integrity. The reschedulings must be set out in writing and duly documented.

**Table 11. Percentages according to credit rating and counterparty type for credit risk**

| Type and credit rating of the counterparty | % |
|---|---|
| Investment grade | 1% |
| BB+/BB- | 8% |
| Below BB- | 12% |
| Individuals | 6% |
| SMEs | 6.8% |
| Others | 8% |

### Original Spanish

> "D.3. REQUISITO DE PATRIMONIO POR RIESGO DE CRÉDITO
>
> a) El requisito de patrimonio de riesgo de crédito corresponde a un monto referido a instrumentos representativos de deuda que el prestador de servicios de intermediación de instrumentos financieros considere en el cálculo de su patrimonio mínimo. Se exceptuará de la aplicación de dicho porcentaje el saldo de la cuenta efectivo y equivalentes de efectivo.
>
> 1) Se deberá clasificar cada uno de los instrumentos financieros de acuerdo con la clasificación crediticia y de tipo de contraparte de la Tabla 11.
>
> 2) Una vez efectuada esta clasificación se deberán aplicar los porcentajes dispuestos en la Tabla 11, sobre el valor de los instrumentos financieros.
>
> b) El prestador de servicios financieros de intermediación deberá mantener un registro en el que anotará toda aquella información que permita determinar claramente los activos que han permanecido impagos, el plazo durante el cual estuvieron bajo esa calidad, el número y fecha en que se efectuaron reprogramaciones y la identificación de los deudores correspondientes. Este registro deberá mantenerse en un medio y sistemas que garanticen su fiabilidad e integridad. Las reprogramaciones deberán constar por escrito y estar debidamente documentadas.
>
> Tabla 11. Porcentajes según clasificación crediticia y tipo de la contraparte para riesgo de crédito
>
> Tipo y clasificación
> crediticia de la %
> contraparte
> Grado inversión 1%
> BB+/BB- 8%
> Bajo BB- 12%
> Personas 6%
> Pymes 6,8%
> Otros 8%"

> **TN:** "Personas" is rendered "Individuals" and "Pymes" (pequeñas y medianas empresas) as "SMEs". Table 11 is reproduced in the Original Spanish blockquote in pdfplumber's extraction order (the first header cell wraps across three lines); the English table is realigned row-first.

### Cross-references
- Ley 21.521 Art. 11 — capital requirement implemented.
- NCG 502 §V.D — credit-risk amount as a component of the total adjusted-equity requirement.
- NCG 502 §V.D.3.1 — counterparty-risk requirement that applies these same Table 11 weights.

> **Source:** NCG 502 §V.D.3 (12-ene-2024).

---

## V.D.3.1 — Equity Requirement for Counterparty Risk
**NCG anchor:** N° 502, Sección V, D.3.1
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, counterparty-risk, credit-equivalent, pfe, derivatives

### Plain-English text

a) The equity requirement for counterparty risk corresponds to an amount referring to the own-account intermediation of derivatives and contracts for differences of the service provider, which shall be calculated by means of the "credit equivalent" and credit-risk weights according to the type and credit rating of the counterparty.

b) The calculation of the "credit equivalent" for derivatives and contracts for differences considers:

1) The fair value of the derivative instrument or contract for differences.

2) An additional amount, which considers the potential future variation (PFE) of the price of the derivative or contract for differences. For this purpose, the notional value of the derivative or contract for differences must be multiplied according to the type of underlying asset and term to maturity in accordance with Table 12. For the "residual term" of Table 12, contracts for difference must be considered in the "up to one year" category.

3) The guarantees constituted in favour of the intermediation-service provider by its clients must be discounted.

4) The "credit equivalent" shall be equal to the maximum value between 0 and the sum of the amounts mentioned above, in accordance with the formula:

`Credit equivalent = Max(Fair value + PFE − Guarantees, 0)`

c) For the purpose of calculating the equity requirement for counterparty risk, the credit weights according to the type and credit rating of the counterparty must be applied to the "credit equivalent" in accordance with Table 11 of the previous section.

d) The calculation methodology is exemplified in Table 13.

**Table 12. Potential-future-variation (PFE) weights**

| Contract type | Residual term | Proposed PFE weights |
|---|---|---|
| Interest rate or inflation | Up to one year | 0% |
| Interest rate or inflation | Between 1 and 5 years | 0.5% |
| Interest rate or inflation | More than 5 years | 1.5% |
| Exchange rate | Up to 1 year | Basket 1: 1.5% / Basket 2: 4.5% |
| Exchange rate | Between 1 and 5 years | Basket 1: 7% / Basket 2: 20% |
| Exchange rate | More than 5 years | Basket 1: 13% / Basket 2: 30% |
| Equities | Up to 1 year | 6% |
| Equities | Between 1 and 5 years | 8% |
| Equities | More than 5 years | 10% |
| Commodities | — | 18% |
| Others | — | 32% |

**Table 13. Calculation of the equity requirement for counterparty risk**

| Credit equivalent (E) | Weight (P) | Equity requirement |
|---|---|---|
| Max(Fair value + PFE − Guarantees, 0) | Investment grade: 1%; BB+/BB-: 8%; Below BB-: 12%; Individuals: 6%; SMEs: 6.8%; Others: 8% | ∑E*P |

### Original Spanish

> "D.3.1. REQUISITO DE PATRIMONIO POR RIESGO DE CONTRAPARTE
>
> a) El requisito de patrimonio de riesgo de contraparte corresponde a un monto referido a la intermediación por cuenta propia de derivados y contratos por diferencias del prestador de servicios, el cual será calculado por medio del “equivalente de crédito” y ponderadores de riesgo de crédito según el tipo y clasificación crediticia de la contraparte.
>
> b) El cálculo del “equivalente de crédito” para derivados y contratos por diferencias considera:
>
> 1) El valor razonable del instrumento derivado o contrato por diferencias.
>
> 2) Un monto adicional, que considera la variación potencial futura (PFE) del precio del derivado o contrato por diferencias. Para ello, se deberá multiplicar el valor nocional del derivado o contrato por diferencias según el tipo de activo subyacente y plazo al vencimiento de acuerdo con la Tabla 12. Para el “plazo residual” de la Tabla 12, los contratos por diferencia deberán ser considerados en la categoría “hasta un año”
>
> 3) Se deberán descontar las garantías constituidas en favor del prestador de servicios de intermediación por parte de sus clientes.
>
> 4) El “equivalente de crédito” será igual a el máximo valor entre 0 y la suma de los montos mencionados anteriormente, de acuerdo con la fórmula:
>
> 𝐄𝐪𝐮𝐢𝐯𝐚𝐥𝐞𝐧𝐭𝐞 𝐝𝐞 𝐜𝐫é𝐝𝐢𝐭𝐨=𝐌𝐚𝐱(𝐕𝐚𝐥𝐨𝐫 𝐫𝐚𝐳𝐨𝐧𝐚𝐛𝐥𝐞+𝐏𝐅𝐄−𝐆𝐚𝐫𝐚𝐧𝐭í𝐚𝐬,𝟎)
>
> c) A efectos de calcular el requisito de patrimonio por riesgo de contraparte, se deberá aplicar al “equivalente de crédito" los ponderadores de crédito según el tipo y clasificación crediticia de la contraparte de acuerdo con la Tabla 11 de la sección anterior.
>
> d) La metodología de cálculo se ejemplifica en la Tabla 13.
>
> Tabla 12. Ponderadores de variación potencial futura (PFE)
>
> Tipo de
> Plazo residual Propuesta ponderadores PFE
> contrato
> Hasta un año 0%
> Tasa de
> interés o Entre 1 y 5 años 0,5%
> inflación
> Más de 5 años 1,5%
> Canasta 1 Canasta 2
> Tipo de Hasta 1 año 1,5% 4,5%
> cambio Entre 1 y 5 años 7% 20%
> Más de 5 años 13% 30%
> Hasta 1 año 6%
> Acciones Entre 1 y 5 años 8%
> Más de 5 años 10%
> Materias
> 18%
> primas
> Otros 32%
>
> Tabla 13. Cálculo del requisito de patrimonio por riesgo de contraparte
>
> Requisito de
> Equivalente de crédito (E) Ponderador (P)
> patrimonio
>  Grado inversión:
> 1%
>  BB+/BB-: 8%
> Max(Valor razonable+PFE
>  Bajo BB-: 12% ∑E*P
> −Garantías,0)
>  Personas: 6%
>  Pymes: 6,8%
>  Otros: 8%"

> **TN:** The credit-equivalent formula and Tables 12 and 13 are reproduced in the Original Spanish blockquote in pdfplumber's extraction order (multi-line wrapped headers; the Basket 1/Basket 2 sub-columns and the bullet list of weights interleave with the surrounding cells); the English tables are realigned row-first. "Grado inversión / Personas / Pymes" follow the renderings used in §V.D.3.

### Cross-references
- Ley 21.521 Art. 11 — capital requirement implemented.
- NCG 502 §V.D.3 — credit-risk section whose Table 11 weights are applied to the credit equivalent (items a) and c)).
- NCG 502 §V.D.2.3 — Basket 1 / Basket 2 currency classification referenced by the exchange-rate PFE weights of Table 12.

> **Source:** NCG 502 §V.D.3.1 (12-ene-2024).

---

## V.D.4 — Credit- and Market-Risk Equity Requirement for Crypto-Assets
**NCG anchor:** N° 502, Sección V, D.4
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, crypto-assets, credit-risk, market-risk, partial-offset

### Plain-English text

a) This requirement applies to the own portfolio of the providers of intermediation-of-financial-instruments services, classified in Block 3 according to their business volume.

b) This Commission (CMF) shall publish a list of crypto-assets eligible for applying the partial-offset criterion. The assets included in this list shall be referred to as "Type A" assets; the rest shall be classified as "Type B". The "Type A" crypto-assets shall be included in the list by this Commission according to the characteristics of liquidity, market capitalisation, transactionality, and price availability that those assets have. Whereas the assets that do not have those characteristics must be classified in the second group.

c) The partial-offset criterion shall be applied to "Type A" assets for the purpose of calculating their credit- and market-risk equity requirements. The said offset shall not be applied to "Type B" assets.

d) The calculation of the partial-offset criterion applicable to "Type A" assets considers the net position of each crypto-asset (subscript "k") in accordance with the following formula. An equity requirement of 100% is applied to the net position of each "Type A" asset:

`Net positionₖ = Max(Long positionₖ, |Short positionₖ|) − 0.65 * Min(Long positionₖ, |Short positionₖ|)`

e) For "Type B" assets, an equity requirement of 100% is applied to the gross position of each crypto-asset (subscript "k"), in accordance with the following formula:

`Positionₖ = Max(abs(long positionₖ), abs(Short positionₖ))`

f) The equity requirement for market and credit risk for crypto-assets is exemplified in Table 14.

**Table 14. Calculation of the market- and credit-risk equity requirement for crypto-assets**

| | Exposure (E) | Weight (P) | Equity requirement |
|---|---|---|---|
| Type A | Net positionₖ = Max(Long positionₖ, \|Short positionₖ\|) − 0.65 * Min(Long positionₖ, \|Short positionₖ\|) | 100% | ∑E*P |
| Type B | Gross positionₖ = Max(abs(long positionₖ), abs(Short positionₖ)) | 100% | ∑E*P |

### Original Spanish

> "D.4. REQUISITO DE PATRIMONIO DE RIESGO DE CRÉDITO Y MERCADO PARA CRIPTOACTIVOS
>
> a) Este requisito aplica a la cartera propia de los prestadores de servicios de intermediación de instrumentos financieros, clasificados en el Bloque 3 de acuerdo con su volumen de negocios.
>
> b) Esta Comisión publicará una lista de criptoactivos elegibles para aplicar el criterio de compensación parcial. Los activos incluidos en esta lista se denominarán activos “Tipo A”, el resto será clasificado como “Tipo B”. Los criptoactivos “Tipo A” serán incluidos en la lista por esta Comisión de acuerdo con las características de liquidez, capitalización de mercado, transaccionalidad y disponibilidad de precios que dichos activos tengan. Mientras que los activos que no cuenten con dichas características deberán ser clasificados en el segundo grupo.
>
> c) Se aplicará el criterio de compensación parcial a los activos “Tipo A” a efectos de calcular sus requisitos de patrimonio de riesgo de crédito y mercado. A los activos “Tipo B” no les será aplicada dicha compensación.
>
> d) El cálculo del criterio de compensación parcial aplicable a los activos “Tipo A” considera la posición neta de cada activo criptográfico (subíndice “k”) de acuerdo con la siguiente fórmula. Se aplica un requisito de patrimonio de 100% sobre la posición neta de cada activo “Tipo A”.
>
> 𝐏𝐨𝐬𝐢𝐜𝐢ó𝐧 𝐧𝐞𝐭𝐚 =𝐌𝐚𝐱(𝐏𝐨𝐬𝐢𝐜𝐢ó𝐧 𝐥𝐚𝐫𝐠𝐚 ,|𝐏𝐨𝐬𝐢𝐜𝐢ó𝐧 𝐜𝐨𝐫𝐭𝐚 |)−𝟎.𝟔𝟓
> 𝐤 𝐤 𝐤
> ∗𝐌𝐢𝐧(𝐏𝐨𝐬𝐢𝐜𝐢ó𝐧 𝐥𝐚𝐫𝐠𝐚 ,|𝐏𝐨𝐬𝐢𝐜𝐢ó𝐧 𝐜𝐨𝐫𝐭𝐚 |)
> 𝐤 𝐤
>
> e) Para los activos “Tipo B”, se aplica un requisito de patrimonio de 100% sobre la posición bruta de cada activo criptográfico (subíndice “k”), de acuerdo con siguiente fórmula.
>
> 𝐏𝐨𝐬𝐢𝐜𝐢ó𝐧 =𝐌𝐚𝐱(𝐚𝐛𝐬(𝐩𝐨𝐬𝐢𝐜𝐢ó𝐧 𝐥𝐚𝐫𝐠𝐚 ),𝐚𝐛𝐬(𝐏𝐨𝐬𝐢𝐜𝐢ó𝐧 𝐜𝐨𝐫𝐭𝐚 ))
> 𝐤 𝐤 𝐤
>
> f) El requisito de patrimonio por riesgo de mercado y crédito para activos criptográficos se ejemplifica en la Tabla 14.
>
> Tabla 14. Cálculo del requisito de patrimonio por riesgo de mercado y crédito de criptoactivos
>
> Requisito
> Ponderador
> Exposición (E) de
> (P)
> patrimonio
> A Posición neta =Max(Posición larga ,|Posición corta |)
> k k k
> o − 100%
> p
> i 0.65∗Min(Posición larga ,|Posición corta |)
> T k k
> ∑E*P
> B
> Posición bruta
> o k 100%
> p =Max(abs(posición larga ),abs(Posición corta ))
> i k k
> T"

> **TN:** "Posición larga / Posición corta" are rendered "Long position / Short position". The two formulas and Table 14 are reproduced in the Original Spanish blockquote in pdfplumber's extraction order, in which the formula body and the "k" subscripts split across lines and the "Tipo A"/"Tipo B" row labels extract as the rotated characters "A o p i T" and "B o p i T" (vertical cell text); the English presents them linearised and row-first.

### Cross-references
- Ley 21.521 Art. 11 — capital requirement implemented.
- NCG 502 §V.A — Block 3 classification to which this requirement applies (item a)).
- NCG 502 §V.D.4.1 — published list of "Type A" crypto-assets.
- NCG 502 §V.D — crypto-asset amount as a component of the total adjusted-equity requirement.

> **Source:** NCG 502 §V.D.4 (12-ene-2024).

---

## V.D.4.1 — List of Type A Crypto-Assets
**NCG anchor:** N° 502, Sección V, D.4.1
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, crypto-assets, type-a, partial-offset, list

### Plain-English text

Table 15 defines the list of Type A crypto-assets, eligible for applying the partial-offset criterion.

**Table 15. List of Type A crypto-assets**

| Name | Code |
|---|---|
| Bitcoin | BTC |
| Ethereum | ETH |
| Tether | USDT |
| BNB | BNB |
| XRP | XRP |
| USD Coin | USDC |
| Cardano | ADA |
| Dogecoin | DOGE |

### Original Spanish

> "D.4.1. LISTADO DE CRIPTOACTIVOS TIPO A
>
> La Tabla 15 define el listado de criptoactivos de Tipo A, elegibles para aplicar el criterio de compensación parcial.
>
> Tabla 15. Listado de criptoactivos de Tipo A
>
> Nombre Código
> Bitcoin BTC
> Ethereum ETH
> Tether USDT
> BNB BNB
> XRP XRP
> USD Coin USDC
> Cardano ADA
> Dogecoin DOGE"

> **TN:** Table 15 is reproduced in the Original Spanish blockquote in pdfplumber's extraction order (which here happens to be row-first); the English table mirrors it.

### Cross-references
- Ley 21.521 Art. 11 — capital requirement implemented.
- NCG 502 §V.D.4 — partial-offset criterion applied to the "Type A" assets listed here.

> **Source:** NCG 502 §V.D.4.1 (12-ene-2024).

---

## V.D.5 — General Provisions
**NCG anchor:** N° 502, Sección V, D.5
**Implements:** Ley 21.521 Art. 11 (capital / guarantee requirements)
**Tags:** capital, guarantees, non-compliance-reporting, monitoring-systems

### Plain-English text

a) When a financial-service provider (PSF) incurs, for any cause, non-compliance with any of the conditions prescribed in this regulation, it must give notice by means of the official channel for communication and submission of information between the Commission (CMF) and its supervised entities before 18:00 hours of the business day following the one on which the non-compliance was detected.

b) The financial-service provider (PSF) must have systems that enable it to know the status of permanent compliance with the minimum-equity and guarantee conditions required by this regulation. The Commission (CMF) may require at any time the background information and records that account for that compliance.

### Original Spanish

> "D.5. DISPOSICIONES GENERALES
>
> a) Cuando un prestador de servicios financieros incurra por cualquier causa en incumplimiento de alguna de las condiciones prescritas en esta norma, deberá dar aviso por medio del canal oficial de comunicación y envío de información entre la Comisión y sus fiscalizados antes de las 18:00 horas del día hábil siguiente a aquel en que se advirtió el incumplimiento.
>
> b) El prestador de servicios financieros deberá contar con sistemas que le permitan conocer el estado de cumplimiento permanente de las condiciones de patrimonio mínimo y garantías requeridas por la presente norma. La Comisión podrá requerir en cualquier momento los antecedentes y registros que den cuenta de dicho cumplimiento."

### Cross-references
- Ley 21.521 Art. 11 — capital/guarantee requirements whose compliance these provisions safeguard.
- NCG 502 §V.B and §V.C — minimum-equity and guarantee / adjusted-equity conditions to be monitored.

> **Source:** NCG 502 §V.D.5 (12-ene-2024).

---

<!-- source: corpus/ncg/502-psf-obligations-consolidated/seccion-06-09-disposiciones-finales.md -->
## FILE: corpus/ncg/502-psf-obligations-consolidated/seccion-06-09-disposiciones-finales.md

# NCG 502 — Secciones VI–IX: Final Provisions (Disposiciones Finales)

**Regulation:** NCG 502 consolidated — baseline 12-ene-2024 as amended by NCG 524 (02-dic-2024). Amended sections carry a `> **Source:**` footer naming the 524 item(s); see `../524-amendments-changelog/changes.md`.
_law:_ NCG-502

---

## VI — Operational Capacity
**NCG anchor:** N° 502, Sección VI
**Implements:** Ley 21.521 Art. 5 (registration / operational readiness) and Art. 7 (authorization to provide services — operational-capacity condition)
**Tags:** operational-capacity, authorization, infrastructure, stress-testing

### Plain-English text

Those who provide the alternative trading system (sistema alternativo de transacción), order routing (enrutamiento de órdenes), and intermediation and custody of financial instruments (intermediación y custodia de instrumentos financieros) services must have the operational capacity (capacidad operacional) to support the processing of the transactions or operations carried out through their systems or infrastructure, in accordance with what is established in Article 7 of Ley N° 21.521.

To evidence that operational capacity, the applicant, at the time of requesting authorization for the services, must declare — identifying itself by means of the electronic mechanism provided for those purposes on the Commission (CMF)'s website — that its systems and infrastructure will be in a position to process the projected transactions or operations once it has the Commission (CMF)'s authorization to carry out the service, and those estimated for the following three years. For those purposes, it must attach a description of the estimates made regarding the current and future capacity of its systems and infrastructure by type of service, expressing the capacity thereof as the maximum number of transactions or operations that may be carried out per unit of time and reporting the functional testing performed to verify that capacity, including the stress tests (pruebas de stress o tensión) carried out to determine the headroom with respect to expected demand and the procedures defined to monitor and adjust the operational capacity. In the case of those who provide the intermediation or custody of financial instruments services and are classified in Block 2 and Block 3 referred to in Section IV of this regulation, they must additionally attach a compliance report (informe de cumplimiento) issued by a third party regarding the reliability and sufficiency of the tests performed by the entity, as well as their results. That third party must be a firm that, within its lines of business, contemplates the assessment of the operational capacity of systems, a circumstance that shall be evidenced by means of the declaration that the applicant for the respective authorization will make in that regard.

### Original Spanish

> "VI. CAPACIDAD OPERACIONAL
>
> Quienes presten el servicio de sistema alternativo de transacción, enrutamiento de órdenes, intermediación y custodia de instrumentos financieros deberán contar con la capacidad operacional para soportar el procesamiento de las operaciones o transacciones que mediante sus sistemas o infraestructura se realicen conforme a lo establecido en el artículo 7 de la Ley N°21.521.
>
> Para acreditar dicha capacidad operacional el solicitante, al momento de requerir la autorización de los servicios, deberá declarar, identificándose mediante el mecanismo electrónico dispuesto para esos efectos en el sitio en Internet de la Comisión, que sus sistemas e infraestructura estarán en condiciones de procesar las operaciones o transacciones proyectadas una vez que cuente con la autorización de la Comisión para llevar a cabo el servicio y las estimadas para los próximos tres años. Para esos efectos deberá acompañar una descripción de las estimaciones realizadas sobre la capacidad actual y futura de sus sistemas e infraestructura por tipo de servicio, expresando la capacidad de los mismos como número máximo de operaciones o transacciones que se podrán realizar por unidad de tiempo y dando cuenta de las pruebas de funcionamiento realizadas para verificar dicha capacidad, incluyendo las pruebas de stress o tensión que se hubieren efectuado para determinar la holgura respecto a la demanda esperada y los procedimientos definidos para monitorear y ajustar la capacidad operacional. Tratándose de quienes presten los servicios de intermediación o custodia de instrumentos financieros y estén clasificadas en el Bloque 2 y 3 al que se refiere la Sección IV de esta normativa, además deberán acompañar un informe de cumplimiento efectuada por un tercero respecto de la confiabilidad y suficiencia de las pruebas realizadas por la entidad, así como también de sus resultados. Dicho tercero deberá ser una empresa que, dentro de sus líneas de negocio, contemple la evaluación de la capacidad operacional de sistemas, circunstancia que se acreditará mediante la declaración que respecto a esa circunstancia hará el solicitante de la autorización respectiva."

### Cross-references
- Ley 21.521 Art. 7 — establishes the authorization-to-provide-services regime, including the operational-capacity condition that this section operationalizes.
- Ley 21.521 Art. 5 — registration prerequisite; operational readiness is assessed at the authorization stage that follows registration.
- NCG 502 §IV — the corporate-governance and risk-management section that defines the Block 2 / Block 3 classification referenced in the third-party certification requirement.
- NCG 502 §II — the service-authorization section whose application triggers the operational-capacity declaration required here.

> **Source:** NCG 502 §VI (12-ene-2024), as amended by NCG 524 item F.1 (02-dic-2024).

---

## VII — Inherent Activities
**NCG anchor:** N° 502, Sección VII
**Implements:** Ley 21.521 Art. 5 (scope of activities inherent to regulated services — permitted without separate authorization as complementary activity)
**Tags:** inherent-activities, permitted-activities, complementary-activity, scope

### Plain-English text

For the purposes of Article 5 of Ley Fintec (Ley 21.521), the following activities are deemed inherent (inherentes) to the activity regulated by law and may therefore be carried out without requiring authorization as a complementary activity (actividad complementaria):

a) Carrying out foreign-exchange transactions (operaciones de cambio de divisas), for those who have the intermediation and custody of financial instruments activity authorized.

b) Tax advisory (asesoría tributaria) and financial planning (planificación financiera), for those who have the investment advisory or credit advisory activity authorized.

c) Studies related to financial, micro-economic, or macro-economic matters, for those who have the investment advisory, credit advisory, or intermediation of financial instruments activity authorized.

d) Generation, commercialization, and dissemination of reports containing credit or commercial information, for those who have the credit advisory or intermediation of financial instruments activity authorized.

e) Collection and exercise of rights, for those who have intermediation or custody of financial instruments authorized.

f) Commercialization and development of technological tools for the provision of financial services or support for the same, to the extent they are related to the services authorized to the entity.

g) Investment of own capital (capital propio) in financial instruments and securities.

h) Investment-limit control for clients, for those who have the intermediation or custody of financial instruments activity authorized.

i) Referring clients or acting as agents (mandatarios) for the sole reception of client orders from third parties authorized in Chile or abroad to act as intermediaries, for those who have the order routing, credit advisory, and investment advisory activity authorized.

j) Channelling orders to domestic or international entities, for those who have the order routing activity authorized.

k) Compilation, processing, communication, and processing of data on financial obligations and commercial reports, for those who have the credit advisory activity authorized.

> **TN:** Item k) reproduces the PDF's apparent double use of "tratamiento" and "procesamiento" in the same sentence ("Compilación, tratamiento, comunicación y procesamiento de datos…"). Both are rendered as stated; "tratamiento" → "processing" and "procesamiento" → "processing" are near-synonyms in context, but the Spanish distinguishes them. The English is rendered faithfully following the PDF.

l) Intermediation of publicly offered securities (valores de oferta pública) exempt from registration in the registries kept by the Commission (CMF), for those who have the intermediation of financial instruments activity authorized.

m) Channelling of orders for the purchase or sale of publicly offered securities exempt from registration in the registries kept by the Commission (CMF), for those who have the order routing activity authorized.

n) Custody of publicly offered securities exempt from registration in the registries kept by the Commission (CMF), for those who have the custody of financial instruments activity authorized.

o) Financial education services (servicios de educación financiera).

The foregoing is without prejudice to the complementary activities that this Commission (CMF) may authorize by regulation (normativa).

### Original Spanish

> "VII. ACTIVIDADES INHERENTES
>
> Para efectos de lo establecido en el artículo 5 de la Ley Fintec, se reputan inherentes al giro regulado por ley y, por tanto, pueden realizarse sin que se requiera de su autorización como actividad complementaria, las siguientes actividades:
>
> a) Realización de operaciones de cambio de divisas, para quienes tienen autorizada la actividad de intermediación y custodia de instrumentos financieros.
>
> b) Asesoría tributaria y de planificación financiera, para quienes tienen autorizada la actividad de asesoría de inversión o asesoría crediticia.
>
> c) Estudios relacionados con ámbitos financieros o micro o macroeconómicos, para quienes tienen autorizada la actividad de asesoría de inversión, asesoría crediticia o intermediación de instrumentos financieros.
>
> d) Generación, comercialización y difusión de reportes con información crediticia o comercial, en el caso de quienes tienen autorizada la actividad de asesoría crediticia o intermediación de instrumentos financieros.
>
> e) Cobranza y ejercicio de derechos, para quienes tienen autorizado intermediación o custodia de los instrumentos financieros.
>
> f) Comercialización y desarrollo de herramientas tecnológicas para la prestación de servicios financieros o de soporte a los mismos, en la medida que tengan relación con los servicios autorizados a la entidad.
>
> g) Inversión del capital propio en instrumentos financieros y valores.
>
> h) Control de límites de inversión para clientes, para quienes tienen autorizada la actividad de intermediación o custodia de instrumentos financieros.
>
> i) Referir clientes o actuar como mandatarios para la sola recepción de órdenes de clientes por terceros habilitados en Chile o en el extranjero para actuar como intermediarios, en el caso de quienes tienen autorizada la actividad de enrutador de órdenes, de asesoría crediticia y de asesoría de inversión.
>
> j) Canalizar órdenes hacia entidades nacionales o internacionales, para quienes tienen autorizada la actividad de enrutador de órdenes.
>
> k) Compilación, tratamiento, comunicación y procesamiento de datos de obligaciones económicas e informes comerciales, para quienes tienen autorizada la actividad de asesoría crediticia.
>
> l) Intermediación de valores de oferta pública exceptuados de su inscripción en los registros que lleva la Comisión, para quienes tienen autorizada la actividad de intermediación de instrumentos financieros.
>
> m) Canalización de órdenes para la compra o venta de valores de oferta pública exceptuados de su inscripción en los registros que lleva la Comisión, para quienes tienen autorizada la actividad de enrutador de órdenes.
>
> n) Custodia de valores de oferta pública exceptuados de su inscripción en los registros que lleva la Comisión, para quienes tienen autorizada la actividad de custodia de instrumentos financieros.
>
> o) Servicios de educación financiera
>
> Lo anterior sin perjuicio de las actividades complementarias que esta Comisión autorice mediante normativa."

### Cross-references
- Ley 21.521 Art. 5 — designates which activities are inherent to the regulated services, thereby permitting them without separate complementary-activity authorization; this section implements the CMF's listing of those activities.
- Ley 21.521 Art. 7 — the service-authorization framework; inherent activities under this section do not require separate authorization thereunder.
- NCG 502 §II — the authorization-to-provide-services section; inherent activities listed here fall outside its requirements.

> **Source:** NCG 502 §VII (12-ene-2024), as amended by NCG 524 item G.1 (02-dic-2024).

---

## VIII — Records (Registros)
**NCG anchor:** N° 502, Sección VIII
**Implements:** Ley 21.521 Art. 9 (record-keeping obligations for registered service providers)
**Tags:** records, registros, recordkeeping, client-identification, transactions, custody

### Plain-English text

Entities registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) must maintain at least the records established in this section for each of the services regulated by Ley N° 21.521 that the entity provides. The mechanisms or systems that entities use to maintain those records must ensure that the information contained therein remains complete and unalterable over time. In turn, such mechanisms and systems must enable the entity to respond in a timely manner, and in the established formats, to the requirements made by the Commission (CMF) by means of the regulation that establishes the Information System Manual (Manual de Sistema de Información) for the entities of Ley N° 21.521.

**VIII.1 — Investment Advisory.** Those who provide the investment advisory service must maintain at least the following information:

| Record type | Information | Description |
|---|---|---|
| Clients | Client identification | All data that allows the client to be individualized, such as RUT, full name, nationality, domicile, whether they are Qualified or Institutional when this has been verified, and what their relationship with the entity is, in the event they are related to it, among other information required by regulation. |
| Clients | Identification of the representative and those who may act on behalf of the client | All data that allows those acting on behalf of the client before the entity to be individualized, such as RUT and full name. |
| Clients | Last active-client condition | Date of the last interaction with the entity that gave it the character of active client, as well as the type of interaction that conferred that character. |
| Accredited | Identification of the person who, in accordance with this regulation and NCG N° 503, must hold knowledge accreditation | All data that allows the accredited person and the reason for accreditation to be individualized, such as RUT, full name, date of accreditation, type of accreditation or exception, date of last training, function performed, among other information required by regulation. |

**VIII.2 — Credit Advisory.** Those who provide the credit advisory service must maintain at least the following information:

| Record type | Information | Description |
|---|---|---|
| Clients | Client identification | All data that allows the client to be individualized, such as RUT, full name, nationality, domicile, whether they are Qualified or Institutional when this has been verified, and what their relationship with the entity is, in the event they are related to it, among other information required by regulation. |
| Clients | Identification of the representative and those who may act on behalf of the client | All data that allows those acting on behalf of the client before the entity to be individualized, such as RUT, full name. |
| Clients | Last active-client condition | Date of the last interaction with the entity that gave it the character of active client, as well as the type of interaction that conferred that character. |
| Accredited | Identification of the person responsible for verifying the coherence of the algorithms, in the event the evaluations emanate from them, or from whom the credit evaluation emanates | All data that allows identifying the persons, who require an approved academic program, designated by the credit advisor as responsible for verifying the coherence of the algorithm or from whom the credit evaluations or identity verifications emanate, such as RUT, full name, date of completion of the academic program, type of academic program, date of last training, function performed, among other information required by regulation. |

**VIII.3 — Crowdfunding Platform.** Those who provide the crowdfunding platform service must store the following information:

| Record type | Information | Description |
|---|---|---|
| Clients | Client identification | All data that allows the client to be individualized, such as RUT, full name, nationality, domicile, whether they are Qualified or Institutional when this has been verified, and what their relationship with the entity is, in the event they are related to it, among other information required by regulation. |
| Clients | Identification of the representative and those who may act on behalf of the client | All data that allows those acting on behalf of the client before the entity to be individualized, such as RUT, full name. |
| Clients | Last active-client condition | Date of the last interaction with the entity that gave it the character of active client, as well as the type of interaction that conferred that character. |
| Projects or financing needs | Information that allows identifying the project, the form of financing, and the person in charge of it or who obtains financing | All data that allows the person or entity that requires financing to be individualized, the manner in which it will be carried out, and who acts for that person. |
| Persons who participate in the financing | Identification of the persons | All data that allows those who participate in the financing to be individualized, such as RUT, full name, nationality, domicile, whether they are Qualified or Institutional when this has been verified, and what their relationship with the entity is, in the event they are related to it, among other information required by regulation. In the event that information is contained in the client registry, the RUT of the person participating in the financing shall suffice. |

**VIII.4 — Alternative Trading System.** Those who provide the alternative trading system service must maintain at least the following information:

| Record type | Information | Description |
|---|---|---|
| Clients | Client identification | All data that allows the client to be individualized, such as RUT, full name, nationality, domicile, whether they are Qualified or Institutional when this has been verified, and what their relationship with the entity is, in the event they are related to it, among other information required by regulation. |
| Clients | Identification of the representative and those who may act on behalf of the client | All data that allows those acting on behalf of the client before the entity to be individualized, such as RUT, full name. |
| Clients | Last active-client condition | Date of the last interaction with the entity that gave it the character of active client, as well as the type of interaction that conferred that character. |
| Transactions | Information detailing all transactions carried out through the system | All data of the transaction, that is, date, time, identification of the buyer, seller, or counterparty to the contract, price or rate, amount, currency, etc. |

**VIII.5 — Intermediation of Financial Instruments.** Those who provide the intermediation of financial instruments service must maintain at least the following information:

| Record type | Information | Description |
|---|---|---|
| Clients | Client identification | All data that allows the client to be individualized, such as RUT, full name, nationality, domicile, whether they are Qualified or Institutional when this has been verified, and what their relationship with the entity is, in the event they are related to it, among other information required by regulation. |
| Clients | Identification of the representative and those who may act on behalf of the client | All data that allows those acting on behalf of the client before the entity to be individualized, such as RUT, full name. |
| Clients | Last active-client condition | Date of the last interaction with the entity that gave it the character of active client, as well as the type of interaction that conferred that character. |
| Orders | Order information | All data that allows knowing the instructions received from the client, that is, date, time, instrument, type of order (purchase, sale, long or short position). In addition, the identification data of whoever gave those instructions on behalf of the client or of the order router, as applicable. |
| Transactions | Information on transactions | All data of the transaction by means of which the client's order was executed, or of the acquisitions or disposals made by the intermediary itself, that is, date and time of the transaction, date agreed for settlement if applicable, identification of the buyer, seller, or counterparty to the contract, price or rate, amount, currency, etc. |

**VIII.6 — Custody of Financial Instruments.** Those who provide the custody of financial instruments service must maintain at least the following information:

| Record type | Information | Description |
|---|---|---|
| Clients | Client identification | All data that allows the client to be individualized, such as RUT, full name, nationality, domicile, whether they are Qualified or Institutional when this has been verified, and what their relationship with the entity is, in the event they are related to it, among other information required by regulation. |
| Clients | Identification of the representative and those who may act on behalf of the client | All data that allows those acting on behalf of the client before the entity to be individualized, such as RUT, full name. |
| Clients | Last active-client condition | Date of the last interaction with the entity that gave it the character of active client, as well as the type of interaction that conferred that character. |
| Custody | Information on instruments in custody | All data that allows knowing the instruments in custody, their movements and owners, such as client identification, instrument identification code, balance, deposits, withdrawals, deficit, surplus, etc. |
| Exercise of rights | Information on the exercise of rights arising from the instrument | All data of collection transactions, exercise of voting rights, and exercise of other rights arising from the instrument, such as client identification, instrument identification, date of exercise, type of right, amount or quantity, etc. |

### Original Spanish

> "VIII. REGISTROS
>
> Las entidades inscritas en el Registro de Prestadores de Servicios Financieros deberán mantener a lo menos los registros que en la presente sección se establecen para cada uno de los servicios regulados por la Ley N°21.521 que preste la entidad. Los mecanismos o sistemas que empleen las entidades para mantener esos registros deben asegurar que la información en ella contenida permanecerá íntegra e inalterable en el tiempo. A su vez, tales mecanismos y sistemas deberán permitir a la entidad responder de manera oportuna, y en los formatos establecidos, a los requerimientos que efectúe la Comisión mediante normativa que establece el Manual de Sistema de Información de las entidades de la Ley N°21.521.
>
> VIII.1. ASESORÍA DE INVERSIÓN
>
> Quienes presten el servicio de asesoría de inversión deberán mantener a lo menos la siguiente información:
>
> Clientes — Identificación del cliente: Todos los datos que permitan individualizar al cliente, tales como RUT, nombre completo, nacionalidad, domicilio, si es Calificado o Institucional cuando ello haya sido verificado, y cuál es su relación con la entidad, en caso de que fuere relacionado a ésta, entre otra información exigida por normativa. Identificación del representante y quienes pueden actuar a nombre del cliente: Todos los datos que permitan individualizar a quienes actúan por cuenta del cliente frente a la entidad, tales como RUT y nombre completo. Ultima condición de cliente activo: Fecha de la última interacción con la entidad y que le dio el carácter de cliente activo, así como el tipo de interacción que le dio ese carácter. Acreditados — Identificación de la persona que, conforme a la presente normativa y la NCG N°503 debe contar con acreditación de conocimientos: Todos los datos que permitan individualizar a la persona acreditada y la razón de acreditación, tales como RUT, nombre completo, fecha de acreditación, tipo de acreditación o excepción, fecha de última capacitación, función que desempeña, entre otra información exigida por normativa.
>
> VIII.2. ASESORÍA CREDITICIA
>
> Quienes presten el servicio de asesoría crediticia deberán mantener a lo menos la siguiente información:
>
> Clientes — Identificación del cliente: Todos los datos que permitan individualizar al cliente, tales como RUT, nombre completo, nacionalidad, domicilio, si es Calificado o Institucional cuando ello haya sido verificado, y cuál es su relación con la entidad, en caso de que fuere relacionado a ésta, entre otra información exigida por normativa. Identificación del representante y quienes pueden actuar a nombre del cliente: Todos los datos que permitan individualizar a quienes actúan por cuenta del cliente frente a la entidad, tales como RUT, nombre completo. Ultima condición de cliente activo: Fecha de la última interacción con la entidad y que le dio el carácter de cliente activo, así como el tipo de interacción que le dio ese carácter. Acreditados — Identificación de la persona responsable de verificar la coherencia de los algoritmos, en caso de que las evaluaciones emanen de ellos, o de la cual emana la evaluación crediticia: Todos los datos que permitan identificar a las personas, que requieren un programa académico aprobado, designado por el asesor crediticio como responsable en verificar la coherencia del algoritmo o de la cual, emana las evaluaciones crediticias o las verificaciones de identidad, tales como RUT, nombre completo, fecha de realización del programa académico, tipo de programa académico, fecha de última capacitación, función que desempeña, entre otra información exigida por normativa.
>
> VIII.3. PLATAFORMA DE FINANCIAMIENTO COLECTIVO
>
> Quienes presten el servicio de plataforma de financiamiento colectivo deberán almacenar la siguiente información:
>
> Clientes — Identificación del cliente: Todos los datos que permitan individualizar al cliente, tales como RUT, nombre completo, nacionalidad, domicilio, si es Calificado o Institucional cuando ello haya sido verificado, y cuál es su relación con la entidad, en caso de que fuere relacionado a ésta, entre otra información exigida por normativa. Identificación del representante y quienes pueden actuar a nombre del cliente: Todos los datos que permitan individualizar a quienes actúan por cuenta del cliente frente a la entidad, tales como RUT, nombre completo. Ultima condición de cliente activo: Fecha de la última interacción con la entidad y que le dio el carácter de cliente activo, así como el tipo de interacción que le dio ese carácter. Proyectos o necesidades de financiamiento — Información que permita identificar el proyecto, la forma de financiamiento y la persona a cargo de este o que obtiene financiamiento: Todos los datos que permitan individualizar a la persona o entidad que requiere de financiamiento, la forma en que será efectuado este y quien actúa por dicha persona. Personas que concurren al financiamiento — Identificación de las personas: Todos los datos que permitan individualizar a quienes concurran al financiamiento, tales como RUT, nombre completo, nacionalidad, domicilio, si es Calificado o Institucional cuando ello haya sido verificado, y cuál es su relación con la entidad, en caso de que fuere relacionado a ésta, entre otra información exigida por normativa. En caso de que esa información esté contenida en el registro de clientes, bastará con el RUT de la persona que concurre al financiamiento.
>
> VIII.4. SISTEMA ALTERNATIVO DE TRANSACCIÓN
>
> Quienes presten el servicio de sistema alternativo de transacción deberán mantener a lo menos la siguiente información:
>
> Clientes — Identificación del cliente: Todos los datos que permitan individualizar al cliente, tales como RUT, nombre completo, nacionalidad, domicilio, si es Calificado o Institucional cuando ello haya sido verificado, y cuál es su relación con la entidad, en caso de que fuere relacionado a ésta, entre otra información exigida por normativa. Identificación del representante y quienes pueden actuar a nombre del cliente: Todos los datos que permitan individualizar a quienes actúan por cuenta del cliente frente a la entidad, tales como RUT, nombre completo. Ultima condición de cliente activo: Fecha de la última interacción con la entidad y que le dio el carácter de cliente activo, así como el tipo de interacción que le dio ese carácter. Transacciones — Información con el detalle de todas las transacciones efectuadas a través del sistema: Todos los datos de la operación, esto es, fecha, hora, identificación del comprador, vendedor o contraparte del contrato, precio o tasa, monto, moneda, etc.
>
> VIII.5. INTERMEDIACIÓN DE INSTRUMENTOS FINANCIEROS
>
> Quienes presten el servicio de intermediación de instrumentos financieros deberán mantener a lo menos la siguiente información:
>
> Clientes — Identificación del cliente: Todos los datos que permitan individualizar al cliente, tales como RUT, nombre completo, nacionalidad, domicilio, si es Calificado o Institucional cuando ello haya sido verificado, y cuál es su relación con la entidad, en caso de que fuere relacionado a ésta, entre otra información exigida por normativa. Identificación del representante y quienes pueden actuar a nombre del cliente: Todos los datos que permitan individualizar a quienes actúan por cuenta del cliente frente a la entidad, tales como RUT, nombre completo. Ultima condición de cliente activo: Fecha de la última interacción con la entidad y que le dio el carácter de cliente activo, así como el tipo de interacción que le dio ese carácter. Ordenes — Información de la orden: Todos los datos que permitan conocer las instrucciones recibidas del cliente, esto es, fecha, hora, instrumento, tipo de orden (compra, venta, posición larga o corta). Además, los datos de identificación de quien dio esas instrucciones por cuenta del cliente o del enrutador, según corresponda. Operaciones — Información de las operaciones: Todos los datos de la operación mediante la que se ejecutó la orden del cliente, o de las adquisiciones o enajenaciones que hizo el propio intermediario, esto es, fecha y hora de la operación, fecha pactada para la liquidación si correspondiere, identificación del comprador, vendedor o contraparte del contrato, precio o tasa, monto, moneda, etc.
>
> VIII.6. CUSTODIA DE INSTRUMENTOS FINANCIEROS
>
> Quienes presten el servicio de custodia de instrumentos financieros deberán mantener a lo menos la siguiente información:
>
> Clientes — Identificación del cliente: Todos los datos que permitan individualizar al cliente, tales como RUT, nombre completo, nacionalidad, domicilio, si es Calificado o Institucional cuando ello haya sido verificado, y cuál es su relación con la entidad, en caso de que fuere relacionado a ésta, entre otra información exigida por normativa. Identificación del representante y quienes pueden actuar a nombre del cliente: Todos los datos que permitan individualizar a quienes actúan por cuenta del cliente frente a la entidad, tales como RUT, nombre completo. Ultima condición de cliente activo: Fecha de la última interacción con la entidad y que le dio el carácter de cliente activo, así como el tipo de interacción que le dio ese carácter. Custodia — Información de los instrumentos en custodia: Todos los datos que permitan conocer los instrumentos en custodia, sus movimientos y propietarios, tales como, identificación del cliente, código de identificación del instrumento, saldo, ingresos, egresos, déficit, superávit, etc. Ejercicio de derechos — Información del ejercicio de derechos emanados del instrumento: Todos los datos de las operaciones de cobro, de ejercicio de derechos de voto y ejercicio demás derechos que emanen del instrumento, tales como identificación del cliente, identificación del instrumento, fecha de ejercicio, tipo de derecho, monto o cuantía, etc."

### Cross-references
- Ley 21.521 Art. 9 — record-keeping and information obligations that this section operationalizes per service.
- NCG 502 §III — disclosure-and-information-delivery section whose underlying client/transaction data is captured by these records.
- NCG 502 Anexo N°1 — defines "cliente activo," "Calificado," and "Institucional" terms used in the record descriptions.
- NCG 503 — the knowledge-accreditation regulation cross-referenced in the VIII.1 accredited-persons record.

> **TN:** NCG 524 spliced text into an existing sentence here; consolidated Spanish is faithful (verified against the 524 source PDF) but is not contiguous in either single source PDF. The §VIII record tables (VIII.1–VIII.6) are transcribed as flat prose because pdfplumber extracts the 524 PDF's three-column record tables in a column-interleaved order that breaks descriptions mid-sentence; individual cell passages match the 524 PDF, but the aggregated section block reaches only ~0.24 chunk-coverage against either source PDF.

> **Source:** NCG 502 §VIII (Registros) — inserted by NCG 524 item G.1 (02-dic-2024); replaces the former §VIII (Derogación), now renumbered §X.

---

## IX — Additional Provisions (Disposiciones Adicionales)
**NCG anchor:** N° 502, Sección IX
**Implements:** Ley 21.521 (cross-service prudential and reporting obligations)
**Tags:** additional-provisions, disposiciones-adicionales, financial-statements, external-audit, risk-management, custody

### Plain-English text

1. Entities that provide two or more of the services regulated by Ley N° 21.521 shall be subject to the highest requirements, in matters of corporate governance and risk management, of the different Blocks to which they belong.

2. Those who provide the intermediation or custody of financial instruments service must submit their quarterly Financial Statements to the Commission (CMF), in accordance with the format and on the date established by regulation. The same obligation applies to those who provide the crowdfunding platform and alternative trading system services and are in Block 3.

3. Those who provide the custody of financial instruments service shall have the obligation to carry out, at least once a year, a report issued by an external audit firm with the opinion regarding the accuracy of the balances of instruments and monies held by the entity in custody as of 30 June of each year. That report must be submitted to the Commission (CMF) no later than August of the respective year. This obligation shall apply as from the year following that of authorization of the custody of financial instruments activity by this Commission (CMF).

4. As an input to assign a global rating of the quality of risk management of entities that provide the crowdfunding platform and alternative trading system services, this Commission (CMF) may request the submission of a certification or risk-management evaluation or an agreed-upon-procedures report, carried out by an external audit firm from this Commission (CMF)'s Registry of External Audit Firms (Registro de Empresas de Auditoría Externa). The entity contracted for these purposes may not simultaneously provide the external audit service to the entity.

5. Entities that provide the intermediation or custody of financial instruments services must submit to this Commission (CMF), no later than 30 days after the close of each annual period, a risk-management self-assessment, approved by the board of directors or equivalent body. This assessment must consider the degree of compliance with the provisions established in section IV.E of this regulation.

6. For the purpose of assigning a global rating of the quality of risk management to entities that provide the intermediation or custody of financial instruments services, this Commission (CMF) may request as an input to carry out this evaluation a certification or risk-management evaluation or an agreed-upon-procedures report carried out by an external audit firm from this Commission (CMF)'s Registry of External Audit Firms. The foregoing does not prevent the Commission (CMF), in qualified cases, from assigning a rating of the quality of risk management in an intermediate period. The entity contracted for these purposes may not simultaneously provide the external audit service to the entity.

### Original Spanish

> "IX. DISPOSICIONES ADICIONALES
>
> 1. A las entidades que presten dos o más servicios de aquellos regulados por la Ley N°21.521 les serán aplicables las exigencias más altas que, en materia de gobierno corporativo y gestión de riesgos, tengan los distintos Bloques a los que pertenezcan.
>
> 2. Quienes presten el servicio de intermediación o custodia de instrumentos financieros, deberán enviar a la Comisión sus Estados Financieros trimestrales, conforme al formato y en la fecha establecida mediante normativa. La misma obligación tendrán quienes presten los servicios de plataforma de financiamiento colectivo y sistema alternativo de transacción y estén en el Bloque 3.
>
> 3. Quienes presten el servicio de custodia de instrumentos financieros tendrán la obligación de efectuar, a lo menos una vez al año, un informe emitido por una empresa de auditoría externa con la opinión respecto a la exactitud de los saldos de instrumentos y dineros mantenidos por la entidad en custodia al 30 de junio de cada año. Dicho informe deberá ser remitido a la Comisión a más tardar en agosto del año respectivo. Esta obligación regirá a contar del año siguiente al de autorización de la actividad de custodia de instrumentos financieros por parte de esta Comisión.
>
> 4. Como insumo para asignar una calificación global de la calidad de la gestión de riesgos de las entidades que presten los servicios de plataformas de financiamiento colectivo y sistemas alternativos de transacción, esta Comisión podrá solicitar el envío de una certificación o evaluación de gestión de riesgos o un informe de procedimiento acordado, efectuado por una empresa de auditoría externa del Registro de Empresas de Auditoría Externa de esta Comisión. La entidad contratada para estos efectos no podrá prestar simultáneamente el servicio de auditoría externa a la entidad.
>
> 5. Las entidades que presten los servicios de intermediación o custodia de instrumentos financieros deberán enviar a esta Comisión a más tardar 30 días después del cierre de cada ejercicio anual una autoevaluación de gestión de riesgos, aprobada por el directorio u órgano equivalente. Esta evaluación deberá considerar el grado de cumplimiento de las disposiciones establecidas en la sección IV.E de la presente normativa.
>
> 6. A efectos de asignar una calificación global de la calidad de la gestión de riesgos a las entidades que presten los servicios de intermediación o custodia de instrumentos financieros, esta Comisión podrá solicitar como insumo para realizar esta evaluación, una certificación o evaluación de gestión de riesgos o un informe de procedimiento acordado efectuado por una empresa de auditoría externa del Registro de Empresas de Auditoría Externa de esta Comisión. Lo anterior, no obsta a que la Comisión, en casos calificados, pueda asignar una calificación de la calidad de la gestión de riesgos en un período intermedio. La entidad contratada para estos efectos no podrá prestar simultáneamente el servicio de auditoría externa a la entidad."

### Cross-references
- Ley 21.521 — overarching framework for the cross-service prudential, reporting, and risk-management obligations consolidated here.
- NCG 502 §IV.E — risk-management quality-evaluation regime referenced by numerals 5 and 6.
- NCG 502 §V — capital/guarantee Block classification referenced by numeral 1 ("highest requirements of the Blocks").
- NCG 502 §XI — entry-into-force clause that defers numeral 5 (self-assessment) to 1 July 2027.

> **Source:** NCG 502 §IX (Disposiciones Adicionales) — inserted by NCG 524 item G.1 (02-dic-2024); replaces the former §IX (Vigencia), now renumbered §XI.

---

## X — Repeal (Derogación)
**NCG anchor:** N° 502, Sección X
**Implements:** n/a (repeal clause)
**Tags:** repeal, derogacion, ncg-493, ncg-494

### Plain-English text

General Regulation N° 493 of 2023 (Norma de Carácter General N° 493 de 2023) and General Regulation N° 494 of 2023 (Norma de Carácter General N° 494 de 2023) are hereby repealed.

### Original Spanish

> "X. DEROGACIÓN
>
> Deróguese la Norma de Carácter General N°493 de 2023 y la Norma de Carácter General N°494 de 2023."

### Cross-references
- NCG 493 (2023) — repealed by this clause upon entry into force of NCG 502.
- NCG 494 (2023) — repealed by this clause upon entry into force of NCG 502.
- NCG 502 §XI — the entry-into-force clause that determines when this repeal takes effect.

> **Source:** NCG 502 §VIII (Derogación) (12-ene-2024), renumbered to §X by NCG 524 item G.1 (02-dic-2024).

---

## XI — Entry into Force (Vigencia)
**NCG anchor:** N° 502, Sección XI
**Implements:** n/a (effective-date clause)
**Tags:** vigencia, entry-into-force, transitional-provisions, investment-advisory

### Plain-English text

This regulation enters into force (entra en vigor) as of 3 February 2024. The foregoing, except for paragraphs 2 and 3 of Title E.7.3 of Section IV, Title E of Section V, and numeral 5 of Section IX, which shall take effect on 1 July 2027.

Accordingly, pursuant to Article 2 of the transitory provisions (disposiciones transitorias) of the Law, providers of crowdfunding platform (plataforma de financiamiento colectivo), alternative trading system (sistema alternativo de transacción), credit advisory (asesoría crediticia), custody of financial instruments (custodia de instrumentos financieros), order routing (enrutamiento de órdenes), and intermediation of financial instruments (intermediación de instrumentos financieros) services must submit the respective applications for registration and authorization for the activities they were carrying out as of the date of entry into force of this regulation before 3 February 2025. It is noted that registration alone does not entitle the relevant entity to provide the services it intends to carry out, which is why it is the responsibility of each entity to procure the authorization for the services it wishes to provide at the same time as its registration, making both applications in parallel and submitting the supporting documents for both processes in a timely manner. In those registration applications, entities may attach audited financial statements of up to 18 months old for purposes of compliance with the provisions established in section II.F, letter e), of this regulation.

Service providers referred to in the second paragraph of this section that do not make the applications to this Commission (CMF) before 3 February 2025, or that have done so within that period but whose application is deemed abandoned (declarada abandonada) for failure to remedy the observations formulated within the period established by the Commission (CMF) or is rejected by it, must refrain from continuing to provide their services for the purpose of entering into new transactions and must carry out only those acts tending toward the conclusion of the transactions regulated by Ley N° 21.521 contracted before that date. Notwithstanding the foregoing, the operation of firms whose authorization application has been submitted within the corresponding period and is under evaluation shall be permitted. In the case of investment advisory (asesoría de inversión) service providers, that deadline shall continue to be the one established in the final paragraph of the entry-into-force section of General Regulation N° 494, that is, before 3 February 2024.

Natural and legal persons (personas naturales y jurídicas) that, as of the date of entry into force of this General Regulation, are registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) must comply with this regulation and submit to this Commission (CMF) the supporting documents for registration and authorization of the investment advisory service before 3 August 2024, through the official channel for communication and submission of information between the Commission (CMF) and its supervised entities. If that deadline passes without the required supporting documents having been submitted, the Commission (CMF) may proceed with the revocation of the respective authorization and cancellation from the Registry. Those persons may continue providing the services referred to in the second paragraph of this section that they were carrying out as of the date of entry into force of this regulation, without prejudice that they must submit the respective authorization applications before 3 February 2025 and shall be subject to what is provided in the preceding paragraph with respect to those services.

Pending applications for registration in the Registry of Financial-Service Providers and for authorization of the investment advisory service that are in process as of the date of issue of this regulation shall be without effect (quedarán sin efecto), and the entities must refrain from providing the investment advisory service for as long as they do not present a new registration and authorization application. In order to continue providing that service while both applications are being processed, they must resubmit them no later than 3 February 2024. If presented after that deadline, they may not provide the investment advisory service while the Commission (CMF) has not granted the respective authorization. Once the procedure is declared abandoned for failure to remedy the observations formulated by the Commission (CMF) within the period established for that purpose, or the application is rejected, the entity may not continue providing the advisory service.

As long as General Regulation N° 503, which establishes the requirements to accredit suitability for the performance of functions, does not enter into force, the accreditation of knowledge by natural persons who carry out investment advisory functions, whether on their own behalf or on behalf of a legal person registered in the Registry of Financial-Service Providers referred to in section A of Section II of this regulation, must be carried out in accordance with what is established in General Regulation N° 412.

For the purposes of what is established in the final paragraph of Titles C and D of Section II of this regulation, the stock exchanges (bolsas de valores) shall have until 3 February 2025 to comply with the information obligations referred to in that paragraph with respect to the crowdfunding platform and alternative trading system services that they are providing or operating as of the present date.

> **TN:** "Ley Fintec" used in §VII is the informal name for Ley N° 21.521 (Ley para Promover la Competencia e Inclusión Financiera a través de la Innovación y Tecnología en la Prestación de Servicios Financieros). The full formal name is used throughout the plain-English translations; "Ley Fintec" is preserved in Spanish quotations.

### Original Spanish

> "XI. VIGENCIA
>
> La presente normativa entra en vigor a contar del 3 de febrero de 2024. Lo anterior, salvo los párrafos 2 y 3 del Título E.7.3. de la sección IV, el título E de la sección V y el numeral 5 de la Sección IX, que entrarán a regir el 1 de julio de 2027.
>
> Por lo anterior, conforme lo dispuesto en el artículo segundo de las disposiciones transitorias de la Ley, los prestadores de los servicios de plataforma de financiamiento colectivo, sistemas alternativos de transacción, asesoría crediticia, custodia de instrumentos financieros, enrutamiento de órdenes e intermediación de instrumentos financieros deberán presentar las respectivas solicitudes de inscripción y autorización para las actividades que estuvieren realizando a la fecha de entrada en vigencia de esta normativa antes del 3 de febrero de 2025. Se hace presente que la sola inscripción no habilita a la respectiva entidad a prestar los servicios que pretende realizar, razón por la que es responsabilidad de cada entidad el procurar obtener, junto con su inscripción, la autorización de los servicios que desea realizar, efectuando ambas solicitudes de manera paralela y acompañando los antecedentes para ambos procesos de forma oportuna. En dichas solicitudes de inscripción las entidades podrán acompañar estados financieros auditados de una antigüedad de hasta 18 meses para efectos del cumplimiento de lo establecido en la sección II.F. en la letra e) de esta normativa.
>
> Los prestadores de servicios a los que se refiere el segundo párrafo de esta sección que no efectúen las solicitudes ante esta Comisión antes del 3 de febrero de 2025, o habiéndola efectuado en ese plazo ésta sea declarada abandonada por no haberse subsanado las observaciones formuladas dentro del plazo establecido por la Comisión o rechazada por ésta, deberán abstenerse de continuar prestando sus servicios para la celebración de nuevas operaciones y deberán realizar únicamente los actos tendientes a la conclusión de las operaciones reguladas en la Ley N°21.521 contratadas antes de la fecha previamente señalada. Sin perjuicio de lo anterior, se permitirá la operación de empresas cuya solicitud de autorización haya sido enviada durante el plazo correspondiente y se encuentren en evaluación. En el caso de los prestadores del servicio de asesoría de inversión dicho plazo seguirá siendo el establecido en el inciso final de la sección de vigencia de la Norma de Carácter General N°494, esto es, antes del 3 de febrero de 2024.
>
> Las personas naturales y jurídicas que a la fecha de entrada en vigencia de la presente Norma de Carácter General se encuentren inscritas en el Registro de Prestadores de Servicios financieros, deberán ajustarse a lo dispuesto en esta normativa y remitir a esta Comisión los antecedentes para la inscripción y autorización del servicio de asesoría de inversión antes del 3 de agosto de 2024, a través del canal oficial de comunicación y envío de información entre la Comisión y sus fiscalizados. Cumplido ese plazo sin haber remitido los antecedentes exigidos, la Comisión podrá proceder a la revocación de la autorización respectiva y a la cancelación en dicho Registro. Dichas personas podrán seguir prestando los servicios a los que se refiere el segundo párrafo de esta sección que estuvieren realizando a la fecha de entrada en vigencia de esta normativa, sin perjuicio de que deberán remitir las respectivas solicitudes de autorización antes del 3 de febrero de 2025 y quedarán sujetos a lo dispuesto en el inciso precedente respecto de tales servicios.
>
> Las solicitudes de inscripción en el Registro de Prestadores de Servicios Financieros y de autorización del servicio de asesoría de inversión que estén pendientes de tramitación a la fecha de emisión de esta normativa quedarán sin efecto, debiendo las entidades abstenerse de prestar el servicio de asesoría de inversión en tanto no presenten una nueva solicitud de inscripción y de autorización. Para poder continuar prestando dicho servicio mientras se tramitan ambas solicitudes, deberán ingresarlas nuevamente a más tardar el 3 de febrero de 2024. En caso de que se presenten con posterioridad a dicho plazo no podrán prestar el servicio de asesoría de inversión mientras la Comisión no hubiere conferido la respectiva autorización. Declarado abandonado el procedimiento por no haberse subsanado las observaciones formuladas por la Comisión dentro del plazo establecido por ésta para ello, o rechazada la solicitud, la entidad no podrá seguir prestando el servicio de asesoría.
>
> En tanto no entre en vigencia la Norma de Carácter General N°503 que establece las exigencias para acreditar la idoneidad para el desempeño de funciones, la acreditación de conocimientos por parte de las personas naturales que desarrollen funciones de asesoría de inversión, sea por sí o por cuenta de una persona jurídica inscrita en el Registro de Prestadores de Servicios Financieros, a la que refiere el apartado A. de la Sección II de la presente normativa, deberá efectuarse de según lo establecido en la Norma de Carácter General N°412.
>
> Para efectos de lo establecido en el último párrafo de los Títulos C. y D. de la Sección II de esta normativa, las bolsas de valores tendrán hasta el 3 de febrero de 2025 para cumplir con las obligaciones de información a que se refiere dicho párrafo respecto de los servicios de plataforma de financiamiento colectivo y sistema alternativos de transacción que estén prestando u operando a la presente fecha."

### Cross-references
- Ley 21.521 Art. 2 (Disposiciones Transitorias, Art. Segundo) — the transitory provision that establishes the grace period for existing service providers to apply for registration and authorization.
- NCG 494 (2023) — the prior investment-advisory regulation whose entry-into-force deadline (3 February 2024) is preserved for investment advisory providers; repealed by §X of this regulation.
- NCG 493 (2023) — the prior regulation repealed by §X.
- NCG 503 — suitability-accreditation regulation; until it enters into force, NCG 412 governs knowledge accreditation for investment-advisory functions.
- NCG 412 — interim knowledge-accreditation regime for investment advisory pending NCG 503.
- NCG 502 §II.F(e) — the audited-financial-statements requirement to which the 18-month transitional allowance applies.
- NCG 502 §II.C / §II.D — the disclosure obligations whose compliance deadline for stock exchanges is set to 3 February 2025.
- NCG 502 §I.A — the registration application procedure that existing registrants must comply with.
- NCG 502 §X — the repeal clause whose effective date is determined by this section.

> **Source:** NCG 502 §IX (Vigencia) (12-ene-2024), as amended and renumbered to §XI by NCG 524 item G.1 (02-dic-2024).

---
