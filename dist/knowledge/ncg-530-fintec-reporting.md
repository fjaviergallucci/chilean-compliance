<!-- GENERATED — do not edit by hand. Source: corpus/_agent-policy.md + corpus/. Regenerate: python -m tools.build_dist -->
# ncg-530-fintec-reporting

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

<!-- source: corpus/ncg/530-fintec-reporting/README.md -->
## FILE: corpus/ncg/530-fintec-reporting/README.md

# NCG 530 — Manual de Sistema de Información Fintec (MSI Fintec) — Reporting Obligations

**Issued:** 2025-01-20 by the Comisión para el Mercado Financiero (CMF). **In force:** 2026-01-01.
**Implements:** Ley 21.521 (Ley Fintec) Título II; NCG N° 502. References NCG N° 515 for the reporting channel.
**Source PDF:** `sources/ncg_530_2025-2.pdf`.

NCG 530 sets the periodic information that authorized financial-service providers
(PSF) registered in the RPSF must submit to the CMF: sixteen normative reporting
files (FINTEC01–FINTEC16), each owed by specific service types, plus the Manual del
Sistema de Información de Fintec (MSI Fintec) general instructions.

## Scope of this corpus (read carefully)
This corpus captures the **obligations layer**:
- the operative body (Secciones I–III): the FINTEC01–16 list, the MSI Fintec
  creation, and the entry into force;
- Anexo N°1 (MSI Fintec) **Sección I — Instrucciones Generales**: the reporting
  channel, fiscalization-report rules, data-type specifications, fixed-length
  record rules, and first-record structure;
- a derived catalog of the sixteen FINTEC files (`catalog-fintec-files.md`).

**OUT OF SCOPE:** Anexo N°2 (Compendio de Archivos Normativos — the field-by-field
record layouts of the sixteen files) and Anexo N°3 (Tablas y codificaciones — code
tables). These ~100 pages of structured reference data are not transcribed; consult
`sources/ncg_530_2025-2.pdf` (Anexos N°2 and N°3) for the exact record layouts and
codes.

## Section layout
- `seccion-01-obligations.md` — body Secciones I–III (FINTEC01–16; MSI Fintec creation; vigencia)
- `seccion-02-msi-instructions.md` — Anexo N°1, Sección I general instructions (arabic-numbered 1–4)
- `catalog-fintec-files.md` — derived table of the sixteen FINTEC files (code, name, obligated parties, periodicity, purpose)

## Citation convention
`NCG 530 §I` (body, Roman) and `NCG 530 §1`–`§4` (Anexo N°1 general instructions,
arabic). Each section's `> **Source:**` footer carries the 20-ene-2025 date.

## _law_ hint
_law:_ NCG-530

---

<!-- source: corpus/ncg/530-fintec-reporting/catalog-fintec-files.md -->
## FILE: corpus/ncg/530-fintec-reporting/catalog-fintec-files.md

# NCG 530 — FINTEC Reporting Files Catalog

Derived index of the sixteen normative reporting files defined by NCG 530 body
Sección I. The authoritative obligation text is in `seccion-01-obligations.md §I`
(round-trip-verified). The per-file **record layouts** (fields, types, lengths) are
**out of scope** — see `sources/ncg_530_2025-2.pdf` Anexo N°2.

_law:_ NCG-530

| Code | Name (EN) | Name (ES, verbatim) | Obligated service type(s) | Purpose |
|------|-----------|---------------------|---------------------------|---------|
| FINTEC01 | Volume, size, and nature of the business and number of clients | Volumen, tamaño y naturaleza del negocio y número de clientes | Intermediation, custody, order routing, crowdfunding, alternative trading systems, credit advisory, investment advisory | Business profile reporting |
| FINTEC02 | Minimum equity and guarantees | Patrimonio mínimo y garantías | Intermediation, custody, order routing | Minimum capital compliance |
| FINTEC03 | Equity requirement and assets weighted by operational risk | Requerimiento de patrimonio y activos ponderados por riesgo operacional | Intermediation, custody | Operational-risk capital reporting |
| FINTEC04 | Equity requirement and assets weighted by market risk | Requerimiento de patrimonio y activos ponderados por riesgo de mercado | Intermediation | Market-risk capital reporting |
| FINTEC05 | Equity requirement and assets weighted by credit risk | Requerimiento de patrimonio y activos ponderados por riesgo de crédito | Intermediation | Credit-risk capital reporting |
| FINTEC06 | Equity requirement and assets weighted by crypto-asset risk | Requerimiento de patrimonio y activos ponderados por riesgo de criptoactivos | Intermediation | Crypto-risk capital reporting |
| FINTEC07 | Transactions - Intermediaries | Transacciones - Intermediarios | Intermediation | Intermediary transaction reporting |
| FINTEC08 | Own-portfolio balance - Intermediaries | Saldo de cartera propia - Intermediarios | Intermediation | Intermediary proprietary holdings |
| FINTEC09 | Income and information, credit advisory | Ingresos e información, asesorías crediticias | Credit advisory | Credit-advisory income reporting |
| FINTEC10 | Income and information investment advisory | Ingresos e información asesorías de inversión | Investment advisory | Investment-advisory income reporting |
| FINTEC11 | Availability indicator, registry of financial-instrument transactions, and registry of financing operations | Indicador de disponibilidad, registro de transacciones de instrumentos financieros y registro de operaciones de financiamiento | Crowdfunding, custody, alternative trading systems | Availability and transaction registry |
| FINTEC12 | Registry of balances per client in custody | Registro de saldos por cliente en custodia | Custody | Per-client custody balances |
| FINTEC13 | Registry of reconciled cash in custody and registry of transfers to recover | Registro de efectivo en custodia conciliado y registro de transferencias por recuperar | Custody | Custody cash reconciliation |
| FINTEC14 | Disaggregated registry of executed transactions | Registro desagregado de transacción efectuadas | Block 3 alternative trading systems | Disaggregated executed transactions |
| FINTEC15 | General information on technological infrastructure and cybersecurity | Información general de infraestructura tecnológica y ciberseguridad | Block 2 and 3 alternative trading systems and custody | Tech infrastructure and cybersecurity |
| FINTEC16 | Own-portfolio balance - SAT | Saldo de cartera propia - SAT | Block 3 alternative trading systems | SAT proprietary holdings |

> **Source:** NCG 530 body §I (20-ene-2025). Record layouts: Anexo N°2 (out of scope).

---

<!-- source: corpus/ncg/530-fintec-reporting/seccion-01-obligations.md -->
## FILE: corpus/ncg/530-fintec-reporting/seccion-01-obligations.md

# NCG 530 — Información a Remitir y Manual MSI Fintec (Reporting Obligations)

**Regulation:** NCG 530 (Manual de Sistema de Información Fintec), 20-ene-2025.
_law:_ NCG-530

## I — Information to Submit
**NCG anchor:** N° 530, Sección I
**Implements:** Ley 21.521 Título II (services whose providers must report); NCG 502 (the registration/authorization regime being reported on)
**Tags:** reporting, fintec, normative-files, msi-fintec, rpsf

### Plain-English text

The entities registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) kept by the Commission for the Financial Market, and which hold the corresponding authorization to provide one or more of the services of Title II of Ley N° 21.521, must submit to this Commission, through the communication mechanisms provided for that purpose in the pertinent regulation, in the terms established in this regulation and in the Manual of the Fintec Information System (Manual de Sistema de información Fintec) (Anexo N°1), the following normative files, whose specific content is found in Anexo N°2, in accordance with the requirements established by type of authorized service:

**FINTEC01: Volume, size, and nature of the business and number of clients:** must be submitted by the providers of the services of intermediation of financial instruments, custody of financial instruments, order routing, crowdfunding platforms, alternative trading systems, credit advisory, and investment advisory, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC02: Minimum equity and guarantees:** must be submitted by the providers of the services of intermediation of financial instruments, custody of financial instruments, and order routing, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC03: Equity requirement and assets weighted by operational risk:** must be submitted by the providers of the services of intermediation of financial instruments and custody of financial instruments, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC04: Equity requirement and assets weighted by market risk:** must be submitted by the providers of the services of intermediation of financial instruments, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC05: Equity requirement and assets weighted by credit risk:** must be submitted by the providers of the services of intermediation of financial instruments, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC06: Equity requirement and assets weighted by crypto-asset risk:** must be submitted by the providers of the services of intermediation of financial instruments, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC07: Transactions - Intermediaries:** must be submitted by the providers of the services of intermediation of financial instruments, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC08: Own-portfolio balance - Intermediaries:** must be submitted by the providers of the services of intermediation of financial instruments, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC09: Income and information, credit advisory:** must be submitted by the providers of the credit-advisory services, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC10: Income and information investment advisory:** must be submitted by the providers of the investment-advisory services, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC11: Availability indicator, registry of financial-instrument transactions, and registry of financing operations:** must be submitted by the providers of the services of crowdfunding platforms, custody-of-financial-instruments services, and alternative trading systems regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC12: Registry of balances per client in custody:** must be submitted by the providers of the custody-of-financial-instruments services, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC13: Registry of reconciled cash in custody and registry of transfers to recover:** must be submitted by the providers of the custody-of-financial-instruments services, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC14: Disaggregated registry of executed transactions:** must be submitted by the providers of the block 3 alternative trading systems services, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC15: General information on technological infrastructure and cybersecurity:** must be submitted by the providers of the alternative trading systems services and custody-of-financial-instruments services, both classified in blocks 2 and 3, regulated by Ley N° 21.521 and authorized by this Commission.

**FINTEC16: Own-portfolio balance - SAT:** must be submitted by the providers of the alternative trading systems services classified in block 3, regulated by Ley N° 21.521 and authorized by this Commission.

The entities that provide services regulated by Title II of Ley 21.521 that are not required to be registered in the Registry of Financial-Service Providers, pursuant to the provisions of Article 5 of Ley N° 21.521, or that are exempted from applying for authorization and from complying with the provisions of NCG N°502, shall not submit to this Commission the normative files established in Anexo N°2.

### Original Spanish

> "I INFORMACIÓN A REMITIR
>
> Las entidades inscritas en el Registro de Prestadores de Servicios Financieros que lleva la Comisión para el Mercado Financiero, y que cuentan con la autorización correspondiente para prestar uno o más de los servicios del Título II de la Ley N°21.521, deberán remitir a esta Comisión, a través de los mecanismos de comunicación dispuestos para ello en la normativa pertinente, en los términos establecidos en la presente normativa y en el Manual de Sistema de información Fintec (Anexo N°1), los siguientes archivos normativos, cuyo contenido específico se encuentra en el Anexo N°2, de acuerdo a las exigencias establecidas por tipo de servicio autorizado:
>
> FINTEC01: Volumen, tamaño y naturaleza del negocio y número de clientes: debe ser remitido por los prestadores de servicios de intermediación de instrumentos financieros, custodia de instrumentos financieros, enrutamiento de órdenes, plataformas de financiamiento colectivo, sistemas alternativos de transacción, asesoría crediticia y asesoría de inversión, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC02: Patrimonio mínimo y garantías: debe ser remitido por los prestadores de servicios de intermediación de instrumentos financieros, custodia de instrumentos financieros y enrutamiento de órdenes, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC03: Requerimiento de patrimonio y activos ponderados por riesgo operacional: debe ser remitido por los prestadores de servicios de intermediación de instrumentos financieros y custodia de instrumentos financieros, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC04: Requerimiento de patrimonio y activos ponderados por riesgo de mercado: debe ser remitido por los prestadores de servicios de intermediación de instrumentos financieros, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC05: Requerimiento de patrimonio y activos ponderados por riesgo de crédito: debe ser remitido por los prestadores de servicios de intermediación de instrumentos financieros, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC06: Requerimiento de patrimonio y activos ponderados por riesgo de criptoactivos: debe ser remitido por los prestadores de servicios de intermediación de instrumentos financieros, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC07: Transacciones - Intermediarios: debe ser remitido por los prestadores de servicios de intermediación de instrumentos financieros, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC08: Saldo de cartera propia - Intermediarios: debe ser remitido por los prestadores de servicios de intermediación de instrumentos financieros, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC09: Ingresos e información, asesorías crediticias: debe ser remitido por los prestadores de servicios de asesoría crediticia, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC10: Ingresos e información asesorías de inversión: debe ser remitido por los prestadores de servicios de asesoría de inversión, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC11: Indicador de disponibilidad, registro de transacciones de instrumentos financieros y registro de operaciones de financiamiento: debe ser remitido por los prestadores de servicios de plataformas de financiamiento colectivo, servicios de custodia de instrumentos financieros y sistemas alternativos de transacción regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC12: Registro de saldos por cliente en custodia: debe ser remitido por los prestadores de servicios de custodia de instrumentos financieros, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC13: Registro de efectivo en custodia conciliado y registro de transferencias por recuperar: debe ser remitido por los prestadores de servicios de custodia de instrumentos financieros, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC14: Registro desagregado de transacción efectuadas: debe ser remitido por los prestadores de servicios de sistemas alternativos de transacciones del bloque 3, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC15: Información general de infraestructura tecnológica y ciberseguridad: debe ser remitido por los prestadores de servicios de sistemas alternativos de transacciones y servicios de custodia de los instrumentos financieros, ambos clasificados en el bloque 2 y 3, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> FINTEC16: Saldo de cartera propia - SAT: debe ser remitido por los prestadores de servicios de sistemas alternativos de transacciones clasificado en el bloque 3, regulados por la Ley N°21.521 y autorizados por esta Comisión.
>
> Las entidades que prestan servicios regulados por el Título II de la ley 21.521 que no requieren estar inscritos en el Registro de Prestadores de Servicios Financieros, conforme a lo dispuesto en el artículo 5 de la Ley N°21.521, o que estén exceptuados de solicitar autorización y de cumplir las disposiciones de la NCG N°502, no deberán remitir a esta Comisión los archivos normativos establecidos en el Anexo N°2."

### Cross-references
- NCG 502 §I.A — the registration/authorization regime in the Registry of Financial-Service Providers whose obligated entities must submit these files; see `../502-psf-obligations-consolidated/seccion-01-registro.md`.
- Ley 21.521 Art. 5 — the registration obligation under Title II that determines which entities report; see `../../21521-fintech/titulo-02-servicios.md`.

> **Source:** NCG 530 §I (20-ene-2025, in force 01-ene-2026).

---

## II — Manual of the Fintec Information System (MSI Fintec)
**NCG anchor:** N° 530, Sección II
**Implements:** Ley 21.521 Título II; NCG 502
**Tags:** msi-fintec, manual, normative-files, anexo

### Plain-English text

For the purpose of systematizing the instructions for the periodic submission of information to this Commission by the entities registered in the Registry of Financial-Service Providers kept by the CMF, and which hold the corresponding authorization to provide one or more of the services of Title II of Ley N° 21.521, the following is established:

1.- The "Manual of the Fintec Information System" (Manual de Sistema de Información Fintec), hereinafter MSI Fintec, shall be created, which shall contain the instructions for the preparation and submission of the files, tables, and any other component referring to information to be submitted to this Commission, and which shall be structured in accordance with Anexo N°1 of this regulation.

2.- The normative files "FINTEC01", "FINTEC02", "FINTEC03", "FINTEC04", "FINTEC05", "FINTEC06", "FINTEC07", "FINTEC08", "FINTEC09", "FINTEC10", "FINTEC11", "FINTEC12", "FINTEC13", "FINTEC14", "FINTEC15", and "FINTEC16", which are included in Anexo N°2 of this regulation, shall be incorporated into the second Subsection of Section II of the "Manual of the Fintec Information System" called "Compendium of Fintec Normative Files" (Compendio de Archivos Normativos Fintec).

3.- The tables that are included in Anexo N°3 of this regulation shall be incorporated into the second subsection of Section III of the "Manual of the Fintec Information System", called "Tables and codifications of the Fintec Information System" (Tablas y codificaciones del Sistema de Información Fintec).

### Original Spanish

> "II MANUAL DE SISTEMA DE INFORMACIÓN FINTEC (MSI FINTEC)
>
> Con la finalidad de sistematizar las instrucciones de envío de información periódica a esta Comisión por parte de las entidades inscritas en el Registro de Prestadores de Servicios Financieros que lleva la CMF, y que cuentan con la autorización correspondiente para prestar uno o más de los servicios del Título II de la Ley N°21.521, se establece lo siguiente:
>
> 1.- Créase el “Manual de Sistema de Información Fintec” en adelante MSI Fintec, el que contendrá las instrucciones para la confección y envío de los archivos, tablas y cualquier otro componente que se refiera a información a ser remitida a esta Comisión, el que se estructurará de acuerdo con el Anexo N°1 de esta normativa.
>
> 2.- Incorpórese los archivos normativos “FINTEC01”, “FINTEC02”, “FINTEC03”, “FINTEC04”, “FINTEC05”, “FINTEC06”, “FINTEC07”, “FINTEC08”, “FINTEC09”, “FINTEC10”, “FINTEC11”, “FINTEC12”, “FINTEC13”, “FINTEC14”, “FINTEC15” y “FINTEC16”, que se incluyen en el Anexo N°2 de esta normativa, en la segunda Subsección de la Sección II del “Manual de Sistema de Información Fintec” denominado “Compendio de Archivos Normativos Fintec”.
>
> 3.- Incorpórese las tablas que se incluyen en el Anexo N°3 de esta normativa, en la segunda subsección de la Sección III del “Manual de Sistema de Información Fintec”, denominada “Tablas y codificaciones del Sistema de Información Fintec”."

### Cross-references
- NCG 530 §I — the FINTEC01–FINTEC16 files that this section incorporates into the MSI Fintec.
- Ley 21.521 Art. 4 — the CMF's normative powers under which the MSI Fintec is created; see `../../21521-fintech/titulo-02-servicios.md`.

> **Source:** NCG 530 §II (20-ene-2025, in force 01-ene-2026).

---

## III — Entry into Force
**NCG anchor:** N° 530, Sección III
**Implements:** Ley 21.521 Título II
**Tags:** vigencia, entry-into-force

### Plain-English text

These instructions shall be in force as from 1 January 2026.

### Original Spanish

> "III VIGENCIA
>
> Las presentes instrucciones rigen a partir del 1 de enero de 2026."

### Cross-references
- NCG 530 §I–§II — the obligations that enter into force on the date stated here.

> **Source:** NCG 530 §III (20-ene-2025, in force 01-ene-2026).

---

<!-- source: corpus/ncg/530-fintec-reporting/seccion-02-msi-instructions.md -->
## FILE: corpus/ncg/530-fintec-reporting/seccion-02-msi-instructions.md

# NCG 530 — Anexo N°1: MSI Fintec General Instructions

**Regulation:** NCG 530, Anexo N°1 (Manual del Sistema de Información de Fintec), Sección I — Instrucciones Generales, 20-ene-2025.
_law:_ NCG-530

> **Scope note:** Anexo N°1 Sección II (Archivos Normativos) and Anexos N°2/N°3 (the
> per-file record layouts and code tables) are out of scope; see
> `sources/ncg_530_2025-2.pdf`.

## 1 — Official Communication and Submission Channel
**NCG anchor:** N° 530, Anexo N°1, Sección I, N° 1
**Implements:** Ley 21.521 Título II; NCG 502; references NCG 515 (reporting channel)
**Tags:** msi-fintec, submission-channel, cmf-supervisa, ncg-515

### Plain-English text

The information must be submitted through the respective application of the official channel of communication and submission of information between the Commission and its supervised entities "CMF Supervisa" provided for that purpose on this Commission's website (www.cmfchile.cl), in accordance with the provisions established for that purpose in NCG N°515, or the one that replaces it.

### Original Spanish

> "CANAL OFICIAL DE COMUNICACIÓN Y ENVÍO DE INFORMACIÓN ENTRE LA COMISIÓN Y SUS FISCALIZADOS
>
> La información debe ser remitida a través de la respectiva aplicación del canal oficial de comunicación y envío de información entre la Comisión y sus fiscalizados “CMF Supervisa” dispuesto en el sitio web de esta Comisión (www.cmfchile.cl), de acuerdo a lo establecido al efecto en la NCG N°515, o el que lo reemplace."

### Cross-references
- NCG 515 — establishes the "CMF Supervisa" official channel through which the files are submitted.
- NCG 502 §I.A — the registry/authorization regime applicable to the supervised entities.

> **Source:** NCG 530 §1 (20-ene-2025, in force 01-ene-2026).

---

## 2 — Fiscalization Reporting
**NCG anchor:** N° 530, Anexo N°1, Sección I, N° 2
**Implements:** Ley 21.521 Título II; NCG 502
**Tags:** msi-fintec, reporting, deadlines, fiscalization

### Plain-English text

The supervised entity must submit the requested information within the deadline indicated for each file. The file must contain the individualization of each of the requested records and fields. In the event that the supervised entity does not have information for a specific record for a period to be reported, it must not send that record and, in its place, must report the value "0" in the row of the record corresponding to the Squaring Cover Sheet (Carátula de Cuadratura) of the respective Fintec file.

The deadline for the delivery of the normative files is specified in each one of them and must be counted as from the last day of the period that will be reported.

### Original Spanish

> "REPORTE DE INFORMACIÓN DE FISCALIZACIÓN
>
> La entidad fiscalizada deberá remitir la información solicitada dentro del plazo indicado para cada archivo. El archivo deberá contener la individualización de cada uno de los registros y campos requeridos. En caso de que la entidad fiscalizada no disponga de información para un registro específico para un período a reportar, no deberá enviar el dicho registro y, en su lugar, deberá reportar el valor “0” en la fila del registro correspondiente de la Carátula de Cuadratura del archivo Fintec respectivo.
>
> El plazo para la entrega de los archivos normativos está especificado en cada uno de ellos y debe contarse a partir del último día del período que será reportado."

### Cross-references
- NCG 530 §I — the FINTEC files whose per-file deadlines govern the reporting described here.

> **Source:** NCG 530 §2 (20-ene-2025, in force 01-ene-2026).

---

## 3 — Content Specifications of the Files
**NCG anchor:** N° 530, Anexo N°1, Sección I, N° 3
**Implements:** Ley 21.521 Título II; NCG 502
**Tags:** msi-fintec, data-types, record-format, file-structure

### Plain-English text

**Definition of data types**

The data types used in the text files (that is, plain-text txt files) are structured in accordance with the following table:

| Data type | Specification | Physical representation |
|---|---|---|
| RUT | R (09) VX(01) | NNNNNNNNNå |
| Dates (Fechas) | F(08) | AAAAMMDD |
| Periods (Periodos) | P(06) | AAAAMM |
| Numeric (Numérico) | 9(n) | N…N (string of n digits) Adjust to the right and fill with zeros |
| Character (Carácter) | X(n) | å…å (string of n characters) Adjust to the left and fill with blanks (spaces) |
| Numeric with sign (Numérico con signo) | S9(n) | N…Ns (string of n digits with sign) Sign is "trailing separate" |
| Numeric with decimal (Numérico con decimal) | 9(n)V9(m) | N…N,N…N (number of n digits for the integer figure and m decimals) |

Where: A: year (año); M: month (mes); D: day (día); N: numeral (0 …9); å: alphanumeric (alfanuméricos); S: sign +ó- (signo +ó-).

**Length of the records**

The files are fixed-length record files, so that the first record and, in certain cases, also other records of the file shall have a filler to complete the length.

**First record**

The first record shall always contain the datum that identifies the entity, the file type, and the period date to which the information refers. In general, unless otherwise indicated in the respective instructions, the first record shall have the following structure:

1. Entity code … 9(10)
2. File identification … X(08)
3. Period … P(06) or F(08)
4. Filler … x(…)

### Original Spanish

> "ESPECIFICACIONES DEL CONTENIDO DE LOS ARCHIVOS
>
> Definición de tipos de datos
> Los tipos de datos usados en los archivos de texto (es decir, archivos de texto plano txt) se estructuran conforme a la siguiente tabla:
>
> Largo de los registros
> Los archivos son de registros de largo fijo, por lo que el primer registro y, en ciertos casos, también otros registros del archivo tendrán un filler para completar el largo.
>
> Primer registro
> El primer registro contendrá siempre el dato que identifica a la entidad, el tipo de archivo y la fecha período a que se refiere la información. En general, salvo que se indique otra cosa en las respectivas instrucciones, el primer registro tendrá la siguiente estructura:
> 1. Código de la entidad ............................................................. 9(10)
> 2. Identificación del archivo ........................................................ X(08)
> 3. Período ............................................................................. P(06) o F(08)
> 4. Filler ................................................................................. x(…)"

> **TN:** The data-type specification table is rendered in the English text; its tabular cell values are not reproduced in this Original Spanish block.

### Cross-references
- NCG 530 §4 — the padding and formatting rules that complement these content specifications.

> **Source:** NCG 530 §3 (20-ene-2025, in force 01-ene-2026).

---

## 4 — Information Requirement
**NCG anchor:** N° 530, Anexo N°1, Sección I, N° 4
**Implements:** Ley 21.521 Título II; NCG 502
**Tags:** msi-fintec, padding, formatting, numeric-format, date-format

### Plain-English text

In the event that the field has a length shorter than the one specified in the respective file, it must be completed with space characters at the end -for those fields whose format is alphanumeric-, or by prepending zeros for fields of numeric format, so as to complete in this way the length requested in the field in question.

In the case of decimal numbers, the integer part must be completed with zeros to the left, and the decimal part, with zeros at the end of the field. This criterion must also be followed in the event that there is no information for the field, for which it must be completed with spaces or zeros according to the format of the field up to completing its length.

The numeric values must be reported without thousands or decimal separators, unless specifically indicated otherwise for a particular field. The dates must be reported in accordance with the format provided in the description of the respective field.

### Original Spanish

> "REQUERIMIENTO DE INFORMACIÓN.
>
> En caso de que el campo cuente con una longitud menor a la especificada en el respectivo archivo, se deberá completar con caracteres de espacio al final -para aquellos campos cuyo formato sea alfanumérico-, o anteponer ceros para los campos de formato numérico, para completar de este modo la longitud solicitada en el campo en cuestión.
>
> En caso de números decimales, la parte entera se deberá completar con ceros a la izquierda, y la parte decimal, con ceros al final del campo. También se deberá seguir este criterio en caso de que no se cuente con información para el campo, para lo cual se deberá completar con espacios o ceros según el formato del campo hasta completar su longitud.
>
> Los valores numéricos deberán informarse sin separadores de miles ni decimales, salvo que se indique específicamente lo contrario para un campo en particular. Las fechas deberán informarse de acuerdo con el formato dispuesto en la descripción del campo respectivo."

### Cross-references
- NCG 530 §3 — the data-type and record-structure specifications to which these padding rules apply.

> **Source:** NCG 530 §4 (20-ene-2025, in force 01-ene-2026).

---
