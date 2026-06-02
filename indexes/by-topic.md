# By Topic

Topical lookup of Chilean compliance topics relevant to fintech and data
protection work. Every bullet ends with one or more article citations into
the corpus. AIs querying this index should `Read` the cited articles in
full before reasoning — bullets summarize, they do not substitute.

Topics VI–VIII sourced from `titulo-06-agencia.md` and `titulo-07-sanciones.md`
contain English summaries pending literal H4 translation. Those citations
are flagged inline.

---

## Topic: Storing National IDs (cédula / RUT)

- *Definition of personal data including cédula* — The cédula de identidad number is explicitly listed as an identifier that makes a person identifiable; storing it constitutes processing of personal data subject to this law. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-2` — Ley 19.628 Art. 2(f) (definition of personal data; cédula de identidad named as identifier example).

- *Lawful basis required for storing IDs* — Processing (which includes storage) of any personal data, including national IDs, requires a lawful basis. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-12` — Ley 19.628 Art. 12 (consent as lawful basis for processing).
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-13` — Ley 19.628 Art. 13 (other lawful bases: contract, legal obligation, legitimate interest).

- *Open Finance: KYC/identification data* — Customer identification and registration data collected during onboarding is one of the data categories in the Open Finance System; sharing requires customer consent. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-17` — Ley 21.521 Art. 17(2) (identification and registration data of customers in SFA scope; consent required for sharing).

---

## Topic: Contact Information (email, phone, address)

- *Contact details as personal data* — Contact information (email, phone, address) links to an identifiable natural person and constitutes personal data under Art. 2(f). **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-2` — Ley 19.628 Art. 2(f) (definition of personal data; "identifiers" includes contact data that allows identification).

- *Controller must publish contact channel for rights requests* — The data controller must maintain a permanently operative email address or equivalent for data subjects to exercise their rights. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter` — Ley 19.628 Art. 14 ter(c) (controller must publish postal address, email, or contact form on its website).

- *Lawful basis for processing contact information* — Contact data collected to perform a contract (e.g., account onboarding) is lawfully processed without separate consent. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-13` — Ley 19.628 Art. 13(c) (processing necessary for conclusion or performance of a contract is lawful without consent).

- *Foreign-controller contact obligation* — Controllers without Chilean domicile that process data of Chilean residents must maintain an operative contact address. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14` — Ley 19.628 Art. 14 (paragraph 2) (foreign controller must designate and maintain an email address or suitable contact method for data subjects and the Agency).

---

## Topic: Bank Statements (display / aggregation)

- *Financial transaction history in the Open Finance System* — Bank account transaction history and conditions contracted with information-providing institutions are a defined SFA data category; accessing them requires prior customer consent. Five-year lookback limit applies. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-17` — Ley 21.521 Art. 17(3) (account information, credit-card data, money-lending, savings, investment instruments; consent required; five-year limit).

- *Information-providing institutions subject to SFA* — Banks and card issuers must participate as information-providing institutions and deliver financial data to registered information-based service providers on customer consent. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-18` — Ley 21.521 Art. 18 (banks and authorized issuers are mandatory SFA participants; registry of Financial-Service Providers also listed).

- *Financial-obligation data processing rule* — Processing of economic/financial/banking/commercial obligation data is a specific lawful basis under Ley 19.628, governed by Título III rules. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-13` — Ley 19.628 Art. 13(a) (financial-obligation data may be processed without consent subject to Título III).
  - `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-17` — Ley 19.628 Art. 17 (types of financial obligation data that may be communicated; protest, default, credit performance).

- *Breach notification for financial data* — Security breaches affecting financial/banking/commercial data require mandatory notification to data subjects (not just to the Agency). **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-sexies` — Ley 19.628 Art. 14 sexies (breach notification duty; financial data triggers mandatory subject-level notification).

---

## Topic: Investment Tracker (read-only aggregation)

- *Information-based service providers (read-only access)* — Aggregating investment and savings data from information-providing institutions requires registration as an Information-Based Service Provider in the CMF registry. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-19` — Ley 21.521 Art. 19 (registration requirement; consent prerequisite; prohibition on providers with serious data-protection infringements).

- *Savings and investment instruments in SFA scope* — Savings and investment instruments (e.g., savings accounts, investment funds) are expressly included in the SFA data perimeter. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-17` — Ley 21.521 Art. 17(3)(e) (savings or investment instruments included in SFA commercial-conditions data category).

- *Consent and purpose limitation for aggregation* — Information-based service providers may only access data for the purpose consented to; they may not store or use data beyond the scope of the customer authorisation. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-23` — Ley 21.521 Art. 23 (consent must be free, informed, explicit, purpose-specific, and time-limited; revocable at any time).
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-24` — Ley 21.521 Art. 24 (information-based service providers must not use, store, or access data beyond the authorisation; must respond to customers for data breaches).

- *Security standards for aggregation platforms* — Platforms accessing SFA data must comply with CMF-set information-security, cybersecurity, and risk-management standards. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-22` — Ley 21.521 Art. 22 (minimum security, cybersecurity, and risk-management standards; sensitive data classification under Ley 19.628 must be considered).

---

## Topic: Investment Application (execution / advisory)

- *Registration obligation for investment advisory and intermediation* — Entities providing investment advisory or intermediation of financial instruments on a professional basis must be registered in the CMF's Registry of Financial-Service Providers. **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-5` — Ley 21.521 Art. 5 (mandatory registration; investment advisory and intermediation listed; international companies must have Chilean domicile).

- *Authorisation requirements for investment advisory* — Prior CMF authorisation is required; applicants must demonstrate information systems, suitability/knowledge (Art. 9), and governance/risk management (Art. 12). **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-7` — Ley 21.521 Art. 7(5) (investment advisory authorisation requirements: information systems, suitability, governance).

- *Suitability standard for advisory systems* — Both persons and systems used for investment advisory must comply with objectivity, coherence, and consistency standards. CMF sets knowledge-certification requirements. **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-9` — Ley 21.521 Art. 9 (suitability standard for persons and systems providing investment and credit advisory).

- *Customer suitability / profile-aligned offering* — Providers must adopt policies to avoid offering products inconsistent with the needs, expectations, and risk tolerance communicated by the customer. **See:**
  - `corpus/21521-fintech/titulo-04-otras-disposiciones.md#article-28` — Ley 21.521 Art. 28 (suitability obligation; customer profile assessment; CMF supervision).

- *Guarantees for intermediation and custody services* — Once business-volume thresholds are reached, intermediation and order routing services must constitute bank guarantees or insurance policies. **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-10` — Ley 21.521 Art. 10 (guarantee requirements for intermediation, order routing, and custody services).

- *Governance and risk management for investment advisory PSFs (in practice)* — Board must approve and periodically review risk-management, internal-control, and compliance policies. NCG 502 §IV.A covers the board responsibility matrix, mandatory policies, dedicated risk and compliance functions, and internal audit requirements.
  NCG 502 §IV.A — see `corpus/ncg/502-psf-obligations/seccion-04a-gobierno-asesoria-inversion.md`.

- *Disclosure obligations for investment advisory (in practice)* — NCG 502 §III sets out per-service disclosure rules: pre-contractual information sheets, fee schedules, conflict-of-interest disclosures, and ongoing reporting to customers.
  NCG 502 §III — see `corpus/ncg/502-psf-obligations/seccion-03-divulgacion.md`.

---

## Topic: AI-Based Recommendations

- *Automated-decision rights (opt-out and safeguards)* — Data subjects have the right to object to decisions based solely on automated processing (including profiling) that produce legal or significant effects. The controller must ensure the right to an explanation, human intervention, and review of the decision. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8-bis` — Ley 19.628 Art. 8 bis (automated individual decisions and profiling: right to object; exceptions for contract/consent/law; mandatory safeguards in all cases).

- *Transparency duty for automated recommendations* — The controller must publicly disclose the existence of automated decisions (including profiling) and provide meaningful information about the logic applied and foreseeable consequences. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter` — Ley 19.628 Art. 14 ter(l) (public disclosure of automated decisions and profiling logic on controller's website).

- *Right of access to automated-decision logic* — Data subjects may request confirmation of automated processing and receive meaningful information about the logic applied. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-5` — Ley 19.628 Art. 5(f) (right of access includes meaningful information about logic applied in automated processing under Art. 8 bis).

- *DPIA required for systematic automated profiling at scale* — Where automated evaluation of personal aspects produces significant legal effects, a Data Protection Impact Assessment is mandatory before processing begins. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-ter` — Ley 19.628 Art. 15 ter(a) (DPIA always required for systematic exhaustive profiling that produces significant legal effects).

- *Suitability standard for advisory systems (Fintech angle)* — AI/algorithmic systems used for investment or credit advisory must meet CMF objectivity, coherence, and consistency standards. **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-9` — Ley 21.521 Art. 9 (systems used for investment advisory and credit advisory must meet suitability standards; CMF sets certification rules).

---

## Topic: AI-Based Document Parsing (PDFs, statements)

- *Processing personal data during document parsing* — Extracting data from bank statements or identity documents constitutes processing of personal data and requires a lawful basis. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-2` — Ley 19.628 Art. 2(o) (definition of processing: collection, processing, storage, communication in any form by automated or non-automated means).
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-12` — Ley 19.628 Art. 12 (consent as the primary lawful basis for processing).

- *Processor / outsourcing contract required* — Where document parsing is performed by a third-party AI service, a written data-processing agreement is mandatory specifying subject, duration, purpose, data types, and obligations. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis` — Ley 19.628 Art. 15 bis (third-party processor must follow controller's instructions; data-processing contract is mandatory; sub-processing requires specific written authorisation).

- *Purpose limitation for parsed data* — Data extracted by parsing may only be used for the purpose for which it was collected; repurposing requires re-consent or a compatible purpose. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-3` — Ley 19.628 Art. 3(b) (purpose principle: personal data must be collected for specific, explicit, lawful purposes and processing limited to those purposes).

- *Retention after parsing task is complete* — Where data was collected only for pre-contractual processing, the controller must erase or anonymize it once the purpose is fulfilled. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14` — Ley 19.628 Art. 14(d) (controller must erase or anonymize data obtained for pre-contractual measures once that use ends).

- *DPIA for large-scale automated document processing* — Large-scale or mass automated processing triggers a mandatory DPIA before operations begin. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-ter` — Ley 19.628 Art. 15 ter(b) (DPIA always required for large-scale or mass data processing).

---

## Topic: Cross-Border Data Transfer (US/EU cloud)

- *General authorisation rule* — International data transfers are lawful if the destination country has an adequacy determination, or if contractual clauses / binding corporate rules / certification mechanisms establish adequate guarantees. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-27` — Ley 19.628 Art. 27 (general authorisation: adequacy, contractual clauses, binding corporate rules, certification; specific non-habitual transfers with consent or contract).

- *Adequacy determination by the Agency* — The APDP determines which countries have adequate protection levels, considering principles, data-subject rights, information-security obligations, and liability rules. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-28` — Ley 19.628 Art. 28 (adequacy criteria; Agency publishes list of adequate countries and model clauses; binding corporate rules for intra-group transfers; ad-hoc Agency authorisation available).

- *Agency supervision of international transfers* — The Agency supervises international transfers and may issue recommendations, adopt precautionary measures, or suspend data flows in qualified cases. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-29` — Ley 19.628 Art. 29 (Agency supervision, recommendations, precautionary measures, and temporary suspension of data flows).

- *Transparency disclosure for cross-border transfers* — Controllers must publicly disclose on their website whether they transfer data to third countries and whether those countries offer adequate protection; where protection is inadequate, available guarantees must be stated. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter` — Ley 19.628 Art. 14 ter(h) (website disclosure of international transfers and adequacy/guarantee status).

- *Burden of proof on the transferring controller* — The controller that effected the international transfer must demonstrate to the Agency that the transfer was carried out in conformity with the law. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-28` — Ley 19.628 Art. 28 (paragraph 6: burden of proof on the controller; Agency may authorise ad-hoc transfers by reasoned decision).

- *Territorial scope: processing targeting Chilean residents* — Even controllers not established in Chile are subject to this law if their data processing is directed at offering goods/services to Chilean data subjects, or at monitoring their behaviour. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-1-bis` — Ley 19.628 Art. 1 bis(c) (targeting/monitoring of Chilean residents triggers the law regardless of controller's domicile).

---

## Topic: Consent (general)

- *Consent definition* — Consent must be free, specific, unequivocal, and informed; it must be given through a statement or clear affirmative action; revocable at any time; burden of proof on the controller. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-2` — Ley 19.628 Art. 2(p) (definition of consent).
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-12` — Ley 19.628 Art. 12 (general rule for consent: requirements, presumption of non-free consent tied to contract, burden of proof, revocation).

- *Consent for automated decisions* — Using consent as the legal basis for automated decisions requires prior and express consent in the form prescribed by Art. 12. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8-bis` — Ley 19.628 Art. 8 bis(b) (consent exception to automated-decision prohibition requires prior and express consent per Art. 12).

- *Sensitive data: express consent required* — Processing sensitive personal data requires express consent (written, verbal, or equivalent technology). Exceptions are narrow. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-16` — Ley 19.628 Art. 16 (express consent required for sensitive data; exceptions listed in Art. 16(a)–(f)).

- *Consent in the Open Finance System* — SFA financial-data sharing requires prior explicit customer consent specifying data type, purpose, and maximum validity period; revocable at any time. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-23` — Ley 21.521 Art. 23 (SFA consent: free, informed, explicit, specific as to type, purpose, validity; revocable; CMF sets implementation rules).

- *Right of erasure upon consent withdrawal* — When the data subject withdraws consent and no other legal basis exists, erasure must be granted on request. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-7` — Ley 19.628 Art. 7(b) (withdrawal of consent without other legal basis is a ground for erasure).

---

## Topic: Lawful Basis for Processing

- *Six lawful bases* — Processing is lawful under: (a) consent; (b) financial-obligation data under Título III; (c) legal obligation; (d) contract / pre-contractual measures; (e) legitimate interests; (f) legal proceedings. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-12` — Ley 19.628 Art. 12 (consent as general lawful basis).
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-13` — Ley 19.628 Art. 13 (non-consent lawful bases: financial-obligation data, legal obligation, contract, legitimate interests, legal proceedings).

- *Lawfulness principle* — The controller must be able to demonstrate the lawfulness of processing; this principle is foundational. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-3` — Ley 19.628 Art. 3(a) (lawfulness and fairness principle; controller must be able to demonstrate lawfulness).

- *Financial-obligation data special basis* — Data relating to economic, financial, banking, or commercial obligations may be processed without consent, subject to the rules of Título III. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-17` — Ley 19.628 Art. 17 (types of financial-obligation data that may be communicated under the special basis).

---

## Topic: Purpose Limitation

- *Purpose principle* — Personal data must be collected for specific, explicit, and lawful purposes. Processing must be limited to those purposes; repurposing requires compatible purpose, new consent, contractual justification, or statutory basis. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-3` — Ley 19.628 Art. 3(b) (purpose principle; conditions for compatible repurposing).

- *Processor bound to purpose* — A third-party processor is prohibited from processing data for any purpose other than the one agreed with the controller. If it exceeds its mandate it becomes a controller for all legal purposes. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis` — Ley 19.628 Art. 15 bis (processor must follow controller's instructions; purpose-deviation makes processor a controller and imposes joint-and-several liability).

- *Purpose limitation in the Open Finance System* — Information-based service providers and payment initiation service providers may not use, store, or access customer data for purposes not covered by the customer's authorisation. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-24` — Ley 21.521 Art. 24 (purpose limitation enforced on SFA participants; access must stop when consent expires or is revoked).

- *Processing financial obligation data for a different purpose is a serious infringement* — currently summarized; await H4 for literal translation: **See:**
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-34-ter` — Ley 19.628 Art. 34 ter(a) (serious infringement: processing for a purpose different from that for which data was collected).

---

## Topic: Retention Policy

- *Proportionality principle sets the default rule* — Personal data may be retained only for the period necessary to fulfil the purposes of processing; thereafter they must be erased or anonymized. A longer period requires statutory authorisation or consent. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-3` — Ley 19.628 Art. 3(c) (proportionality principle: retention period limited to necessity; erasure or anonymization required after).

- *Controller must disclose retention period publicly* — The period during which personal data will be retained must be stated on the controller's website. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter` — Ley 19.628 Art. 14 ter(i) (public disclosure obligation: retention period).

- *Right of access includes retention period* — Data subjects may request disclosure of the period during which their data will be processed. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-5` — Ley 19.628 Art. 5(d) (right of access: the period during which data will be processed must be disclosed).

- *Financial data: five-year hard limit* — Financial obligation data relating to an identified or identifiable person may not be communicated once five years have elapsed since the obligation became enforceable; data must stop after payment or extinction. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-18` — Ley 19.628 Art. 18 (five-year limit; post-payment prohibition; exception for court proceedings).

- *Prescribed financial obligations: mandatory erasure* — Controllers must erase data relating to prescribed obligations without need for a request, court order, or authority instruction. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-17` — Ley 19.628 Art. 17 (paragraph 8: mandatory erasure of prescribed-obligation data without request).

- *Privacy by default: data minimization in retention* — Controllers must apply measures to ensure only strictly necessary data is processed, taking into account retention period and accessibility. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quáter` — Ley 19.628 Art. 14 quáter (privacy-by-default obligation; retention period is an explicit factor to consider).

- *SFA transaction history: five-year lookback limit* — Transaction history shared through the Open Finance System may not extend back more than five years. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-17` — Ley 21.521 Art. 17(3) (five-year lookback limit on transaction history in SFA).

---

## Topic: Data Subject Rights (access, rectification, deletion, blocking, portability)

- *Catalogue of rights* — Every data subject has the rights of access, rectification, erasure, opposition, portability, and blocking. These rights are personal, non-transferable, and irrevocable. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-4` — Ley 19.628 Art. 4 (catalogue of rights; non-waiver; heirs).

- *Right of access* — Data subjects may request confirmation of processing, access to their data, and information on origin, purposes, recipients, retention period, legitimate interests, and automated-decision logic. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-5` — Ley 19.628 Art. 5 (right of access: content of the right; controller always obliged to respond).

- *Right of rectification* — Data subjects may request correction of inaccurate, outdated, or incomplete data; rectification must be communicated downstream. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-6` — Ley 19.628 Art. 6 (right of rectification: grounds, downstream notification, prohibition on reprocessing uncorrected data).

- *Right of erasure* — Data subjects may request deletion when data are no longer necessary, consent is withdrawn (without other basis), data were unlawfully obtained, data are expired, or a court/authority order requires it. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-7` — Ley 19.628 Art. 7 (right of erasure: six grounds; six exceptions where erasure does not apply).

- *Right of opposition* — Data subjects may object to processing based on legitimate interests, direct marketing/profiling, or publicly accessible sources. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8` — Ley 19.628 Art. 8 (right of opposition: three grounds; exception for public-interest research/statistics).

- *Right of blocking* — Data subjects may request temporary suspension of processing pending resolution of a rectification, erasure, or opposition request; also available as an alternative to erasure. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8-ter` — Ley 19.628 Art. 8 ter (right of blocking: during pending rights request or as alternative to erasure; storage unaffected).

- *Right of portability* — Data subjects may request a copy in a structured, generic, commonly-used electronic format; direct controller-to-controller transmission required where technically feasible; requires automated processing based on consent. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-9` — Ley 19.628 Art. 9 (right of portability: format, conditions, direct transmission, non-erasure default).

- *Exercise procedure* — Rights requests must be submitted in writing (email, form, equivalent electronic medium); controller must respond within 30 calendar days (extendable once). Rights of rectification, erasure, and opposition are free of charge; access is free at least quarterly. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-10` — Ley 19.628 Art. 10 (form and means; free exercise; cost rules for access/portability; controller must implement technological tools).
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-11` — Ley 19.628 Art. 11 (procedure before the controller: content of request, 30-day response deadline, temporary blocking request, downstream notification duty).

---

## Topic: Breach Notification

- *Duty to report to the Agency* — The controller must report to the Agency, without undue delay, security breaches that cause accidental or unlawful destruction, leakage, loss, alteration, or unauthorised access to personal data, where there is reasonable risk to data subjects' rights. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-sexies` — Ley 19.628 Art. 14 sexies (Agency notification duty; record-keeping; enhanced obligations for sensitive data, children's data, and financial data).

- *Subject-level notification for sensitive, children's, and financial data* — Where breaches affect sensitive personal data, data of children under 14, or financial/banking/commercial data, the controller must also notify the affected data subjects directly (or via mass-media if individual notification is not possible). **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-sexies` — Ley 19.628 Art. 14 sexies (paragraph 3: subject notification requirements; language, content of notification, individual notification preference with mass-media fallback).

- *Security measures as prerequisite* — Controllers must adopt and maintain security measures (pseudonymization, encryption, resilience, restoration, regular testing) before a breach occurs; breach liability is assessed against those measures. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quinquies` — Ley 19.628 Art. 14 quinquies (security measures: confidentiality, integrity, availability, resilience; burden of proof on controller in controversy).

- *SFA security incident reporting* — Participants in the Open Finance System must report security incidents to the CMF without delay, and adopt risk-mitigation measures. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-22` — Ley 21.521 Art. 22 (paragraph 2) (SFA security breach reporting to CMF; risk-mitigation measures required).

- *Omitting breach notification is a serious infringement* — currently summarized; await H4 for literal translation: **See:**
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-34-ter` — Ley 19.628 Art. 34 ter(k) (serious infringement: omitting communications or records required for security breaches under Art. 14 quinquies).

- *Operational incident reporting to CMF for investment advisers (in practice)* — Investment advisory PSFs must report operational incidents to CMF using the standard Anexo N°2 form; escalation thresholds and deadlines are set out in §IV.A.5.
  NCG 502 §IV.A.5 / Anexo N°2 — see `corpus/ncg/502-psf-obligations/seccion-04a-gobierno-asesoria-inversion.md` and `corpus/ncg/502-psf-obligations/anexo-02-reporte-incidentes.md`.

- *Operational incident reporting for platforms/ATS (in practice)* — Crowdfunding platform and ATS PSFs must notify CMF of operational incidents within prescribed deadlines; the reporting template is Anexo N°2.
  NCG 502 §IV.C.7 / Anexo N°2 — see `corpus/ncg/502-psf-obligations/seccion-04c-gobierno-plataformas-sat.md` and `corpus/ncg/502-psf-obligations/anexo-02-reporte-incidentes.md`.

- *Operational incident reporting for intermediation/custody (in practice)* — Intermediation and custody PSFs follow the same CMF incident-report framework; §IV.E.8 specifies the applicable deadlines and severity thresholds.
  NCG 502 §IV.E.8 / Anexo N°2 — see `corpus/ncg/502-psf-obligations/seccion-04e-gobierno-intermediacion-custodia.md` and `corpus/ncg/502-psf-obligations/anexo-02-reporte-incidentes.md`.

- *Operational loss reporting (in practice)* — All PSFs must maintain an operational-loss register and report aggregate losses to CMF periodically using the Anexo N°3 form.
  NCG 502 Anexo N°3 — see `corpus/ncg/502-psf-obligations/anexo-03-reporte-perdidas.md`.

---

## Topic: Automated Decision-Making

- *Right to object to automated decisions* — Data subjects have the right to oppose and not be subject to decisions based solely on automated processing (including profiling) that produce legal effects or significantly affect them. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8-bis` — Ley 19.628 Art. 8 bis (automated decisions and profiling: right to object; exceptions; mandatory safeguards including explanation, human intervention, review).

- *Exceptions to the opt-out* — Automated decisions are permitted where necessary for a contract, where the data subject has given prior and express consent, or where the law expressly authorises them with safeguards. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8-bis` — Ley 19.628 Art. 8 bis(a)–(c) (three exceptions; safeguards mandatory even in exception cases).

- *Definition of profiling* — Profiling is defined as any form of automated processing used to evaluate, analyse, or predict aspects of a natural person's professional performance, economic situation, health, preferences, interests, reliability, behaviour, location, or movements. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-2` — Ley 19.628 Art. 2(w) (definition of profiling / elaboración de perfiles).

- *DPIA mandatory for systematic profiling* — A Data Protection Impact Assessment is always required before processing operations involving systematic exhaustive evaluation of personal aspects based on automated processing or decisions (including profiling) that produce significant legal effects. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-ter` — Ley 19.628 Art. 15 ter(a) (DPIA always required for systematic profiling producing significant legal effects).

- *Opposition to marketing profiling* — Data subjects may always oppose processing carried out exclusively for direct marketing purposes, including profiling. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8` — Ley 19.628 Art. 8(b) (opposition right for direct-marketing profiling; no override possible).

---

## Topic: Sensitive Personal Data

- *Definition of sensitive personal data* — Sensitive data covers racial/ethnic origin, political/trade-union/guild affiliation, socio-economic situation, ideological/philosophical convictions, religious beliefs, health data, biological profile, biometric data, and sexual life/orientation/gender identity. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-2` — Ley 19.628 Art. 2(g) (definition of sensitive personal data).

- *Express consent required as general rule* — Sensitive personal data may only be processed where the data subject gives express consent (written, verbal, or equivalent technology); narrow exceptions apply. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-16` — Ley 19.628 Art. 16 (general rule: express consent; six exceptions including vital interests, legal claims, public-law non-profits, and explicit statutory authorisation).

- *Health and biological-profile data: heightened rules* — Health data and biological-profile data (including genetic data) may only be processed for purposes specified in special health laws; additional exceptions apply; collection in employment, insurance, or identification contexts is prohibited unless expressly authorised by law. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-16-bis` — Ley 19.628 Art. 16 bis (health and biological-profile data: restricted purposes; employment/insurance/identification collection prohibition).

- *Biometric data: additional information duties* — Biometric data may only be processed where the controller provides specific information: identification of the biometric system, specific purpose, processing period, and how rights may be exercised. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-16-ter` — Ley 19.628 Art. 16 ter (biometric personal data: definition; information-duty prerequisites; no-consent exceptions limited to Art. 16 bis para. 2 cases).

- *Breach notification: sensitive data triggers subject-level notification* — Security breaches affecting sensitive personal data require mandatory direct notification to affected data subjects. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-sexies` — Ley 19.628 Art. 14 sexies (paragraph 3: breach affecting sensitive data triggers subject-level notification obligation).

- *Processing sensitive data without basis is a very serious infringement* — currently summarized; await H4 for literal translation: **See:**
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-34-quáter` — Ley 19.628 Art. 34 quáter(e) (very serious infringement: knowingly processing or ceding sensitive data in violation of the law).

---

## Topic: Sanctions and Penalties

- *General liability regime* — Data controllers (natural or legal persons, public or private) are liable for infringements of this law; liability is administrative without prejudice to civil and other legal liability. Currently summarized; await H4 for literal translation: **See:**
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-33` — Ley 19.628 Art. 33 (general liability regime).

- *Infringement tiers* — Infringements are classified as minor (leves), serious (graves), and very serious (gravísimas). Currently summarized; await H4 for literal translation: **See:**
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-34` — Ley 19.628 Art. 34 (three-tier classification of infringements).
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-34-bis` — Ley 19.628 Art. 34 bis (minor infringements: transparency failures, missing contact information, failure to respond to requests).
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-34-ter` — Ley 19.628 Art. 34 ter (serious infringements: unlawful processing, purpose deviation, security failures, breach of processor obligations, obstruction of rights, unlawful international transfers).
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-34-quáter` — Ley 19.628 Art. 34 quáter (very serious infringements: fraudulent processing, malicious purpose deviation, sensitive-data confidentiality breach, children's data violations, deliberate concealment of breaches, knowing unlawful international transfers, non-compliance with Agency orders).

- *Fines* — Minor: up to 5,000 UTM (or written warning). Serious: up to 10,000 UTM. Very serious: up to 20,000 UTM. Reincidence and percentage-of-turnover rules apply for large enterprises. Currently summarized; await H4 for literal translation: **See:**
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-35` — Ley 19.628 Art. 35 (sanction scales; reincidence multiplier; turnover-percentage cap for large-enterprise recidivists).

- *Civil liability* — The controller must indemnify patrimonial and extra-patrimonial damage caused by unlawful processing. Civil action accrues once the Agency resolution or judicial sentence is final; five-year prescription. Currently summarized; await H4 for literal translation: **See:**
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-47` — Ley 19.628 Art. 47 (civil liability: patrimonial and extra-patrimonial damages; procedural pathway; five-year prescription).

- *Accessory sanction: suspension of operations* — For repeated very serious infringements within 24 months, the Agency may suspend processing operations for up to 30 days. Currently summarized; await H4 for literal translation: **See:**
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-38` — Ley 19.628 Art. 38 (accessory sanctions: suspension of operations; partial or total; cannot affect data subjects' rights).

- *Prescription* — Sanctions actions prescribe in four years from the infringement; three years from the final sanction resolution for execution. Currently summarized; await H4 for literal translation: **See:**
  - `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-40` — Ley 19.628 Art. 40 (prescription: four years for action; three years for execution; interrupted by notification of administrative procedure).

---

## Topic: Open Finance System (Sistema de Finanzas Abiertas)

- *Objectives and principles of the SFA* — The Open Finance System promotes competition, innovation, and financial inclusion by enabling consented exchange of financial customer data via standardised secure interfaces. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-16` — Ley 21.521 Art. 16 (SFA objectives, principles: proportionality, quality, transparency, data security/privacy, non-discrimination, interoperability).

- *Data perimeter of the SFA* — The SFA covers: public product/service terms (open data); KYC/identification data; transaction history for accounts, cards, loans, insurance, savings, investments (consent required; 5-year lookback); financial portability communications; payment initiation data; and CMF-extended categories. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-17` — Ley 21.521 Art. 17 (perimeter: six data categories; consent required for categories 2, 3, 5, 6; five-year transaction history limit).

- *Mandatory information-providing institutions* — Banks, card issuers, and authorized payment-instrument issuers must participate; CMF may extend obligation to cooperatives, fund managers, stockbrokers, and others. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-18` — Ley 21.521 Art. 18 (list of mandatory and CMF-extensible information-providing institutions).

- *Registration of information-based service providers* — Providers wishing to access SFA data must voluntarily register in the CMF's Information-Based Service Provider registry; denied to those with serious repeated data-protection infringements. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-19` — Ley 21.521 Art. 19 (registration requirements; technical/security compliance; suspension power; infringement bar).

- *SFA consent requirements* — Customer consent for SFA data sharing must be free, informed, explicit, purpose-specific, and time-bound; revocable at any time. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-23` — Ley 21.521 Art. 23 (consent and authentication requirements for SFA data queries and payment initiation).

- *Liability of SFA participants* — All SFA participants are responsible for integrity, availability, security, and confidentiality of data in each transaction and for compliance with Ley 19.628. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-24` — Ley 21.521 Art. 24 (participant liability; purpose limitation; breach response; complaint handling).

---

## Topic: Registration with CMF

- *Mandatory registration in the Registry of Financial-Service Providers* — Professional provision of crowdfunding platform, alternative trading system, intermediation, order routing, credit advisory, investment advisory, or custody services requires registration in the CMF's Registry. The registration requirement cannot be excepted even under CMF normative exemptions. **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-5` — Ley 21.521 Art. 5 (services requiring registration; entities that may provide services without registration; international-company domicile requirement).
  - `corpus/21521-fintech/titulo-02-servicios.md#article-4` — Ley 21.521 Art. 4 (CMF normative powers; registration obligation cannot be excepted; personal data obligations also cannot be excepted).

- *Registration requirements* — Applicants must submit the prescribed form plus identity/legal-capacity documents; CMF has 30 business days to rule; legal persons only; exclusive-purpose requirement; prior serious-infraction bar (10-year lookback). **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-6` — Ley 21.521 Art. 6 (registration requirements: form, documents, CMF timeline, exclusive-purpose rule, disqualification conditions).

- *Prior authorisation to commence services* — After registration, a separate CMF authorisation is required before commencing provision of most services; requirements differ by service type. **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-7` — Ley 21.521 Art. 7 (authorisation requirements per service type; CMF 6-month review period; CMF may suspend authorisation).

- *CMF supervision of all registered services* — The CMF supervises all Title II services using the powers granted by its organic law; may require information from registered entities by general regulation. **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-2` — Ley 21.521 Art. 2 (CMF supervision; information-reporting requirements from registered entities).

- *SFA information-based service providers: separate CMF registry* — Providers wishing to access SFA data register in a separate CMF registry (distinct from the Financial-Service Providers Registry). **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-19` — Ley 21.521 Art. 19 (Information-Based Service Provider registry; CMF approval within 6 months).

- *Registration application requirements (in practice)* — NCG 502 §I.A specifies the full set of antecedents a PSF must submit: completed CMF form, corporate and shareholder documents, evidence of exclusive purpose, and a conformity declaration.
  NCG 502 §I.A — see `corpus/ncg/502-psf-obligations/seccion-01-registro.md`.

- *Cancellation of registration (in practice)* — NCG 502 §I.B details the grounds and procedures by which CMF may cancel a PSF's registration, including remediation periods and winding-down obligations.
  NCG 502 §I.B — see `corpus/ncg/502-psf-obligations/seccion-01-registro.md`.

- *Exceptions to registration (in practice)* — NCG 502 §I.C sets out the specific activities and thresholds that fall outside the mandatory registration requirement.
  NCG 502 §I.C — see `corpus/ncg/502-psf-obligations/seccion-01-registro.md`.

- *Authorisation requirements by service type (in practice)* — NCG 502 §II sets out the pre-conditions CMF evaluates (governance documentation, systems evidence, capital) before granting authorisation, distinguishing investment advisory, credit advisory, platforms/ATS, order routing, and intermediation/custody.
  NCG 502 §II — see `corpus/ncg/502-psf-obligations/seccion-02-autorizacion.md`.

---

## Topic: Data Processor / Outsourcing

- *Third-party processor relationship* — The controller may process data through a third-party mandatary or processor. The processor must follow the controller's instructions and is prohibited from processing beyond the agreed purpose or ceding data without express authorisation. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis` — Ley 19.628 Art. 15 bis (processor obligations: instructions, purpose limitation, sub-processing rules, security obligations, breach reporting to controller, data return/erasure on completion).

- *Definition of processor* — A third-party mandatary or processor is any natural or legal person that processes personal data on behalf of the data controller. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-2` — Ley 19.628 Art. 2(x) (definition of tercero mandatario o encargado / third-party mandatary or processor).

- *Mandatory written contract* — The processor relationship must be governed by a written contract specifying: subject of assignment, duration, purpose, data types, data-subject categories, and parties' rights and obligations. Sub-delegation requires specific written authorisation; sub-processor liability is joint and several. Agency makes model contracts available. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis` — Ley 19.628 Art. 15 bis (paragraph 3: mandatory contract content; sub-delegation rules; Agency model contracts).

- *Processor security and confidentiality obligations* — The processor must comply with the duty of confidentiality (Art. 14 bis) and the duty to adopt security measures (Art. 14 quinquies). Differentiated SME compliance standards apply. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis` — Ley 19.628 Art. 15 bis (paragraph 4: processor must comply with Arts. 14 bis and 14 quinquies; SME differentiation applies; breach must be reported to controller).

- *Liability if processor exceeds mandate* — If the processor processes data for a different purpose or cedes data without authorisation, it is deemed a data controller for all legal purposes and is jointly and severally liable with the original controller for damages. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis` — Ley 19.628 Art. 15 bis (paragraph 2: liability conversion upon mandate-exceeding; joint-and-several liability).

- *Cession vs. processor relationship* — Cession of personal data (transferring data to another controller) is distinct from the processor relationship; cession requires its own consent or legal basis and makes the transferee a controller. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15` — Ley 19.628 Art. 15 (cession of personal data: lawful bases, written form, consent where required; null-and-void cession without required consent).

- *Outsourcing controls for platforms/ATS (in practice)* — PSFs operating crowdfunding platforms or alternative trading systems must apply specific outsourcing-management procedures: provider due diligence, written contracts with continuity clauses, right of audit, and concentration-risk limits.
  NCG 502 §IV.C.3.3 — see `corpus/ncg/502-psf-obligations/seccion-04c-gobierno-plataformas-sat.md`.

- *Outsourcing controls for intermediation/custody (in practice)* — Intermediation and custody PSFs face equivalent outsourcing requirements, with additional rules for custody-chain sub-delegation.
  NCG 502 §IV.E.4.3 — see `corpus/ncg/502-psf-obligations/seccion-04e-gobierno-intermediacion-custodia.md`.

---

## Topic: Cybersecurity

- *Security standards for SFA platform access* — Platforms accessing SFA data must comply with CMF-set information-security, cybersecurity, and risk-management standards. **See:**
  - `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-22` — Ley 21.521 Art. 22 (minimum security, cybersecurity, and risk-management standards; sensitive data classification under Ley 19.628 must be considered).

- *Security measures as data-protection prerequisite* — Controllers must adopt and maintain security measures (pseudonymization, encryption, resilience, restoration, regular testing) before a breach occurs. **See:**
  - `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quinquies` — Ley 19.628 Art. 14 quinquies (security measures: confidentiality, integrity, availability, resilience; burden of proof on controller).

- *Cybersecurity procedures for platforms/ATS (in practice)* — PSFs operating crowdfunding platforms or ATS must implement documented information-security and cybersecurity procedures covering access controls, vulnerability management, penetration testing, and security-event monitoring.
  NCG 502 §IV.C.3.1 — see `corpus/ncg/502-psf-obligations/seccion-04c-gobierno-plataformas-sat.md`.

- *Cybersecurity procedures for investment advisory PSFs (in practice)* — Investment advisory PSFs must maintain equivalent information-security controls; §IV.A.2.2 specifies the minimum policy requirements applicable to their governance framework.
  NCG 502 §IV.A.2.2 — see `corpus/ncg/502-psf-obligations/seccion-04a-gobierno-asesoria-inversion.md`.

- *Cybersecurity procedures for intermediation/custody PSFs (in practice)* — Intermediation and custody PSFs must apply cybersecurity controls aligned with the risks of their activity, including network segmentation and endpoint protection.
  NCG 502 §IV.E.4.1 — see `corpus/ncg/502-psf-obligations/seccion-04e-gobierno-intermediacion-custodia.md`.

---

## Topic: Risk Management / Governance

- *Governance and risk management (law requirement)* — CMF may require governance structures and risk-management processes as a condition of authorisation. **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-12` — Ley 21.521 Art. 12 (governance and risk-management requirements set by CMF regulation).

- *Board responsibility and policies for investment advisory PSFs (in practice)* — The board must formally approve the risk-management framework, internal-control policies, compliance function charter, and conflict-of-interest policy. The risk and compliance functions must report directly to the board or a board committee.
  NCG 502 §IV.A — see `corpus/ncg/502-psf-obligations/seccion-04a-gobierno-asesoria-inversion.md`.

- *Governance for credit advisory PSFs (in practice)* — Parallel board-responsibility and policy-approval requirements apply to credit advisory PSFs, with additional rules for model governance and fair-lending policies.
  NCG 502 §IV.B — see `corpus/ncg/502-psf-obligations/seccion-04b-gobierno-asesoria-crediticia.md`.

- *Governance for crowdfunding platforms and ATS (in practice)* — Platforms and ATS must adopt board-approved operational, risk-management, and technology policies; §IV.C addresses project-vetting controls, investor eligibility procedures, and platform-integrity rules.
  NCG 502 §IV.C — see `corpus/ncg/502-psf-obligations/seccion-04c-gobierno-plataformas-sat.md`.

- *Governance for order-routing PSFs (in practice)* — Order-routing providers must maintain best-execution policies, conflict-of-interest controls, and operational-resilience frameworks approved by their board.
  NCG 502 §IV.D — see `corpus/ncg/502-psf-obligations/seccion-04d-gobierno-enrutamiento.md`.

- *Governance for intermediation and custody PSFs (in practice)* — Intermediation and custody PSFs face the most extensive governance requirements: segregation of client assets, custody controls, transaction-monitoring policies, and an independent internal audit function.
  NCG 502 §IV.E — see `corpus/ncg/502-psf-obligations/seccion-04e-gobierno-intermediacion-custodia.md`.

---

## Topic: Business Continuity

- *Business continuity for platforms/ATS (in practice)* — Crowdfunding platforms and ATS must maintain a documented business continuity plan (BCP) and disaster recovery plan (DRP), tested at least annually, covering critical systems and customer-data recovery.
  NCG 502 §IV.C.3.2 — see `corpus/ncg/502-psf-obligations/seccion-04c-gobierno-plataformas-sat.md`.

- *Business continuity for intermediation/custody PSFs (in practice)* — Intermediation and custody PSFs must maintain equivalent BCP/DRP arrangements, with additional requirements for post-recovery reconciliation of custody records.
  NCG 502 §IV.E.4.2 — see `corpus/ncg/502-psf-obligations/seccion-04e-gobierno-intermediacion-custodia.md`.

---

## Topic: Capital Requirements

- *Minimum equity (law requirement)* — CMF sets minimum equity thresholds per service type; providers must maintain compliance throughout operation. **See:**
  - `corpus/21521-fintech/titulo-02-servicios.md#article-11` — Ley 21.521 Art. 11 (minimum equity requirements; CMF may adjust by regulation).

- *Capital classification (in practice)* — NCG 502 §V.A classifies eligible capital components (paid-in capital, retained earnings, reserves) and sets the deductions that reduce regulatory capital.
  NCG 502 §V.A — see `corpus/ncg/502-psf-obligations/seccion-05-capital-garantias.md`.

- *Minimum equity by service type (in practice)* — NCG 502 §V.B specifies the absolute minimum-equity floor for each PSF service category; providers below the threshold must remediate within the prescribed period or cease operations.
  NCG 502 §V.B — see `corpus/ncg/502-psf-obligations/seccion-05-capital-garantias.md`.

- *Risk-weighted assets and capital charge (in practice)* — NCG 502 §V.D sets out the risk-weighting framework: credit risk, operational risk, market risk, and specific charges by asset class; §V.D.4 covers capital charges for crypto-asset exposures.
  NCG 502 §V.D — see `corpus/ncg/502-psf-obligations/seccion-05-capital-garantias.md`.

- *Crypto-asset capital charge (in practice)* — PSFs holding or intermediating crypto-assets must apply the highest risk-weight tier under §V.D.4; §V.D.4.1 lists Type-A crypto-assets (those qualifying for a lower charge if certain criteria are met).
  NCG 502 §V.D.4 / §V.D.4.1 — see `corpus/ncg/502-psf-obligations/seccion-05-capital-garantias.md`.

---

## Topic: Disclosure Obligations (PSF)

- *Disclosure obligations for each PSF service type (in practice)* — NCG 502 §III operationalises the information-delivery requirements of Ley 21.521: pre-contractual key-information sheets, tariff schedules, risk warnings, conflict-of-interest disclosures, and post-trade or periodic reporting vary by service.
  NCG 502 §III — see `corpus/ncg/502-psf-obligations/seccion-03-divulgacion.md`.

---

## Topic: Crypto-Assets

- *Crypto-asset capital charge (in practice)* — PSFs with crypto-asset exposures must hold capital calculated under the highest risk-weight tier; §V.D.4.1 defines the Type-A crypto-asset list eligible for a reduced charge if specific custody and valuation conditions are satisfied.
  NCG 502 §V.D.4 / §V.D.4.1 — see `corpus/ncg/502-psf-obligations/seccion-05-capital-garantias.md`.

---

## Topic: Operational Capacity

- *Operational capacity and final provisions (in practice)* — NCG 502 §VI–IX cover the operational-capacity self-assessment obligations PSFs must perform before commencing services, the CMF's ongoing reporting requirements, transitional provisions, and the entry-into-force rules.
  NCG 502 §VI–IX — see `corpus/ncg/502-psf-obligations/seccion-06-09-disposiciones-finales.md`.
