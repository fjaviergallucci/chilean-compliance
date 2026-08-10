<!-- GENERATED — do not edit by hand. Source: corpus/_agent-policy.md + corpus/. Regenerate: python -m tools.build_dist -->
# ncg-514-open-finance

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

<!-- source: corpus/ncg/514-open-finance/README.md -->
## FILE: corpus/ncg/514-open-finance/README.md

# NCG 514 — Sistema de Finanzas Abiertas (Open Finance System)

**Issued:** 2024-07-03 by the Comisión para el Mercado Financiero (CMF).
**Implements:** Ley 21.521 (Ley Fintec) Título III, arts. 17–27 + transitorios 3°/4°.
**Source PDF:** `sources/ncg_514_2024.pdf`.

NCG 514 regulates the Sistema de Finanzas Abiertas (SFA / open finance): the
perimeter and participant registries (PSBI, PSIP, IPI, IPC), system operation
(APIs, directory, data quality, outsourcing), security and safeguards (risk
management, cybersecurity, authentication, consent), the information to be
shared, other provisions, and the normative annexes defining the data sets.

Its consent (§III.D) and data-protection (§IV.D) provisions tie to **Ley 19.628**
as well as Ley 21.521; cross-references bridge both laws.

## Section layout
- `seccion-01-perimetro.md` — Sección I: Perímetro del SFA
- `seccion-02-funcionamiento.md` — Sección II: Funcionamiento del Sistema
- `seccion-03-seguridad-resguardos.md` — Sección III: Seguridad y Resguardos
- `seccion-04-informacion.md` — Sección IV: Información del Sistema
- `seccion-05-otras-disposiciones.md` — Sección V: Otras Disposiciones
- `seccion-06-anexos.md` — Sección VI: Anexos Normativos (SFA data-set specifications)

## Citation convention
`NCG 514 §III.D.1` — NCG number, § symbol, hierarchical section. Each section's
`> **Source:**` footer carries the 03-jul-2024 date.

## _law_ hint
_law:_ NCG-514

---

<!-- source: corpus/ncg/514-open-finance/seccion-01-perimetro.md -->
## FILE: corpus/ncg/514-open-finance/seccion-01-perimetro.md

# NCG 514 — Sección I: Perimeter of the Open Finance System (Perímetro del Sistema de Finanzas Abiertas)

**Regulation:** NCG 514 (Sistema de Finanzas Abiertas), 03-jul-2024.
_law:_ NCG-514

## I — Perimeter of the Open Finance System
**NCG anchor:** N° 514, Sección I
**Implements:** Ley 21.521 Título III (Open Finance System / Sistema de Finanzas Abiertas)
**Tags:** open-finance, sfa, perimeter, scope

### Plain-English text

This section establishes the perimeter of the Open Finance System (SFA) (Sistema de Finanzas Abiertas): the definitions and nomenclature used throughout the regulation, the participant entities of the system, and the registries and rosters by means of which entities are enabled to operate within it. It comprises subsections A (definitions and nomenclature), B (participant entities), C (Registry of Information-Based Service Providers), D (Registry of Payment-Initiation Service Providers), E (roster of Information-Providing Institutions and Account-Providing Institutions), and F (roster of Information-Based Service Providers). It has no standalone body text of its own; the substantive rules begin at subsection A below.

### Original Spanish

> "SECCIÓN I: PERÍMETRO DEL SISTEMA DE FINANZAS ABIERTAS"

### Cross-references
- Ley 21.521 Título III — establishes the Open Finance System (SFA), which this section implements.
- NCG 514 §I.A–§I.F — the subsections that make up this section.

> **Source:** NCG 514 §I (03-jul-2024).

---

## I.A — Definitions and Nomenclature
**NCG anchor:** N° 514, Sección I, A
**Implements:** Ley 21.521 Art. 17 (scope of the Open Finance System; defined terms)
**Tags:** open-finance, definitions, nomenclature, api

### Plain-English text

For the purposes and aims of this regulation, and except where expressly stated otherwise, the following definitions and nomenclature shall apply.

**Application Programming Interfaces (APIs).** In Spanish, "Interfaz de Programación de Aplicaciones" (Application Programming Interface). A technological mechanism by means of which two or more programs or computer systems can communicate with one another. A fundamental part of such communication depends on the characteristics of the technical documentation describing the available connection methods, and on the elements and attributes of the information exchange detailed in the API Specification.

**Test Area (Área de Pruebas).** Corresponds to an environment of computer components (that is, servers, applications, and databases, among others) where it is possible to test, without altering production systems, the changes or developments of code and computer programs. In the field of open finance, these constitute environments that allow testing with fictitious data of the APIs and their various implementation and consumption mechanisms, as well as other elements associated with their use, for testing or conformity-certification purposes.

**Authentication (Autenticación).** A process or mechanism designed to confirm that someone is who they claim to be (identity declaration). In relational terms, it translates into the interaction of a person who wishes to report and declare their identity (the declarant) and one who verifies or confirms it (the confirmer or verifier). In the field of the SFA, two types of authentication are regulated: the authentication of the customer and the authentication of the PSBI or PSIP that intends to make use of the respective API.

**Strong Customer Authentication (Autenticación Reforzada de Cliente).** A type of customer authentication designed for scenarios that require a higher level of robustness in terms of security and safeguarding of data protection, based on the use or conjunction of two or more elements independent of one another, categorized as knowledge (something the user knows), possession (something that is possessed), and inherence (something that one is). In technological terms, it is frequently related to multi-factor authorization mechanisms.

**Certification Authority – Certificate Authority (Autoridad Certificadora).** An entity or organization providing certification and trust services, charged with the issuance, handling, validation, and revocation of Digital Certificates for their use in the SFA, in accordance with the requirements set out in this regulation.

**Digital Certificates (Certificados Digitales).** Cryptographic certificates designed under public-key infrastructure and which comply, among others, with the x509 standard — defined by the Internet Engineering Task Force — in its version 3 or higher, which are issued by a Certification Authority for their use by the respective Participant holding them in authentication processes, digital signature, or encryption of data in various processes and operations within the framework of the SFA, especially for the establishment of secure channels of communication between entities, on the basis of mutual authentication (mTLS), and for the signing and encryption of messages between them.

**Customer(s) (Cliente(s)).** Natural or legal persons who have contracted a financial service or product.

**Participants Directory (Directorio de Participantes).** A technological development that allows the search, query, and updating of the Participants enabled in the SFA, including their registration or authorization data, roles and profiles, API resources, and digital certificates, among others.

**Endpoint.** In the context of an API implementation, it consists of the location of a resource, duly documented in the respective specification, intended to receive queries about a given type of information and to send responses to them, as requested.

**API Specification (Especificación de una API).** A document that contains the detailed technical information about how to effectively use and integrate a given API.

**ISO 20.022.** A technical standard prepared by the International Organization for Standardization (ISO) for the design of data-messaging schemes for the financial industry. The standard describes a number of relevant data, metadata, and processes associated with the financial industry, particularly as regards payment operations. In the context of the SFA, the standard provides a dictionary of payment variables and states that enable the use of common nomenclature in the API specifications, especially those related to payment initiation and account data.

**OpenAPI (specification) (OpenAPI (especificación)).** Corresponds to a technical specification of an open nature, designed for the description and development of APIs and RESTful services.

**Pagination (Paginación).** An API-management technique intended for the efficient handling of requests to an endpoint that involve the retrieval of a significant number of records, by means of the division of the respective response into a series of bounded sets of such records, called pages.

**Participant(s) (Participante(s)).** A collective notion that encompasses the IPI, IPC, PSBI, and PSIP enabled to operate within the SFA.

**Functional Tests (Pruebas Funcionales).** A type of test designed to attest that the various components of an application operate in accordance with what is declared in the software or in a given standard or technical specification.

**Resource (of an API) (Recurso (de una API)).** Refers to an object or piece of information or representation of a situation or circumstance that is accessible through an API.

**Representational State Transfer (REST).** A style or approach to software architecture for distributed systems implemented on the web. It considers design principles such as the existence of a client-server architecture, stateless operations, well-defined request operations, use of universal syntax, and caching capability, among others.

**RESTful.** That service which adheres to and effectively complies with the principles of the REST style, emphasizing its incorporation in applications and APIs.

**Time to Last Byte (TTLB).** A metric used to measure the time it takes for a recipient to receive the last byte of a requested packet or group of data.

**Acronyms (Siglas):**

- API: Application Programming Interface.
- ARC: Strong Customer Authentication (Autenticación Reforzada de Clientes).
- BCCh: Central Bank of Chile (Banco Central de Chile).
- CA: Certificate Authority – Certification Authority (Autoridad Certificadora).
- CD: Digital Certificate (Certificado Digital).
- CMF: Commission for the Financial Market (Comisión para el Mercado Financiero).
- FAPI: Financial-Grade API.
- HTTP: Hypertext Transfer Protocol.
- IPC: Account-Providing Institution (Institución Proveedora de Cuentas).
- IPI: Information-Providing Institution (Institución Proveedora de Información).
- JSON: JavaScript Object Notation.
- mTLS: Mutual Transport Layer Security.
- OIDF: Open ID Foundation.
- PKI: Public Key Infrastructure – Infraestructura de Claves Públicas.
- PSBI: Information-Based Service Provider (Proveedor de Servicios Basados en Información).
- PSIP: Payment-Initiation Service Provider (Proveedor de Servicios de Iniciación de Pagos).
- REST: Representational State Transfer.
- SFA: Open Finance System (Sistema de Finanzas Abiertas).
- TTLB: Time to Last Byte – Tiempo al Último Byte.

### Original Spanish

> "A. Definiciones y nomenclatura
>
> Para los efectos y propósitos de esta norma, y salvo mención expresa en otro sentido, se considerarán las siguientes definiciones y nomenclatura.
>
> Application Programming Interfaces (APIs). En español, “Interfaz de Programación de Aplicaciones”. Mecanismo tecnológico por medio del cual dos o más programas o sistemas computacionales pueden comunicarse entre sí. Parte fundamental de dicha comunicación depende de las características de la documentación técnica que describe los métodos de conexión disponibles, y los elementos y atributos del intercambio de información que se detallan en la Especificación de la API.
>
> Área de Pruebas. Corresponde a un entorno de componentes informáticos (esto es, servidores, aplicativos y bases de datos, entre otros) donde es posible probar, sin alterar los sistemas productivos, los cambios o desarrollos de códigos y programas computacionales. En el ámbito de las finanzas abiertas, constituyen ambientes que permiten probar con data ficticia las APIs y sus diversos mecanismos de implementación y consumo, así como otros elementos asociados al uso de éstas, para fines de pruebas o de certificación de conformidad.
>
> Autenticación. Proceso o mecanismo diseñado para confirmar que alguien es quien dice ser (declaración de identidad). En términos relacionales, se traduce en la interacción de una persona que quiere informar y declarar su identidad (el declarante) y quien la verifica o confirma (el confirmador o verificador). En el ámbito del SFA se regulan dos tipos de autenticaciones: la autenticación del cliente y la autenticación del PSBI o PSIP que pretende hacer uso de la respectiva API.
>
> Autenticación Reforzada de Cliente. Tipo de autenticación de Clientes diseñada para escenarios que requieren un mayor nivel de robustez en términos de seguridad y resguardo de la protección de datos, basada en el uso o conjunción de dos o más elementos independientes entre sí, categorizados como conocimiento (algo que el usuario sabe), posesión (algo que se posee), e inherencia (algo que se es). En términos tecnológicos, con frecuencia se relaciona a los mecanismos de autorización de múltiples factores.
>
> Autoridad Certificadora – Certificate Authority. Entidad u organización prestadora de servicios de certificación y confianza, encargada de la emisión, manejo, validación y revocación de Certificados Digitales para su uso en el SFA, conforme con los requerimientos dispuestos en la presente Norma.
>
> Certificados Digitales. Certificados criptográficos diseñados bajo infraestructura de claves públicas y que cumplan, entre otros, el estándar x509 -definido por el Grupo de Trabajo de Ingeniería de Internet- en su versión 3 o superior, que son emitidos por una Autoridad Certificadora para su uso por parte del respectivo Participante titular en procesos de autenticación, firma digital o cifrado de datos en diversos procesos y operaciones en el marco de SFA, especialmente para el establecimiento de canales seguros de comunicación entre entidades, sobre la base de la autenticación mutua (mTLS), y para el firmado y cifrado de mensajes entre éstas.
>
> Cliente(s). Personas naturales o jurídicas que hayan contratado un servicio o producto financiero.
>
> Directorio de Participantes. Desarrollo tecnológico que permite la búsqueda, consulta y actualización de los participantes habilitados en el SFA, incluyendo sus datos de registro o autorización, roles y perfiles, recursos de API y certificados digitales, entre otros.
>
> Endpoint. En el contexto de una implementación de API, consiste en la ubicación de un recurso, debidamente documentado en la especificación respectiva, destinado a recibir consultas sobre un determinado tipo de información y enviar respuestas a las misma, según le fuera solicitado.
>
> Especificación de una API. Documento que contiene la información técnica detallada sobre cómo usar e integrar de forma efectiva una determinada API.
>
> ISO 20.022. Es un estándar técnico preparado por la Organización Internacional de Normalización (ISO) para el diseño de esquemas de mensajería de datos para la industria financiera. El estándar describe un número relevante de datos, metadatos y procesos asociados a la industria financiera, particularmente en lo que respecta a operaciones de pago. En el contexto del SFA, el estándar proporciona un diccionario de variables y estados de pago que habilitan el uso de nomenclatura común en las especificaciones de las APIs, en especial, las relacionadas con iniciación de pagos y datos de cuentas.
>
> OpenAPI (especificación). Corresponde a una especificación técnica de carácter abierto, diseñada para la descripción y desarrollo de APIs y servicios RESTFul.
>
> Paginación. Técnica de gestión de APIs destinada al manejo eficiente de solicitudes a un endpoint, que impliquen la recuperación de un número significativo de registros, mediante la división de la respectiva respuesta en una serie de conjuntos acotados de tales registros, denominadas páginas.
>
> Participante(s). Noción colectiva que engloba a las IPI, IPC, PSBI y PSIP habilitados para operar dentro del SFA.
>
> Pruebas Funcionales. Tipo de prueba diseñada para acreditar que los diversos componentes de una aplicación operan conforme a lo declarado en el software o en un estándar o especificación técnica determinada.
>
> Recurso (de una API). Refiere a un objeto o pieza de información o representación de una situación o circunstancia, que es accesible a través de una API.
>
> Representational State Transfer (REST). Estilo o aproximación de arquitectura de software para sistemas distribuidos e implementados en la web. Considera principios de diseño tales como la existencia de arquitectura cliente-servidor sin estado, operaciones de peticiones bien definidas, uso de sintaxis universal, capacidad de caché, entre otros.
>
> RESTful. Es aquel servicio que adhiere y cumple de manera efectiva los principios del estilo REST, enfatizando su incorporación en aplicaciones y APIs.
>
> Time to Last Byte (TTLB). Métrica empleada para medir el tiempo que demora en recibirse por parte de un destinatario el último byte de un paquete o grupo de datos solicitado.
>
> Siglas
>
> API : Application Programming Interface.
> ARC : Autenticación Reforzada de Clientes.
> BCCh : Banco Central de Chile.
> CA : Certificate Authority – Autoridad Certificadora.
> CD : Certificado Digital.
> CMF : Comisión para el Mercado Financiero.
> FAPI : Financial-Grade API.
> HTTP : Hypertext Transfer Protocol.
> IPC : Institución Proveedora de Cuentas.
> IPI : Institución Proveedora de Información.
> JSON : JavaScript Object Notation.
> mTLS : Mutual Transport Layer Security.
> OIDF : Open ID Foundation.
> PKI : Public Key Infraestructure – Infraestructura de Claves Públicas.
> PSBI : Proveedor de Servicios Basados en Información.
> PSIP : Proveedor de Servicios de Iniciación de Pagos.
> REST : Representational State Transfer.
> SFA : Sistema de Finanzas Abiertas.
> TTLB : Time to Last Byte – Tiempo al Último Byte."

> **TN:** The PDF lists the acronym "PKI" with the misspelling "Infraestructure"; preserved verbatim in the Original Spanish, corrected silently in the English rendering ("Public Key Infrastructure").

### Cross-references
- Ley 21.521 Título III — the Open Finance System framework whose defined terms (Participant, IPI, IPC, PSBI, PSIP) this subsection fixes.
- Ley 21.521 Art. 17 — scope of the SFA, to which these definitions apply.

> **Source:** NCG 514 §I.A (03-jul-2024).

---

## I.B — Participant Entities
**NCG anchor:** N° 514, Sección I, B
**Implements:** Ley 21.521 Art. 18, 19 and 20 (Information-Providing Institutions, Account-Providing Institutions, Information-Based Service Providers, and Payment-Initiation Service Providers)
**Tags:** open-finance, participants, ipi, ipc, psbi, psip

### Plain-English text

The participant institutions of the SFA shall be those that qualify as Information-Providing Institutions (IPI) (Instituciones Proveedoras de Información), Account-Providing Institutions (IPC) (Instituciones Proveedoras de Cuentas), Information-Based Service Providers (PSBI) (Proveedores de Servicios Basados en Información), and Payment-Initiation Service Providers (PSIP) (Proveedores de Servicios de Iniciación de Pago), in accordance with the provisions of Articles 18, 19, and 20 of the Ley Fintec, respectively.

Such entities, in accordance with their particular role in the system, must adopt the measures necessary to permit, as applicable, the query, access, delivery, and exchange of information, expeditiously and securely, with respect to the types of financial data, products, and services relating to customers who have contracted financial products or services ("Customers"), or carried out financial operations with them.

### Original Spanish

> "B. Entidades participantes
>
> Las instituciones participantes del SFA serán aquellas que califiquen como Instituciones Proveedoras de Información (IPI), Instituciones Proveedoras de Cuentas (IPC), Proveedores de Servicios Basados en Información (PSBI), y Proveedores de Servicios de Iniciación de Pago (PSIP), conforme con lo señalado en los artículos 18, 19 y 20 de la Ley Fintec, respectivamente.
>
> Tales entidades, conforme con su rol particular en el sistema, deberán adoptar las medidas necesarias para permitir, según corresponda, la consulta, acceso, entrega e intercambio de información, de forma expedita y segura, respecto de los tipos de datos, productos y servicios financieros relativos a clientes, que hayan contratado productos o servicios financieros (“Clientes”), o realizado operaciones financieras con ellos."

### Cross-references
- Ley 21.521 Art. 18 — Information-Providing Institutions (IPI) and Account-Providing Institutions (IPC).
- Ley 21.521 Art. 19 — Information-Based Service Providers (PSBI).
- Ley 21.521 Art. 20 — Payment-Initiation Service Providers (PSIP).
- NCG 514 §I.C–§I.F — the registries and rosters by which these entities are enabled to operate.

> **Source:** NCG 514 §I.B (03-jul-2024).

---

## I.C — Registry of Information-Based Service Providers
**NCG anchor:** N° 514, Sección I, C
**Implements:** Ley 21.521 Art. 19 (Information-Based Service Providers / registration in the PSBI Registry)
**Tags:** open-finance, registration, psbi, registry

### Plain-English text

This subsection governs the Registry of Information-Based Service Providers (Registro de Prestadores de Servicios Basados en Información), referred to in Article 19 of the Ley Fintec. It comprises subparagraphs C.1 (registration in the Registry, with its application content and supporting documents), C.2 (amendment of the Registry), and C.3 (cancellation of registration). The substantive rules begin at subparagraph C.1 below.

### Original Spanish

> "C. Registro de Prestadores de Servicios Basados en Información"

### Cross-references
- Ley 21.521 Art. 19 — establishes the participation of PSBI in the SFA and the registry that this subsection operationalizes.
- NCG 514 §I.C.1, §I.C.2, §I.C.3 — the subparagraphs that make up this subsection.
- NCG 514 §I.F — the special roster (Nómina PSBI) for IPI and registered Financial-Service Providers that participate as PSBI without new registration.

> **Source:** NCG 514 §I.C (03-jul-2024).

---

## I.C.1 — Registration in the Registry
**NCG anchor:** N° 514, Sección I, C.1
**Implements:** Ley 21.521 Art. 19 (voluntary registration in the PSBI Registry)
**Tags:** open-finance, registration, psbi, application, foreign-entity

### Plain-English text

As provided in the first paragraph (inciso primero) of Article 19 of the Ley Fintec, those providers of services enabled by financial information that intend to participate in the SFA, for the purpose of querying, accessing, and receiving data in order to provide services to customers, may register voluntarily in the Registry of Information-Based Service Providers (hereinafter also the "PSBI Registry") (Registro de Prestadores de Servicios Basados en Información).

The Information-Providing Institutions referred to in Article 18 of the Ley Fintec, and the entities registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) that the Commission (CMF) maintains, as provided in Article 2 of that law, may participate voluntarily as PSBI without the need for a new registration, but subject to compliance with the requirements applicable to registered entities. For such purposes, they must apply for their enablement in the special roster of participants referred to in Section I.F of this regulation.

For the purpose of applying for registration in the Registry of Information-Based Service Providers referred to in Article 19 of the Ley Fintec, the interested entity must submit an application through the electronic channel provided for that purpose on the Commission (CMF)'s website. The application must be presented by the legal or conventional representative (representante legal o convencional) of the entity (hereinafter, the "Applicant"), who shall be personally responsible for the truthfulness and integrity of all the information provided to the Commission (CMF), without prejudice to the responsibility incumbent on the respective entity.

This application shall be applicable only to entities other than those specified in the Ley Fintec as Information-Providing Institutions and Financial-Service Providers, who, for the purpose of requesting their enablement as PSBI, must proceed in accordance with Section I.F of this regulation.

Only legal persons (personas jurídicas) incorporated in accordance with the laws of the Republic of Chile and with corporate domicile (domicilio social) within the national territory may apply for their registration in this Registry. Exceptionally, foreign entities may also apply for their incorporation, to the extent that, prior to the submission of the respective application, they establish an agency (agencia) in Chile in accordance with the procedure detailed and regulated in the provisions of Title XI of Ley N° 18.046 on Stock Corporations (Sociedades Anónimas), or in Book II, Title VII, § 9 of the Commercial Code (Código de Comercio), as applicable.

### Original Spanish

> "1. Inscripción en el Registro
>
> Conforme señala el inciso primero del artículo 19 de la Ley Fintec, podrán inscribirse voluntariamente en el Registro de Prestadores de Servicios Basados en Información (en adelante también el “Registro PSBI”) aquellos proveedores de servicios habilitados por información financiera que pretendan participar en el SFA, con el fin de consultar, acceder y recibir datos para efectos de proveer servicios a los clientes.
>
> Las Instituciones Proveedoras de Información señaladas en el artículo 18 de la Ley Fintec, y las entidades inscritas en el Registro de Prestadores de Servicios Financieros que lleva la Comisión, conforme dispone el artículo 2 de la referida ley, podrán voluntariamente participar como PSBI sin necesidad de nueva inscripción, pero sujetas al cumplimiento de los requisitos aplicables a las entidades inscritas. Para tales efectos, deberán solicitar su habilitación en la nómina especial de participantes que da cuenta la Sección I.F. de la presente Norma.
>
> Con objeto de solicitar la inscripción en el Registro de Prestadores de Servicios Basados en Información al que se refiere el artículo 19 de la Ley Fintec, la entidad interesada deberá ingresar una solicitud a través del canal electrónico dispuesto al efecto en el sitio web de la Comisión. La solicitud deberá ser presentada por el representante legal o convencional de la entidad (en adelante, el “Solicitante”), quien será personalmente responsable de la veracidad e integridad de toda la información proporcionada a la Comisión, sin perjuicio de la responsabilidad que le compete a la respectiva entidad.
>
> Esta solicitud solo será aplicable a entidades distintas a las especificadas en la Ley Fintec como Instituciones Proveedoras de Información y Prestadores de Servicios Financieros, quienes para efecto de requerir su habilitación como PSBI deberán remitirse a la Sección I.F. de esta norma.
>
> Podrán solicitar su inscripción en este Registro solo personas jurídicas constituidas conforme a las normas de la República de Chile y con domicilio social dentro del territorio nacional. Excepcionalmente podrán también solicitar su incorporación entidades extranjeras, en la medida que constituyan de forma previa al ingreso de la respectiva solicitud una agencia en Chile conforme con el procedimiento detallado y regulado en las disposiciones del Título XI de la Ley N°18.046 sobre Sociedades Anónimas o en el Libro II, Título VII, § 9 del Código de Comercio, según corresponda."

### Cross-references
- Ley 21.521 Art. 19 — the voluntary PSBI registration that this subparagraph operationalizes.
- Ley 21.521 Art. 18 — IPI that may participate as PSBI without new registration via the Nómina PSBI.
- Ley 21.521 Art. 2 — the Registry of Financial-Service Providers whose registrants may participate as PSBI.
- NCG 514 §I.C.1.1 (application content), §I.C.1.2 (supporting documents), and §I.F (Nómina PSBI).

> **Source:** NCG 514 §I.C.1 (03-jul-2024).

---

## I.C.1.1 — Content of the Application
**NCG anchor:** N° 514, Sección I, C.1.1
**Implements:** Ley 21.521 Art. 19 (PSBI registration application content)
**Tags:** open-finance, registration, psbi, application-content

### Plain-English text

The registration application must contain the following information:

a) Identification data:

i. Corporate name (razón social) of the entity and trade or commercial name (nombre de fantasía o comercial), where it has one.

ii. Unique Tax Roll (Rol Único Tributario). In the case of foreign stock corporations (sociedades anónimas extranjeras), the Unique Tax Roll of the agency in Chile must be indicated, as well as the Legal Entity Identifier of the respective company, if it has one.

iii. Identification of the natural person (persona natural) empowered to act in representation, conventional or legal, in Chile, of the entity, indicating at least their full name, nationality, and identity card or passport number, as applicable.

iv. Telephone number.

v. Domicile or postal address of the entity.

vi. URL of the entity's website, if it exists.

vii. Email address for the purposes of the notifications and communications made by this Commission (CMF).

b) Corporate data:

i. Identification of each principal partner, director, or administrator, considering their full name, nationality, and identity card or passport number, as applicable. For the purposes of this information, a principal partner (socio principal) shall be understood to mean natural persons who directly or indirectly hold an interest equal to or greater than 10% of the capital, or who have the capacity to elect at least one member of the board of directors or management.

ii. A diagram describing the corporate structure (malla societaria) of the applicant entity within its business group (grupo empresarial), providing data on its controller, in the terms of Articles 96 and 97 of Ley N° 18.045 on Securities Markets. The Applicant must at all times keep available to the Commission (CMF) an updated and current copy of this diagram.

### Original Spanish

> "1.1 Contenido de la solicitud
>
> La solicitud de inscripción deberá contener la siguiente información:
>
> a) Datos de identificación:
>
> i. Razón social de la entidad y nombre de fantasía o comercial en caso de contar con uno.
>
> ii. Rol Único Tributario. Tratándose de sociedades anónimas extranjeras deberá indicarse el Rol Único Tributario de la agencia en Chile, como asimismo el Legal Entity Identifier de la respectiva sociedad, si tuviere.
>
> iii. Identificación de la persona natural con poder para actuar en representación, convencional o legal en Chile, de la entidad, debiendo indicar, a lo menos, su nombre completo, nacionalidad, y cédula de identidad o número de pasaporte, según corresponda.
>
> iv. Número de teléfono.
>
> v. Domicilio o dirección postal de la entidad.
>
> vi. URL del sitio web de la entidad, de existir.
>
> vii. Dirección de correo electrónico para efectos de las notificaciones y comunicaciones que practique esta Comisión.
>
> b) Datos Corporativos:
>
> i. Identificación de cada socio principal, director o administrador, considerando su nombre completo, nacionalidad, y cédula de identidad o número de pasaporte, según corresponda. Para los efectos de esta información se entenderá como socio principal a las personas naturales que posean directa o indirectamente una participación igual o superior al 10% del capital o tengan la capacidad de elegir a lo menos un miembro del directorio o administración.
>
> ii. Diagrama descriptivo de la malla societaria de la entidad solicitante dentro de su grupo empresarial, proveyendo datos de su controlador, en los términos de los artículos 96 y 97 de la Ley N°18.045, de Mercado de Valores. El Solicitante deberá siempre mantener a disposición de la Comisión una copia actualizada y vigente de este diagrama."

### Cross-references
- Ley 21.521 Art. 19 — the PSBI registration whose application content this subparagraph specifies.
- Ley 18.045 Art. 96–97 — the business-group and controller definitions used in the corporate-structure diagram.
- NCG 514 §I.C.1.2 — the supporting documents that accompany this application.

> **Source:** NCG 514 §I.C.1.1 (03-jul-2024).

---

## I.C.1.2 — Supporting Documents
**NCG anchor:** N° 514, Sección I, C.1.2
**Implements:** Ley 21.521 Art. 19 (PSBI registration supporting documents)
**Tags:** open-finance, registration, psbi, supporting-documents, consent, data-processing

### Plain-English text

The following supporting documents must accompany the application:

a) Corporate bylaws (Estatutos sociales). Certificates of good standing (certificados de vigencia) of the company and a copy, with currency, of the updated corporate bylaws, issued by the competent body in accordance with the entity's registral regime.

i. Traditional regime (Régimen tradicional). A copy of the deed of incorporation and of the amending deeds of the last 10 years, of the registrations in the Registry of Commerce (Registro de Comercio), of the abstracts (extractos) of each of these, and of their publication in the Official Gazette (Diario Oficial), together with the company's certificate of good standing and a copy of the corporate registration evidencing the marginal annotations made. These documents may not have a currency greater than 15 days from their issuance.

ii. Regime of Ley N° 20.659. A copy of the certificate of currency of incorporation and of the updated corporate bylaws issued by the Registry of Enterprises and Companies (Registro de Empresas y Sociedades).

iii. Agency of a foreign company (Agencia de una sociedad extranjera). A copy of the abstract (extracto) referred to in Article 123 of Ley N° 18.046 or Article 449 of the Commercial Code (Código de Comercio), as applicable, must be attached. Likewise, an authorized copy of the protocolization (protocolización) of documents addressed by Articles 447 of the Commercial Code and 121 of Ley N° 18.046, as applicable, must be attached. These documents may not have a currency greater than 45 days from their issuance.

b) Power and representation of the applicant (Poder y representación del solicitante). A copy of the public or private instrument evidencing the designation of the Applicant as legal or conventional representative with powers sufficient to represent the entity in the registration process.

c) Business plan and activities (Plan de negocios y actividades). A referential synthesis of the strategic plan and of the business plan, indicating the principal lines of business and the activities it intends to carry out, expressly referring to the services that it will provide to customers in its capacity as PSBI, indicating the segment or segments or type of customers concerned in its services, as well as a description of the categories or groups of financial data and information available in the SFA that it will employ for the development of its activity, as indicated in Section IV.A. As part of the Plan, it must indicate, in addition to the services enabled by financial information, the accessory activities that it will carry out (if applicable), including the provision of payment-initiation services, as well as economic activities of another nature. The Applicant must at all times keep available to the Commission (CMF) an updated and current copy of this document.

d) Organizational chart and organizational structure (Organigrama y estructura organizacional). The Applicant must provide a general description of the structural organization of the entity, with a description of the principal functions of its areas. Likewise, it must detail key positions, committees, and the structure of responsibilities of the area or areas charged with compliance with the management, operational, and security requirements addressed by this regulation, which must be clear, coherent, and transparent. In applicable cases, consider the corporate support structures. The Applicant must at all times keep available to the Commission (CMF) an updated and current copy of this document.

e) Description of relationship with customers (Descripción de relacionamiento con clientes). An informative document must be provided detailing: (i) the services that will be provided to customers and under what conditions; (ii) the measures that the entity will adopt to guarantee the correct functioning of its systems as regards consent management together with the authorization and authentication of customers; and (iii) the procedures that the entity will establish for customers to exercise the rights that the Ley Fintec confers on them. The Applicant must at all times keep available to the Commission (CMF) an updated and current copy of this document.

f) Customer consent and its management (Consentimiento de Clientes y su gestión). A document must be provided detailing the terms that will be used to request the consent of customers in accordance with the provisions of Article 23 of the Ley Fintec, as well as a description of the flow or flows of obtaining, registering, maintaining, safeguarding, and managing the consent that the entity will implement in each case.

g) Processing of personal data (Tratamiento de datos personales). A description must accompany the procedure for registering, controlling, tracking, and restricting access to customers' data, including those that qualify as sensitive under the terms of Ley N° 19.628. As part of this requirement, the entity must accompany a description of the technical and organizational security measures that it will implement in view of the risks detected, as well as the data-processing-activities record model (modelo de registro de actividades de tratamiento de datos) (hereinafter "RAT") that it will implement, which must, at least, contain the following information: (i) the name and contact data of the data-processing controller and of the data-protection officer, where such designation exists; (ii) the purposes of each data processing; the time for which the data will be kept; and the basis or source of lawfulness that applies to each activity; (iii) a description of the categories of data subjects and of the personal data to be processed; (iv) the principal data-capture points (puntos de captura) associated with each data-processing activity; and (v) the categories or types of recipients or third-party receivers of the data.

h) No special disqualification under Article 19 of the Ley Fintec (No afectación de inhabilidad especial del artículo 19 de la Ley Fintec). A simple sworn declaration (declaración jurada simple), signed by the legal or conventional representative with sufficient power, must accompany, stating that the entity is not subject to the registration disqualification (inhabilidad de registro) set out in the final paragraph (inciso final) of Article 19 of the Ley Fintec. The Applicant must report the existence of modifications to this document as soon as it becomes aware of the occurrence of any circumstance that modifies it.

i) Management policies (Políticas de gestión). A document or set of documents containing the policies referred to in Section III of this regulation.

j) Certificate of implementation of interface security profiles (Certificado de implementación de perfiles de seguridad de interfaces). A document attesting the due issuance and currency of the certificate of correct technical implementation of the security standard in accordance with the parameters described in Annex N° 3 of this regulation. The conditions that the third party issuing the respective certificate must comply with shall be a matter of the said Annex N° 3.

k) Certificate of current insolvency proceedings or bankruptcies (Certificado de procedimientos concursales vigentes o quiebras). A document issued by the Superintendency of Insolvency and Re-entrepreneurship (Superintendencia de Insolvencia y Reemprendimiento), evidencing that the person or entity whose registration is applied for is not in the bankruptcy registries, nor subject to an insolvency proceeding of liquidation or reorganization, no more than 30 days old. In the case of agencies, this circumstance shall refer to the foreign entity and shall be evidenced by means of a sworn declaration issued for that purpose by the legal representative. The applicant must report the existence of modifications to this document as soon as it becomes aware of the occurrence of any circumstance that modifies it.

l) Functional tests (Pruebas funcionales). A document evidencing, through a findings report (reporte de hallazgos) provided by a third party, the conduct of Functional Tests of API consumption in Test Areas. Both the conditions that this third party must have and the minimum testing elements to be carried out must conform to the specifications of Annex N° 3 of this regulation.

In the case of documents issued abroad, they must be accompanied by the respective Apostille Certificate (Certificado de Apostilla), in the case of being granted in countries that are members of the Hague Apostille Convention of 5 October 1961. In the case of documents issued in countries that are not members of the Convention, the documents, prior to their submission, must be submitted to the procedure of legalization and ratification of signatures by consular or diplomatic channels, established in Article 345 of the Code of Civil Procedure (Código de Procedimiento Civil). Likewise, documents originally issued in a language other than Spanish must be accompanied by an official translation into Spanish, duly apostilled or legalized, as the case may be.

Once the application has been submitted and the completeness of the supporting documents required in this section has been verified, the entity will be registered in the PSBI Registry, subject to prior payment by the Applicant of the fees established in Article 33 of D.L. N° 3.538.

### Original Spanish

> "1.2 Antecedentes adjuntos
>
> Se deberá acompañar con la solicitud los siguientes antecedentes:
>
> a) Estatutos sociales. Certificados de vigencia de la sociedad y copia con vigencia de estatutos sociales actualizado, expedido por el organismo competente conforme el régimen registral de la entidad.
>
> i. Régimen tradicional. Copia de la escritura de constitución y de las escrituras modificatorias de los últimos 10 años, de las inscripciones, en el Registro de Comercio, de los extractos de cada una de éstas, y de la publicación de éstos en el Diario Oficial, junto con el certificado de vigencia de la sociedad y una copia de la inscripción social con constancia de las anotaciones marginales practicadas. Estos documentos no podrán tener una vigencia superior a 15 días desde su respectiva expedición.
>
> ii. Régimen de la Ley N°20.659. Copia del certificado de vigencia de incorporación y de estatuto social actualizado expedido por el Registro de Empresas y Sociedades.
>
> iii. Agencia de una sociedad extranjera. Se deberá adjuntar copia del extracto a que se refiere el artículo 123 de la Ley N°18.046 o el artículo 449 del Código de Comercio, según corresponda. Asimismo, se deberá adjuntar copia autorizada de la protocolización de documentos de que tratan los artículos 447 del Código de Comercio y 121 de la Ley N°18.046, según corresponda. Estos documentos no podrán tener una vigencia superior a 45 días desde su expedición.
>
> b) Poder y representación del solicitante. Copia del instrumento público o privado donde consta la designación del Solicitante como representante legal o convencional con poderes suficientes para representar a la entidad en el proceso de registro.
>
> c) Plan de negocios y actividades. Síntesis referencial del plan estratégico y de negocios, indicando las principales líneas de negocios y las actividades que pretende realizar, refiriéndose expresamente a los servicios que proveerá a clientes en su calidad de PSBI, indicando el o los segmentos o tipo de clientes concernidos en sus servicios, así como una descripción de las categorías o grupos de datos e información financiera disponible en el SFA que empleará para el desarrollo de su actividad, según lo indicado en la Sección IV.A. Como parte del Plan se deberá indicar, además de los servicios habilitados por información financiera, las actividades accesorias que llevará a cabo (de aplicar), incluyendo la prestación de servicios de iniciación de pagos, así como actividades económicas de otra índole. El Solicitante deberá siempre mantener a disposición de la Comisión una copia actualizada y vigente de este documento.
>
> d) Organigrama y estructura organizacional. El Solicitante debe aportar una descripción general de la organización estructural de la entidad, con una descripción de las principales funciones de sus áreas. Asimismo, deberá detallar cargos claves, comités y estructura de responsabilidades de la o las áreas encargadas del cumplimiento de los requisitos de gestión, operativos y de seguridad que da cuenta esta Norma, la que deberá ser clara, coherente y transparente. En los casos que corresponda, considerar las estructuras de apoyo corporativas. El Solicitante deberá siempre mantener a disposición de la Comisión una copia actualizada y vigente de este documento.
>
> e) Descripción de relacionamiento con clientes. Se debe aportar un documento informativo que detalle (i) los servicios que se prestarán a los clientes y en qué condiciones; (ii) las medidas que adoptará la entidad para garantizar el correcto funcionamiento de sus sistemas en materia de gestión de consentimiento junto con la autorización y autenticación de clientes; y (iii) los procedimientos que dispondrá la entidad para que los clientes ejerzan los derechos que le confiere la Ley Fintec. El Solicitante deberá siempre mantener a disposición de la Comisión una copia actualizada y vigente de este documento.
>
> f) Consentimiento de Clientes y su gestión. Se deberá aportar un documento que pormenorice los términos que se emplearán para requerir el consentimiento de los clientes de conformidad con lo dispuesto en el artículo 23 de la Ley Fintec, como, asimismo, una descripción del o de los flujos de obtención, registro, mantención, resguardo y gestión del consentimiento que en cada caso implementará la entidad.
>
> g) Tratamiento de datos personales. Se deberá acompañar una descripción del procedimiento para registrar, controlar, rastrear y restringir el acceso a los datos de los clientes, incluyendo aquellos que califiquen como sensibles conforme con los términos de la Ley N°19.628. Como parte de este requisito, la entidad deberá acompañar una descripción de las medidas técnicas y organizativas de seguridad que implementará en atención a los riesgos detectados, así como el modelo de registro de actividades de tratamiento de datos (en adelante “RAT”) que implementará, el que deberá, a lo menos, contar con la siguiente información: (i) el nombre y los datos de contacto del responsable del tratamiento y del oficial de protección de datos, de existir tal designación; (ii) los fines de cada tratamiento de datos; tiempo que mantendrán los datos; y la base o fuente de licitud que aplica a cada actividad; (iii) una descripción de las categorías de titulares de datos y de datos personales a tratar; (iv) los principales puntos de captura asociados a cada actividad de tratamiento de datos; y (v) las categorías o tipos de destinatarios o terceros receptores de los datos.
>
> h) No afectación de inhabilidad especial del artículo 19 de la Ley Fintec. Se deberá acompañar declaración jurada simple, suscrita por el representante legal o convencional con poder suficiente, que indique que la entidad no se encuentra afecta a la inhabilidad de registro dispuesta en el inciso final del artículo 19 de la Ley Fintec. El Solicitante deberá informar la existencia de modificaciones a este documento tan pronto tome conocimiento de la ocurrencia de alguna circunstancia que modifique el mismo.
>
> i) Políticas de gestión. Documento o conjunto de documentos que contenga las políticas a que se refiere la Sección III de esta norma.
>
> j) Certificado de implementación de perfiles de seguridad de interfaces. Documento que acredite la debida expedición y vigencia del certificado de correcta implementación técnica del estándar de seguridad conforme con los parámetros que se describan en el Anexo N°3 de esta Norma. Las condiciones que deberá cumplir el tercero que expida el respectivo certificado serán materia del referido Anexo N°3.
>
> k) Certificado de procedimientos concursales vigentes o quiebras. Documento expedido por la Superintendencia de Insolvencia y Reemprendimiento, en el que conste que la persona o entidad cuya inscripción se solicita no se encuentra en los registros de quiebra, ni está sometida a un procedimiento concursal de liquidación o de reorganización, de una antigüedad no superior a los 30 días. Para el caso de agencias, esta circunstancia estará referida a la entidad extranjera y se acreditará mediante declaración jurada expedida al efecto por el representante legal. El solicitante deberá informar la existencia de modificaciones a este documento tan pronto tome conocimiento de la ocurrencia de alguna circunstancia que modifique el mismo.
>
> l) Pruebas funcionales. Documento que evidencie a través de un reporte de hallazgos provisto por un tercero sobre la realización de Pruebas Funcionales de consumo de APIs en Áreas de Prueba. Tanto las condiciones que debe tener este tercero, como los elementos mínimos de prueba a efectuarse se deberán ajustar a las especificaciones del Anexo N°3 de esta Norma.
>
> En el caso de los documentos expedidos en el extranjero, los mismos deben acompañarse con el respectivo Certificado de Apostilla, en el caso de otorgarse en países miembros del Convenio de la Apostilla de la Haya de 5 de octubre de 1961. En el caso de documentos expedidos en países no miembros del Convenio, los documentos, previo a su presentación, deben someterse al procedimiento de legalización y ratificación de firmas por vía consular o diplomática, establecido en el artículo 345 del Código de Procedimiento Civil. Asimismo, los documentos que originalmente se expidan en un idioma distinto al castellano, deben acompañarse con una traducción oficial al castellano, debidamente apostillada o legalizada, según sea el caso.
>
> Ingresada la solicitud y verificada la completitud de los antecedentes requeridos en la presente sección, se procederá a la inscripción de la entidad en el Registro PSBI, previo pago por parte del Solicitante de los derechos establecidos en el artículo 33 del D.L. N°3.538."

### Cross-references
- Ley 21.521 Art. 19 — the PSBI registration whose supporting documents this subparagraph specifies, and the registration disqualification (inciso final) declared under item h).
- Ley 21.521 Art. 23 — the customer-consent regime referenced in item f).
- Ley 19.628 — the personal-data protection law referenced in item g).
- Ley 18.046 Art. 121, 123 and Commercial Code Art. 447, 449 — foreign-agency documentation referenced in item a)iii.
- NCG 514 §III (management policies, item i), §IV.A (data categories, item c), and Annex N° 3 (security profiles and functional tests, items j and l).

> **Source:** NCG 514 §I.C.1.2 (03-jul-2024).

---

## I.C.2 — Amendment of the Registry
**NCG anchor:** N° 514, Sección I, C.2
**Implements:** Ley 21.521 Art. 19 (maintenance of PSBI registration data)
**Tags:** open-finance, psbi, registry, amendment, credentials

### Plain-English text

From the date of the registration application and while the entity remains in the PSBI Registry, it must report, through the official channel of communication and transmission of information between the Commission (CMF) and its supervised entities, any modification or change that the information provided in connection with the application under point 1.1 above may have undergone, within the period of five business days from the occurrence of the respective event or from the entity's becoming aware of it. The foregoing is without prejudice that, in the case of changes to the identification information of the Applicant that are of a registral nature (naturaleza registral), such communication must be accompanied by an application for annotation in the PSBI Registry, the fees established in Article 33 of D.L. N° 3.538 being payable.

Together with registration in the PSBI Registry, the Commission (CMF) will grant the entity's representative a set of credentials for the access and use of the system implemented by the Commission (CMF) for that purpose.

### Original Spanish

> "2. Modificación del Registro
>
> Desde la fecha de la solicitud de inscripción y mientras la entidad se encuentre en el Registro PSBI, se deberá informar, a través del canal oficial de comunicación y envío de información entre la Comisión y sus fiscalizados, cualquier modificación o cambio que haya sufrido la información proporcionada con motivo de la solicitud en el punto 1.1 anterior, dentro del plazo de cinco días hábiles de ocurrido el hecho respectivo o tomado conocimiento de éste por parte de la entidad. Lo anterior, sin perjuicio que, tratándose de cambios a la información de identificación del Solicitante que tenga naturaleza registral, dicha comunicación deberá ser acompañada de una solicitud de anotación en el Registro PSBI, debiéndose pagar los derechos establecidos en el artículo 33 del D.L. N°3.538.
>
> Junto con la inscripción en el Registro PSBI, la Comisión otorgará al representante de la entidad un conjunto de credenciales para el acceso y utilización del sistema implementado por la Comisión para ese objetivo."

### Cross-references
- Ley 21.521 Art. 19 — the PSBI registration whose data this subparagraph requires to be kept current.
- NCG 514 §I.C.1.1 — the application content (point 1.1) whose modifications must be reported.

> **Source:** NCG 514 §I.C.2 (03-jul-2024).

---

## I.C.3 — Cancellation of Registration
**NCG anchor:** N° 514, Sección I, C.3
**Implements:** Ley 21.521 Art. 19 (cancellation of PSBI registration)
**Tags:** open-finance, psbi, cancellation, wind-down

### Plain-English text

For the purpose of requesting its cancellation from the PSBI Registry, the registered entity must send to the Commission (CMF) an application for cancellation signed by its representative, also accompanying supporting documents evidencing the cessation of the services or functionalities that require the SFA or that are linked to the provision of information-based services attached to the SFA.

The foregoing does not preclude the eventual determination of sanctions that imply or contemplate the cancellation of the entity from the PSBI Registry for non-compliance with the requirements of the Ley Fintec and/or of the provisions of this regulation.

The entity that has applied for the cancellation of its registration, or that has had its definitive suspension decreed or the termination of the currency of its registration on the occasion of the exercise of powers by the CMF, must put into execution a plan intended to guarantee that there are no transactions or operations pending execution as at the date on which the cancellation takes effect, including leaving without effect the information-access authorizations that were current as at that date, or within another period that the CMF provides in that regard, and must report to the Commission (CMF) the measures it has adopted for such purposes, together with the timetable of progress of those measures. Likewise, it must report to its respective customers the termination of its participation in the SFA, and the impact that this may have with respect to the services it provides.

### Original Spanish

> "3. Cancelación de la inscripción
>
> Para efectos de requerir su cancelación del Registro PSBI, la entidad registrada deberá remitir a la Comisión una solicitud de cancelación suscrita por su representante, acompañando además antecedentes que den cuenta de la cesación de los servicios o funcionalidades que requieren del SFA o se encuentren vinculados con la prestación de servicios basados en la información, adscrita al SFA.
>
> Lo anterior, no excluye la eventual determinación de sanciones que impliquen o consideren la cancelación de la entidad del Registro PSBI por incumplimiento de los requerimientos de la Ley Fintec y/o de las disposiciones de la presente normativa.
>
> La entidad que haya solicitado la cancelación de su registro, o bien se haya decretado su suspensión definitiva o el término de la vigencia de su inscripción con ocasión del ejercicio de facultades por parte de la CMF, deberá poner en ejecución un plan destinado a garantizar que no existan transacciones u operaciones pendientes de ejecución a la fecha que surta efecto la cancelación, incluyendo dejar sin efecto las autorizaciones de acceso de información que estuviesen vigentes a la fecha, o bien dentro de otro plazo que la CMF disponga al particular, debiendo informar a la Comisión las medidas que ha adoptado para tales propósitos, junto con el cronograma de avance de las mismas. Asimismo, deberá informar a sus respectivos clientes del término de su participación en el SFA, y el impacto que aquello puede tener respecto de los servicios que provee."

### Cross-references
- Ley 21.521 Art. 19 — the PSBI registration whose cancellation this subparagraph governs.
- NCG 514 §I.C.1 — the registration that this subparagraph winds down.

> **Source:** NCG 514 §I.C.3 (03-jul-2024).

---

## I.D — Registry of Payment-Initiation Service Providers
**NCG anchor:** N° 514, Sección I, D
**Implements:** Ley 21.521 Art. 20 (Payment-Initiation Service Providers / registration in the PSIP Registry)
**Tags:** open-finance, registration, psip, registry, payment-initiation

### Plain-English text

The PSIP are those entities that may instruct, on behalf of a customer and before the respective Account-Providing Institution (Institución Proveedora de Cuentas), the execution of payment orders or electronic funds transfers, including predefined recurring payments in favor of the third-party beneficiaries that the customers indicate, charged to their respective accounts and means of payment.

### Original Spanish

> "D. Registro de Proveedores de Servicios de Iniciación de Pagos
>
> Los PSIP son aquellas entidades que pueden instruir, a nombre de un cliente y ante la Institución Proveedora de Cuentas respectiva, la ejecución de órdenes de pago o transferencias electrónicas de fondos, incluyendo pagos recurrentes predefinidos en favor de los terceros beneficiarios que los clientes indiquen, con cargo a sus respectivas cuentas y medios de pago."

### Cross-references
- Ley 21.521 Art. 20 — establishes the PSIP and the registry that this subsection operationalizes.
- NCG 514 §I.D.1–§I.D.7 — the subparagraphs (registration, BCCh requirements, joint registration, guarantees, payment-initiation conditions, amendment, cancellation) that make up this subsection.

> **Source:** NCG 514 §I.D (03-jul-2024).

---

## I.D.1 — Registration in the Registry
**NCG anchor:** N° 514, Sección I, D.1
**Implements:** Ley 21.521 Art. 20 (PSIP registration)
**Tags:** open-finance, registration, psip, application, foreign-entity

### Plain-English text

For the purpose of applying for registration in the Registry of Payment-Initiation Service Providers (Registro de Prestadores de Servicios de Iniciación de Pagos) referred to in Article 20 of Ley N° 21.521 (the "PSIP Registry"), the interested entity must submit an application through the channel provided for that purpose on the Commission (CMF)'s website. The application must be presented by the legal or conventional representative (representante legal o convencional) of the entity (hereinafter, the "Applicant"), who shall be responsible for the truthfulness and integrity of all the information provided to the Commission (CMF).

Only legal persons (personas jurídicas) incorporated in accordance with the laws of the Republic of Chile and with corporate domicile (domicilio social) within the national territory may apply for their registration in this Registry. Exceptionally, foreign entities may also apply for their incorporation, to the extent that, prior to the submission of the respective application, they establish an agency (agencia) in Chile in accordance with the procedure detailed and regulated in the provisions of Title XI of Ley N° 18.046 on Stock Corporations (Sociedades Anónimas), or in Book II, Title VII, § 9 of the Commercial Code (Código de Comercio), as applicable.

### Original Spanish

> "1. Inscripción en el Registro
>
> A efectos de solicitar la inscripción en el Registro de Prestadores de Servicios de Iniciación de Pagos al que se refiere el artículo 20 de la Ley N°21.521 (“Registro PSIP”), la entidad interesada deberá ingresar una solicitud a través del canal dispuesto al efecto en el sitio web de la Comisión. La solicitud deberá ser presentada por el representante legal o convencional de la entidad (en adelante, el “Solicitante”) quien será responsable de la veracidad e integridad de toda la información proporcionada a la Comisión.
>
> Podrán solicitar su inscripción en este Registro solo personas jurídicas constituidas conforme a las normas de la República de Chile y con domicilio social dentro del territorio nacional. Excepcionalmente, podrán también solicitar su incorporación entidades extranjeras en la medida que constituyan, de forma previa al ingreso de la respectiva solicitud, una agencia en Chile conforme con el procedimiento detallado y regulado en las disposiciones del Título XI de la Ley N°18.046 sobre Sociedades Anónimas o en el Libro II, Título VII, § 9 del Código de Comercio, según corresponda."

### Cross-references
- Ley 21.521 Art. 20 — the PSIP registration that this subparagraph operationalizes.
- Ley 18.046 Title XI / Commercial Code Book II, Title VII, § 9 — the foreign-agency incorporation procedure.
- NCG 514 §I.D.1.1 (application content) and §I.D.1.2 (supporting documents).

> **Source:** NCG 514 §I.D.1 (03-jul-2024).

---

## I.D.1.1 — Content of the Application
**NCG anchor:** N° 514, Sección I, D.1.1
**Implements:** Ley 21.521 Art. 20 (PSIP registration application content)
**Tags:** open-finance, registration, psip, application-content

### Plain-English text

The registration application must contain the following information:

a) Identification data:

i. Corporate name (razón social) of the entity and trade or commercial name (nombre de fantasía o comercial), where it has one.

ii. Unique Tax Roll (Rol Único Tributario). In the case of foreign stock corporations (sociedades anónimas extranjeras), the Unique Tax Roll of the agency in Chile must be indicated, as well as the Legal Entity Identifier of the respective company, if it has one.

iii. Identification of the natural person (persona natural) empowered to act in conventional or legal representation in Chile of the entity, indicating at least their full name, nationality, and identity card or passport number, as applicable.

iv. Telephone number.

v. Domicile or postal address of the entity.

vi. URL of the entity's website, if it exists.

vii. Email address for the purposes of the notifications and communications made by this Commission (CMF).

b) Corporate data:

i. Identification of each principal partner, director, or administrator, considering their full name, nationality, and identity card or passport number, as applicable. For the purposes of this information, a principal partner (socio principal) shall be understood to mean natural persons who directly or indirectly hold an interest equal to or greater than 10% of the capital, or who have the capacity to elect at least one member of the board of directors or management.

ii. A diagram describing the corporate structure (malla societaria) of the applicant entity within its business group (grupo empresarial), providing data on its controller, in the terms of Articles 96 and 97 of Ley N° 18.045 on Securities Markets. The Applicant must at all times keep available to the Commission (CMF) an updated and current copy of this diagram.

### Original Spanish

> "1.1 Contenido de la solicitud
>
> La solicitud de inscripción deberá contener la siguiente información:
>
> a) Datos de identificación:
>
> i. Razón social de la entidad y nombre de fantasía o comercial en caso de contar con uno.
>
> ii. Rol Único Tributario. Tratándose de sociedades anónimas extranjeras deberá indicarse el Rol Único Tributario de la agencia en Chile, como asimismo el Legal Entity Identifier de la respectiva sociedad, si tuviere.
>
> iii. Identificación de la persona natural con poder para actuar en representación convencional o legal en Chile de la entidad, debiendo indicar, a lo menos, su nombre completo, nacionalidad, y cédula de identidad o número de pasaporte, según corresponda.
>
> iv. Número de teléfono.
>
> v. Domicilio o dirección postal de la entidad.
>
> vi. URL del sitio web de la entidad, de existir.
>
> vii. Dirección de correo electrónico para efectos de las notificaciones y comunicaciones que practique esta Comisión.
>
> b) Datos Corporativos:
>
> i. Identificación de cada socio principal, director o administrador, considerando su nombre completo, nacionalidad, y cédula de identidad o número de pasaporte, según corresponda. Para los efectos de esta información se entenderá como socio principal a las personas naturales que posean directa o indirectamente una participación igual o superior al 10% del capital o tengan la capacidad de elegir a lo menos un miembro del directorio o administración.
>
> ii. Diagrama descriptivo de la malla societaria de la entidad solicitante dentro de su grupo empresarial, proveyendo datos de su controlador, en los términos de los artículos 96 y 97 de la Ley N°18.045, de Mercado de Valores. El Solicitante deberá siempre mantener a disposición de la Comisión una copia actualizada y vigente de este diagrama."

### Cross-references
- Ley 21.521 Art. 20 — the PSIP registration whose application content this subparagraph specifies.
- Ley 18.045 Art. 96–97 — the business-group and controller definitions used in the corporate-structure diagram.
- NCG 514 §I.D.1.2 — the supporting documents that accompany this application.

> **Source:** NCG 514 §I.D.1.1 (03-jul-2024).

---

## I.D.1.2 — Supporting Documents
**NCG anchor:** N° 514, Sección I, D.1.2
**Implements:** Ley 21.521 Art. 20 (PSIP registration supporting documents)
**Tags:** open-finance, registration, psip, supporting-documents, guarantees, fund-custody

### Plain-English text

The following supporting documents must accompany the application:

a) Corporate bylaws (Estatutos sociales). Certificates of good standing (certificados de vigencia) of the company and a copy, with currency, of the updated corporate bylaws, issued by the competent body in accordance with the entity's registral regime.

i. Traditional regime (Régimen tradicional). A copy of the deed of incorporation and of the amending deeds of the last 10 years, of the registrations of the abstracts (extractos) of each of these, and of their publication in the Official Gazette (Diario Oficial), together with the company's certificate of good standing and a copy of the corporate registration evidencing the marginal annotations made. These documents may not have a currency greater than 15 days from their issuance, respectively.

ii. Regime of Ley N° 20.659. A copy of the certificate of currency of incorporation and of the updated corporate bylaws issued by the Registry of Enterprises and Companies (Registro de Empresas y Sociedades).

iii. Agency of a foreign company (Agencia de una sociedad extranjera). A copy of the abstract (extracto) referred to in Article 123 of Ley N° 18.046 or Article 449 of the Commercial Code (Código de Comercio), as applicable, must be attached. Likewise, an authorized copy of the bylaws and the certificate of incorporation of the foreign company, issued or visaed by a competent notary public (ministro de fe) in the respective jurisdiction, must be attached.

b) Power and representation of the applicant (Poder y representación del solicitante). A copy of the public or private instrument evidencing the designation of the applicant as legal or conventional representative with powers sufficient to represent the entity in the registration process.

c) Business plan and activities (Plan de negocios y actividades). A referential synthesis of the strategic plan and the business plan, indicating the principal lines of business, the activities it intends to carry out, expressly referring to the services it will provide to customers in its capacity as PSIP, indicating the segment or segments or type of customers to whom it will offer its services, as well as a description of the categories or groups of financial data and information available in the SFA that it will employ for the development of its activity, as indicated in Section IV.A. As part of the plan, it must indicate, in addition to the payment-initiation services, the accessory activities that it will carry out (if applicable), including the provision of information-based services, as well as economic activities of another nature. The Applicant must at all times keep available to the Commission (CMF) an updated and current copy of this document.

d) Ley N° 20.009 responsibility (Responsabilidad Ley N° 20.009). A description must be provided of the measures adopted by the entity to protect and safeguard the funds of customers who have the status of paying users (usuarios pagadores) in the context of payment initiation, as well as the mechanisms for managing claims regarding unauthorized operations under the terms of Ley N° 20.009, including the measures to prevent the occurrence of frauds or the malicious use of means of payment.

e) Transitory custody of funds (Custodia transitoria de fondos). The Applicant must indicate in its application, by means of a simple sworn declaration (declaración jurada simple) prepared for that purpose, whether it is its intention to develop business models that involve the maintenance or transitory custody of funds in the terms of the fourth paragraph (inciso cuarto) of Article 20 of the Ley Fintec. Should the foregoing be the case, in accordance with the provisions of Section I.D.2 of this regulation, it must accompany the supporting documents evidencing compliance with the requirements that the Central Bank of Chile (BCCh) determines in accordance with its legal powers.

f) Organizational chart and organizational structure (Organigrama y estructura organizacional). The Applicant must provide a description of the structural organization of the entity, with a description of the principal functions of its areas, key positions, committees, and structure of responsibilities. Where applicable, consider the corporate support functions. The Applicant must at all times keep available to the Commission (CMF) an updated and current copy of this document.

g) Description of relationship with Customers (Descripción sobre relacionamiento con Clientes). An informative document must be provided detailing: (i) the services that will be provided to customers and under what conditions; (ii) the measures that the entity will adopt to guarantee the correct functioning of its systems as regards consent management together with the authorization and authentication of customers; and (iii) the procedures that the entity will establish for customers to exercise the rights that the Ley Fintec confers on them. The Applicant must at all times keep available to the Commission (CMF) an updated and current copy of this document.

h) Customer consent and its management (Consentimiento de clientes y su gestión). A document must be provided detailing the terms that will be used to request the consent of customers in accordance with the provisions of Article 23 of the Ley Fintec, as well as a description of the flow or flows of obtaining, registering, maintaining, safeguarding, and managing the consent that the entity will implement in each case.

i) Processing of personal data (Tratamiento de datos personales). A description must accompany the procedure for registering, controlling, tracking, and restricting access to customers' data, including those that qualify as sensitive under the terms of Ley N° 19.628. As part of this requirement, the entity must accompany a description of the technical and organizational security measures that it will implement for this purpose, including the technical procedures that guarantee compliance regarding the payment-initiation data referred to in the fourth paragraph (inciso cuarto) of Article 20 of the Ley Fintec, as well as the data-processing-activities record model that it will implement, which must, at least, contain the following information: (i) the name and contact data of the data-processing controller and of the data-protection officer, where such designation exists; (ii) the purposes of each data processing, the time for which the data will be kept, and the basis or source of lawfulness that applies to each activity; (iii) a description of the categories of data subjects and of the personal data to be processed; (iv) the principal capture points associated with each data-processing activity; and (v) the categories or types of recipients or third-party receivers of the data.

j) No special disqualification under Article 20 of the Ley Fintec (No afectación de inhabilidad especial del artículo 20 de la Ley Fintec). A simple sworn declaration (declaración jurada simple), signed by the legal or conventional representative with sufficient power, must accompany, stating that the entity is not subject to the registration disqualification (inhabilidad de registro) set out in the final paragraph (inciso final) of Article 20 of the Ley Fintec. The Applicant must report the existence of modifications to this document as soon as it becomes aware of the occurrence of any circumstance that modifies it.

k) Management policies (Políticas de gestión). A document containing the policies referred to in Section III of this regulation.

l) Certificate of Implementation of Security Profiles (Certificado de Implementación de Perfiles de Seguridad). A document attesting the due issuance and currency of the certificate of correct technical implementation of the security standard in accordance with the parameters described in Annex N° 3 of this regulation. The conditions that the third party issuing the respective certificate must comply with shall be a matter of the said Annex N° 3.

m) Guarantees (Garantías). The documentation evidencing the contracting of one of the guarantee instruments referred to in Section I.D.4 of this regulation must be provided.

n) Certificate of current insolvency proceedings or bankruptcies (Certificado de procedimientos concursales vigentes o quiebras). A document issued by the Superintendency of Insolvency and Re-entrepreneurship (Superintendencia de Insolvencia y Reemprendimiento), evidencing that the person or entity whose registration is applied for is not in the bankruptcy registries, nor subject to an insolvency proceeding of liquidation, reorganization, or renegotiation, no more than 30 days old. In the case of agencies, this circumstance shall refer to the foreign entity and shall be evidenced by means of a sworn declaration issued for that purpose by the legal representative. The Applicant must report the existence of modifications to this document as soon as it becomes aware of the occurrence of any circumstance that modifies it.

o) Functional tests (Pruebas funcionales). A document evidencing, through a findings report (reporte de hallazgos), the conduct of Functional Tests of API consumption in Test Areas in accordance with the elements detailed in Annex N° 3 of this regulation.

In the case of documents issued abroad, they must be accompanied by the respective "Apostille Certificate" (Certificado de Apostilla), in the case of being granted in countries that are members of the Hague Apostille Convention of 5 October 1961. In the case of documents issued in countries that are not members of the said convention, the documents, prior to their submission, must be submitted to the procedure of legalization and ratification of signatures by consular or diplomatic channels, established in Article 345 of the Code of Civil Procedure (Código de Procedimiento Civil). Likewise, documents originally issued in a language other than Spanish must be accompanied by an official translation into Spanish, duly apostilled or legalized, as the case may be.

Once the application has been submitted and the completeness of the supporting documents required in this section has been verified, the entity will be registered in the PSIP Registry, subject to prior payment by the Applicant of the fees established in Article 33 of D.L. N° 3.538.

### Original Spanish

> "1.2. Antecedentes adjuntos
>
> Se deberá acompañar con la solicitud los siguientes antecedentes:
>
> a) Estatutos sociales. Certificados de vigencia de la sociedad y copia con vigencia de estatutos sociales actualizado, expedido por el organismo competente conforme el régimen registral de la entidad.
>
> i. Régimen tradicional. Copia de la escritura de constitución y de las escrituras modificatorias de los últimos 10 años, de las inscripciones de los extractos de cada una de éstas, y de la publicación de éstos en el Diario Oficial, junto con el certificado de vigencia de la sociedad y una copia de la inscripción social con constancia de las anotaciones marginales practicadas. Estos documentos no podrán tener una vigencia superior a 15 días desde su expedición, respectivamente.
>
> ii. Régimen de la Ley N°20.659. Copia del certificado de vigencia de incorporación y de estatuto social actualizado expedido por el Registro de Empresas y Sociedades.
>
> iii. Agencia de una sociedad extranjera. Se deberá adjuntar copia del extracto a que se refiere el artículo 123 de la Ley N°18.046 o el artículo 449 del Código de Comercio, según corresponda. Asimismo, se deberá adjuntar copia autorizada de estatutos y certificado de incorporación de la sociedad extranjera, expedido o visado por ministro de fe competente en la jurisdicción respectiva.
>
> b) Poder y representación del solicitante. Copia del instrumento público o privado donde consta la designación del solicitante como representante legal o convencional con poderes suficientes para representar a la entidad en el proceso de registro.
>
> c) Plan de negocios y actividades. Síntesis referencial del plan estratégico y el plan de negocios, indicando las principales líneas de negocios, las actividades que pretende realizar, refiriéndose expresamente a los servicios que proveerá a clientes en su calidad de PSIP, indicando el o los segmentos o tipo de clientes por los cuales ofrecerá sus servicios, así como una descripción de las categorías o grupos de datos e información financiera disponible en el SFA que empleará para el desarrollo de su actividad, según lo indicado en la Sección IV.A. Como parte del plan se deberá indicar, además de los servicios de iniciación de pagos, las actividades accesorias que llevará a cabo (de aplicar), incluyendo la prestación de servicios basados en información, así como actividades económicas de otra índole. El Solicitante deberá siempre mantener a disposición de la Comisión una copia actualizada y vigente de este documento.
>
> d) Responsabilidad Ley N°20.009. Se deberá proporcionar una descripción de las medidas adoptadas por la entidad para proteger y cautelar los fondos de los clientes que revistan la calidad de usuarios pagadores en el contexto de la iniciación de pagos, como, asimismo, los mecanismos de gestión de reclamaciones ante operaciones no autorizadas en los términos de la Ley N°20.009, incluyendo las medidas de prevención de ocurrencia de fraudes o uso malicioso de instrumentos de pago.
>
> e) Custodia transitoria de fondos. El Solicitante deberá indicar en su solicitud, a través de una declaración jurada simple preparada al efecto, si es su intención desarrollar modelos de negocios que impliquen la mantención o custodia transitoria de fondos en los términos del inciso cuarto del artículo 20 de la Ley Fintec. De ser efectivo lo anterior, de conformidad con lo dispuesto en la Sección I.D.2 de esta Norma, deberá acompañar los antecedentes que acrediten el cumplimiento de los requisitos que determine el Banco Central de Chile en conformidad con sus atribuciones legales.
>
> f) Organigrama y estructura organizacional. El Solicitante debe aportar una descripción de la organización estructural de la entidad, con una descripción de las principales funciones de sus áreas, cargos claves, comités y estructura de responsabilidades. En caso de que corresponda, considerar las funciones de apoyo corporativas. El Solicitante deberá siempre mantener a disposición de la Comisión una copia actualizada y vigente de este documento.
>
> g) Descripción sobre relacionamiento con Clientes. Se debe aportar un documento informativo que detalle: (i) los servicios que se prestarán a los clientes y en qué condiciones; (ii) las medidas que adoptará la entidad para garantizar el correcto funcionamiento de sus sistemas en materia de gestión de consentimiento junto con la autorización y autenticación de clientes; y (iii) los procedimientos que dispondrá la entidad para que los clientes ejerzan los derechos que le confiere la Ley Fintec. El Solicitante deberá siempre mantener a disposición de la Comisión una copia actualizada y vigente de este documento.
>
> h) Consentimiento de clientes y su gestión. Se deberá aportar un documento que pormenorice los términos que se emplearán para requerir el consentimiento de los clientes de conformidad con lo dispuesto en el artículo 23 de la Ley Fintec, como asimismo una descripción del o de los flujos de obtención, registro, mantención, resguardo y gestión del consentimiento que en cada caso implementará la entidad.
>
> i) Tratamiento de datos personales. Se deberá acompañar una descripción del procedimiento para registrar, controlar, rastrear y restringir el acceso a los datos de los clientes, incluyendo aquellos que califiquen como sensibles conforme con los términos de la Ley N°19.628. Como parte de este requisito, la entidad deberá acompañar una descripción de las medidas técnicas y organizativas de seguridad que implementará para este fin, incluyendo los procedimientos técnicos que garanticen el cumplimiento respecto de los datos de iniciación de pagos dispuesto en el inciso cuarto del artículo 20 de la Ley Fintec, así como el modelo de registro de actividades de tratamiento de datos que implementará, el que deberá, a lo menos, contar con la siguiente información: (i) el nombre y los datos de contacto del responsable de tratamiento y del oficial de protección de datos, de existir tal designación; (ii) los fines de cada tratamiento de datos, tiempo que mantendrá los datos y la base o fuente de licitud que aplica a cada actividad; (iii) una descripción de las categorías de titulares de datos y de datos personales a tratar; (iv) los principales puntos de captura asociados a cada actividad de tratamiento de datos; y (v) las categorías o tipos de destinatarios o terceros receptores de los datos.
>
> j) No afectación de inhabilidad especial del artículo 20 de la Ley Fintec. Se deberá acompañar declaración jurada simple, suscrita por el representante legal o convencional con poder suficiente, que indique que la entidad no se encuentra afecta a la inhabilidad de registro dispuesta en el inciso final del artículo 20 de la Ley Fintec. El Solicitante deberá informar la existencia de modificaciones a este documento tan pronto tome conocimiento de la ocurrencia de alguna circunstancia que modifique el mismo.
>
> k) Políticas de gestión. Documento que contenga las políticas a que se refiere la Sección III esta norma.
>
> l) Certificado de Implementación de Perfiles de Seguridad. Documento que acredite la debida expedición y vigencia del certificado de correcta implementación técnica del estándar de seguridad conforme con los parámetros que se describan en el Anexo N°3 de esta Norma. Las condiciones que deberá cumplir el tercero que expida el respectivo certificado serán materia del referido Anexo N°3.
>
> m) Garantías. Se debe aportar la documentación que acredite la contratación de alguno de los instrumentos de garantía que da cuenta la Sección I.D.4. de esta Norma.
>
> n) Certificado de procedimientos concursales vigentes o quiebras. Documento expedido por la Superintendencia de Insolvencia y Reemprendimiento, en el que conste que la persona o entidad cuya inscripción se solicita no se encuentra en los registros de quiebra, ni está sometida a un procedimiento concursal de liquidación, reorganización o renegociación, de una antigüedad no superior a los 30 días. Para el caso de agencias, esta circunstancia estará referida a la entidad extranjera y se acreditará mediante declaración jurada expedida al efecto por el representante legal. El Solicitante deberá informar la existencia de modificaciones a este documento tan pronto tome conocimiento de la ocurrencia de alguna circunstancia que modifique el mismo.
>
> o) Pruebas funcionales. Documento que evidencie a través de un reporte de hallazgos, la realización de Pruebas Funcionales de consumo de APIs en Áreas de Prueba conforme con los elementos que se detallen en el Anexo N°3 de esta Norma.
>
> En el caso de los documentos expedidos en el extranjero, los mismos deben acompañarse con el respectivo “Certificado de Apostilla”, en el caso de otorgarse en países miembros del Convenio de la Apostilla de la Haya de 5 de octubre de 1961. En el caso de documentos expedidos en países no miembros del referido convenio, los documentos, previo a su presentación, deben someterse al procedimiento de legalización y ratificación de firmas por vía consular o diplomática, establecido en el artículo 345 del Código de Procedimiento Civil. Asimismo, los documentos que originalmente se expidan en un idioma distinto al castellano, deben acompañarse con una traducción oficial al castellano, debidamente apostillada o legalizada, según sea el caso.
>
> Ingresada la solicitud y verificada la completitud de los antecedentes requeridos en la presente sección, se procederá a la inscripción de la entidad en el Registro PSIP, previo pago por parte del Solicitante de los derechos establecidos en el artículo 33 del D.L. N°3.538."

### Cross-references
- Ley 21.521 Art. 20 — the PSIP registration whose supporting documents this subparagraph specifies, the transitory fund-custody power (inciso cuarto) referenced in items e) and i), and the registration disqualification (inciso final) declared under item j).
- Ley 21.521 Art. 23 — the customer-consent regime referenced in item h).
- Ley 20.009 — the unauthorized-operations liability regime referenced in item d).
- Ley 19.628 — the personal-data protection law referenced in item i).
- NCG 514 §I.D.2 (BCCh requirements, item e), §I.D.4 (guarantees, item m), §III (management policies, item k), §IV.A (data categories, item c), and Annex N° 3 (security profiles and functional tests, items l and o).

> **Source:** NCG 514 §I.D.1.2 (03-jul-2024).

---

## I.D.2 — BCCh Requirements under the Fourth Paragraph of Article 20 of the Ley Fintec
**NCG anchor:** N° 514, Sección I, D.2
**Implements:** Ley 21.521 Art. 20 (transitory custody of funds; BCCh-determined requirements)
**Tags:** open-finance, psip, fund-custody, bcch, payment-initiation

### Plain-English text

In accordance with the provisions of the fourth paragraph (inciso cuarto) of Article 20 of the Ley Fintec, the PSIP may contemplate in their operating model, exceptionally, the possibility of accessing and maintaining, transitorily, the money or funds received from customers, as part of the execution of a payment-initiation operation. For the purposes of the foregoing, they must comply with the requirements that the Central Bank of Chile (BCCh) provides for that purpose, which shall be additional and complementary to those established in this regulation for registration as PSIP.

It shall be the obligation of the PSIP that wishes to execute that model, whether exclusively or in conjunction with other modalities that do not involve transitory custody, to evidence before the Commission (CMF), prior to its effective exercise, compliance with the requirements provided by the BCCh in its regulation.

In accordance with the provisions of the said paragraph of Article 20 of the Ley Fintec, the temporary custody of funds shall not exceed 72 hours, counted from the execution of the respective payment-initiation operation.

### Original Spanish

> "2. Requisitos del BCCh conforme con inc. cuarto del art. 20 de la Ley Fintec
>
> De conformidad con lo dispuesto en el inciso cuarto del artículo 20 de la Ley Fintec, los PSIP podrán contemplar en su modelo de funcionamiento, de manera excepcional, la posibilidad de acceder y mantener de forma transitoria el dinero o fondos recibidos de los clientes, como parte de la ejecución de una operación de iniciación de pagos. Para efectos de lo anterior, deberán cumplir los requisitos que el BCCh disponga al efecto, los que resultarán adicionales y complementarios a los establecidos en la presente normativa para el registro como PSIP.
>
> Será obligación del PSIP que quiera ejecutar dicho modelo, sea de forma exclusiva o complementaria con otras modalidades que no impliquen custodia transitoria, el acreditar ante la Comisión, de forma previa a su ejercicio efectivo, el cumplimiento de los requisitos dispuestos por el BCCh en su normativa.
>
> De acuerdo lo dispone el referido inciso del artículo 20 de la Ley Fintec, la custodia de fondos temporal no podrá superar las 72 horas, contadas desde que se ejecute la operación de iniciación de pagos respectiva."

### Cross-references
- Ley 21.521 Art. 20 (inciso cuarto) — the transitory fund-custody power and the BCCh-determined requirements that this subparagraph operationalizes.
- NCG 514 §I.D.1.2 item e) — the sworn declaration of intent to develop transitory-custody models.

> **Source:** NCG 514 §I.D.2 (03-jul-2024).

---

## I.D.3 — Joint Registration in the PSBI Registry and the PSIP Registry
**NCG anchor:** N° 514, Sección I, D.3
**Implements:** Ley 21.521 Art. 19 and Art. 20 (joint PSBI/PSIP registration)
**Tags:** open-finance, registration, psbi, psip, joint-registration

### Plain-English text

The applicant interested in registering as PSBI and PSIP may do so jointly, through a single application, having to indicate that intention explicitly in its submission, for which it must accompany the supporting documents that allow separate evidence, where applicable, of compliance with the requirements applicable to both types of registrable entities.

### Original Spanish

> "3. Inscripción conjunta en el Registro de PSBI y en el Registro de PSIP
>
> El solicitante interesado en registrarse como PSBI y PSIP podrá realizarlo conjuntamente, a través de una única solicitud, debiendo indicar explícitamente dicha intención en su presentación, para lo cual deberá acompañar los antecedentes que permitan acreditar de forma separada, en lo que corresponda, el cumplimiento de los requisitos aplicables a ambos tipos de entidades registrables."

### Cross-references
- Ley 21.521 Art. 19 — PSBI registration.
- Ley 21.521 Art. 20 — PSIP registration.
- NCG 514 §I.C.1 and §I.D.1 — the respective PSBI and PSIP registration requirements that a joint application must satisfy separately.

> **Source:** NCG 514 §I.D.3 (03-jul-2024).

---

## I.D.4 — Associated Guarantees
**NCG anchor:** N° 514, Sección I, D.4
**Implements:** Ley 21.521 Art. 20 (PSIP guarantees); Ley 20.009 Art. 5 (liability for unauthorized operations)
**Tags:** open-finance, psip, guarantees, insurance-policy, bank-guarantee

### Plain-English text

The PSIP must evidence compliance with minimum levels of guarantees as a function of the amounts they operate, which comply with the following formula:

`Guarantees = Max [ UF 1.000 ; 0.07% * Average Daily Amount * 15 ]`

Where Average Daily Amount (Monto diario promedio) corresponds to the total amount of operations in the last three months, divided by the total number of days in the period. The value of the guarantees must be updated quarterly, and the renewals of bank guarantee certificates (boletas bancarias) or endorsements of policies that are applicable must be presented and evidenced to this Commission (CMF).

Exceptionally, for the first six months of operations of the PSIP once it is registered before this Commission (CMF), the factor associated with the Average Daily Amount shall be equivalent to zero, thereby making applicable for that period only the base amount of UF 1.000. Once the said initial six months of operation have elapsed, compliance with the level of guarantees shall consider the effective operating values, and it shall be the exclusive responsibility of the PSIP to review that the guarantee instruments thus constituted are adequate and sufficient, according to the result obtained from the foregoing formula.

For the constitution of the guarantee amount indicated above, the entity may contract one of the following instruments:

**a. Insurance Policy (Póliza de Seguro)**

This must cover the damages and losses caused to third parties, for which it is civilly liable, that result from the provision of the services proper to payment initiation, for acts, errors, or omissions occurring during the term of the policy and that affect third parties through the insured. It must cover in particular the liabilities that could derive from the payment-initiation activity for the execution of unauthorized payment orders, late or defective execution, and the right of indemnification (derecho de resarcimiento) referred to in the seventh paragraph (inciso séptimo) of Article 5 of Ley N° 20.009. It must also cover the civil liability of its dependents, of its administrators, representatives, attorneys-in-fact, or of any person who participates in the functions of its line of business on behalf of the PSIP and, in general, of every person for whom it is civilly liable in the exercise of its payment-initiation activity.

The policy must cover, as a minimum, the required guarantee amount determined in accordance with the formula in this section. In the event that the coverage amount includes any franchise, deductible, or limit, this must not affect the payments that the entity must make in relation to the reimbursement requests made by customers or for indemnification by the Issuers (Emisores) that are IPC.

The coverage must comprise both the damages and losses caused to third parties, and the costs and expenses of the proceedings that they or their successors in title bring against the insured.

The costs of defense of the insured, including the respective fees, even where it concerns unfounded claims, must also be borne by the insurance company.

Lastly, the insurance must indicate that the payment of the indemnification to the injured third party shall be made by virtue of an enforceable judgment (sentencia ejecutoriada), or of a judicial or extrajudicial settlement entered into by the insured with the consent of the company.

**b. Bank Guarantee Certificate (Boleta de Garantía Bancaria)**

In the case of constituting the guarantee by means of a bank certificate (boleta bancaria), it must be taken out at a bank authorized to operate in the national market, considering as a minimum the guarantee amount determined in accordance with the formula in this section. The document must indicate that it is taken out in favor of the beneficiaries of the guarantee, that is, the present or future creditors, whether Customers or issuers of means of payment, who may come to be such due to the execution of payment-initiation services, and particularly for liabilities that could derive from the payment-initiation activity for the execution of unauthorized payment orders, late or defective execution, and the right of indemnification referred to in the seventh paragraph (inciso séptimo) of Article 5 of Ley N° 20.009. It must be payable on simple demand (pagadera a simple requerimiento).

The entity must designate a bank as representative of the possible beneficiaries of the bank certificate, which shall be the holder thereof. The representative of the beneficiaries of the bank certificate, in order to make it effective and without it being necessary to evidence it to the granting entity, must be judicially notified of the fact of a lawsuit having been filed against the secured entity (entidad caucionada).

The money proceeding from the realization of the bank certificate shall remain in pledge by operation of law (prenda de pleno derecho) in substitution of the guarantee, being kept in adjustable deposits by the representative, until the obligation to maintain the guarantee ceases.

### Original Spanish

> "4. Garantías asociadas
>
> Los PSIP deberán acreditar el cumplimiento de niveles mínimos de garantías en función a sus montos operados, que cumplan con la siguiente fórmula:
>
> Garantías = Max[UF1.000 ; 0,07% * Monto diario promedio * 15]
>
> Donde, Monto diario promedio corresponde al monto total de las operaciones en los últimos tres meses, dividido por el número total de días del periodo. El valor de las garantías deberá actualizarse trimestralmente, debiendo presentarse y acreditarse ante esta Comisión las renovaciones de boletas bancarias o endosos de pólizas que resulten aplicables.
>
> De forma excepcional, para los primeros seis meses de operaciones del PSIP una vez se registre ante esta Comisión, el factor asociado a Monto diario promedio equivaldrá a cero, haciendo por tanto aplicable para dicho periodo únicamente el monto base de UF 1.000. Transcurridos los referidos seis meses iniciales de operación, el cumplimiento del nivel de garantías considerará los valores efectivos de operación, y será responsabilidad exclusiva del PSIP revisar que los instrumentos de garantía así constituidos resulten adecuados y suficientes, según el resultado obtenido de la fórmula anterior.
>
> Para la constitución del monto de garantía antes indicado, la entidad podrá contratar alguno de los siguientes instrumentos:
>
> a. Póliza de Seguro
>
> Esta deberá cubrir los daños y perjuicios causados a terceros, de los cuales sea civilmente responsable, que resulten de la prestación de los servicios propios de iniciación de pagos, por actos, errores u omisiones ocurridos durante la vigencia de la póliza y que afecten a los terceros por el asegurado. Debe cubrir de forma particular las responsabilidades que se pudieran derivar de la actividad de iniciación de pagos por ejecución de órdenes de pago no autorizadas, ejecución tardía o defectuosa, y derecho de resarcimiento de que trata el inciso séptimo del artículo 5° de la Ley N°20.009. Deberá cubrir, asimismo, la responsabilidad civil de sus dependientes, de sus administradores, representantes, apoderados o de cualquier persona que participe en las funciones de su giro por cuenta del PSIP y, en general, la de toda persona por la cual sea civilmente responsable en el ejercicio de su actividad de iniciación de pagos.
>
> La póliza deberá cubrir como mínimo el monto de garantía exigible determinado conforme con la fórmula en esta sección. En caso de que el monto de cobertura incluya cualquier franquicia, deducible o límite, ello no deberá afectar a los pagos que la entidad deba realizar en relación con las solicitudes de reembolso efectuadas por clientes o de resarcimiento por los Emisores que sean IPC.
>
> La cobertura deberá comprender tanto los daños y perjuicios causados a terceros, como los gastos y costas del proceso que éstos o sus causahabientes promuevan en contra del asegurado.
>
> También deberá ser de cargo de la compañía aseguradora los gastos de defensa del asegurado, incluso los honorarios respectivos, aun cuando se trate de reclamaciones infundadas.
>
> Por último, el seguro deberá indicar que el pago de la indemnización al tercero perjudicado se efectuará en virtud de sentencia ejecutoriada, o de transacción judicial o extrajudicial celebrada por el asegurado con el consentimiento de la compañía.
>
> b. Boleta de Garantía Bancaria
>
> En el caso de constituirse la garantía mediante boleta bancaria, ella deberá ser tomada en un banco autorizado para operar en el mercado nacional, considerando como mínimo el monto de garantía determinado conforme la fórmula de esta sección. El documento deberá señalar que es tomada a favor de los beneficiarios de la garantía, esto es, los acreedores presentes o futuros, sean Clientes o emisores de medios de pagos, que llegare a tener debido a la ejecución de servicios de iniciación de pagos, y particularmente, por responsabilidades que se pudieran derivar de la actividad de iniciación de pagos por ejecución de órdenes de pago no autorizadas, ejecución tardía o defectuosa, y derecho de resarcimiento de que trata el inciso séptimo del artículo 5° de la Ley N°20.009. Deberá ser pagadera a simple requerimiento.
>
> La entidad deberá designar a un banco como representante de los posibles beneficiarios de la boleta bancaria, quien será el tenedor de ésta. El representante de los beneficiarios de la boleta bancaria, para hacerla efectiva y sin que sea necesario acreditarlo a la entidad otorgante, deberá ser notificado judicialmente del hecho de haberse interpuesto demanda en contra de la entidad caucionada.
>
> El dinero proveniente de la realización de la boleta bancaria quedará en prenda de pleno derecho en sustitución de la garantía, manteniéndose en depósitos reajustables por el representante, hasta que cese la obligación de mantener la garantía."

### Cross-references
- Ley 21.521 Art. 20 — the PSIP regime requiring guarantees as a condition of operation.
- Ley 20.009 Art. 5 (inciso séptimo) — the right of indemnification for unauthorized operations that the guarantee must cover.
- NCG 514 §I.D.1.2 item m) — the requirement to accompany guarantee documentation with the registration application.

> **Source:** NCG 514 §I.D.4 (03-jul-2024).

---

## I.D.5 — Specific Conditions of Payment Initiation
**NCG anchor:** N° 514, Sección I, D.5
**Implements:** Ley 21.521 Art. 20 and Título III transitorio (payment-initiation conditions; transitional registration obligation)
**Tags:** open-finance, psip, payment-initiation, consent, transitional

### Plain-English text

**Entities obligated to register in the Registry**

In accordance with the provisions of the fourth transitional article (artículo cuarto transitorio) of the Ley Fintec, the entities that, with the consent of the respective customers, are providing the payment-initiation services regulated in Title III of that law, making use of their credentials, authentication means, or through other mechanisms, must comply with the obligation to apply for their registration before the Commission (CMF) within a period not exceeding twelve months counted from the entry into force of this regulation.

**On the payment-initiation service**

The PSIP must exercise their payment-initiation activity considering the following requirements and restrictions:

a. They shall not initiate payment orders or funds transfers without the prior authorization of the customer granted for that purpose in accordance with the provisions of this regulation and the standards defined in Annex N° 3. Recurring payments shall require consent from the first transaction or from the time the respective agreement or recurring-charges scheme is subscribed.

b. The PSIP shall not maintain or take custody of the funds of the ordering or paying customer, except with prior evidence before the CMF of compliance with the rules issued by the Central Bank of Chile for operating models with temporary custody of funds.

c. The PSIP must refrain from requesting from the ordering or paying customers more information or data than is strictly necessary to initiate the payment order or funds transfer, without prejudice to compliance with the rules on prevention of money laundering, financing of terrorism, and non-proliferation of weapons of mass destruction that are applicable.

d. The PSIP must adopt the technical and organizational measures necessary to effectively comply with the limitation on the use of personal data referred to in the fourth paragraph (inciso cuarto) of Article 20 of the Ley Fintec. Without prejudice to the foregoing, in the case of a PSIP that, in addition, is registered or enabled as PSBI, it may equally employ, with the due consent of the customer, the information resulting from the execution of payment initiation in conjunction with other categories of information accessible as part of the SFA, for the purposes of the provision of financial review, conciliation, or reconciliation services. The foregoing is without prejudice to the other uses of the information that it may provide to its customers in its role as PSBI, with the due consent of its customers.

### Original Spanish

> "5. Condiciones específicas de la Iniciación de Pagos
>
> Entidades obligadas a inscribirse en el Registro
>
> Conforme lo dispone el artículo cuarto transitorio de la Ley Fintec, las entidades que con consentimiento de los respectivos clientes se encuentren prestando los servicios de iniciación de pagos regulados en el Título III de dicha ley, haciendo uso de sus credenciales, medios de autentificación o a través de otros mecanismos, deberán dar cumplimiento a la obligación de solicitar su registro ante la Comisión en un plazo que no exceda de doce meses contado a partir de la entrada en vigor de esta norma.
>
> Sobre el servicio de iniciación de pagos
>
> Los PSIP deberán ejercer su actividad de iniciación de pagos considerando los siguientes requisitos y restricciones:
>
> a. No se podrán iniciar órdenes de pago o transferencias de fondos sin autorización previa del cliente para el efecto otorgada de conformidad con lo dispuesto en esta norma y los estándares definidos en el Anexo N°3. Los pagos recurrentes requerirán de consentimiento a partir de la primera transacción o desde que se suscriba el respectivo acuerdo o esquema de cargos recurrentes.
>
> b. El PSIP no podrá mantener o custodiar los fondos del cliente ordenante o pagador, salvo acreditación previa ante la CMF del cumplimiento de las normas que dicte el Banco Central de Chile para los modelos de operación con custodia temporal de fondos.
>
> c. Los PSIP deberán abstenerse de solicitar a los clientes ordenantes o pagadores más información o datos de los estrictamente necesarios para iniciar la orden de pago o transferencia de fondos, sin perjuicio de dar cumplimiento a las normas de prevención de lavado de activos, financiamiento del terrorismo y no proliferación de armas de destrucción masiva, que resulten aplicables.
>
> d. Los PSIP deberán adoptar las medidas técnicas y organizativas necesarias para dar cumplimiento efectivo a la limitación de uso de datos personales que da cuenta el inciso cuarto del artículo 20 de la Ley Fintec. Sin perjuicio de lo anterior, tratándose de un PSIP que, además, se encuentre registrado o habilitado como PSBI, podrá igualmente emplear, con el debido consentimiento del cliente, la información resultante de la ejecución de iniciación de pagos en conjunción con otras categorías de información accesibles como parte del SFA, para los propósitos de la prestación de servicios de revisión, conciliación o reconciliación financiera. Lo anterior es sin perjuicio de los demás usos de la información que pueda proveer a sus clientes en su rol de PSBI, con el debido consentimiento de sus clientes."

### Cross-references
- Ley 21.521 Art. 20 (inciso cuarto) — the limitation on the use of personal data referenced in item d), and the fund-custody restriction in item b).
- Ley 21.521 art. cuarto transitorio — the transitional obligation of entities already providing payment-initiation services to register within twelve months.
- NCG 514 §I.D.2 (temporary fund custody, item b) and Annex N° 3 (authorization standards, item a).

> **Source:** NCG 514 §I.D.5 (03-jul-2024).

---

## I.D.6 — Amendment of the Registry
**NCG anchor:** N° 514, Sección I, D.6
**Implements:** Ley 21.521 Art. 20 (maintenance of PSIP registration data)
**Tags:** open-finance, psip, registry, amendment, credentials

### Plain-English text

From the date of the registration application and while the entity remains in the PSIP Registry, it must report, through the official channel of communication and transmission of information between the Commission (CMF) and its supervised entities, any modification or change that the information provided in connection with the application under point 1.1 above may have undergone, within the period of five business days from the occurrence of the respective event or from the entity's becoming aware of it. The foregoing is without prejudice that, in the case of changes to the identification information of the Applicant that are of a registral nature (naturaleza registral), such communication must be accompanied by an application for annotation in the PSIP Registry, the fees established in Article 33 of D.L. N° 3.538 being payable.

Together with registration in the PSIP Registry, the Commission (CMF) will grant the entity's representative a set of credentials for the access and use of the system implemented by the Commission (CMF) for that purpose.

### Original Spanish

> "6. Modificación del Registro
>
> Desde la fecha de la solicitud de inscripción y mientras la entidad se encuentre en el Registro PSIP, deberá informar, a través del canal oficial de comunicación y envío de información entre la Comisión y sus fiscalizados, cualquier modificación o cambio que haya sufrido la información proporcionada con motivo de la solicitud en el punto 1.1 anterior, dentro del plazo de cinco días hábiles de ocurrido el hecho respectivo o tomado conocimiento de éste por parte de la entidad. Lo anterior, sin perjuicio que, tratándose de cambios a la información de identificación del Solicitante que tenga naturaleza registral, dicha comunicación deberá ser acompañada de una solicitud de anotación en el Registro PSIP, debiéndose pagar los derechos establecidos en el artículo 33 del D.L. N°3.538.
>
> Junto con la inscripción en el Registro de PSIP, la Comisión otorgará al representante de la entidad un conjunto de credenciales para el acceso y utilización del sistema implementado por la Comisión para ese objetivo."

### Cross-references
- Ley 21.521 Art. 20 — the PSIP registration whose data this subparagraph requires to be kept current.
- NCG 514 §I.D.1.1 — the application content (point 1.1) whose modifications must be reported.

> **Source:** NCG 514 §I.D.6 (03-jul-2024).

---

## I.D.7 — Cancellation of Registration
**NCG anchor:** N° 514, Sección I, D.7
**Implements:** Ley 21.521 Art. 20 (cancellation of PSIP registration)
**Tags:** open-finance, psip, cancellation, wind-down

### Plain-English text

For the purpose of requesting its cancellation from the PSIP Registry, the registered entity must send to the Commission (CMF) an application for cancellation signed by its representative, also accompanying supporting documents evidencing the cessation of the services or functionalities that are linked to the payment initiation attached to the SFA.

The foregoing is without prejudice to the eventual determination of sanctions that imply or contemplate the cancellation of the entity from the PSIP Registry for non-compliance with the requirements of the Ley Fintec and of the provisions of this regulation.

The entity that has applied for the cancellation of its registration, or that has had the termination of its currency decreed by virtue of the exercise of powers by the CMF, must establish and report to the Commission (CMF) a detailed plan that guarantees and evidences that there are no transactions or operations pending execution nor claims by the beneficiaries of the payments as at the date on which the cancellation takes effect, and must report to its respective customers the termination of its access to the SFA, and must refrain from carrying out payment-initiation services without having current registration.

### Original Spanish

> "7. Cancelación de la Inscripción
>
> Para efectos de requerir su cancelación del Registro PSIP, la entidad registrada deberá remitir a la Comisión una solicitud de cancelación suscrita por su representante, acompañando además antecedentes que den cuenta de la cesación de los servicios o funcionalidades que se encuentren vinculados con la iniciación de pagos adscrita al SFA.
>
> Lo anterior, sin perjuicio de la eventual determinación de sanciones que impliquen o consideren la cancelación de la entidad del Registro PSIP por incumplimiento de los requerimientos de la Ley Fintec y de las disposiciones de la presente normativa.
>
> La entidad que haya solicitado la cancelación de su registro, o bien, se haya decretado el término de su vigencia en virtud del ejercicio de facultades por parte de la CMF, deberá disponer e informar a la Comisión de un plan detallado que garantice y acredite que no existan transacciones u operaciones pendientes de ejecución ni acreencias con los beneficiarios de los pagos a la fecha que surta efecto la cancelación, debiendo informar a sus respectivos clientes del término de su acceso al SFA, y debiendo abstenerse de realizar, sin contar con registro vigente, servicios de iniciación de pagos."

### Cross-references
- Ley 21.521 Art. 20 — the PSIP registration whose cancellation this subparagraph governs.
- NCG 514 §I.D.1 — the registration that this subparagraph winds down.

> **Source:** NCG 514 §I.D.7 (03-jul-2024).

---

## I.E — Roster of Information-Providing Institutions and Account-Providing Institutions
**NCG anchor:** N° 514, Sección I, E
**Implements:** Ley 21.521 Art. 18 (Information-Providing Institutions and Account-Providing Institutions; mandatory roster incorporation)
**Tags:** open-finance, roster, ipi, ipc, mandatory-incorporation

### Plain-English text

All entities considered as IPI and IPC in accordance with Article 18 of the Ley Fintec shall have to submit the supporting documents that allow evidence of compliance with the requirements that the said law makes applicable to them, having to submit the documents mentioned below for their incorporation and enablement in a list of entities called the "Nómina IPI" and the "Nómina IPC". This shall be an obligation of incorporation in the roster applicable to all IPI and IPC, which must be complied with in accordance with the gradual implementation and enforceability periods of the SFA stipulated in Section V.C of this regulation.

### Original Spanish

> "E. Nómina de Instituciones Proveedoras de Información y Proveedoras de Cuentas
>
> Todas las entidades consideradas como IPI e IPC de conformidad con el artículo 18 de la Ley Fintec, tendrán que presentar los antecedentes que permiten acreditar el cumplimiento de las exigencias que la referida ley les hace aplicable, debiendo presentar los antecedentes mencionados a continuación para su incorporación y habilitación en un listado de entidades denominado como “Nómina IPI” y “Nómina IPC”. Esta será una obligación de incorporación a la nómina aplicable a todas las IPI e IPC, que deberá ser cumplida conforme con los plazos de implementación y exigibilidad gradual del SFA que se estipula en la Sección V.C. de esta Norma."

### Cross-references
- Ley 21.521 Art. 18 — establishes the IPI and IPC whose mandatory roster incorporation this subsection governs.
- NCG 514 §I.E.1 (incorporation requirements), §I.E.2 (incorporation periods), and §V.C (gradual implementation and enforceability periods).

> **Source:** NCG 514 §I.E (03-jul-2024).

---

## I.E.1 — Incorporation in the Roster
**NCG anchor:** N° 514, Sección I, E.1
**Implements:** Ley 21.521 Art. 18 (IPI/IPC roster incorporation requirements)
**Tags:** open-finance, roster, ipi, ipc, incorporation-requirements

### Plain-English text

Incorporation in this roster is mandatory for the entities that the Ley Fintec has defined as having to be part of the SFA, which must comply with at least the following requirements:

a) Submit the information background associated with its incorporation in the Participants Directory (Directorio de Participantes).

b) Evidence compliance, with respect to the interfaces that are enforceable on it, with the standards and technical specifications addressed by this regulation and its Annex N° 3.

c) Evidence, through the issuance of a findings report (reporte de hallazgos) and a results certification, provided by a provider of accredited prestige and experience in matters of technical certification, technological-project development, or business-process quality assurance, the conduct of Functional Tests on its APIs, considering also the contingency scenarios, in accordance with the elements of testing — among which are the requirements on the number of tests and certifications, the types of certificates and means of accrediting compliance, and the roles and need for participation of third-party accrediting entities required — detailed in Annex N° 3 of this regulation. The said report must deliver an opinion without observations (opinión sin observaciones) of the tests carried out.

d) Accompany the documentation on the strong-customer-authentication (ARC) mechanisms it has implemented, and the form and technical requirements applicable to its linkage or redirection by the PSBI or PSIP.

e) Accompany a certificate issued by a third party that complies with the requirements of Annex N° 3 of this regulation, on the implementation of interface security profiles, evidencing the due issuance and currency of the certificate of correct technical implementation of the security standard in accordance with the parameters described in the said annex.

f) Evidence before the Commission (CMF) the adoption and implementation of the risk-management policies indicated in Section III of this regulation. The participants that, by virtue of other regulatory provisions, already have or must have risk-management and internal-control policies and procedures, must complement them, including the aspects associated with the operation of the SFA that are described in the said section.

The IPI that does not comply with the requirements set out for its incorporation in the respective Nómina IPI within the maximum periods established in this regulation shall be barred from applying for its enablement in the Nómina PSBI, in accordance with the provisions of Section I.C of this regulation.

The provisions of the preceding paragraph shall be without prejudice to the eventual application of sanctions by the Commission (CMF) in the exercise of its legal powers, for non-compliance with the periods established in this regulation, in accordance with the provisions of the Ley Fintec and the provisions of this regulation.

For these purposes, there shall be two differentiated rosters:

- Roster of Information-Providing Institutions (Nómina de Instituciones Proveedoras de Información); and
- Roster of Account-Providing Institutions (Nómina de Instituciones Proveedoras de Cuentas).

The entities that, in accordance with the Ley Fintec, perform more than one role, must separately evidence, where applicable, the background documents to be fully current in both rosters.

### Original Spanish

> "1. Incorporación a la Nómina
>
> La incorporación en esta nómina es obligatoria para las entidades que la Ley Fintec haya definido que deben ser parte del SFA, las que deberán dar cumplimiento al menos a los siguientes requisitos:
>
> a) Presentar los antecedentes de información asociados a su incorporación en el Directorio de Participantes.
>
> b) Acreditar el cumplimiento, respecto de las interfaces que le resulten exigibles, de los estándares y especificaciones técnicas que den cuenta esta norma y su Anexo N°3.
>
> c) Evidenciar a través de la emisión de un reporte de hallazgos y de certificación de resultados, provisto por un proveedor de acreditable prestigio y experiencia en materias de certificación técnica, desarrollo de proyectos tecnológicos, o aseguramiento de calidad de procesos empresariales, la realización de Pruebas Funcionales sobre sus APIs, considerando además los escenarios de contingencia, conforme con los elementos de prueba -entre los cuales se encuentran los requisitos sobre la cantidad de pruebas y certificaciones, los tipos de certificados y medios de acreditación de cumplimiento y, los roles y necesidad de participación de terceras entidades acreditadoras requeridos- que se detallen en el Anexo N°3 de esta Norma. Dicho reporte debe entregar una opinión sin observaciones de las pruebas realizadas.
>
> d) Acompañar la documentación sobre los mecanismos de ARC que tiene implementados, y la forma y requerimientos técnicos aplicables para su vinculación o redireccionamiento por parte de los PSBI o PSIP.
>
> e) Acompañar un certificado expedido por un tercero que cumpla los requisitos del Anexo N°3 de esta Norma, de implementación de perfiles de seguridad de interfaces que acredite la debida expedición y vigencia de la correcta implementación técnica del estándar de seguridad conforme con los parámetros que se describan en el referido anexo.
>
> f) Acreditar ante la Comisión la adopción e implementación de las políticas de gestión de riesgo indicadas en la Sección III de esta Norma. Los participantes que en virtud de otras disposiciones normativas ya cuenten o deban contar con políticas y procedimientos de gestión de riesgos y control interno, deberán complementar las mismas, incluyendo los aspectos asociados a la operación del SFA que se describen en la referida sección.
>
> La IPI que no cumpla con los requisitos dispuestos para su incorporación en la respectiva Nómina IPI dentro de los plazos máximos establecidos en esta Norma, estará impedida de solicitar su habilitación en la Nómina PSBI, conforme lo dispuesto en la Sección I.C de esta Norma.
>
> Lo indicado en el párrafo anterior será sin perjuicio de la eventual aplicación de sanciones por parte de la Comisión en ejercicio de sus facultades legales, por incumplimiento de los plazos establecidos en esta normativa, de conformidad con lo dispuesto en la Ley Fintec y las disposiciones de esta Norma.
>
> Para estos efectos, habrá dos nóminas diferenciadas:
>
> • Nómina de Instituciones Proveedoras de Información; y
>
> • Nómina de Instituciones Proveedoras de Cuentas.
>
> Las entidades que conforme a la Ley Fintec desempeñen más de un rol, deberán acreditar de forma separada, en lo que corresponda, los antecedentes para estar plenamente vigentes en ambas nóminas."

### Cross-references
- Ley 21.521 Art. 18 — the IPI and IPC whose mandatory roster incorporation this subparagraph governs.
- NCG 514 §I.C — the Nómina PSBI from which a non-compliant IPI is barred.
- NCG 514 §III (risk-management policies, item f) and Annex N° 3 (standards, functional tests, ARC, and security profiles, items b–e).

> **Source:** NCG 514 §I.E.1 (03-jul-2024).

---

## I.E.2 — Periods for Incorporation in the Nómina IPI and Nómina IPC
**NCG anchor:** N° 514, Sección I, E.2
**Implements:** Ley 21.521 Art. 18 (gradual incorporation periods for IPI/IPC)
**Tags:** open-finance, roster, ipi, ipc, periods, gradual-implementation

### Plain-English text

The IPI obligated by law to share and exchange information in the SFA, as well as the IPC obligated to process and exchange information regarding payment orders, must evidence compliance with the requirements and apply for their incorporation in the Nómina IPI and the Nómina IPC, as applicable, in accordance with the following periods:

- IPI of the first paragraph of Article 18, and IPC of Article 20 of the Ley Fintec. They must submit their application within the first 90 days of the entry into force of this regulation; and
- IPI of the second paragraph of Article 18 of the Ley Fintec (subparagraphs (a) to (h)). They must submit their application within the 18 months following the entry into force of this regulation.

The foregoing periods do not include compliance with the elements considered in Section V, subparagraph C, where specific periods are specified for aspects of compliance and development of the APIs, among them the conduct of functional tests.

### Original Spanish

> "2. Plazos de incorporación a las Nóminas IPI e IPC
>
> Las IPI obligadas por ley a compartir e intercambiar información en el SFA, así como los IPC obligados a cursar e intercambiar información respecto a órdenes de pago, deberán acreditar el cumplimiento de los requisitos y solicitar su incorporación en la Nómina IPI y la Nómina IPC, según corresponda, conforme con los siguientes plazos:
>
> • IPI del inciso primero del artículo 18, e IPC del artículo 20 de la Ley Fintec. Deberán presentar su solicitud dentro de los primeros 90 días de entrada en vigencia de la presente Norma; e
>
> • IPI del inciso segundo del artículo 18 de la Ley Fintec (letras (a) a (h)). Deberán presentar su solicitud dentro de los 18 meses siguientes a la entrada en vigencia de la presente Norma.
>
> Los anteriores plazos no incluyen el cumplimiento de los elementos considerados en la sección V letra C, donde se especifican plazos específicos para aspectos de cumplimiento desarrollo de las APIs, entre ellas la realización de pruebas funcionales."

### Cross-references
- Ley 21.521 Art. 18 — the IPI categories (first and second paragraphs) whose incorporation periods this subparagraph sets.
- Ley 21.521 Art. 20 — the IPC whose incorporation period is set at 90 days.
- NCG 514 §V.C — the specific periods for API compliance and development not covered by this subparagraph.

> **Source:** NCG 514 §I.E.2 (03-jul-2024).

---

## I.F — Roster of Information-Based Service Providers
**NCG anchor:** N° 514, Sección I, F
**Implements:** Ley 21.521 Art. 19 (voluntary participation as PSBI by IPI and Financial-Service Providers via the Nómina PSBI)
**Tags:** open-finance, roster, psbi, nomina-psbi, voluntary-participation

### Plain-English text

In accordance with the provisions of the first paragraph (inciso primero) of Article 19 of the Ley Fintec, the entities that qualify as IPI and those entities registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) referred to in Title II of that law may participate voluntarily in the SFA, as PSBI. For these cases, participation shall not require a new registration, without prejudice that they must apply for their incorporation and evidence before the Commission (CMF) compliance with the requirements set out for PSBI.

For such purposes, the Commission (CMF) shall maintain a list of the entities indicated above that apply for their voluntary incorporation as PSBI, which shall be called the "Nómina PSBI". The inclusion of an entity in the Nómina PSBI shall be carried out subject to prior verification by the Commission (CMF) of compliance with the requirements indicated below.

In line with the provisions of Section I.E.1 of this regulation, the inclusion of an IPI in the Nómina PSBI must always be preceded by the entity's compliance with the requirements set out for its inclusion in the respective Nómina IPI.

The incorporation in the roster shall be carried out by means of an application to the CMF, in which the intention to provide these services is expressed, and where compliance with all the requirements that the Commission (CMF) determines in this regulation for the PSBI is evidenced.

### Original Spanish

> "F. Nómina de Proveedores de Servicios Basados en Información
>
> De acuerdo con lo dispuesto en el inciso primero del artículo 19 de la Ley Fintec, podrán participar de forma voluntaria en el SFA, como PSBI, las entidades que califiquen como IPI y aquellas entidades inscritas en el Registro de Prestadores de Servicios de Financieros al que se refiere el Título II de la referida ley. Para estos casos, la participación no requerirá una nueva inscripción, sin perjuicio de que deberán solicitar su incorporación y acreditar ante la Comisión el cumplimiento de los requisitos dispuestos para los PSBI.
>
> Para tales propósitos, la Comisión mantendrá un listado de las entidades antes indicadas que soliciten su incorporación voluntaria como PSBI, que se denominará “Nómina PSBI”. La inclusión de una entidad en la Nómina PSBI se realiza previa verificación por parte de la Comisión del cumplimiento de los requisitos que se indican a continuación.
>
> En línea con lo dispuesto en la Sección I.E.1. de esta Norma, la inclusión de una IPI en la Nómina PSBI deberá estar siempre precedida del cumplimiento por parte de la entidad de los requisitos dispuestos para su inclusión en la respectiva Nómina IPI.
>
> La incorporación en la nómina se efectuará mediante una solicitud a la CMF, en la que se manifieste la intención de prestar estos servicios, y donde se acredite el cumplimiento de todos los requerimientos que la Comisión determine en la presente Norma para los PSBI."

### Cross-references
- Ley 21.521 Art. 19 (inciso primero) — the voluntary participation as PSBI that this subsection enables via the Nómina PSBI.
- Ley 21.521 Título II — the Registry of Financial-Service Providers whose registrants may join the Nómina PSBI.
- NCG 514 §I.E.1 — the Nómina IPI compliance that must precede an IPI's inclusion in the Nómina PSBI.
- NCG 514 §I.C — the PSBI requirements that Nómina PSBI applicants must evidence; §I.F.1 (cancellation of the roster).

> **Source:** NCG 514 §I.F (03-jul-2024).

---

## I.F.1 — Cancellation of the Roster
**NCG anchor:** N° 514, Sección I, F.1
**Implements:** Ley 21.521 Art. 18 and Art. 20 (loss of IPI/IPC status; termination of roster incorporation)
**Tags:** open-finance, roster, cancellation, ipi, ipc, psbi

### Plain-English text

The entities that lose their status as Information-Providing Institution (Institución Proveedora de Información) or Account-Providing Institution (Institución Proveedora de Cuentas) under the terms of Articles 18 and 20 of the Ley Fintec must submit to the Commission (CMF) an application for the termination of their incorporation in the respective rosters, having to accompany a plan that guarantees the adequate termination of the functioning of their respective interfaces, including a detailed timetable of the measures that will be adopted for such purposes.

The foregoing shall be without prejudice to the power of the Commission (CMF) to terminate ex officio (de oficio) the incorporation in a roster upon the concurrence of the legal requirements for such effects, including the cancellation or revocation of the registration or authorization of existence of the respective entity, as may be applicable by virtue of its nature and the sectoral regulation applicable to it.

In the case of the Nómina PSBI, the registered entity may apply for the cancellation of its registration on the same terms indicated in Section I.C.3, supra, of this regulation.

### Original Spanish

> "Cancelación de la Nómina
>
> Las entidades que pierdan su condición de Institución Proveedora de Información o Institución Proveedora de Cuentas en los términos de los artículos 18 y 20 de la Ley Fintec, deberán presentar a la Comisión una solicitud de término de su incorporación en las nóminas respectivas, debiendo acompañar un plan que garantice el adecuado término del funcionamiento de sus respectivas interfaces, incluyendo un cronograma detallado de las medidas que se adoptarán para tales propósitos.
>
> Lo anterior resultará sin perjuicio de la facultad de la Comisión de poner término de oficio a la incorporación a una nómina por concurrir los requisitos legales para dichos efectos, incluyendo la cancelación o revocación del registro o autorización de existencia de la respectiva entidad, conforme resulte aplicable en virtud de su naturaleza y la normativa sectorial que le aplique.
>
> Tratándose de la Nómina PSBI, la entidad inscrita podrá solicitar la cancelación de su inscripción en los mismos términos indicados en la Sección I.C.3, supra, de esta Norma."

### Cross-references
- Ley 21.521 Art. 18 — the IPI/IPC status whose loss triggers termination of roster incorporation.
- Ley 21.521 Art. 20 — the IPC/account-provider status referenced in the loss-of-status trigger.
- NCG 514 §I.C.3 — the PSBI cancellation terms applicable to the Nómina PSBI.
- NCG 514 §I.E — the Nómina IPI and Nómina IPC whose termination this subparagraph governs.

> **Source:** NCG 514 §I.F.1 (03-jul-2024).

---

<!-- source: corpus/ncg/514-open-finance/seccion-02-funcionamiento.md -->
## FILE: corpus/ncg/514-open-finance/seccion-02-funcionamiento.md

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

---

<!-- source: corpus/ncg/514-open-finance/seccion-03-seguridad-resguardos.md -->
## FILE: corpus/ncg/514-open-finance/seccion-03-seguridad-resguardos.md

# NCG 514 — Sección III: System Security and Safeguards (Seguridad y Resguardos del Sistema)

**Regulation:** NCG 514 (Sistema de Finanzas Abiertas), 03-jul-2024.
_law:_ NCG-514

## III — System Security and Safeguards
**NCG anchor:** N° 514, Sección III
**Implements:** Ley 21.521 Art. 22 (security and safeguards of the Open Finance System)
**Tags:** open-finance, sfa, security, safeguards

### Plain-English text

This section establishes the security and safeguards of the Open Finance System (SFA) (Sistema de Finanzas Abiertas): the risk management and internal control duties of the Participants, the information security, cybersecurity, and business-continuity requirements, the authentication and verification standards, the consent regime, and other standards (interoperability and cost distribution). It comprises subsections A (risk management and internal control), B (information security, cybersecurity, and business continuity), C (authentication and verification), D (consent), and E (other standards). It has no standalone body text of its own; the substantive rules begin at subsection A below.

### Original Spanish

> "SECCIÓN III: SEGURIDAD Y RESGUARDOS DEL SISTEMA"

### Cross-references
- Ley 21.521 Art. 22 — the security and safeguards of the SFA, which this section implements.
- NCG 514 §III.A–§III.E — the subsections that make up this section.

> **Source:** NCG 514 §III (03-jul-2024).

---

## III.A — Risk Management and Internal Control
**NCG anchor:** N° 514, Sección III, A
**Implements:** Ley 21.521 Art. 22 (risk management and internal control of SFA Participants)
**Tags:** open-finance, risk-management, internal-control, governance

### Plain-English text

The Participants of the SFA must comply with the following risk management (gestión de riesgos) principles, in those matters proper to the operation of the System.

The Participants that are subject to other regulatory provisions concerning risk management and internal control (control interno) must supplement those with the requirements proper to the SFA described below.

### Original Spanish

> "A. Gestión de riesgos y control interno
>
> Los Participantes del SFA deberán cumplir con los siguientes principios de gestión de riesgo, en aquellas materias propias del funcionamiento del Sistema.
>
> Los Participantes que estén sujetos a otras disposiciones normativas referidas a gestión de riesgos y control interno deberán complementar aquellas con las exigencias propias del SFA descritas a continuación."

### Cross-references
- Ley 21.521 Art. 22 — the risk-management and internal-control duties of SFA Participants that this subsection develops.
- NCG 514 §III.A.1–§III.A.5 — the subparagraphs that make up this subsection.

> **Source:** NCG 514 §III.A (03-jul-2024).

---

## III.A.1 — Responsibility of the Board
**NCG anchor:** N° 514, Sección III, A.1
**Implements:** Ley 21.521 Art. 22 (governance responsibility for risk management in the SFA)
**Tags:** open-finance, risk-management, board, governance, internal-control

### Plain-English text

The Board (Directorio), or equivalent body of the entity, is the instance responsible for approving and authorizing the risk-management and internal-control policies, at a minimum once a year or with the frequency that may be necessary, leaving evidence thereof. For those purposes, the board or equivalent body must give effect to the risk-management requirements set out below:

a) Establish the mission, vision, and strategic objectives, considering the responsibilities that the regulatory framework may provide for the entity.

b) Approve risk-management policies that are coherent with the business plan and model, the strategic objectives, and the regulatory framework, and be informed of their compliance.

c) Periodically evaluate the sufficiency of resources of the instances in charge of risk management.

d) Establish an organizational structure adequate for the entity's risk management.

e) Establish employee-hiring policies that ensure the entity has personnel with the due experience to perform their functions, and ensure that qualified resources are available for risk management.

f) Evaluate the pertinence of creating and forming a Risk-Management Committee (Comité de Gestión de Riesgos), or a similar instance, that allows it to address and monitor relevant aspects of the business.

### Original Spanish

> "1. Responsabilidad del Directorio
>
> El Directorio, u órgano equivalente de la entidad, es la instancia responsable de aprobar y autorizar las políticas de gestión de riesgos y control interno, como mínimo una vez al año o con la frecuencia que sea necesaria, dejando evidencia de ello. Para esos efectos, el directorio u órgano equivalente deberá dar cumplimiento a los requisitos de gestión de riesgos que se señalan a continuación:
>
> a) Establecer la misión, visión y objetivos estratégicos, considerando las responsabilidades que el marco regulatorio disponga para la entidad.
>
> b) Aprobar políticas de gestión de riesgos que sean coherentes con el plan y modelo de negocios, los objetivos estratégicos y el marco regulatorio e informarse de su cumplimiento.
>
> c) Evaluar periódicamente la suficiencia de recursos de las instancias encargadas de la gestión de riesgos.
>
> d) Establecer una estructura organizacional adecuada para la gestión de riesgos de la entidad.
>
> e) Establecer políticas de contratación de empleados que aseguren que la entidad disponga de personal con la debida experiencia para desempeñar sus funciones, y velar porque se cuente con los recursos calificados para la gestión de riesgos.
>
> f) Evaluar la pertinencia de crear y conformar un Comité de Gestión de Riesgos o una instancia similar que le permita tratar y monitorear aspectos relevantes de los negocios."

### Cross-references
- Ley 21.521 Art. 22 — the governance responsibility for SFA risk management that this subparagraph allocates to the board.
- NCG 514 §III.A.2 — the risk-management function that reports to the board.
- NCG 514 §III.A.3 — the risk-management plan that the board approves.

> **Source:** NCG 514 §III.A.1 (03-jul-2024).

---

## III.A.2 — Risk-Management Function
**NCG anchor:** N° 514, Sección III, A.2
**Implements:** Ley 21.521 Art. 22 (risk-management function within SFA Participants)
**Tags:** open-finance, risk-management, control, segregation-of-functions

### Plain-English text

The risk-management function is the instance responsible for the monitoring of the controls defined in the entity's risk-management and internal-control policies and procedures, as well as for coordination with other internal instances that are part of the lines of defense in risk management. This function must report directly to the board or equivalent body. If a Participant already has an organizational structure for risk management, the SFA risk-management function may be incorporated into that structure, formally assigning the responsibilities that correspond in order to give full effect to this regulation.

The risk-management function may be performed by a person, internal unit, or by the entity's senior management. Each Participant shall always be responsible for the risk-management function, even when some specific tasks associated with this function are delegated to third parties. The board or equivalent body must ensure the adequate segregation of functions and the independence of the risk-management functions with respect to the business areas.

With the aim of implementing the foregoing, the risk-management function must:

a) Propose the minimum policies and procedures and verify their compliance periodically.

b) Issue a report documenting the non-compliances detected with the policies and procedures, their causes, the measures adopted, and the effectiveness of those measures. Such report must be directed to higher instances, that is, the board or equivalent body.

c) Propose changes in the risk-management policies and procedures on the basis of the deficiencies found in its control activities.

d) Prepare an annual plan that addresses the nature, scope, and timing of the activities that the risk-management function shall develop, which must be approved by higher instances, that is, the board or equivalent body.

### Original Spanish

> "2. Función de gestión de riesgos
>
> La función de gestión de riesgos es la instancia responsable del monitoreo de los controles definidos en las políticas y los procedimientos de gestión de riesgos y control interno de la entidad, así como la coordinación con otras instancias internas que sean parte de las líneas de defensa en la gestión de riesgo. Esta función deberá reportar directamente al directorio u órgano equivalente. Si un Participante ya cuenta con una estructura organizacional para la gestión de los riesgos, la función de gestión de riesgos del SFA puede ser incorporada en dicha estructura, asignando formalmente las responsabilidades que correspondan para dar cabal cumplimiento a la presente normativa.
>
> La función de gestión de riesgos podrá ser realizada por una persona, unidad interna o por la alta administración de la entidad. Cada Participante será siempre responsable de la función de gestión de riesgos, aun cuando algunas tareas específicas asociadas a esta función estén delegadas en terceros. El directorio u órgano equivalente deberá velar por la adecuada segregación de funciones y la independencia de las funciones de gestión de riesgos respecto de las áreas de negocio.
>
> Con objeto de implementar lo anteriormente señalado, la función de gestión de riesgos deberá:
>
> a) Proponer las políticas y procedimientos mínimos y verificar su cumplimiento periódicamente.
>
> b) Emitir un informe documentando los incumplimientos detectados a las políticas y procedimientos, sus causas, medidas adoptadas y efectividad de dichas medidas. Dicho informe debe ser dirigido a instancias superiores, esto es, el directorio u órgano equivalente.
>
> c) Proponer cambios en las políticas y en los procedimientos de gestión de riesgos en función de las deficiencias encontradas en sus actividades de control.
>
> d) Elaborar un plan anual que se refiera a la naturaleza, el alcance y oportunidad de las actividades que la función de gestión de riesgos desarrollará, el que deberá ser aprobado por instancias superiores, esto es, el directorio u órgano equivalente."

### Cross-references
- Ley 21.521 Art. 22 — the risk-management function within SFA Participants that this subparagraph defines.
- NCG 514 §III.A.1 — the board to which the risk-management function reports.
- NCG 514 §III.A.3 — the risk-management plan whose compliance this function controls.

> **Source:** NCG 514 §III.A.2 (03-jul-2024).

---

## III.A.3 — Risk-Management Plan
**NCG anchor:** N° 514, Sección III, A.3
**Implements:** Ley 21.521 Art. 22 (risk-management plan of SFA Participants)
**Tags:** open-finance, risk-management, plan, operational-continuity, controls

### Plain-English text

The risk-management function shall prepare a plan with risk-mitigation strategies and the planning of contingencies in relation to the principal risks. The plan must contemplate, at least, the risks of operational continuity, information security, and cybersecurity.

The board or equivalent body, according to the legal person concerned, must approve the risk-management plan with a minimum annual frequency. The risk-management function shall control the compliance with the risk-management plan and its respective procedures.

This plan shall consider the preparation of risk-mitigation strategies, and the planning of contingency measures shall consider the following:

a) Identification of the processes into which the activities proper to the business are broken down, and the respective persons responsible for those processes.

b) Formal identification of the inherent risks to which the entity is exposed in the development of its activities.

c) Measurement of the inherent risks identified in the activities considered.

d) Definition of the control mechanisms to mitigate the inherent risks identified. In this respect, such control mechanisms must consider:

&nbsp;&nbsp;&nbsp;&nbsp;i. Description of the controls and their objective.

&nbsp;&nbsp;&nbsp;&nbsp;ii. Identification of the persons responsible for the control.

&nbsp;&nbsp;&nbsp;&nbsp;iii. Rating of the effectiveness of the controls, by an instance independent of the person responsible for them.

e) Verification of the consistency of the residual risks with the mitigation strategy for them.

f) Existence of procedures for the reporting and communication of risk management to the board or equivalent body and to all interested parties.

g) Existence of a program of continuous improvement of risk management.

### Original Spanish

> "3. Plan de gestión de riesgos
>
> La función de gestión de riesgos elaborará un plan con estrategias de mitigación de riesgos y la planificación de contingencias en relación con los principales riesgos. El plan deberá contemplar, a lo menos, los riesgos de continuidad operacional, seguridad de la información y ciberseguridad.
>
> El directorio u órgano equivalente, según la persona jurídica de que se trate, deberá aprobar el plan de gestión de riesgos como mínimo con una frecuencia anual. La función de gestión de riesgos controlará el cumplimiento del plan de gestión de riesgos y sus respectivos procedimientos.
>
> Este plan considerará la elaboración de estrategias de mitigación de riesgos y la planificación de medidas de contingencias considerará lo siguiente:
>
> a) Identificación de procesos en los que se descomponen las actividades propias del negocio, y los respectivos responsables de dichos procesos.
>
> b) Identificación formal de los riesgos inherentes a los que se expone la entidad en el desarrollo de sus actividades.
>
> c) Medición de los riesgos inherentes identificados en las actividades consideradas.
>
> d) Definición de los mecanismos de control para mitigar los riesgos inherentes identificados. Al respecto, dichos mecanismos de control deberán considerar:
>
> i. Descripción de los controles y su objetivo.
>
> ii. Identificación de los responsables del control.
>
> iii. Calificación de la efectividad de los controles, por una instancia independiente del responsable de éstos.
>
> e) Verificación de la consistencia de los riesgos residuales con la estrategia de mitigación de éstos.
>
> f) Existencia de procedimientos de información y comunicación de la gestión de riesgos al directorio u órgano equivalente y a todas las partes interesadas.
>
> g) Existencia de un programa de mejora continua de la gestión de riesgos."

### Cross-references
- Ley 21.521 Art. 22 — the risk-management plan of SFA Participants that this subparagraph mandates.
- NCG 514 §III.A.2 — the risk-management function that prepares and controls this plan.
- NCG 514 §III.B — the information-security, cybersecurity, and business-continuity risks the plan must contemplate.
- NCG 514 §II.B — the alternative mechanism, whose existence is independent of the operational-continuity requirements of the principal interface addressed by this Section III.A.3.

> **Source:** NCG 514 §III.A.3 (03-jul-2024).

---

## III.A.4 — Operational Risk
**NCG anchor:** N° 514, Sección III, A.4
**Implements:** Ley 21.521 Art. 22 (operational-risk management of SFA Participants)
**Tags:** open-finance, operational-risk, controls, risk-appetite

### Plain-English text

With the aim of developing an adequate operational-risk (riesgo operacional) management, the Participants of the SFA must consider the elements set out below, adapted to their business model, volume of operations, and number and type of customers:

a) The operational-risk-management policies and procedures must be designed to provide reasonable assurance that the entity can safeguard the integrity and security of the customers' information, even in the presence of disruptive events, safeguarding its services, processes, and, in consequence, the information assets.

b) The policies and procedures must establish the risk-appetite levels defined by the board or equivalent body, which shall determine the need to avoid, reduce, transfer, or accept the risks and, in accordance therewith, design mitigating controls.

c) The key indicators to measure operational risk, consistent with the entity's integral risk evaluation and monitoring methodology.

### Original Spanish

> "4. Riesgo Operacional
>
> Con el objeto de desarrollar una adecuada gestión de riesgo operacional, los Participantes del SFA deberán considerar los elementos que se señalan a continuación, adaptados a su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Las políticas y procedimientos de gestión de riesgo operacional deben estar diseñadas para brindar una seguridad razonable que la entidad pueda resguardar la integridad y seguridad de la información de los clientes, incluso ante la presencia de eventos disruptivos, salvaguardando sus servicios, procesos y, en consecuencia, los activos de información.
>
> b) Las políticas y procedimientos deben establecer los niveles de apetito por riesgo definidos por el directorio u órgano equivalente, que determinará la necesidad de evitar, reducir, transferir o aceptar los riesgos y, acorde con ello, diseñar controles mitigantes.
>
> c) Los indicadores claves para medir el riesgo operacional acordes con la metodología de evaluación y monitoreo de riesgos integrales de la entidad."

### Cross-references
- Ley 21.521 Art. 22 — the operational-risk management of SFA Participants that this subparagraph develops.
- NCG 514 §III.A.3 — the risk-management plan in which operational risk is a required element.
- NCG 514 §III.B — the information-security and cybersecurity elements that operational-risk management must include.

> **Source:** NCG 514 §III.A.4 (03-jul-2024).

---

## III.A.5 — Outsourcing of Services
**NCG anchor:** N° 514, Sección III, A.5
**Implements:** Ley 21.521 Art. 22 (outsourcing within operational-risk management of the SFA)
**Tags:** open-finance, outsourcing, third-parties, operational-risk

### Plain-English text

The services provided by suppliers, related to regulatory compliance, business continuity, information security, and the quality of the services, products, information, and image of the contracting entity, must be considered in the entity's operational-risk-management processes. In that sense, for the evaluation of risks of contracting suppliers, the following risks must be considered, among others:

a) *Substitution risk (Riesgo de sustitución)*: the possibility of being able or not to substitute a supplier within a determined term that guarantees the continuity of the contracted service.

b) *Intervention risk (Riesgo de intervención)*: the possibility that the entity has to take charge of the contracted function.

c) *Subcontracting risk (Riesgo de subcontratación)*: the possibility that the supplier in turn subcontracts all or part of the service, reducing the entity's capacity to supervise the subcontracted function.

d) *Concentration risk (Riesgo de concentración)*: the possibility that an entity contracts one or several services with a single supplier, increasing the possibility of failures or prolonged interruptions.

### Original Spanish

> "5. Externalización de servicios
>
> Los servicios prestados por proveedores, relacionados con el cumplimiento normativo, la continuidad del negocio, la seguridad de la información y la calidad de los servicios, productos, información e imagen de la entidad contratante, deberán ser considerados en los procesos de gestión de riesgo operacional de la entidad. En tal sentido, para la evaluación de riesgos de contratación de proveedores, se deberán considerar, entre otros, los siguientes riesgos:
>
> a) Riesgo de sustitución: la posibilidad de sustituir o no a un proveedor dentro de un plazo determinado que garantice la continuidad del servicio contratado.
>
> b) Riesgo de intervención: la posibilidad de que la entidad tenga que hacerse cargo de la función contratada.
>
> c) Riesgo de subcontratación: la posibilidad de que el proveedor subcontrate a su vez todo o parte del servicio, reduciendo la capacidad de la entidad de supervisar la función subcontratada.
>
> d) Riesgo de concentración: la posibilidad que una entidad contrate uno o varios servicios en un mismo proveedor, incrementando la posibilidad de fallas o interrupciones prolongadas."

### Cross-references
- Ley 21.521 Art. 22 — the operational-risk framework within which outsourcing (externalización) is evaluated.
- NCG 514 §II.F — the general outsourcing-of-services provision that refers back to these requirements.
- NCG 514 §II.A.3 — the monitoring-outsourcing rule subject to the outsourcing requirements developed here.

> **Source:** NCG 514 §III.A.5 (03-jul-2024).

---

## III.B — Information Security, Cybersecurity, and Business Continuity
**NCG anchor:** N° 514, Sección III, B
**Implements:** Ley 21.521 Art. 22 (information security, cybersecurity, and business continuity in the SFA)
**Tags:** open-finance, information-security, cybersecurity, business-continuity

### Plain-English text

In the field of information security (seguridad de la información) and cybersecurity (ciberseguridad), the operational-risk management must include the following elements, applicable to all entities participating in the SFA, adapted to their business model, volume of operations, and number and type of customers:

a) Have an information-security and cybersecurity policy and procedures.

b) Have an information- and communication-technology (TIC) policy and procedures.

c) Define the profile and necessary number of persons with verifiable knowledge or experience in information-security and cybersecurity standards.

d) Establish in the procedures the roles and responsibilities in the administration of the information-security and cybersecurity risk of the entity's personnel, including the Board or equivalent body.

e) Generate contractual agreements for the revocation of information-access rights and the destruction of information assets as part of the process of position change or termination of an employee.

f) Carry out auditing (internal or external) of the information-security and cybersecurity management processes, with the necessary depth and scope.

g) Have procedures that allow the Board or equivalent body to keep informed, in a timely and periodic manner, about the information-security and cybersecurity management system. Record of the reporting of information on these matters must be left in the respective minutes of the board or equivalent body and in the Committees formed to review these matters.

### Original Spanish

> "B. Seguridad de la Información, Ciberseguridad y Continuidad del Negocio
>
> En el ámbito de seguridad de la información y ciberseguridad, la gestión de riesgo operacional deberá incluir los siguientes elementos, aplicables a todas las entidades participantes del SFA, adaptados a su modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Contar con una política y procedimientos de seguridad de la información y ciberseguridad.
>
> b) Contar con una política y procedimientos de tecnologías de información y comunicación (TIC).
>
> c) Definir perfil y número necesario de personas con conocimientos o experiencia comprobables en estándares de seguridad de la información y ciberseguridad.
>
> d) Establecer en los procedimientos los roles y responsabilidades en la administración del riesgo de seguridad de la información y ciberseguridad del personal de la entidad, incluido el Directorio u órgano equivalente.
>
> e) Generar acuerdos contractuales para la revocación de derechos de acceso a información y destrucción de activos de información como parte del proceso de cambio de posición o desvinculación de un empleado.
>
> f) Realizar auditoría (interna o externa) de los procesos de gestión de la seguridad de la información y ciberseguridad, con la profundidad y alcance necesario.
>
> g) Disponer de procedimientos que le permitan al Directorio u órgano equivalente mantenerse informado, en forma oportuna y periódica, sobre el sistema de gestión de la seguridad de la información y ciberseguridad. Deberá dejarse constancia del reporte de la información en estas materias en las respectivas actas del directorio u órgano equivalente y en los Comités que se conformen para revisar estas materias."

### Cross-references
- Ley 21.521 Art. 22 — the information-security, cybersecurity, and business-continuity duties of SFA Participants that this subsection develops.
- NCG 514 §III.A.4 — the operational-risk management into which these elements are integrated.
- NCG 514 §III.B.1–§III.B.3 — the subparagraphs that make up this subsection.

> **Source:** NCG 514 §III.B (03-jul-2024).

---

## III.B.1 — Information Security and Cybersecurity Management
**NCG anchor:** N° 514, Sección III, B.1
**Implements:** Ley 21.521 Art. 22 (information-security and cybersecurity management procedures in the SFA)
**Tags:** open-finance, information-security, cybersecurity, asset-inventory, access-control

### Plain-English text

The entity must consider the following procedures, adapted to its business model, volume of operations, number and type of customers:

a) Have a clear definition of information assets (technological and non-technological) that is sufficient for the adequate management of the associated risks.

b) Classify the information, taking into consideration the dimensions of availability, confidentiality, and integrity.

c) Define the critical information assets, indispensable for the entity's operation, classified from a perspective of availability, confidentiality, and integrity.

d) Implement an inventory of information assets that allows the principal characteristics of the asset to be known.

e) Update the inventory of information assets on a periodic basis.

f) Establish access controls to the facilities and business, operational, and technical-dependency infrastructures.

g) Establish access controls to the systems, in a manner that mitigates the risks of impersonation or improper use by third parties.

h) Implement tools for the recording, control, and monitoring of the activities of users and administrators of systems and information assets, including high-privilege users, in order to identify patterns of non-habitual use that generate suspicion of inadequate use.

i) Prepare procedures to grant, revoke, or modify the privileges granted to the users of the systems, network services, operating systems, databases, and business applications on the basis of the roles and responsibilities of the personnel, taking care to deliver the accesses strictly necessary for them to fulfill their current functions.

j) Establish controls that allow mitigating the risks derived from the use of mobile devices and from remote access made by internal or external personnel.

k) Verify the control and monitoring mechanisms of the environmental conditions for the secure location of the technological and communications equipment and tools.

l) Prepare procedures for the security of the entity's operations and communications, by means of the implementation of:

&nbsp;&nbsp;&nbsp;&nbsp;i. Tools and controls for the proactive detection and protection against cyber attacks and other anomalous activities.

&nbsp;&nbsp;&nbsp;&nbsp;ii. A configuration-management process for the systems and information assets.

&nbsp;&nbsp;&nbsp;&nbsp;iii. Tools and procedures for the backup, transfer, restoration, and secure deletion of information, including physical and electronic media. For this, the following must be considered:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. The provisions relating to the backup, transfer, restoration, and deletion of information, established in the rules that safeguard data protection, including non-disclosure agreements.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. The backup-administration processes that ensure the availability, confidentiality, and integrity of the information upon the occurrence of an incident, which must be concordant with the analysis of the risks for the management of business continuity. The backups of the information must be kept in environments free of malicious code and in facilities distinct from the production sites. In addition, periodic backup-restoration tests, at least annual, must be carried out to verify that the critical information can be recovered if the original data are lost or damaged.

&nbsp;&nbsp;&nbsp;&nbsp;iv. Tools and procedures of identification, authentication, and access control for the digital channels through which the entity interacts with its customers.

&nbsp;&nbsp;&nbsp;&nbsp;v. Tools and procedures so that the information that the entity stores or processes by means of cloud services preserves its characteristics of availability, confidentiality, and integrity.

The entity must have procedures for the management of information-security and cybersecurity incidents, considering:

a) A high-level instance, defined by the board or equivalent body, in charge of the management of information-security and cybersecurity incidents.

b) Response and recovery procedures upon incidents, approved by the board or equivalent body, that consider the timely recovery of the critical functions, the backup and support processes, the critical information assets, and the interdependencies with third parties. Such procedures must consider the provisions relating to the recording, reporting, and communication of incidents. Likewise, depending on the severity of the incident, it shall be appropriate to escalate the situation to the board or equivalent, according to the type of legal person concerned, for decision-making. The response and recovery procedures upon incidents must be updated at least annually, and each time changes are recorded in the information assets or incidents occur that threaten their security.

c) Communications procedures to keep the board or equivalent body informed in a timely manner, according to the type of legal person concerned and this Commission (CMF), as indicated in number 2 below, of the occurrence of an incident and the measures adopted to resolve it. These procedures must consider the provisions relating to the recording, reporting, and communication of incidents of Section III.B.2 of this regulation. In addition, in the case of incidents that affect the quality or continuity of the services to customers, the institution shall be in charge of informing the users in a timely manner of the occurrence of the event, and must update the available information until the root cause of the incident and the measures adopted to resolve it are known.

d) Procedures for the development, acquisition, and updating of the entity's technological infrastructure, that consider:

&nbsp;&nbsp;&nbsp;&nbsp;i. The technological-infrastructure needs of the entity.

&nbsp;&nbsp;&nbsp;&nbsp;ii. Implementation of a change-management process. Before the move to production of a service or information asset, the entities must carry out functional, integral, security, cybersecurity, continuity, and regulatory tests, to ensure that there is no adverse impact on information security and on business operations.

&nbsp;&nbsp;&nbsp;&nbsp;iii. Implementation of a technological-obsolescence-management process, that allows the software and hardware to be kept with support.

&nbsp;&nbsp;&nbsp;&nbsp;iv. Implementation of a software-security-updates-management process.

The entity must have a procedure for the continuous improvement of the information-security and cybersecurity tools, procedures, and controls that considers:

a) Collect and analyze information about the functioning of information assets.

b) Analyze the information-security and cybersecurity incidents and the effectiveness of the measures adopted to resolve them.

c) Execute tests to identify threats and vulnerabilities in information security:

&nbsp;&nbsp;&nbsp;&nbsp;i. The tests shall be carried out with a periodicity not greater than one year, and shall be supervised by the instance responsible for the entity's risk management.

&nbsp;&nbsp;&nbsp;&nbsp;ii. The tests must be based on risk scenarios planned and designed to demonstrate that the implemented mechanisms and tools adequately fulfill their objective of preserving information security, including cyber attacks.

&nbsp;&nbsp;&nbsp;&nbsp;iii. The results of the tests carried out must be reported to the board or equivalent body, including recommendations for improvement in the tools, procedures, and controls.

### Original Spanish

> "1. Gestión de Seguridad de la Información y Ciberseguridad
>
> La entidad deberá considerar los siguientes procedimientos, adaptados a su modelo de negocios, volumen de operaciones, número y tipo de clientes:
>
> a) Contar con una definición clara de activos de información (tecnológicos y no tecnológicos) que sea suficiente para la adecuada gestión de los riesgos asociados.
>
> b) Clasificar la información, teniendo en consideración las dimensiones de disponibilidad, confidencialidad e integridad.
>
> c) Definir los activos de información críticos, indispensables para el funcionamiento de la entidad, clasificados desde una perspectiva de disponibilidad, confidencialidad e integridad.
>
> d) Implementar un inventario de activos de información que permita conocer las principales características del activo.
>
> e) Actualizar el inventario de activos de información en forma periódica.
>
> f) Establecer controles de acceso a las instalaciones e infraestructuras de negocios, operativas y dependencias técnicas.
>
> g) Establecer controles de acceso a los sistemas, de manera de mitigar los riesgos de suplantación o uso indebido por parte de terceros.
>
> h) Implementar herramientas de registro, control y monitoreo de las actividades de los usuarios y administradores de sistemas y activos de información, incluidos usuarios de alto privilegio, para identificar patrones de uso no habituales que generen sospechas de un uso inadecuado.
>
> i) Elaborar procedimientos para otorgar, revocar o modificar los privilegios otorgados a los usuarios de los sistemas, servicios de red, sistemas operativos, bases de datos y aplicaciones de negocios en función de los roles y responsabilidades del personal, cuidando de entregar los accesos estrictamente necesarios para que éste cumpla sus funciones actuales.
>
> j) Establecer controles que permitan mitigar los riesgos derivados del uso de dispositivos móviles y del acceso remoto realizado por personal interno o externo.
>
> k) Verificar los mecanismos de control y monitoreo de las condiciones ambientales para la localización segura de los equipos y herramientas tecnológicas y de comunicaciones.
>
> l) Elaborar procedimientos de seguridad de las operaciones y comunicaciones de la entidad, mediante la implementación de:
>
> i. Herramientas y controles para la detección y protección proactiva de ataques cibernéticos y otras actividades anómalas.
>
> ii. Un proceso de gestión de la configuración de los sistemas y activos de información.
>
> iii. Herramientas y procedimientos para el respaldo, transferencia, restauración y eliminación segura de la información, incluyendo medios físicos y electrónicos. Para ello se deberá considerar:
>
> a. Las disposiciones relativas al respaldo, transferencia, restauración y eliminación de información, establecidas en las normas que resguardan la protección de datos, incluyendo acuerdos de no divulgación.
>
> b. Los procesos de administración de respaldos que aseguren la disponibilidad, confidencialidad e integridad de la información ante la ocurrencia de un incidente, los que deben ser concordantes con el análisis de los riesgos para la gestión de la continuidad del negocio. Los respaldos de la información se deben mantener en ambientes libres de códigos maliciosos y en instalaciones distintas a los sitios de producción. Además, se deben realizar pruebas de restauración de respaldos periódicos, al menos anuales, para verificar que la información crítica se puede recuperar si los datos originales se pierden o dañen.
>
> iv. Herramientas y procedimientos de identificación, autenticación y control de acceso para los canales digitales a través de los cuales la entidad interactúa con sus clientes.
>
> v. Herramientas y procedimientos para que la información que la entidad almacene o procese mediante servicios en la nube conserve sus características de disponibilidad, confidencialidad e integridad.
>
> La entidad deberá contar con procedimientos para la gestión de incidentes de seguridad de la información y ciberseguridad, considerando:
>
> a) Una instancia de alto nivel, definida por el directorio u órgano equivalente, encargada de la gestión de incidentes de seguridad de la información y ciberseguridad.
>
> b) Procedimientos de respuesta y recuperación ante incidentes, aprobados por el directorio u órgano equivalente, que consideren la recuperación oportuna de las funciones críticas, los procesos de respaldo y soporte, los activos de información críticos y las interdependencias con terceros. Dichos procedimientos deberán considerar las disposiciones relativas al registro, reporte y comunicación de incidentes. Asimismo, dependiendo de la severidad del incidente, corresponderá escalar la situación al directorio o equivalente, según el tipo de persona jurídica de que se trate, para la toma de decisiones. Los procedimientos de respuesta y recuperación ante incidentes deberán actualizarse al menos anualmente, y cada vez que se registran cambios en los activos de información o se produzcan incidentes que amenacen la seguridad de éstos.
>
> c) Procedimientos de comunicaciones para mantener informado en forma oportuna al directorio u órgano equivalente, según el tipo de persona jurídica de que se trate y a esta Comisión, según se indica en el número 2 siguiente, de la ocurrencia de un incidente y las medidas adoptadas para resolverlo. Estos procedimientos deberán considerar las disposiciones relativas al registro, reporte y comunicación de incidentes de la Sección III.B.2 de esta Norma. Además, tratándose de incidentes que afecten la calidad o continuidad de los servicios a los clientes, la institución se encargará de informar oportunamente a los usuarios sobre la ocurrencia del evento, debiendo actualizar la información disponible hasta conocer la causa raíz del incidente y las medidas adoptadas para resolverlo.
>
> d) Procedimientos para el desarrollo, adquisición y actualización de la infraestructura tecnológica de la entidad, que consideren:
>
> i. Las necesidades de infraestructura tecnológica de la entidad.
>
> ii. Implementación de un proceso de gestión de cambio. Antes del paso a producción de un servicio o activo de información, las entidades deben realizar pruebas funcionales, integrales, de seguridad, de ciberseguridad, de continuidad y normativas, para asegurar que no haya impacto adverso en la seguridad de la información y en las operaciones del negocio.
>
> iii. Implementación de un proceso de gestión de obsolescencia tecnológica, que permita mantener el software y hardware con soporte.
>
> iv. Implementación de un proceso de gestión de actualizaciones de seguridad de software.
>
> La entidad deberá contar con un procedimiento para el mejoramiento continuo de las herramientas, procedimientos y controles de seguridad de la información y ciberseguridad que considere:
>
> a) Recolectar y analizar información sobre el funcionamiento de activos de información.
>
> b) Analizar los incidentes de seguridad de la información y ciberseguridad y la efectividad de las medidas adoptadas para resolverlo.
>
> c) Ejecutar pruebas para identificar amenazas y vulnerabilidades en la seguridad de la información:
>
> i. Las pruebas se realizarán con una periodicidad no mayor a un año, y se supervisarán por la instancia responsable de la gestión de riesgos de la entidad.
>
> ii. Las pruebas deberán estar basadas en escenarios de riesgo planificados y diseñados para demostrar que los mecanismos y herramientas implementados para preservar la seguridad de la información cumplen adecuadamente con su objetivo, incluyendo ataques cibernéticos.
>
> iii. Los resultados de las pruebas realizadas deberán ser reportados al directorio u órgano equivalente, incluyendo recomendaciones de mejora en las herramientas, procedimientos y controles."

### Cross-references
- Ley 21.521 Art. 22 — the information-security and cybersecurity management duties this subparagraph develops.
- NCG 514 §III.B.2 — the incident recording, reporting, and communication provisions referenced in the incident-management procedures.
- NCG 514 §III.B.2.3 — the business-continuity analysis with which backup-administration must be concordant.
- Ley 19.628 — the data-protection rules that govern the backup, transfer, restoration, and deletion of information referenced in item l.iii.a.

> **TN:** The Spanish nests two distinct enumeration levels under item l.iii (roman numerals "i–v" for sub-tools, then lower-case letters "a, b" for backup sub-elements); the English preserves both levels with the corresponding indentation. The page break between PDF pages 43 and 44 splits item l.iii across pages; reassembled here as a single item.

> **Source:** NCG 514 §III.B.1 (03-jul-2024).

---

## III.B.2 — Information on Incidents
**NCG anchor:** N° 514, Sección III, B.2
**Implements:** Ley 21.521 Art. 22 (reporting of incidents affecting the SFA)
**Tags:** open-finance, incidents, reporting, cybersecurity, business-continuity

### Plain-English text

This subparagraph governs the information on incidents (incidentes) that the actors and participants of the SFA must communicate to the Commission (CMF). It comprises subparagraphs 2.1 (operational-incident reports), 2.2 (cybersecurity-incident reports), and 2.3 (business continuity). The substantive rules begin at subparagraph 2.1 below.

### Original Spanish

> "2. Información de incidentes"

### Cross-references
- Ley 21.521 Art. 22 — the incident-reporting duties of SFA Participants that this subparagraph organizes.
- NCG 514 §III.B.2.1–§III.B.2.3 — the sub-subparagraphs that make up this subparagraph.
- NCG 514 §III.B.1 — the incident-management procedures that reference these reporting provisions.

> **Source:** NCG 514 §III.B.2 (03-jul-2024).

---

## III.B.2.1 — Operational-Incident Reports
**NCG anchor:** N° 514, Sección III, B.2.1
**Implements:** Ley 21.521 Art. 22 (reporting of operational incidents in the SFA)
**Tags:** open-finance, incidents, operational, reporting, responsible-officer

### Plain-English text

a) The actors of the SFA must communicate to this Commission (CMF) the operational incidents that affect the business continuity, the resources, and the information of the entity or of its customers, and the quality of the services related to the SFA. By way of example, and without being exhaustive, they must report: failures in services important for the operations of the business; technological problems that affect information security; cyberspace attacks; viruses or malware detected in the network; events of unavailability or interruption of any service or product that affects customers, on any channel; losses or leaks of information of the entity or of customers; and incidents that affect the patrimony of the entity or of customers, as a result of internal or external frauds.

b) The participants of the SFA must report to the Commission (CMF) the occurrence of any event that compromises the integrity or security of the information assets or operational events.

c) When this Commission (CMF) considers it necessary, it may require from the entity an internal report with: analysis of the causes of the incident; generation of documentation and investigation reports; analysis of the impact on the services; procedure to avoid the incident being repeated; and other additional matters that this Commission (CMF) may require in this respect.

d) The board or equivalent body must designate an officer in charge (funcionario encargado) and a substitute to report and send information on operational incidents to the Commission (CMF) and keep it informed in a timely manner with respect to the incident and the measures adopted to resolve it.

### Original Spanish

> "2.1 Reportes incidentes operacionales
>
> a) Los actores del SFA deberán comunicar a esta Comisión los incidentes operacionales que afecten la continuidad del negocio, los recursos e información de la entidad o de sus clientes, y la calidad de los servicios relacionados con el SFA. Como ejemplo, y sin ser exhaustivos, deberán reportarse fallas en servicios importantes para las operaciones del negocio; problemas tecnológicos que afecten la seguridad de la información; ataques del ciberespacio; virus o malware detectados en la red; eventos de indisponibilidad o interrupción de algún servicio o producto que afecte a los clientes, en cualquier canal; pérdidas o fugas de información de la entidad o de clientes; e incidentes que afecten el patrimonio de la entidad o de los clientes, producto de fraudes internos o externos.
>
> b) Los participantes del SFA deberán reportar a la Comisión la ocurrencia de todo evento que comprometa la integridad o seguridad de los activos de información o eventos operacionales.
>
> c) Cuando esta Comisión lo considere necesario, podrá requerir a la entidad un informe interno con: análisis de las causas del incidente; generación de documentación e informes de investigación; análisis del impacto en los servicios; procedimiento para evitar que el incidente se repita; y otras materias adicionales que esta Comisión pueda requerir al respecto.
>
> d) El directorio u órgano equivalente deberá designar un funcionario encargado y un suplente para reportar y enviar información de incidentes operacionales a la Comisión y mantenerla informado oportunamente respecto al incidente y las medidas adoptadas para resolverlo."

### Cross-references
- Ley 21.521 Art. 22 — the operational-incident reporting duties this sub-subparagraph develops.
- NCG 514 §III.B.2.2 — the cybersecurity-incident reporting procedure (RIO platform, timing, and report content).
- NCG 514 §II.D — the information-quality deficiencies that are reported through the operational-incident channels.

> **Source:** NCG 514 §III.B.2.1 (03-jul-2024).

---

## III.B.2.2 — Cybersecurity-Incident Reports
**NCG anchor:** N° 514, Sección III, B.2.2
**Implements:** Ley 21.521 Art. 22 (reporting of cybersecurity incidents in the SFA)
**Tags:** open-finance, incidents, cybersecurity, rio, reporting, timing

### Plain-English text

The communication to the CMF of the operational incidents must be carried out by means of the Operational-Incidents Report (Reporte de Incidentes Operacionales) (RIO) present on the CMF website, at any time, on both business and non-business days, within the maximum term of 30 minutes elapsed from the moment the entity became aware of the fact. With respect to institutions that currently maintain other regulations with a reporting time different from the aforementioned, they must consider, for the purpose of the incidents related to the SFA, the reporting time mentioned above. Where appropriate, this report must be supplemented with new follow-up reports of the incident with the resolution of the problem, the actions to be taken, and the causes of the incident.

For these purposes, the entity must designate an officer in charge (funcionario encargado), who shall carry out the reports and shall send the information as indicated in this numeral, and whose designation and/or replacement must be communicated to the CMF. This person, or whoever replaces them, who could be the same as those already designated in numeral 2.1, must have an executive level and be designated by the entity both for this purpose and to respond to eventual queries from the Commission (CMF). The information must be reported in accordance with the following scheme:

1) *At the moment of the start of the incident (Al momento de inicio del incidente).* The report must include, at least, the following aspects:

&nbsp;&nbsp;&nbsp;&nbsp;a. Unique identifying number of the incident (assigned by the CMF).

&nbsp;&nbsp;&nbsp;&nbsp;b. Name of the reporting entity.

&nbsp;&nbsp;&nbsp;&nbsp;c. Name and telephone of the reporting person.

&nbsp;&nbsp;&nbsp;&nbsp;d. Description of the incident.

&nbsp;&nbsp;&nbsp;&nbsp;e. Date and time of the start of the incident.

&nbsp;&nbsp;&nbsp;&nbsp;f. Possible or identified causes.

&nbsp;&nbsp;&nbsp;&nbsp;g. Products or services affected.

&nbsp;&nbsp;&nbsp;&nbsp;h. Type and name of supplier or third party involved (if applicable).

&nbsp;&nbsp;&nbsp;&nbsp;i. Type and estimated number of customers affected.

&nbsp;&nbsp;&nbsp;&nbsp;j. Dependencies and/or assets affected (if applicable).

&nbsp;&nbsp;&nbsp;&nbsp;k. Measures adopted and in progress.

&nbsp;&nbsp;&nbsp;&nbsp;l. Other background information.

Not having all the information of the fields mentioned must not be an impediment to sending the communication within the term defined in this numeral. As indicated previously, the initial report must be supplemented by the entity, to the extent that it has the relevant information with respect to the incident.

2) *At the moment of closure of the incident (Al momento de cierre del incidente).* Once the incident has been overcome, this situation must be reported through the platform already mentioned. Such report must include, at least, the following aspects:

&nbsp;&nbsp;&nbsp;&nbsp;a. Unique identifying number of the incident.

&nbsp;&nbsp;&nbsp;&nbsp;b. Name of the reporting entity.

&nbsp;&nbsp;&nbsp;&nbsp;c. Name and telephone of the reporting person.

&nbsp;&nbsp;&nbsp;&nbsp;d. Description of the incident.

&nbsp;&nbsp;&nbsp;&nbsp;e. Identified causes.

&nbsp;&nbsp;&nbsp;&nbsp;f. Date and time of the start of the incident.

&nbsp;&nbsp;&nbsp;&nbsp;g. Date of closure of the incident.

&nbsp;&nbsp;&nbsp;&nbsp;h. Products or services affected.

&nbsp;&nbsp;&nbsp;&nbsp;i. Type and name of supplier involved (if applicable).

&nbsp;&nbsp;&nbsp;&nbsp;j. Type and number of customers affected.

&nbsp;&nbsp;&nbsp;&nbsp;k. Dependencies and/or assets affected (if applicable).

&nbsp;&nbsp;&nbsp;&nbsp;l. Measures adopted.

&nbsp;&nbsp;&nbsp;&nbsp;m. Other background information.

### Original Spanish

> "2.2 Reportes incidentes de ciberseguridad
>
> La comunicación a la CMF de los incidentes operacionales deberá realizarse a través del Reporte de Incidentes Operacionales (RIO) presente en el sitio web de la CMF, en cualquier horario, tanto en días hábiles como no hábiles, en el plazo máximo de 30 minutos transcurridos desde que la entidad tomó conocimiento del hecho. Respecto a instituciones que mantienen actualmente otra normativa con un tiempo distinto de reporte, deberán considerar para efecto de los incidentes relacionados con el SFA el tiempo de información antes mencionado. Cuando corresponda, este informe se deberá complementar con nuevos reportes de seguimiento del incidente con la resolución del problema, las acciones a tomar y las causas del incidente.
>
> Para estos efectos, la entidad deberá designar un funcionario encargado, quien realizará los reportes y enviará la información según lo indicado en este numeral, y su designación y/o reemplazo deberá ser comunicado a la CMF. Esta persona, o quien la reemplace, que podrían ser los mismos ya designados en el numeral 2.1, deberán tener un nivel ejecutivo y ser designado por la entidad tanto para este efecto, como para responder eventuales consultas por parte de la Comisión. La información deberá ser reportada de acuerdo con el siguiente esquema:
>
> 1) Al momento de inicio del incidente. El reporte deberá incluir, al menos, los siguientes aspectos:
>
> a. Número único identificador del incidente (asignado por la CMF).
>
> b. Nombre de la entidad informante.
>
> c. Nombre y teléfono de la persona informante.
>
> d. Descripción del incidente.
>
> e. Fecha y hora de inicio del incidente.
>
> f. Causas posibles o identificadas.
>
> g. Productos o servicios afectados.
>
> h. Tipo y nombre de proveedor o tercero involucrado (si corresponde).
>
> i. Tipo y número estimado de clientes afectados.
>
> j. Dependencias y/o activos afectados (si corresponde).
>
> k. Medidas adoptadas y en curso.
>
> l. Otros antecedentes.
>
> No contar con toda la información de los campos mencionados no debe ser impedimento para enviar la comunicación en el plazo definido en este numeral. Tal como se señaló previamente, el reporte inicial debe ser complementado por la entidad, en la medida que disponga de la información relevante respecto del incidente.
>
> 2) Al momento de cierre del incidente. Una vez superado el incidente, se deberá informar de esta situación a través de la plataforma ya mencionada. Dicho reporte deberá incluir, al menos, los siguientes aspectos:
>
> a. Número único identificador del incidente.
>
> b. Nombre de la entidad informante.
>
> c. Nombre y teléfono de la persona informante.
>
> d. Descripción del incidente.
>
> e. Causas identificadas.
>
> f. Fecha y hora de inicio del incidente.
>
> g. Fecha de cierre del incidente.
>
> h. Productos o servicios afectados.
>
> i. Tipo y nombre de proveedor involucrado (si corresponde).
>
> j. Tipo y número de clientes afectados.
>
> k. Dependencias y/o activos afectados (si corresponde).
>
> l. Medidas adoptadas.
>
> m. Otros antecedentes."

### Cross-references
- Ley 21.521 Art. 22 — the incident-reporting duties this sub-subparagraph develops.
- NCG 514 §III.B.2.1 — the operational-incident reports whose officer in charge may be the same person designated here.
- NCG 514 §III.B.1 — the incident-management procedures that invoke these reporting requirements.

> **Source:** NCG 514 §III.B.2.2 (03-jul-2024).

---

## III.B.2.3 — Business Continuity
**NCG anchor:** N° 514, Sección III, B.2.3
**Implements:** Ley 21.521 Art. 22 (business continuity of SFA Participants)
**Tags:** open-finance, business-continuity, crisis-plan, bia, disaster-recovery

### Plain-English text

In the field of business continuity (continuidad del negocio), the Participants of the SFA must take into account the following minimum elements, adapted according to the business model, volume of operations, and number and type of customers:

a) Have a business-continuity policy that considers at least the following:

&nbsp;&nbsp;&nbsp;&nbsp;i. Response procedures upon the occurrence of internal or external events that could create an interruption in the continuity of the business operations.

&nbsp;&nbsp;&nbsp;&nbsp;ii. Definition of the principal functions and responsibilities on the matter, in particular, which shall be the instances in charge of defining, designing, executing, and improving the procedures and methodologies for business-continuity management.

&nbsp;&nbsp;&nbsp;&nbsp;iii. The business-continuity policies, which must be updated and approved annually by the board or its equivalent, according to the type of legal person concerned, and each time significant changes occur.

b) Have persons with verifiable knowledge or experience in business-continuity standards and experience in the management of the associated risks, whose principal activities shall be the development and improvement of the policies, procedures, and controls for business-continuity management.

c) Have training and awareness policies and procedures to guarantee that the entity's personnel are duly prepared to face the defined contingency scenarios and that they understand their responsibilities in the management of the risks of the business-continuity system.

d) Establish procedures that allow the Board or equivalent body to be informed in a timely and periodic manner about business-continuity management. Record of the reporting of information on these matters must be left in the respective minutes of the Board or equivalent body and in the Committees formed to review these matters.

As regards the procedures to address events that compromise the availability in the provision of the service, these institutions must adopt at least the following procedures:

a) A Crisis Plan (Plan de Crisis) in which the procedures for escalation, communications, management, and reporting of operational-continuity events are determined in order to keep the Board or equivalent informed in a timely manner, according to the type of legal person concerned, all interested parties, and this Commission (CMF), with respect to relevant information referring to the continuity event, the measures adopted to resolve it, and to coordinate an adequate response within the objective points and objective recovery times provided in the Business Impact Analysis (Análisis de Impacto del Negocio) (BIA).

b) A procedure for the continuous improvement of the business-continuity policies, plans, and procedures, in order to reduce the response times when an equal or similar incident is repeated; identify improvements in the processes; facilitate the exchange of knowledge; and have information that allows decision-making to be supported if new incidents materialize.

c) Annual tests of the Business-Continuity Plan and Disaster Recovery, with the aim of ensuring that it is adequate and effective. These tests must consider at least the following:

&nbsp;&nbsp;&nbsp;&nbsp;i. They must be supervised by the instance responsible for the entity's Risk Management.

&nbsp;&nbsp;&nbsp;&nbsp;ii. They must be based on risk scenarios that are similar to real events, including severe but plausible scenarios. The foregoing, in order to demonstrate that the business-continuity procedures will function in case of being necessary, including cyber attacks, disasters, and sanitary and social contingencies. Reports of the results of the tests carried out must be prepared and issued to the Board or equivalent body, that contain, where appropriate, recommendations and actions to implement improvements to the Business-Continuity Plan and Disaster Recovery.

### Original Spanish

> "2.3 Continuidad del negocio
>
> En el ámbito de continuidad de negocio los Participantes del SFA deberán tomar en cuenta los siguientes elementos mínimos, adaptados de acuerdo con el modelo de negocios, volumen de operaciones, y número y tipo de clientes:
>
> a) Contar con una política de continuidad de negocio que considere a lo menos lo siguiente:
>
> i. Procedimientos de respuesta ante la ocurrencia de eventos internos o externos que pudieran crear una interrupción en la continuidad de las operaciones del negocio.
>
> ii. Definición de las principales funciones y responsabilidades sobre la materia, en especial, cuáles serán las instancias encargadas de definir, diseñar, ejecutar y mejorar los procedimientos y metodologías para la gestión de continuidad de negocio.
>
> iii. Las políticas de continuidad de negocio, las que deben ser actualizadas y aprobadas anualmente por el directorio o su equivalente, según el tipo de persona jurídica de que se trate, y cada vez que se produzcan cambios significativos.
>
> b) Contar con personas con conocimientos o experiencia comprobables en estándares de continuidad de negocio y experiencia en la gestión de los riesgos asociados, cuyas actividades principales serán el desarrollo y mejora de las políticas, procedimientos y controles para la gestión de continuidad de negocio.
>
> c) Contar con políticas y procedimientos de capacitación y concientización para garantizar que el personal de la entidad esté debidamente preparado para enfrentar los escenarios de contingencia definidos y que comprendan sus responsabilidades en la gestión de los riesgos del sistema de continuidad de negocio.
>
> d) Establecer procedimientos que permitan informar oportuna y periódicamente al Directorio u órgano equivalente sobre la gestión de continuidad de negocio. Deberá dejarse constancia del reporte de la información en estas materias en las respectivas actas del Directorio u órgano equivalente y en los Comités que se conformen para revisar estas materias.
>
> En cuanto a los procedimientos para abordar eventos que comprometan la disponibilidad en la prestación del servicio, estas instituciones deberán adoptar como mínimo los siguientes procedimientos:
>
> a) Plan de Crisis en el que se determine los procedimientos de escalamiento, comunicaciones, gestión y reporte de eventos de continuidad operacional para mantener informado en forma oportuna al Directorio o equivalente, según el tipo de persona jurídica de que se trate, a todas las partes interesadas y a esta Comisión, respecto de información relevante referida al evento de continuidad, las medidas adoptadas para resolverlo y para coordinar una respuesta adecuada dentro de los puntos objetivos y tiempos objetivos de recuperación previstos en el Análisis de Impacto del Negocio (BIA).
>
> b) Procedimiento para el mejoramiento continuo de las políticas, planes y procedimientos de continuidad del negocio para disminuir los tiempos de respuesta cuando se repita un incidente igual o similar; identificar mejoras en los procesos; facilitar el intercambio de conocimientos; y tener información que permita apoyar la toma de decisiones si se materializan nuevos incidentes.
>
> c) Pruebas anuales del Plan de Continuidad de Negocio y Recuperación de Desastres, con el fin de asegurar que es adecuado y efectivo. Estas pruebas deberán considerar a lo menos lo siguiente:
>
> i. Deberán ser supervisadas por la instancia responsable de la Gestión de Riesgos de la entidad.
>
> ii. Deberán estar basadas en escenarios de riesgo que se asimilen a eventos reales, incluyendo escenarios severos, pero plausibles. Lo anterior, para demostrar que los procedimientos de continuidad de negocio funcionarán en caso de ser necesarios, incluyendo ataques cibernéticos, desastres, y contingencias sanitarias y sociales. Se deberán elaborar y emitir reportes de los resultados de las pruebas realizadas al Directorio u órgano equivalente, que contengan, cuando corresponda, recomendaciones y acciones para implementar mejoras al Plan de Continuidad de Negocio y Recuperación ante Desastres."

### Cross-references
- Ley 21.521 Art. 22 — the business-continuity duties of SFA Participants that this sub-subparagraph develops.
- NCG 514 §III.A.3 — the risk-management plan that must contemplate operational-continuity risks.
- NCG 514 §III.B.1 — the backup-administration processes that must be concordant with business-continuity risk analysis.

> **Source:** NCG 514 §III.B.2.3 (03-jul-2024).

---

## III.B.3 — Information-Security and Contingency Standards of the APIs
**NCG anchor:** N° 514, Sección III, B.3
**Implements:** Ley 21.521 Art. 22 (information-security and contingency standards for the SFA interfaces/APIs)
**Tags:** open-finance, apis, information-security, contingency, encryption, retention

### Plain-English text

The supervised entities must have policies, procedures, and technical and human resources to monitor that the data requests submitted through APIs are carried out under conditions of security. For this purpose, the supervised entities must comply, as a minimum, with the following instructions:

a) Monitor the information of the APIs, having to verify and guarantee that the specifications of the fields of the data requests of the APIs and their responses conform to the definitions stipulated for the exchange of information among the participants of the SFA.

b) Have adequate safeguards and backups of the information in conformity with the best practices and with the laws and regulations applicable in this matter. The entities must take the necessary safeguards to avoid leaks, losses, or exposure of the information and the resources that can be accessed through the APIs.

c) Maintain a record of the events proper to the SFA (for example, the data request made through the API), for a minimum term of 5 years, which must contain the information necessary to determine, as a minimum: the participant that made the request; the moment at which it was made; the information that is transmitted in the API; and the result of the process. In any event, according to the level of sensitivity or criticality of the information, it must be encrypted.

d) Correctly delete the information once the maximum legal terms to maintain historical information expire.

Contingency sites shall be requested that allow continuity of the functioning of the system in case of failure of the processing sites that give support to the APIs due to operational incidents.

### Original Spanish

> "3. Estándares de seguridad de la información y de contingencia de las APIs
>
> Las entidades supervisadas deben contar con políticas, procedimientos y recursos técnicos y humanos para monitorear que las solicitudes de datos presentadas a través de API se realicen en condiciones de seguridad. Para el efecto, las entidades vigiladas deben dar cumplimiento, como mínimo, a las siguientes instrucciones:
>
> a) Monitorear la información de las APIs, debiendo verificar y garantizar que las especificaciones de los campos de las solicitudes de datos de las APIs y sus respuestas se ajusten a las definiciones estipuladas para el intercambio de información entre los participantes del SFA.
>
> b) Contar con resguardos y respaldos adecuados de la información en conformidad a las mejores prácticas y a las leyes y normativas aplicables en esta materia. Las entidades deberán tomar los resguardos necesarios para evitar filtraciones, pérdidas, o exposición de la información y los recursos a los que pueden acceder a través de las APIs.
>
> c) Mantener registro de los eventos propios del SFA (por ejemplo, la solicitud de datos realizada a través de las API), por un plazo mínimo de 5 años, los cuales deben contener la información necesaria para determinar, como mínimo: el participante que realizó la solicitud; el momento en que ésta se realizó; la información que se transmite en la API; y el resultado del proceso. En todo caso, según el nivel de sensibilidad o criticidad de la información, ésta se deberá encriptar.
>
> d) Eliminar correctamente la información una vez que venzan los plazos máximos legales para mantener información histórica.
>
> Se solicitará sitios de contingencia que permitan dar continuidad al funcionamiento del sistema en caso de fallar los sitios de procesamiento que den soporte a las APIs debido a incidentes operacionales."

### Cross-references
- Ley 21.521 Art. 22 — the information-security and contingency standards for the SFA APIs that this subparagraph develops.
- NCG 514 §II.A — the APIs (means of information exchange) whose security and contingency this subparagraph regulates.
- NCG 514 §II.B — the alternative mechanism for delivery of information upon unavailability of the APIs.
- Ley 19.628 — the data-protection laws applicable to the safeguards, retention, and deletion of the information referenced in items b and d.

> **Source:** NCG 514 §III.B.3 (03-jul-2024).

---

## III.C — Authentication and Verification
**NCG anchor:** N° 514, Sección III, C
**Implements:** Ley 21.521 Art. 22 (authentication and verification standards of the SFA)
**Tags:** open-finance, authentication, verification, sca

### Plain-English text

This subsection governs the authentication (autenticación) and verification (verificación) standards of the SFA: the minimum authentication and customer-confirmation standards, the authentication of the financial customer by the IPI and IPC, and the verification standards of the PSBI and PSIP. It comprises subparagraphs C.1 (minimum authentication and customer-confirmation standards), C.2 (authentication of the financial customer by the IPI and IPC), and C.3 (verification standards of the PSBI and PSIP). The substantive rules begin at subparagraph C.1 below.

### Original Spanish

> "C. Autenticación y verificación"

### Cross-references
- Ley 21.521 Art. 22 — the authentication and verification standards of the SFA that this subsection develops.
- NCG 514 §III.C.1–§III.C.3 — the subparagraphs that make up this subsection.

> **Source:** NCG 514 §III.C (03-jul-2024).

---

## III.C.1 — Minimum Authentication and Customer-Confirmation Standards
**NCG anchor:** N° 514, Sección III, C.1
**Implements:** Ley 21.521 Art. 22 (minimum authentication standards for the SFA)
**Tags:** open-finance, authentication, openid-connect, oauth, standards

### Plain-English text

It shall be appropriate to use, where applicable, the OpenID Connect standard — based on identity layers added on top of the OAuth read/write data-access authorization standard in its version 2.0 — on the terms and under the operational flows that are developed in Annex N° 3 of this regulation, for the services and APIs that are described therein.

### Original Spanish

> "1. Estándares mínimos de autenticación y confirmación de clientes
>
> Corresponderá utilizar, en lo que corresponda, el estándar Open ID Connect, -basado en capas de identificación aditivas sobre el estándar de autorización de acceso a lectura o escritura de datos OAuth en su versión 2.0., en los términos y bajo los flujos operativos que se desarrollen en el Anexo N°3 de esta Norma, para los servicios y APIs que allí se describan."

### Cross-references
- Ley 21.521 Art. 22 — the authentication standards of the SFA that this subparagraph fixes.
- NCG 514 §II.A.2 — Table N° 1, which fixes OAuth 2.0 and OpenID Connect as the authorization/authentication standard of the APIs.
- NCG 514 Annex N° 3 — the operational flows for the OpenID Connect standard referenced here.

> **Source:** NCG 514 §III.C.1 (03-jul-2024).

---

## III.C.2 — Authentication of the Financial Customer by the IPI and IPC
**NCG anchor:** N° 514, Sección III, C.2
**Implements:** Ley 21.521 Art. 22 (strong customer authentication in the SFA)
**Tags:** open-finance, authentication, sca, mfa, payment-initiation

### Plain-English text

Strong Customer Authentication (SCA) (Autenticación Reforzada del Cliente / ARC) shall be required for the query of SFA data that considers access to customer information subject to the granting of their consent.

This authentication must consider the use of two or more elements categorized as knowledge (something the user knows), possession (something the user possesses), and inherence (something the user is), which must be independent of one another, in the sense that the non-compliance of one of them does not compromise the reliability of the others, and each one of them must be designed in such a manner that it protects the confidentiality of the authentication data.

The IPI and IPC must, once the PSBI and PSIP have been authenticated, require the authentication of the Customer, which shall include the authorization of access and confirmation of charges in the case of payment initiation. This authentication can only be carried out by means of SCA schemes on the basis of mechanisms compatible with the methods already available that the IPI and IPC have in operation for the access to their electronic channels by their customers.

### Original Spanish

> "2. Autenticación del cliente financiero por parte de la IPI e IPC
>
> Se requerirá una Autenticación Reforzada del Cliente -ARC- para la consulta de datos del SFA que consideren el acceso a información de clientes sujeto al otorgamiento de su consentimiento.
>
> Esta autenticación deberá considerar el uso de dos o más elementos categorizados como conocimiento (algo que el usuario sabe), posesión (algo que el usuario posee) e inherencia (algo que el usuario es), los cuales deberán ser independientes entre sí, en el sentido de que el incumplimiento de uno de ellos no compromete la confiabilidad de los demás, y cada uno de ellos deberá estar diseñado, de tal manera, que proteja la confidencialidad de los datos de autenticación.
>
> Las IPI e IPC deberán, una vez autenticado al PSBI y PSIP, requerir la autenticación del Cliente, lo que incluirá la autorización de acceso y confirmación de cargos tratándose de iniciación de pagos. Esta autenticación solo puede hacerse mediante esquemas ARC sobre la base de mecanismos compatibles con los métodos ya disponibles que tengan en funcionamiento las IPI e IPC para el acceso a sus canales electrónicos por parte de sus clientes."

### Cross-references
- Ley 21.521 Art. 22 — the strong-customer-authentication requirement in the SFA that this subparagraph develops.
- NCG 514 §III.D — the consent regime to which customer authentication is tied.
- NCG 514 §III.C.1 — the OpenID Connect / OAuth 2.0 standards underlying this authentication.

> **TN:** The Spanish defines the term "Autenticación Reforzada del Cliente -ARC-", rendered here as Strong Customer Authentication (SCA), per the locked SFA-term mapping; the Spanish acronym ARC is preserved in the Original Spanish block.

> **Source:** NCG 514 §III.C.2 (03-jul-2024).

---

## III.C.3 — Verification Standards of the PSBI and PSIP by the IPI and IPC
**NCG anchor:** N° 514, Sección III, C.3
**Implements:** Ley 21.521 Art. 22 (verification of participants via digital certificates in the SFA)
**Tags:** open-finance, verification, digital-certificate, ca, participants-directory

### Plain-English text

The IPI and IPC must receive a Digital Certificate from the PSBI or PSIP, in which their identity is authenticated. This Digital Certificate must be issued by a Certification Authority that complies with the requirements and the extended-validation practices of the identity and nature of the requiring Participant that are defined in Annex N° 3 of the regulation.

Additionally, the IPI and IPC must compare and confirm the permissions/roles indicated by the certificate against the profiles authorized in the Directory that the Commission (CMF) shall keep for these purposes.

This confirmation with the Participants Directory must be carried out in accordance with what is established in Annex N° 3 of this regulation, on the basis of the request that accompanies the certificate.

The currency of the service of each PSBI and PSIP must be confirmed on the terms detailed in Annex N° 3 of this regulation.

### Original Spanish

> "3. Estándares de verificación del PSBI y PSIP por parte del IPI e IPC
>
> Las IPI e IPC deberán recibir un Certificado Digital por parte del PSBI o PSIP donde se autentique su identidad. Este Certificado Digital deberá ser emitido por una Autoridad Certificadora que cumpla los requisitos y las prácticas de validación extendida de la identidad y naturaleza del Participante requirente que se definan en el Anexo N°3 de la Norma.
>
> Adicionalmente, la IPI e IPC deberá comparar y confirmar los permisos/roles indicados por el certificado versus los perfiles autorizados en el Directorio que llevará la Comisión para estos efectos.
>
> Esta confirmación con el Directorio de Participantes deberá ser realizada de acuerdo con lo que se establezca en el Anexo N°3 de la presente normativa, en función de la solicitud que acompaña al certificado.
>
> Deberá confirmarse la vigencia del servicio de cada PSBI y PSIP en los términos que se detallen en el Anexo N°3 de esta Norma."

### Cross-references
- Ley 21.521 Art. 22 — the participant-verification requirement in the SFA that this subparagraph develops.
- NCG 514 §II.C — the Participants Directory against which the certificate permissions/roles are confirmed.
- NCG 514 Annex N° 3 — the CA requirements, extended-validation practices, and confirmation procedures referenced.

> **Source:** NCG 514 §III.C.3 (03-jul-2024).

---

## III.D — Consent
**NCG anchor:** N° 514, Sección III, D
**Implements:** Ley 21.521 Art. 23 (open-finance consent) AND Ley 19.628 Art. 12 (data-subject consent)
**Tags:** open-finance, consent, data-protection, titular

### Plain-English text

This subsection governs the consent (consentimiento) regime of the SFA: the granting of consent and the management of consent together with the information obligations. It comprises subparagraphs D.1 (granting of consent) and D.2 (management of consent and information obligations). The substantive rules begin at subparagraph D.1 below.

This subsection is the junction between the open-finance regime and the personal-data-protection regime: the consent granted under Título III of Ley 21.521 operationalizes the data-subject consent required by Ley 19.628 for the processing of personal data.

### Original Spanish

> "D. Consentimiento"

### Cross-references
- Ley 21.521 Art. 23 — the open-finance consent regime of the SFA that this subsection develops.
- Ley 19.628 Art. 12 — the data-subject (titular) consent for the processing of personal data that this subsection operationalizes in the open-finance context.
- NCG 514 §III.D.1–§III.D.2 — the subparagraphs that make up this subsection.

> **Source:** NCG 514 §III.D (03-jul-2024).

---

## III.D.1 — Granting of Consent
**NCG anchor:** N° 514, Sección III, D.1
**Implements:** Ley 21.521 Art. 23 (granting of open-finance consent) AND Ley 19.628 Art. 12 (free, informed, specific data-subject consent)
**Tags:** open-finance, consent, data-protection, titular, dark-patterns, durable-medium

### Plain-English text

For the purposes of what is established in Título III of Ley N° 21.521, the consent shall be deemed granted by the data subject (titular), both for the IPI and IPC and for the PSBI and PSIP, where the following conditions are complied with:

a) That the will has been manifested in an express manner, on the following terms:

&nbsp;&nbsp;&nbsp;&nbsp;i. *In the case of a Natural Person (En el caso de Persona Natural)*: by the respective data subject (titular), their legal representative, or proxy (mandatario) with specific power to authorize the transmission and processing of the data or to authorize the initiation of payments, as appropriate.

&nbsp;&nbsp;&nbsp;&nbsp;ii. *In the case of a Legal Person (En el caso de Persona Jurídica)*: by the legal representative(s) or attorneys-in-fact, authorized either to act jointly or separately, in the case of payment initiation, or any of the legal representatives or proxies (mandatarios) with specific power to authorize the transmission and processing of the corresponding data.

b) That the PSBI and PSIP have implemented the consent-management mechanism on the terms and conditions established in Section III.E.2 of this regulation.

c) That the will is stored on a durable medium (soporte duradero), that is apt to safeguard its security, integrity, and access, with respect to the identity of the data subject (titular), as well as to the circumstances and conditions under which it was requested and granted, in a manner that it may subsequently be verified that such consent was manifested in a free, informed, express, and specific manner as to the type of information required, the purpose, and the maximum validity period of that authorization.

d) That the person or computer system that interacts with the data subject (titular) or customer shall not exercise any undue influence over them to induce them to manifest their will. For example, the use of interfaces that induce users to take unintended, involuntary, or potentially harmful decisions with respect to their personal data; requiring that the consent be granted for the application of a discount or obtaining of royalties; conditioning the provision of the service on it, unless its provision is unviable without such consent; or that the options employed for it to be granted are marked by default, are in colors, sizes, or font styles that highlight them over those options that refer to not granting the consent or with respect to those established for shorter periods.

e) At the moment of requesting the consent for the transmission, processing, or assignment of data, or initiation of payments, the data subject or customer must be precisely and clearly informed of the data on which the exchange, processing, assignment to third parties, or initiation within the framework of the SFA is consented to; to which institution the authorization for it is conferred, or to initiate and process the payment(s); for what period or frequency; and for what purpose. Such request shall not contain other information or require the consent of the data subject or customer for distinct acts or purposes.

f) That the data on which the consent bears, and its currency, are strictly necessary for the respective purpose, a circumstance that the PSBI or PSIP must accredit when it is required by the Commission (CMF) within the framework of its supervision processes, it not being appropriate for the IPI or IPC to pronounce in that respect or to alter the original requirement formulated by the PSBI or PSIP within the framework of the SFA.

g) That the information that is brought to the knowledge of the data subject or customer to obtain the consent is expressed in simple, clear, precise language and avoiding technicalities, except in cases where it proves strictly necessary, having to explain them clearly. In addition, it must have mechanisms that allow persons in a situation of disability to access this information.

h) Once the data subject or customer has granted the consent, they must be informed that both the PSBI or PSIP and the IPI or IPC shall make available to them a control panel and the manner in which they may access it, by means of which they may know, verify, and revoke the consents they have granted.

i) That the data subject (titular) or customer has been authenticated in accordance with the standards that are established for it in Section III.C of this regulation.

It is prohibited for the IPI or the IPC to alter the content of the consent request formulated by the PSBI or PSIP within the framework of the SFA, to ask for an additional consent for the same exchange, processing, or initiation, to adopt measures or practices that disincentivize the granting of the consent, or that deteriorate the user experience of those data subjects or customers. At the moment of adopting or implementing new technologies, the IPI or IPC must tend to the use of those that improve the user experience and minimize the number of redirections of the user within the framework of the SFA.

Once the consent has been granted, it must be communicated and stored simultaneously both by the PSBI or PSIP and by the respective IPI or IPC.

### Original Spanish

> "1. Otorgamiento del consentimiento
>
> Para efectos de lo establecido en el Título III de la Ley N°21.521 se reputará otorgado el consentimiento por parte del titular de los datos, tanto para la IPI e IPC, como para el PSBI y PSIP, cumpliéndose con las siguientes condiciones:
>
> a) La voluntad haya sido manifestada de manera expresa, en los siguientes términos:
>
> i. En el caso de Persona Natural: por el respectivo titular, su representante legal o mandatario con poder específico para autorizar la transmisión y tratamiento de los datos o para autorizar la iniciación de pagos, según corresponda.
>
> ii. En el caso de Persona Jurídica: por él o los representantes legales o apoderados, autorizados ya sea para actuar conjunta o separadamente, en el caso de iniciación de pagos, o cualesquiera de los representantes legales o mandatarios con poder específico para autorizar la transmisión y tratamiento de los datos correspondientes.
>
> b) El PSBI y PSIP haya implementado el mecanismo de gestión del consentimiento en los términos y condiciones establecidas en la sección III.E.2 de esta normativa.
>
> c) La voluntad sea almacenada en un soporte duradero, que sea apto para resguardar su seguridad, integridad y acceso, respecto de la identidad del titular de los datos, así como de las circunstancias y condiciones en que fue solicitado y otorgado, de manera que pueda verificarse posteriormente que dicho consentimiento fue manifestado de manera libre, informada, expresa y específica en cuanto al tipo de información requerida, la finalidad y el periodo máximo de validez de esa autorización.
>
> d) La persona o sistema informático que interactúe con el titular de los datos o cliente no ejercerá ninguna influencia indebida sobre éste para inducirlo a manifestar su voluntad. Por ejemplo, el uso de interfaces que induzcan a los usuarios a tomar decisiones no intencionadas, involuntarias o potencialmente lesivas con respecto a sus datos personales; exigir que el consentimiento sea otorgado para la aplicación de un descuento u obtención de regalías; condicionarlo para la prestación del servicio a menos que sea inviable su prestación sin dicho consentimiento; o que las opciones empleadas para que éste se otorgue estén marcadas por defecto, estén con colores, tamaños o estilos de fuentes que las destaquen por sobre aquellas opciones que se refieran a no otorgar el consentimiento o respecto de aquellas establecidas para períodos más cortos.
>
> e) Al momento de solicitar el consentimiento para la transmisión, tratamiento o cesión de datos, o iniciación de pagos, se deberá poner en conocimiento del titular o cliente de manera precisa y clara los datos sobre los cuales consiente el intercambio, tratamiento, cesión a terceros o iniciación en el marco del SFA; a qué institución confiere la autorización para ello, o iniciar y cursar el o los pagos; por qué período o frecuencia; y para qué finalidad. Dicha solicitud no podrá contener otra información o requerir el consentimiento del titular o cliente para actos o fines distintos.
>
> f) Que los datos sobre los que versa el consentimiento y vigencia de éste sean los estrictamente necesarios para la finalidad respectiva, circunstancia que el PSBI o PSIP deberá acreditar cuando ello sea requerido por la Comisión en el marco de sus procesos de fiscalización, no correspondiendo a la IPI o IPC pronunciarse a ese respecto ni alterar el requerimiento original formulado por la PSBI o PSIP en el marco del SFA.
>
> g) Que la información que se pone en conocimiento del titular o cliente para obtener el consentimiento esté expresada en un lenguaje sencillo, claro, preciso y evitando tecnicismos, salvo en los casos en que resulte estrictamente necesario, debiendo explicarlos claramente. Además, deberá disponer de mecanismos que permitan a personas en situación de discapacidad acceder a esta información.
>
> h) Una vez que el titular o cliente haya otorgado el consentimiento se le deberá informar que, tanto el PSBI o PSIP como la IPI o IPC, pondrán a su disposición un panel de control y la forma en que podrá acceder al mismo, mediante el cual podrá conocer, verificar y revocar los consentimientos que haya otorgado.
>
> i) Que el titular de los datos o cliente se haya autenticado conforme a los estándares que para ello se establecen en la sección III.C de esta normativa.
>
> Queda prohibido a la IPI o a la IPC alterar el contenido de la solicitud de consentimiento formulada por la PSBI o PSIP en el marco del SFA, pedir un consentimiento adicional para el mismo intercambio, tratamiento o iniciación, adoptar medidas o prácticas que desincentiven el otorgamiento del consentimiento por los titulares o clientes, o que deterioren la experiencia usuaria de esos titulares o clientes. Al momento de adoptar o implementar nuevas tecnologías, las IPI o IPC deberán propender al uso de aquellas que mejoren la experiencia usuaria y minimicen el número de direccionamientos del usuario en el marco del SFA.
>
> Una vez otorgado el consentimiento, éste deberá ser comunicado y almacenado simultáneamente tanto por la PSBI o PSIP como por la IPI o IPC respectiva."

### Cross-references
- Ley 21.521 Art. 23 — the open-finance consent regime under Título III of Ley 21.521 that this subparagraph operationalizes.
- Ley 19.628 Art. 12 — the requirement that data-subject (titular) consent be free, informed, express, and specific for the processing of personal data, which conditions (a), (c), (e), and (g) operationalize in the open-finance context.
- NCG 514 §III.C — the authentication standards by which the data subject must be authenticated (condition i).
- NCG 514 §III.D.2 — the consent-management mechanism and control panel referenced in conditions (b) and (h).

> **TN:** The Spanish in (b) cites "la sección III.E.2"; this is an internal cross-reference error in the source — the consent-management mechanism is addressed in Section III.D.2 (this subsection), not III.E.2 (cost distribution). The Original Spanish reproduces "III.E.2" verbatim; the Cross-references point to the substantively correct §III.D.2.

> **Source:** NCG 514 §III.D.1 (03-jul-2024).

---

## III.D.2 — Management of Consent and Information Obligations
**NCG anchor:** N° 514, Sección III, D.2
**Implements:** Ley 21.521 Art. 23 (open-finance consent management) AND Ley 19.628 Art. 12 (data-subject control over consent)
**Tags:** open-finance, consent, control-panel, revocation, data-protection, titular

### Plain-English text

The PSBI, PSIP, IPI, and IPC must make available to the data subjects (titulares) and customers a control panel (panel de control) by means of which they may know, verify, and revoke the consents they have granted.

This control panel must comply with the following conditions and requirements, regardless of whether it is made available to the data subjects or customers directly by the institution or by third parties on its behalf:

a) They must be of free and remote access for the data subject or customer.

b) They must have an easy-to-use interface, that is, one that allows the data subject or customer to know and revoke the consents in a simple and intuitive manner. In addition, they must consider the mechanisms provided in numeral 1.g) above.

c) They must have authentication mechanisms equivalent to those required in Section III.C of this regulation.

d) The interface must allow the detail of each consent granted to be obtained, in a manner that that data subject or customer may inform themselves with respect to:

&nbsp;&nbsp;&nbsp;&nbsp;i. The institution to which they granted the consent to exchange, process, assign, or acquire their data, or to initiate and effect the payment. For which the commercial or fantasy name must be indicated, as well as the corporate name.

&nbsp;&nbsp;&nbsp;&nbsp;ii. The specific purpose for which such consent was granted.

&nbsp;&nbsp;&nbsp;&nbsp;iii. The type of information whose exchange, processing, or assignment was consented to.

&nbsp;&nbsp;&nbsp;&nbsp;iv. Date on which the consent was granted, including the time at which it was recorded, thus allowing the existence of multiple consents granted during a same day to be adequately identified.

&nbsp;&nbsp;&nbsp;&nbsp;v. Term, frequency, or period for which the consent was granted.

&nbsp;&nbsp;&nbsp;&nbsp;vi. Current state of the respective consent, that is, whether it is current, suspended, lapsed, or revoked.

&nbsp;&nbsp;&nbsp;&nbsp;vii. The identification of the legal representative(s) or proxies (mandatarios) who granted or revoked the consent for that person, where applicable.

e) Have a recording system or mechanism that allows preserving, in an integral manner and for at least 5 years, the accesses and interactions carried out by the data subjects, that is available to the Commission (CMF) for its supervision processes.

f) Allow the visualization of all the consents that have been granted, revoked, or lapsed during the last 5 years.

g) Have a system intended to prevent and avoid the continued carrying out of payment initiations, exchange, or processing of data once the consent has been revoked. For the foregoing, such system must have a real-time communication mechanism with the others implemented by the PSBI, PSIP, IPI, and IPC, in order to keep the states of the consents updated, in a manner that the customer may manage their consents indistinctly in the respective PSBI or IPI, PSIP or IPC.

In the event that the data subject (titular) or customer does not access the control panel enabled by the PSBI or PSIP for a period of more than one calendar year and there exist current consents, a communication must be sent to the place or medium that the data subject or customer has established for that purpose, in which they are reminded that such control panel exists, through which they may manage the consent(s) granted, as well as review the lapsed and revoked consents. Such communication must be remitted within the first five business days immediately subsequent to the completion of that year of inactivity.

### Original Spanish

> "2. Gestión del consentimiento y obligaciones de información
>
> Las PSBI, PSIP, IPI e IPC deberán poner a disposición de los titulares de datos y clientes un panel de control a través del cual puedan conocer, verificar y revocar los consentimientos que hayan otorgado.
>
> Este panel de control deberá cumplir las siguientes condiciones y requisitos, independiente de si es puesto a disposición de los titulares o clientes directamente por la institución o por terceros por cuenta de ésta:
>
> a) Deben ser de acceso gratuito y remoto para el titular o cliente.
>
> b) Deben contar con una interfaz fácil de utilizar, esto es, que permita al titular o cliente conocer y revocar los consentimientos de manera simple e intuitiva. Además, deberán considerar los mecanismos dispuestos en el numeral 1.g), anterior.
>
> c) Deben contar con mecanismos de autenticación equivalentes a los exigidos en la Sección III.C de esta normativa.
>
> d) La interfaz debe permitir obtener el detalle de cada consentimiento otorgado, de manera que ese titular o cliente pueda informarse respecto a:
>
> i. La institución a la que otorgó el consentimiento para intercambiar, tratar, ceder o adquirir sus datos, o iniciar y efectuar el pago. Para lo cual deberá indicarse el nombre comercial o de fantasía, así como razón social.
>
> ii. La finalidad específica para la cual se otorgó dicho consentimiento.
>
> iii. El tipo de información cuyo intercambio, tratamiento o cesión fue consentido.
>
> iv. Fecha en la que se otorgó el consentimiento, incluida la hora en que se registró el mismo, permitiendo así identificar adecuadamente la existencia de múltiples consentimientos otorgados durante un mismo día.
>
> v. Plazo, frecuencia o período para el que el consentimiento fue otorgado.
>
> vi. Estado actual del consentimiento respectivo, es decir, si está vigente, suspendido, caducado o revocado.
>
> vii. La identificación del o los representantes legales o mandatarios que otorgaron o revocaron el consentimiento por esa persona, en caso de que corresponda.
>
> e) Contar con un sistema o mecanismo de registro que permita preservar, de manera íntegra y por al menos 5 años, los accesos e interacciones efectuadas por los titulares, que esté a disposición de la Comisión para sus procesos de fiscalización.
>
> f) Permitir la visualización de todos los consentimientos que han sido otorgados, revocados o caducados durante los últimos 5 años.
>
> g) Contar con un sistema destinado a prevenir y evitar que se continue efectuando iniciaciones de pago, intercambio o tratamiento de datos una vez revocado el consentimiento. Para lo anterior, dicho sistema deberá contar con un mecanismo de comunicación en tiempo real con los demás implementados por las PSBI, PSIP, IPI e IPC para mantener actualizados los estados de los consentimientos, de manera que el cliente pueda gestionar sus consentimientos indistintamente en la PSBI o IPI, PSIP o IPC respectiva.
>
> En caso de que el titular de los datos o cliente no acceda al panel de control habilitado por la PSBI o PSIP por un periodo de más de un año calendario y existan consentimientos vigentes, se deberá enviar una comunicación al lugar o medio que el titular o cliente haya establecido para ese efecto en la que se le recuerde que existe dicho panel de control a través del cual puede gestionar el o los consentimientos otorgados, así como revisar los consentimientos caducados y revocados. Dicha comunicación se deberá remitir dentro de los cinco primeros días hábiles inmediatamente posteriores al cumplimiento de ese año de inactividad."

### Cross-references
- Ley 21.521 Art. 23 — the open-finance consent-management regime that this subparagraph develops.
- Ley 19.628 Art. 12 — the data subject's (titular) right to grant, know, and revoke consent over the processing of personal data, which the control panel operationalizes (free/remote access, revocation, and state visibility).
- NCG 514 §III.C — the authentication mechanisms that the control panel must equivalently require (condition c).
- NCG 514 §III.D.1 — the granting-of-consent conditions referenced (numeral 1.g) in condition b.

> **Source:** NCG 514 §III.D.2 (03-jul-2024).

---

## III.E — Other Standards
**NCG anchor:** N° 514, Sección III, E
**Implements:** Ley 21.521 Art. 21 (interoperability of the SFA) and Art. 25 (cost distribution)
**Tags:** open-finance, interoperability, cost-distribution, standards

### Plain-English text

This subsection governs other standards of the SFA: the interoperability (interoperabilidad) standards and the distribution of costs. It comprises subparagraphs E.1 (interoperability standards) and E.2 (cost distribution). The substantive rules begin at subparagraph E.1 below.

### Original Spanish

> "E. Otros Estándares"

### Cross-references
- Ley 21.521 Art. 21 — the interfaces/APIs whose interoperability subparagraph E.1 ensures.
- Ley 21.521 Art. 25 — the reimbursable-cost regime that subparagraph E.2 develops.
- NCG 514 §III.E.1–§III.E.2 — the subparagraphs that make up this subsection.

> **Source:** NCG 514 §III.E (03-jul-2024).

---

## III.E.1 — Interoperability Standards
**NCG anchor:** N° 514, Sección III, E.1
**Implements:** Ley 21.521 Art. 21 (interoperability and non-discrimination in the SFA)
**Tags:** open-finance, interoperability, non-discrimination, standards, access

### Plain-English text

Interoperability is constituted by the following principles:

a) For the operation of the SFA, the technical standards specified by this Commission (CMF) must be complied with.

b) The IPI or IPC may not give discriminatory treatment to the third-party data recipients. This means, for example, that they must not give priority to certain institutions over others at the moment of giving access to the extraction of information, in development times, access to the APIs, services of responses to queries, maximum response limits to equal requests, among others.

c) Every IPI or IPC, once it certifies the identity of the entities that provide services whether based on information or on payment initiation, must provide the respective services authorized to the information user according to their profiles, without need of agreement between the parties.

d) The conditions of service must be published so that all parties may access them.

e) Any additional technical criterion that is indispensable, and that is not contained in the standards, must ensure not to make impossible the access to a PSBI or PSIP.

### Original Spanish

> "1. Estándares de interoperabilidad
>
> La interoperabilidad queda constituida con los siguientes principios:
>
> a) Para el funcionamiento del SFA deberán cumplirse los estándares técnicos especificados por esta Comisión.
>
> b) Las IPI o IPC no pueden dar un trato discriminatorio a los terceros receptores de datos. Esto quiere decir, por ejemplo, que no deben dar prioridad a determinadas instituciones por sobre otras al momento de dar acceso a la extracción de información, en tiempos de desarrollo, acceso a las APIs, servicios de respuestas a consultas, límites máximos de respuestas ante solicitudes igualitarias, entre otros.
>
> c) Toda IPI o IPC, una vez que certifique la identidad de las entidades que proveen servicios ya sea basados en información o de iniciación de pagos, deberá brindar los servicios respectivos autorizados al usuario de información según sus perfiles, sin necesidad de acuerdo entre las partes.
>
> d) Se deben publicar las condiciones de servicio para que todas las partes puedan acceder a ellas.
>
> e) Cualquier criterio técnico adicional que sea indispensable, y que no esté contenido en los estándares, deberá velar por no imposibilitar el acceso a una PSBI o PSIP."

### Cross-references
- Ley 21.521 Art. 21 — the SFA interfaces/APIs whose interoperability and non-discriminatory access this subparagraph ensures.
- NCG 514 §II.A.2 — the technical standards of the APIs that underlie interoperability.
- NCG 514 §III.C.3 — the certification of participant identity referenced in item c.

> **Source:** NCG 514 §III.E.1 (03-jul-2024).

---

## III.E.2 — Cost Distribution
**NCG anchor:** N° 514, Sección III, E.2
**Implements:** Ley 21.521 Art. 25 (reimbursable incremental costs and thresholds in the SFA)
**Tags:** open-finance, cost-distribution, thresholds, reimbursement, payment-initiation

### Plain-English text

**General conditions (Condiciones generales).** The direct incremental costs that each IPI requests to be reimbursed must be fixed on the basis of public, objective, equitable, and non-discriminatory conditions, having to apply for their determination the objective parameters that the Commission (CMF) fixes. For the purpose of the charge, the IPI must make available on their websites, in a section especially designed for the purpose, an electronic document that contains and describes the referred conditions in their current version.

In the same manner, the IPI may not effect charges or make charges to the PSBI, except for the reimbursement of the direct incremental costs to attend to the volume of queries to their interfaces, once the volume thresholds of requests defined by the CMF (hereinafter the "Thresholds") are exceeded, in conformity with Article 25 of the Ley Fintec.

In the same manner, it must be borne in mind that, as provided in the sixth paragraph of Article 20 of the Ley Fintec, the execution of payment orders "shall not give rise to the charge of commissions or additional charges on the part of the [IPC] to the Customer holder thereof, with respect to what had already been agreed for the use of the respective account or means of payment or the carrying out of transfers charged to it. Nor may charges be effected on the part of the [IPC] to the [PSIP]."

**Determination of Thresholds (Determinación de Umbrales).** In application of what is provided in Article 20 of the Ley Fintec, the payment-initiation services are excluded from the determination of reimbursable costs.

For the case of information of: Terms and conditions; Service channels; Enrollment; Historical financial positions; Use and transaction history; and Information about current products; a Threshold of calls or queries shall be considered according to the set of information at a monthly level, per customer (as applicable) and per PSBI.

All of the foregoing, in accordance with what is described in summary form in the following table:

**Table N° 2: SFA Call Thresholds (Tabla N° 2: Umbrales de llamadas del SFA)**

| Set of Information (Conjunto de información) | Rule (Regla) |
|---|---|
| Terms and conditions (Términos y condiciones) | 120 monthly calls per PSBI. |
| Service channels (Canales de atención) | 120 monthly calls per PSBI. |
| Enrollment (Enrolamiento) | 4 monthly calls per customer and PSBI. |
| Historical financial positions (Posiciones financieras históricas) | 150 monthly calls per customer and PSBI. |
| Use and transaction history (Historia de uso y transacciones) | 150 monthly calls per customer and PSBI. |
| Current products (Productos vigentes) | 150 monthly calls per customer and PSBI. |

The indicated thresholds govern for the set of information, regardless of whether this set may contemplate more than one API for its query.

Those calls made within the framework of the functional tests addressed by this regulation shall not be computed for the exceeding of the threshold. In the same manner, the calls that do not obtain successful responses by responsibility of the respective IPI shall not be considered for the computation.

**On the parameters to consider in the determination of reimbursable costs (Sobre los parámetros a considerar en la determinación de costos reembolsables).** Those incremental costs that the IPI must effectively incur to attend to these queries, whether carried out directly by the institution or through the contracting of suppliers, shall be considered. In any event, as provided in the fourth paragraph of Article 25 of the Ley Fintec, "[t]he reimbursement of costs on the part of the participating institutions shall not be appropriate with respect to the development of the interface or information-exchange mechanism defined for the implementation of the SFA, in accordance with Article 21 [of the Ley Fintec]."

The detail of the incremental costs that may be considered shall be those available in Annex N° 4, "Technical Specifications for Cost Distribution," of this regulation.

**Minimum information to participants (Información mínima a participantes).** The charges shall apply once the conditions of these are published. Any modification in the tariff terms must be informed to the Participants with at least 30 days' anticipation of their entry into currency.

Monthly, each IPI must inform the PSBI of the effective consumption of their interfaces and the quantity of calls that have exceeded the charge threshold.

**Review of thresholds (Revisión de umbrales).** The CMF may review and modify the thresholds that are current. For this it may consider the information of the operation of the SFA, which may be required directly from the Participants.

**On the non-compliance of payment of the reimbursable costs (Sobre el incumplimiento del pago de los costos reembolsables).** In case of non-compliance of payment of the aforementioned reimbursable costs on the part of an Information-Based Service Provider (Proveedor de Servicios basados en Información), the Information-Providing Institution (Institución Proveedora de Información) must continue attending to the queries of information that do not exceed the aforementioned thresholds, except where there exist payment balances overdue for a term greater than sixty consecutive days.

### Original Spanish

> "2. Distribución de costos
>
> Condiciones generales
>
> Los costos incrementales directos que cada IPI solicite reembolsar, deberán fijarse sobre la base de condiciones públicas, objetivas, equitativas y no discriminatorias, debiendo aplicar para la determinación de estos los parámetros objetivos que fije la Comisión. Para efectos del cobro, las IPI deberán poner a disposición en sus sitios web, en una sección especialmente diseñada al efecto, un documento electrónico que contenga y describa las referidas condiciones en su versión vigente.
>
> De la misma forma, las IPI no podrán efectuar cobros o realizar cargos a los PSBI, salvo el reembolso de los costos incrementales directos para atender el volumen de consultas a sus interfaces, una vez superado los umbrales de volumen de solicitudes definido por la CMF (en adelante los “Umbrales”), de conformidad en el artículo 25 de la Ley Fintec.
>
> De igual manera, debe tenerse presente que según dispone el inciso sexto del artículo 20 de la Ley Fintec, la ejecución de órdenes de pago “no podrá dar lugar a cobro de comisiones o cobros adicionales por parte de la [IPC] al Cliente titular de ella, respecto a lo que ya hubiera convenido para el uso de la respectiva cuenta o medio de pago o la realización de transferencias con cargo a ésta. Tampoco se podrán efectuar cobros por parte de la [IPC] al [PSIP]”.
>
> Determinación de Umbrales
>
> En aplicación de lo dispuesto en el artículo 20 de la Ley Fintec, los servicios de iniciación de pagos quedan excluidos de la determinación de costos reembolsables.
>
> Para el caso de información de: Términos y condiciones; Canales de atención; Enrolamiento; Posiciones financieras históricas; Historial de uso y transacciones; e Información sobre productos vigentes; se considerará un Umbral de llamadas o consultas según conjunto de información a nivel mensual, por cliente (según resulte aplicable) y por PSBI.
>
> Todo lo anterior, conforme se describe de forma resumida en la siguiente tabla:
>
> Tabla N°2: Umbrales de llamadas del SFA
>
> CONJUNTO DE INFORMACIÓN REGLA
>
> Términos y condiciones 120 llamadas mensuales por PSBI.
>
> Canales de atención 120 llamadas mensuales por PSBI.
>
> Enrolamiento 4 llamadas mensuales por cliente y PSBI.
>
> Posiciones financieras históricas 150 llamadas mensuales por cliente y PSBI.
>
> Historia de uso y transacciones 150 llamadas mensuales por cliente y PSBI.
>
> Productos vigentes 150 llamadas mensuales por cliente y PSBI.
>
> Los umbrales señalados rigen para el conjunto de información, independiente que este conjunto pueda contemplar más de una API para su consulta.
>
> No se computarán para la superación del umbral aquellas llamadas realizadas en el marco de pruebas funcionales que trata esta Norma. De misma forma, no serán consideradas para el cómputo las llamadas que no obtengan respuestas exitosas por responsabilidad de la IPI respectiva.
>
> Sobre los parámetros a considerar en la determinación de costos reembolsables
>
> Se considerarán aquellos costos incrementales que efectivamente debe incurrir el IPI para atender estas consultas, ya sean efectuados directamente por la institución o por la contratación de proveedores. Con todo, conforme dispone el inciso cuarto del artículo 25 de la Ley Fintec, “[n]o procederá el reembolso de costos por parte de las instituciones participantes respecto del desarrollo de la interfaz o mecanismo de intercambio de información definido para la implementación del SFA, conforme al artículo 21 [de la Ley Fintec]”.
>
> El detalle de los costos incrementales que se podrán considerar serán los disponibles en el Anexo N°4, “Especificaciones técnicas para Distribución de Costos”, de esta normativa.
>
> Información mínima a participantes
>
> Los cobros aplicarán una vez que se encuentren publicadas las condiciones de éstos. Cualquier modificación en los términos tarifarios deberá ser informada a los Participantes con al menos 30 días de anticipación a su entrada en vigencia.
>
> Mensualmente, cada IPI deberá informar a los PSBI el consumo efectivo de sus interfaces y la cantidad de llamadas que han superado el umbral de cobro.
>
> Revisión de umbrales
>
> La CMF podrá revisar y modificar los umbrales que se encuentren vigentes. Para esto podrá considerar la información del funcionamiento del SFA, la cual podrá ser requerida directamente a los Participantes.
>
> Sobre el incumplimiento del pago de los costos reembolsables
>
> En caso de incumplimiento de pago de los costos reembolsables antes mencionados por parte de un Proveedor de Servicios basados en Información, la Institución Proveedora de Información deberá continuar atendiendo las consultas de información que no superen los umbrales antes referidos, salvo que existan saldos de pago vencidos por un plazo superior a sesenta días corridos."

### Cross-references
- Ley 21.521 Art. 25 — the reimbursable-cost regime and thresholds that this subparagraph develops.
- Ley 21.521 Art. 20 — the sixth paragraph excluding payment-initiation charges, quoted in the general conditions.
- Ley 21.521 Art. 21 — the interface/information-exchange-mechanism development excluded from reimbursement (fourth paragraph of Art. 25).
- NCG 514 Annex N° 4 — the technical specifications for cost distribution referenced.

> **TN:** Table N° 2 (CONJUNTO DE INFORMACIÓN / REGLA) is a two-column shaded table in the source PDF; the Original Spanish block reproduces the cell text in the PDF's extraction reading order, while the English Plain-English rendering presents it as a label–value table. Article references to the "Ley Fintec" are to Ley 21.521 (the Fintech Law); rendered as cited in the source.

> **Source:** NCG 514 §III.E.2 (03-jul-2024).

---

<!-- source: corpus/ncg/514-open-finance/seccion-04-informacion.md -->
## FILE: corpus/ncg/514-open-finance/seccion-04-informacion.md

# NCG 514 — Sección IV: System Information (Información del Sistema)

**Regulation:** NCG 514 (Sistema de Finanzas Abiertas), 03-jul-2024.
_law:_ NCG-514

## IV — System Information
**NCG anchor:** N° 514, Sección IV
**Implements:** Ley 21.521 Art. 24–26 (information shared through the Open Finance System)
**Tags:** open-finance, sfa, system-information, data-sharing

### Plain-English text

This section establishes the information of the Open Finance System (SFA) (Sistema de Finanzas Abiertas): the data to be shared in the SFA and their characteristics, the deadlines for the availability of the data sets, the variables to be shared, and the data protection applicable to the Customers' information. It comprises subsections A (data to be shared in the SFA), B (deadlines for the availability of the data sets), C (variables to be shared in the SFA), and D (data protection). The substantive rules begin at subsection A below.

### Original Spanish

> "SECCIÓN IV: INFORMACIÓN DEL SISTEMA"

### Cross-references
- Ley 21.521 Art. 24–26 — the information-sharing regime of the SFA that this section implements.
- NCG 514 §IV.A–§IV.D — the subsections that make up this section.

> **Source:** NCG 514 §IV (03-jul-2024).

---

## IV.A — Data to Be Shared in the SFA
**NCG anchor:** N° 514, Sección IV, A
**Implements:** Ley 21.521 Art. 24–26 (categories and characteristics of data shared through the SFA)
**Tags:** open-finance, data-to-be-shared, data-sets, taxonomies, ipi, psbi

### Plain-English text

The information to be shared in the SFA is that which is included in the following categories, with the characteristics that are indicated below in matters of delivery, updating, historical scope of the data, subjects obligated to provide the information in the system, and who may access it.

A detail of the taxonomies of variables and data to be supplied and shared is included in Annex N° 1. Annex N° 2 contains the codification that allows the distinct products to be reported in the system to be distinguished.

**Table N° 3: Types of data to be shared in the SFA (Tabla N° 3: Tipos de datos a compartir en el SFA)**

| Category (Categoría) | Set of information (Conjunto de información) | Detail of the information (Detalle de la información) |
|---|---|---|
| Terms, conditions, and service channels (Términos, condiciones y canales de atención) | Terms and conditions (Términos y condiciones) | General description: List of products that the company offers and their conditions. — Updating of the information: Weekly. — Time to make the information available in the SFA once the updating deadline has elapsed: Up to 5 minutes. — History of the datum: Not applicable. — Provide the information: IPI. — Access the information: PSBI. |
| | Service channels (Canales de atención) | General description: List of service locations, websites, and ATMs with their respective locations. — Updating of the information: Weekly. — Time to make the information available in the SFA once the updating deadline has elapsed: Up to 5 minutes. — History of the datum: Not applicable. — Provide the information: IPI. — Access the information: PSBI. |
| Identification and registration (Identificación y registro) | Enrollment (Enrolamiento) | General description: List of data and information that the customer provides at the moment of an enrollment. — Updating of the information: Daily. — Time to make the information available in the SFA once the updating deadline has elapsed: Up to 5 minutes. — Provide the information: IPI. — Access the information: PSBI. — Scope of the type of customer of which data are shared: Legal and natural persons. |
| Contracted Commercial Conditions and the Use or History of Transactions (Condiciones Comerciales Contratadas y el Uso o Historia de Transacciones) | Historical financial positions (Posiciones financieras históricas) | General description: Set of products that the customer has and their characteristics over time, both for financial assets and liabilities. — Updating of the information: Monthly. — Time to make the information available in the SFA once the updating deadline has elapsed: Up to 5 minutes. — Time unit of the information: Monthly (balance at month-end). — Historical period of the information: 12 months. — Provide the information: IPI according to applicability indicated in Annex N° 1. — Access the information: PSBI. — Scope of the type of customer of which data are shared: Legal and natural persons. |
| | Use and transaction history (Historia de uso y transacciones) | General description: Information that gives account of the use of the financial instruments and of access to these. — Updating of the information: Daily. — Time to make the information available in the SFA once the updating deadline has elapsed: Up to 5 minutes. — Time unit of the information: Not applicable. It is reported as a function of the date of use or contracting. — Historical period of the information: 12 months. — Provide the information: IPI according to applicability indicated in Annex N° 1. — Access the information: PSBI and PSIP. — Scope of the type of customer of which data are shared: Legal and natural persons. |
| | Current products (Productos vigentes) | General description: Online information of the customer current at the date of query. — Time to make the information available in the SFA: Up to 5 minutes. — Time unit of the information: Not applicable. — Historical depth of the information: Not applicable. — Provide the information: IPI according to applicability indicated in Annex N° 1. — Access the information: PSBI. — Scope of the type of customer of which data are shared: Legal and natural persons. |
| Payment initiation (Iniciación de pagos) | Payment initiation (Iniciación de pagos) | General description: Minimum information necessary for the carrying out of the execution of payment initiations. — Updating of the information: Real time. — Time unit of the information: Not applicable. — Historical depth of the information: Not applicable. — Participants in the exchange of information: IPC and PSIP. — Scope of the type of customer of which payments are made: Legal and natural persons. |

The data of the SFA must comply with the following conditions:

a) Be available at the moment of the customer's request.

b) Be always current and validated with respect to the situation of the customer according to the conditions determined in this regulation. In particular, they must reflect any change in the conditions, adjustments, rectifications that have been carried out or reported to the IPI and IPC.

c) Be available under the same conditions indicated above, both for the principal mechanism and for the alternative one.

For the case of information of online balances, all current products must be reported, independently of whether they present a zero balance at the moment of the query. Additionally, for this same set of information, in the case that the balances are calculated considering daily updates or with a greater periodicity, the date of the last available information must be reflected.

### Original Spanish

> "A. Datos para compartir en el SFA
>
> La información para compartir en el SFA es la que se incluye en las siguientes categorías, con las características que a continuación se señala en materia de entrega, actualización, alcance histórico de los datos, sujetos obligados a proveer la información en el sistema, y quienes pueden acceder a la misma.
>
> Un detalle de las taxonomías de variables y datos a ser suministrados y compartidos se incluye en el Anexo N°1. En el Anexo N°2 se encuentra la codificación que permite distinguir los distintos productos a informar en el sistema.
>
> Tabla N°3: Tipos de datos a compartir en el SFA
>
> CATEGORÍA CONJUNTO DE DETALLE DE LA INFORMACIÓN INFORMACIÓN Términos, Términos y • Descripción general: Listado de condiciones y condiciones productos que ofrece la compañía y canales de sus condiciones. atención • Actualización de la información: Semanal. • Tiempo para disponer la información en el SFA una vez cumplido el plazo de actualización: Hasta 5 minutos. • Historia del dato: No aplica. • Proveen la información: IPI. • Acceden a la información: PSBI. Canales de • Descripción general: Listado de los atención locales de atención, sitios web y ATM con sus respectivas ubicaciones. • Actualización de la información: Semanal. • Tiempo para disponer la información en el SFA una vez cumplido el plazo de actualización: Hasta 5 minutos. • Historia del dato: No aplica. • Proveen la información: IPI. • Acceden a la información: PSBI. Identificación y Enrolamiento • Descripción general: Listado de registro datos e información que provee el cliente al momento de un enrolamiento. • Actualización de la información: Diaria. • Tiempo para disponer la información en el SFA una vez cumplido el plazo de actualización: Hasta 5 minutos. • Proveen la información: IPI. • Acceden a la información: PSBI. • Alcance del tipo de cliente del cual se comparten datos: Personas jurídicas y naturales. Condiciones Posiciones • Descripción general: Set de Comerciales financieras productos que tiene el cliente y sus Contratadas y el históricas características en el tiempo, tanto Uso o Historia para activos y pasivos financieros. de • Actualización de la información: Transacciones Mensual. • Tiempo para disponer la información en el SFA una vez cumplido el plazo de actualización: Hasta 5 minutos. • Unidad de tiempo de la información: Mensual (saldo a fin de mes). • Periodo histórico de la información: 12 meses. • Proveen la información: IPI según aplicabilidad indicada en el Anexo N°1. • Acceden a la información: PSBI. • Alcance del tipo de cliente del cual se comparten datos: Personas jurídicas y naturales. Historia de uso • Descripción general: Información y transacciones que da cuenta del uso de los instrumentos financieros y del acceso a éstos. • Actualización de la información: Diaria. • Tiempo para disponer la información en el SFA una vez cumplido el plazo de actualización: Hasta 5 minutos. • Unidad de tiempo de la información: No aplica. Se reporta en función a la fecha del uso o contratación. • Periodo histórico de la información: 12 meses. • Proveen la información: IPI según aplicabilidad indicada en el Anexo N°1. • Acceden a la información: PSBI y PSIP. • Alcance del tipo de cliente del cual se comparten datos: Personas jurídicas y naturales. Productos • Descripción general: Información en vigentes línea del cliente vigente a la fecha de consulta. • Tiempo para disponer la información en el SFA: Hasta 5 minutos. • Unidad de tiempo de la información: No aplica. • Profundidad histórica de la información: No aplica. • Proveen la información: IPI según aplicabilidad indicada del Anexo N°1. • Acceden a la información: PSBI. • Alcance del tipo de cliente del cual se comparten datos: Personas jurídicas y naturales. Iniciación de Iniciación de • Descripción general: Información pagos pagos mínima necesaria para la realización de ejecución de iniciaciones de pagos. • Actualización de la información: Tiempo real. • Unidad de tiempo de la información: No aplica. • Profundidad histórica de la información: No aplica. • Participantes en el intercambio de información: IPC y PSIP. • Alcance del tipo de cliente del cual se realizan pagos: Personas jurídicas y naturales.
>
> Los datos del SFA deberán cumplir con las siguientes condiciones:
>
> a) Estar disponibles al momento de la solicitud del cliente.
>
> b) Estar siempre vigentes y validados respecto a la situación del cliente según las condiciones determinadas en la presente normativa. En particular, deberán reflejar cualquier cambio en las condiciones, ajustes, rectificaciones que se hayan realizado o informado al IPI e IPC.
>
> c) Estar disponibles en las mismas condiciones antes señaladas, tanto para el mecanismo principal como para el alternativo.
>
> Para el caso de información de saldos en línea, deben informarse todos los productos vigentes, independientemente si presentan saldo cero al momento de la consulta. Adicionalmente, para este mismo conjunto de información, en el caso de que los saldos se calculen considerando actualizaciones diarias o con una periodicidad mayor, debe reflejarse la fecha de la última información disponible."

### Cross-references
- Ley 21.521 Art. 24–26 — the information-sharing regime of the SFA whose categories and characteristics this subsection develops.
- NCG 514 §IV.B — the deadlines for the availability of the data sets identified in this table.
- NCG 514 §IV.C — the variables to be shared, detailed in Annex N° 1.
- NCG 514 Annex N° 1 — the taxonomies of variables and data to be supplied and shared.
- NCG 514 Annex N° 2 — the codification that distinguishes the distinct products reported in the system.

> **TN:** Table N° 3 (CATEGORÍA / CONJUNTO DE INFORMACIÓN / DETALLE DE LA INFORMACIÓN) is a three-column table whose third column is a bulleted list of label–value items in the source PDF, spanning PDF pages 60–63. The English Plain-English rendering presents it as a row-per-information-set table with the bulleted items joined by em-dash separators; the Original Spanish block reproduces the table cell text verbatim in the PDF's column-interleaved line-extraction order (category and set-of-information words appear intermixed with the wrapped bullet lines, exactly as pdfplumber reads the table). Where a category spans multiple information sets, the category cell appears once and is blank for continuation rows in the source.

> **Source:** NCG 514 §IV.A (03-jul-2024).

---

## IV.B — Deadlines for the Availability of the Data Sets
**NCG anchor:** N° 514, Sección IV, B
**Implements:** Ley 21.521 Art. 24–26 (availability deadlines of the data sets shared through the SFA)
**Tags:** open-finance, deadlines, availability, data-sets

### Plain-English text

The dates on which the sets of information identified in Table N° 3 must be current in the system are those indicated in Section V.C of this regulation.

### Original Spanish

> "B. Plazos para la disponibilidad de los conjuntos de datos
>
> Las fechas en que los conjuntos de información identificados en la Tabla N°3 deben estar vigentes en el sistema, son aquellas señaladas en la Sección V.C de esta Norma."

### Cross-references
- Ley 21.521 Art. 24–26 — the data-sharing regime whose availability deadlines this subsection addresses.
- NCG 514 §IV.A — Table N° 3, which identifies the sets of information whose availability dates are set here.
- NCG 514 §V.C — the gradual-implementation calendar that fixes the dates on which the data sets must be current.

> **Source:** NCG 514 §IV.B (03-jul-2024).

---

## IV.C — Variables to Be Shared in the SFA
**NCG anchor:** N° 514, Sección IV, C
**Implements:** Ley 21.521 Art. 24–26 (variables shared through the SFA)
**Tags:** open-finance, variables, data-sets, taxonomies

### Plain-English text

The complete detail of the variables to be shared in the SFA is found in Annex N° 1.

### Original Spanish

> "C. Variables para compartir en el SFA
>
> El detalle completo de las variables a compartir en el SFA se encuentra en el Anexo N°1."

### Cross-references
- Ley 21.521 Art. 24–26 — the data-sharing regime whose shared variables this subsection addresses.
- NCG 514 §IV.A — Table N° 3, the data categories whose variables are detailed in Annex N° 1.
- NCG 514 Annex N° 1 — the complete detail of the variables to be shared in the SFA.

> **Source:** NCG 514 §IV.C (03-jul-2024).

---

## IV.D — Data Protection
**NCG anchor:** N° 514, Sección IV, D
**Implements:** Ley 19.628 Art. 4 (lawful processing / consent), Art. 12 (data-subject rights), and Art. 16 (data communication to third parties) (data-subject rights, lawful processing, and transfer of the Customers' data) AND Ley 21.521 Título III (data protection in the Open Finance System)
**Tags:** open-finance, data-protection, data-subject-rights, lawful-basis, consent, ley-19628

### Plain-English text

The Participants of the SFA must, at all times, safeguard the integrity, availability, security, and confidentiality of the data involved in each transaction and the adequate protection of the information of the customers, in consideration of the provisions of this regulation and of the Ley N° 19.628 on the protection of personal data, in what may be applicable.

The data protection of the Customers in the system must consider the following elements, additional to those already considered in the rest of the regulation:

a) The data of the Customers available in the SFA may only be assigned or transmitted to third parties in conformity with one or more bases of lawfulness that may be applicable.

b) Among the entities, the information shall only be delivered through the interfaces of the SFA to those that have a current registration in the Directory of Participants, that have the roles associated with the request for information, and that comply with all the conditions established for accessing the requested information.

c) The IPI must abstain from communicating through the SFA data that exceed the maximum age indicated in this regulation.

d) The Participants must adopt adequate procedures to channel and manage the exercise of the rights of the data subjects (titulares de datos) with respect to data incorporated into the interfaces of the SFA.

e) The data authorized to be shared by the Customer may only be used by the PSBI and/or by the PSIP for the specific purposes indicated at the moment of granting their consent, without prejudice to the concurrence of another basis of lawfulness of processing.

f) The functioning and operation of the SFA shall be independent of the exercise by the data subjects of the rights that the applicable data-protection regulation confers on them, which shall conform to the conditions, scopes, and requirements that are defined therein.

### Original Spanish

> "D. Protección de datos
>
> Los Participantes del SFA deberán, en todo momento, resguardar la integridad, disponibilidad, seguridad y confidencialidad de los datos involucrados en cada transacción y la adecuada protección de la información de los clientes, en consideración a las disposiciones de la presente Norma y de la Ley N°19.628 de protección de datos personales, en lo que resulte aplicable.
>
> La protección de datos de los Clientes en el sistema deberá considerar los siguientes elementos, adicionales a los ya considerados en el resto de la normativa:
>
> a) Los datos de los Clientes disponibles en el SFA solo podrán cederse o transmitirse a terceros de conformidad con una o más bases de licitud que resulten aplicables.
>
> b) Entre las entidades solo se entregará la información a través de las interfaces del SFA a aquellos que tengan inscripción vigente en el Directorio de Participantes, que tengan los roles asociados a la solicitud de información y que cumplan con todas las condiciones establecidas para acceder a la información solicitada.
>
> c) Las IPI deben abstenerse de comunicar a través del SFA datos que excedan la antigüedad máxima indicada en la presente normativa.
>
> d) Los Participantes deberán adoptar procedimientos adecuados para canalizar y gestionar el ejercicio de los derechos de los titulares de datos respecto de datos incorporados a las interfaces del SFA.
>
> e) Los datos autorizados a compartir por el Cliente solo pueden ser utilizados por el PSBI y/o por el PSIP para los propósitos específicos señalados al momento de otorgar su consentimiento, sin perjuicio de la concurrencia de otra base de licitud de tratamiento.
>
> f) El funcionamiento y operatoria del SFA resultará independiente del ejercicio por parte de los titulares de datos de los derechos que les confiera la normativa de protección de datos aplicable, los que se ceñirán a las condiciones, alcances y requisitos que en aquella se definan."

### Cross-references
- Ley 21.521 Título III — the Open Finance System regime within which this data-protection obligation operates, which this subsection implements together with Ley 19.628.
- Ley 19.628 Art. 4 — the lawful-processing and consent rule that underlies the "bases of lawfulness" (bases de licitud) governing the assignment or transmission of customer data (items a and e).
- Ley 19.628 Art. 12 — the data-subject rights (derechos de los titulares) whose exercise the Participants must channel and manage (items d and f).
- Ley 19.628 Art. 16 — the rules on communication/disclosure of personal data to third parties operationalized by the delivery and abstention conditions (items b and c).
- NCG 514 §II — the Directory of Participants and the roles required to access information referenced in item b.
- NCG 514 §III.D — the consent regime under which the Customer authorizes the data to be shared (item e).
- NCG 514 §IV.A — the maximum age of the data that the IPI must not exceed when communicating (item c).

> **TN:** This subsection sits at a data-protection junction (dual-law): it operationalizes both Ley 21.521 Título III (the SFA) and Ley 19.628 (general personal-data protection). The source text cites only "la Ley N° 19.628 de protección de datos personales … en lo que resulte aplicable" by name; the specific Ley 19.628 articles named in the Implements line and cross-references (Art. 4 lawful processing/consent, Art. 12 data-subject rights, Art. 16 communication to third parties) are identified as the provisions that the listed elements (a–f) operationalize, not as express citations in the NCG text. "Bases de licitud" is rendered "bases of lawfulness."

> **Source:** NCG 514 §IV.D (03-jul-2024).

---

<!-- source: corpus/ncg/514-open-finance/seccion-05-otras-disposiciones.md -->
## FILE: corpus/ncg/514-open-finance/seccion-05-otras-disposiciones.md

# NCG 514 — Sección V: Other Provisions (Otras Disposiciones)

**Regulation:** NCG 514 (Sistema de Finanzas Abiertas), 03-jul-2024.
_law:_ NCG-514

## V — Other Provisions
**NCG anchor:** N° 514, Sección V
**Implements:** Ley 21.521 Título III (Open Finance System) and transitory articles (the supervisory, sanction, phase-in, and entry-into-force provisions of the SFA)
**Tags:** open-finance, sfa, other-provisions, suspensions, sanctions, implementation-deadlines, entry-into-force

### Plain-English text

This section establishes the other provisions applicable to the Open Finance System (SFA) (Sistema de Finanzas Abiertas): the temporary suspensions of the participation of entities, the sanctions, the implementation deadlines of the system, the information requirements, and the entry into force of the regulation. It comprises subsections A (temporary suspensions), B (sanctions), C (implementation deadlines of the system), D (information requirements), and E (entry into force). The substantive rules begin at subsection A below.

### Original Spanish

> "SECCIÓN V: OTRAS DISPOSICIONES"

### Cross-references
- Ley 21.521 Título III — the Open Finance System regime within which these other provisions operate.
- NCG 514 §V.A–§V.E — the subsections that make up this section.

> **Source:** NCG 514 §V (03-jul-2024).

---

## V.A — Temporary Suspensions
**NCG anchor:** N° 514, Sección V, A
**Implements:** Ley 21.521 Art. 27 (penúltimo inciso) (the CMF power to temporarily suspend, partially or totally, the participation of entities or their interfaces)
**Tags:** open-finance, temporary-suspensions, cybersecurity, operational-risk, cmf-supervision

### Plain-English text

The Commission (CMF), in conformity with the good functioning of the System, and as provided in the penultimate paragraph of Article 27 of the Ley Fintec, may temporarily suspend, in a partial or total manner, the participation of the entities or their interfaces when any of the following circumstances are verified:

a) Entities that show deficiencies in the quality of the information that they supply through their interfaces.

b) Entities that suffer some type of cybersecurity incident that affects or compromises the information assets associated with the SFA or involves a breach of the personal data of the financial customers.

c) Entities that have suffered some operational incident that prevents them from the transfer and/or exchange of data in a secure manner or that affects the correct functioning of the System.

d) Entities that present deficiencies in their management of operational or cybersecurity risks.

e) Entities that present other inconveniences or evidence problems that may generate a negative effect on the System.

In line with the foregoing, the Participants of the SFA, under no circumstance, may affect the information assets associated with the SFA, among them, the personal data of the financial customers. Therefore, in the event that a Participant of the SFA considers that there exists a relevant risk of affectation of such assets that requires urgent actions, it must take immediate preventive measures, such as the disconnection of its systems from the SFA or the denial of requests at its interfaces and systems. Together with the foregoing, it must immediately send a report to the CMF informing of the measures adopted with the pertinent explanatory grounds, as well as adopt as soon as possible the corrective actions to resolve the situation that motivated it.

Once the situation that motivated the measures is resolved, the Participant of the SFA must immediately leave without effect the measures adopted and inform the CMF of this situation.

With respect to the preventive measures adopted and their corrective actions, the Participant must keep at the disposal of the Commission all the antecedents that found such decisions, in order that the Commission may evaluate their pertinence, opportuneness, and suitability and, if appropriate, exercise the necessary actions according to its legal powers.

### Original Spanish

> "A. Suspensiones temporales
>
> La Comisión, en conformidad con el buen funcionamiento del Sistema, y lo dispuesto en el inciso penúltimo del artículo 27 de la Ley Fintec, podrá suspender temporalmente, de forma parcial o total, la participación de las entidades o sus interfaces cuando se verifiquen alguna de las siguientes circunstancias:
>
> a) Entidades que muestren deficiencias en la calidad de la información que suministren a través de sus interfaces.
>
> b) Entidades que sufren algún tipo de incidente de ciberseguridad que afecte o comprometa los activos de información asociados al SFA o involucre una vulneración de los datos personales de los clientes financieros.
>
> c) Entidades que hayan sufrido algún incidente operacional que les impida la transferencia y/o intercambio de datos en forma segura o que afecte el correcto funcionamiento del Sistema.
>
> d) Entidades que presenten deficiencias en su gestión de riesgos operacionales o de ciberseguridad.
>
> e) Entidades que presenten otros inconvenientes o evidencien problemas que puedan generar un efecto negativo sobre el Sistema.
>
> En línea con lo anterior, los Participantes del SFA, bajo ninguna circunstancia, deben afectar los activos de información asociados al SFA, entre ellos, los datos personales de los clientes financieros. Por lo anterior, en caso de que un Participante del SFA estime que existe un riesgo relevante de afectación de tales activos que requiera acciones urgentes, deberá tomar medidas preventivas inmediatas, tales como la desconexión de sus sistemas del SFA o la denegación de solicitudes en sus interfaces y sistemas. Junto con lo anterior, deberá enviar de inmediato un reporte a la CMF informando las medidas adoptadas con los fundamentos explicativos pertinentes, así como adoptar a la brevedad las acciones correctivas para solucionar la situación que la motivó.
>
> Una vez solucionada la situación que motivó las medidas, el Participante del SFA deberá de inmediato dejar sin efecto las medidas adoptadas e informar a la CMF esta situación.
>
> Respecto a las medidas preventivas adoptadas y sus acciones correctivas, el Participante deberá mantener a disposición de la Comisión todos los antecedentes que fundamenten tales decisiones, a fin de que la Comisión pueda evaluar su pertinencia, oportunidad e idoneidad y, si corresponde, ejercer las acciones necesarias según sus facultades legales."

### Cross-references
- Ley 21.521 Art. 27 — the penultimate paragraph that empowers the Commission (CMF) to temporarily suspend the participation of entities or their interfaces.
- NCG 514 §V.B — the sanctions regime that applies in addition to the temporary suspensions established here.
- NCG 514 §IV.D — the data-protection obligations whose breach (item b) may give rise to a suspension.

> **Source:** NCG 514 §V.A (03-jul-2024).

---

## V.B — Sanctions
**NCG anchor:** N° 514, Sección V, B
**Implements:** Ley 21.521 Art. 27 (sanction of SFA Participants that infringe the law or this regulation) AND DL N° 3.538 de 1980 Título III (the rules under which the Commission imposes sanctions)
**Tags:** open-finance, sanctions, cmf-supervision, registration-cancellation, dl-3538

### Plain-English text

In conformity with Article 27 of the Ley Fintec, the Participants of the SFA that incur in infractions of the provisions of said law or fail to comply with the instructions of the present regulation, shall be sanctioned in conformity with the rules established in Title III of DL N° 3.538, of 1980, without prejudice to sanctions contained in other legal bodies.

The Commission (CMF), in conformity with its powers, may sanction with a definitive suspension or cancellation of registration, without prejudice to determining the temporary suspension while antecedents are gathered, as part of a sanctioning process.

### Original Spanish

> "B. Sanciones
>
> De conformidad con el artículo 27 de la Ley Fintec, los Participantes del SFA que incurrieren en infracciones a las disposiciones de dicha ley o incumplieren las instrucciones de la presente normativa, serán sancionados conforme a las reglas establecidas en el Título III del DL N°3.538, de 1980, sin perjuicio de sanciones contenidas en otros cuerpos legales.
>
> La Comisión, conforme a sus facultades, podrá sancionar con una suspensión definitiva o cancelación de registro, sin perjuicio de determinar la suspensión temporal mientras se recaban antecedentes, como parte de un proceso sancionatorio."

### Cross-references
- Ley 21.521 Art. 27 — the article under which SFA Participants that infringe the law or this regulation are sanctioned.
- DL N° 3.538 de 1980 Título III — the sanctioning rules of the Commission (CMF) applied to SFA Participants.
- NCG 514 §V.A — the temporary suspensions that the Commission may also determine while antecedents are gathered.

> **Source:** NCG 514 §V.B (03-jul-2024).

---

## V.C — Implementation Deadlines of the System
**NCG anchor:** N° 514, Sección V, C
**Implements:** Ley 21.521 (transitory articles on the phase-in of the Open Finance System) and Art. 18 (entities obligated to participate in the SFA)
**Tags:** open-finance, implementation-deadlines, phase-in, gradualidad, apis, milestones

### Plain-English text

The SFA shall have a period of implementation in two stages. The first of them, which shall last 24 months, considers the technological preparation and development of the tasks proper to the participants and to the Commission. This period of 24 months begins with the publication of the present regulation. Once said period is concluded, the present regulation shall enter into force.

The milestones of the gradual implementation (phase-in) (implementación gradual), once this regulation is in force, consider the following deadlines for compliance with the availability of the information APIs within the framework established by the Ley Fintec:

- The banks, the issuers of credit cards, and the issuers of payment cards with provision of funds, must comply with the following deadlines:

a) 6 months for implementation of APIs on General Terms and Conditions and on Service Channels.

b) 15 months for implementation of APIs on Enrollment, Historical Financial Positions, Use and transaction history, and Current products; all the foregoing referring to natural-person customers, excepting the information on lines of credit associated with current accounts, sight accounts, and credit cards, which must be available at 18 months of entry into force of this regulation.

c) 18 months for implementation of APIs on Enrollment, Historical Financial Positions, Use and transaction history, and Current products; all the foregoing referring to legal-person customers.

d) 18 months for implementation of APIs on Payment Initiation.

- For the entities indicated in the second paragraph, subparagraphs (a) to (h) of Article 18 of the Ley Fintec, the corresponding deadlines for them to have their APIs available shall be:

a) 24 months for implementation of APIs on General Terms and Conditions and Service Channels.

b) 36 months for implementation of APIs on Enrollment, Historical Financial Positions, Use and transaction history, and Current products, of every type of customer.

The Commission (CMF) shall consider that the deadlines have been complied with when, at the stipulated dates, the IPI and IPC:

a) Have developed the APIs in accordance with the calendar of implementation previously indicated, and the respective alternative mechanism indicated in the Regulation.

b) Have provided the pertinent documentation to the Directory of Participants.

c) Have carried out the respective functional tests.

d) Have the effective information of the customers associated with each API (not only test information) already available in the System.

In the case of entities indicated in the second paragraph, subparagraphs (a) to (h) of Article 18 of the Ley Fintec, that directly issue payment cards or open sight accounts, the deadline of 18 months for payment initiation shall apply.

### Original Spanish

> "C. Plazos de implementación del sistema
>
> El SFA tendrá un periodo de implementación en dos etapas. La primera de ella, que durará 24 meses, considera la preparación tecnológica y desarrollo de las tareas propias que corresponden a los participantes y a la Comisión. Este periodo de 24 meses comienza con la publicación de la presente normativa. Una vez terminado dicho periodo, la presente norma entrará en vigencia.
>
> Los hitos de la implementación gradual, una vez vigente esta normativa, consideran los siguientes plazos de cumplimiento de disponibilidad de las APIs de información dentro del marco establecido por la Ley Fintec:
>
> • Los bancos, los emisores de tarjetas de crédito y los emisores de tarjetas de pago con provisión de fondos, deberán cumplir con los siguientes plazos:
>
> a) 6 meses para implementación de APIs sobre Términos y Condiciones Generales y de Canales de Atención.
>
> b) 15 meses para implementación de APIs sobre Enrolamiento, Posiciones Financieras Históricas, Historial de usos y transacciones, y Productos vigentes; todo lo anterior referido a clientes personas naturales, exceptuando la información sobre líneas de crédito asociadas a cuentas corriente, cuentas vista y tarjetas de crédito, que deberán estar disponibles a los 18 meses de entrada en vigencia de esta norma.
>
> c) 18 meses para implementación de APIs sobre Enrolamiento, Posiciones Financieras Históricas, Historial de usos y transacciones, y Productos vigentes; todo lo anterior referido a clientes personas jurídicas.
>
> d) 18 meses para implementación de APIs sobre Iniciación de Pagos.
>
> • Para las entidades indicadas en el inciso segundo, letras (a) a la (h) del artículo 18 de la Ley Fintec, los plazos correspondientes para que deban tener disponibles sus APIs serán:
>
> a) 24 meses para implementación de APIs sobre Términos y Condiciones Generales y Canales de Atención.
>
> b) 36 meses para implementación de APIs sobre Enrolamiento, Posiciones Financieras Históricas, Historial de usos y transacciones, y Productos vigentes, de todo tipo de clientes.
>
> La Comisión considerará que se ha cumplido con los plazos cuando, a las fechas estipuladas, las IPI e IPC:
>
> a) Hayan desarrollado las APIs de acuerdo al calendario de implementación antes indicado, y el respectivo mecanismo alternativo indicado en la Norma.
>
> b) Hayan proporcionado la documentación pertinente al Directorio de Participantes.
>
> c) Hayan realizado las respectivas pruebas funcionales.
>
> d) Tengan la información efectiva de las clientes asociadas a cada API (no solo información de pruebas) ya disponible en el Sistema.
>
> En el caso de entidades indicadas en el inciso segundo, letras (a) a la (h) del artículo 18 de la Ley Fintec, que emitan directamente tarjetas de pago o aperturen cuentas vistas, aplicará el plazo de 18 meses para iniciación de pagos."

### Cross-references
- Ley 21.521 Art. 18 — the entities obligated to participate in the SFA whose phase-in deadlines this subsection fixes (second paragraph, subparagraphs (a) to (h)).
- NCG 514 §IV.A — Table N° 3, the data sets (Terms and Conditions, Enrollment, Historical Financial Positions, Use and transaction history, Current products, Payment initiation) whose API availability is scheduled here.
- NCG 514 §IV.B — the availability deadlines of the data sets, which refer to this calendar.
- NCG 514 §V.E — the entry into force at 24 months that conditions the start of the gradual-implementation milestones.

> **Source:** NCG 514 §V.C (03-jul-2024).

---

## V.D — Information Requirements
**NCG anchor:** N° 514, Sección V, D
**Implements:** Ley 21.521 Art. 26 (information shared with the Commission) AND DL N° 3.538 de 1980 (the CMF power to require information for supervision purposes)
**Tags:** open-finance, information-requirements, cmf-supervision, reporting

### Plain-English text

The detail and the format of the information required in this regulation that must be sent to the Commission (CMF) for purposes of supervision, shall be specified in one or more regulations that shall be issued subsequent to the publication of this NCG.

### Original Spanish

> "D. Requerimientos de información
>
> El detalle y el formato de la información requerida en esta normativa que debe ser enviada a la Comisión para efectos de supervisión, será especificado en una o más normas que se dictarán en forma posterior a la publicación de esta NCG."

### Cross-references
- Ley 21.521 Art. 26 — the information-sharing regime under which information is sent to the Commission (CMF).
- DL N° 3.538 de 1980 — the supervisory powers of the Commission (CMF) under which information may be required.
- NCG 514 §V.B — the sanctions regime that backs the supervision for which this information is required.

> **Source:** NCG 514 §V.D (03-jul-2024).

---

## V.E — Entry into Force
**NCG anchor:** N° 514, Sección V, E
**Implements:** Ley 21.521 (transitory articles on the entry into force of the Open Finance System)
**Tags:** open-finance, entry-into-force, vigencia, transitory

### Plain-English text

The provisions incorporated in this Regulation shall enter into force 24 months counted from its issuance.

### Original Spanish

> "E. Entrada en vigencia
>
> Las disposiciones incorporadas en esta Norma entrarán en vigencia 24 meses contados desde su dictación."

### Cross-references
- Ley 21.521 — the Open Finance System regime whose transitory entry-into-force scheme this subsection gives effect to.
- NCG 514 §V.C — the 24-month implementation period whose conclusion coincides with this entry into force.

> **Source:** NCG 514 §V.E (03-jul-2024).

---

<!-- source: corpus/ncg/514-open-finance/seccion-06-anexos.md -->
## FILE: corpus/ncg/514-open-finance/seccion-06-anexos.md

# NCG 514 — Sección VI: Normative Annexes (Anexos Normativos)

**Regulation:** NCG 514 (Sistema de Finanzas Abiertas), 03-jul-2024.
_law:_ NCG-514

## VI — Normative Annexes
**NCG anchor:** N° 514, Sección VI
**Implements:** Ley 21.521 Art. 24–26 (data shared through the Open Finance System) AND Ley 21.521 Art. 20 (payment initiation)
**Tags:** open-finance, sfa, annexes, data-sets, variables, taxonomies

### Plain-English text

This section contains the normative annexes of the regulation. Annex N° 1 (Variables for the information sets of the SFA / Variables para conjuntos de información del SFA) details, set by set, the variables and fields that the Information-Providing Institutions (IPI) must provide and that are shared in the Open Finance System (SFA): (1) Terms and conditions, (2) Service channels and ATM, (3) Enrollment, (4) Historical financial positions, (5) Transactional information, (6) Active products, and (7) Payment initiation. Annex N° 2 (Products of the SFA / Productos del SFA) contains the codification that distinguishes the distinct financial products reported in the system. Annex N° 3 (Technical Annex / Anexo Técnico) and Annex N° 4 (Technical specifications for the distribution of costs / Especificaciones técnicas para la distribución de costos) are reserved as "to be defined" (por definir).

### Original Spanish

> "SECCIÓN VI. ANEXOS NORMATIVOS
>
> Anexo N°1: Variables para conjuntos de información del SFA"

### Cross-references
- Ley 21.521 Art. 24–26 — the data-sharing regime of the SFA whose taxonomies of variables these annexes detail.
- NCG 514 §IV.A — Table N° 3, which references Annex N° 1 (variable taxonomies) and Annex N° 2 (product codification).
- NCG 514 §VI.1–§VI.7 — the seven data-set specifications that make up Annex N° 1.
- NCG 514 §VI.A2–§VI.A4 — the standalone Annexes N° 2, N° 3, and N° 4.

> **Source:** NCG 514 §VI (03-jul-2024).

---

## VI.1 — Annex N° 1 (1): Terms and Conditions
**NCG anchor:** N° 514, Sección VI, Anexo N°1, 1
**Implements:** Ley 21.521 Art. 24–26 (terms-and-conditions data set shared through the SFA)
**Tags:** open-finance, data-set, terms-and-conditions, variables, ipi

### Plain-English text

Data set "Terms and conditions" (Términos y condiciones). For each variable, the table gives its detail and indicates that the IPI that must provide the information is "All" (Todos).

| Variable (Variable) | Detail (Detalle) |
|---|---|
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Periodicity of the maintenance costs (Temporalidad de los costos de mantención) | Indicate whether it is monthly, quarterly, semiannual, or annual. If the product has no maintenance costs, indicate "NA". |
| Maintenance costs (Costos de mantención) | Amount of the maintenance, expressed in pesos if nominal. If it is in terms of a percentage over some base, indicate percentage. If the product has no maintenance costs indicate "NA". |
| Base of maintenance costs (Base costos de mantención) | If the maintenance cost is a percentage, indicate here the base over which that percentage is applied. |
| Commissions (Comisiones) | Amount of commissions for use, withdrawals, among others. Expressed in pesos if nominal. If it is in terms of a percentage over some base, indicate percentage. If the product has no commissions indicate "NA". |
| Base of commissions (Base comisiones) | If the commissions are a percentage, indicate here the base over which that percentage is applied. |
| Currency (Moneda) | Currency in which the product is expressed according to table 1 of the Information System Manual (MSI). For example, if it is a checking account in dollars that is being reported, then it must report "dollar" according to the codes of table 1 of the MSI. |
| Terms of duration (Términos de duración) | Term of validity of the product expressed in days. If not applicable (the product does not require renewal or does not expire) indicate "NA". |
| Associated benefits (Beneficios asociados) | Benefits associated with obtaining the product. Text type. |
| Eligibility criteria (Criterios de elegibilidad) | Minimum standards for obtaining the product: customer's age, minimum income, etc. Indicate at least for all the minimum variables for obtaining the product. Text type. |
| Type of customer (Tipo de cliente) | Indicate whether the product may be opened by a natural person, a legal person, or both. |
| Minimum opening standards (Estándares mínimos de apertura) | Minimum standards for the opening of the product (for example: minimum amount to deposit when opening the account, minimum investment amount, etc.). Text type. |

> **TN:** "IPI que debe proveer la información: Todos" ("IPI that must provide the information: All") applies to the whole table. The Spanish block transcribes the table verbatim in the PDF's column-interleaved line-extraction order (pdfplumber reads the wrapped variable-name column and the wrapped detail column line by line), so variable names appear intermixed with their detail text exactly as the source PDF extracts.

### Original Spanish

> "1. Términos y condiciones
> VARIABLES DETALLE IPI QUE DEBE
> PROVEER LA
> INFORMACIÓN:
> Tipo de Indique el código respectivo de la tabla de productos del SFA Todos
> producto
> financiero
> Categoría Indique si aplica alguna categoría comercial asociada al producto.
> comercial Tipo texto
> Temporalidad Indique si es mensual, trimestral, semestral o anual. Si el producto
> de los costos de no tiene costos de mantención, indique "NA"
> mantención
> Costos de Monto de la mantención, expresado en pesos si es nominal. Si es en
> mantención términos de porcentaje sobre alguna base, indique porcentaje. Si el
> producto no tiene costos de mantención indique "NA"
> Base costos de Si el costo de mantención es un porcentaje, indique aquí la base
> mantención sobre la cual se aplica ese porcentaje
> Comisiones Monto de comisiones por uso, retiros, entre otros. Expresado en
> pesos si es nominal. Si es en términos de porcentaje sobre alguna
> base, indique porcentaje. Si el producto no tiene comisiones indique
> "NA"
> Base Si las comisiones son en porcentaje, indique aquí la base sobre la
> comisiones cual se aplica ese porcentaje
> Moneda Moneda en que está expresado el producto según tabla 1 del Manual
> Sistema de Información (MSI). Por ejemplo, si es una cuenta
> corriente en dólares la que está informando, entonces deberá
> informar “dólar” según los códigos de la tabla 1 del MSI
> Términos de Plazo de vigencia del producto expresado en días. Si no aplica (el
> duración producto no requiere renovación o no vence) indique "NA"
> Beneficios Beneficios asociados a la obtención del producto. Tipo texto
> asociados
> Criterios de Estándares mínimos para la obtención del producto: edad del cliente,
> elegibilidad ingresos mínimos, etc. Indique al menos para todas las variables
> mínimas para la obtención del producto. Tipo texto
> Tipo de cliente Indique si el producto puede ser aperturado por persona natural,
> persona jurídica o ambos
> Estándares Estándares mínimos para la apertura del producto (por ejemplo:
> mínimos de monto mínimo a depositar al abrir la cuenta, monto mínimo de
> apertura inversión, etc.). Tipo texto"

### Cross-references
- Ley 21.521 Art. 24–26 — the data-sharing regime whose "terms and conditions" set this annex details.
- NCG 514 §IV.A — Table N° 3, which lists "Terms and conditions" among the sets of information to be shared.
- NCG 514 §VI.A2 — Annex N° 2, the table of products of the SFA referenced by "Type of financial product".

> **Source:** NCG 514 §VI Annex N° 1 (1) (03-jul-2024).

---

## VI.2 — Annex N° 1 (2): Service Channels and ATM
**NCG anchor:** N° 514, Sección VI, Anexo N°1, 2
**Implements:** Ley 21.521 Art. 24–26 (service-channels data set shared through the SFA)
**Tags:** open-finance, data-set, service-channels, atm, variables, ipi

### Plain-English text

Data set "Service channels and ATM" (Canales de atención y ATM). The table is organized by type of information (service channels; ATM) and information subcategory (in-person, web pages and app, telephone, text messages, e-mail, social networks). For service channels the IPI that must provide the information is "All" (Todos); for ATM it is "Banks" (Bancos).

**Service channels (Canales de atención):**

| Subcategory (Subcategoría) | Variable (Variable) | Detail (Detalle) |
|---|---|---|
| In-person (Presenciales) | Type (Tipo) | Identifies the type of in-person service channel (example: Head Office, Branch, Auxiliary Cashier, banking Correspondent, Support Office, Branch abroad, Representation Office abroad, Placement Agent, among others). |
| | Address (Dirección) | Street and number. |
| | City (Ciudad) | City name. |
| | Commune (Comuna) | Commune name. |
| | Region (Región) | Region name. |
| | Type of schedule (Tipo de horario) | Indicate whether the service schedule is continuous or split. |
| | Opening time (Hora de apertura) | Opening time of the office. Generate an opening time for each continuous-schedule block. |
| | Closing time (Hora de cierre) | Closing time of the office. Generate a closing time for each continuous-schedule block. |
| | Service schedule (Horario de atención) | Aggregated daily opening and closing schedule. |
| | Available services (Servicios disponibles) | Indicate the services to which customers may have access in the indicated service channel (example: opening of products, closing of products, advisory to customers, etc.). |
| Web pages and app (Páginas web y app) | Type (Tipo) | Website or app. |
| | Website (Sitio web) | Link of the website. |
| | Service schedule (Horario de atención) | Schedule within which the services may be performed. |
| | Available services (Servicios disponibles) | Indicate the services to which customers may have access in the indicated service channel (example: opening of products, closing of products, advisory to customers, etc.). |
| Telephone (Telefónico) | Available services (Servicios disponibles) | Indicate the services to which customers may have access in the indicated service channel (example: opening of products, closing of products, advisory to customers, etc.). |
| | Telephone (Teléfono) | Indicate the telephone associated with each service previously mentioned. |
| | Service schedule (Horario de atención) | Indicate the schedule within which the service previously mentioned is feasible to access through the telephone channel. |
| Text messages (Mensajes de texto) | Available services (Servicios disponibles) | Indicate the services to which customers may have access in the indicated service channel (example: opening of products, closing of products, advisory to customers, etc.). |
| | Number (Número) | Indicate the number associated with each service previously mentioned. |
| | Service schedule (Horario de atención) | Schedule within which the services may be performed. |
| E-mail (Correo electrónico) | Available services (Servicios disponibles) | Indicate the services to which customers may have access in the indicated service channel (example: opening of products, closing of products, advisory to customers, etc.). |
| | Mailbox (Casilla) | Indicate the associated e-mail. |
| | Service schedule (Horario de atención) | Schedule within which the services may be performed. |
| Social networks (Redes sociales) | Available services (Servicios disponibles) | Indicate the services to which customers may have access in the indicated service channel (example: opening of products, closing of products, advisory to customers, etc.). |
| | Social network (Red social) | Indicate the associated social network and the account. |
| | Service schedule (Horario de atención) | Schedule within which the services may be performed. |

**ATM (ATM):** IPI: Banks (Bancos).

| Variable (Variable) | Detail (Detalle) |
|---|---|
| Address (Dirección) | Street and number. |
| City (Ciudad) | City name. |
| Commune (Comuna) | Commune name. |
| Region (Región) | Region name. |
| Type of schedule (Tipo de horario) | Indicate whether it is a continuous or split schedule. |
| Opening time (Hora de apertura) | Opening time of the office. Generate an opening time for each continuous-schedule block. |
| Closing time (Hora de cierre) | Closing time of the office. Generate a closing time for each continuous-schedule block. |
| Service schedule (Horario de atención) | Aggregated daily opening and closing schedule. |
| Type of service (Tipo de servicio) | Indicate whether at the ATM one may make withdrawals, deposits, among others. |

> **TN:** This data-set table spans PDF pages 69–70. The Spanish block transcribes both pages verbatim in pdfplumber's column-interleaved line-extraction order (type-of-information, subcategory, variable, and detail columns read line by line, so the wrapped cell text appears intermixed). The "IPI QUE DEBE PROVEER LA INFORMACIÓN" column value is "Todos" for the service-channels block and "Bancos" for the ATM block.

### Original Spanish

> "2. Canales de atención y ATM
> TIPO DE SUBCATEGORÍA VARIABLES DETALLE IPI QUE DEBE
> INFORMACIÓN DE PROVEER LA
> INFORMACIÓN INFORMACIÓN:
> Canales de Presenciales Tipo Identifica el tipo de canal de Todos
> atención atención presencial (ejemplo: Casa
> Matriz, Sucursal, Caja Auxiliar,
> Corresponsalía bancaria, Oficina
> de apoyo, Sucursal en el exterior,
> Oficina de representación en el
> exterior, Agente Colocador, entre
> otros)
> Dirección Calle y número
> Ciudad Nombre ciudad
> Comuna Nombre comuna
> Región Nombre región
> Tipo de Indicar si horario de atención es
> horario continuo o discontinuo
> Hora de Hora de apertura de la oficina.
> apertura Generar hora de apertura por cada
> bloque de horario continuo
> Hora de Hora de cierre de la oficina.
> cierre Generar hora de cierre por cada
> bloque de horario continuo
> Horario de Horario de apertura y cierre
> atención agregado diario
> Servicios Indique los servicios a los cuales
> disponibles los clientes pueden acceder en el
> canal de atención indicado
> (ejemplo: Apertura de productos,
> cierre de productos, asesoría a
> clientes, etc.)
> Páginas web y app Tipo Sitio web o app
> Sitio web Enlace del Sitio web
> Horario de Horario dentro del cual se pueden
> atención realizar los servicios
> Servicios Indique los servicios a los cuales
> disponibles los clientes pueden acceder en el
> canal de atención indicado
> (ejemplo: Apertura de productos,
> cierre de productos, asesoría a
> clientes, etc.)
> Telefónico Servicios Indique los servicios a los cuales
> disponibles los clientes pueden acceder en el
> canal de atención indicado
> (ejemplo: Apertura de productos,
> cierre de productos, asesoría a
> clientes, etc.)
> Teléfono Indique el teléfono asociado a
> cada servicio mencionado
> previamente
> Horario de Indique el horario en el cual el
> atención servicio antes mencionado es
> factible de acceder mediante el
> canal telefónico
> Mensajes de texto Servicios Indique los servicios a los cuales
> disponibles los clientes pueden acceder en el
> canal de atención indicado
> (ejemplo: Apertura de productos,
> cierre de productos, asesoría a
> clientes, etc.)
> Número Indique el número asociado a cada
> servicio mencionado previamente
> Horario de Horario dentro del cual se pueden
> atención realizar los servicios
> Correo electrónico Servicios Indique los servicios a los cuales
> disponibles los clientes pueden acceder en el
> canal de atención indicado
> (ejemplo: Apertura de productos,
> cierre de productos, asesoría a
> clientes, etc.)
> Casilla Indique el correo electrónico
> asociado
> Horario de Horario dentro del cual se pueden
> atención realizar los servicios
> Redes sociales Servicios Indique los servicios a los cuales
> disponibles los clientes pueden acceder en el
> canal de atención indicado
> (ejemplo: Apertura de productos,
> cierre de productos, asesoría a
> clientes, etc.)
> Red social Indique la red social asociada y la
> cuenta
> Horario de Horario dentro del cual se pueden
> atención realizar los servicios
> ATM Dirección Calle y número Bancos
> Ciudad Nombre ciudad
> Comuna Nombre comuna
> Región Nombre región
> Tipo de Indicar si es horario continuo o
> horario discontinuo
> Hora de Hora de apertura de la oficina.
> apertura Generar hora de apertura por cada
> bloque de horario continuo
> Hora de Hora de cierre de la oficina.
> cierre Generar hora de cierre por cada
> bloque de horario continuo
> Horario de Horario de apertura y cierre
> atención agregado diario
> Tipo de Indicar si en el ATM se pueden
> servicio realizar giros, depósitos, entre
> otros"

### Cross-references
- Ley 21.521 Art. 24–26 — the data-sharing regime whose "service channels" set this annex details.
- NCG 514 §IV.A — Table N° 3, which lists "Service channels" among the sets of information to be shared.

> **Source:** NCG 514 §VI Annex N° 1 (2) (03-jul-2024).

---

## VI.3 — Annex N° 1 (3): Enrollment
**NCG anchor:** N° 514, Sección VI, Anexo N°1, 3
**Implements:** Ley 21.521 Art. 24–26 (enrollment data set shared through the SFA)
**Tags:** open-finance, data-set, enrollment, variables, ipi

### Plain-English text

Data set "Enrollment" (Enrolamiento). The IPI that must provide the information is "All" (Todos).

| Variable (Variable) | Detail (Detalle) |
|---|---|
| Customer's name (Nombre del cliente) | Names and surnames of the customer. |
| Business name (Razón social) | Business name in the case of being a legal person. |
| RUT (RUT) | RUT in this format: 11.111.111-1. |
| Corporate purpose or economic activity (Objeto social o actividad económica) | Expression of activity. In case it is not available indicate "ND". |
| Date of start of relationship as customer (Fecha de inicio de relación como cliente) | Day, month, and year of the start of the relationship. If the customer has multiple active products, consider the oldest date from when there is a relationship with that customer. |
| Address (Dirección) | Street, number, commune, and region of the customer. In case it is not available indicate "ND". |
| Website (Sitio web) | Website where applicable. In case it is not available, indicate "ND". |
| E-mail (Correo electrónico) | E-mail. In case it is not available, indicate "ND". |
| Telephone (Teléfono) | Telephone or cellphone. In case it is not available, indicate "ND". |
| Legal representative (Representante legal) | Legal representative where one exists (name and surnames). In case it is not applicable, indicate "NA". |
| Legal-representative RUT (RUT representante legal) | RUT in this format: 11.111.111-1. In case it is not applicable, indicate "NA". |

> **TN:** "IPI que debe proveer la información: Todos" applies to the whole table. The Spanish block transcribes the table verbatim in pdfplumber's column-interleaved line-extraction order. "ND" (no disponible / not available) and "NA" (no aplica / not applicable) are reporting sentinels left verbatim.

### Original Spanish

> "3. Enrolamiento
> VARIABLES DETALLE IPI QUE DEBE
> PROVEER LA
> INFORMACIÓN:
> Nombre del cliente Nombres y apellidos del cliente Todos
> Razón social Razón social en caso de ser persona jurídica
> RUT RUT con este formato: 11.111.111-1
> Objeto social o actividad Expresión de actividad. En caso de no estar disponible
> económica indique "ND" Fecha de inicio de Dia, mes y año del inicio de la relación. Si el cliente tiene
> relación como cliente múltiples productos vigentes, considere la fecha más
> antigua desde cuando tiene una relación con él
> Dirección Calle, número, comuna y región del cliente. En caso de no
> estar disponible indique "ND" Sitio web Sitio web en caso de aplicar. En caso de no estar
> disponible, indique "ND" Correo electrónico Correo electrónico. En caso de no estar disponible, indique "ND" Teléfono Teléfono o celular. En caso de no estar disponible, indique "ND" Representante legal Representante legal en caso de existir (nombre y
> apellidos). En caso de no aplicar, indique "NA" RUT representante legal RUT con este formato: 11.111.111-1. En caso de no
> aplicar, indique "NA"."

### Cross-references
- Ley 21.521 Art. 24–26 — the data-sharing regime whose "enrollment" set this annex details.
- NCG 514 §IV.A — Table N° 3, which lists "Enrollment" among the sets of information to be shared.

> **Source:** NCG 514 §VI Annex N° 1 (3) (03-jul-2024).

---

## VI.4 — Annex N° 1 (4): Historical Financial Positions
**NCG anchor:** N° 514, Sección VI, Anexo N°1, 4
**Implements:** Ley 21.521 Art. 24–26 (historical-financial-positions data set shared through the SFA)
**Tags:** open-finance, data-set, historical-financial-positions, variables, ipi

### Plain-English text

Data set "Historical financial positions" (Posiciones financieras históricas). The table is organized by financial product (a–f) with the variables, their detail, and the IPI that must provide the information for each. Footnote (1) indicates that the detail of products to be reported is in Annex N° 2; footnote (2) gives the arrears-level codes.

**a) Checking accounts and their associated lines of credit, sight accounts, fund-provision accounts, and savings accounts (Cuentas corrientes y sus líneas de crédito asociadas, cuentas a la vista, cuentas de provisión de fondos y cuentas de ahorro)** — IPI: Banks, Payment cards with fund provision, Savings-and-credit cooperatives.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Date (last 12 months) (Fecha (últimos 12 meses)) | Reported date. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type (e.g., "Premium" card for Companies). |
| Balance at month-end (Saldo a fin de mes) | Balance at month-end. |
| Currency (Moneda) | Currency in which the credit balance is held according to table 1 of the MSI. |
| Total line of credit or overdraft at month-end (Línea de crédito o de sobregiro total a fin de mes) | Total amount of the line. |
| Used line of credit or overdraft at month-end (Línea de crédito o de sobregiro utilizada a fin de mes) | Total amount of the used line. |
| Available line of credit or overdraft at month-end (Línea de crédito o de sobregiro disponible a fin de mes) | Total amount of the available line. |

**b) Credit cards, with their respective associated lines of credit (Tarjetas de crédito, con sus respectivas líneas de crédito asociadas)** — IPI: Banks, Card issuers, Savings-and-credit cooperatives.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Date (last 12 months) (Fecha (últimos 12 meses)) | Reported date. |
| Type of financial products (Tipo de productos financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Type of debt (Tipo de deuda) | Indicates whether it is credit in installments, cash advance, or revolving. |
| Balance at month-end (Saldo a fin de mes) | Balance at month-end. |
| Currency (Moneda) | Currency of the debt according to table 1 of the MSI. |
| Total approved line (Línea total aprobada) | Total approved line of the card. |
| Unused line (Línea no utilizada) | Amount of the unused line. |

**c) Money-credit operations (Operaciones de crédito de dinero)** — IPI: Banks, Savings-and-credit cooperatives, Mortgage Mutual Fund Administering Agents, Endorsable parties and Insurance Companies, Institutions that place funds by means of money-credit operations on a massive basis, Compensation Funds (Cajas de Compensación).

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Date (last 12 months) (Fecha (últimos 12 meses)) | Reported date. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Balance at month-end (Saldo a fin de mes) | Balance at month-end. |
| Currency of the debt (Moneda de la deuda) | Currency of the debt according to table 1 of the MSI. |
| Arrears level (Nivel de mora) | Arrears level of the credit (2). |
| Link with a promotional instrument (Vinculación con instrumento de fomento) | Indicate whether it is associated with a promotional instrument according to table 62 of the banking information-system manual. |
| Amount of the guarantee (Monto de la garantía) | Amount of the guarantee. |

**d) Insurance policies (Pólizas de seguro)** — IPI: Insurance companies.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Policy number (Número de póliza) | Code of the insurance. |
| Additional-clause number (CAD) (Número de cláusula adicional (CAD)) | CAD number ancillary to an insurance contract. |
| Date (last 12 months) (Fecha (últimos 12 meses)) | Reported date. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Current premium (Prima vigente) | Amount in pesos of the premium. |
| Periodicity of the premium (Periodicidad de la prima) | Monthly, Annual, or One-time. |
| Frequency of premium payment (Frecuencia del pago de la prima) | Monthly, Annual, or One-time. |
| Type of sale (Tipo de venta) | Direct or intermediated. |
| Broker RUT (RUT del corredor) | Indicate the RUT of the associated broker. |
| Broker name (Nombre del corredor) | Indicate the name of the associated broker. |
| Insured amount (Monto asegurado) | Indicate the insured amount. |
| Currency of the insured amount (Moneda del monto asegurado) | Indicate the currency of the insured amount according to table 1 of the MSI. |

**e) Savings or investment instruments (Instrumentos de ahorro o inversión)** — covering Time deposits (Depósitos a plazo), Mutual Funds and Investment Funds (Fondos Mutuos y Fondos de Inversión), and Voluntary Pension Savings (APV).

For Time deposits — IPI: Banks, Savings-and-credit cooperatives:

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Type of term (Tipo de plazo) | Fixed-term, renewable, or indefinite deposit. |
| Date (last 12 months) (Fecha (últimos 12 meses)) | Reported date. |
| Investment stock at month-end (Stock de Inversión a fin de mes) | Amount of the asset at month-end. |
| Currency of the investment (Moneda de la inversión) | Currency of the asset according to table 1 of the MSI. |
| Term of the deposit (Plazo del depósito) | Indicate the original term of the deposit, in days. |
| Remaining term (Plazo remanente) | Indicate the remaining term of the deposit, in days. |
| Annualized effective interest rate (Tasa de interés efectiva anualizada) | Indicate the annualized interest rate of the instrument. |

For Mutual Funds and Investment Funds — IPI: General Fund Administrators and Portfolio Managers:

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Series (Serie) | Indicate the series of the fund. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Ticker (Nemotécnico) | Ticker. |
| Date (last 12 months) (Fecha (últimos 12 meses)) | Reported date. |
| Investment stock at month-end (Stock de Inversión a fin de mes) | Amount of the asset on the last day of the month. |
| Currency of the asset (Moneda del activo) | Currency of the asset according to table 1 of the MSI. |

For APV — IPI: Banks, Insurance companies, General Fund Administrators and Portfolio Managers, Brokers:

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Date (last 12 months) (Fecha (últimos 12 meses)) | Reported date. |
| Investment stock at month-end (Stock de Inversión a fin de mes) | Amount of the final asset of the month. |
| Currency of the investment (Moneda de la inversión) | Currency of the asset according to table 1 of the MSI. |

**f) Payment-card-operation services (Servicios de operación de tarjetas de pago)** — IPI: Payment-card operators.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Date (last 12 months) (Fecha (últimos 12 meses)) | Reported date. |
| Monthly amounts paid (Montos pagados mensuales) | Monthly amounts paid. |

Footnote (1): Detail of products to be reported in Annex N° 2.

Footnote (2): With the codes: 0 (Credit up to date), 1 (Less than 30 days of arrears), 2 (30 days or more, but less than 60 days of arrears), 3 (60 days or more, but less than 90 days of arrears), 4 (90 days or more, but less than 180 days of arrears), 5 (180 days or more, but less than 1 year of arrears), 6 (One year or more, but less than two years of arrears), 7 (Two years or more, but less than three years of arrears), 8 (Three years or more, but less than 4 years of arrears) and 9 (Four years or more of arrears).

> **TN:** This data-set table spans PDF pages 72–75 and is the longest in the annex. The Spanish block transcribes all four pages verbatim in pdfplumber's column-interleaved line-extraction order (financial-product, detail-product, variable, detail, and IPI columns read line by line, so product groupings and IPI lists appear intermixed with the wrapped variable/detail cell text). The footnotes (1) and (2) follow the table on PDF page 75. One source artifact "t abla 1 del MSI" (a stray space in "tabla") is preserved verbatim as extracted.

### Original Spanish

> "4. Posiciones financieras históricas
> PRODUCTO DETALLE VARIABLES DETALLE IPI QUE DEBE
> FINANCIERO PRODUCTO PROVEER LA
> (1) FINANCIERO INFORMACIÓN:
> a) Cuentas Rut cliente RUT con este formato: Bancos
> corrientes y 11.111.111-1 Tarjetas de pago
> sus líneas de ID interno del producto ID del producto. Único con provisión de
> crédito que permite la fondos
> asociadas, trazabilidad de este Cooperativas de
> cuentas a la Fecha (últimos 12 Fecha informada ahorro y crédito
> vista, cuentas meses)
> de provisión de Tipo de producto Indique el código
> fondos y financiero respectivo de la tabla de
> cuentas de productos del SFA
> ahorro Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto (Ej. Tarjeta
> “Premium” para
> Empresas.)
> Saldo a fin de mes Saldo a fin de mes
> Moneda Moneda en la cual está la
> acreencia según tabla 1
> del MSI
> Línea de crédito o de Monto total de la línea
> sobregiro total a fin de total
> mes
> Línea de crédito o de Monto total de la línea
> sobregiro utilizada a fin utilizada
> de mes
> Línea de crédito o de Monto total de la línea
> sobregiro disponible a fin disponible
> de mes
> b) Tarjetas de Rut cliente RUT con este formato: Bancos
> crédito, con sus 11.111.111-1 Emisores de
> respectivas ID interno del producto ID del producto. Único tarjetas de
> líneas de que permite la crédito
> crédito trazabilidad de este. Cooperativas de
> asociadas Fecha (últimos 12 Fecha informada ahorro y crédito
> meses)
> Tipo de productos Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Tipo de deuda Indica si es crédito en
> cuotas, avance en
> efectivo o rotativo
> Saldo a fin de mes Saldo a fin de mes
> Moneda Moneda de la deuda
> según tabla 1 del MSI
> Línea total aprobada Línea total aprobada de
> la tarjeta
> Línea no utilizada Monto de la línea no
> utilizada
> c) Operaciones Rut cliente RUT con este formato: Bancos
> de crédito de 11.111.111-1 Cooperativas de
> dinero ID interno del producto ID del producto. Único Ahorro y Crédito
> que permite la
> trazabilidad de este
> Fecha (últimos 12 Fecha informada Agentes
> meses) Administradores
> Tipo de producto Indique el código de Mutuos
> financiero respectivo de la tabla de Hipotecarios
> productos del SFA Endosables y
> Categoría comercial Indique si aplica alguna Compañías de
> categoría comercial Seguros
> asociada al producto. Instituciones que
> Tipo texto coloquen fondos
> Saldo a fin de mes Saldo a fin de mes por medio de
> Moneda de la deuda Moneda de la deuda operaciones de
> según tabla 1 del MSI crédito de dinero
> Nivel de mora Nivel de mora del crédito de manera
> (2) masiva
> Vinculación con Indicar si está asociada a Cajas de
> instrumento de fomento un instrumento de Compensación
> fomento según tabla 62
> del manual de sistema de
> información bancario
> Monto de la garantía Monto de la garantía
> d) Pólizas de Rut cliente RUT con este formato: Compañías de
> seguro 11.111.111-1 seguros
> ID interno del producto ID del producto. Único
> que permite la
> trazabilidad de este
> Número de póliza Código del seguro
> Número de cláusula Número de CAD
> adicional (CAD) accesoria al contrato de
> un seguro
> Fecha (últimos 12 Fecha informada
> meses)
> Tipo de producto Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Prima vigente Monto en pesos de la
> prima
> Periodicidad de la prima Mensual, Anual o Única
> Frecuencia del pago de Mensual, Anual o Única
> la prima
> Tipo de venta Directa o intermediada
> RUT del corredor Indique el RUT del
> corredor asociado
> Nombre del corredor Indique el nombre del
> corredor asociado
> Monto asegurado Indique el monto
> asegurado
> Moneda del monto Indique la moneda del
> asegurado monto asegurado según
> t abla 1 del MSI
> e) Depósitos a Rut cliente RUT con este formato: Bancos
> Instrumentos plazo 11.111.111-1 Cooperativas de
> de ahorro o ID interno del producto ID del producto. Único Ahorro y Crédito
> inversión que permite la
> trazabilidad de este
> Tipo de producto Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Tipo de plazo Depósito a plazo fijo,
> renovable o indefinido
> Fecha (últimos 12 Fecha informada
> meses)
> Stock de Inversión a fin Monto del activo al final
> de mes de mes
> Moneda de la inversión Moneda del activo según
> tabla 1 del MSI
> Plazo del depósito Indicar el plazo original
> del depósito, en días
> Plazo remanente Indicar plazo remanente
> del depósito, en días.
> Tasa de interés efectiva Indicar la tasa de interés
> anualizada anualizada del
> instrumento
> Fondos Mutuos Rut cliente RUT con este formato: Administradoras
> y Fondos de 11.111.111-1 Generales de
> Inversión ID interno del producto ID del producto. Único Fondos y
> que permite la Administradores
> trazabilidad de este de Cartera
> Tipo de producto Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Serie Indique la serie del fondo
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Nemotécnico Nemotécnico
> Fecha (últimos 12 Fecha informada
> meses)
> Stock de Inversión a fin Monto del activo al
> de mes último día de mes
> Moneda del activo Moneda del activo según
> tabla 1 del MSI
> APV Rut cliente RUT con este formato: Bancos
> 11.111.111-1 Compañías de
> ID interno del producto ID del producto. Único seguros
> que permite la Administradoras
> trazabilidad de este Generales de
> Tipo de producto Indique el código Fondos y
> financiero respectivo de la tabla de Administradores
> productos del SFA de Cartera
> Categoría comercial Indique si aplica alguna Corredoras
> categoría comercial
> asociada al producto.
> Tipo texto
> Fecha (últimos 12 Fecha informada
> meses)
> Stock de Inversión a fin Monto del activo final de
> de mes mes
> Moneda de la inversión Moneda del activo según
> tabla 1 del MSI
> f) Servicios de Rut cliente RUT con este formato: Operadores de
> operación de 11.111.111-1 tarjetas de pago
> tarjetas de Tipo de producto Indique el código
> pago financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Fecha (últimos 12
> meses) Fecha informada
> Montos pagados Montos pagados
> mensuales mensuales
> (1) Detalle de productos a informar en Anexo N°2
> (2) Con los códigos: 0 (Crédito al día), 1 (Menos de 30 días de mora), 2 (30 días o
> más, pero menos de 60 días de mora), 3 (60 días o más, pero menos de 90 días de
> mora), 4 (90 días o más, pero menos de 180 días de mora), 5 (180 días o más, pero
> menos de 1 año de mora), 6 (Un año o más, pero menos de dos años de mora), 7
> (Dos años o más, pero menos de tres años de mora), 8 (Tres años o más, pero menos
> de 4 años de mora) y 9 (Cuatro años o más de mora)."

### Cross-references
- Ley 21.521 Art. 24–26 — the data-sharing regime whose "historical financial positions" set this annex details.
- NCG 514 §IV.A — Table N° 3, which lists "Historical financial positions" among the sets of information to be shared.
- NCG 514 §VI.A2 — Annex N° 2, the product codification referenced by footnote (1) and by "Type of financial product".

> **Source:** NCG 514 §VI Annex N° 1 (4) (03-jul-2024).

---

## VI.5 — Annex N° 1 (5): Transactional Information
**NCG anchor:** N° 514, Sección VI, Anexo N°1, 5
**Implements:** Ley 21.521 Art. 24–26 (transactional-information data set shared through the SFA)
**Tags:** open-finance, data-set, transactional-information, variables, ipi

### Plain-English text

Data set "Transactional information" (Información transaccional). The table is organized by financial product (a–f); the "detail of the financial product" column is "All" (Todos) except where the product groups it within e). Footnote (1) refers the detail of products to be reported to Annex N° 2.

**a) Checking accounts and their associated lines of credit; sight accounts; fund-provision accounts; and savings accounts** — IPI: Banks, Payment cards with fund provision, Savings-and-credit cooperatives.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal transaction ID (ID interno de la transacción) | Transaction ID that is unique and must allow traceability of the operation. |
| Date of the operation (Fecha de la operación) | Date of the operation reported (year-month-day-hour). |
| Accounting date of the operation (Fecha contable de la operación) | Accounting date of the operation reported (year-month-day-hour). |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Category of the operation (Categoría de la operación) | Transfers, debit purchase, ATM operation, other. |
| Type of operation (Tipo de operación) | Credit or charge. |
| Amount of the operation (Monto de la operación) | Original amount of the operation. |
| Type of person (Tipo de persona) | In charges, indicates whether the charge is against commerce or not. |
| Counterparty RUT (RUT contraparte) | Counterparty RUT. |
| Counterparty name (Nombre contraparte) | Counterparty name. |
| Currency of the operation (Moneda de la operación) | Currency in which the credit or the charge was made according to table 1 of the MSI. |

**b) Credit cards, with their respective associated lines of credit** — IPI: Banks, Card issuers, Savings-and-credit cooperatives.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of financial products (Tipo de productos financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Date of the operation (Fecha de la operación) | Date of the operation reported (year-month-day-hour). |
| Accounting date of the operation (Fecha contable de la operación) | Accounting date of the operation reported (year-month-day-hour). |
| Type of operation (Tipo de operación) | Indicates the type of card operation (installments, cash advance, revolving). |
| Amount of the operation (Monto de la operación) | Amount of the operation. |
| Currency of the operation (Moneda de la operación) | Currency in which the credit or the charge was made. |
| Type of person (Tipo de persona) | In charges, indicates whether the charge is against commerce or not. |
| Commerce information (Información del comercio) | Commerce information in conformity with Decree 44/2012 MINECON. |

**c) Money-credit operations** — IPI: Banks, Savings-and-credit cooperatives, Mortgage Mutual Fund Administering Agents, Endorsable parties and Insurance Companies, Institutions that place funds by means of money-credit operations on a massive basis, Compensation Funds.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Date of the operation (Fecha de la operación) | Date of the operation reported (year-month-day). |
| Accounting date of the operation (Fecha contable de la operación) | Accounting date of the operation reported (year-month-day). |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Amount of the operation (Monto de la operación) | Original amount of the operation expressed in pesos. |
| Currency of the credit (Moneda del crédito) | Currency in which the credit was delivered according to table 1 of the MSI. |
| Annual interest rate (Tasa de interés anual) | Annual interest rate of the credit. |
| Term of the credit (Plazo del crédito) | Term (in months) of the credit. |
| Link with a promotional instrument (Vinculación con instrumento de fomento) | Indicate whether it is associated with a promotional instrument according to table 62 of the banking information-system manual. |
| Amount of the guarantee (Monto de la garantía) | Amount of the guarantee. |

**d) Insurance policies** — IPI: Insurance companies.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Policy number (Numero de póliza) | Code of the insurance. |
| Additional-clause number (CAD) (Número de cláusula adicional (CAD)) | CAD number ancillary to an insurance contract. |
| Contracting date (Fecha de la contratación) | Date of contracting of the insurance reported. |
| Validity date, start (Fecha de vigencia, inicio) | Start date of validity of the insurance. |
| Validity date, end (Fecha de vigencia, fin) | Final date of validity of the insurance. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Premium stipulated at the moment of contracting (Prima estipulada al momento de contratar) | Amount in pesos of the premium. |
| Periodicity of the premium (Periodicidad de la prima) | Monthly, Annual, or One-time. |
| Frequency of premium payment (Frecuencia del pago de la prima) | Monthly, Annual, or One-time. |
| Type of sale (Tipo de venta) | Direct or intermediated. |
| Broker RUT (RUT del corredor) | Indicate the RUT of the associated broker. |
| Broker name (Nombre del corredor) | Indicate the name of the associated broker. |
| Insured amount (Monto asegurado) | Indicate the insured amount. |
| Currency of the insured amount (Moneda del monto asegurado) | Indicate the currency of the insured amount according to table 1 of the MSI. |

**e) Savings or investment instruments** — covering Time deposits, Mutual Funds and Investment Funds, and APV.

For Time deposits — IPI: Banks, Savings-and-credit cooperatives:

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Type of term (Tipo de plazo) | Fixed-term, renewable, or indefinite deposit. |
| Type of operation (Tipo de operación) | Contracting, contribution, redemption. |
| Date of the operation (Fecha de la operación) | Date of the operation reported (year-month-day). |
| Amount of the operation (Monto de la operación) | Amount of the operation. |
| Currency (Moneda) | Currency of the operation according to table 1 of the MSI. |
| Term of the deposit (Plazo del depósito) | Indicate the original term of the deposit, in days. |
| Annualized effective interest rate (Tasa de interés efectiva anualizada) | Indicate the annualized interest rate of the instrument. |

For Mutual Funds and Investment Funds — IPI: General Fund Administrators and Portfolio Managers:

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Series (Serie) | Indicate the series of the fund. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Ticker (Nemotécnico) | Ticker. |
| Date of the operation (Fecha de la operación) | Date of the operation reported (year-month-day). |
| Type of operation (Tipo de operación) | Contracting, contribution, redemption. |
| Amount of the operation (Monto de la operación) | Amount of the initial contribution, contribution and redemption. |
| Currency (Moneda) | Currency of the contribution/redemption according to table 1 of the MSI. |

For APV — IPI: Banks, Insurance companies, General Fund Administrators and Portfolio Managers, Brokers:

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Contracting date (Fecha de la contratación) | Date of contracting reported (year-month-day). |
| Type of operation (Tipo de operación) | Contracting, contribution, redemption. |
| Contribution/Redemption (Aporte/Rescate) | Amount of the movement. |
| Currency (Moneda) | Currency of the contribution/redemption according to table 1 of the MSI. |

**f) Payment-card-operation services** — IPI: Payment-card operators.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Validity of an affiliation contract (Vigencia de un contrato de afiliación) | Date of the affiliation reported (year-month-day). |

Footnote (1): Detail of products to be reported in Annex N° 2.

> **TN:** This data-set table spans PDF pages 76–79. The Spanish block transcribes all four pages verbatim in pdfplumber's column-interleaved line-extraction order (financial-product, detail-product, variable, detail, and IPI columns read line by line, so product groupings and IPI lists appear intermixed with the wrapped variable/detail cell text). The footnote (1) follows the table on PDF page 79.

### Original Spanish

> "5. Información transaccional
> PRODUCTO DETALLE VARIABLES DETALLE IPI QUE DEBE
> FINANCIERO PRODUCTO PROVEER LA
> (1) FINANCIE INFORMACIÓN:
> RO
> a) Cuentas Todos Rut cliente RUT con este formato: Bancos
> corrientes y sus 11.111.111-1 Tarjetas de pago
> líneas de crédito ID interno de la ID de la transacción que con provisión de
> asociadas; transacción es único y que debe
> fondos
> cuentas a la permitir hacer
> Cooperativas de
> vista; cuentas de trazabilidad de la
> provisión de operación Ahorro y Crédito
> fondos; y Fecha de la operación Fecha de la operación
> cuentas de informada (año-mes-día-
> ahorro hora)
> Fecha contable de la Fecha contable de la
> operación operación informada
> (año-mes-día-hora)
> Tipo de producto Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Categoría de la operación Transferencias, compra
> con débito, operación en
> cajero automático, otra
> Tipo de operación Abono o cargo
> Monto de la operación Monto original de la
> operación
> Tipo de persona En cargos, indica si el
> cargo es contra comercio
> o no
> RUT contraparte RUT contraparte
> Nombre contraparte Nombre contraparte
> Moneda de la operación Moneda en la cual fue
> realizado el abono o el
> cargo según tabla 1 del
> MSI
> b) Tarjetas de Todos Rut cliente RUT con este formato: Bancos
> crédito, con sus 11.111.111-1 Emisores de
> respectivas ID interno del producto ID del producto. Único tarjetas de crédito
> líneas de crédito que permite la
> Cooperativas de
> asociadas trazabilidad de este
> Ahorro y Crédito
> Tipo de productos Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Fecha de la operación Fecha de la operación
> informada (año-mes-día-
> hora)
> Fecha contable de la Fecha contable de la
> operación operación informada
> (año-mes-día-hora)
> Tipo de operación Indica el tipo de
> operación de tarjeta
> (cuotas, avance en
> efectivo, rotativo)
> Monto de la operación Monto de la operación
> Moneda de la operación Moneda en la cual fue
> realizado el abono o el
> cargo
> Tipo de persona En cargos, indica si el
> cargo es contra comercio
> o no
> Información del comercio Información del comercio
> conforme con Decreto
> 44/2012 MINECON
> c) Operaciones Todos Rut cliente RUT con este formato: Bancos
> de crédito de 11.111.111-1 Cooperativas de
> dinero ID interno del producto ID del producto. Único Ahorro y Crédito
> que permite la
> Agentes
> trazabilidad de este
> Administradores
> Fecha de la operación Fecha de la operación
> de Mutuos
> informada (año-mes-
> día). Hipotecarios
> Fecha contable de la Fecha contable de la Endosables y
> operación operación informada Compañías de
> (año-mes-día). Seguros
> Tipo de producto Indique el código Instituciones que
> financiero respectivo de la tabla de
> coloquen fondos
> productos del SFA.
> por medio de
> Categoría comercial Indique si aplica alguna
> categoría comercial operaciones de
> asociada al producto. crédito de dinero
> Tipo texto de manera masiva
> Monto de la operación Monto original de la Cajas de
> operación expresada en Compensación
> pesos
> Moneda del crédito Moneda en que fue
> entregado el crédito
> según tabla 1 del MSI
> Tasa de interés anual Tasa de interés anual del
> crédito
> Plazo del crédito Plazo (en meses) del
> crédito
> Vinculación con Indicar si está asociada a
> instrumento de fomento un instrumento de
> fomento según tabla 62
> del manual de sistema de
> información bancario
> Monto de la garantía Monto de la garantía
> d) Pólizas de Todos Rut cliente RUT con este formato: Compañías de
> seguro 11.111.111-1 Seguros
> ID interno del producto ID del producto. Único
> que permite la
> trazabilidad de este
> Numero de póliza Código del seguro
> Número de cláusula Número de CAD
> adicional (CAD) accesoria al contrato de
> un seguro
> Fecha de la contratación Fecha de contratación del
> seguro informado
> Fecha de vigencia, inicio Fecha de inicio de
> vigencia del seguro
> Fecha de vigencia, fin Fecha final de vigencia
> del seguro
> Tipo de producto Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Prima estipulada al Monto en pesos de la
> momento de contratar prima
> Periodicidad de la prima Mensual, Anual o Única
> Frecuencia del pago de la Mensual, Anual o Única
> prima
> Tipo de venta Directa o intermediada
> RUT del corredor Indique el RUT del
> corredor asociado
> Nombre del corredor Indique el nombre del
> corredor asociado
> Monto asegurado Indique el monto
> asegurado
> Moneda del monto Indique la moneda del
> asegurado monto asegurado según
> tabla 1 del MSI
> e) Instrumentos Depósitos a Rut cliente RUT con este formato: Bancos
> de ahorro o plazo 11.111.111-1 Cooperativas de
> inversión ID interno del producto ID del producto. Único Ahorro y Crédito
> que permite la
> trazabilidad de este
> Tipo de producto Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Tipo de plazo Depósito a plazo fijo,
> renovable o indefinido
> Tipo de operación Contratación, aporte,
> rescate
> Fecha de la operación Fecha de la operación
> informada (año-mes-día)
> Monto de la operación Monto de la operación
> Moneda Moneda de la operación
> según tabla 1 del MSI
> Plazo del depósito Indicar el plazo original
> del depósito, en días.
> Tasa de interés efectiva Indicar la tasa de interés
> anualizada anualizada del
> instrumento
> Fondos Rut cliente RUT con este formato: Administradoras
> Mutuos y 11.111.111-1 Generales de
> Fondos de ID interno del producto ID del producto. Único Fondos y
> Inversión que permite la Administradores
> trazabilidad de este de Cartera
> Tipo de producto Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Serie Indique la serie del fondo
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Nemotécnico Nemotécnico
> Fecha de la operación Fecha de la operación
> informada (año-mes-día)
> Tipo de operación Contratación, aporte,
> rescate
> Monto de la operación Monto del aporte inicial,
> aporte y rescate
> Moneda Moneda del
> aporte/rescate según
> tabla 1 del MSI
> APV Rut cliente RUT con este formato: Bancos
> 11.111.111-1 Compañías de
> ID interno del producto ID del producto. Único Seguros
> que permite la
> Administradoras
> trazabilidad de este
> Generales de
> Tipo de producto Indique el código
> Fondos y
> financiero respectivo de la tabla de
> productos del SFA Administradores
> Categoría comercial Indique si aplica alguna de Cartera
> categoría comercial Corredoras
> asociada al producto.
> Tipo texto
> Fecha de la contratación Fecha de la contratación
> informada (año-mes-día)
> Tipo de operación Contratación, aporte,
> rescate
> Aporte/Rescate Monto del movimiento
> Moneda Moneda del
> aporte/rescate según
> tabla 1 del MSI
> f) Servicios de Todos Rut cliente RUT con este formato: Operadores de
> operación de 11.111.111-1 tarjetas de pago
> tarjetas de pago Tipo de producto Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Vigencia de un contrato de Fecha de la afiliación
> afiliación informada (año-mes-día)
> (1) Detalle de productos a informar en Anexo N°2"

### Cross-references
- Ley 21.521 Art. 24–26 — the data-sharing regime whose "transactional information" set this annex details.
- NCG 514 §IV.A — Table N° 3, which lists "Use and transaction history" among the sets of information to be shared.
- NCG 514 §VI.A2 — Annex N° 2, the product codification referenced by footnote (1) and by "Type of financial product".

> **Source:** NCG 514 §VI Annex N° 1 (5) (03-jul-2024).

---

## VI.6 — Annex N° 1 (6): Active Products
**NCG anchor:** N° 514, Sección VI, Anexo N°1, 6
**Implements:** Ley 21.521 Art. 24–26 (active-products data set shared through the SFA)
**Tags:** open-finance, data-set, active-products, variables, ipi

### Plain-English text

Data set "Active products" (Productos Vigentes). The table is organized by financial product (a–f); the "detail of the financial product" column is "All" (Todos) except where the product groups it within e). Footnote (1) refers the detail of products to Annex N° 2; footnote (2) gives the arrears-level codes.

**a) Checking accounts and their associated lines of credit; sight accounts; fund-provision accounts; and savings accounts** — IPI: Banks, Payment cards with fund provision, Savings-and-credit cooperatives.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Date of contracting of the product (Fecha de contracción del producto) | Date of the contracting of the product reported (year-month-day). |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate, where applicable, the commercial category associated with the product. Text type. |
| Balance (Saldo) | Current balance. |
| Currency (Moneda) | Currency of the balance according to table 1 of the MSI. |
| Total line of credit or overdraft (Línea de crédito o de sobregiro total) | Total amount of the line. |
| Used line of credit or overdraft (Línea de crédito o de sobregiro utilizada) | Total amount of the used line. |
| Available line of credit or overdraft (Línea de crédito o de sobregiro disponible) | Total amount of the available line. |

**b) Credit cards, with their respective associated lines of credit** — IPI: Banks, Card issuers, Savings-and-credit cooperatives.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Date of contracting of the product (Fecha de contratación del producto) | Date of the contracting of the product reported (year-month-day). |
| Type of financial products (Tipo de productos financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Type of debt (Tipo de deuda) | Indicates the type of card operation (installments, cash advance, revolving). |
| Balance (Saldo) | Current balance of the product. |
| Currency (Moneda) | Currency of the debt according to table 1 of the MSI. |
| Total approved line (Línea total aprobada) | Total approved line. |
| Unused line (Línea no utilizada) | Amount of the unused line. |

**c) Money-credit operations** — IPI: Banks, Savings-and-credit cooperatives, Mortgage Mutual Fund Administering Agents, Endorsable parties and Insurance Companies, Institutions that place funds by means of money-credit operations on a massive basis, Compensation Funds.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Balance (Saldo) | Current balance of the product. |
| Currency (Moneda) | Currency of the balance reported according to table 1 of the MSI. |
| Arrears level (Nivel de mora) | Arrears level of the credit (2). |
| Link with a promotional instrument (Vinculación con instrumento de fomento) | Indicate whether it is associated with a promotional instrument according to table 62 of the banking information-system manual. |
| Amount of the guarantee (Monto de la garantía) | Amount of the guarantee. |

**d) Insurance policies** — IPI: Insurance companies.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Policy number (Numero de póliza) | Code of the insurance. |
| Additional-clause number (CAD) (Número de cláusula adicional (CAD)) | CAD number ancillary to an insurance contract. |
| Date of contracting of the product (Fecha de contratación del producto) | Date of the contracting of the product reported (year-month-day). |
| Validity date, start (Fecha de vigencia, inicio) | Start date of validity of the insurance. |
| Validity date, end (Fecha de vigencia, fin) | Final date of validity of the insurance. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Current premium (Prima vigente) | Amount in pesos of the premium. |
| Periodicity of the premium (Periodicidad de la prima) | Monthly, Annual, or One-time. |
| Frequency of premium payment (Frecuencia del pago de la prima) | Monthly, Annual, or One-time. |
| Type of sale (Tipo de venta) | Direct or intermediated. |
| Broker RUT (RUT del corredor) | Indicate the RUT of the associated broker. |
| Broker name (Nombre del corredor) | Indicate the name of the associated broker. |
| Insured amount (Monto asegurado) | Indicate the insured amount. |
| Currency of the insured amount (Moneda del monto asegurado) | Indicate the currency of the insured amount according to table 1 of the MSI. |

**e) Savings or investment instruments** — covering Time deposits, Mutual Funds and Investment Funds, and APV.

For Time deposits — IPI: Banks, Savings-and-credit cooperatives:

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of instrument (Tipo de instrumento) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Type of term (Tipo de plazo) | Fixed-term, renewable, or indefinite deposit. |
| Date of contracting of the product (Fecha de contracción del producto) | Date of the contracting of the product reported (year-month-day). |
| Balance (Saldo) | Amount of the investment to date. |
| Currency of the investment (Moneda de la inversión) | Currency of the investment according to table 1 of the MSI. |
| Term of the deposit (Plazo del depósito) | Indicate the original term of the deposit, in days. |
| Remaining term (Plazo remanente) | Indicate the remaining term of the deposit, in days. |
| Annualized effective interest rate (Tasa de interés efectiva anualizada) | Indicate the annualized interest rate of the instrument. |

For Mutual Funds and Investment Funds — IPI: General Fund Administrators and Portfolio Managers:

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Series (Serie) | Indicate the series of the fund. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Ticker (Nemotécnico) | Ticker. |
| Date of contracting of the product (Fecha de contratación del producto) | Date of the contracting of the product reported (year-month-day). |
| Balance (Saldo) | Amount of the investment to date. |
| Currency of the asset (Moneda del activo) | Currency of the asset according to table 1 of the MSI. |

For APV — IPI: Banks, Insurance companies, General Fund Administrators and Portfolio Managers, Brokers:

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Internal product ID (ID interno del producto) | Product ID. Unique, allowing its traceability. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Date of contracting of the product (Fecha de contratación del producto) | Date of the contracting of the product reported (year-month-day). |
| Balance (Saldo) | Amount of the investment to date. |
| Currency of the investment (Moneda de la inversión) | Currency of the investment according to table 1 of the MSI. |

**f) Payment-card-operation services** — IPI: Payment-card operators.

| Variable | Detail |
|---|---|
| Customer RUT (Rut cliente) | RUT in this format: 11.111.111-1. |
| Type of financial product (Tipo de producto financiero) | Indicate the respective code from the table of products of the SFA. |
| Commercial category (Categoría comercial) | Indicate whether any commercial category associated with the product applies. Text type. |
| Validity of an affiliation contract (Vigencia de un contrato de afiliación) | Indicates whether it has a current affiliation contract. |

Footnote (1): Detail of products to be reported in Annex N° 2.

Footnote (2): With the codes: 0 (Credit up to date), 1 (Less than 30 days of arrears), 2 (30 days or more, but less than 60 days of arrears), 3 (60 days or more, but less than 90 days of arrears), 4 (90 days or more, but less than 180 days of arrears), 5 (180 days or more, but less than 1 year of arrears), 6 (One year or more, but less than two years of arrears), 7 (Two years or more, but less than three years of arrears), 8 (Three years or more, but less than 4 years of arrears) and 9 (Four years or more of arrears).

> **TN:** This data-set table spans PDF pages 80–83. The Spanish block transcribes all four pages verbatim in pdfplumber's column-interleaved line-extraction order. The footnotes (1) and (2) follow the table on PDF page 83.

### Original Spanish

> "6. Productos Vigentes
> PRODUCTO DETALLE VARIABLES DETALLE IPI QUE DEBE
> FINANCIERO PRODUCTO PROVEER LA
> FINANCIERO INFORMACIÓN:
> a) Cuentas Todos Rut cliente RUT con este formato: Bancos
> corrientes y sus 11.111.111-1 Tarjetas de pago
> líneas de ID interno del producto ID del producto. Único con provisión de
> crédito que permite la fondos
> asociadas; trazabilidad de este Cooperativas de
> cuentas a la Fecha de contracción del Fecha de la contratación Ahorro y Crédito
> vista; cuentas producto del producto informada
> de provisión de (año-mes-día)
> fondos; y Tipo de producto Indique el código
> cuentas de financiero respectivo de la tabla de
> ahorro productos del SFA
> Categoría comercial Indique, si aplica, la
> categoría comercial
> asociada al producto.
> Tipo texto
> Saldo Saldo vigente
> Moneda Moneda del saldo según
> tabla 1 del MSI
> Línea de crédito o de Monto total de la línea
> sobregiro total total
> Línea de crédito o de Monto total de la línea
> sobregiro utilizada utilizada
> Línea de crédito o de Monto total de la línea
> sobregiro disponible disponible
> b) Tarjetas de Todos Rut cliente RUT con este formato: Bancos
> crédito, con sus 11.111.111-1 Emisores de
> respectivas ID interno del producto ID del producto. Único tarjetas de
> líneas de que permite la crédito
> crédito trazabilidad de este Cooperativas de
> asociadas Fecha de contratación Fecha de la contratación Ahorro y Crédito
> del producto del producto informada
> (año-mes-día)
> Tipo de productos Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Tipo de deuda Indica el tipo de
> operación de tarjeta
> (cuotas, avance en
> efectivo, rotativo)
> Saldo Saldo vigente del
> producto
> Moneda Moneda de la deuda
> según tabla 1 del MSI
> Línea total aprobada Línea total aprobada
> Línea no utilizada Monto de la línea no
> utilizada
> c) Operaciones Todos Rut cliente RUT con este formato: Bancos
> de crédito de 11.111.111-1 Cooperativas de
> dinero ID interno del producto ID del producto. Único Ahorro y Crédito
> que permite la
> trazabilidad de este
> Tipo de producto Indique el código Agentes
> financiero respectivo de la tabla de Administradores
> productos del SFA de Mutuos
> Categoría comercial Indique si aplica alguna Hipotecarios
> categoría comercial Endosables y
> asociada al producto. Compañías de
> Tipo texto Seguros
> Saldo Saldo vigente del Instituciones que
> producto coloquen fondos
> Moneda Moneda del saldo por medio de
> informado según tabla 1 operaciones de
> del MSI crédito de dinero
> Nivel de mora Nivel de mora del crédito de manera
> (2) masiva
> Vinculación con Indicar si está asociada a Cajas de
> instrumento de fomento un instrumento de Compensación
> fomento según tabla 62
> del manual de sistema de
> información bancario
> Monto de la garantía Monto de la garantía
> d) Pólizas de Todos Rut cliente RUT con este formato: Compañías de
> seguro 11.111.111-1 Seguros
> ID interno del producto ID del producto. Único
> que permite la
> trazabilidad de este
> Numero de póliza Código del seguro
> Número de cláusula Número de CAD
> adicional (CAD) accesoria al contrato de
> un seguro
> Fecha de contratación Fecha de la contratación
> del producto del producto informada
> (año-mes-día)
> Fecha de vigencia, inicio Fecha de inicio de
> vigencia del seguro
> Fecha de vigencia, fin Fecha final de vigencia
> del seguro
> Tipo de producto Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Prima vigente Monto en pesos de la
> prima
> Periodicidad de la prima Mensual, Anual o Única
> Frecuencia del pago de Mensual, Anual o Única
> la prima
> Tipo de venta Directa o intermediada
> RUT del corredor Indique el RUT del
> corredor asociado
> Nombre del corredor Indique el nombre del
> corredor asociado
> Monto asegurado Indique el monto
> asegurado
> Moneda del monto Indique la moneda del
> asegurado monto asegurado según
> tabla 1 del MSI
> e) Depósitos a Rut cliente RUT con este formato: Bancos
> Instrumentos plazo 11.111.111-1 Cooperativas de
> de ahorro o ID interno del producto ID del producto. Único ahorro y crédito
> inversión que permite la
> trazabilidad de este
> Tipo de instrumento Indique el código
> respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Tipo de plazo Depósito a plazo fijo,
> renovable o indefinido
> Fecha de contracción del Fecha de la contratación
> producto del producto informada
> (año-mes-día)
> Saldo Monto de la inversión a la
> fecha
> Moneda de la inversión Moneda de la inversión
> según tabla 1 del MSI
> Plazo del depósito Indicar el plazo original
> del depósito, en días
> Plazo remanente Indicar plazo remanente
> del depósito, en días
> Tasa de interés efectiva Indicar la tasa de interés
> anualizada anualizada del
> instrumento
> Fondos Mutuos Rut cliente RUT con este formato: Administradoras
> y Fondos de 11.111.111-1 generales de
> Inversión ID interno del producto ID del producto. Único fondos y
> que permite la administradores
> trazabilidad de este de cartera
> Tipo de producto Indique el código
> financiero respectivo de la tabla de
> productos del SFA
> Serie Indique la serie del fondo
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Nemotécnico Nemotécnico
> Fecha de contratación Fecha de la contratación
> del producto del producto informada
> (año-mes-día)
> Saldo Monto de la inversión a la
> fecha
> Moneda del activo Moneda del activo según
> tabla 1 del MSI
> APV Rut cliente RUT con este formato: Bancos
> 11.111.111-1 Compañías de
> ID interno del producto ID del producto. Único seguros
> que permite la
> Administradoras
> trazabilidad de este
> generales de
> Tipo de producto Indique el código
> fondos y
> financiero respectivo de la tabla de
> productos del SFA administradores
> Categoría comercial Indique si aplica alguna de cartera
> categoría comercial Corredoras
> asociada al producto.
> Tipo texto
> Fecha de contratación Fecha de la contratación
> del producto del producto informada
> (año-mes-día)
> Saldo Monto de la inversión a la
> fecha
> Moneda de la inversión Moneda de la inversión
> según tabla 1 del MSI
> f) Servicios de Rut cliente RUT con este formato: Operadores de
> operación de 11.111.111-1 Tarjetas de Pago
> tarjetas de Tipo de producto Indique el código
> pago financiero respectivo de la tabla de
> productos del SFA
> Categoría comercial Indique si aplica alguna
> categoría comercial
> asociada al producto.
> Tipo texto
> Vigencia de un contrato Indica si tiene un
> de afiliación contrato de afiliación
> vigente
> (1) Detalle de productos a informar en Anexo N°2
> (2) Con los códigos: 0 (Crédito al día), 1 (Menos de 30 días de mora), 2 (30 días o más,
> pero menos de 60 días de mora), 3 (60 días o más, pero menos de 90 días de mora), 4
> (90 días o más, pero menos de 180 días de mora), 5 (180 días o más, pero menos de 1
> año de mora), 6 (Un año o más, pero menos de dos años de mora), 7 (Dos años o más,
> pero menos de tres años de mora), 8 (Tres años o más, pero menos de 4 años de mora)
> y 9 (Cuatro años o más de mora)."

### Cross-references
- Ley 21.521 Art. 24–26 — the data-sharing regime whose "active products" set this annex details.
- NCG 514 §IV.A — Table N° 3, which lists "Current products" (Productos vigentes) among the sets of information to be shared.
- NCG 514 §VI.A2 — Annex N° 2, the product codification referenced by footnote (1) and by "Type of financial product".

> **Source:** NCG 514 §VI Annex N° 1 (6) (03-jul-2024).

---

## VI.7 — Annex N° 1 (7): Payment Initiation
**NCG anchor:** N° 514, Sección VI, Anexo N°1, 7
**Implements:** Ley 21.521 Art. 20 (payment-initiation service) AND Ley 21.521 Art. 25 (information shared for payment initiation)
**Tags:** open-finance, data-set, payment-initiation, variables, ipc, psip

### Plain-English text

Data set "Payment initiation" (Iniciación de Pagos). The parties involved (Partes involucradas) are the IPC and the PSIP.

| Variable (Variable) | Detail (Detalle) |
|---|---|
| Type of operation (Tipo de operación) | Payment order, electronic funds transfer (TEF), recurring payment. |
| Periodicity (Periodicidad) | Periodicity of the payment and its deadline date. |
| Payment limit (Límite de pagos) | For the case of recurring payments: maximum amount and minimum amount. |
| Origin institution (Institución de origen) | Code of the payment's origin institution. |
| Origin account (Cuenta de origen) | Origin account number. |
| Type of origin account (Tipo de cuenta de origen) | Indicate the respective code from the table of products of the SFA. |
| Payer RUT (RUT pagador) | RUT of the payer in this format: 11.111.111-1. |
| Payer name (Nombre pagador) | Name or business name of the payer. |
| Destination institution (Institución de destino) | Code of the payment's destination institution. |
| Destination account (Cuenta de destino) | Destination account number. |
| Type of destination account (Tipo de cuenta de destino) | Indicate the respective code from the table of products of the SFA. |
| Payment-recipient RUT (RUT receptor del pago) | RUT of the recipient of the payment or addressee in this format: 11.111.111-1. |
| Payment-recipient name (Nombre receptor del pago) | Name or business name of the recipient of the payment or addressee. |
| Amount (Monto) | Amount of the operation or payment. |
| Currency (Moneda) | Currency of the operation according to table 1 of the MSI. |
| Date and time of the operation (Fecha y hora de la operación) | Date and time of the operation (e.g.: DD-MM-AAAA HH:MM:SS). |

> **TN:** The third column here is "PARTES INVOLUCRADAS" ("PARTIES INVOLVED": IPC and PSIP), not the "IPI that must provide the information" used by the other data sets, because payment initiation is an exchange between the IPC and the PSIP rather than a provision by an IPI. The Spanish block transcribes the table verbatim in pdfplumber's column-interleaved line-extraction order.

### Original Spanish

> "7. Iniciación de Pagos
> VARIABLES DETALLE PARTES
> INVOLUCRADAS
> Tipo de operación Orden de pago, TEF, pago recurrente IPC y PSIP
> Periodicidad Periodicidad del pago y su fecha límite
> Límite de pagos Para el caso de pagos recurrentes: Monto máximo y monto
> mínimo
> Institución de origen Código de institución de origen del pago
> Cuenta de origen Número de cuenta de origen
> Tipo de cuenta de Indique el código respectivo de la tabla de productos del SFA
> origen
> RUT pagador RUT del pagador con este formato: 11.111.111-1
> Nombre pagador Nombre o razón social del pagador
> Institución de destino Código de institución de destino del pago
> Cuenta de destino Número de cuenta de destino
> Tipo de cuenta de Indique el código respectivo de la tabla de productos del SFA
> destino
> RUT receptor del pago RUT del receptor del pago o destinatario con este formato:
> 11.111.111-1
> Nombre receptor del Nombre o razón social del receptor del pago o destinatario
> pago
> Monto Monto de la operación o pago
> Moneda Moneda de la operación según tabla 1 del MSI
> Fecha y hora de la Fecha y hora de la operación (ej: DD-MM-AAAA HH:MM:SS)
> operación"

### Cross-references
- Ley 21.521 Art. 20 — the payment-initiation service whose minimum exchange data this annex specifies.
- Ley 21.521 Art. 25 — the data-sharing regime under which payment-initiation information is exchanged.
- NCG 514 §IV.A — Table N° 3, which lists "Payment initiation" among the sets of information to be shared.
- NCG 514 §VI.A2 — Annex N° 2, the product table referenced by "Type of origin/destination account".

> **Source:** NCG 514 §VI Annex N° 1 (7) (03-jul-2024).

---

## VI.A2 — Annex N° 2: Products of the SFA
**NCG anchor:** N° 514, Sección VI, Anexo N°2
**Implements:** Ley 21.521 Art. 24–26 (codification of products reported in the SFA)
**Tags:** open-finance, products, codification, taxonomy, sfa-code

### Plain-English text

Annex N° 2 (Products of the SFA / Productos del SFA) sets the SFA code (CÓDIGO SFA) for each product, organized by category (a–g). The codes are: account products A001–A007; credit card B001; money-credit products C001–C019; insurance products D001–D425 (life individual, traditional collective, banking/retail, pension, and general lines); savings-or-investment products E001–E302; payment-card-operation service F001; and services of entities registered as Financial-Service Providers G001–G005.

**a) Checking accounts and their associated lines of credit; sight accounts; fund-provision accounts; and savings accounts:** Checking account (Cuenta corriente) A001; Sight account (Cuenta a la vista) — Sight account (Cuenta vista) A002, RUT account (Cuenta RUT) A003; Account with fund provision (Cuenta con provisión de fondos) A004; Savings accounts (Cuentas de ahorro) — for housing (para la vivienda) A005, with deferred withdrawal (con giro diferido) A006, with unconditional withdrawal (con giro incondicional) A007.

**b) Credit cards, with their respective associated lines of credit:** Credit card (Tarjeta de crédito) B001.

**c) Money-credit operations:** Credits (Créditos) — Consumer (Consumo): installment credit not deducted from payroll (Crédito en cuotas distintos de descuento por planilla) C001, installment credit deducted from payroll (Crédito en cuotas mediante descuento por planilla) C002, lines of credit on a checking account (Líneas de crédito en cuenta corriente) C003, other consumer credits (Otros créditos de consumo) C004; Housing mortgage (Hipotecario de vivienda): mortgage in letters of credit (Hipotecario en letras de crédito) C005, endorsable mortgage mutual (Mutuo hipotecario endosable) C006, mortgage purchased from ANAP (Hipotecario comprado a ANAP) C007, non-endorsable mortgage mutual (Mutuo hipotecario no endosable) C008, other mortgage credits (Otros créditos hipotecarios) C009, mutuals financed with mortgage bonds (Mutuos financiados con bonos hipotecarios) C010, complementary housing credits (Créditos complementarios de vivienda) C011; Commercial (Comercial): owed by banks (Adeudado por bancos) C012, commercial placements (Colocaciones comerciales) C013, factoring operations (Operaciones de factoring) C014, commercial leasing (Leasing comercial) C015, mortgage loans for general purposes (Préstamos hipotecarios para fines generales) C016; Student (Estudiantiles): Law N° 20.027 student loans (Préstamos estudiantiles Ley N° 20.027) C017, CORFO-guaranteed student loans (Préstamos estudiantiles con garantía CORFO) C018, other student loans (Otros préstamos estudiantiles) C019.

**d) Insurance policies:** Life (Vida) — Individual Insurance (Seguros Individuales) D101–D150, Traditional Collective Insurance (Seguros Colectivos Tradicionales) D201–D250, Banking/Retail Insurance (Seguros Banca Seguros y Retail) D301–D350, and Pension Insurance (Seguros Previsionales) D421–D425; General (Generales) — Damage to Property (Daños a los Bienes) D001–D009, Other Damage to Property (Otros Daños a los Bienes) D010–D012, Civil Liability (Responsabilidad Civil) D013–D016, Transport (Transporte) D017–D019, Engineering (Ingeniería) D020–D023, Guarantee and Credit (Garantía y Crédito) D024–D029, Health and Personal Accidents (Salud y Accidentes Personales) D030–D032, and Other Insurance (Otros Seguros) D033–D050.

**e) Savings or investment instruments:** Time deposits (Depósitos a plazo) E001–E003; Mutual Funds (Fondos Mutuos) E101–E108; Investment Funds (Fondos de Inversión) E201–E202; APV E301–E302.

**f) Payment-card-operation services:** Payment-card operation (Operación de tarjetas de pago) F001.

**g) Services of entities registered as Financial-Service Providers (Servicios de las entidades registradas como Prestadoras de Servicios Financieros):** Credit and investment advisors (Asesores de crédito e inversión) G001; Crowdfunding platform (Plataforma de financiamiento colectivo) G002; Alternative trading systems (Sistemas alternativos de transacción) G003; Intermediation and custody of financial instruments (Intermediación y custodia de instrumentos financieros) G004; Order routing (Enrutamiento de órdenes) G005.

> **TN:** This product-codification table spans PDF pages 85–89. The Spanish block transcribes all five pages verbatim in pdfplumber's column-interleaved line-extraction order (category, subcategory, sub-subcategory, product, and SFA-code columns read line by line, so product names appear intermixed with their codes and groupings exactly as the source PDF extracts). Several insurance rows in the banking/retail block share repeated codes (D303, D350) as printed in the source; these are preserved verbatim. Locked SFA terms are used in the English: "plataforma de financiamiento colectivo" → "crowdfunding platform", "sistemas alternativos de transacción" → "alternative trading systems", "enrutamiento de órdenes" → "order routing", per the lexicon.

### Original Spanish

> "Anexo N°2: Productos del SFA
> CATEGORÍA CÓDIGO SFA
> a) Cuentas Cuenta corriente A001
> corrientes y sus Cuenta a la vista Cuenta vista A002
> líneas de crédito Cuenta RUT A003
> asociadas; cuentas Cuenta con A004
> a la vista; cuentas provisión de fondos
> de provisión de Cuentas de ahorro Cuentas de ahorro A005
> fondos; y cuentas para la vivienda
> de ahorro Cuentas de ahorro A006
> con giro diferido
> Cuentas de ahorro A007
> con giro
> incondicional
> b) Tarjetas de Tarjeta de crédito B001
> crédito, con sus
> respectivas líneas
> de crédito
> asociadas
> c) Operaciones de Créditos C onsumo Crédito en cuotas C001
> crédito de dinero distintos de
> descuento por
> planilla
> Crédito en cuotas C002
> mediante
> descuento por
> planilla
> Líneas de crédito en C003
> cuenta corriente
> Otros créditos de C004
> consumo
> Hipotecario de Hipotecario en C005
> vivienda letras de crédito
> Mutuo hipotecario C006
> endosable
> Hipotecario C007
> comprado a ANAP
> Mutuo hipotecario C008
> no endosable
> Otros créditos C009
> hipotecarios
> Mutuos financiados C010
> con bonos
> hipotecarios
> Créditos C011
> complementarios
> de vivienda
> Comercial Adeudado por C012
> bancos
> Colocaciones C013
> comerciales
> Operaciones de C014
> factoring
> Leasing comercial C015
> Préstamos C016
> hipotecarios para
> fines generales
> Estudiantiles Préstamos C017
> estudiantiles Ley N°
> 20.027
> Préstamos C018
> estudiantiles con
> garantía CORFO
> Otros préstamos C019
> estudiantiles
> d) Pólizas de Vida Seguros Vida Entera D101
> seguro Individuales
> Temporal de Vida D102
> Seguros con Cuenta D103
> Única de Inversión
> (CUI)
> Mixto o Dotal D104
> Rentas Privadas y D105
> Otras Rentas
> Dotal puro o Capital D106
> Diferido
> Protección Familiar D107
> Incapacidad o D108
> Invalidez
> Salud D109
> Accidentes D110
> Personales
> Asistencia D111
> Desgravamen D112
> Hipotecario
> Desgravamen D113
> Consumos y Otros
> SOAP D114
> Otros D150
> Seguros Colectivos Vida Entera D201
> Tradicionales
> Temporal de Vida D202
> Seguros con Cuenta D203
> Única de inversión
> (CUI)
> Mixto o Dotal D204
> Rentas Privadas y D205
> Otras Rentas
> Dotal puro o Capital D206
> Diferido
> Protección Familiar D207
> Incapacidad o D208
> Invalidez
> Salud D209
> Accidentes D210
> Personales
> Asistencia D211
> Desgravamen D212
> Hipotecario
> Desgravamen D213
> Consumos y Otros
> SOAP D214
> Otros D250
> Seguros Banca Vida Entera D301
> Seguros y Retail
> Temporal de Vida D302
> Seguros con Cuenta D303
> Única de inversión
> (CUI)
> Mixto o Dotal D304
> Rentas Privadas y D305
> Otras Rentas
> Dotal puro o Capital D306
> Diferido
> Protección Familiar D307
> Incapacidad o D350
> Invalidez
> Salud D303
> Accidentes D303
> Personales
> Asistencia D303
> Desgravamen D303
> Hipotecario
> Desgravamen D303
> Consumos y Otros
> SOAP D303
> Otros D350
> Seguros Renta Vitalicia de D421
> Previsionales Vejez
> Renta Vitalicia de D421-1
> Vejez Normal
> Renta Vitalicia de D421-2
> Vejez Anticipada
> Renta Vitalicia D422
> Invalidez
> Renta Vitalicia de D422-1
> Invalidez Total
> Renta Vitalicia de D422-2
> Invalidez Parcial
> Renta Vitalicia de D423
> Sobrevivencia
> Seguro con Ahorro D424
> Previsional (APV)
> Seguro con Ahorro D425
> Previsional
> Colectivo (APVC)
> Generales Daños a los Bienes Incendio D001
> Pérdida de D002
> Beneficios por
> Incendio
> Otros Riesgos D003
> Adicionales a
> Incendio
> Terremoto y D004
> Tsunami
> Pérdida de D005
> Beneficios por
> Terremoto
> Otros Riesgo de la D006
> Naturaleza
> Terrorismo D007
> Robo D008
> Cristales D009
> Otros Daños a los Daños Físicos D010
> Bienes Vehículos
> Motorizados
> Casco Marítimo D011
> Casco Aéreo D012
> Responsabilidad Responsabilidad D013
> Civil Civil Hogar y
> Condominios
> Responsabilidad D014
> Civil Profesional
> Responsabilidad D015
> Civil Industria,
> Infraestructura y
> Comercio
> Responsabilidad D016
> Civil Vehículos
> Motorizados
> Transporte Transporte D017
> Terrestre
> Transporte D018
> Marítimo
> Transporte Aéreo D019
> Ingeniería Equipo Contratista D020
> Todo Riesgo D021
> Construcción y
> Montaje
> Avería de D022
> Maquinaria
> Equipo Electrónico D023
> Garantía y Crédito Garantía D024
> Fidelidad D025
> Seguro Extensión y D026
> Garantía
> Seguro de Crédito D027
> por Ventas a Plazo
> Seguro de Crédito a D028
> la Exportación
> Otros Seguros de D029
> Crédito
> Salud y Accidentes Salud D030
> Personales
> Accidentes D031
> Personales
> Seguro Obligatorio D032
> de Accidentes
> Personales (SOAP)
> Otros Seguros Seguro Cesantía D033
> Seguro de Título D034
> Seguro Agrícola D035
> Seguro de D036
> Asistencia
> Otros Seguros D050
> e) Instrumentos de Depósitos a plazo Plazo fijo E001
> ahorro o inversión Plazo renovable E002
> Plazo indefinido E003
> Fondos Mutuos Deuda de corto E101
> plazo con duración
> menor o igual a 90
> días
> Deuda de corto E102
> plazo con duración
> menor o igual a 365
> días
> Deuda de mediano E103
> y largo plazo
> Mixto E104
> De capitalización E105
> De libre inversión E106
> Estructurado E107
> Dirigido a E108
> inversionistas
> calificados
> Fondos de Rescatables E201
> Inversión
> No Rescatables E202
> APV Depósitos de E301
> Ahorro Previsional
> Voluntario
> Depósitos E302
> Convenidos
> f) Servicios de Operación de F001
> operación de tarjetas de pago
> tarjetas de pago
> g) Servicios de las Asesores de crédito G001
> entidades e inversión
> registradas como Plataforma de G002
> Prestadoras de financiamiento
> Servicios colectivo
> Financieros Sistemas G003
> alternativos de
> transacción
> Intermediación y G004
> custodia de
> instrumentos
> financieros
> Enrutamiento de G005
> órdenes"

### Cross-references
- Ley 21.521 Art. 24–26 — the data-sharing regime whose product taxonomy this annex codifies.
- NCG 514 §IV.A — Table N° 3, which references Annex N° 2 as the codification distinguishing the products reported in the system.
- NCG 514 §VI.4–§VI.7 — the data sets whose "Type of financial product"/"Type of account" variables resolve against these SFA codes.

> **Source:** NCG 514 §VI Annex N° 2 (03-jul-2024).

---

## VI.A3 — Annex N° 3: Technical Annex
**NCG anchor:** N° 514, Sección VI, Anexo N°3
**Implements:** Ley 21.521 Título III (technical specifications of the Open Finance System)
**Tags:** open-finance, technical-annex, reserved, por-definir

### Plain-English text

Annex N° 3 (Technical Annex / Anexo Técnico): To be defined (Por definir).

### Original Spanish

> "Anexo N°3: Anexo Técnico
> Por definir."

### Cross-references
- Ley 21.521 Título III — the Open Finance System regime whose technical specifications this reserved annex will contain.
- NCG 514 §V — the API specifications and technical standards to which a future Technical Annex would relate.

> **TN:** This annex is reserved in the source PDF as "Por definir" ("To be defined") with no substantive content as of the 03-jul-2024 version.

> **Source:** NCG 514 §VI Annex N° 3 (03-jul-2024).

---

## VI.A4 — Annex N° 4: Technical Specifications for the Distribution of Costs
**NCG anchor:** N° 514, Sección VI, Anexo N°4
**Implements:** Ley 21.521 Título III (cost-distribution specifications of the Open Finance System)
**Tags:** open-finance, cost-distribution, technical-specifications, reserved, por-definir

### Plain-English text

Annex N° 4 (Technical specifications for the distribution of costs / Especificaciones técnicas para la distribución de costos): To be defined (Por definir).

This annex is followed by the signature block of the regulation: Solange Michelle Berstein Jáuregui, Presidenta, Comisión para el Mercado Financiero.

### Original Spanish

> "Anexo N°4: Especificaciones técnicas para la distribución de costos
> Por definir.
> SOLANGE MICHELLE BERSTEIN JÁUREGUI
> PRESIDENTA
> COMISIÓN PARA EL MERCADO FINANCIERO"

### Cross-references
- Ley 21.521 Título III — the Open Finance System regime whose cost-distribution specifications this reserved annex will contain.

> **TN:** This annex is reserved in the source PDF as "Por definir" ("To be defined") with no substantive content as of the 03-jul-2024 version. The Spanish block also captures the closing signature block of the regulation on the same/following page.

> **Source:** NCG 514 §VI Annex N° 4 (03-jul-2024).

---
