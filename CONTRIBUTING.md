# Contributing to chile-compliance

Thanks for considering a contribution. This corpus is meant to be community-improvable — translations, scenarios, new amendments, and tooling fixes are all welcome.

## Where to start

As of v1.0.0, every article in the corpus carries a literal lexicon-conformant translation. The most useful contributions now are:

- **Translation corrections.** If you find an English rendering that doesn't track the Spanish, open an issue (`Translation fix or improvement` template) or send a PR with the change plus a `> **TN:** ...` note explaining the rationale.
- **New scenarios** in `indexes/scenarios.md` covering use cases that aren't yet on the list.
- **CMF circulars and APDP guidance** as they are published. These are out of scope today but are valuable additions when issued.
- **All in-scope CMF NCGs are now in the corpus** (NCG 502 consolidated with 524; NCG 514 Open Finance; NCG 503 idoneidad; NCG 530 Fintec reporting). Future NCG/circular additions (e.g. NCG 515, APDP guidance) and coverage of other fintech-adjacent statutes (Leyes 18.045, 18.046, 18.840) are welcome.

To propose any of the above, open an issue using the matching `.github/ISSUE_TEMPLATE/` so the discussion has the right shape, then send a PR.

### Translation fix workflow (when applicable)

1. Open the affected file and locate the article.
2. Update the English text to track the Spanish more precisely.
3. Add a `> **TN:** ...` note immediately after any phrase you rendered non-literally, explaining why.
4. Keep the `### Original Spanish` block unchanged.
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
3. Update `.claude-plugin/plugin.json` to add the new section to `corpus_status`.
4. Update `SKILL.md`'s "What this skill covers" section.
5. Update the README status table.

For adding a new statute entirely (e.g., Ley 18.045):

1. Create `corpus/<law-num>-<slug>/` with the same per-Título file structure.
2. Add the source PDF to `sources/`.
3. Run `python tools/extract_articles.py sources/<pdf>` to get an article inventory.
4. Translate each Título following the same conventions.
5. Add the law to `.claude-plugin/plugin.json` `corpus_status`.

The tooling is law-agnostic — the same scripts work on any Chilean BCN PDF that follows standard `Artículo N.-` and `TÍTULO N` structure. NCG-format (hierarchical ToC) regulations use `extract_ncg_sections.py` + `check_ncg_parity.py` instead; follow the NCG 502 corpus as the pattern.

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
python -m tools.check_ncg_parity corpus/ncg/502-psf-obligations-consolidated/_toc.json corpus/ncg/502-psf-obligations-consolidated
python -m tools.check_roundtrip "sources/NCG 502.pdf" corpus/ncg/502-psf-obligations-consolidated --mode ncg --also-pdf sources/ncg_524_2024.pdf --threshold 0.70 --exclude I.A --exclude I.C.2 --exclude II.A --exclude II.F --exclude III.C --exclude IV.C.6 --exclude IV.D.4 --exclude VIII --exclude Anexo
python -m tools.check_ncg_parity corpus/ncg/503-idoneidad/_toc.json corpus/ncg/503-idoneidad
python -m tools.check_roundtrip sources/ncg_503_2024.pdf corpus/ncg/503-idoneidad --mode ncg --threshold 0.80
python -m tools.check_ncg_parity corpus/ncg/530-fintec-reporting/_toc.json corpus/ncg/530-fintec-reporting
python -m tools.check_roundtrip sources/ncg_530_2025-2.pdf corpus/ncg/530-fintec-reporting --mode ncg --threshold 0.80
```

Note: the NCG round-trip runs at threshold 0.80 due to one known pdfplumber page-break artifact; the law round-trips above use the default threshold.

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
