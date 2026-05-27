<!--
Thanks for contributing to chile-compliance.

Please make sure you have read CONTRIBUTING.md and that your change follows
the project's conventions. The maintainer reviews PRs against this checklist.
-->

## Summary

<!-- One paragraph: what does this PR change and why? -->

## Type of change

- [ ] Translation fix or improvement (existing article)
- [ ] New article translated (resolves `<!-- REVIEW: -->` markers)
- [ ] New scenario added to `indexes/scenarios.md`
- [ ] Glossary update
- [ ] New source added (law, amendment, circular)
- [ ] Tooling change
- [ ] Documentation only
- [ ] Other (please describe)

## Affected files

<!-- Bullet list of files touched. -->

## Translation accuracy (if applicable)

- [ ] I followed `corpus/_lexicon.md` conventions.
- [ ] Defined terms include the Spanish in parens on first use per file.
- [ ] Obligation verbs follow the lexicon (deberá → must, podrá → may, etc.).
- [ ] Numbering is preserved exactly.
- [ ] Verbatim Spanish blocks are unchanged from the source PDF.
- [ ] Non-literal renderings are explained via `> **TN:** ...` notes.

## Quality gates run locally

Paste the output (or just confirm each passes):

- [ ] `python -m pytest tools/tests/ -v`
- [ ] `python -m tools.check_extraction_parity sources/Ley-21521_04-ENE-2023-1.pdf corpus/21521-fintech --exclude-titulo V`
- [ ] `python -m tools.check_extraction_parity sources/LEY-19628_28-AGO-1999.pdf corpus/19628-data-protection-consolidated --exclude-titulo Transitorio`
- [ ] `python -m tools.check_roundtrip sources/Ley-21521_04-ENE-2023-1.pdf corpus/21521-fintech --sample 0`
- [ ] `python -m tools.check_roundtrip sources/LEY-19628_28-AGO-1999.pdf corpus/19628-data-protection-consolidated --sample 0`
- [ ] `python -m tools.check_glossary_completeness indexes/glossary.md corpus/21521-fintech`
- [ ] `python -m tools.check_glossary_completeness indexes/glossary.md corpus/19628-data-protection-consolidated`

## Related issues

<!-- Link any issue this PR resolves: `Closes #N`. -->

## Notes for the reviewer

<!-- Optional: anything specific you want feedback on, or tradeoffs you considered. -->
