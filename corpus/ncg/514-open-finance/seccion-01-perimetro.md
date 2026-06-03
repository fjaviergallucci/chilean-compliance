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
