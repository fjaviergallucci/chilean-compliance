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
