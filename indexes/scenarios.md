# Scenarios

Pre-built compliance checklists for common features. Every checklist item ends
in a citation to the corpus. When using a scenario, READ the cited articles
in full — these checklists summarize, they do not substitute for the article
text itself.

---

## Scenario 1: Storing National IDs and Contact Information

**Likely fintech scope (Ley 21.521):** No — storing RUTs, names, emails, and
phones is a data-management function, not a regulated fintech service; no CMF
registration is required for this feature alone. However, if this data
underpins a service that does fall under Ley 21.521 (e.g., an investment
application), the broader registration requirements apply.

**Data-protection scope (Ley 19.628):** Yes — RUTs and contact details are
personal data under Art. 2(f); any storage or processing of this data triggers
full Ley 19.628 obligations.

### Obligations checklist

- [ ] Confirm that storing RUTs constitutes processing of personal data and document
  this in your data register — Ley 19.628 Art. 2(f).
  (See `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-2`.)

- [ ] Establish and document a lawful basis for processing RUTs and contact
  information before collection begins (consent, contract, or legal obligation
  are the most common bases) — Ley 19.628 Art. 12 and Art. 13.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-12`.)
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-13`.)

- [ ] If a service contract is the lawful basis (e.g., onboarding for a product),
  ensure the contract is concluded and its terms make clear that contact data
  will be used for account management — Ley 19.628 Art. 13(c).
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-13`.)

- [ ] Publish a permanently operative email address or contact form on the
  product/company website for data-subject rights requests — Ley 19.628 Art. 14 ter(c).
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter`.)

- [ ] Publish the retention period for RUT and contact data on the company
  website — Ley 19.628 Art. 14 ter(i).
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter`.)

- [ ] Delete or anonymize RUTs and contact data once the purpose for which they
  were collected is fulfilled and no other legal basis for retention exists —
  Ley 19.628 Art. 3(c).
  (See `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-3`.)

- [ ] Implement technical security measures (pseudonymization, access controls,
  encryption at rest) before storing ID data in production — Ley 19.628 Art. 14 quinquies.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quinquies`.)

- [ ] Adopt privacy-by-design and privacy-by-default measures: collect only fields
  strictly necessary for the stated purpose; do not pre-tick optional marketing
  fields — Ley 19.628 Art. 14 quáter.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quáter`.)

- [ ] If any third-party service (e.g., a cloud CRM or identity-verification API)
  processes RUTs or contact data on your behalf, execute a written data-processing
  agreement covering subject, duration, purpose, and security obligations before
  granting access — Ley 19.628 Art. 15 bis.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis`.)

- [ ] Build and maintain a process for data subjects to exercise access,
  rectification, erasure, blocking, and portability rights; set a 30-calendar-day
  response deadline — Ley 19.628 Art. 10 and Art. 11.
  (See `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-10`.)
  (See `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-11`.)

- [ ] If your product will share or receive customer identification/KYC data
  through the Open Finance System (e.g., during onboarding via an SFA channel),
  obtain explicit prior customer consent specifying purpose and validity —
  Ley 21.521 Art. 17(2).
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-17`.)

### Watch-outs

- **Consent is not automatically free when tied to a service contract.** If you
  make consent to data collection a precondition for using a service, consent is
  presumed not freely given; use the contract lawful basis (Art. 13(c)) instead
  of consent for data strictly necessary to perform the contract.
  (Ley 19.628 Art. 12.)

- **Foreign-controller obligation.** If your infrastructure or corporate entity
  is not domiciled in Chile but you process data of Chilean residents, you must
  designate and maintain a Chilean contact address for data subjects and the
  Agency. (Ley 19.628 Art. 14.)
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14`.)

- **Breach notification for ID data.** A breach affecting RUTs or contact data
  that poses reasonable risk to data subjects must be reported to the APDP
  without undue delay. If financial or sensitive data is also involved, direct
  notification to affected data subjects is additionally required. (Ley 19.628
  Art. 14 sexies.)

### Related scenarios

- Scenario 2: if RUT/contact data is processed together with bank statements,
  the additional financial-data rules and mandatory breach-notification-to-subjects
  obligations apply.
- Scenario 7: if RUTs or contact data are stored in US/EU cloud infrastructure,
  cross-border transfer rules are triggered.

---

## Scenario 2: Aggregating / Displaying Bank Statements (Read-Only)

**Likely fintech scope (Ley 21.521):** Yes — read-only aggregation and display
of a user's bank account and transaction data falls within the Open Finance
System (SFA); you must register as an Information-Based Service Provider in the
CMF's SFA registry before accessing bank data.

**Data-protection scope (Ley 19.628):** Yes — transaction history is financial
personal data; its processing triggers both general Ley 19.628 obligations and
the special financial-data rules of Título III.

### Obligations checklist

- [ ] Register as an Information-Based Service Provider in the CMF's SFA registry
  before requesting any bank transaction data from information-providing
  institutions — Ley 21.521 Art. 19.
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-19`.)

- [ ] Obtain prior explicit customer consent for each data access, specifying
  the data type (transaction history), purpose (display/aggregation), and
  maximum validity period before querying any bank API — Ley 21.521 Art. 23.
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-23`.)

- [ ] Limit data access and storage strictly to the scope covered by the
  customer's authorisation; do not store transaction data for purposes not
  specified in the consent — Ley 21.521 Art. 24.
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-24`.)

- [ ] Do not retrieve or display bank transaction history going back more than
  five years — Ley 21.521 Art. 17(3).
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-17`.)

- [ ] Implement and maintain the CMF-prescribed information-security,
  cybersecurity, and risk-management standards for SFA platform access;
  document compliance before going live — Ley 21.521 Art. 22.
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-22`.)

- [ ] Report any security incident affecting SFA data to the CMF without delay;
  simultaneously adopt risk-mitigation measures — Ley 21.521 Art. 22(2).
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-22`.)

- [ ] Document a lawful basis for processing financial obligation data (the
  financial-obligation basis under Art. 13(a) applies where data is used in
  the SFA context; confirm which basis applies for your specific use) —
  Ley 19.628 Art. 13(a).
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-13`.)

- [ ] Apply the financial-data rules of Título III: do not communicate
  transaction data relating to obligations that were extinguished more than
  five years ago; apply mandatory erasure rules for prescribed obligations
  without waiting for a request — Ley 19.628 Art. 17 and Art. 18.
  (See `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-17`.)
  (See `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-18`.)

- [ ] Implement security measures (encryption in transit and at rest, access
  controls, audit logs) for all stored or transmitted transaction data —
  Ley 19.628 Art. 14 quinquies.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quinquies`.)

- [ ] In the event of a breach affecting bank transaction data, notify affected
  data subjects directly (or via mass media if individual notification is
  impossible) in addition to reporting to the APDP — Ley 19.628 Art. 14 sexies.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-sexies`.)

- [ ] Publish on the company website: the existence of the SFA data aggregation
  feature, the purposes of processing, and the retention period for transaction
  data — Ley 19.628 Art. 14 ter.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter`.)

- [ ] Provide a mechanism for customers to revoke their SFA consent at any time
  and immediately cease data access upon revocation — Ley 21.521 Art. 23.
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-23`.)

- [ ] Submit the SFA registration application with all required antecedents (corporate documents, exclusive-purpose evidence, conformity declaration) — NCG 502 §I.A.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-01-registro.md`.)

- [ ] Implement documented information-security and cybersecurity procedures before accessing any SFA data in production — NCG 502 §IV.C.3.1.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04c-gobierno-plataformas-sat.md`.)

- [ ] Establish and test a business continuity plan and disaster recovery plan covering the SFA aggregation platform — NCG 502 §IV.C.3.2.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04c-gobierno-plataformas-sat.md`.)

- [ ] Apply outsourcing controls (provider due diligence, written contracts with continuity and audit clauses) to any third-party infrastructure supporting the aggregation service — NCG 502 §IV.C.3.3.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04c-gobierno-plataformas-sat.md`.)

- [ ] Establish the operational-incident reporting procedure and report any incident to CMF using the Anexo N°2 form within the prescribed deadlines — NCG 502 §IV.C.7 / Anexo N°2.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04c-gobierno-plataformas-sat.md` and `corpus/ncg/502-psf-obligations-consolidated/anexo-02-reporte-incidentes.md`.)

- [ ] Maintain an operational-loss register and submit periodic loss reports to CMF using the Anexo N°3 form — NCG 502 Anexo N°3.
  (See `corpus/ncg/502-psf-obligations-consolidated/anexo-03-reporte-perdidas.md`.)

- [ ] Determine your SFA participant role (consuming account data makes you a PSBI — Information-Based Service Provider) and register in the corresponding CMF SFA registry before requesting any data — NCG 514 §I.C / §I.E.
  (See `corpus/ncg/514-open-finance/seccion-01-perimetro.md`.)

- [ ] Connect through the SFA APIs and meet the API/information-exchange standards (principal mechanism, technical/data standards, availability and performance) before querying bank data — NCG 514 §II.A.
  (See `corpus/ncg/514-open-finance/seccion-02-funcionamiento.md`.)

- [ ] Implement open-finance consent management per the SFA operational rules: granting of consent and ongoing consent management/information obligations — NCG 514 §III.D (+ Ley 19.628 Art. 12).
  (See `corpus/ncg/514-open-finance/seccion-03-seguridad-resguardos.md`.)
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-12`.)

- [ ] Satisfy the SFA security, cybersecurity, business-continuity, and authentication standards (information-security management, incident reporting, API contingency standards, and customer/participant authentication) — NCG 514 §III.B / §III.C.
  (See `corpus/ncg/514-open-finance/seccion-03-seguridad-resguardos.md`.)

- [ ] Meet the SFA data-protection obligations for shared information, tying participant duties to Ley 19.628 — NCG 514 §IV.D (+ Ley 19.628).
  (See `corpus/ncg/514-open-finance/seccion-04-informacion.md`.)

- [ ] Identify the data sets and variables you must consume (data sets, variables, availability deadlines) and the exact field specifications in the annexes (terms and conditions, service channels/ATM, enrollment, historical financial positions, transactional information) — NCG 514 §IV.A / §VI annexes.
  (See `corpus/ncg/514-open-finance/seccion-04-informacion.md` and `corpus/ncg/514-open-finance/seccion-06-anexos.md`.)

### Watch-outs

- **Read-only does not exempt from SFA registration.** Even if you only display
  data and never execute transactions, accessing bank APIs for account
  aggregation falls within the SFA and requires CMF registration.
  (Ley 21.521 Art. 19.)

- **Purpose limitation is strictly enforced.** Using aggregated transaction
  data for secondary purposes (e.g., marketing analytics, credit scoring) that
  were not specified in the original consent is a serious infringement. (Ley
  19.628 Art. 34 ter.)
  (See `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-34-ter`.)

- **Five-year lookback is a hard limit on what you may query**, not merely a
  display filter. Do not request data older than five years from information-providing
  institutions even if you intend to truncate it client-side.
  (Ley 21.521 Art. 17(3).)

### Related scenarios

- Scenario 1: bank statements contain RUTs and contact data, so obligations from
  Scenario 1 apply cumulatively.
- Scenario 3: if you also display investment/savings instruments alongside bank
  statements, Scenario 3's investment-tracker obligations apply.
- Scenario 7: if transaction data is sent to or stored in non-Chilean cloud
  infrastructure, Scenario 7's cross-border transfer rules apply.

---

## Scenario 3: Investment Tracker (Read-Only Aggregation)

**Likely fintech scope (Ley 21.521):** Yes — aggregating investment and savings
data from information-providing institutions (banks, fund managers, brokers)
requires registration as an Information-Based Service Provider in the CMF's SFA
registry; savings and investment instruments are explicitly within the SFA data
perimeter.

**Data-protection scope (Ley 19.628):** Yes — holdings data is financial
personal data and processing it triggers full Ley 19.628 obligations.

### Obligations checklist

- [ ] Register as an Information-Based Service Provider in the CMF's SFA registry
  before accessing any investment or savings data from information-providing
  institutions; confirm no prior serious data-protection infringements bar
  registration — Ley 21.521 Art. 19.
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-19`.)

- [ ] Obtain prior explicit customer consent for each data query, specifying
  the categories of investment data, the aggregation purpose, and maximum validity
  period — Ley 21.521 Art. 23.
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-23`.)

- [ ] Confirm that the data you plan to access falls within the SFA perimeter
  (savings or investment instruments under Art. 17(3)(e)); expand only to
  CMF-approved categories — Ley 21.521 Art. 17(3).
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-17`.)

- [ ] Do not use, store, or further process investment data for any purpose
  beyond the scope of the customer's authorisation — Ley 21.521 Art. 24.
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-24`.)

- [ ] Limit transaction history queries to a five-year lookback maximum —
  Ley 21.521 Art. 17(3).
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-17`.)

- [ ] Comply with CMF-set information-security, cybersecurity, and risk-management
  standards; document the security architecture and controls before going live —
  Ley 21.521 Art. 22.
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-22`.)

- [ ] Establish a procedure to respond to customer complaints about data integrity
  errors or unauthorized access to investment data — Ley 21.521 Art. 24.
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-24`.)

- [ ] Publish on the website: that investment data is aggregated via the SFA,
  the purposes, the data retention period, and that the user can revoke consent
  at any time — Ley 19.628 Art. 14 ter.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter`.)

- [ ] Implement and document security measures (encryption, access controls,
  pseudonymization where feasible) for all stored holdings data —
  Ley 19.628 Art. 14 quinquies.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quinquies`.)

- [ ] Apply privacy-by-default: store the minimum fields required to present
  the tracker view; do not retain raw position data beyond session if it is
  not needed persistently — Ley 19.628 Art. 14 quáter.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quáter`.)

- [ ] Submit the SFA registration application with all required antecedents (corporate documents, exclusive-purpose evidence, conformity declaration) — NCG 502 §I.A.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-01-registro.md`.)

- [ ] Implement documented information-security and cybersecurity procedures before accessing any SFA investment data in production — NCG 502 §IV.C.3.1.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04c-gobierno-plataformas-sat.md`.)

- [ ] Establish and test a business continuity plan and disaster recovery plan covering the investment tracker platform — NCG 502 §IV.C.3.2.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04c-gobierno-plataformas-sat.md`.)

- [ ] Apply outsourcing controls to any third-party infrastructure used for data aggregation or storage — NCG 502 §IV.C.3.3.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04c-gobierno-plataformas-sat.md`.)

- [ ] Establish the CMF operational-incident reporting procedure; report incidents using the Anexo N°2 form within prescribed deadlines — NCG 502 §IV.C.7 / Anexo N°2.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04c-gobierno-plataformas-sat.md` and `corpus/ncg/502-psf-obligations-consolidated/anexo-02-reporte-incidentes.md`.)

- [ ] Maintain an operational-loss register and submit periodic loss reports to CMF using the Anexo N°3 form — NCG 502 Anexo N°3.
  (See `corpus/ncg/502-psf-obligations-consolidated/anexo-03-reporte-perdidas.md`.)

- [ ] Determine your SFA participant role (an investment tracker that consumes account/holdings data is a PSBI — Information-Based Service Provider) and register in the corresponding CMF SFA registry — NCG 514 §I.C / §I.E.
  (See `corpus/ncg/514-open-finance/seccion-01-perimetro.md`.)

- [ ] Connect through the SFA APIs and meet the API/information-exchange standards (principal mechanism, technical/data standards, availability and performance) before querying investment or savings data — NCG 514 §II.A.
  (See `corpus/ncg/514-open-finance/seccion-02-funcionamiento.md`.)

- [ ] Implement open-finance consent management per the SFA operational rules: granting of consent and ongoing consent management/information obligations — NCG 514 §III.D (+ Ley 19.628 Art. 12).
  (See `corpus/ncg/514-open-finance/seccion-03-seguridad-resguardos.md`.)
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-12`.)

- [ ] Satisfy the SFA security, cybersecurity, business-continuity, and authentication standards (information-security management, incident reporting, API contingency standards, and customer/participant authentication) — NCG 514 §III.B / §III.C.
  (See `corpus/ncg/514-open-finance/seccion-03-seguridad-resguardos.md`.)

- [ ] Meet the SFA data-protection obligations for shared information, tying participant duties to Ley 19.628 — NCG 514 §IV.D (+ Ley 19.628).
  (See `corpus/ncg/514-open-finance/seccion-04-informacion.md`.)

- [ ] Identify the data sets and variables you must consume (data sets, variables, availability deadlines) and the exact field specifications in the annexes (historical financial positions, transactional information, terms and conditions, enrollment) — NCG 514 §IV.A / §VI annexes.
  (See `corpus/ncg/514-open-finance/seccion-04-informacion.md` and `corpus/ncg/514-open-finance/seccion-06-anexos.md`.)

### Watch-outs

- **Displaying aggregate holdings does not automatically make you an investment
  adviser.** However, if the tracker shows personalized performance comparisons,
  benchmark recommendations, or suggested rebalancing actions, you risk crossing
  into investment advisory territory, which triggers Scenario 4 requirements.
  (Ley 21.521 Art. 5.)

- **CMF may bar registration if your organization has a history of serious
  data-protection infringements.** Conduct a clean-slate review of prior
  regulatory actions before applying. (Ley 21.521 Art. 19.)

### Related scenarios

- Scenario 2: investment tracker and bank-statement aggregation share the same
  SFA legal framework; if both features coexist in a single app, obligations
  accumulate.
- Scenario 4: adding advisory or execution features to the tracker requires the
  full registration and authorisation regime for investment applications.
- Scenario 7: if holdings data is processed in non-Chilean cloud infrastructure,
  cross-border transfer rules apply.

---

## Scenario 4: Investment Application (Executing Orders or Providing Advisory)

**Likely fintech scope (Ley 21.521):** Yes — executing orders, intermediating
financial instruments, or providing investment advisory on a professional basis
requires both registration in the CMF's Registry of Financial-Service Providers
and a separate prior CMF authorisation before commencing services.

**Data-protection scope (Ley 19.628):** Yes — customer profiles, trading history,
and portfolio data are financial personal data triggering full Ley 19.628
obligations; profiling for suitability assessment also triggers automated-decision
rules.

### Obligations checklist

- [ ] Register in the CMF's Registry of Financial-Service Providers for the
  investment advisory and/or intermediation service categories before offering
  any service to customers; international companies must establish Chilean
  domicile — Ley 21.521 Art. 5 and Art. 6.
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-5`.)
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-6`.)

- [ ] Obtain prior CMF authorisation to commence services after completing
  registration; submit evidence of information systems, suitability, and
  governance as required for investment advisory — Ley 21.521 Art. 7(5).
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-7`.)

- [ ] Ensure all persons and systems used to provide investment advisory meet
  CMF objectivity, coherence, and consistency standards; comply with CMF
  knowledge-certification requirements — Ley 21.521 Art. 9.
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-9`.)

- [ ] Implement governance structures and risk-management processes as required
  by CMF regulation, including documentation of control frameworks —
  Ley 21.521 Art. 12.
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-12`.)

- [ ] Adopt written policies to avoid offering products inconsistent with the
  customer's stated needs, expectations, and risk tolerance; document the
  customer-profile assessment process — Ley 21.521 Art. 28.
  (See `corpus/21521-fintech/titulo-04-otras-disposiciones.md#article-28`.)

- [ ] Once business-volume thresholds are reached, constitute bank guarantees
  or insurance policies for intermediation and order-routing services —
  Ley 21.521 Art. 10.
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-10`.)

- [ ] Comply with CMF information-reporting obligations: register required
  information with CMF by general regulation; maintain records of transactions
  and advice given — Ley 21.521 Art. 2 and Art. 8.
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-2`.)
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-8`.)

- [ ] Establish and document a lawful basis (contract or consent) for
  processing customer financial personal data collected during onboarding
  and during the advisory/execution lifecycle — Ley 19.628 Art. 12 and Art. 13.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-12`.)
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-13`.)

- [ ] Apply Título III rules to any financial obligation data: respect the
  five-year communication limit and mandatory erasure of prescribed obligations
  without requiring a customer request — Ley 19.628 Art. 17 and Art. 18.
  (See `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-17`.)
  (See `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-18`.)

- [ ] Implement security measures (encryption, access controls, audit trails)
  for all customer portfolio and transaction data; document security architecture
  as required by CMF and by Ley 19.628 — Ley 19.628 Art. 14 quinquies.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quinquies`.)

- [ ] Execute written data-processing agreements with all third-party providers
  (custodians, clearing systems, identity-verification services) that process
  customer data on your behalf — Ley 19.628 Art. 15 bis.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis`.)

- [ ] Publish on the website: data categories processed, purposes, retention
  period, third-party recipients, and customer rights; maintain a permanently
  operative contact channel for rights requests — Ley 19.628 Art. 14 ter.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter`.)

- [ ] Submit the CMF registration application with all required antecedents (corporate documents, exclusive-purpose evidence, shareholder information, conformity declaration) — NCG 502 §I.A.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-01-registro.md`.)

- [ ] Obtain NCG 502 §II authorisation: submit governance documentation, systems evidence, and capital confirmation as required for the investment advisory and/or intermediation service category — NCG 502 §II.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-02-autorizacion.md`.)

- [ ] Board approves governance, risk-management, compliance, and conflict-of-interest policies before commencing services — NCG 502 §IV.A (investment advisory) or §IV.E (intermediation/custody).
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04a-gobierno-asesoria-inversion.md` and `corpus/ncg/502-psf-obligations-consolidated/seccion-04e-gobierno-intermediacion-custodia.md`.)

- [ ] Implement information-security and cybersecurity controls per NCG 502 §IV.A.2.2 (advisory) / §IV.E.4.1 (intermediation/custody).
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04a-gobierno-asesoria-inversion.md` and `corpus/ncg/502-psf-obligations-consolidated/seccion-04e-gobierno-intermediacion-custodia.md`.)

- [ ] Establish and test a business continuity plan and disaster recovery plan — NCG 502 §IV.E.4.2 (intermediation/custody); apply equivalent BCP standards for advisory per §IV.A.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04e-gobierno-intermediacion-custodia.md`.)

- [ ] Apply outsourcing controls (due diligence, written contracts, audit rights, concentration-risk limits) to all third-party service providers — NCG 502 §IV.E.4.3 (intermediation/custody) / §IV.A.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04e-gobierno-intermediacion-custodia.md`.)

- [ ] Establish the CMF operational-incident reporting procedure and report incidents using the Anexo N°2 form — NCG 502 §IV.A.5 / §IV.E.8 / Anexo N°2.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-04a-gobierno-asesoria-inversion.md` and `corpus/ncg/502-psf-obligations-consolidated/anexo-02-reporte-incidentes.md`.)

- [ ] Maintain an operational-loss register and submit periodic loss reports to CMF using the Anexo N°3 form — NCG 502 Anexo N°3.
  (See `corpus/ncg/502-psf-obligations-consolidated/anexo-03-reporte-perdidas.md`.)

- [ ] Meet minimum-equity and guarantee requirements per NCG 502 §V.B; maintain capital above the floor throughout operation and constitute bank guarantees or insurance once volume thresholds are reached — NCG 502 §V.B.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-05-capital-garantias.md`.)

- [ ] Deliver pre-contractual key-information sheets, fee schedules, and conflict-of-interest disclosures per NCG 502 §III disclosure obligations for the applicable service type — NCG 502 §III.
  (See `corpus/ncg/502-psf-obligations-consolidated/seccion-03-divulgacion.md`.)

- [ ] If the application also consumes customer account/holdings data through the Open Finance System, determine your SFA participant role (PSBI; PSIP if you also initiate payments) and register in the corresponding CMF SFA registry — NCG 514 §I.C / §I.D / §I.E.
  (See `corpus/ncg/514-open-finance/seccion-01-perimetro.md`.)

- [ ] Connect through the SFA APIs and meet the API/information-exchange standards before querying any SFA data — NCG 514 §II.A.
  (See `corpus/ncg/514-open-finance/seccion-02-funcionamiento.md`.)

- [ ] Implement open-finance consent management per the SFA operational rules (granting and ongoing management of consent, information obligations) — NCG 514 §III.D (+ Ley 19.628 Art. 12).
  (See `corpus/ncg/514-open-finance/seccion-03-seguridad-resguardos.md`.)
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-12`.)

- [ ] Satisfy the SFA security, cybersecurity, continuity, and authentication standards for SFA participants — NCG 514 §III.B / §III.C.
  (See `corpus/ncg/514-open-finance/seccion-03-seguridad-resguardos.md`.)

- [ ] Meet the SFA data-protection obligations for shared information — NCG 514 §IV.D (+ Ley 19.628).
  (See `corpus/ncg/514-open-finance/seccion-04-informacion.md`.)

- [ ] Identify the SFA data sets, variables, and the exact field specifications in the annexes that your application must consume — NCG 514 §IV.A / §VI annexes.
  (See `corpus/ncg/514-open-finance/seccion-04-informacion.md` and `corpus/ncg/514-open-finance/seccion-06-anexos.md`.)

### Watch-outs

- **Registration and authorisation are separate sequential steps.** You may not
  commence services after registration alone; a separate CMF authorisation with
  a 6-month review period applies. (Ley 21.521 Art. 7.)

- **Minimum equity requirements apply.** CMF sets minimum equity thresholds
  per service type; verify current CMF normative before finalizing the capital
  structure. (Ley 21.521 Art. 11.)
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-11`.)

- **Cancellation of registration.** CMF may cancel registration for serious
  infractions listed in Art. 14 of Ley 21.521; maintain compliance logs to
  demonstrate adherence. (Ley 21.521 Art. 13 and Art. 14.)
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-13`.)
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-14`.)

### Related scenarios

- Scenario 3: if the application also aggregates holdings data from third-party
  institutions via the SFA, add the SFA registration and consent obligations
  from Scenario 3.
- Scenario 5: if AI generates investment recommendations within the application,
  add all AI-recommendation obligations from Scenario 5.
- Scenario 7: if customer trading data is processed in non-Chilean infrastructure,
  add Scenario 7 obligations.

---

## Scenario 5: AI-Based Recommendations

**Likely fintech scope (Ley 21.521):** Maybe — if the AI recommends financial
actions (e.g., "buy this fund", "rebalance your portfolio"), the system likely
constitutes investment advisory and requires CMF registration under Art. 5;
if recommendations are purely informational or generic, scope is narrower but
the suitability standard (Art. 9) still applies to the system itself.

**Data-protection scope (Ley 19.628):** Yes — AI recommendations using
personal financial or behavioural data constitute automated individual decisions
and/or profiling, triggering specific rights, transparency duties, and DPIA
requirements.

### Obligations checklist

- [ ] Determine whether the AI recommendation feature constitutes investment
  advisory under Ley 21.521; if yes, complete CMF registration and authorisation
  before deploying the feature — Ley 21.521 Art. 5.
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-5`.)

- [ ] Ensure the AI system meets CMF objectivity, coherence, and consistency
  standards for advisory systems; document the methodology and validation
  process — Ley 21.521 Art. 9.
  (See `corpus/21521-fintech/titulo-02-servicios.md#article-9`.)

- [ ] Conduct a Data Protection Impact Assessment (DPIA) before deploying
  the AI system if it performs systematic exhaustive profiling that produces
  legally significant effects for data subjects — Ley 19.628 Art. 15 ter(a).
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-ter`.)

- [ ] If the AI performs large-scale automated processing of personal data
  (regardless of whether individual effects are significant), conduct a DPIA
  before going live — Ley 19.628 Art. 15 ter(b).
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-ter`.)

- [ ] Implement the mandatory safeguards for automated individual decisions:
  give data subjects the right to obtain human review, the right to an explanation
  of the recommendation logic, and the right to contest the decision —
  Ley 19.628 Art. 8 bis.
  (See `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8-bis`.)

- [ ] Establish a lawful basis for automated decisions: either obtain prior and
  express consent per Art. 12, use the decision for contract performance, or
  have statutory authorisation — Ley 19.628 Art. 8 bis(a)–(c).
  (See `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8-bis`.)

- [ ] Publish on the company website the existence of automated decision-making
  and profiling, a meaningful description of the logic applied, and the
  foreseeable consequences for data subjects — Ley 19.628 Art. 14 ter(l).
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter`.)

- [ ] Provide data subjects with access to information about the logic applied
  to automated decisions concerning them, upon request — Ley 19.628 Art. 5(f).
  (See `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-5`.)

- [ ] Implement and document a mechanism for customers to opt out of automated
  recommendations and receive a human-reviewed alternative — Ley 19.628 Art. 8 bis.
  (See `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8-bis`.)

- [ ] Adopt written customer-profile assessment policies so that recommendations
  are consistent with the customer's stated needs, expectations, and risk
  tolerance — Ley 21.521 Art. 28.
  (See `corpus/21521-fintech/titulo-04-otras-disposiciones.md#article-28`.)

- [ ] Establish a lawful basis and purpose limitation for the personal data
  used to train or run the recommendation model; do not repurpose customer
  data for model improvement without a compatible purpose or new consent —
  Ley 19.628 Art. 3(b).
  (See `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-3`.)

- [ ] If the recommendation model uses financial obligation data as input,
  apply Título III rules and the five-year limit — Ley 19.628 Art. 17.
  (See `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-17`.)

### Watch-outs

- **Marketing profiling has an absolute opt-out.** If any recommendation is
  driven by direct-marketing profiling (as opposed to genuine advisory), data
  subjects may always oppose with no override possible. (Ley 19.628 Art. 8(b).)
  (See `corpus/19628-data-protection-consolidated/titulo-01-utilizacion.md#article-8`.)

- **Safeguards are mandatory even when an exception applies.** Even where
  automated decisions are permitted (contract, consent, or law), you must
  still implement the explanation, human-review, and contest safeguards.
  (Ley 19.628 Art. 8 bis.)

- **DPIA cannot be deferred.** The DPIA must be completed before the processing
  begins; retroactive DPIAs do not satisfy the legal requirement. (Ley 19.628
  Art. 15 ter.)

### Related scenarios

- Scenario 4: if the AI is embedded in an investment application, all of
  Scenario 4's CMF registration and authorisation obligations apply.
- Scenario 6: if the AI parses user-supplied documents (PDFs, statements)
  as input, add Scenario 6 obligations.
- Scenario 7: if the recommendation model runs in non-Chilean cloud infrastructure
  or sends data offshore for inference, add Scenario 7 obligations.

---

## Scenario 6: AI-Based Document Parsing (PDFs, Statements)

**Likely fintech scope (Ley 21.521):** No — document parsing is a data-processing
operation, not a regulated fintech service in its own right; however, if parsed
data feeds a regulated service (e.g., investment advisory, account aggregation),
the applicable fintech obligations from those scenarios apply to the downstream
use.

**Data-protection scope (Ley 19.628):** Yes — extracting information from bank
statements, identity documents, or financial PDFs constitutes processing of
personal data (including potentially financial obligation and sensitive data);
full Ley 19.628 obligations apply.

### Obligations checklist

- [ ] Confirm that document parsing constitutes processing of personal data
  under Art. 2(o) and document this classification in your data register —
  Ley 19.628 Art. 2(o).
  (See `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-2`.)

- [ ] Establish a lawful basis for the parsing operation before processing any
  document; for user-submitted documents, consent is typically the most
  appropriate basis — Ley 19.628 Art. 12.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-12`.)

- [ ] Collect only fields actually needed from parsed documents; do not store
  full document images or extraneous personal data not required for the
  stated purpose — Ley 19.628 Art. 3(b).
  (See `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-3`.)

- [ ] Erase or anonymize all raw document data and extracted fields once
  the purpose for which the document was submitted is fulfilled; do not retain
  parsed data in production storage beyond its necessary lifetime —
  Ley 19.628 Art. 14(d).
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14`.)

- [ ] If a third-party AI service (e.g., an OCR or LLM API) processes the
  documents on your behalf, execute a mandatory written data-processing agreement
  specifying subject, duration, purpose, data types, and security obligations
  before sending any document — Ley 19.628 Art. 15 bis.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis`.)

- [ ] Ensure the third-party processor does not sub-process data (e.g., route
  documents to another provider) without your specific written authorisation;
  unauthorized sub-processing makes the processor a controller and creates
  joint liability — Ley 19.628 Art. 15 bis.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis`.)

- [ ] If parsing will operate at large scale or in mass volumes, conduct a
  DPIA before beginning production processing — Ley 19.628 Art. 15 ter(b).
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-ter`.)

- [ ] Implement security measures for documents in transit and at rest: encrypt
  documents during transmission to the parsing service and in any temporary
  storage; maintain access logs — Ley 19.628 Art. 14 quinquies.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quinquies`.)

- [ ] Apply financial-data rules to any financial obligation information extracted
  from bank statements or credit documents: respect the five-year
  communication/retention limit and mandatory erasure rules for prescribed
  obligations — Ley 19.628 Art. 17 and Art. 18.
  (See `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-17`.)
  (See `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md#article-18`.)

- [ ] Publish on the website: that user documents are processed by automated
  means, the purpose, the data types extracted, the retention period, and
  whether any third-party processor is used — Ley 19.628 Art. 14 ter.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter`.)

- [ ] Implement privacy by design: process documents in ephemeral environments
  where feasible; avoid persisting raw document content longer than strictly
  necessary for the parsing task — Ley 19.628 Art. 14 quáter.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quáter`.)

### Watch-outs

- **Purpose limitation applies to extracted fields, not just the document.**
  If you extract 20 fields but only need 5 for the stated purpose, storing the
  other 15 is a purpose-limitation violation even if the original consent
  covered "document processing." (Ley 19.628 Art. 3(b).)

- **Breach affecting financial data requires subject-level notification.** If a
  breach exposes parsed bank statement data, you must notify affected data
  subjects directly, not merely report to the APDP. (Ley 19.628 Art. 14 sexies.)
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-sexies`.)

- **Sub-processing chain liability.** If the third-party AI service uses
  sub-processors (common with US cloud AI providers), each sub-processor
  must be individually authorized in writing; failure makes the primary
  processor a controller with joint liability. (Ley 19.628 Art. 15 bis.)

### Related scenarios

- Scenario 1: identity documents (cédulas) parsed for KYC are governed by
  Scenario 1's ID-storage rules.
- Scenario 5: if the parsed output feeds an AI recommendation engine, add all
  Scenario 5 obligations.
- Scenario 7: if documents are sent to a US or EU cloud AI API for parsing,
  cross-border transfer rules apply before the first document is transmitted.

---

## Scenario 7: Cross-Border Data Transfer (US/EU Cloud Infrastructure)

**Likely fintech scope (Ley 21.521):** Maybe — cross-border data transfer is
not a regulated fintech service, but CMF-regulated services require CMF-compliant
infrastructure and security standards regardless of where servers are located;
confirm with CMF that non-Chilean infrastructure satisfies Art. 22 SFA standards
if the application is SFA-registered.

**Data-protection scope (Ley 19.628):** Yes — any personal data transferred
to a server, cloud region, or third-party service outside Chile is an
international data transfer subject to Ley 19.628 Título V; this applies even
if your legal entity is Chilean.

### Obligations checklist

- [ ] Determine whether the destination country (US or EU member state) has
  received an adequacy determination from the Chilean APDP; if yes, the
  transfer is lawful under the general rule — Ley 19.628 Art. 27 and Art. 28.
  (See `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-27`.)
  (See `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-28`.)

- [ ] If no adequacy determination exists, establish alternative guarantees
  before transferring any personal data: execute standard contractual clauses
  (SCCs) modelled on those published by the APDP, adopt binding corporate
  rules (for intra-group transfers), or use a recognized certification
  mechanism — Ley 19.628 Art. 27 and Art. 28.
  (See `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-27`.)
  (See `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-28`.)

- [ ] For one-off, non-habitual transfers where the above is unavailable,
  obtain explicit data-subject consent or confirm the transfer is necessary
  for contract performance before proceeding — Ley 19.628 Art. 27.
  (See `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-27`.)

- [ ] Retain documentary evidence of the legal basis for every international
  transfer (adequacy decision reference, signed SCCs, or consent record);
  burden of proof lies with the transferring controller in any Agency
  investigation — Ley 19.628 Art. 28.
  (See `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-28`.)

- [ ] Publish on the company website: that data is transferred to third
  countries, whether those countries have adequate protection, and if not,
  what guarantees are in place — Ley 19.628 Art. 14 ter(h).
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-ter`.)

- [ ] Monitor APDP publications for new adequacy determinations and updated
  model contractual clauses; update transfer agreements promptly when the
  APDP issues recommendations or precautionary measures — Ley 19.628 Art. 29.
  (See `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-29`.)

- [ ] Confirm that the APDP has not issued a suspension or restriction on data
  flows to the target country or cloud provider; do not transfer data in
  defiance of an Agency precautionary measure — Ley 19.628 Art. 29.
  (See `corpus/19628-data-protection-consolidated/titulo-05-responsabilidad.md#article-29`.)

- [ ] If your company is not domiciled in Chile but processes data of Chilean
  residents (e.g., a Chilean-facing product hosted in the US), confirm that
  Ley 19.628 applies to you under the targeting/monitoring criterion and
  designate a Chilean contact address — Ley 19.628 Art. 1 bis(c).
  (See `corpus/19628-data-protection-consolidated/titulo-00-preliminar.md#article-1-bis`.)

- [ ] Treat the foreign cloud provider as a data processor: execute a
  written data-processing agreement covering subject, duration, purpose,
  data types, security obligations, and sub-processing restrictions before
  any data leaves Chile — Ley 19.628 Art. 15 bis.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-15-bis`.)

- [ ] Apply security measures in transit: enforce TLS for all data transfers;
  require encryption at rest in the cloud environment; document the security
  standards applied — Ley 19.628 Art. 14 quinquies.
  (See `corpus/19628-data-protection-consolidated/titulo-02-derechos.md#article-14-quinquies`.)

### Watch-outs

- **Using a US cloud provider (AWS, GCP, Azure) is not inherently lawful by
  default.** As of the knowledge cutoff, Chile's APDP has not published a
  comprehensive adequacy list; SCC-equivalent clauses are the practical
  route. (Ley 19.628 Art. 27–28.)

- **Unlawful international transfer is a serious infringement**, not a minor
  one; knowing violation is elevated to very serious. Fines reach 10,000 UTM
  (serious) or 20,000 UTM (very serious). (Ley 19.628 Art. 34 ter and
  Art. 34 quáter.)
  (See `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-34-ter`.)
  (See `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md#article-34-quáter`.)

- **Sub-processors in additional countries trigger separate transfer analyses.**
  If your US cloud provider stores data in multiple AWS regions (e.g., US
  East and EU West), each region is a separate transfer; the DPA must cover
  all processing locations. (Ley 19.628 Art. 15 bis, Art. 27.)

- **CMF-regulated SFA participants must also satisfy CMF security standards**
  for the specific infrastructure used; a data-protection-law-compliant
  transfer does not automatically satisfy CMF Art. 22 security requirements.
  (Ley 21.521 Art. 22.)
  (See `corpus/21521-fintech/titulo-03-finanzas-abiertas.md#article-22`.)

### Related scenarios

- Scenario 1: if RUT/contact data is stored in non-Chilean cloud, this
  scenario's obligations apply in addition to Scenario 1's.
- Scenario 2 and 3: SFA-aggregated bank and investment data transferred offshore
  require both SFA Art. 22 security compliance and Título V transfer authorisation.
- Scenario 6: documents sent to US/EU cloud AI APIs for parsing trigger this
  scenario before the first API call.
