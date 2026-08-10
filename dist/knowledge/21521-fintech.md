<!-- GENERATED — do not edit by hand. Source: corpus/_agent-policy.md + corpus/. Regenerate: python -m tools.build_dist -->
# 21521-fintech

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

<!-- source: corpus/21521-fintech/README.md -->
## FILE: corpus/21521-fintech/README.md

# Ley 21.521 — Promotes Competition and Financial Inclusion through Innovation and Technology (Ley Fintec)

**Published:** 2023-01-04
**Promulgated:** 2022-12-22
**Single version in force from:** 2023-02-03
**Issuing body:** Ministerio de Hacienda
**Source PDF:** `sources/Ley-21521_04-ENE-2023-1.pdf`
**Corpus status:** see `.claude-plugin/plugin.json` → `corpus_status.21521_fintech`

## Scope (summary)
Regulates the commercial provision of: crowdfunding platforms, alternative
trading systems, credit advisory, investment advisory, custody of financial
instruments, order routing, and intermediation of financial instruments.
Supervised by the Commission for the Financial Market (CMF).

## File layout
- `titulo-NN-<slug>.md` — one file per Título, in source order.
- Each article: `## Article N` H2 anchor, English-first text, then `### Original Spanish` block.

## Citation convention
`Ley 21.521 Art. N(letter)(num)` — e.g., `Art. 3(2)` for the investment-advisory definition.

## Effective-date discipline
This law has been in force since 2023-02-03. No staged provisions.

## Títulos in this law

- **Título I** — Disposiciones generales
- **Título II** — Servicios financieros basados en tecnología
- **Título III** — Del Sistema de Finanzas Abiertas
- **Título IV** — Otras disposiciones
- **Título V** — Modificaciones a otros cuerpos normativos

---

<!-- source: corpus/21521-fintech/titulo-01-general.md -->
## FILE: corpus/21521-fintech/titulo-01-general.md

# Ley 21.521 — Título I: General Provisions (Disposiciones generales)

**Law:** Ley 21.521 (in force 2023-02-03)
_law:_ 21.521

## Article 1 — Objectives of the law and principles
**Spanish anchor:** Art. 1°
**Tags:** scope, principles, supervision

### Plain-English text

This law (ley) is intended to establish a general framework to incentivize the provision (prestación) of financial services (servicios financieros) through technological means by the providers (proveedores) governed by it.

This law is founded on the principles (principios) of financial inclusion and innovation, promotion of competition, protection of the financial customer, adequate safeguarding of processed data, preservation of financial integrity and stability, and prevention of money laundering (lavado de activos) and the financing of drug trafficking (narcotráfico) and terrorism. These principles must be observed by all persons bound by this law (sujetos obligados por ella).

The provision of the services referred to above shall be subject to the supervision (fiscalización) of the Commission for the Financial Market (Comisión para el Mercado Financiero, hereinafter "Commission (CMF)"), which shall have all the powers conferred on it by Decree-Law No. 3.538 of 1980, for the purpose of overseeing compliance with the provisions of this law. In issuing the regulations (normativa) that the Commission (CMF) promulgates for the implementation of this law, it must observe the principles of risk-based proportionality (proporcionalidad basada en riesgos), modularity in services rendered (modularidad en los servicios prestados), and technological neutrality (neutralidad tecnológica).

> **TN:** "dictación de la normativa" is rendered as "issuing the regulations" (rather than literally "the dictation of the regulation") to convey CMF's formal rulemaking act in plain English. "Dictación" is a Chilean legal term of art for the formal promulgation of secondary-level rules; the functional English equivalent is "issuance" or "promulgation." The lexicon maps "normativa de carácter general" to "general regulation (CMF rulemaking)"; here the text uses the shorter form "normativa" in context of implementation rulemaking, so "regulations" is used without the parenthetical qualifier. The verb "efectúe" later in the same paragraph is similarly rendered as "promulgates" for consistency in this register.

> **TN:** "sujetos obligados por ella" is rendered as "persons bound by this law" rather than the more literal "obligated subjects" to align with standard common-law drafting style. The Spanish term covers both natural persons (personas naturales) and legal persons (personas jurídicas).

### Original Spanish

> Artículo 1.- Objetivos de la ley y principios. Esta ley tiene por objeto
> establecer un marco general para incentivar la prestación de servicios financieros a
> través de medios tecnológicos que realicen los proveedores regidos por ella.
>
> Esta ley está basada en los principios de inclusión e innovación financiera,
> promoción de la competencia, protección al cliente financiero, adecuado resguardo
> de los datos tratados, preservación de la integridad y estabilidad financiera y
> prevención del lavado de activos y financiamiento del narcotráfico y del
> terrorismo, los cuales deberán ser observados por todos los sujetos obligados por
> ella.
>
> La prestación de los servicios señalados quedará sometida a la fiscalización
> de la Comisión para el Mercado Financiero, la que dispondrá de todas las facultades
> que le confiere el decreto ley N° 3.538, de 1980, para efectos de vigilar el
> cumplimiento de las disposiciones de la presente ley. En la dictación de la
> normativa que la Comisión efectúe para su implementación, deberá observar los
> principios de proporcionalidad basada en riesgos, modularidad en los servicios
> prestados y neutralidad tecnológica.

### Cross-references
- Defined "Comisión" → Art. 3(4) (see `titulo-02-services.md` once translated).
- Supervisory framework references → Art. 4 (CMF normativa de carácter general).

---

<!-- source: corpus/21521-fintech/titulo-02-servicios.md -->
## FILE: corpus/21521-fintech/titulo-02-servicios.md

# Ley 21.521 — Título II: Technology-Based Financial Services (Servicios financieros basados en tecnología)

**Law:** Ley 21.521 (in force 2023-02-03)
_law:_ 21.521

## Article 2 — Scope and supervision
**Spanish anchor:** Art. 2°
**Tags:** scope, supervision, registration

### Plain-English text

This Title (título) regulates the marketing of the following services:

a) Crowdfunding platforms (plataformas de financiamiento colectivo).
b) Alternative trading systems (sistemas alternativos de transacción).
c) Credit advisory (asesoría crediticia) and investment advisory (asesoría de inversión).
d) Custody of financial instruments (custodia de instrumentos financieros).
e) Order routing (enrutamiento de órdenes) and intermediation of financial instruments (intermediación de instrumentos financieros).

It shall be the responsibility of (corresponderá a) the Commission for the Financial Market (Comisión para el Mercado Financiero, hereinafter "Commission (CMF)") to supervise (fiscalizar) the provision of the services listed above. To that end it shall have the powers conferred on it by this law and its organic law (ley orgánica), including the authority to adopt such preventive or corrective measures as may be deemed necessary for the proper protection of investors. For these purposes, the Commission (CMF) may require entities registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) — by means of a general regulation (norma de carácter general) — to submit such information as is necessary to supervise compliance with this law, at the frequency, in the form, and through the medium established by such regulation.

### Original Spanish

> Artículo 2.- Alcance y fiscalización. El presente título regula la
> comercialización de los siguientes servicios:
>
> a) Plataformas de financiamiento colectivo.
> b) Sistemas alternativos de transacción.
> c) Asesoría crediticia y de inversión.
> d) Custodia de instrumentos financieros.
> e) Enrutamiento de órdenes e intermediación de instrumentos financieros.
>
> Corresponderá a la Comisión para el Mercado Financiero fiscalizar la
> prestación de los servicios antes indicados. Para ello contará con las atribuciones
> que le confieren esta ley y su ley orgánica, incluyendo la facultad de adoptar las
> medidas preventivas o correctivas que se estimen necesarias para el debido resguardo
> de los inversionistas. Para estos efectos, la Comisión podrá exigir a las entidades
> inscritas en el Registro de Prestadores de Servicios Financieros, mediante norma de
> carácter general, que le remitan aquella información que sea necesaria para
> fiscalizar el cumplimiento de la presente ley, en la periodicidad, forma y medio que
> establezca dicha normativa.

### Cross-references
- Defined terms for each service listed here → Art. 3 (definitions).
- Registry of Financial-Service Providers → Art. 3(12), Art. 5.
- General regulation powers → Art. 4.

---

## Article 3 — Definitions
**Spanish anchor:** Art. 3°
**Tags:** definitions, crowdfunding, alternative-trading, credit-advisory, investment-advisory, custody, order-routing, intermediation

### Plain-English text

For the purposes of this law, the following terms shall mean:

1. **Credit advisory** (asesoría crediticia): the provision of evaluation or recommendation services to third parties regarding the capacity or probability of payment of natural persons (personas naturales) and legal persons (personas jurídicas) or entities, or their identity, for the purpose of obtaining, modifying, or renegotiating a credit or financing arrangement.

2. **Investment advisory** (asesoría de inversión): the provision of evaluation or recommendation services to third parties regarding the advisability of making certain investments or transactions in publicly offered securities (valores de oferta pública), financial instruments (instrumentos financieros), or investment projects (proyectos de inversión). This does not include pension advisory services, pension advisory entities, pension financial advisors, or financial advisory entities covered by Decree-Law No. 3.500 of 1980, nor insurance company sales agents.

3. **Virtual financial assets** (activos financieros virtuales) or crypto-assets (criptoactivos): digital representations of units of value, goods, or services — other than money, whether in domestic currency or foreign exchange — that can be transferred, stored, or exchanged digitally.

4. **Commission** (Comisión): the Commission for the Financial Market (Comisión para el Mercado Financiero).

5. **Custody of financial instruments** (custodia de instrumentos financieros): holding in one's own name on behalf of third parties, or in the name of those third parties, financial instruments (instrumentos financieros), money, or foreign exchange arising from the flows or disposal of financial instruments held in custody, or delivered by those third parties for the acquisition of financial instruments or to secure transactions in those instruments.

6. **Order routing** (enrutamiento de órdenes): the service of channelling orders received from third parties for the purchase or sale of publicly offered securities (valores de oferta pública) or financial instruments (instrumentos financieros) to alternative trading systems (sistemas alternativos de transacción), securities intermediaries (intermediarios de valores), or commodity-exchange brokers (corredores de bolsas de productos).

7. **Fintech** (Fintec): activities that involve the use and application of innovation and technological developments for the design, offering, and provision of financial products and services.

> **TN:** The law spells this "Fintec" (one final "h") throughout the Spanish text. The English rendering "Fintech" is used as the standard international form; the Spanish spelling is preserved in the Original Spanish block.

8. **Financial instrument** (instrumento financiero): any security, contract, document, or intangible asset designed, employed, or structured with the purpose of generating monetary income, or representing an outstanding debt or a virtual financial asset. For the purposes of this law, financial instruments shall include securities not registered in the Securities and Foreign Securities Registry of Law No. 18.045, derivative contracts, contracts for difference, invoices (facturas), among others, regardless of whether their medium is physical or electronic. For the purposes of this law, financial instruments shall NOT include publicly offered securities; nor money or foreign exchange, regardless of whether their medium is physical or digital.

9. **Intermediation of financial instruments** (intermediación de instrumentos financieros): a service whereby activities of buying or selling financial instruments (instrumentos financieros) are carried out for third parties, by any of the following means: acquiring or disposing of financial instruments in one's own name, with the prior intention of selling or buying those same instruments to or from the third party; or acquiring or selling financial instruments in the name of, or on behalf of, said third party.

10. **Crowdfunding platform** (plataforma de financiamiento colectivo): a physical or virtual venue through which those who have investment projects (proyectos de inversión) or financing needs disseminate, communicate, offer, or promote those projects or needs, or their characteristics, and make contact with — or obtain contact information of — those who have available resources or the intention to participate in or meet those projects or needs; in order to facilitate the materialisation of the financing transaction.

11. **Investment project** (proyecto de inversión): an initiative intended to generate (tiene por finalidad la generación de) interest, profits, or monetary consideration for those who contribute to its financing.

> **TN:** "tener por finalidad" is rendered as "is intended to" by analogy with the lexicon convention for "tener por objeto" (which maps to "is intended to"). The two purpose-object formulations are functionally equivalent in Chilean legislative drafting; no separate lexicon entry exists yet for "tener por finalidad".

12. **Registry** (Registro): the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros).

13. **Alternative trading system** (sistema alternativo de transacción): a physical or virtual venue that allows its participants to quote, offer, or trade financial instruments (instrumentos financieros) or publicly offered securities (valores de oferta pública), and that is not authorised to act as a stock exchange under Law No. 18.045 or as a commodity exchange under Law No. 19.220.

### Original Spanish

> Artículo 3.- Definiciones. Para efectos de la presente ley, se entenderá por:
>
> 1. Asesoría crediticia: la prestación de servicios de evaluaciones o
> recomendaciones a terceros respecto de la capacidad o probabilidad de pago de
> personas naturales y jurídicas o entidades, o de la identidad de éstas, para fines
> de la obtención, modificación o renegociación de un crédito o financiamiento.
>
> 2. Asesoría de inversión: la prestación de servicios de evaluaciones o
> recomendaciones a terceros respecto de la conveniencia de realizar determinadas
> inversiones u operaciones en valores de oferta pública, instrumentos financieros o
> proyectos de inversión. No comprende la asesoría previsional, entidades de
> asesoría previsional, asesores financieros previsionales o entidades de asesoría
> financiera a que se refiere el decreto ley N° 3.500, de 1980, ni los agentes de
> venta de compañías de seguros.
>
> 3. Activos financieros virtuales o criptoactivos: representación digital de
> unidades de valor, bienes o servicios, con excepción de dinero, ya sea en moneda
> nacional o divisas, que pueden ser transferidos, almacenados o intercambiados
> digitalmente.
>
> 4. Comisión: Comisión para el Mercado Financiero.
>
> 5. Custodia de instrumentos financieros: mantener a nombre propio por cuenta de
> terceros, o a nombre de éstos, instrumentos financieros, dinero o divisas que
> provengan de los flujos o de la enajenación de instrumentos financieros mantenidos
> en custodia, o que hayan sido entregados por éstos para la adquisición de
> instrumentos financieros o para garantizar las operaciones con esos instrumentos.
>
> 6. Enrutamiento de órdenes: servicio de canalización de órdenes recibidas de
> terceros para la compra o venta de valores de oferta pública o instrumentos
> financieros a sistemas alternativos de transacción, intermediarios de valores o
> corredores de bolsas de productos.
>
> 7. Fintec: actividades que impliquen el uso y aplicación de la innovación y
> los desarrollos tecnológicos para el diseño, oferta y prestación de productos y
> servicios financieros.
>
> 8. Instrumento financiero: todo título, contrato, documento o bien incorporal,
> diseñado, empleado o estructurado con la finalidad de generar rentas monetarias, o
> representar una deuda insoluta o un activo financiero virtual. Se considerarán
> instrumentos financieros para los efectos de esta ley los valores no inscritos en el
> Registro de Valores y de Valores Extranjeros de la ley N° 18.045, contratos
> derivados, contratos por diferencia, facturas, entre otros, independiente de si su
> soporte es físico o electrónico. No serán considerados instrumentos financieros
> para los efectos de esta ley, los valores de oferta pública; ni el dinero o divisas,
> independiente de si su soporte es físico o digital.
>
> 9. Intermediación de instrumentos financieros: servicio en virtud del cual se
> realizan actividades de compra o venta de instrumentos financieros para terceros,
> mediante cualquiera de las siguientes formas: adquiriendo o enajenando por cuenta
> propia instrumentos financieros, con el ánimo anterior de vender o comprar esos
> mismos instrumentos al tercero, o adquiriendo o vendiendo instrumentos financieros a
> nombre de o para dicho tercero.
>
> 10. Plataforma de financiamiento colectivo: lugar físico o virtual por medio
> del cual quienes tienen proyectos de inversión o necesidades de financiamiento
> difunden, comunican, ofertan o promocionan esos proyectos o necesidades, o las
> características de éstos, y se contactan u obtienen información de contacto de
> quienes cuentan con recursos disponibles o la intención de participar en esos
> proyectos o necesidades o satisfacerlos; a fin de facilitar la materialización de la
> operación de financiamiento.
>
> 11. Proyecto de inversión: aquella iniciativa que tiene por finalidad la
> generación de intereses, utilidades o contraprestaciones pecuniarias para quienes
> contribuyan a su financiamiento.
>
> 12. Registro: Registro de Prestadores de Servicios Financieros.
>
> 13. Sistema alternativo de transacción: lugar físico o virtual que permite a
> sus participantes cotizar, ofrecer o transar instrumentos financieros o valores de
> oferta pública, y que no está autorizado para actuar como bolsa de valores de
> acuerdo con la ley N° 18.045 o como bolsa de productos de acuerdo con la ley N°
> 19.220.

### Cross-references
- Art. 2 — services regulated and supervised.
- Art. 5 — registration obligation referencing this Registry (definition 12).
- Art. 8 — information obligations reference financial instruments (definition 8).
- Glossary: see `corpus/_lexicon.md` for all defined terms.

---

## Article 4 — Normative powers of the CMF
**Spanish anchor:** Art. 4°
**Tags:** supervision, governance, risk-management

### Plain-English text

The requirements and obligations established by this law may be excepted, as determined by the Commission (CMF) by means of a general regulation (norma de carácter general), with respect to those entities that — by reason of the nature of the service provided, in terms of the number or type of participants, volume of transactions, or financial instruments (instrumentos financieros) traded, quoted, or offered by certain entities, or other conditions of a similar nature — do not compromise public confidence (fe pública) or financial stability (estabilidad financiera) by not exceeding the limits set out in the respective general regulation or by reason of the conditions it establishes. Likewise, the Commission (CMF) may establish less onerous forms of compliance with the requirements and obligations of this law when the limits established in the respective general regulations are not exceeded. In any event, the registration obligation (obligación de inscripción) set out in the following article shall not be excepted.

In the exercise of this power, the Commission (CMF) shall not (no podrá) exempt entities from compliance with the personal data obligations established by this law.

### Original Spanish

> Artículo 4.- Atribuciones normativas. Los requisitos y exigencias establecidas
> en la presente ley podrán ser exceptuados conforme lo determine la Comisión
> mediante norma de carácter general, respecto de aquellas entidades que, por la
> naturaleza del servicio prestado, en términos del número o tipo de participantes,
> volumen de operaciones o instrumentos financieros negociados, cotizados u ofertados
> por determinadas entidades, u otras condiciones de similar naturaleza, no comprometan
> la fe pública o estabilidad financiera al no superar los límites establecidos en la
> respectiva norma de carácter general o en atención a las condiciones que ella
> establezca. Asimismo, la Comisión podrá establecer formas de cumplimiento menos
> gravosas de los requisitos y exigencias de esta ley, cuando no se superen los
> límites establecidos en las normas de carácter general respectivas. Con todo, no
> podrá exceptuarse de la obligación de inscripción señalada en el artículo
> siguiente.
>
> En ejercicio de esta atribución la Comisión no podrá exceptuar del
> cumplimiento de las obligaciones que en materia de datos personales establece esta
> ley.

### Cross-references
- Art. 5 — registration obligation that cannot be excepted under Art. 4.
- Personal data obligations — see Títulos III-IV (to be translated).

---

## Article 5 — Regulated services and registration obligation
**Spanish anchor:** Art. 5°
**Tags:** registration, crowdfunding, alternative-trading, credit-advisory, investment-advisory, custody, order-routing, intermediation

### Plain-English text

Only those registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) administered by the Commission (CMF) may engage on a professional basis in the provision of services of crowdfunding platform (plataforma de financiamiento colectivo), alternative trading system (sistema alternativo de transacción), intermediation of financial instruments (intermediación de instrumentos financieros), order routing (enrutamiento de órdenes), credit advisory (asesoría crediticia), investment advisory (asesoría de inversión), and custody of financial instruments (custodia de instrumentos financieros). Legal persons (personas jurídicas) registered in that Registry may provide one or more of the services listed above, subject to compliance with the requirements and obligations set out in this law for each service provided, and may also carry out such additional activities as the Commission (CMF) may authorise by means of a general regulation (norma de carácter general). Entities registered in the Registry must keep available to the public, through their website, information regarding the type of activity or service they are authorised to perform by the Commission (CMF). International companies that provide the services described above must have a registered address (domicilio) in Chile for those purposes.

The following entities supervised by the Commission (CMF) may provide the services referred to in the preceding paragraph without needing to be registered in the Registry of Financial-Service Providers, and subject to the legal and regulatory framework governing their line of business or corporate purpose, or the complementary regulation issued by the Commission (CMF) for this purpose:

1. In the case of the crowdfunding platform service and the operation of alternative trading systems: securities intermediaries under Law No. 18.045, and commodity exchanges and commodity brokers under Law No. 19.220.

2. In the case of the order routing service: general fund management companies (sociedades administradoras generales de fondos) under Law No. 20.712.

3. In the case of the order routing and intermediation of financial instruments service: banks, securities intermediaries under Law No. 18.045, and commodity brokers under Law No. 19.220.

4. In the case of the credit advisory service: risk rating agencies (clasificadoras de riesgo) under Law No. 18.045.

5. In the case of the investment advisory service: securities intermediaries under Law No. 18.045; general fund managers and portfolio managers (administradores de carteras) under Law No. 20.712; banks; insurance and reinsurance companies; and commodity brokers under Law No. 19.220.

6. In the case of the custody of financial instruments service: securities intermediaries, commodity brokers, commodity exchanges under Law No. 19.220, and companies regulated by Law No. 18.876.

7. In the case of the intermediation and custody of financial instruments services: banks.

8. Other institutions supervised by the Commission (CMF) and registered in its registries, which it authorises by means of a general regulation (norma de carácter general).

### Original Spanish

> Artículo 5.- Servicios regulados y obligación de inscripción. Sólo podrán
> dedicarse en forma profesional a la prestación de servicios de plataforma de
> financiamiento colectivo, sistema alternativo de transacción, intermediación de
> instrumentos financieros, enrutamiento de órdenes, asesoría crediticia, asesoría
> de inversión y custodia de instrumentos financieros, quienes estén inscritos en el
> Registro de Prestadores de Servicios Financieros administrado por la Comisión. Las
> personas jurídicas inscritas en dicho Registro podrán prestar uno o más de los
> servicios indicados anteriormente, sujeto al cumplimiento de los requisitos y
> exigencias contemplados en la presente ley para cada servicio prestado, y podrán
> asimismo realizar aquellas actividades adicionales que autorice la Comisión mediante
> norma de carácter general. Las entidades inscritas en el Registro deberán mantener
> a disposición del público y a través de su sitio web información respecto del
> tipo de actividad o servicio que se encuentran autorizados a efectuar por parte de la
> Comisión. Las empresas internacionales que presten los servicios anteriormente
> descritos deberán tener domicilio en Chile para esos efectos.
>
> Podrán prestar los servicios mencionados en el inciso anterior las siguientes
> entidades fiscalizadas por la Comisión, sin necesidad de estar inscritos en el
> Registro de Prestadores de Servicios Financieros, y conforme al marco legal y
> normativo que les rige en atención a su giro u objeto o a la normativa
> complementaria que dicte la Comisión al efecto:
>
> 1. En el caso del servicio de plataformas de financiamiento colectivo y la
> operación de sistemas alternativos de transacción, intermediarios de valores de la
> ley N° 18.045, y las bolsas y corredores de productos de la ley N° 19.220.
>
> 2. En el caso del servicio de enrutamiento de órdenes, las sociedades
> administradoras generales de fondos de la ley N° 20.712.
>
> 3. En el caso del servicio de enrutamiento de órdenes e intermediación de
> instrumentos financieros, los bancos, los intermediarios de valores de la ley N°
> 18.045 y corredores de productos de la ley N° 19.220.
>
> 4. En el caso del servicio de asesoría crediticia, las clasificadoras de riesgo
> de la ley N° 18.045.
>
> 5. En el caso del servicio de asesoría de inversión, los intermediarios de
> valores de la ley N°18.045, las administradoras generales de fondos y
> administradores de carteras de la ley N°20.712, los bancos, las compañías de
> seguros y reaseguros, y los corredores de productos de la ley N° 19.220.
>
> 6. En el caso del servicio de custodia de instrumentos financieros, los
> intermediarios de valores, corredores de productos, bolsas de productos de la ley N°
> 19.220 y empresas reguladas por la ley N° 18.876.
>
> 7. En el caso de los servicios de intermediación y custodia de instrumentos
> financieros, los bancos.
>
> 8. Otras instituciones fiscalizadas por la Comisión, e inscritas en sus
> registros, que ésta autorice por norma de carácter general.

### Cross-references
- Art. 3(12) — definition of "Registry".
- Art. 4 — normative powers; registration cannot be excepted.
- Art. 6 — registration requirements.
- Art. 7 — authorisation for service provision.

---

## Article 6 — Registration requirements
**Spanish anchor:** Art. 6°
**Tags:** registration, governance

### Plain-English text

To be registered in the Registry, a request must be submitted to the Commission (CMF) in the form and through the means established by the Commission (CMF) by means of a general regulation (norma de carácter general), indicating the applicant's intention to provide one or more of the services regulated by this law, together with the documents specified by the Commission (CMF) through such regulation that establish the applicant's identity and legal capacity.

Registration shall not proceed for legal persons (personas jurídicas) that, in the ten years prior to the date of the application, have been sanctioned with cancellation of registration for any of the serious infractions (infracciones graves) referred to in Article 14, administratively sanctioned for conduct constituting offences under Laws No. 18.045, No. 18.046, No. 19.220, No. 20.712, No. 20.720, Decree with Force of Law No. 3 of 1997 of the Ministry of Finance, and Decree with Force of Law No. 251 of 1931 of the Ministry of Finance, or for the offences referred to in Article 27 of Law No. 19.913 or Article 8 of Law No. 18.314. Registration shall likewise not proceed for legal persons (personas jurídicas) whose principal partners, directors, or managers have been sanctioned or convicted of such conduct within the same period, including those that serve as the basis for the money laundering (lavado de activos) offence set out in subparagraph a) of Article 27 of Law No. 19.913. For these purposes, a principal partner (socio principal) shall mean any person who holds a stake equal to or greater than 10% of the capital or has the capacity to appoint at least one member of the board of directors or management.

Registration shall proceed only — and thus only those persons shall be permitted to provide the services regulated by this law — where the applicant is a legal person (persona jurídica) whose exclusive line of business is the provision of one or more such services, without prejudice to the provisions of the second paragraph of the preceding article.

The Commission (CMF) must rule on registration applications within thirty business days (días hábiles) from the date of the respective application. That period shall be suspended if the Commission (CMF), by digital communication, asks the applicant to correct errors or omissions in the application, and shall only resume once that procedure has been completed. Once any defects have been remedied or observations have been addressed, as applicable, and the period referred to in this article has expired, the Commission (CMF) must rule on the application and, where appropriate, effect the registration within three business days.

### Original Spanish

> Artículo 6.- Requisitos de inscripción. Para ser inscrito en el Registro se
> deberá remitir una solicitud a la Comisión, en la forma y por los medios que ésta
> establezca mediante norma de carácter general, que señale la intención del
> solicitante de prestar uno o más de los servicios regulados por la presente ley, y
> acompañará los antecedentes que la Comisión indique mediante dicha normativa que
> acrediten la identidad y capacidad legal del solicitante.
>
> No procederá la inscripción de las personas jurídicas que, en los diez años
> anteriores a la fecha de la solicitud, hubieren sido sancionadas con la cancelación
> de la inscripción por cualesquiera de las infracciones graves a que se refiere el
> artículo 14, sancionadas administrativamente por incurrir en las conductas
> constitutivas de delito de las leyes N° 18.045, N° 18.046, N° 19.220, N° 20.712,
> N° 20.720, el decreto con fuerza de ley N° 3, de 1997, del Ministerio de Hacienda y
> el decreto con fuerza de ley N° 251, de 1931, del Ministerio de Hacienda o por los
> delitos a que se refiere el artículo 27 de la ley N° 19.913 o el artículo 8 de la
> ley N° 18.314. Tampoco procederá la inscripción de las personas jurídicas cuyos
> socios principales, directores o administradores hayan sido sancionados o condenados
> por ese tipo de conductas en igual período, incluyendo aquellas que sirven de base
> al delito de lavado de activos y que se señalan en la letra a) del artículo 27 de
> la ley N° 19.913. Para estos efectos, se considerará socio principal a las personas
> que posean una participación igual o superior al 10% del capital o tengan la
> capacidad de elegir a lo menos un miembro del directorio o administración.
>
> Solo procederá la inscripción y, por tanto, sólo podrán prestar los
> servicios regulados por la presente ley, las personas jurídicas cuyo giro exclusivo
> sea la prestación de uno o más de tales servicios, sin perjuicio de lo señalado en
> el inciso segundo del artículo anterior.
>
> La Comisión deberá pronunciarse sobre las solicitudes de inscripción en el
> Registro dentro del plazo de treinta días hábiles a contar de la fecha de la
> solicitud respectiva. Dicho plazo se suspenderá si la Comisión, mediante
> comunicación digital, pide al solicitante corregir los errores u omisiones que
> presente su solicitud y sólo se reanudará cuando se haya cumplido con dicho
> trámite. Subsanados los defectos o atendidas las observaciones formuladas en su caso
> y vencido el plazo a que se refiere este artículo, la Comisión deberá pronunciarse
> sobre la solicitud y, en su caso, efectuar la inscripción dentro de tres días
> hábiles.

### Cross-references
- Art. 5 — services requiring registration.
- Art. 14 — serious infractions that bar registration.
- Law No. 19.913 — AML/CFT offences.
- Law No. 18.314 — terrorist financing offences.

---

## Article 7 — Authorisation to provide services
**Spanish anchor:** Art. 7°
**Tags:** registration, crowdfunding, alternative-trading, intermediation, order-routing, investment-advisory, credit-advisory, custody, governance, risk-management

### Plain-English text

Prior to commencing the provision of the services listed below, the respective authorisation of the Commission (CMF) must be obtained. This obligation also applies to those who decide to provide any of these services in addition to the service or services reported in their original registration application. For that purpose, the applicant must demonstrate, in the form, through the means, and under the conditions established by the Commission (CMF) by means of a general regulation (norma de carácter general), that the following requirements are met:

1. Crowdfunding platform (plataforma de financiamiento colectivo):
   a) Having the systems and procedures necessary to comply with the information and disclosure obligations established by Article 8.
   b) Complying with the corporate governance (gobierno corporativo) and risk-management (gestión de riesgo) requirements established by Article 12.

2. Alternative trading system (sistema alternativo de transacción):
   a) Having the systems and procedures necessary to comply with the information and disclosure obligations established by Article 8.
   b) Having the operational capacity to support the processing of the transactions carried out through its systems or infrastructure.
   c) Complying with the corporate governance (gobierno corporativo) and risk-management (gestión de riesgo) requirements established by Article 12.
   d) Having internal rules aimed at ensuring the existence of a fair, competitive, orderly, and transparent secondary market in financial instruments (instrumentos financieros), in order to promote proper price formation and allow the best execution of users' orders.

3. Intermediation of financial instruments (intermediación de instrumentos financieros):
   a) Having the systems and procedures necessary to comply with the information and disclosure obligations established by Article 8.
   b) Having the operational capacity to support the processing of transactions carried out through its systems or infrastructure.
   c) Having the guarantees (garantías) required by Article 10.
   d) Having the equity (patrimonio) required by Article 11.
   e) Complying with the corporate governance (gobierno corporativo) and risk-management (gestión de riesgo) requirements established by Article 12.

4. Order routing (enrutamiento de órdenes):
   a) Having the systems and procedures necessary to comply with the information and disclosure obligations established by Article 8.
   b) Having the operational capacity to support the processing of transactions carried out through its systems or infrastructure.
   c) Having the guarantees (garantías) required by Article 10.
   d) Complying with the corporate governance (gobierno corporativo) and risk-management (gestión de riesgo) requirements established by Article 12.

5. Investment advisory (asesoría de inversión):
   a) Having the systems and procedures necessary to comply with the information and disclosure obligations established by Article 8.
   b) Having the suitability (idoneidad) and knowledge required by Article 9.
   c) Complying with the corporate governance (gobierno corporativo) and risk-management (gestión de riesgo) requirements established by Article 12.

6. Credit advisory (asesoría crediticia):
   a) Having the systems and procedures necessary to comply with the information and disclosure obligations established by Article 8.
   b) Having the suitability (idoneidad) and knowledge required by Article 9.
   c) Complying with the corporate governance (gobierno corporativo) and risk-management (gestión de riesgo) requirements established by Article 12.

7. Custody of financial instruments (custodia de instrumentos financieros):
   a) Having the systems and procedures necessary to comply with the information obligations established by Article 8.
   b) Having the operational capacity to support the processing of transactions carried out through its systems or infrastructure.
   c) Having the guarantees (garantías) required by Article 10.
   d) Having the equity (patrimonio) required by Article 11.
   e) Complying with the corporate governance (gobierno corporativo) and risk-management (gestión de riesgo) requirements established by Article 12.

The Commission (CMF) shall have a maximum period of six months to grant or reject the authorisation referred to in this article, counted from the application submitted by the entity registered in the Registry. That period shall be suspended if the Commission (CMF), by digital communication, asks the applicant to correct errors or omissions in the application, and shall only resume once that procedure has been completed.

For an entity registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) to provide two or more of the services referred to in this article simultaneously, it must demonstrate that it meets all of the requirements applicable to each individual service prior to commencing provision of each one of them, it being understood that for this purpose there is no need to accumulate compliance with the requirements of Articles 10 and 11.

The Commission (CMF) may, at any time and by a reasoned decision (resolución fundada), suspend the authorisation to carry out any of the activities regulated by this law with respect to any registered entity that fails to meet the requirements established for the exercise of the respective activity, or as a precautionary measure when necessary for the proper protection of investors, public confidence (fe pública), or financial stability (estabilidad financiera). This is without prejudice to any criminal and administrative sanctions that may be applicable for non-compliance.

> **TN:** Art. 7 uses both "transacciones" (in 2(b)) and "operaciones" (in 3(b), 4(b), 7(b)) in the operational-capacity context. Both are rendered as "transactions" in English. The Spanish distinction is not legally significant in this context — the law does not turn on it for any defined obligation in Título II.

### Original Spanish

> Artículo 7.- Autorización para prestación de servicios. Previo a iniciar la
> prestación de los servicios señalados a continuación se deberá contar con la
> autorización respectiva de la Comisión. Esta obligación también rige para quienes
> decidan prestar alguno de estos servicios de manera adicional al o a los informados
> en su solicitud de inscripción original. Para ese efecto, el solicitante deberá
> acreditar, en la forma, medios y condiciones que la Comisión establezca mediante
> norma de carácter general, que cumplen con las siguientes exigencias:
>
> 1. Plataforma de financiamiento colectivo:
> a) Contar con los sistemas y procedimientos necesarios para cumplir con las
> obligaciones de información y difusión establecidas por el artículo 8.
> b) Cumplir con las exigencias de gobierno corporativo y gestión de riesgo
> establecidas en el artículo 12.
>
> 2. Sistema alternativo de transacción:
> a) Contar con los sistemas y procedimientos necesarios para cumplir con las
> obligaciones de información y difusión establecidas por el artículo 8.
> b) Tener la capacidad operacional para soportar el procesamiento de las
> transacciones que mediante sus sistemas o infraestructura se realicen.
> c) Cumplir con las exigencias de gobierno corporativo y gestión de riesgo
> establecidas en el artículo 12.
> d) Contar con una reglamentación interna orientada a velar por la existencia de
> un mercado secundario de instrumentos financieros equitativo, competitivo, ordenado y
> transparente, a fin de promover una adecuada formación de precios y permitir la
> mejor ejecución de las órdenes de sus usuarios.
>
> 3. Intermediación de instrumentos financieros:
> a) Contar con los sistemas y procedimientos necesarios para cumplir con las
> obligaciones de información y difusión establecidas por el artículo 8.
> b) Tener la capacidad operacional para soportar el procesamiento de las
> operaciones que mediante sus sistemas o infraestructura se realicen.
> c) Contar con las garantías exigidas por el artículo 10.
> d) Contar con el patrimonio exigido por el artículo 11.
> e) Cumplir con las exigencias de gobierno corporativo y gestión de riesgo
> establecidas en el artículo 12.
>
> 4. Enrutamiento de órdenes:
> a) Contar con los sistemas y procedimientos necesarios para cumplir con las
> obligaciones de información y difusión establecidas por el artículo 8.
> b) Tener la capacidad operacional para soportar el procesamiento de las
> operaciones que mediante sus sistemas o infraestructura se realicen.
> c) Contar con las garantías exigidas por el artículo 10.
> d) Cumplir con exigencias de gobierno corporativo y gestión de riesgo
> establecidas en el artículo 12.
>
> 5. Asesoría de inversión:
> a) Contar con los sistemas y procedimientos necesarios para cumplir con las
> obligaciones de información y difusión establecidas por el artículo 8.
> b) Contar con la idoneidad y conocimientos exigidos por el artículo 9.
> c) Cumplir con las exigencias de gobierno corporativo y gestión de riesgo
> establecidas en el artículo 12.
>
> 6. Asesoría crediticia:
> a) Contar con los sistemas y procedimientos necesarios para cumplir con las
> obligaciones de información y difusión establecidas por el artículo 8.
> b) Contar con la idoneidad y conocimientos exigidos por el artículo 9.
> c) Cumplir con las exigencias de gobierno corporativo y gestión de riesgo
> establecidas en el artículo 12.
>
> 7. Custodia de instrumentos financieros:
> a) Contar con los sistemas y procedimientos necesarios para cumplir con las
> obligaciones de información establecidas por el artículo 8.
> b) Tener la capacidad operacional para soportar el procesamiento de las
> operaciones que se realicen mediante sus sistemas o infraestructura.
> c) Contar con las garantías exigidas por el artículo 10.
> d) Contar con el patrimonio exigido por el artículo 11.
> e) Cumplir con las exigencias de gobierno corporativo y gestión de riesgo
> establecidas en el artículo 12.
>
> La Comisión dispondrá del plazo máximo de seis meses para otorgar o rechazar
> la autorización a que se refiere el presente artículo, contado desde la solicitud
> que al efecto presente la entidad inscrita en el Registro. Dicho plazo se suspenderá
> si la Comisión, mediante comunicación digital, pide al solicitante corregir los
> errores u omisiones que presente su solicitud y sólo se reanudará cuando se haya
> cumplido con dicho trámite.
>
> Para que una entidad inscrita en el Registro de Prestadores de Servicios
> Financieros pueda prestar de manera simultánea dos o más de los servicios
> señalados en el presente artículo, deberá acreditar que cumple todos y cada uno de
> los requisitos aplicables a cada uno de los servicios previo a dar inicio a la
> prestación de cada uno de ellos, sin entenderse por este motivo, la necesidad de
> acumular el cumplimiento de los requisitos de los artículos 10 y 11.
>
> La Comisión, en cualquier momento y por resolución fundada, podrá suspender
> la autorización para realizar cualesquiera de las actividades reguladas por la
> presente ley, a aquella entidad inscrita que no cumpliere con los requisitos
> establecidos para el ejercicio de la actividad respectiva o como medida preventiva
> cuando resulte necesario para el debido resguardo de los inversionistas, la fe
> pública o la estabilidad financiera. Lo anterior, sin perjuicio de las sanciones
> penales y administrativas que resulten aplicables por el incumplimiento.

### Cross-references
- Art. 8 — information and disclosure obligations.
- Art. 9 — suitability requirements for advisory services.
- Art. 10 — guarantee requirements.
- Art. 11 — minimum equity requirements.
- Art. 12 — corporate governance and risk management standards.
- Art. 13 — cancellation of registration linked to art. 7 compliance.

---

## Article 8 — Information obligations
**Spanish anchor:** Art. 8°
**Tags:** crowdfunding, alternative-trading, intermediation, order-routing, investment-advisory, credit-advisory, custody

### Plain-English text

The Commission (CMF) shall establish, by means of a general regulation (norma de carácter general) issued pursuant to Article 4, the information that entities registered in the Registry that carry out any of the following activities must provide to their clients or disclose to the public at large:

1. Crowdfunding platform (plataforma de financiamiento colectivo):
   a) The characteristics and conditions of the investment projects (proyectos de inversión) or financing needs.
   b) Potential conflicts of interest that the crowdfunding platform (plataforma de financiamiento colectivo) may have.

2. Alternative trading system (sistema alternativo de transacción):
   a) Quotations and transactions carried out through its systems or infrastructure.
   b) The access conditions and operating conditions of those systems or infrastructure, and the settlement conditions for transactions carried out therein.
   c) Interruptions or contingencies in its systems.

3. Intermediation of financial instruments (intermediación de instrumentos financieros):
   a) The access conditions and operating conditions of its systems or infrastructure.
   b) Potential conflicts of interest that it may have in the performance of its mandate.
   c) Interruptions or contingencies in its systems.
   d) The economic, financial, and legal situation of the registered entity.

4. Order routing (enrutamiento de órdenes):
   a) The access conditions and operating conditions of its systems or infrastructure.
   b) Potential conflicts of interest that it may have in the performance of its mandate.
   c) Interruptions or contingencies in its systems.

5. Investment advisory (asesoría de inversión):
   a) Conflicts of interest that may arise in the exercise of its activity.
   b) The variables, methods, criteria, or guidelines that guide the recommendation process.
   c) The risks inherent in the recommended investment.

6. Credit advisory (asesoría crediticia):
   a) Conflicts of interest that may arise in the exercise of its activity.
   b) The general variables, methods, criteria, or guidelines that guide the evaluation process.

7. Custody of financial instruments (custodia de instrumentos financieros):
   a) The security, access, and operating conditions of its systems or infrastructure.
   b) Interruptions or contingencies in its systems.
   c) The economic, financial, and legal situation of the entity.

Entities that provide the services regulated in Article 2 must report annually to the Internal Revenue Service (Servicio de Impuestos Internos) on the balances of financial instruments (instrumentos financieros) as defined in numeral 8 of Article 3 that their clients hold in custody, and on the transactions they carried out through the entity in respect of those instruments, for the purposes of income tax, additional tax, value-added tax, and/or stamp and seal tax, or other applicable taxes, in the form and within the deadline determined by the Service by resolution.

### Original Spanish

> Artículo 8.- Obligaciones de información. La Comisión establecerá mediante
> norma de carácter general, conforme a lo dispuesto en el artículo 4, aquella
> información que deberán proveer a sus clientes o difundir al público en general
> quienes estén inscritos en el Registro y realicen alguna de las siguientes
> actividades:
>
> 1. Plataforma de financiamiento colectivo:
> a) Las características y condiciones de los proyectos de inversión o
> necesidades de financiamiento.
> b) Los eventuales conflictos de intereses que pudiere tener la plataforma de
> financiamiento colectivo.
>
> 2. Sistema alternativo de transacción:
> a) Las cotizaciones y operaciones que mediante sus sistemas o infraestructura se
> realicen.
> b) Las condiciones de acceso y funcionamiento de tales sistemas o
> infraestructura, y de liquidación de las operaciones que en éstos se realicen.
> c) Las interrupciones o contingencias que presenten sus sistemas.
>
> 3. Intermediación de instrumentos financieros:
> a) Las condiciones de acceso y funcionamiento de sus sistemas o infraestructura.
> b) Los eventuales conflictos de intereses que pudiere tener en el ejercicio de
> su encargo.
> c) Las interrupciones o contingencias que presenten sus sistemas.
> d) La situación económica, financiera y legal de la entidad inscrita.
>
> 4. Enrutamiento de órdenes:
> a) Las condiciones de acceso y funcionamiento de sus sistemas o infraestructura.
> b) Los eventuales conflictos de intereses que pudiere tener en el ejercicio de
> su encargo.
> c) Las interrupciones o contingencias que presenten sus sistemas.
>
> 5. Asesoría de inversión:
> a) Los conflictos de intereses que puedan surgir en el ejercicio de su
> actividad.
> b) Las variables, métodos, criterios o directrices que guían el proceso de
> recomendación.
> c) Los riesgos inherentes a la inversión recomendada.
>
> 6. Asesoría crediticia:
> a) Los conflictos de intereses que puedan surgir en el ejercicio de su
> actividad.
> b) Las variables, métodos, criterios o directrices generales que guían el
> proceso de evaluación.
>
> 7. Custodia de instrumentos financieros:
> a) Las condiciones de seguridad, acceso y funcionamiento de sus sistemas o
> infraestructura.
> b) Las interrupciones o contingencias que presenten sus sistemas.
> c) La situación económica, financiera y legal de la entidad.
>
> Las entidades que presten los servicios regulados en el artículo 2 deberán
> informar anualmente al Servicio de Impuestos Internos sobre los saldos de los
> instrumentos financieros definidos en el numeral 8 del artículo 3 que mantengan en
> custodia sus clientes y de las transacciones que por su intermedio realizaron
> respecto a dichos instrumentos, para la aplicación del impuesto a la renta, impuesto
> adicional, impuesto al valor agregado y/o impuesto de timbres y estampillas, u otros
> impuestos que correspondan, en la forma y plazo que éste determine mediante
> resolución.

### Cross-references
- Art. 2 — services regulated.
- Art. 3(8) — definition of financial instrument for tax reporting.
- Art. 4 — CMF normative powers.
- Art. 7 — authorisation requirements include Art. 8 compliance.

---

## Article 9 — Suitability for service provision
**Spanish anchor:** Art. 9°
**Tags:** investment-advisory, credit-advisory, governance

### Plain-English text

Natural persons (personas naturales) performing functions for entities that provide investment advisory (asesoría de inversión) and credit advisory (asesoría crediticia) services registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros), as well as the systems used by those entities to provide their services, must comply with standards of objectivity, coherence, and consistency between the elements used to make their recommendation or evaluation and the needs expressed by the clients who contract those services.

The Commission (CMF), by means of a general regulation (norma de carácter general), shall establish the circumstances that must be demonstrated to qualify that such persons and systems meet the conditions referred to in the preceding paragraph, such as knowledge certification or certification of inviolability, among others.

### Original Spanish

> Artículo 9.- Idoneidad para la prestación de los servicios. Las personas
> naturales que desempeñen funciones para las entidades que presten servicios de
> asesoría de inversión y asesoría crediticia, inscritas en el Registro de
> Prestadores de Servicios Financieros, así como los sistemas que dichas entidades
> utilicen para la prestación de sus servicios, deberán cumplir con estándares de
> objetividad, coherencia y consistencia entre los elementos empleados para efectuar su
> recomendación o evaluación y las necesidades manifestadas por los clientes que
> contratan dichos servicios.
>
> La Comisión, mediante norma de carácter general, establecerá las
> circunstancias que se deberán acreditar para calificar que tales personas y sistemas
> cuentan con las condiciones a que se refiere el inciso anterior, tales como
> certificación de conocimientos o de inviolabilidad, entre otros.

### Cross-references
- Art. 7(5)(b) and 7(6)(b) — authorisation requirements for advisory services include Art. 9 compliance.
- Art. 3(1) — definition of credit advisory.
- Art. 3(2) — definition of investment advisory.

---

## Article 10 — Guarantees
**Spanish anchor:** Art. 10°
**Tags:** intermediation, order-routing, custody, capital-requirements, risk-management

### Plain-English text

Once the business volume or number of clients potentially affected by the acts or omissions of entities has been reached — as established by the Commission (CMF) by means of a general regulation (norma de carácter general) — those providing services of intermediation of financial instruments (intermediación de instrumentos financieros), order routing (enrutamiento de órdenes), or custody of financial instruments (custodia de instrumentos financieros) must constitute one or more guarantees (garantías), as the case may be, to answer for the correct and full performance of all obligations arising from their activity and, in particular, for any potential losses that their actions or omissions in the provision of services may cause to their clients. The entities referred to above shall be liable for slight fault (culpa leve) in the provision of the aforementioned services.

The guarantee (garantía) must be constituted by means of a bank guarantee (boleta bancaria) or insurance policy (póliza de seguros) for the amount determined by the Commission (CMF) according to the parameters established by means of a general regulation (norma de carácter general), taking into account the potential impact or harm the entity may cause to its client in relation to the service or services provided and the quality of the entity's corporate governance (gobierno corporativo) and risk management (gestión de riesgos).

Notwithstanding the foregoing, the Commission (CMF), by means of a general regulation (norma de carácter general) and with the aim of reconciling the protection of public confidence (fe pública) and financial stability (estabilidad financiera) with the economic viability of the business models regulated by this article, may substitute the individual guarantee referred to above with a guarantee co-financed by more than one entity obligated to constitute it under this article, which must be of a sufficient amount and adequate characteristics to address the risks of all the co-financing entities.

### Original Spanish

> Artículo 10.- Garantías. Alcanzado el volumen de negocios o número de
> clientes que pudieran resultar afectados con las actuaciones u omisiones en que
> pudieren incurrir las entidades, según haya establecido la Comisión por norma de
> carácter general, quienes presten los servicios de intermediación de instrumentos
> financieros, enrutamiento de órdenes o custodia de instrumentos financieros,
> deberán constituir una o más garantías, según sea el caso, para responder del
> correcto y cabal cumplimiento de todas las obligaciones emanadas de su actividad y,
> especialmente, por los eventuales perjuicios que pudieren ocasionar a sus clientes
> por sus acciones u omisiones en la prestación de los servicios. Las entidades antes
> indicadas responderán de culpa leve en la prestación de los servicios antes
> mencionados.
>
> La garantía deberá constituirse mediante boleta bancaria o póliza de seguros
> por el monto que determine la Comisión, según los parámetros establecidos mediante
> norma de carácter general en consideración al impacto o perjuicio potencial que
> pueda ocasionar la entidad a su cliente en atención al o los servicios prestados, la
> calidad del gobierno corporativo y gestión de riesgos de la entidad.
>
> No obstante lo establecido en los incisos anteriores, la Comisión, mediante
> norma de carácter general y con el objeto de compatibilizar la protección de la fe
> pública y estabilidad financiera con la viabilidad económica de los modelos de
> negocios regulados por el presente artículo, podrá sustituir la garantía
> individual antes señalada por una garantía cofinanciada por más de una entidad de
> las obligadas a su constitución por este artículo, la que deberá ser de un monto
> suficiente y de características adecuadas para enfrentar los riesgos de todas las
> entidades que la cofinancian.

### Cross-references
- Art. 7(3)(c), 7(4)(c), 7(7)(c) — authorisation requirements include Art. 10 compliance.
- Art. 11 — minimum equity requirements (related capital-adequacy regime).
- Art. 12 — corporate governance quality affects guarantee amount.

---

## Article 11 — Minimum equity
**Spanish anchor:** Art. 11°
**Tags:** intermediation, custody, capital-requirements, risk-management, governance

### Plain-English text

Once the business volume established by the Commission (CMF) by means of a general regulation (norma de carácter general) has been reached — a volume from which it may be reasonably presumed that the risks faced by the entity may compromise public confidence (fe pública) or financial stability (estabilidad financiera) — entities providing the services of intermediation or custody of financial instruments (intermediación o custodia de instrumentos financieros) must maintain at all times a minimum equity (patrimonio mínimo) equal to or greater than the higher of:

a) 5,000 UF; or
b) 3% of the entity's financial- and operational-risk-weighted assets, calculated in accordance with the method established by the Commission (CMF) by means of a general regulation (norma de carácter general). For entities with deficiencies in their risk management (gestión de riesgos), that percentage may be increased to 6% by the Commission (CMF) based on its assessment of the quality of risk management.

If the entity's minimum equity falls below the amount established in this article, it must notify the Commission (CMF) as soon as it becomes aware of the situation and, within five calendar days, submit a regularisation plan (plan de regularización) containing concrete measures to remedy the deficit and ensure the entity's normal operation; that period may be extended by the Commission (CMF) to a total of ten calendar days. While that situation persists, the entity must refrain from carrying out new transactions that could deepen the equity deficit or deteriorate the entity's financial situation.

Likewise, if the Commission (CMF) becomes aware that an entity is in the situation referred to in the preceding paragraph, or if it is foreseeable that the entity will imminently incur an equity deficit if current market conditions or the entity's own conduct continues, and this has not been communicated to the Commission (CMF) in a timely manner, the Commission (CMF) may require the entity to submit a regularisation plan within the period referred to in the preceding paragraph. If the equity deficit is not remedied within six months from the date on which it arose, the entity must cease providing the services of intermediation of financial instruments and custody of financial instruments, and submit for the Commission's (CMF's) approval a programme for winding down operations and transferring clients (programa de término de operaciones y traspaso de clientes).

Upon receiving the programme for winding down operations and transferring clients referred to in the preceding paragraph, the Commission (CMF) may appoint one or more receivers (interventores) for the period it determines by reasoned decision (resolución fundada). The administration of the entity shall be subject, in the exercise of its functions, to the instructions issued by the receiver or receivers appointed by the Commission (CMF). The receiver shall have all powers of the ordinary course of business that the law and the entity's bylaws confer on the board of directors, or whoever acts in that capacity, and on the general manager. The appointment of a receiver must be made from among Commission (CMF) officers or duly qualified external professionals, subject to their meeting the suitability and technical capacity requirements determined by the Commission (CMF) by means of a general regulation (norma de carácter general). In the latter case, the receiver's fees shall be paid from the Commission's (CMF's) annual budget.

> **TN:** "interventor" is rendered as "receiver" as the closest functional English equivalent for a regulator-appointed official who oversees and controls an entity's administration during a structured wind-down. This should not be confused with an insolvency receiver under common-law systems; the interventor here does not displace management but subjects it to regulatory instruction, and is closer to a supervisory "controller" or "administrator" under CMF oversight.

In proceedings seeking to enforce the liability of any entity registered in the Registry that provides the services referred to in the first paragraph of this article, or to compel enforcement of such entity's obligations to third parties, the financial instruments or monies delivered to it in deposit or to honour payment instructions made shall in no case be subject to attachment, pre-trial measures, precautionary measures, or other restrictions on ownership.

However, such measures may be ordered, in accordance with the general rules, where they concern personal obligations of the third parties who delivered those financial instruments in deposit — but only with respect to those instruments owned by the respective third party.

### Original Spanish

> Artículo 11.- Patrimonio mínimo. Alcanzado el volumen de negocios que la
> Comisión haya establecido por norma de carácter general y que permitan presumir
> razonablemente que con los riesgos que enfrenta la entidad se puede comprometer la fe
> pública o la estabilidad financiera, las entidades que presten los servicios de
> intermediación o custodia de instrumentos financieros, deberán contar
> permanentemente con un patrimonio mínimo, igual o superior al mayor entre:
>
> a) 5.000 UF; o
> b) El 3% de los activos ponderados por riesgos financieros y operacionales de la
> entidad, calculado conforme al método que al efecto establezca la Comisión mediante
> norma de carácter general. Tratándose de entidades que presenten deficiencias en su
> gestión de riesgos, dicho porcentaje podrá ser incrementado hasta el 6% por la
> Comisión en atención a la evaluación de la calidad de gestión de riesgos que
> ésta realice.
>
> En el evento que el patrimonio mínimo de la entidad disminuyere a un monto
> inferior al establecido en el presente artículo, ésta deberá comunicarlo a la
> Comisión tan pronto tome conocimiento de ello y presentar dentro del plazo de cinco
> días corridos un plan de regularización que deberá contener medidas concretas del
> referido déficit que le permitan remediar la situación en que se encuentra y
> asegurar su normal funcionamiento, plazo que podrá ser prorrogado por la Comisión
> hasta completar diez días corridos en total. Mientras se mantenga dicha situación,
> deberá abstenerse de realizar nuevas operaciones que pudieran profundizar el
> déficit patrimonial o deteriorar la situación financiera de la entidad.
>
> Asimismo, en caso de que la Comisión tomare conocimiento de que una entidad se
> encuentra en los supuestos indicados en el inciso precedente o cuando resulte
> previsible que incurrirá en déficit patrimonial de manera inminente de mantenerse
> las circunstancias de mercado o en atención al actuar de la propia entidad, y esto
> no le hubiere sido comunicado oportunamente, la Comisión podrá requerir a la
> entidad la presentación de un plan de regularización dentro del plazo indicado en
> el inciso anterior. De no subsanarse el déficit patrimonial dentro del plazo de seis
> meses contado desde que aquél se hubiere producido, la entidad deberá dejar de
> prestar el servicio de intermediación de instrumentos financieros y custodia de
> instrumentos financieros, y presentar para aprobación de la Comisión un programa de
> término de operaciones y traspaso de clientes.
>
> Recibido el programa de término de operaciones y traspaso de clientes a que se
> refiere el inciso anterior, la Comisión podrá designar uno o más interventores por
> el período que determine mediante resolución fundada. La administración de la
> entidad quedará sometida, en el ejercicio de sus funciones, a las instrucciones que
> le imparta el o los interventores designados por la Comisión. El interventor tendrá
> todas las facultades del giro ordinario que la ley y los estatutos señalan al
> directorio, o a quien haga sus veces, y al gerente general. La designación de
> interventor deberá recaer en funcionarios de la Comisión o en profesionales
> externos debidamente calificados, sujeto a que cumplan los requisitos de idoneidad y
> capacidad técnica que la Comisión determine mediante norma de carácter general. En
> este último caso, los servicios del interventor serán remunerados con cargo del
> presupuesto anual de la Comisión.
>
> En los juicios en que se persiga la responsabilidad de alguna de las entidades
> inscritas en el Registro y que presten los servicios señalados en el inciso primero,
> o la ejecución forzada de las obligaciones de éstas con terceros, no se podrá, en
> caso alguno, embargar, ni decretar medidas prejudiciales o precautorias u otras
> limitaciones al dominio respecto de los instrumentos financieros o dineros que les
> hubieren sido entregados en depósito o para honrar las instrucciones de pago
> efectuadas.
>
> Sin embargo, podrán decretarse tales medidas, de conformidad a las reglas
> generales, cuando se trate de obligaciones personales de los terceros que le hayan
> entregado esos instrumentos financieros en depósito, pero sólo respecto de aquellos
> de propiedad del tercero respectivo.

### Cross-references
- Art. 7(3)(d) and 7(7)(d) — authorisation requirements include Art. 11 compliance.
- Art. 10 — guarantee requirements (complementary capital-adequacy regime).
- Art. 12 — risk management quality affects minimum equity percentage.
- Art. 14(b) — failure to comply with regularisation plan is a serious infraction.

---

## Article 12 — Corporate governance and risk management
**Spanish anchor:** Art. 12°
**Tags:** governance, risk-management

### Plain-English text

In order to safeguard the information and interests of their clients and ensure their financial and operational continuity, those registered in the Registry must design, approve, and implement policies, procedures, and controls that reconcile their financial and economic viability with their capacity to have suitable strategic responses to the risks inherent in their lines of business.

It shall be the responsibility of the Commission (CMF) to establish, by means of a general regulation (norma de carácter general), the corporate governance (gobierno corporativo) and risk management (gestión de riesgos) standards — including cybersecurity and information security aspects — against which it will be presumed that those registered in the Registry comply with the provision set out in the preceding paragraph, without prejudice to the fact that each entity must adopt or adapt those standards according to its size, volume, and nature of business, and risks.

In the case of entities registered in the Registry that provide intermediation or custody of financial instruments services, the standards established by the Commission (CMF) shall be those against which it assesses the quality of the entity's corporate governance (gobierno corporativo) and risk management (gestión de riesgos) for the purpose of determining the amount of the guarantee and minimum equity referred to in Articles 10 and 11.

### Original Spanish

> Artículo 12.- Gobierno corporativo y gestión de riesgos. Con el objeto de
> resguardar la información e intereses de sus clientes, y asegurar su continuidad
> financiera y operacional, quienes estén inscritos en el Registro deben diseñar,
> aprobar e implementar políticas, procedimientos y controles que compatibilicen su
> viabilidad económica-financiera con su capacidad de contar con respuestas
> estratégicas idóneas para los riesgos inherentes a sus líneas de negocios.
>
> Corresponderá a la Comisión establecer, mediante norma de carácter general,
> los estándares de gobierno corporativo y gestión de riesgos, incluyendo aspectos de
> ciberseguridad y seguridad de información, que permitirán presumir que quienes
> estén inscritos en el Registro cumplen con la disposición señalada en el inciso
> anterior, sin perjuicio que corresponderá a cada entidad adoptar o adaptar tales
> estándares conforme a su tamaño, volumen y naturaleza de sus negocios, y riesgos.
>
> En el caso de entidades inscritas en el Registro que presten los servicios de
> intermediación o custodia de instrumentos financieros, los estándares establecidos
> por la Comisión serán aquellos contra los que ésta evaluará la calidad del
> gobierno corporativo y gestión de riesgos de la entidad para efectos de la
> determinación del monto de la garantía y patrimonio mínimo a que se refieren los
> artículos 10 y 11.

### Cross-references
- Art. 7 — authorisation requirements include Art. 12 compliance across all service types.
- Art. 10 — guarantee amounts depend on corporate governance quality per Art. 12.
- Art. 11 — minimum equity percentage depends on risk management quality per Art. 12.

---

## Article 13 — Cancellation of registration
**Spanish anchor:** Art. 13°
**Tags:** registration, supervision

### Plain-English text

The Commission (CMF) may cancel the registration in the Registry of any person that has been sanctioned for the serious infractions (infracciones graves) referred to in Article 14, or of persons who, while registered in the Registry, have carried out activities other than those regulated by this law, or — if those activities are among those regulated — have not been authorised pursuant to the procedure established in Article 7. Cancellation sanctions shall be ancillary (accesorias) to those applicable to the entity for the conduct that led to such cancellation. Additionally, the Commission (CMF) may cancel the registration of those who have not applied for authorisation to carry out any of the activities regulated by this law within twelve months from the relevant registration.

The Commission (CMF) shall cancel the registration in the Registry of all those who request it voluntarily or of those entities that become a debtor in insolvency liquidation proceedings (procedimiento concursal de liquidación). If the Commission (CMF) has initiated an administrative sanction proceeding against the applicant, the cancellation application shall be suspended until that proceeding has concluded, or shall be set aside if registration is cancelled as a sanction for the serious infractions referred to above.

### Original Spanish

> Artículo 13.- Cancelación de inscripción. La Comisión podrá cancelar la
> inscripción en el Registro de todo quien hubiere sido sancionado por las
> infracciones graves a que se refiere el artículo 14, o quienes, estando inscritos en
> el Registro, hubieren realizado actividades distintas de aquellas reguladas por la
> presente ley o, siendo de estas últimas, que no hubieren sido autorizadas conforme
> al procedimiento establecido en el artículo 7. Las sanciones de cancelación de la
> inscripción serán accesorias a las que corresponda aplicar a la entidad por las
> conductas que motivaron dicha cancelación. Adicionalmente, la Comisión podrá
> cancelar la inscripción de quienes no hubieren solicitado la autorización para
> realizar alguna de las actividades reguladas por la presente ley dentro del plazo de
> doce meses contado desde la inscripción correspondiente.
>
> La Comisión cancelará la inscripción en el Registro de todos quienes así lo
> soliciten voluntariamente o de aquellas entidades que pasen a tener la calidad de
> deudor en un procedimiento concursal de liquidación. En caso de que la Comisión
> hubiere iniciado un proceso administrativo sancionatorio en contra del solicitante,
> quedará suspendida su solicitud de cancelación hasta que dicho proceso haya
> terminado, o será dejada sin efecto, en caso de que se cancele la inscripción como
> sanción por las infracciones graves antes señaladas.

### Cross-references
- Art. 14 — list of serious infractions that trigger cancellation.
- Art. 7 — authorisation procedure; failure to obtain authorisation triggers cancellation power.
- Art. 6 — registration; prior sanctions bar re-registration for 10 years (Art. 6, para. 2).

---

## Article 14 — Serious infractions
**Spanish anchor:** Art. 14°
**Tags:** supervision, intermediation, alternative-trading, crowdfunding, investment-advisory, credit-advisory, custody, AML-CFT

### Plain-English text

For the purposes of Articles 6 and 13, the following shall be considered serious infractions (infracciones graves):

a) Providing the services regulated by this law without being registered in the Registry or without having obtained authorisation to provide those services in accordance with the requirements and conditions established for their provision.

b) Failing to comply, for reasons attributable to the entity's management, with the regularisation plan (plan de regularización) or the programme for winding down operations and transferring clients referred to in Article 11, or violating the prohibition on carrying out activities set out in that provision.

c) Failing to constitute the guarantee (garantía) required by Article 10, or constituting it for an amount lower than that required.

d) Maliciously submitting false, incomplete, or misleading information to the Commission (CMF) regarding the economic, financial, or legal situation of the entity.

e) Maliciously delivering false, incomplete, or misleading information to clients or the public at large regarding the matters referred to in Article 8.

f) Maliciously disseminating false, incomplete, or misleading information regarding companies, projects, or persons whose financing needs are being or will be disseminated on a crowdfunding platform (plataforma de financiamiento colectivo).

g) Maliciously disseminating false information regarding financial instruments (instrumentos financieros) traded on alternative trading systems (sistemas alternativos de transacción), or the issuers of those instruments, with the purpose of altering the economic valuation that investors have of those instruments.

h) Misappropriating, for one's own benefit or for the benefit of third parties, financial instruments (instrumentos financieros), foreign exchange, or monies held in custody on behalf of clients.

i) Maliciously disseminating false or biased information for the provision of investment advisory (asesoría de inversión) or credit advisory (asesoría crediticia) services, with the purpose of inducing error, even if no advantage is thereby obtained for oneself or third parties.

j) Engaging in price manipulation (manipulación de precio) of financial instruments (instrumentos financieros), meaning any action carried out with the purpose of artificially stabilising, fixing, or varying the prices of financial instruments that does not fall within the conduct authorised by the Commission (CMF) by means of a general regulation (norma de carácter general).

k) Making fictitious quotations or transactions with respect to any financial instrument (instrumento financiero), or carrying out or inducing or attempting to induce the purchase or sale of financial instruments through any deceptive or fraudulent act, practice, mechanism, or artifice.

l) Maliciously providing false background information or knowingly certifying false facts to the Commission (CMF), to alternative trading systems (sistemas alternativos de transacción), or to the public at large, for the purposes of this law.

### Original Spanish

> Artículo 14.- Infracciones graves. Para efectos de lo establecido en los
> artículos 6 y 13, se considerarán infracciones graves:
>
> a) Prestar los servicios regulados por la presente ley, sin estar inscrito en el
> Registro o sin haber obtenido la autorización para prestar los servicios conforme a
> los requisitos y condiciones establecidos para la prestación de esos servicios.
>
> b) Incumplir, por razones imputables a la administración de la entidad, el plan
> de regularización y el programa de término de operaciones y traspaso de clientes a
> que se refiere el artículo 11 o infringir la prohibición de realizar actividades
> indicada en dicha norma.
>
> c) No haber constituido la garantía exigida por el artículo 10 o haberla
> constituido por un monto inferior al requerido.
>
> d) Presentar antecedentes maliciosamente falsos, incompletos o inductivos a
> error a la Comisión respecto de la situación económica, financiera o legal de la
> entidad.
>
> e) Entregar información maliciosamente falsa, incompleta o inductiva a error a
> clientes o al público en general respecto de las materias señaladas en el artículo
> 8.
>
> f) Difundir información maliciosamente falsa, incompleta o inductiva a error
> respecto de las empresas, proyectos o personas cuyas necesidades de financiamiento
> están siendo o serán difundidas en una plataforma de financiamiento colectivo.
>
> g) Difundir información maliciosamente falsa respecto de los instrumentos
> financieros negociados en sistemas alternativos de transacción, o los emisores de
> aquéllos, con la finalidad de alterar la valoración económica que los
> inversionistas tienen de esos instrumentos.
>
> h) Utilizar en forma indebida en beneficio propio o de terceros los instrumentos
> financieros, divisas o dineros mantenidos en custodia por cuenta de clientes.
>
> i) Difundir información maliciosamente falsa o tendenciosa para la prestación
> de servicios de asesoría de inversión o asesoría crediticia, con el objeto de
> inducir a error, aun cuando no se obtenga con ello ventajas para sí o terceros.
>
> j) Incurrir en conductas de manipulación de precio respecto de instrumentos
> financieros, entendiendo por tal la acción que se efectúa con el objeto de
> estabilizar, fijar o hacer variar artificialmente los precios de instrumentos
> financieros, y que no se enmarque dentro de las conductas autorizadas por la
> Comisión mediante norma de carácter general.
>
> k) Efectuar cotizaciones o transacciones ficticias respecto de cualquier
> instrumento financiero o efectuar transacciones o inducir o intentar inducir a la
> compra o venta de instrumentos financieros, por medio de cualquier acto, práctica,
> mecanismo o artificio engañoso o fraudulento.
>
> l) Proporcionar maliciosamente antecedentes falsos o certificar a sabiendas
> hechos falsos a la Comisión, a los sistemas alternativos de transacción o al
> público en general, para los efectos de lo dispuesto en esta ley.

### Cross-references
- Art. 6 — serious infractions bar re-registration for 10 years.
- Art. 10 — guarantee obligation; Art. 14(c) directly references Art. 10.
- Art. 11 — regularisation plan; Art. 14(b) directly references Art. 11.
- Art. 8 — information obligations; Art. 14(e) directly references Art. 8.
- Art. 13 — cancellation of registration triggered by serious infractions.

---

## Article 15 — Aggravating circumstances
**Spanish anchor:** Art. 15°
**Tags:** supervision, AML-CFT

### Plain-English text

Being subject to the supervision (supervisión) of the Commission (CMF) and committing the offences described in Articles 467 through 473 of the Penal Code on the occasion of providing the services regulated by this law shall be considered an aggravating circumstance in those offences.

The penalty (pena) shall be increased by one degree when any of the acts described in the preceding paragraph is perpetrated by someone who feigns the status of being registered in the Registry or of being supervised by the Commission (CMF).

Any person who commits any of the acts provided for in Law No. 21.459 against a provider of services regulated by this law shall be subject to the penalty set out therein increased by one degree.

> **TN:** "delitos contemplados en los artículos 467 a 473 del Código Penal" refers to the Chilean Penal Code offences covering fraud and related property offences (estafa and related crimes). The plain-English text preserves the statutory reference without substituting common-law equivalents, consistent with treatment of statutory references throughout this corpus.

### Original Spanish

> Artículo 15.- Agravantes. Se considerará como circunstancia agravante en los
> delitos contemplados en los artículos 467 a 473 del Código Penal, el hecho de
> cometerlos estando sujeto a la supervisión de la Comisión y con ocasión de la
> prestación de los servicios regulados en la presente ley.
>
> La pena se aumentará en un grado cuando se perpetrare alguno de los hechos
> descritos en el inciso anterior por quien fingiere la calidad de inscrito en el
> Registro o de supervisado por la Comisión.
>
> El que cometiera cualquiera de los hechos previstos en la ley N° 21.459 contra
> un prestador de servicios regulados en la presente ley se le impondrá la pena allí
> señalada aumentada en un grado.

### Cross-references
- Articles 467–473 of the Chilean Penal Code — fraud and property offences.
- Law No. 21.459 — computer crimes law (cybercrime).
- Art. 13 — cancellation of registration as ancillary sanction.
- Art. 14 — serious infractions (administrative sanctions; Art. 15 covers criminal aggravation).

---

<!-- source: corpus/21521-fintech/titulo-03-finanzas-abiertas.md -->
## FILE: corpus/21521-fintech/titulo-03-finanzas-abiertas.md

# Ley 21.521 — Título III: Open Finance System (Del Sistema de Finanzas Abiertas)

**Law:** Ley 21.521 (in force 2023-02-03)
_law:_ 21.521

---

## Article 16 — Objectives and principles of the Open Finance System
**Spanish anchor:** Art. 16°
**Tags:** open-finance, technical-standards, customer-protection, supervision

### Plain-English text

With the aim of promoting competition, innovation, and financial inclusion, this Title establishes the basic rules and principles for the implementation of an open finance system (sistema de finanzas abiertas), hereinafter the "Open Finance System (Sistema de Finanzas Abiertas, or SFA)" or the "System," that enables the exchange among different providers of financial-customer information (información de clientes financieros) who have expressly consented (consentido expresamente) to such exchange, and other types of data referred to in the following article, through remote and automated access interfaces (interfaces de acceso remoto y automatizado) that allow direct interconnection and communication between the institutions participating in the System, under adequate security standards (estándares de seguridad) and subject to compliance with the requirements and conditions established in this law and the general regulations (normativa) issued by the Commission (CMF) on the matters set out therein.

The Open Finance System shall be applicable to the institutions, financial products and services, types of data, and services set out in the following articles and under the terms and conditions determined by the general regulations (normativa) issued by the Commission (CMF) for that purpose.

In fulfilling their duties and obligations, institutions participating in the Open Finance System (Sistema de Finanzas Abiertas, or SFA) must observe the principles of proportionality, quality, transparency and customer information (transparencia e información al cliente), data security and privacy, non-discriminatory treatment, and interoperability among participating institutions.

### Original Spanish

> Artículo 16.- Objetivos y Principios del Sistema de Finanzas Abiertas. Con el
> objetivo de promover la competencia, innovación e inclusión en el sistema
> financiero, el presente título establece las reglas y principios básicos para la
> implementación de un sistema de finanzas abiertas, en adelante, "Sistema de Finanzas
> Abiertas" o "Sistema", que permita el intercambio entre distintos prestadores de
> servicios de información de clientes financieros que hayan consentido expresamente
> en ello y otros tipos de datos señalados en el artículo siguiente, a través de
> interfaces de acceso remoto y automatizado que permitan una interconexión y
> comunicación directa entre las instituciones participantes del Sistema, bajo
> adecuados estándares de seguridad y sujeto al cumplimiento de las exigencias y
> condiciones establecidas en esta ley y la normativa que dicte la Comisión, en las
> materias que se señalan al efecto.
>
> El Sistema de Finanzas Abiertas resultará aplicable a las instituciones,
> productos y servicios financieros, tipos de datos y servicios que se indican en los
> artículos siguientes y en los términos y condiciones que determine la normativa que
> dicte al efecto la Comisión.
>
> En el cumplimiento de sus deberes y obligaciones, las instituciones que
> participen en el Sistema de Finanzas Abiertas deberán observar los principios de
> proporcionalidad, calidad, transparencia e información al cliente, seguridad y
> privacidad de los datos, trato no discriminatorio e interoperabilidad entre
> instituciones participantes.

### Cross-references
- Art. 17 — perimeter and scope; types of data referred to in this article.
- Art. 1 — general principles of the law (proportionality, innovation, competition).
- Art. 27 — supervision by the Commission (CMF).

---

## Article 17 — Perimeter and scope of the Open Finance System
**Spanish anchor:** Art. 17°
**Tags:** open-finance, data-providers, data-recipients, account-information, payment-initiation, technical-standards

### Plain-English text

The institutions participating in the Open Finance System (Sistema de Finanzas Abiertas, or SFA) shall be those that qualify as information-providing institutions (instituciones proveedoras de información), information-based service-providing institutions (instituciones proveedoras de servicios basados en información), account-providing institutions (instituciones proveedoras de cuentas), and payment initiation service providers (proveedores de servicios de iniciación de pago), as set out in Articles 18, 19, and 20.

Such institutions must adopt the measures necessary to allow the consultation, access, delivery, and exchange of information (información), as applicable, with respect to the types of data, financial products, and services relating to financial customers (clientes financieros) — whether natural persons (personas naturales) or legal persons (personas jurídicas) — who have contracted financial products or services or carried out financial transactions with them, hereinafter "Customers (Clientes)" or "Customer (Cliente)," in an expeditious and secure manner and under the conditions, timeframes, and specifications defined by the Commission (CMF) by means of a general regulation (norma de carácter general).

The Open Finance System must cover the following:

1. Information on the general terms and conditions of financial products and services offered to the public, and public service channels made available by the information-providing institutions listed in Article 18. Such information must be kept available to the public through a public-access interface that information-providing institutions (Instituciones Proveedoras de Información) must maintain, in open-data format.

2. Identification and registration information of Customers and their representatives, collected by information-providing institutions during the Customer enrolment process, contracting of products and services, or execution of transactions, or in order to comply with regulatory requirements for customer due diligence (debido conocimiento del Cliente). Such information may only be communicated pursuant to the authorisation granted by the Customer in accordance with Article 23.

3. Information on the commercial conditions contracted and the use or transaction history of Customers with respect to the financial products and services they have contracted with information-providing institutions, as applicable, including: a) current accounts and their associated lines of credit, sight accounts (cuentas a la vista), provision-of-funds accounts (cuentas de provisión de fondos), and savings accounts; b) credit cards with their respective associated lines of credit; c) money lending transactions (operaciones de crédito de dinero); d) insurance policies; e) savings or investment instruments; f) payment card and similar payment-method services; and g) other financial products or services defined by the Commission (CMF) by means of a general regulation (norma de carácter general). Such information may only be communicated pursuant to the authorisation granted by the Customer in accordance with Article 23. Transaction history may not extend back more than five years.

4. Communications between financial service providers regulated under Law No. 21.236, for the purposes of the financial portability (portabilidad financiera) process established in that legislation, as determined by the regulation (reglamento) of that law.

5. Data or information necessary for the provision of payment initiation services, as set out in Article 20 and subject to the prior authorisation of the Customer in accordance with Article 23.

6. Other data or information relating to financial products or services or the initiation of other types of transactions that the Commission (CMF) may set out by means of a general regulation (norma de carácter general), subject to the prior authorisation of the Customer.

### Original Spanish

> Artículo 17.- Perímetro y alcance del Sistema de Finanzas Abiertas. Las
> instituciones participantes del Sistema de Finanzas Abiertas serán aquellas que
> califiquen como instituciones proveedoras de información, instituciones proveedoras
> de servicios basados en información, instituciones proveedoras de cuentas y
> proveedores de servicios de iniciación de pago, conforme a lo señalado en los
> artículos 18, 19 y 20.
>
> Tales instituciones deberán adoptar las medidas necesarias para permitir la
> consulta, acceso, entrega e intercambio de información, según corresponda, respecto
> de los tipos de datos, productos y servicios financieros relativos a clientes
> financieros, sean personas naturales o jurídicas, que hayan contratado productos o
> servicios financieros o realizado operaciones financieras con ellos, en adelante,
> "Clientes" o "Cliente", de forma expedita y segura y en las condiciones, plazos y
> según las especificaciones que defina la Comisión mediante norma de carácter
> general.
>
> El Sistema de Finanzas Abiertas deberá comprender lo siguiente:
>
> 1. Información sobre términos y condiciones generales de los productos y
> servicios financieros que ofrezcan al público y canales de atención al público
> dispuestos por las instituciones proveedoras de información indicadas en el
> artículo 18. Dicha información se deberá mantener a disposición del público a
> través de una interfaz de acceso público que deberán mantener disponible las
> Instituciones Proveedoras de Información y en formato de datos abiertos.
>
> 2. Información de identificación y registro de los Clientes y sus
> representantes recabada por las instituciones proveedoras de información durante el
> proceso de enrolamiento del Cliente, contratación de los productos y servicios o
> ejecución de operaciones, o bien para dar cumplimiento a exigencias regulatorias de
> debido conocimiento del Cliente. Dicha información sólo podrá ser comunicada
> conforme a la autorización que otorgue el Cliente de acuerdo con lo dispuesto en
> artículo 23.
>
> 3. Información sobre las condiciones comerciales contratadas y el uso o
> historial de transacciones realizadas por los Clientes respecto de los productos y
> servicios financieros que mantengan contratados con instituciones proveedoras de
> información, según sea aplicable, incluyendo: a) cuentas corrientes y sus líneas
> de crédito asociadas, cuentas a la vista, cuentas de provisión de fondos y cuentas
> de ahorro; b) tarjetas de crédito, con sus respectivas líneas de crédito
> asociadas; c) operaciones de crédito de dinero; d) pólizas de seguro; e)
> instrumentos de ahorro o inversión; f) servicios de operación de tarjetas y medios
> de pago similares, y g) otros productos o servicios financieros que defina la
> Comisión por norma de carácter general. Dicha información sólo podrá ser
> comunicada conforme a la autorización que otorgue el Cliente de acuerdo a lo
> dispuesto en artículo 23. La información e historial de transacciones realizadas no
> podrá tener una antigüedad superior a cinco años.
>
> 4. Comunicaciones entre proveedores de servicios financieros regulados en la ley
> N° 21.236, para los efectos del proceso de portabilidad financiera establecido en
> dicha legislación, según determine el reglamento de esa ley.
>
> 5. Datos o información necesaria para la prestación de servicios de
> iniciación de pagos, conforme a lo dispuesto en el artículo 20 y sujeto a previa
> autorización que otorgue el Cliente de acuerdo a lo dispuesto en el artículo 23.
>
> 6. Otros datos o información relativa a productos o servicios financieros o
> iniciación de otro tipo de transacciones que la Comisión pueda disponer mediante
> norma de carácter general, sujeto a la previa autorización que otorgue el Cliente.

### Cross-references
- Art. 18 — information-providing institutions (definition and list).
- Art. 19 — information-based service-providing institutions.
- Art. 20 — payment initiation service providers.
- Art. 23 — customer consent requirements.
- Law No. 21.236 — financial portability law (numeral 4).

---

## Article 18 — Information-providing institutions
**Spanish anchor:** Art. 18°
**Tags:** open-finance, data-providers, supervision, technical-standards

### Plain-English text

For the purposes set out in the preceding article, the following must participate in the Open Finance System (Sistema de Finanzas Abiertas, or SFA) as information-providing institutions (instituciones proveedoras de información): banks and issuers of credit cards, prepaid payment cards (tarjetas de pago con provisión de fondos), or any other system similar to such payment instruments that are authorised by the Commission (CMF), as well as such other institutions supervised by the Commission (CMF) as it determines by means of a general regulation (norma de carácter general), hereinafter the "Information-Providing Institutions (Instituciones Proveedoras de Información)." The participation of Information-Providing Institutions in the Open Finance System carries the obligation to grant access to and deliver the information that, pursuant to this law, is requested by Information-Based Service-Providing Institutions (Instituciones Proveedoras de Servicios Basados en Información), under the terms and conditions established therein.

To that end, the Commission (CMF) shall extend the obligation to participate in the Open Finance System to the institutions set out below, and may establish differentiated rules for entities according to their market relevance in terms of market share, number of Customers, availability of Customer data by category as set out in the preceding article, or other objective criteria:

a) Payment-card operators authorised by the Commission (CMF).

b) Savings-and-credit cooperatives (cooperativas de ahorro y crédito) supervised by the Commission (CMF), governed by the General Cooperatives Law (Ley General de Cooperativas), the consolidated, coordinated, and systematised text of which was established by Decree with Force of Law No. 5 of 2003 of the Ministry of the Economy, Development and Reconstruction.

c) Agents managing endorsable mortgage loans (mutuos hipotecarios endosables) and insurance companies regulated pursuant to Decree with Force of Law No. 251 of 1931 of the Ministry of Finance, on insurance companies, corporations, and commodity exchanges.

d) Institutions that place funds by means of money lending transactions (operaciones de crédito de dinero) on a mass scale, as set out in Article 31 of Law No. 18.010.

e) General fund managers (administradoras generales de fondos) and portfolio managers (administradores de cartera) regulated pursuant to Law No. 20.712, on the management of third-party funds.

f) Stockbrokers (corredoras de bolsa) regulated by Law No. 18.045 on the securities market.

g) Family Allowance Compensation Funds (Cajas de Compensación de Asignación Familiar) regulated by Law No. 18.833.

h) Entities registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) maintained by the Commission (CMF) pursuant to this law.

i) Other financial institutions supervised by the Commission (CMF) as it determines by means of a general regulation (norma de carácter general).

The Commission (CMF) shall determine, by means of a general regulation (norma de carácter general), the type of information that Information-Providing Institutions must communicate through the Open Finance System in accordance with the preceding article.

### Original Spanish

> Artículo 18.- Instituciones proveedoras de información. Para los efectos
> indicados en el artículo anterior, deberán participar en el Sistema de Finanzas
> Abiertas en calidad de instituciones proveedoras de información los bancos y
> emisores de tarjetas de crédito, tarjetas de pago con provisión de fondos o de
> cualquier otro sistema similar a los referidos medios de pago que se encuentren
> autorizados por la Comisión, así como aquellas instituciones fiscalizadas por la
> Comisión que ésta determine mediante norma de carácter general, en adelante, las
> "Instituciones Proveedoras de Información". La participación de las Instituciones
> Proveedoras de Información en el Sistema de Finanzas Abiertas conlleva la
> obligación de dar acceso y entregar la información que conforme a esta ley le sea
> solicitada por Instituciones Proveedoras de Servicios Basados en Información, en los
> términos y condiciones establecidas en ella.
>
> Al efecto, la Comisión extenderá la obligación de participar en el Sistema de
> Finanzas Abiertas a las instituciones que se indican a continuación, y podrá
> establecer normas diferenciadas para las entidades según su relevancia en cada
> mercado, en términos de participación de mercado, número de Clientes,
> disponibilidad de datos de Clientes según las categorías indicadas en el artículo
> anterior u otros criterios objetivos:
>
> a) Operadores de tarjetas de pago autorizados por la Comisión.
>
> b) Cooperativas de ahorro y crédito fiscalizadas por la Comisión, regidas por
> la Ley General de Cooperativas, cuyo texto refundido, concordado y sistematizado fue
> fijado por el decreto con fuerza de ley N° 5, de 2003, del Ministerio de Economía,
> Fomento y Reconstrucción.
>
> c) Agentes administradores de mutuos hipotecarios endosables y compañías de
> seguros reguladas conforme al decreto con fuerza de ley N° 251, de 1931, del
> Ministerio de Hacienda, sobre compañías de seguros, sociedades anónimas y bolsas
> de comercio.
>
> d) Instituciones que coloquen fondos por medio de operaciones de crédito de
> dinero de manera masiva, conforme a lo señalado en el artículo 31 de la ley N°
> 18.010.
>
> e) Administradoras generales de fondos y administradores de cartera reguladas
> conforme a la ley N° 20.712, sobre administración de fondos de terceros.
>
> f) Corredoras de bolsa regulados por la ley N° 18.045 de Mercado de Valores.
>
> g) Cajas de Compensación de Asignación Familiar reguladas por la ley N°
> 18.833.
>
> h) Entidades inscritas en el Registro de Prestadores de Servicios Financieros
> que lleva la Comisión conforme a esta ley.
>
> i) Otras instituciones financieras fiscalizadas por la Comisión, que ésta
> determine mediante norma de carácter general.
>
> La Comisión determinará, por norma de carácter general, el tipo de
> información que deberán comunicar las Instituciones Proveedoras de Información a
> través del Sistema de Finanzas Abiertas conforme a lo indicado en el artículo
> anterior.

### Cross-references
- Art. 17 — data categories that information-providing institutions must share.
- Art. 19 — information-based service-providing institutions that request data from Art. 18 entities.
- Art. 27 — CMF supervision and rulemaking powers over System participants.
- Registry of Financial-Service Providers → Art. 3(12), Art. 5.

---

## Article 19 — Information-based service-providing institutions
**Spanish anchor:** Art. 19°
**Tags:** open-finance, data-recipients, consent, supervision, technical-standards

### Plain-English text

Those financial-information-enabled service providers (proveedores de servicios habilitados por información financiera) that voluntarily register in the public Registry of Information-Based Service Providers (Registro de Proveedores de Servicios basados en Información) maintained by the Commission (CMF) may participate in the Open Finance System (Sistema de Finanzas Abiertas, or SFA) to consult, access, and receive data for the purpose of providing services to Customers, hereinafter the "Information-Based Service Providers (Proveedores de Servicios basados en Información)." Entities qualifying as Information-Providing Institutions listed in the preceding article and entities registered in the Registry of Financial-Service Providers (Registro de Prestadores de Servicios Financieros) maintained by the Commission (CMF) may also voluntarily participate as Information-Based Service Providers, without the need for a new registration, but subject to compliance with the requirements applicable to registered entities.

The Commission (CMF) shall determine by means of a general regulation (norma de carácter general) the requirements and supporting documents that must accompany the providers referred to above in order to register in the Registry of Information-Based Service Providers. For those purposes, they must demonstrate compliance with the technical and information-security requirements established in Articles 21 and 22, which may set differentiated requirements depending on the type of data to which Information-Based Service Providers may have access. The Commission (CMF) must rule on registration applications in the aforementioned Registry within six months from the date of the respective application. That period shall be suspended if the Commission (CMF), by digital communication, asks the applicant to remedy the technical and information-security deficiencies detected, and shall only resume once that procedure has been completed. Once the deficiencies referred to above have been remedied and the period referred to in this article has expired, the Commission (CMF) must rule on the application and, where appropriate, effect the registration within three business days (días hábiles).

The Commission (CMF) may, at any time and by a reasoned decision (resolución fundada), suspend the authorisation to carry out information queries under the Open Finance System with respect to Information-Based Service Providers that have ceased to comply with the requirements established by this law, or as a precautionary measure when necessary for the adequate protection of Customers. This is without prejudice to any criminal and administrative sanctions applicable for non-compliance.

While registered in the aforementioned Registry, Information-Based Service Providers may access the interfaces regulated by Article 21 that Information-Providing Institutions enable for information queries. Information-Providing Institutions must communicate the information requested by the Information-Based Service Provider, which must have the consent (consentimiento) granted by the respective Customer under the terms of Article 23, without it being necessary for there to be a contractual relationship between the two institutions.

Those who have committed most serious and repeated violations (infracciones gravísimas y reiteradas) within a twenty-four-month period of the legal obligations regarding personal data protection (protección de datos personales) shall not (no podrán) register in the Registry of Information-Based Service Providers nor voluntarily participate as Information-Based Service Providers.

### Original Spanish

> Artículo 19.- Instituciones Proveedoras de Servicios basados en Información.
> Podrán participar en el Sistema de Finanzas Abiertas para consultar, acceder y
> recibir datos para efectos de proveer servicios a los Clientes, aquellos proveedores
> de servicios habilitados por información financiera que se registren voluntariamente
> para estos efectos en el Registro de Proveedores de Servicios basados en Información
> de carácter público que llevará la Comisión, en adelante, los "Proveedores de
> Servicios basados en Información". Podrán participar voluntariamente como estos
> últimos las entidades que califiquen como Instituciones Proveedoras de Información
> indicadas en el artículo anterior y las entidades inscritas en el Registro de
> Prestadores de Servicios Financieros que lleva la Comisión, sin necesidad de nueva
> inscripción, pero sujeto al cumplimiento de los requisitos aplicables a las
> entidades inscritas.
>
> La Comisión determinará mediante norma de carácter general los requisitos y
> antecedentes que deberán acompañar los proveedores antes referidos para inscribirse
> en el Registro de Proveedores de Servicios basados en Información. Deberán
> acreditar, para tales efectos, el cumplimiento de los requisitos técnicos y de
> seguridad de información establecidos en los artículos 21 y 22, los cuales podrán
> establecer exigencias diferenciadas en atención al tipo de datos a los que los
> Proveedores de Servicios basados en Información podrán acceder. La Comisión
> deberá pronunciarse sobre las solicitudes de inscripción en el Registro antes
> mencionado dentro del plazo de seis meses contado desde la fecha de la solicitud
> respectiva. Dicho plazo se suspenderá si la Comisión, mediante comunicación
> digital, pide al solicitante subsanar las deficiencias técnicas y de seguridad de
> información que se hubieren detectado y sólo se reanudará cuando se haya cumplido
> con dicho trámite. Subsanadas las deficiencias antes aludidas y vencido el plazo a
> que se refiere este artículo, la Comisión deberá pronunciarse sobre la solicitud
> y, en su caso, efectuar la inscripción dentro de tres días hábiles.
>
> La Comisión, en cualquier momento y por resolución fundada, podrá suspender
> la autorización para realizar consultas de información bajo el Sistema de Finanzas
> Abiertas a aquellos Proveedores de Servicios basados en Información que hayan dejado
> de cumplir con los requisitos establecidos por la presente ley o como medida
> preventiva cuando resulte necesario para el debido resguardo de los Clientes. Lo
> anterior, sin perjuicio de las sanciones penales y administrativas que resulten
> aplicables por el incumplimiento.
>
> Mientras se mantengan inscritos en el mencionado Registro, los Proveedores de
> Servicios basados en Información podrán acceder a las interfaces reguladas en el
> artículo 21 que habiliten las Instituciones Proveedoras de Información para
> formular consultas de información. Las Instituciones Proveedoras de Información
> deberán comunicar la información solicitada por el Proveedor de Servicios basados
> en Información, el que deberá contar con el consentimiento otorgado por el
> respectivo Cliente en los términos del artículo 23, sin que resulte necesario
> contar con una relación contractual entre ambas instituciones.
>
> No podrán inscribirse en el Registro de Proveedores de Servicios basados en
> Información ni participar voluntariamente como Proveedores de Servicios basados en
> Información quienes hubieren cometido infracciones gravísimas y reiteradas en un
> período de veinticuatro meses a las obligaciones legales en materia de protección
> de datos personales.

### Cross-references
- Art. 18 — information-providing institutions (the data source side).
- Art. 21 — interfaces that Information-Based Service Providers access.
- Art. 22 — security standards that applicants must comply with.
- Art. 23 — customer consent requirements for information queries.
- Art. 27 — CMF supervision including power to suspend authorisation.

---

## Article 20 — Payment initiation service providers
**Spanish anchor:** Art. 20°
**Tags:** open-finance, payment-initiation, data-recipients, consent, customer-protection, technical-standards

### Plain-English text

Payment initiation service providers (Proveedores de Servicios de Iniciación de Pagos) may participate in the Open Finance System (Sistema de Finanzas Abiertas, or SFA) as Information-Based Service-Providing Institutions (Instituciones Proveedoras de Servicios basados en Información). These shall be understood as entities that provide services to Customers who are holders of current accounts, sight accounts, or provision-of-funds accounts (cuentas de provisión de fondos), pursuant to which they may instruct — in the Customer's name and on behalf of the bank or financial institution that provides the relevant account, hereinafter "Account-Providing Institutions (Instituciones Proveedoras de Cuentas)" — the execution of payment orders or electronic fund transfers (transferencias electrónicas de fondos), including predefined recurring payments (pagos recurrentes predefinidos) in favour of the third-party beneficiaries indicated by the customers, charged to their respective accounts and payment instruments.

In order to act as payment initiation service providers, entities must register in the public Registry of Payment Initiation Service Providers (Registro de Proveedores de Servicios de Iniciación de Pagos) maintained by the Commission (CMF), which shall determine by means of a general regulation (norma de carácter general) the supporting documents they must submit for that purpose, the risk management and control requirements (requisitos de gestión y control de riesgo), guarantees (garantías), customer information obligations, and other conditions they must demonstrate for the provision of these services and interconnection with the account-providing or payment-instrument-providing institutions referred to above. The Commission (CMF) must rule on the registration application within six months from the date of the respective application. That period shall be suspended if the Commission (CMF), by a reasoned digital communication, asks the applicant to correct errors or omissions in the application, and shall only resume once that procedure has been completed.

Notwithstanding the foregoing, the Commission (CMF) shall be empowered to issue differentiated rules for payment initiation service providers regarding compliance with any of the requirements or obligations established in this law, taking into account the nature and volume of operations performed by the payment initiation service providers and the risks thereby assumed by supervised institutions, among other objective circumstances that must be considered for this purpose in the general regulation (norma de carácter general) issued to that effect.

Payment initiation service providers shall not (no podrán) have access to or hold, at any time, the funds of Customers of Account-Providing Institutions associated with the payment orders instructed, nor may they access or hold Customer information for purposes other than the provision of the service regulated in this article. Exceptionally, payment initiation service providers may incorporate into their operating model the possibility of accessing and temporarily holding the funds of those Customers, subject to compliance with the rules established by the Central Bank of Chile (Banco Central de Chile) to ensure the normal functioning of the payments in which they intervene, which shall include solvency requirements, liquidity requirements, maximum payment deadlines, and risk management requirements, among other requirements that the Central Bank determines for that purpose. In any event, the maximum payment deadline to third-party beneficiaries of the payment orders or electronic fund transfers shall not (no podrá) exceed seventy-two hours.

The execution of the payment order communicated by the payment initiation service provider, with the prior consent (consentimiento) of the Customer, must be executed by the Account-Providing Institution (Institución Proveedora de Cuenta) without the need for a prior contractual relationship with that provider and without any discrimination with respect to payment orders transmitted directly by the Customer. This is without prejudice to the Customer information obligations regarding the execution of the aforementioned payment order.

Likewise, the execution of such payment order shall not (no podrá) give rise to the charging of fees or additional charges by the account-providing institution to the Customer who holds the account, beyond what has already been agreed for the use of the respective account or payment instrument or for making transfers charged to it. Nor shall charges be made by the account-providing institution to the payment initiation service provider.

For the purposes of Law No. 20.009, payment initiation service providers shall be understood to provide a service associated with electronic transactions (transacciones electrónicas).

Notwithstanding what is stated in the first paragraph, payment initiation service providers that have committed most serious and repeated violations (infracciones gravísimas y reiteradas) within a twenty-four-month period of the legal obligations regarding personal data protection shall not (no podrán) participate in the Open Finance System as Information-Based Service-Providing Institutions.

### Original Spanish

> Artículo 20.- Proveedores de servicios de iniciación de pagos. Podrán
> participar en el Sistema de Finanzas Abiertas en calidad de Instituciones Proveedoras
> de Servicios basados en Información los Proveedores de Servicios de Iniciación de
> Pagos. Se entenderá por tales a aquellas entidades que provean servicios a Clientes
> que sean titulares de cuentas corrientes, cuentas vistas o cuentas de provisión de
> fondos, conforme a los cuales puedan instruir, a nombre del Cliente y ante el banco o
> la institución financiera proveedora de la cuenta respectiva, en adelante,
> "Instituciones Proveedoras de Cuentas", la ejecución de órdenes de pago o
> transferencias electrónicas de fondos, incluyendo pagos recurrentes predefinidos en
> favor de los terceros beneficiarios que los clientes indiquen, con cargo a sus
> respectivas cuentas y medios de pago.
>
> Para poder actuar como Proveedores de Servicios de Iniciación de Pagos, las
> entidades deberán inscribirse en el Registro de Proveedores de Servicios de
> Iniciación de Pagos de carácter público, que llevará la Comisión, la cual
> determinará mediante norma de carácter general los antecedentes que deberán
> acompañar para tales efectos, los requisitos de gestión y control de riesgo,
> garantías, obligaciones de información a Clientes y demás condiciones que deberán
> acreditar para la prestación de estos servicios e interconexión con las
> instituciones proveedoras de las cuentas o medios de pago antes referidos. La
> Comisión deberá pronunciarse respecto de la solicitud de inscripción dentro del
> plazo de seis meses contado desde la fecha de la solicitud respectiva. Dicho plazo se
> suspenderá si la Comisión, mediante comunicación fundada en formato digital, pide
> al solicitante corregir los errores u omisiones que presente su solicitud y sólo se
> reanudará cuando se haya cumplido con dicho trámite.
>
> Con todo, la Comisión estará facultada para dictar normas diferenciadas a los
> Proveedores de Servicios de Iniciación de Pagos respecto del cumplimiento de
> cualesquiera de los requisitos o exigencias establecidas en esta ley, atendiendo a la
> naturaleza y volumen de operaciones que realicen los proveedores de servicios de
> iniciación de pagos y riesgos que por estos conceptos asuman las instituciones
> fiscalizadas, entre otras circunstancias de carácter objetivo que deban considerarse
> para este propósito en la norma de carácter general que se dicte al efecto.
>
> Los Proveedores de Servicios de Iniciación de Pagos no podrán tener acceso ni
> mantener, en ningún momento, los dineros de los Clientes de las Instituciones
> Proveedoras de Cuentas asociados a las órdenes de pago instruidas, ni podrán
> acceder o mantener información de los Clientes para fines distintos de la
> prestación del servicio regulado en este artículo. Excepcionalmente, los
> Proveedores de Servicios de Iniciación de Pagos podrán contemplar en su modelo de
> funcionamiento la posibilidad de acceder y mantener en forma transitoria los dineros
> de los referidos Clientes, sujeto a que cumplan las normas que establezca el Banco
> Central de Chile para cautelar el normal funcionamiento de los pagos en que
> intervengan, las que incluirán requisitos de solvencia, liquidez, plazo máximo de
> pago y gestión de riesgos, entre otros requisitos que el Banco determine al efecto.
> En todo caso, el plazo máximo de pago a los terceros beneficiarios de las órdenes
> de pago o transferencias electrónicas no podrá superar las setenta y dos horas.
>
> La ejecución de la orden de pago comunicada por el proveedor de servicios de
> iniciación de pago, con consentimiento previo del Cliente, deberá ejecutarse por
> parte de la Institución Proveedora de Cuenta sin necesidad de que exista una
> relación contractual previa con dicho proveedor y sin discriminación alguna con
> respecto de las órdenes de pago transmitidas directamente por el cliente. Lo
> anterior, sin perjuicio de las obligaciones de información al Cliente respecto de la
> ejecución de la orden de pago antes referida.
>
> De igual modo, la ejecución de dicha orden no podrá dar lugar a cobro de
> comisiones o cobros adicionales por parte de la institución proveedora de cuenta al
> Cliente titular de ella, respecto a lo que ya hubiera convenido para el uso de la
> respectiva cuenta o medio de pago o la realización de transferencias con cargo a
> ésta. Tampoco se podrán efectuar cobros por parte de la institución proveedora de
> la cuenta al proveedor de servicios de iniciación de pago.
>
> Para los efectos de las disposiciones de la ley N° 20.009, se entenderá que
> los Proveedores de Servicio de Iniciación de Pago prestan un servicio asociado a
> transacciones electrónicas.
>
> No obstante lo señalado en el inciso primero, no podrán participar en el
> Sistema de Finanzas Abiertas en calidad de Instituciones Proveedoras de Servicios
> basados en Información los Proveedores de Servicios de Iniciación de Pagos que
> hubieren cometido infracciones gravísimas y reiteradas en un período de
> veinticuatro meses a las obligaciones legales en materia de protección de datos
> personales.

### Cross-references
- Art. 17(5) — payment initiation data within the SFA scope.
- Art. 19 — Information-Based Service Providers (the category in which payment initiation providers participate).
- Art. 23 — customer consent requirements for payment initiation.
- Art. 24 — liability of participating institutions.
- Law No. 20.009 — fraud liability in electronic transactions (para. 7 reference).
- Central Bank of Chile — prudential rules for transitional fund holding.

---

## Article 21 — Means of information delivery and exchange
**Spanish anchor:** Art. 21°
**Tags:** open-finance, technical-standards, security, data-providers, data-recipients

### Plain-English text

The delivery and exchange of information referred to in this law by Information-Providing Institutions (Instituciones Proveedoras de Información), Information-Based Service Providers (Proveedores de Servicios basados en Información), Account-Providing Institutions (Instituciones Proveedoras de Cuentas), and payment initiation service providers (Proveedores de Servicios de Iniciación de Pagos) participating in the Open Finance System (Sistema de Finanzas Abiertas, or SFA) must be carried out through one or more interfaces (interfaces), of remote and automated access, that System participants must maintain available, the minimum standards (estándares mínimos) for which shall be determined by the Commission (CMF) by means of a general regulation (norma de carácter general).

Such regulation shall establish the requirements and conditions necessary for the design, development, and security mechanisms of these interfaces for the access, sending, or obtaining of data and information in a standardised manner, and shall ensure interoperability among participating institutions and operational continuity through an alternative information-exchange mechanism in the event that one or more of the respective interfaces are disabled, as well as any other requirement that the Commission (CMF) determines to be necessary for the secure and optimal operation of the system. The Commission (CMF) may establish differentiated requirements in consideration of the type of data or information to be transmitted through the interface.

Without prejudice to the foregoing, upon an information exchange request, the parties involved must keep a record of at least: the identification of the requesting party, the reason for and purpose of the request, the type of data requested, and the date of the exchange.

> **TN:** "interfaces de acceso remoto y automatizado" is rendered as "remote and automated access interfaces" rather than "application programming interfaces (API)" because the article uses the broader term "interfaces" throughout — the API terminology appears in Art. 27. The Commission's general regulation will specify whether APIs are the mandated technical form.

### Original Spanish

> Artículo 21.- Medios de entrega e intercambio de información. La entrega y el
> intercambio de información referida en esta ley por parte de las Instituciones
> Proveedoras de Información, Proveedores de Servicios basados en Información,
> Instituciones Proveedoras de Cuentas y Proveedores de Servicios de Iniciación de
> Pagos participantes en el Sistema de Finanzas Abiertas deberá efectuarse por medio
> de una o más interfaces, de acceso remoto y automatizado que deberán mantener
> disponible los participantes del Sistema de Finanzas Abiertas, cuyos estándares
> mínimos determinará la Comisión mediante norma de carácter general.
>
> Dicha normativa establecerá los requisitos y condiciones necesarios para el
> diseño, desarrollo y mecanismos de seguridad de estas interfaces para el acceso,
> envío u obtención de datos e información en forma estandarizada, y asegurará la
> interoperabilidad entre instituciones participantes y la continuidad operacional a
> través de un mecanismo alternativo de intercambio de información en caso que la o
> las interfaces respectivas se encuentren inhabilitadas, así como como cualquier otro
> requisito que la Comisión determine como necesario para el seguro y óptimo
> funcionamiento del sistema. La Comisión podrá establecer exigencias diferenciadas
> en consideración al tipo de datos o información que se transmitirá a través de la
> interfaz.
>
> Sin perjuicio de lo anterior, frente a un requerimiento de intercambio de
> información, los intervinientes deberán dejar constancia de, al menos, la
> individualización del requirente, el motivo y el propósito del requerimiento, el
> tipo de datos que se requieren y la fecha del intercambio.

### Cross-references
- Art. 19 — Information-Based Service Providers access interfaces enabled by Art. 18 entities.
- Art. 22 — security standards applicable to the same participants.
- Art. 25 — cost allocation excludes interface development costs (Art. 25, para. 4).
- Art. 27 — CMF pilot testing of interfaces (Art. 27, para. 3).

---

## Article 22 — Information security standards
**Spanish anchor:** Art. 22°
**Tags:** open-finance, security, technical-standards, data-providers, data-recipients

### Plain-English text

Information-Providing Institutions (Instituciones Proveedoras de Información), Information-Based Service Providers (Proveedores de Servicios basados en Información), Account-Providing Institutions (Instituciones Proveedoras de Cuentas), and payment initiation service providers (Proveedores de Servicios de Iniciación de Pagos) participating in the Open Finance System (Sistema de Finanzas Abiertas, or SFA) must adopt the measures necessary to comply with the minimum information security, cybersecurity (ciberseguridad), and risk management and internal control policy standards (políticas de gestión de riesgos y control interno) established by the Commission (CMF) by means of a general regulation (norma de carácter general), with the purpose of safeguarding the confidentiality, integrity, and availability of data and information, and preventing risks to the information systems that process them, in order to prevent the unauthorised disclosure and/or modification of information, and unauthorised interruptions of technological systems. For those purposes, they must take into account the risk inherent in each type of information and, likewise, the status of data as sensitive (dato sensible) within the meaning of Law No. 19.628. The Commission (CMF) may establish differentiated requirements based on the risk associated with the type of financial products or services or type of data or information to which Information-Based Service Providers and payment initiation service providers may have access, as applicable.

Upon breaches of the security measures referred to in the preceding paragraph, institutions participating in the Open Finance System must report security incidents to the Commission (CMF) without delay, by the means and under the terms and conditions determined by the Commission (CMF) by means of a general regulation (norma de carácter general), and shall adopt the corresponding risk-mitigation measures.

### Original Spanish

> Artículo 22.- Estándares de seguridad de información. Las Instituciones
> Proveedoras de Información, los Proveedores de Servicios basados en Información,
> las Instituciones Proveedoras de Cuentas y los Proveedores de Servicios de
> Iniciación de Pagos participantes en el Sistema de Finanzas Abiertas deberán
> adoptar las medidas necesarias para cumplir con los estándares mínimos de seguridad
> de información, ciberseguridad y políticas de gestión de riesgos y control interno
> que la Comisión establezca por norma de carácter general, con el objeto de
> resguardar la confidencialidad, integridad y disponibilidad de los datos y de la
> información, y prevenir riesgos a los sistemas de información que los procesan, con
> el propósito de prevenir la divulgación y/o modificación no autorizada de la
> información, y las interrupciones no autorizadas de los sistemas tecnológicos.
> Deberán tener en consideración para tales efectos, el riesgo inherente a cada tipo
> de información, como, asimismo, la calidad de dato sensible conforme a las
> disposiciones de la ley N° 19.628. La Comisión podrá establecer exigencias
> diferenciadas en función del riesgo asociado al tipo de productos o servicios
> financieros o tipo de datos o información al que tendrán acceso los Proveedores de
> Servicios basados en Información y los Proveedores de Servicios de Iniciación de
> Pago, según corresponda.
>
> Ante vulneraciones de las medidas de seguridad señaladas en el inciso anterior,
> las instituciones participantes en el Sistema de Finanzas Abiertas deberán reportar
> los incidentes de seguridad a la Comisión sin dilaciones, por los medios y en los
> términos y condiciones que la Comisión determine por norma de carácter general, y
> adoptarán las medidas de mitigación de riesgos correspondientes.

### Cross-references
- Art. 19 — applicants to Information-Based Service Provider registry must demonstrate Art. 22 compliance.
- Art. 21 — interface security mechanisms (design and development requirements).
- Art. 24 — responsibility for data integrity and confidentiality.
- Law No. 19.628 — definition of sensitive personal data (datos personales sensibles).

---

## Article 23 — Consent and authentication requirements
**Spanish anchor:** Art. 23°
**Tags:** open-finance, consent, customer-protection, security, data-recipients, payment-initiation

### Plain-English text

Information-Based Service Providers (Proveedores de Servicios basados en Información) and payment initiation service providers (Proveedores de Servicio de Iniciación de pago), as applicable, must adopt Customer authentication (autentificación del Cliente) mechanisms and obtain the Customer's prior and explicit consent (consentimiento previo y explícito) in order to carry out information queries or initiate payments on their behalf through the Open Finance System (Sistema de Finanzas Abiertas, or SFA), as applicable, through expeditious and secure electronic or digital channels.

In order to query financial information (información financiera) from Information-Providing Institutions (Instituciones Proveedoras de Información), for the purpose of providing services to customers based on that financial information, the customer's consent must be expressed freely, in an informed manner (informada), explicitly, and specifically as to the type of financial information (información financiera), the purpose, and the maximum validity period of that authorisation, and shall identify the Information-Based Service Provider.

In the case of a payment initiation, the data necessary for the instruction of the payment order pursuant to Article 20 must be indicated, including data on the relevant account or payment instrument, the transaction amount, the payment date, identification of the respective payment initiation service provider, and the third-party beneficiary of the payment. Consent may be granted once in the case of a predefined recurring payment designated by the Customer.

The Customer may revoke the consent (consentimiento) granted at any time, and it shall be prohibited for the Information-Based Service Provider or payment initiation service provider concerned to continue using the consent for new information queries or for the initiation of new payment orders.

The Commission (CMF), by means of a general regulation (norma de carácter general), shall establish the manner in which the express consent (consentimiento expreso) of Customers shall be deemed to have been granted for all legal purposes and the manner in which the Customer may revoke that consent. Likewise, the Commission (CMF) shall establish the information that Information-Based Service Providers and payment initiation service providers must provide to Customers regarding the information requests or payment initiations executed pursuant to the authorisations granted.

Information-Providing Institutions and Account-Providing Institutions (Instituciones Proveedoras de Cuenta), as applicable, must adopt mechanisms for authenticating Customers who have given their consent to Information-Based Service Providers or payment initiation service providers, as the case may be. The customer authentication and confirmation mechanisms referred to above must conform to the minimum standards defined by the Commission (CMF) by means of a general regulation (norma de carácter general), which may consider differentiated rules, including enhanced authentication (autenticación reforzada) mechanisms, taking into account the risk and type of data or services involved. Customer authentication mechanisms for these purposes must be compatible with the methods already available at Information-Providing Institutions and Account-Providing Institutions for access to their electronic channels.

Information-Providing Institutions must implement mechanisms for authenticating Information-Based Service Providers and payment initiation service providers, in order to verify that they are registered in the registries maintained by the Commission (CMF), in accordance with the standards defined by the Commission (CMF) by means of a general regulation (norma de carácter general).

> **TN:** "consentimiento" throughout this article is used in the financial-service-customer consent sense (consent to data sharing or payment initiation), not in the personal-data-subject sense of Art. 12 of Ley 19.628. Both senses are present in this law: the customer consent here governs the operational authorisation mechanism; personal-data consent under Ley 19.628 governs the underlying data processing legal basis. The two regimes co-exist and are not collapsed in the translation.

### Original Spanish

> Artículo 23.- Requisitos del consentimiento y autenticación. Los Proveedores
> de Servicios basados en Información y los Proveedores de Servicio de Iniciación de
> pago, en su caso, deberán adoptar mecanismos de autentificación del Cliente y
> obtener su consentimiento previo y explícito para realizar consultas de información
> o iniciar pagos en su nombre a través del Sistema de Finanzas Abiertas, según
> corresponda, a través de medios o canales electrónicos o digitales expeditos y
> seguros.
>
> Para consultar información financiera a Instituciones Proveedoras de
> Información, a efectos de proveer servicios a los clientes basados en dicha
> información financiera, el consentimiento del cliente deberá manifestarse en forma
> libre, informada, expresa y específica en cuanto al tipo de información financiera,
> la finalidad y el periodo máximo de validez de esa autorización, e identificará al
> Proveedor de Servicios basados en Información.
>
> Tratándose de una iniciación de pagos, se deberá indicar los datos necesarios
> para la instrucción de la orden de pago conforme al artículo 20, incluyendo datos
> de la cuenta o medio de pago respectivo, del valor de la transacción, fecha de pago,
> identificación del Proveedor de Servicio de Iniciación de pago respectivo y tercero
> beneficiario del pago. Podrá otorgarse el consentimiento una sola vez tratándose de
> un pago recurrente predefinido por el Cliente.
>
> Éste podrá revocar en cualquier momento el consentimiento otorgado, y estará
> prohibido al Proveedor de Servicios basados en Información o Proveedor de Servicios
> de Iniciación de Pago respectivo continuar utilizando el consentimiento para nuevas
> consultas de información o para la iniciación de nuevas órdenes de pago.
>
> La Comisión, mediante norma de carácter general, establecerá la forma en que
> se reputará otorgado el consentimiento expreso de los Clientes para todos los
> efectos legales y la forma en que el Cliente podrá revocar dicho consentimiento.
> Asimismo, la Comisión establecerá la información que los Proveedores de Servicios
> basados en Información y Proveedores de Servicio de Iniciación de pago deberán
> proporcionar a los Clientes respecto de las solicitudes de información o iniciación
> de pagos ejecutadas conforme a las autorizaciones otorgadas.
>
> Las Instituciones Proveedoras de Información e Instituciones Proveedoras de
> Cuenta, en su caso, deberán adoptar mecanismos para la autenticación de los
> Clientes que hubieren dado su consentimiento a los Proveedores de Servicios basados
> en Información o los Proveedores de Servicio de Iniciación de pago, según sea el
> caso. Los medios de autenticación y confirmación de Clientes antes referidos
> deberán ajustarse a los estándares mínimos que defina la Comisión por norma de
> carácter general, los cuales podrán considerar reglas diferenciadas, incluyendo
> mecanismos de autenticación reforzada, considerando el riesgo y tipo de datos o
> servicios involucrados. Los mecanismos de autenticación de Clientes para estos
> efectos deberán ser compatibles con los métodos ya disponibles en las Instituciones
> Proveedoras de Información e Instituciones Proveedoras de Cuentas para el acceso a
> sus canales electrónicos.
>
> Las Instituciones Proveedoras de Información deberán implementar mecanismos
> para la autenticación de los Proveedores de Servicios basados en Información y
> Proveedores de Servicio de Iniciación de Pagos, a fin de verificar que se encuentren
> inscritas en los Registros que lleva la Comisión, conforme a los estándares que
> ésta defina por norma de carácter general.

### Cross-references
- Art. 17(2), (3), (5) — data categories subject to customer consent.
- Art. 19 — Information-Based Service Providers must hold consent (Art. 19, para. 4).
- Art. 20 — payment initiation; consent elements for payment orders.
- Art. 24 — responsibility of participants tied to consent-compliant data use.
- Law No. 19.628, Art. 12 — personal-data consent (parallel but distinct legal basis).

---

## Article 24 — Liability of institutions participating in the Open Finance System
**Spanish anchor:** Art. 24°
**Tags:** open-finance, customer-protection, consent, security, data-providers, data-recipients

### Plain-English text

Information-Providing Institutions (Instituciones Proveedoras de Información), Account-Providing Institutions (Instituciones Proveedoras de Cuentas), Information-Based Service Providers (Proveedores de Servicios basados en Información), and participating payment initiation service providers (Proveedores de Servicios de Iniciación de Pagos) shall be responsible for safeguarding the integrity, availability, security, and confidentiality of the data involved in each transaction and the adequate privacy of Customer information. This is without prejudice to compliance with the other legal and regulatory requirements applicable to them in relation to the data processing (tratamiento de datos) each of them carries out and the provisions of Law No. 19.628 on the protection of private life.

The access, delivery, and exchange of information between institutions participating in the Open Finance System (Sistema de Finanzas Abiertas, or SFA) in compliance with the applicable provisions of this law and pursuant to the consent (consentimiento) granted by the Customer shall not be understood as a violation of the confidentiality, secrecy, and reserve obligations imposed on Information-Providing Institutions or Account-Providing Institutions pursuant to applicable laws or regulations.

Information-Based Service Providers and payment initiation service providers must implement the necessary measures to guarantee security in the data processing (tratamiento de datos) they carry out in the context of financial information access queries and payment initiations, respectively, with particular protection as regards the purposes for which the Customer authorised it, and without being able to use, store, or access Customer data not covered by the authorisation or consent referred to above, or where that consent has been revoked by the Customer or its validity period has expired. They must likewise adopt the necessary measures and respond to Customers in the event of alteration, destruction, loss, unauthorised processing (tratamiento), communication, or access to Customer data.

Information-Based Service Providers and payment initiation service providers must interrupt access to information and the making of new payment orders as soon as the Customer withdraws their consent or the consent's validity period expires, or where there are vulnerabilities that put Customer information at risk. In the latter case, they must communicate that situation to the Customer, the Commission (CMF), and the respective Information-Providing Institution, under the terms defined by the Commission (CMF) by means of a general regulation (norma de carácter general).

Participating institutions shall be responsible for handling Customer queries and complaints regarding the data and services exchanged through the Open Finance System in which they have participated, for which purpose they must provide Customer service mechanisms, without prejudice to the responsibilities that correspond to them pursuant to the provisions of this law or other laws applicable to them under the general legal framework.

### Original Spanish

> Artículo 24.- Responsabilidad de instituciones participantes en el Sistema de
> Finanzas Abiertas. Las Instituciones Proveedoras de Información, Instituciones
> Proveedoras de Cuentas, los Proveedores de Servicios basados en Información y
> Proveedores de Servicios de Iniciación de Pagos participantes serán responsables de
> resguardar la integridad, disponibilidad, seguridad y confidencialidad de los datos
> involucrados en cada transacción y la adecuada privacidad de la información de los
> Clientes. Lo anterior, sin perjuicio del cumplimiento de las demás exigencias
> legales y normativas que les resulten aplicables en relación con el tratamiento de
> datos que cada uno de ellos realice y las disposiciones de la ley N°19.628, sobre
> protección de la vida privada.
>
> El acceso, entrega e intercambio de información entre instituciones
> participantes del Sistema de Finanzas Abiertas en cumplimiento de las disposiciones
> aplicables en esta ley y conforme al consentimiento otorgado por el Cliente, no se
> entenderá como violación a las obligaciones de confidencialidad, reserva y secreto
> impuestas a las Instituciones Proveedoras de Información o Instituciones Proveedoras
> de Cuentas conforme a las leyes o normativas aplicables.
>
> Los Proveedores de Servicios basados en Información y los Proveedores de
> Servicios de Iniciación de Pagos deberán implementar las medidas necesarias para
> garantizar la seguridad en el tratamiento de datos que realicen en el contexto de las
> consultas de acceso a información financiera e iniciación de pagos,
> respectivamente, con especial resguardo respecto de los fines para los cuales fue
> autorizado por el Cliente, sin que puedan utilizar, almacenar o acceder a datos del
> Cliente no comprendidos dentro de la autorización o consentimiento antes referida o
> en caso que dicho consentimiento haya sido revocado por el Cliente o haya expirado su
> periodo de validez. Asimismo, deberán adoptar las medidas necesarias y responder
> ante los Clientes en caso de alteración, destrucción, pérdida, tratamiento o
> comunicación o acceso no autorizado a datos de los Clientes.
>
> Los Proveedores de Servicios basados en Información y los Proveedores de
> Servicios de Iniciación de Pagos deberán interrumpir el acceso de información y la
> realización de nuevas órdenes de pago tan pronto el Cliente retire su
> consentimiento o expire su periodo de validez o en caso que existan vulnerabilidades
> que pongan en riesgo la información de los Clientes. En este último caso deberán
> comunicar dicha situación al Cliente, a la Comisión y a la Institución Proveedora
> de Información respectiva, en los términos que la Comisión defina mediante norma
> de carácter general.
>
> Las instituciones participantes serán responsables de atender las consultas y
> reclamos de los Clientes respecto de los datos y servicios intercambiados a través
> del Sistema de Finanzas Abiertas en que hayan tenido participación, para lo cual
> deberán disponer de mecanismos de atención de Clientes, sin perjuicio de las
> responsabilidades que les correspondan conforme a las disposiciones de esta ley o
> demás leyes que les resulten aplicables conforme al ordenamiento jurídico general.

### Cross-references
- Art. 22 — information security standards underpinning the obligations in this article.
- Art. 23 — consent revocation triggers the obligation to interrupt data access (para. 4).
- Law No. 19.628 — personal data processing obligations applicable to all participants.
- Law No. 19.496 — consumer protection law (customer complaint mechanisms, para. 5).

---

## Article 25 — Cost allocation for information queries in the Open Finance System
**Spanish anchor:** Art. 25°
**Tags:** open-finance, data-providers, data-recipients, technical-standards

### Plain-English text

Information-Providing Institutions (Instituciones Proveedoras de Información) shall not (no podrán) charge Information-Based Service Providers (Proveedores de Servicios basados en Información) for communicating the Customer data information requested through the interfaces defined for the Open Finance System (Sistema de Finanzas Abiertas, or SFA), except for the reimbursement of direct incremental costs (costos incrementales directos) that they must incur to address the increase in information requests received to the extent those exceed the volume threshold of information requests defined by the Commission (CMF).

The Commission (CMF) shall establish, by means of a general regulation (norma de carácter general), the parameters for determining reimbursable costs and the volume thresholds of information requests above which reimbursement is applicable, taking into account the volume and type of data to be delivered and the incremental operating costs of the interfaces.

The direct incremental costs that the Information-Providing Institution requests to be reimbursed must be set on the basis of public, objective, equitable, and non-discriminatory conditions among participating institutions. In the event of non-compliance by an Information-Based Service Provider in paying the reimbursable costs referred to above, the Information-Providing Institution must continue attending information queries that do not exceed the aforementioned thresholds, unless there are overdue outstanding balances of more than sixty calendar days (días corridos).

No reimbursement of costs shall be applicable among participating institutions with respect to the development of the interface or information exchange mechanism defined for the implementation of the Open Finance System pursuant to Article 21.

Access to Customer data information requested from Information-Providing Institutions through the interfaces defined for the Open Finance System shall not (no podrá) give rise to the charging of fees or additional charges to Customers.

### Original Spanish

> Artículo 25.- Distribución de costos por consultas de información en Sistema
> de Finanzas Abiertas. Las Instituciones Proveedoras de Información no podrán
> efectuar cobros a los Proveedores de Servicios basados en Información por la
> comunicación de la información de datos de Clientes solicitada a través de las
> interfaces definidas para el Sistema de Finanzas Abiertas, con excepción del
> reembolso de los costos incrementales directos en que deban incurrir para atender el
> aumento de solicitudes de información recibidas en la medida que éstas superen el
> umbral de volumen de solicitudes definido por la Comisión.
>
> La Comisión establecerá, mediante norma de carácter general, los parámetros
> para la determinación de los costos reembolsables y los umbrales de volumen de
> solicitudes de información por sobre los cuales corresponderá el reembolso,
> teniendo en consideración el volumen y tipo de datos a ser entregados y los costos
> de operación incrementales de las interfaces.
>
> Los costos incrementales directos que la Institución Proveedora de Información
> solicite reembolsar deberán fijarse en base a condiciones públicas, objetivas,
> equitativas y no discriminatorias entre instituciones participantes. En caso de
> incumplimiento por parte de un Proveedor de Servicios basados en Información en el
> pago de los costos reembolsables antes mencionados, la Institución Proveedora de
> Información deberá continuar atendiendo las consultas de información que no
> superen los umbrales antes referidos, salvo que existan saldos de pago vencidos por
> un plazo superior a sesenta días corridos.
>
> No procederá el reembolso de costos por parte de las instituciones
> participantes respecto del desarrollo de la interfaz o mecanismo de intercambio de
> información definido para la implementación del Sistema de Finanzas Abiertas
> conforme al artículo 21.
>
> El acceso a la información de datos de Clientes solicitada a las Instituciones
> Proveedores de Información a través de las interfaces definidas para el Sistema de
> Finanzas Abiertas no podrá dar lugar a cobro de comisiones o cobros adicionales a
> los Clientes.

### Cross-references
- Art. 21 — interface development (excluded from cost reimbursement under para. 4).
- Art. 26 — non-discriminatory treatment obligation (corollary to non-discriminatory cost conditions in para. 3).

---

## Article 26 — Safeguards to guarantee interoperability and non-discriminatory treatment among participating institutions
**Spanish anchor:** Art. 26°
**Tags:** open-finance, data-providers, data-recipients, technical-standards, supervision

### Plain-English text

Information-Providing Institutions (Instituciones Proveedoras de Información) must comply with the obligations contained in the preceding articles, and shall adopt the necessary measures to guarantee non-discriminatory treatment and interoperability with other institutions participating in the Open Finance System (Sistema de Finanzas Abiertas, or SFA).

Information-Providing Institutions and Account-Providing Institutions (Instituciones Proveedoras de Cuentas) shall not (no podrán) establish restrictions, limitations, or obstacles to the exchange of information or access by authorised Information-Based Service Providers (Proveedores de Servicios basados en Información) or payment initiation service providers (Proveedores de Servicios de Iniciación de Pagos), in terms of priority of access, timeliness and quality of information, requests for customer authorisations, or additional validations beyond the requirements set out in the preceding articles. Nor shall they give any discriminatory treatment to requests for information access or payment initiation instructions received through that interface, as compared to those transactions carried out directly by the Customer through their usual service channels.

### Original Spanish

> Artículo 26.- Resguardos para garantizar interoperabilidad y trato no
> discriminatorio entre instituciones participantes. Las Instituciones Proveedoras de
> Información deberán cumplir con las obligaciones contenidas en los artículos
> anteriores, y adoptarán las medidas necesarias para garantizar un trato no
> discriminatorio y la interoperabilidad con otras instituciones participantes del
> Sistema de Finanzas Abiertas.
>
> Las Instituciones Proveedoras de Información e Instituciones Proveedoras de
> Cuentas no podrán establecer restricciones, limitaciones u obstáculos para el
> intercambio de información o acceso por parte de los Proveedores de Servicios
> basados en Información o Proveedores de Servicios de Iniciación de Pagos
> autorizados, en términos de prioridad en acceso, oportunidad y calidad de
> información, solicitudes de autorizaciones a Clientes o validaciones adicionales a
> las exigencias contempladas en los artículos anteriores. Tampoco podrán dar
> tratamiento discriminatorio alguno a las solicitudes de acceso de información o
> instrucciones de iniciación de pago que reciban a través de dicha interfaz,
> respecto de aquellas transacciones realizadas directamente por el Cliente a través
> de sus canales de servicio habituales.

### Cross-references
- Art. 16 — interoperability and non-discrimination as founding principles of the SFA.
- Art. 21 — interface standards (the technical means through which interoperability operates).
- Art. 25 — non-discriminatory cost conditions (related commercial dimension).
- Art. 27 — CMF supervision and enforcement powers for violations of this article.

---

## Article 27 — Supervisory and oversight powers of the Commission
**Spanish anchor:** Art. 27°
**Tags:** open-finance, supervision, technical-standards, customer-protection

### Plain-English text

It shall be the responsibility of the Commission (CMF) to issue the regulations and instructions necessary for the adequate implementation and operation of the Open Finance System (Sistema de Finanzas Abiertas, or SFA), and to supervise (fiscalizar) compliance with the obligations that correspond to Information-Providing Institutions (Instituciones Proveedoras de Información), Account-Providing Institutions (Instituciones Proveedoras de Cuentas), Information-Based Service Providers (Proveedores de Servicios basados en Información), and payment initiation service providers (Proveedores de Servicios de Iniciación de Pagos). For that purpose, it shall have the powers conferred on it by this law and its organic law (ley orgánica). For those purposes, the Commission (CMF) must observe the principles of risk-based proportionality (proporcionalidad basada en riesgos), technological neutrality (neutralidad tecnológica), and interoperability among participating institutions. This is without prejudice to the duties and obligations that correspond to participating institutions under the general framework, including Law No. 19.496 establishing rules on the protection of consumer rights and Law No. 19.628 on the protection of private life.

For the purposes of issuing the regulations governing the Open Finance System, the public consultation and regulatory impact assessment (evaluación de impacto regulatorio) procedures set out in Article 20, numeral 3, of Decree-Law No. 3.538 of 1980 must be carried out, and a report from the National Economic Prosecutor's Office (Fiscalía Nacional Económica) must be requested pursuant to Article 37 bis of Law No. 19.880.

Likewise, to ensure the adequate implementation of the Open Finance System, the Commission (CMF) may arrange the conduct of pilot testing (pruebas piloto de funcionamiento) with institutions required to participate or that express interest in participating in the Open Finance System, for the purpose of defining the technical and operational aspects of the regulations, particularly in areas relating to information exchange mechanisms and the operation of application programming interfaces (interfaces de programación de aplicaciones, API) and authentication mechanisms among participating institutions.

The Commission (CMF) shall have supervisory powers with respect to institutions participating in the Open Finance System. It may require them to submit the records, documents, data, reports, and in general the information and background it deems necessary to verify compliance with the requirements applicable under this law, as well as to monitor and evaluate the operation of the Open Finance System. It may also compile statistical information as it deems necessary, in the form and under the terms specified by means of a general regulation (norma de carácter general).

To that end, the Commission (CMF) may order the partial or total, temporary or permanent, suspension of one or more participating institutions with respect to the delivery or exchange of information and data carried out, where the requirements established by law and/or the regulations issued to that effect are not complied with and such suspension is necessary to protect the interests of Customers or for the adequate operation of the Open Finance System.

Institutions participating in the Open Finance System that incur in violations of the provisions of this law and the regulations issued pursuant thereto, or fail to comply with instructions or orders legally issued by the Commission (CMF), may be sanctioned in accordance with the rules established in Title III of Decree-Law No. 3.538 of 1980, without prejudice to the special sanctions contained in this or other legislative bodies. These decisions (resoluciones) may be challenged in accordance with the provisions of Title V of that same law.

### Original Spanish

> Artículo 27.- Facultades de supervisión y fiscalización de la Comisión.
> Corresponderá a la Comisión dictar la regulación e instrucciones necesarias para
> la adecuada implementación y funcionamiento del Sistema de Finanzas Abiertas, así
> como fiscalizar el cumplimiento de las obligaciones que competen a las Instituciones
> Proveedoras de Información, Instituciones Proveedoras de Cuentas, Proveedores de
> Servicios basados en Información y Proveedores de Servicios de Iniciación de Pagos.
> Contará para ello con las atribuciones que le confiere esta ley y su ley orgánica.
> Para esos efectos, la Comisión deberá observar los principios de proporcionalidad
> basada en riesgos, neutralidad tecnológica e interoperabilidad entre instituciones
> participantes. Lo anterior, sin perjuicio de los deberes y obligaciones que competan
> a las instituciones participantes conforme al ordenamiento general, incluyendo la ley
> N° 19.496, que establece normas sobre protección de los derechos de los
> consumidores y la ley N° 19.628, sobre protección de la vida privada.
>
> Para efectos de la dictación de la normativa que regule el Sistema de Finanzas
> Abiertas, se deberán llevar a cabo los trámites de consulta pública y evaluación
> de impacto regulatorio contemplados en el artículo 20 número 3 del decreto ley N°
> 3.538, de 1980 y se deberá requerir un informe de la Fiscalía Nacional Económica
> conforme a lo dispuesto en el artículo 37 bis de la ley N° 19.880.
>
> Asimismo, para velar por una adecuada implementación del Sistema de Finanzas
> Abiertas, la Comisión podrá disponer la realización de pruebas piloto de
> funcionamiento con las instituciones que deban participar o que manifiesten interés
> en participar en el Sistema de Finanzas Abiertas, para efectos de definir los
> aspectos técnicos y operativos de la normativa, particularmente en ámbitos
> relativos a los medios de intercambio de información y operatoria de las interfaces
> de programación de aplicaciones y mecanismos de autenticación entre instituciones
> participantes.
>
> La Comisión contará con facultades de fiscalización respecto de las
> instituciones que participen en el Sistema de Finanzas Abiertas. Podrá requerirles
> los registros, documentos, datos, informes y en general, la información y
> antecedentes que estime necesarios para verificar el cumplimiento de las exigencias
> aplicables conforme a esta ley, así como para monitorear y evaluar el funcionamiento
> del Sistema de Finanzas Abiertas. También podrá confeccionar información
> estadística que estime necesaria, en la forma y términos que señale mediante norma
> de carácter general.
>
> A tal efecto, la Comisión podrá ordenar la suspensión parcial o total,
> temporal o definitiva, de una o más instituciones participantes para la entrega o
> del intercambio de información y datos que se realice, cuando se incumplan las
> exigencias establecidas en la ley y/o normativa que se dicte al efecto y resulte
> necesario para el resguardo de los intereses de los Clientes o para el adecuado
> funcionamiento del Sistema de Finanzas Abiertas.
>
> Las instituciones participantes en el Sistema de Finanzas Abiertas que
> incurrieren en infracciones de las disposiciones de esta ley y normativa dictada
> conforme a ello o incumplieren las instrucciones u órdenes legalmente impartidas por
> la Comisión, podrán ser sancionadas conforme a las reglas establecidas en el
> título III del decreto ley N° 3.538, de 1980, sin perjuicio de las sanciones
> especiales contenidas en este u otros cuerpos legales. Estas resoluciones podrán ser
> impugnadas de conformidad con lo establecido en el título V de la misma ley.

### Cross-references
- Art. 1 — general principles of the law, including proportionality and technological neutrality.
- Art. 16 — founding principles of the SFA that the CMF must observe.
- Art. 19 — CMF power to suspend authorisation of Information-Based Service Providers.
- Decree-Law No. 3.538 of 1980, Title III — administrative sanctions procedure.
- Decree-Law No. 3.538 of 1980, Title V — challenge procedure for CMF decisions.
- Law No. 19.880, Art. 37 bis — FNE report requirement for regulations (para. 2).
- Law No. 19.496 — consumer protection (para. 1 cross-reference).
- Law No. 19.628 — personal data protection (para. 1 cross-reference).

---

<!-- source: corpus/21521-fintech/titulo-04-otras-disposiciones.md -->
## FILE: corpus/21521-fintech/titulo-04-otras-disposiciones.md

# Ley 21.521 — Título IV: Other Provisions (Otras disposiciones)

**Law:** Ley 21.521 (in force 2023-02-03)
_law:_ 21.521

---

## Article 28 — Offering financial products and services in line with customer profile
**Spanish anchor:** Art. 28°
**Tags:** other-provisions, customer-protection, supervision, miscellaneous

### Plain-English text

Financial service providers (prestadores de servicios financieros) regulated under Title II of this law, along with banks, insurance companies (compañías de seguros), securities intermediaries (intermediarios de valores), commodity-exchange brokers (corredores de bolsas de productos), fund and individual portfolio managers (administradoras de fondos y carteras individuales) regulated by Law No. 20.712, savings-and-credit cooperatives (cooperativas de ahorro y crédito) supervised by the Commission (CMF), and family allowance compensation funds (cajas de compensación de asignación familiar) regulated by Law No. 18.833, must adopt policies, procedures, and controls designed to prevent the offering of products that are not aligned with the needs, expectations, and risk tolerance that customers have previously communicated to them regarding the products they wish to acquire.

For those purposes, the entities may require customers to provide information about their knowledge and experience as an investor or financial customer, their financial situation, and their investment, savings, financing, or insurance objectives, in view of the type of financial service or product they wish to contract, and must inform customers of the characteristics, conditions, and risks involved.

In cases where a customer decides to contract a service that, in the service provider's opinion, is not aligned with the needs, expectations, or risks communicated by the customer, the entity must adopt such safeguards as are necessary to demonstrate to the Commission (CMF) that the customer was warned of that fact prior to contracting, when the Commission (CMF) so requests in the course of supervising (fiscalización) compliance with this article.

Information, advertising, or publicity of any kind delivered in connection with the offer of financial products or services shall not (no podrá) contain statements, allusions, or representations that may mislead, or that are ambiguous or may cause confusion to the public, regarding the nature, prices, profitability, or any other characteristic of such products or services, or those relating to the entities that provide them.

For the purposes of supervising (fiscalización) compliance with this article, the Commission (CMF) shall have all powers conferred on it by its organic law (ley orgánica).

> **TN:** "disposición al riesgo" is rendered as "risk tolerance" rather than a more literal "willingness to take risk," as "risk tolerance" is the standard regulatory and financial-advice term of art in English-language suitability frameworks (cf. MiFID II, SEC suitability rules). This rendering preserves the normative meaning.

### Original Spanish

> Artículo 28.- Oferta de productos y servicios financieros acorde al perfil. Los
> prestadores de servicios financieros regulados por el título II, y los bancos, las
> compañías de seguros, los intermediarios de valores, los corredores de bolsas de
> productos, las administradoras de fondos y carteras individuales reguladas por la ley
> N° 20.712, y las cooperativas de ahorro y crédito fiscalizados por la Comisión,
> cajas de compensación de asignación familiar reguladas por la ley N°18.833,
> deberán adoptar políticas, procedimientos y controles tendientes a evitar que se
> ofrezcan productos que no sean acorde a las necesidades, expectativas y disposición
> al riesgo que los clientes les hayan previamente comunicado respecto a los productos
> que desean adquirir.
>
> Para esos efectos, las entidades podrán requerir a los clientes información
> sobre sus conocimientos y experiencia como inversionista o cliente financiero, su
> situación financiera y objetivos de inversión, ahorro, financiamiento o
> aseguramiento, en atención al tipo de servicio o producto financiero que deseen
> contratar, y deberán informarles acerca de las características y condiciones de
> éstos y los riesgos involucrados.
>
> En aquellos casos en que un cliente decida contratar un servicio que en opinión
> del prestador de servicios no esté acorde a las necesidades, expectativas o riesgos
> comunicados por el cliente, la entidad deberá adoptar los resguardos que sean
> necesarios a objeto de acreditar ante la Comisión que ese hecho fue advertido al
> cliente previo a la contratación, cuando ésta así lo solicite en la fiscalización
> del cumplimiento de lo establecido en el presente artículo.
>
> La información, propaganda o publicidad que por cualquier medio se entregue
> respecto de la oferta de productos o servicios financieros no podrá contener
> declaraciones, alusiones o representaciones que puedan inducir a error, o que sean
> equívocos o puedan causar confusión al público acerca de la naturaleza, precios,
> rentabilidad o cualquier otra característica de tales productos o servicios o
> aquellas relativas a quienes los presten.
>
> Para efectos de la fiscalización de lo establecido en el presente artículo, la
> Comisión dispondrá de todas las facultades que le confiere su ley orgánica.

### Cross-references
- Title II (Arts. 2–15) — financial service providers regulated under this law (scope of Art. 28 obligation).
- Art. 27 — CMF supervisory powers (Title III); Art. 28 grants equivalent powers for its own scope.
- Law No. 20.712 — fund and portfolio manager regulation (listed entity type).
- Law No. 18.833 — family allowance compensation funds (listed entity type).
- Law No. 19.496 — consumer protection law (customer information rights, complementary framework).

---

## Article 29 — Conditions for bank account access by supervised financial institutions
**Spanish anchor:** Art. 29°
**Tags:** other-provisions, scope-extension, customer-protection, supervision

### Plain-English text

Banks offering current-account (cuenta corriente) services must establish the public, objective, and non-discriminatory conditions under which they will offer and grant access to such services to financial service providers (prestadores de servicios financieros) regulated under Title II of this law, to payment-card issuers and operators (emisores y operadores de tarjetas de pago), and to other financial institutions subject to supervision (fiscalización) by the Commission (CMF) as the Commission may define by means of a general regulation (norma de carácter general). Under the conditions set out above, a bank may deny an account-opening request, or may proceed to suspend or close the current-account contract; in either case it must communicate that decision as promptly as possible and with justified cause (causa justificada) to the relevant financial institution. It must likewise inform the institution of the reasons for its decision, having regard to the specific risks of the applicant institution or its failure to meet the general conditions referred to above.

> **TN:** "causa justificada" is rendered as "justified cause" rather than "just cause" to avoid the labour-law connotation of the latter; in this context the phrase requires that the bank state objective, risk-based grounds for denial, suspension, or termination of the account relationship.

### Original Spanish

> Artículo 29.- Condiciones de acceso a cuentas bancarias por instituciones
> financieras fiscalizadas. Los bancos que ofrezcan servicios de cuenta corriente
> deberán establecer las condiciones públicas, objetivas y no discriminatorias bajo
> las cuales ofrecerán y darán acceso a dichos servicios a los prestadores de
> servicios financieros regulados por el título II, los emisores y operadores de
> tarjetas de pago y otras instituciones financieras sujetas a la fiscalización de la
> Comisión que ésta defina por norma de carácter general. Bajo las condiciones antes
> señaladas, el banco podrá denegar la solicitud de apertura de cuenta o bien se
> podrá proceder a la suspensión o cierre del contrato de cuenta corriente, en cuyo
> caso deberá comunicar dicha decisión a la mayor brevedad, y por causa justificada a
> la institución financiera respectiva. Asimismo, deberá informar las razones que la
> motivan en consideración a los riesgos específicos de la institución solicitante o
> su falta de adecuación a las condiciones generales antes referidas.

### Cross-references
- Title II (Arts. 2–15) — financial service providers whose bank account access is protected by this article.
- Art. 18(h) — entities registered in the Registry of Financial-Service Providers (overlap with Art. 29 obligees).
- Art. 26 — non-discriminatory treatment in the Open Finance System (analogous principle applied here to banking access).
- Art. 27 — CMF power to define by general regulation which additional institutions fall within Art. 29 scope.
- General Banking Law (Ley General de Bancos) — framework governing current-account contracts (applicable background law).

---

<!-- source: corpus/21521-fintech/titulo-05-modificaciones.md -->
## FILE: corpus/21521-fintech/titulo-05-modificaciones.md

# Ley 21.521 — Título V: Modifications to Other Statutes — OUT OF SCOPE

**Law:** Ley 21.521 (in force 2023-02-03)
_law:_ 21.521
**Status:** Not translated. Reference only.

## Why this Título is out of scope

Título V (`Modificaciones a otros cuerpos normativos`) consists entirely of
amendment instructions modifying other Chilean laws. It does NOT contain
operative fintech or data-protection provisions of Ley 21.521 itself; instead
it amends:

- **Ley 18.045** — Mercado de Valores (capital markets / securities)
- **Ley 18.046** — Sociedades Anónimas (corporations)
- **Ley 18.840** — Ley Orgánica Constitucional del Banco Central de Chile (Central Bank)
- **Ley 19.220** — Bolsas de Productos (commodity exchanges)
- **Ley 20.712** — Administración de fondos de terceros (third-party fund management)
- **Ley 20.950** — Medios de pago con provisión de fondos por entidades no bancarias (non-bank payment-instrument issuers)
- **Ley 21.000** — Comisión para el Mercado Financiero (CMF Charter)

These are capital-markets, banking, and CMF-supervision statutes outside the
plugin's scope of "fintech provisions of 21.521 + data-protection compliance".

## What to do if you need Título V content

1. Read the source PDF directly:
   `sources/Ley-21521_04-ENE-2023-1.pdf`, pages roughly covering Arts. 30 onward.
2. For the underlying amended law, consult the official BCN text on `leychile.cl`.
3. If this plugin's scope ever expands to cover capital-markets compliance,
   open an issue or add a new corpus directory (e.g., `corpus/18045-capital-markets/`)
   rather than mixing amendment instructions into this Título III/IV file set.

## Tooling exclusion

This Título is excluded from extraction-parity and round-trip checks via the
`--exclude-titulo V` flag on the parity checker. See
`tools/check_extraction_parity.py`.

## Articles in source order (for reference)

The Spanish PDF contains Articles 30-46 in Título V, each amending one of the
laws listed above. The Articles' `Artículo N.-` opening verbs are typically
`Modifícase la ley N° XYZ en los siguientes términos:`. The extractor in
`tools/extract_articles.py` also picks up nested `Artículo N.-` references
inside quoted amendment text — these are NOT real articles of Ley 21.521.

---
