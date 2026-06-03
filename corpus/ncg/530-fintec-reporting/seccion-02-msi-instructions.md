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
