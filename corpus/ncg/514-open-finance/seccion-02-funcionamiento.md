# NCG 514 — Sección II: System Operation (Funcionamiento del Sistema)

**Regulation:** NCG 514 (Sistema de Finanzas Abiertas), 03-jul-2024.
_law:_ NCG-514

## II — System Operation
**NCG anchor:** N° 514, Sección II
**Implements:** Ley 21.521 Art. 21 (interfaces/APIs of the Open Finance System)
**Tags:** open-finance, sfa, system-operation, apis

### Plain-English text

This section governs the operation of the Open Finance System (SFA) (Sistema de Finanzas Abiertas): the means of information exchange (the APIs and their standards, availability, and performance), the alternative mechanism, the Participants Directory, information quality, the contingency-communication mechanisms, and the outsourcing of services. It comprises subsections A (information-exchange means), B (alternative mechanism), C (Participants Directory), D (information quality), E (contingency-communication mechanisms), and F (outsourcing of services). It has no standalone body text of its own; the substantive rules begin at subsection A below.

### Original Spanish

> "SECCIÓN II: FUNCIONAMIENTO DEL SISTEMA"

### Cross-references
- Ley 21.521 Art. 21 — the interfaces/APIs of the SFA, whose operation this section governs.
- NCG 514 §II.A–§II.F — the subsections that make up this section.
- NCG 514 Annex N° 3 — the technical specifications, standards, and parameters referenced throughout this section.

> **Source:** NCG 514 §II (03-jul-2024).

---

## II.A — Information-Exchange Means
**NCG anchor:** N° 514, Sección II, A
**Implements:** Ley 21.521 Art. 21 (interfaces/APIs as the means of information exchange in the SFA)
**Tags:** open-finance, apis, information-exchange, standards

### Plain-English text

This subsection governs the means of information exchange (medios de intercambio de información) of the SFA: the APIs as the principal mechanism, the standards (estándares) those APIs must comply with, and their availability and performance (disponibilidad y rendimiento). It comprises subparagraphs A.1 (principal mechanism), A.2 (standards of the APIs), and A.3 (availability and performance). The substantive rules begin at subparagraph A.1 below.

### Original Spanish

> "A. Medios de intercambio de información"

### Cross-references
- Ley 21.521 Art. 21 — the interfaces/APIs that constitute the SFA's means of information exchange.
- NCG 514 §II.A.1, §II.A.2, §II.A.3 — the subparagraphs that make up this subsection.

> **Source:** NCG 514 §II.A (03-jul-2024).

---

## II.A.1 — Principal Mechanism
**NCG anchor:** N° 514, Sección II, A.1
**Implements:** Ley 21.521 Art. 21 (APIs as the principal mechanism for data access in the SFA)
**Tags:** open-finance, apis, principal-mechanism, endpoints, bilateral

### Plain-English text

The IPI and IPC must make available APIs for the SFA, together with the technical documentation associated with them, necessary to attend to the data-access requests of the SFA submitted by the PSBI and PSIP.

In the context of the SFA, the supervised entities shall not use mechanisms different from the API to attend to data-access requests, without prejudice to what may be provided regarding the use of an alternative mechanism (mecanismo alternativo) regulated by the CMF. The development and maintenance of the APIs shall be the exclusive responsibility of the Participants of the SFA.

The APIs must be enabled on websites that the institutions themselves shall provide for these purposes, and their addresses and technical specifications (endpoints) shall be communicated to the Commission (CMF), remaining available for the use of the PSBI and the PSIP, as applicable, in the SFA Directory and on the terms established in Annex N° 3 of this regulation, in accordance with what is described in Section II.B.

Even when the development of the APIs may be delegated to another company, for all purposes the entity that participates in the system shall be the sole party responsible for them before the Commission (CMF).

The connection and exchange of information between the Participants of the SFA shall be bilateral. The foregoing, regardless of the possibilities of outsourcing (tercerización) of one or more components associated with the communication or the processing and exchange of information, in accordance with the applicable provisions.

### Original Spanish

> "1. Mecanismo principal
>
> Las IPI e IPC deberán poner a disposición APIs para el SFA, junto con la documentación técnica asociada a éstas, necesarias para atender las solicitudes de acceso a los datos del SFA presentadas por los PSBI e PSIP.
>
> En el contexto del SFA, las entidades fiscalizadas no podrán utilizar mecanismos diferentes a las API para atender solicitudes de acceso a datos, sin perjuicio de lo que se disponga respecto del uso de un mecanismo alternativo regulado por la CMF. El desarrollo y mantención de las APIs será de exclusiva responsabilidad de los Participantes del SFA.
>
> Las APIs deberán estar habilitadas en sitios web que las propias instituciones proveerán para estos efectos, y sus direcciones y especificaciones técnicas (endpoints) serán comunicadas a la Comisión, quedando disponibles para el uso de los PSBI y los PSIP, según corresponda, en el Directorio del SFA y en los términos que se establezcan en el Anexo N°3 de esta normativa, de acuerdo con lo descrito en la Sección II.B.
>
> Aun cuando el desarrollo de las APIs pueda ser delegado a otra empresa, para todos los efectos la entidad que participa en el sistema será la única responsable por las mismas ante la Comisión.
>
> La conexión e intercambio de información entre los Participantes del SFA será bilateral. Lo anterior, independientemente de las posibilidades de tercerización de uno o más componentes asociados a la comunicación o el procesamiento e intercambio de la información, conforme con las disposiciones aplicables."

> **TN:** The Spanish "presentadas por los PSBI e PSIP" uses "e" before "PSIP" (a typographical variant of the conjunction "y"); preserved verbatim in the Original Spanish and rendered "and" in English.

### Cross-references
- Ley 21.521 Art. 21 — the APIs/interfaces that this subparagraph fixes as the principal data-access mechanism.
- NCG 514 §II.A.2 — the standards the APIs must comply with.
- NCG 514 §II.B — the alternative mechanism referenced for availability and the Directory.
- NCG 514 Annex N° 3 — the terms governing endpoint communication and availability.

> **Source:** NCG 514 §II.A.1 (03-jul-2024).

---

## II.A.2 — Standards of the APIs
**NCG anchor:** N° 514, Sección II, A.2
**Implements:** Ley 21.521 Art. 21 (technical standards for the SFA interfaces/APIs)
**Tags:** open-finance, apis, standards, openapi, fapi, iso-20022

### Plain-English text

The APIs developed by the Participants must comply with the following standards:

**Table N° 1: Standards of the APIs**

| Element | Standard |
|---|---|
| Specification and design (Especificación y diseño) | OpenAPI (version 3.1) |
| Messaging (Mensajería) | JSON |
| Architecture (Arquitectura) | REST reference framework and its implementation must be RESTful |
| Data Administration Standards and Data Dictionary (Estándares de Administración de Datos y Diccionario de Datos) | ISO 20.022 latest version |
| Authorization and Authentication (Autorización y Autenticación) | OAuth 2.0 and OpenID Connect |
| Security profiles (Perfiles de seguridad) | FAPI 2.0 in accordance with the profiles indicated in Annex N° 3 |
| Exchange protocol (Protocolo de intercambio) | mTLS |

Compliance with these standards must be accredited by means of a report issued by an independent third party and remitted to the Commission (CMF). The specifications, operational flows, and technical dictionaries associated with the concrete implementation of the said standards shall be developed in Annex N° 3 of this regulation, which shall be updated by the Commission (CMF), considering the gradual nature of the SFA's implementation and the continuous improvement of its processes.

**Particular considerations (Consideraciones particulares).** Without prejudice to what is provided in the preceding paragraphs, in the case of the security-profiles standard FAPI in its version 2.0, this shall apply to the design of all the interfaces considered in this regulation, the definition of the profiles and modalities applicable in each case being a matter for Annex N° 3, considering the nature of the information to be exchanged, when it proves necessary.

As regards ISO 20.022, the requirement of a certification or accreditation by a third party with respect to its correct implementation or conformity with that standard shall not be considered. The messages of each interface (including their elements and components) must be adapted to the said technical standard, in accordance with what the context of use in each case determines, and according to what is provided in the specifications indicated in Annex N° 3 of this regulation.

With the aim of minimizing interruptions and maintaining the functionality of the integrations that are implemented, the respective IPI or IPC, in the development of its interfaces, must ensure, to the extent that it is technically and operationally possible, that every new version of such interfaces is compatible with its previous versions. The foregoing, safeguarding that each version complies with the specifications that are provided for these purposes in Annex N° 3.

### Original Spanish

> "2. Estándares de las APIs
>
> Las APIs que desarrollen los Participantes deben cumplir con los siguientes estándares:
>
> Tabla N°1: Estándares de las APIs
>
> ELEMENTO ESTÁNDAR
>
> OpenAPI (versión 3.1)
>
> Especificación y diseño
>
> Mensajería
>
> JSON
>
> Marco de referencia REST y su
>
> Arquitectura implementación debe ser RESTful
>
> Estándares de Administración de Datos ISO 20.022 última versión
>
> y Diccionario de Datos
>
> OAuth 2.0 y OpenID Connect
>
> Autorización y Autenticación
>
> FAPI 2.0 conforme perfiles que se
>
> Perfiles de seguridad indiquen en Anexo N°3
>
> mTLS
>
> Protocolo de intercambio
>
> El cumplimiento de estos estándares deberá ser acreditado mediante informe emanado de un tercero independiente y remitido a la Comisión. Las especificaciones, flujos operacionales y diccionarios técnicos asociados a la implementación concreta de los referidos estándares se desarrollarán en el Anexo N°3 de esta norma, el que será actualizado por parte de la Comisión, considerando la gradualidad de implementación del SFA y la mejora continua de sus procesos.
>
> Consideraciones particulares
>
> Sin perjuicio de lo dispuesto en los párrafos precedentes, tratándose del estándar de perfiles de seguridad FAPI en su versión 2.0, este aplicará para el diseño de todas las interfaces consideradas en la presente Norma, siendo materia del Anexo N°3 la definición de los perfiles y modalidades aplicables en cada caso, considerando la naturaleza de la información a ser intercambiada, cuando resulte necesario.
>
> En lo que respecta al ISO 20.022, no se considerará la exigencia de una certificación o acreditación de un tercero respecto a su correcta implementación o conformidad con dicho estándar. Los mensajes de cada interfaz (incluyendo sus elementos y componentes) deberán adaptarse al referido estándar técnico, conforme así lo determine el contexto de utilización en cada caso, y según lo que se disponga en las especificaciones que se indiquen en el Anexo N°3 de esta Norma.
>
> Con el fin de minimizar las interrupciones y mantener la funcionalidad de las integraciones que se implementen, la respectiva IPI o IPC, en el desarrollo de sus interfaces, deberá velar, en la medida que sea técnica y operativamente posible, que toda nueva versión de tales interfaces sea compatible con sus versiones previas. Lo anterior, resguardando que cada versión cumpla con las especificaciones que para estos efectos se dispongan en el Anexo N°3."

> **TN:** Tabla N° 1 is a two-column table (ELEMENTO / ESTÁNDAR) in the source PDF; the Original Spanish block reproduces the cell text in the PDF's extraction reading order (which interleaves some row labels and values), while the English Plain-English rendering presents it as an ordered label–value table. This page-break/table artifact may keep this section's round-trip coverage below the prose threshold.

### Cross-references
- Ley 21.521 Art. 21 — the SFA interfaces/APIs whose technical standards this subparagraph fixes.
- NCG 514 §II.A.1 — the principal-mechanism rule that these standards qualify.
- NCG 514 Annex N° 3 — the security profiles, operational flows, technical dictionaries, and version-compatibility specifications referenced throughout.

> **Source:** NCG 514 §II.A.2 (03-jul-2024).

---

## II.A.3 — Availability and Performance
**NCG anchor:** N° 514, Sección II, A.3
**Implements:** Ley 21.521 Art. 21 (availability and performance requirements for the SFA interfaces/APIs)
**Tags:** open-finance, apis, availability, performance, ttlb, monitoring

### Plain-English text

The APIs intended for the query of data associated with the information sets indicated in numerals 1 to 3 of Article 17 of the Ley Fintec must be available for use with a minimum uptime of 95% on a daily basis per calendar day and of 99% on a monthly basis, considering a daily calculation base of 24 hours, beginning and ending at midnight.

With respect to the processing time of these APIs, they must process transactions in a maximum time of 4,000 milliseconds, considering the moment at which the API query is made and the TTLB time elapsed for the response, in accordance with the respective timestamps. In the case of endpoints that provide a relevant number of records, and that are duly identified as such in the specifications addressed by Annex N° 3 of this regulation, the performance metric required shall apply per response page, considering up to 100 records per page.

The pagination conditions, including the attributes of the paginated response, the indication of the total of pages of the response and the total of records, and the navigation links between each one, must follow the specifications and guidelines developed in Annex N° 3 of this regulation.

For their part, the APIs intended for the payment-initiation service by an IPC must have a minimum availability of 95% on a daily basis per calendar day and of 99.5% on a monthly basis.

The payment-initiation APIs must process transactions in a maximum time of 800 milliseconds. The maximum processing time indicated shall not consider the execution and confirmation times that payment operations require for their completion in the payment systems underlying the payment initiation.

The availability and performance parameters of the Payment-Initiation APIs must consider the computation precisions indicated in the first and second paragraphs of this numeral.

The minimum availabilities and performances must be met for each API that the IPI and IPC has, and the measurement of these requirements shall not consider the time of the eventual use of the alternative mechanism required to keep the service available, regardless of its nature.

The minimum uptime shall have as an exception for its computation the scheduled maintenance and updates, duly notified to the Commission (CMF), as well as the temporary suspensions that the Commission (CMF) may mandate in the exercise of its powers.

The scheduled maintenance must comply with the requirements as to the type of permitted maintenance, information periods, maximum extension periods, forms of communication, among other critical elements, in accordance with what is set out in Annex N° 3 of this regulation. In no case may the maintenance of the services have a frequency or scheduling such that it impedes the regular provision of the service provided by the PSBI or PSIP.

Without prejudice that the entities must have mechanisms and/or systems that allow them to permanently monitor the performance and availability of their APIs, the reports to the CMF of the respective standards must be sent monthly on a weekly basis, on the terms defined in the formats for the periodic supply of information that the CMF determines through the mechanisms it establishes. The IPI and IPC may contract with third parties monitoring and verification services of the availability and performance of their interfaces, which shall be subject to the regulations on outsourcing of services issued by the Commission (CMF) that are applicable to them. In no case shall the outsourcing of the monitoring, in whole or in part, affect the responsibility that the IPI and IPC have before the Commission (CMF) with respect to the complete and timely reporting of their availability and performance indicators.

Non-compliance with the minimum parameters indicated in this section may be sanctioned by the Commission (CMF) in accordance with its legal powers.

In any event, the performance and availability terms indicated here shall be applicable, without prejudice to the operational limits of maximum concurrent transactions per minute for each interface that are indicated in Annex N° 3 of this regulation.

Exceptionally, during the first two years of currency of this regulation, the minimum monthly availability metrics addressed by this numeral shall be measured on a quarterly basis, considering a 90-day moving average.

### Original Spanish

> "3. Disponibilidad y rendimiento
>
> Las APIs destinadas a la consulta de los datos asociados a los conjuntos de información indicados en los numerales 1 a 3 del artículo 17 de la Ley Fintec, deben estar disponibles para su uso con un tiempo de actividad mínimo del 95% de forma diaria por día calendario y de 99% de forma mensual, considerando una base de cálculo diario de 24 horas, empezando y terminando a medianoche.
>
> Respecto al tiempo de procesamiento de estas API, ellas deberán procesar transacciones en un tiempo máximo de 4.000 milisegundos, considerando el momento en que se realiza la consulta de la API y el tiempo TTLB transcurrido de la respuesta, conforme revelen las marcas de tiempo respectivas. Tratándose de endpoints que provean un número relevante de registros, y que sean debidamente identificados como tales en las especificaciones que da cuenta el Anexo N°3 de esta Norma, la métrica de rendimiento exigida se aplicará por página de respuesta, considerando hasta 100 registros por cada página.
>
> Las condiciones de paginación, incluyendo los atributos de la respuesta paginada, la indicación del total de páginas de la respuesta y el total de registros, y los vínculos de navegación entre cada una, deberán seguir las especificaciones y lineamientos que se desarrollen en el Anexo N°3 de esta Norma.
>
> Por su parte, las APIs destinadas al servicio de iniciación de pagos por parte de una IPC deberán tener una disponibilidad mínima del 95% de forma diaria por día calendario y de 99,5% de forma mensual.
>
> Las APIs de iniciación de pagos deberán procesar transacciones en un tiempo máximo de 800 milisegundos. El tiempo de procesamiento máximo señalado no considerará los tiempos de ejecución y confirmación que las operaciones de pago requieran para su finalización en los sistemas de pago subyacentes a la iniciación de pagos efectuada.
>
> Los parámetros de disponibilidad y rendimiento de las APIs de Iniciación de Pagos deberán considerar las precisiones de cómputo indicadas en el párrafo primero y segundo de este numeral.
>
> Las disponibilidades y rendimientos mínimos deben cumplirse para cada API que tenga la IPI e IPC, y la medición de estas exigencias no deberá considerar el tiempo de la eventual utilización del mecanismo alternativo requerido para mantener disponible el servicio, indistintamente la naturaleza de éste.
>
> El tiempo de actividad mínimo tendrá como excepción para su cómputo las mantenciones y actualizaciones programadas, debidamente avisadas a la Comisión, así como las suspensiones temporales que mandate la Comisión en el ejercicio de sus facultades.
>
> Las mantenciones programadas deberán cumplir con los requerimientos de tipo de mantención permitida, plazos de información, plazos máximos de extensión, formas de comunicación, entre otros elementos críticos, según lo que se consigna en el Anexo N°3 de la presente normativa. En ningún caso las mantenciones de los servicios podrán tener una frecuencia o programación tal que impidan la provisión regular del servicio provisto por los PSBI o PSIP.
>
> Sin perjuicio que las entidades deberán contar con mecanismos y/o sistemas que les permitan monitorear permanentemente el rendimiento y disponibilidad de sus APIs, los reportes a la CMF de los respectivos estándares se deberán enviar mensualmente en base semanal, en los términos que se definan en los formatos de suministro de información periódica que la CMF determine a través de los mecanismos que esta establezca. Las IPI y IPC podrán contratar con terceros servicios de monitoreo y verificación de disponibilidad y rendimiento de sus interfaces, los que se someterán a las normas sobre tercerización de servicios impartidas por la Comisión que les resulten aplicables. En caso alguno la tercerización del monitoreo, en todo o en parte, afectará la responsabilidad que las IPI e IPC tienen frente a la Comisión respecto al reporte completo y oportuno de sus indicadores de disponibilidad y rendimiento.
>
> El incumplimiento de los parámetros mínimos indicados en esta sección podrá ser sancionado por la Comisión de conformidad con sus atribuciones legales.
>
> Con todo, los términos de rendimiento y disponibilidad aquí indicados resultarán aplicables, sin perjuicio de los límites operativos de transacciones máximas concurrentes por minuto para cada interfaz que se indiquen en el Anexo N°3 de esta Norma.
>
> De forma excepcional, durante los dos primeros años de vigencia de la presente Norma, las métricas de disponibilidad mínima mensual que da cuenta el presente numeral se medirán de forma trimestral, considerando una media móvil de 90 días."

### Cross-references
- Ley 21.521 Art. 17 — the information sets (numerals 1 to 3) whose query APIs are subject to these availability and performance requirements.
- Ley 21.521 Art. 21 — the SFA interfaces/APIs whose availability and performance this subparagraph regulates.
- NCG 514 §II.B — the alternative mechanism excluded from availability measurement.
- NCG 514 §II.F — the outsourcing-of-services rules applicable to contracted monitoring.
- NCG 514 Annex N° 3 — the pagination specifications, maintenance requirements, and concurrent-transaction limits referenced.

> **Source:** NCG 514 §II.A.3 (03-jul-2024).

---

## II.B — Alternative Mechanism
**NCG anchor:** N° 514, Sección II, B
**Implements:** Ley 21.521 Art. 21 (alternative information-delivery mechanism for the SFA interfaces/APIs)
**Tags:** open-finance, alternative-mechanism, contingency, interoperability, consent

### Plain-English text

The IPI and IPC must have an alternative mechanism (mecanismo alternativo) for the delivery of information, which operates in the event of unavailability of the interfaces described in this section, below (infra).

For the foregoing, the IPI and the IPC must report to the Commission (CMF), at the time of applying for their incorporation in the roster (nómina), the supporting documents that evidence the effective development of the alternative mechanism determined by this regulation.

The alternative mechanism must consider the following technical requirements, which shall be duly specified in Annex N° 3 of the regulation:

a) Capacity to maintain the service and the delivery of information.

b) Performance metrics of response to the request for or query of information.

c) Security measures such as to allow the monitoring of the information traffic in the alternative mechanism, as well as the active detection of intruders and the breach or excess of permissions.

d) Secure channels for the transmission of information.

e) Use of credentials that identify the Participants at the moment of downloading the information and that allow adequate traceability with respect to the information accessed, written, or recovered, each time those connect.

The specifications of the alternative mechanism may consider variants or particular elements in accordance with the nature of the information to be exchanged and the technical details of the respective principal interface. In any event, the alternative mechanism and the specifications of Annex N° 3 shall be uniform for all Participants, thereby ensuring the interoperability of the System.

The entity must accredit, as part of its enablement or incorporation process into the respective roster, the implementation of the alternative mechanism whose specifications are indicated in Annex N° 3, which must be subjected to functional tests on the terms indicated for the registration process.

The existence of this alternative mechanism is independent of the operational-continuity requirements of the principal interface addressed by Section III.A.3 of this regulation.

The use of the alternative mechanism shall in no case enable the Participant to process data different from that available in the interfaces of the SFA, and it must for all purposes adhere to the terms of the consent granted by the Customer.

The conditions of activation and use of the alternative mechanism, including triggering events, the role of the Participants, and the duration of its functioning, must comply with the requirements and conditions indicated in Annex N° 3 of this regulation. In any event, for the purposes of this provision, the activation of the alternative mechanism shall not apply in the following cases:

- Scheduled maintenance duly informed and justified by the IPI or IPC to the CMF, that operationally condition the alternative mechanism. The foregoing in accordance with the standards indicated in Annex N° 3.

- Temporary suspensions that the Commission (CMF) mandates and that involve the alternative mechanism.

### Original Spanish

> "B. Mecanismo alternativo
>
> Las IPI e IPC deberán contar con un mecanismo alternativo de entrega de información, que opere en caso de los eventos de indisponibilidad de las interfaces descritas en esta sección, infra.
>
> Para lo anterior, las IPI y las IPC deberán dar cuenta a la Comisión, al momento de solicitar su incorporación en la nómina, los antecedentes que acrediten el desarrollo efectivo del mecanismo alternativo que determina la presente Norma.
>
> El mecanismo alternativo deberá considerar los siguientes requisitos técnicos, los que serán debidamente especificados en el Anexo N°3 de la Norma:
>
> a) Capacidad de mantener el servicio y la entrega de información.
>
> b) Métricas de rendimientos de respuesta a la solicitud o consulta de información.
>
> c) Medidas de seguridad tales que permitan monitorear el tráfico de la información en el mecanismo alternativo, así como la detección activa de intrusos y la vulneración o exceso de permisos.
>
> d) Canales seguros de transmisión de información.
>
> e) Uso de credenciales que identifiquen a los Participantes al momento de descargar la información y que permitan la adecuada trazabilidad respecto a la información accedida, escrita, o recuperada, cada vez que aquellos se conecten.
>
> Las especificaciones del mecanismo alternativo podrán considerar variantes o elementos particulares conforme la naturaleza de la información a intercambiar y los detalles técnicos de la interfaz principal respectiva. Con todo, el mecanismo alternativo y las especificaciones del Anexo N°3 serán uniformes para todos los Participantes, asegurando así la interoperabilidad del Sistema.
>
> La entidad deberá acreditar como parte de su proceso de habilitación o incorporación a la nómina respectiva, la implementación del mecanismo alternativo cuyas especificaciones se indiquen en el Anexo N°3, el que deberá ser sometido a pruebas funcionales en los términos indicados para el proceso de inscripción.
>
> La existencia de este mecanismo alternativo es independiente de los requerimientos de continuidad operacional de la interfaz principal que da cuenta la Sección III.A.3. de esta Norma.
>
> El uso del mecanismo alternativo en caso alguno habilita al Participante a tratar datos distintos de los que se encuentran disponibles en las interfaces del SFA, debiendo para todos los efectos ceñirse a los términos del consentimiento otorgado por el Cliente.
>
> Las condiciones de activación y uso del mecanismo alternativo, incluyendo eventos desencadenantes, rol de los Participantes, y la duración de su funcionamiento, deberán cumplir las exigencias y requerimientos que indique el Anexo N°3 de esta Norma. Con todo, para efectos de esta disposición, no aplicará la activación del mecanismo alternativo en los siguientes casos:
>
> Mantenciones programadas debidamente informadas y justificadas por la IPI o IPC a la CMF, que condicionen operativamente el mecanismo alternativo. Lo anterior según los estándares que se indiquen en el Anexo N°3.
>
> Suspensiones temporales que mandate la Comisión y que involucren el mecanismo alternativo."

### Cross-references
- Ley 21.521 Art. 21 — the SFA interfaces/APIs whose unavailability the alternative mechanism backs up.
- NCG 514 §II.A — the principal interfaces (APIs) whose unavailability triggers the alternative mechanism.
- NCG 514 §III.A.3 — the operational-continuity requirements of the principal interface, independent of this mechanism.
- NCG 514 §II.E — the contingency-communication mechanisms related to unavailability events.
- NCG 514 Annex N° 3 — the technical requirements, uniform specifications, and activation conditions of the alternative mechanism.

> **Source:** NCG 514 §II.B (03-jul-2024).

---

## II.C — Participants Directory
**NCG anchor:** N° 514, Sección II, C
**Implements:** Ley 21.521 Art. 21 (Participants Directory supporting the SFA interfaces/APIs)
**Tags:** open-finance, participants-directory, certificates, endpoints, ca

### Plain-English text

For the adequate interaction of the various participants in the context of the SFA, the CMF shall implement a Participants Directory (Directorio de Participantes) (hereinafter "DP"), of mandatory query by the entities.

The access to, query of, and updating of the information of the DP shall be subject to the directives, operational requirements, and instructions incorporated in the DP manual, which shall be available to be consulted, in its current and updated version, through the technological channels provided by the Commission (CMF).

It shall be the exclusive obligation and responsibility of each participant to ascertain that the information about itself contained in the DP is correct and has not experienced substantive changes that affect its currency or truthfulness.

Without prejudice to other elements that may in the future be incorporated within the DP platform, each participant must supply the following information:

a) Information about the entity and the natural persons who shall appear as functional officer and technical contact in the SFA, as well as about whoever holds the capacity of officer in charge before queries of other participants, in accordance with the provisions of Section II.D.

b) Information about the digital certificate(s) that the entity shall employ for its operation in the SFA, considering download or certificate-repository links, and information of the respective public key(s).

c) Information about the endpoints of each API implemented by the entity, in accordance with the technical specifications of route nomenclature established in Annex N° 3 of this regulation.

For the incorporation of a participant in the Directory, together with having successfully completed the processes of registration or enrollment in the roster, as the case may be, it must obtain from a CA a digital certificate that complies with the attributes and fields indicated in Annex N° 3 of this regulation.

The said Annex N° 3 shall indicate the requirements that the CA must comply with, as well as the extended-validation practices or guidelines that must be considered in the issuance of the respective CD to each Participant, including legal requirements and considerations of the chains of trust and root certificates to be used for purposes of security, integrity, and non-repudiation.

### Original Spanish

> "C. Directorio de Participantes
>
> Para la adecuada interacción de los diversos participantes en el contexto del SFA, la CMF implementará un Directorio de Participantes (en adelante “DP”), de consulta obligatoria por parte de las entidades.
>
> El acceso, consulta, y actualización de la información del DP se someterá a las directrices, requisitos operativos, e instrucciones incorporadas en el manual del DP, que estará disponible para ser consultado, en su versión vigente y actualizada, a través de los canales tecnológicos dispuestos por la Comisión.
>
> Será obligación y responsabilidad exclusiva de cada participante el cerciorarse que la información sobre sí mismo contenida en el DP resulte correcta y no haya experimentado cambios sustantivos que afecten su vigencia o veracidad.
>
> Sin perjuicio de otros elementos que en el futuro se incorporen dentro de la plataforma de DP, cada participante deberá suministrar la siguiente información:
>
> a) Información sobre la entidad y las personas naturales que figurarán como responsable funcional y contacto técnico en el SFA, así como de quien detente la calidad de encargado ante consultas de otros participantes, de acuerdo con lo dispuesto en la Sección II.D.
>
> b) Información sobre el o los certificados digitales que empleará la entidad para su operación en el SFA, considerando vínculos de descarga o repositorio de certificados, e información de la o las claves públicas respectivas.
>
> c) Información sobre los endpoints de cada API implementada por la entidad, conforme con las especificaciones técnicas de denominación de rutas que se establezcan en el Anexo N°3 de esta Norma.
>
> Para la incorporación de un participante en el Directorio, junto con haber cumplido exitosamente los procesos de registro o inscripción en la nómina, según sea el caso, deberá obtener de una CA un certificado digital que cumpla con los atributos y campos que se indiquen en el Anexo N°3 de esta Norma.
>
> El referido Anexo N°3 indicará los requisitos que deberán cumplir las CA, así como las prácticas o lineamientos de validación extendida que deberán considerarse en la emisión de los respectivos CD a cada Participante, incluyendo exigencias y consideraciones legales de las cadenas de confianza y certificados raíces a ser utilizados para fines de seguridad, integridad y no repudiación."

### Cross-references
- Ley 21.521 Art. 21 — the SFA interfaces/APIs whose endpoints and certificates the Participants Directory publishes.
- NCG 514 §II.D — the officer-in-charge designation referenced in item a).
- NCG 514 §I.A — the defined terms Participants Directory, CA (Certification Authority), and CD (Digital Certificate).
- NCG 514 Annex N° 3 — the route nomenclature, certificate attributes, and CA requirements referenced.

> **Source:** NCG 514 §II.C (03-jul-2024).

---

## II.D — Information Quality
**NCG anchor:** N° 514, Sección II, D
**Implements:** Ley 21.521 Art. 21 (information quality of the data exchanged via the SFA interfaces/APIs)
**Tags:** open-finance, information-quality, testing, comparability, error-analysis

### Plain-English text

Both the IPI and the IPC must carry out periodic and random tests of the quality of the data made available to the participants in the SFA. The tests shall be carried out at least on a semi-annual basis and their results shall be delivered to the Commission (CMF). In the event that significant deficiencies are detected, the entities must inform the CMF of the situation through the channels established for reporting operational-continuity events and submit to the Commission (CMF) an action plan that allows it to resolve these deficiencies, without prejudice to the temporary suspensions that the CMF may mandate or other actions that the Commission (CMF) may assess, including — among others — the imposition of sanctions in accordance with the procedures provided for that purpose.

The quality tests carried out by the IPI and IPC must contain at least the following elements:

- *Comparability analysis (Análisis de comparabilidad)*: The information supplied through interfaces attached to the system must comply with comparability criteria. This implies that the institution must verify that the information of its customers that it shares in the SFA is coherent with the information current in its other sources of storage and query.

- *Error-origin analysis (Análisis de origen de errores)*: For those cases in which differences of information are found depending on the source used, the institution must review and verify their potential causes.

Without prejudice to the foregoing, at any moment the Commission (CMF) may carry out tests of the quality of the information, for whose conduct the entities must make available the information requested for these purposes.

The minimum requirements of the tests that the IPI and IPC must carry out are those considered in Annex N° 3. The foregoing does not preclude that, for the purpose of ensuring the quality of the information they provide in the SFA, the IPI and IPC voluntarily carry out additional tests to those required by the regulation.

Without prejudice to the requirement of periodic quality tests addressed by this subparagraph, the IPI and IPC must inform the Commission (CMF) as soon as they become aware of its existence of any significant deficiency in the information transmitted through their interfaces attached to the SFA, by means of communication conducted through the channels provided for that purpose in the matter of reporting operational incidents.

### Original Spanish

> "D. Calidad de información
>
> Tanto las IPI como las IPC deberán realizar pruebas periódicas y aleatorias de calidad de los datos puestos a disposición de los participantes en el SFA. Las pruebas serán realizadas al menos con periodicidad semestral y sus resultados serán entregados a la Comisión. En caso de detectarse deficiencias significativas, las entidades deberán informar a la CMF de la situación a través de los canales establecidos para informar eventos de continuidad operacional y presentar a la Comisión un plan de acción que les permita resolver estas deficiencias, sin perjuicio de las suspensiones temporales que la CMF pueda mandatar u otras acciones que la Comisión evalúe, incluyendo -entre otros- la imposición de sanciones conforme con los procedimientos dispuestos al efecto.
>
> Las pruebas de calidad que realicen las IPI e IPC deben contener al menos los siguientes elementos:
>
> Análisis de comparabilidad: La información suministrada mediante interfaces adscritas al sistema debe cumplir con criterios de comparabilidad. Esto implica que la institución debe verificar que la información de sus clientes que comparte en el SFA es coherente con la información vigente en sus otras fuentes de almacenamiento y consulta.
>
> Análisis de origen de errores: Para aquellos casos en que se encuentren diferencias de información dependiendo de la fuente utilizada, la institución deberá revisar y verificar sus potenciales causas.
>
> Sin perjuicio de lo anterior, en cualquier momento la Comisión podrá efectuar pruebas de calidad de la información, para cuya realización las entidades deberán poner a disposición la información solicitada para estos efectos.
>
> Los requerimientos mínimos de las pruebas que deberán realizar las IPI e IPC son los considerados en el Anexo N°3. Lo anterior no obsta a que, para efectos de asegurar la calidad de la información que proveen en el SFA, voluntariamente las IPI e IPC realicen pruebas adicionales a las exigidas normativamente.
>
> Sin perjuicio de la exigencia de pruebas de calidad periódicas de que trata la presente letra, las IPI e IPC deberán informar a la Comisión tan pronto tomen conocimiento de su existencia, toda deficiencia significativa en la información que se transmite mediante sus interfaces adscritas al SFA, mediante comunicación conducida a través de los canales dispuestos al efecto en materia de reporte de incidentes operacionales."

### Cross-references
- Ley 21.521 Art. 21 — the SFA interfaces/APIs whose data quality this subparagraph regulates.
- NCG 514 §II.E — the contingency/operational-incident reporting channels referenced for significant deficiencies.
- NCG 514 Annex N° 3 — the minimum quality-test requirements referenced.

> **Source:** NCG 514 §II.D (03-jul-2024).

---

## II.E — Contingency-Communication Mechanisms
**NCG anchor:** N° 514, Sección II, E
**Implements:** Ley 21.521 Art. 21 (contingency communication regarding the SFA interfaces/APIs)
**Tags:** open-finance, contingencies, communication, error-handling, responsible-officer

### Plain-English text

The IPI and IPC must have processes to handle and resolve problems of their APIs that may affect other participants of the SFA. This includes providing clear and concise error messages, as well as mechanisms for the Participants to report problems and receive timely responses and solutions.

The entities must designate a responsible officer (funcionario responsable) to be contacted (name, position, email, and institutional telephone), who shall be the person in charge for all purposes of the communication between the Participants of the SFA and the Commission (CMF).

In its work, the responsible person must consider response times in accordance with the criticality of the query or requirement.

For their part, whoever sends a query or requirement to the responsible officer must immediately accompany in the email relevant information about the problem faced, that allows the counterparty to duly process the queries. In no case may information of the customers or data that allow their identification be shared.

In the event that it is indispensable, information of the Customer may be provided, to the extent strictly required, by means of secure channels of communication that allow guaranteeing, through robust protection mechanisms or methods, the integrity of the message and its confidentiality.

### Original Spanish

> "E. Mecanismos de comunicación ante contingencias
>
> Las IPI e IPC deberán contar con procesos para manejar y resolver problemas de sus APIs que puedan afectar a otros participantes del SFA. Esto incluye proporcionar mensajes de error claros y concisos, como, asimismo, mecanismos para que los Participantes informen problemas y reciban respuestas y soluciones oportunas.
>
> Las entidades deben designar un funcionario responsable a quien contactar (nombre, cargo, correo electrónico y teléfono institucional), quien será el encargado para todos los efectos de la comunicación entre los Participantes del SFA y la Comisión.
>
> En su labor, la persona responsable deberá considerar plazos de respuesta acorde con la criticidad de la consulta o requerimiento.
>
> Por su parte, quien envíe una consulta o requerimiento al funcionario responsable, deberá acompañar de inmediato en el correo electrónico información relevante sobre el problema enfrentado, que permita a la contraparte procesar debidamente las consultas. En ningún caso podrá compartirse información de los clientes o datos que permitan su identificación.
>
> En caso de ser imprescindible, se podrá proveer información del Cliente, en lo estrictamente requerido, mediante canales seguros de comunicación que permitan garantizar, a través de mecanismos o métodos robustos de protección, la integridad del mensaje y su confidencialidad."

### Cross-references
- Ley 21.521 Art. 21 — the SFA interfaces/APIs whose contingency communication this subparagraph regulates.
- NCG 514 §II.C — the Participants Directory where the responsible officer is registered.
- NCG 514 §II.D — the operational-incident reporting channels related to information-quality deficiencies.

> **Source:** NCG 514 §II.E (03-jul-2024).

---

## II.F — Outsourcing of Services
**NCG anchor:** N° 514, Sección II, F
**Implements:** Ley 21.521 Art. 21 (outsourcing of SFA-related interface/API functionalities)
**Tags:** open-finance, outsourcing, third-parties

### Plain-English text

For the purpose of providing the services and complying with the operating requirements of the SFA, services may be externalized and the functionalities related to the SFA may be contracted with third parties, subject to compliance with the requirements on the externalization of services that are applicable, including those in Section III.A.5 of this regulation.

### Original Spanish

> "F. Tercerización de servicios
>
> Para efectos de proveer los servicios y cumplir con los requisitos de funcionamiento del SFA, se podrá externalizar servicios y contratar con terceros las funcionalidades relacionadas con el SFA, sujeto al cumplimiento de los requisitos sobre externalización de servicios que resulten aplicables, incluidos en la sección III.A.5 de la presente normativa."

### Cross-references
- Ley 21.521 Art. 21 — the SFA interfaces/APIs whose related functionalities may be outsourced.
- NCG 514 §III.A.5 — the externalization-of-services requirements applicable to outsourcing.
- NCG 514 §II.A.3 — the monitoring-outsourcing rule that this general outsourcing provision complements.

> **Source:** NCG 514 §II.F (03-jul-2024).
