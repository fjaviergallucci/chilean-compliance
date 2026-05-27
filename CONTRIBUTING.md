# Contributing to chile-compliance

Thanks for considering a contribution. This corpus is meant to be community-improvable — translations, scenarios, new amendments, and tooling fixes are all welcome.

## Where to start

The single highest-impact contribution right now is finishing the literal translations of **Ley 19.628 consolidated, Títulos VI–VIII** (Arts. 30–55: APDP regulator, sanctions, constitutional bodies). The Spanish text is verbatim in each article block; the English currently contains structured summaries with `<!-- REVIEW: ... -->` markers.

Priority order based on consuming-AI impact:

| Priority | File | REVIEW markers | Why |
|---|---|---:|---|
| 1 | `corpus/19628-data-protection-consolidated/titulo-07-sanciones.md` | 24 | Sanctions / fines / procedures — every compliance answer involving risk needs literal text here |
| 2 | `corpus/19628-data-protection-consolidated/titulo-06-agencia.md` | 12 | APDP powers — drives who-can-do-what answers |
| 3 | `corpus/19628-data-protection-consolidated/titulo-03-datos-financieros.md` | 3 | Pre-21.719 amendment notes |
| 4 | `corpus/19628-data-protection-consolidated/titulo-08-organos-constitucionales.md` | 2 | Narrow applicability |

To upgrade an article:

1. Open the file and find an article with `<!-- REVIEW: ... -->`.
2. Replace the English summary with a literal lexicon-conforming translation. Keep the verbatim Spanish unchanged.
3. Remove the REVIEW marker.
4. Add a `> **TN:** ...` note immediately after any phrase you rendered non-literally, explaining why.
5. Run the quality gates (below).
6. Open a PR.

## Translation conventions

- **Lexicon** (`corpus/_lexicon.md`) is authoritative. Pull from it unless context demands otherwise.
- **Defined terms** include the Spanish in parens on first use per file: `data subject (titular)`.
- **Obligation verbs** are rigorous: *deberá* → must, *podrá* → may, *no podrá* → shall not, *quedará obligado* → shall be obligated.
- **Numbering preserved exactly**: `Art. 2 lit. g) número 3` becomes `Art. 2(g)(3)` consistently.
- **Original Spanish is verbatim** — never edit the Spanish block to "fix" a typo in the source PDF; if the source has `como como`, the Spanish block has `como como`. The English can render it correctly without the duplication.
- **Translator's notes** (`> **TN:** ...`) explain non-literal choices. **REVIEW markers** (`<!-- REVIEW: <reason> -->`) flag passages awaiting human attention.

## Adding a new scenario

`indexes/scenarios.md` is a compliance checklist by use case. To add one:

1. Identify the feature concretely (e.g., "consumer credit scoring with ML").
2. Determine fintech scope (Ley 21.521 Art. 2) and data-protection scope (always yes if processing personal data).
3. Add a `## Scenario N: <feature>` block following the existing template.
4. Every checklist item must end with an article citation (`Ley 19.628 Art. 12`) AND a `(See corpus/...md#article-N)` link.
5. Run the citation-resolution check (below).

## Adding new amendments, circulars, or laws

When the APDP issues guidance, when CMF publishes a circular, or when a new amendment passes:

1. Drop the source PDF in `sources/`.
2. Add a new section under `corpus/` (e.g., `corpus/apdp-circular-001/`). Don't intermix with existing law files.
3. Update `plugin.json` to add the new section to `corpus_status`.
4. Update `SKILL.md`'s "What this skill covers" section.
5. Update the README status table.

For adding a new statute entirely (e.g., Ley 18.045):

1. Create `corpus/<law-num>-<slug>/` with the same per-Título file structure.
2. Add the source PDF to `sources/`.
3. Run `python tools/extract_articles.py sources/<pdf>` to get an article inventory.
4. Translate each Título following the same conventions.
5. Add the law to `plugin.json` `corpus_status`.

The tooling is law-agnostic — the same scripts work on any Chilean BCN PDF that follows standard `Artículo N.-` and `TÍTULO N` structure.

## Quality gates

Before opening a PR, all of the following must succeed:

```bash
python -m pytest tools/tests/ -v
python -m tools.check_extraction_parity sources/Ley-21521_04-ENE-2023-1.pdf corpus/21521-fintech --exclude-titulo V
python -m tools.check_extraction_parity sources/LEY-19628_28-AGO-1999.pdf corpus/19628-data-protection-consolidated --exclude-titulo Transitorio
python -m tools.check_roundtrip sources/Ley-21521_04-ENE-2023-1.pdf corpus/21521-fintech --sample 0
python -m tools.check_roundtrip sources/LEY-19628_28-AGO-1999.pdf corpus/19628-data-protection-consolidated --sample 0
python -m tools.check_glossary_completeness indexes/glossary.md corpus/21521-fintech
python -m tools.check_glossary_completeness indexes/glossary.md corpus/19628-data-protection-consolidated
```

CI runs these on every PR. Tests must be green to merge.

## Development setup

```bash
git clone https://github.com/fjaviergallucci/chilean-compliance.git
cd chilean-compliance
python -m pip install -r tools/requirements.txt
python -m pytest tools/tests/ -v
```

Python 3.11+ required.

## Pull request conventions

- **Commit messages** use conventional commits: `feat:`, `fix:`, `docs:`, `chore:`, `test:`. Optional scope in parens (`feat(21521): ...`, `fix(tools): ...`).
- **One logical change per PR.** A translation fix to one Título is one PR; a new scenario is another; tooling changes are separate.
- **PR description** must list which quality gates you ran locally and their results.
- **CI must pass** before maintainer review.

## Translation accuracy disputes

Legal translation involves judgment. If you think an existing translation is wrong:

1. Open an issue using the **Translation fix** template; cite the affected article and quote both the current English and the Spanish.
2. Explain your proposed rendering and why. Reference the lexicon or relevant Chilean legal-drafting conventions.
3. The maintainer (and any subject-matter expert reviewers) discusses.
4. If accepted, open a PR with the fix and a `> **TN:** ...` note in the corpus explaining the rationale.

## Not legal advice

Everyone contributing to this corpus must understand: this is a structured citation aid for AI agents, not legal advice. Contributions must not represent personal legal opinions as authoritative statements of Chilean law. When in doubt, cite an article and let the user / consuming AI draw the conclusion.

## License

By contributing, you agree your contributions are licensed under the project's [MIT License](LICENSE).
