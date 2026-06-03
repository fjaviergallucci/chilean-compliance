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
