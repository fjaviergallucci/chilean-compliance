# Lexicon — Spanish to English

Hand-maintained mapping of critical legal terms used by the corpus and the
build pipeline. When translating, pick the English on the right unless a
better contextual rendering is needed — and in that case, add a `> **TN:**`
note in the article.

## Obligation verbs
| Spanish | English |
|---|---|
| deberá / deberán | must |
| podrá / podrán | may |
| no podrá | shall not |
| quedará obligado | shall be obligated |
| corresponderá | it shall be the responsibility of |
| será obligatorio | shall be mandatory |
| tendrá derecho a | shall have the right to |

## Parties and roles
| Spanish | English |
|---|---|
| titular | data subject |
| responsable de datos | data controller |
| mandatario / encargado | data processor |
| Comisión (para el Mercado Financiero) | Commission (CMF) |
| Agencia (de Protección de Datos Personales) | Agency (APDP) |
| persona natural | natural person |
| persona jurídica | legal person |

## Data terms
| Spanish | English |
|---|---|
| datos personales | personal data |
| datos personales sensibles | sensitive personal data |
| tratamiento (de datos) | processing (of data) |
| anonimización | anonymization |
| seudonimización | pseudonymization |
| almacenamiento | storage |
| comunicación de datos | data communication / disclosure |
| transferencia internacional | international transfer |
| base de datos | database |
| fuentes de acceso público | publicly accessible sources |
| perfilamiento | profiling |
| decisión automatizada | automated decision |

## Fintech terms
| Spanish | English |
|---|---|
| asesoría crediticia | credit advisory |
| asesoría de inversión | investment advisory |
| custodia de instrumentos financieros | custody of financial instruments |
| enrutamiento de órdenes | order routing |
| intermediación de instrumentos financieros | intermediation of financial instruments |
| plataforma de financiamiento colectivo | crowdfunding platform |
| sistema alternativo de transacción | alternative trading system |
| activos financieros virtuales | virtual financial assets |
| instrumento financiero | financial instrument |
| Registro de Prestadores de Servicios Financieros | Registry of Financial-Service Providers |

## Procedural / scope terms
| Spanish | English |
|---|---|
| ámbito de aplicación | scope of application |
| tener por objeto | is intended to |
| principios | principles |
| fiscalización | supervision |
| normativa de carácter general | general regulation (CMF rulemaking) |
| inscripción | registration |
| ley | law |
| reglamento | regulation |
| disposición | provision |
| artículo (Art.) | Article (Art.) |
| título | Title |
| literal | subparagraph |
| inciso | paragraph |

## Rendering rules
1. Defined terms keep the Spanish in parentheses on first use per file: `data subject (titular)`.
2. When an obligation verb is genuinely ambiguous (e.g., context could read either as `must` or `shall`), default to `must` and add a `> **TN:**` note.
3. When a term in this lexicon does not fit a particular passage, prefer this lexicon and explain via `> **TN:**` rather than silently substituting.
