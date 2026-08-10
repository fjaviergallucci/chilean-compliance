"""Generate distribution artifacts for hosts that cannot run the MCP server.

Produces ``dist/``:

- ``knowledge/*.md`` — the corpus merged into at most 20 files, the usual upload
  cap for Custom GPT knowledge and similar hosted assistants.
- ``instructions-gpt.md`` — a projection of ``corpus/_agent-policy.md`` that fits
  an ~8000-character instruction field and is phrased for semantic retrieval
  rather than tool calls.

Everything here is generated. ``dist/`` is committed and CI fails when it drifts
from the corpus, which is what keeps the no-code path from rotting: nobody has to
remember to update a second copy by hand.

Regenerate with::

    python -m tools.build_dist
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
INDEXES = ROOT / "indexes"
POLICY = CORPUS / "_agent-policy.md"
DIST = ROOT / "dist"

GENERATED_MARKER = (
    "<!-- GENERATED — do not edit by hand. Source: corpus/_agent-policy.md + corpus/. "
    "Regenerate: python -m tools.build_dist -->"
)
BANNER_MARKER = "<!-- EFFECTIVE-DATE-DISCIPLINE v1 -->"

# Custom GPT instruction fields cap out around here. Mirrored in the test suite.
INSTRUCTIONS_LIMIT = 8000

# One bundle per corpus directory, plus the indexes. Order is stable so
# regeneration is byte-identical and the staleness diff stays meaningful.
_BUNDLES: list[tuple[str, str]] = [
    ("21521-fintech", "corpus/21521-fintech"),
    ("19628-data-protection", "corpus/19628-data-protection-consolidated"),
    ("21719-amendments-changelog", "corpus/21719-amendments-changelog"),
    ("ncg-502-psf-obligations", "corpus/ncg/502-psf-obligations-consolidated"),
    ("ncg-503-idoneidad", "corpus/ncg/503-idoneidad"),
    ("ncg-514-open-finance", "corpus/ncg/514-open-finance"),
    ("ncg-524-amendments-changelog", "corpus/ncg/524-amendments-changelog"),
    ("ncg-530-fintec-reporting", "corpus/ncg/530-fintec-reporting"),
    ("corpus-meta", None),  # loose corpus/*.md (lexicon, policy)
    ("index-by-topic", "indexes/by-topic.md"),
    ("index-glossary", "indexes/glossary.md"),
    ("index-scenarios", "indexes/scenarios.md"),
    ("index-cross-references", "indexes/cross-references.md"),
]

# Purpose-built single files for people who just want to attach one document to a
# chat. "Upload this folder" is not an instruction a non-technical user can follow
# on GitHub, and nobody needs all 2.2 MB to ask what a specific law requires.
_SINGLE_BUNDLES: list[tuple[str, str, str, list[str]]] = [
    (
        "proteccion-datos",
        "Ley 19.628 — Protección de Datos Personales (Chile)",
        "Ley 19.628 consolidada con la Ley 21.719, listas de verificación de "
        "cumplimiento por tipo de negocio, y glosario de términos legales.",
        [
            "corpus/19628-data-protection-consolidated",
            "indexes/scenarios.md",
            "indexes/glossary.md",
        ],
    ),
    (
        "fintech",
        "Ley 21.521 — Ley Fintec (Chile)",
        "Ley 21.521 completa, listas de verificación de cumplimiento por tipo de "
        "producto, y glosario de términos legales.",
        [
            "corpus/21521-fintech",
            "indexes/scenarios.md",
            "indexes/glossary.md",
        ],
    ),
]


# ---------------------------------------------------------------------------
# Effective-date banner
# ---------------------------------------------------------------------------

def _write(path: Path, text: str) -> None:
    """Write LF-terminated output on every platform.

    .gitattributes pins *.md to eol=lf in the working tree, so emitting the
    platform default would make every local rebuild show dist/ as modified and
    the staleness gate would fight the checkout instead of tracking the corpus.
    """
    path.write_text(text, encoding="utf-8", newline="\n")


def _banner() -> str:
    """Lift the canonical banner block out of the policy file."""
    text = POLICY.read_text(encoding="utf-8")
    start = text.index(BANNER_MARKER)
    lines = text[start:].splitlines()
    out = [lines[0]]
    for line in lines[1:]:
        if line.startswith(">") or not line.strip():
            out.append(line)
            if not line.strip() and len(out) > 2 and not out[-2].startswith(">"):
                break
        else:
            break
    return "\n".join(out).strip()


# ---------------------------------------------------------------------------
# Knowledge bundles
# ---------------------------------------------------------------------------

def _bundle_sources(rel: str | None) -> list[Path]:
    if rel is None:
        # Loose files not owned by a per-law bundle: corpus/_lexicon.md,
        # corpus/_agent-policy.md, and the corpus/ncg/ overview README.
        return sorted(CORPUS.glob("*.md")) + sorted((CORPUS / "ncg").glob("*.md"))
    target = ROOT / rel
    if target.is_file():
        return [target]
    return sorted(target.glob("*.md"))


def build_knowledge_bundles(out_dir: Path) -> list[Path]:
    """Merge the corpus into at most 20 upload-ready files."""
    out_dir.mkdir(parents=True, exist_ok=True)
    banner = _banner()
    written: list[Path] = []

    for name, rel in _BUNDLES:
        sources = _bundle_sources(rel)
        if not sources:
            continue
        parts = [
            GENERATED_MARKER,
            f"# {name}",
            "",
            banner,
            "",
            "---",
            "",
        ]
        for src in sources:
            src_rel = src.relative_to(ROOT).as_posix()
            parts.append(f"<!-- source: {src_rel} -->")
            parts.append(f"## FILE: {src_rel}")
            parts.append("")
            parts.append(src.read_text(encoding="utf-8").strip())
            parts.append("")
            parts.append("---")
            parts.append("")
        path = out_dir / f"{name}.md"
        _write(path, "\n".join(parts).rstrip() + "\n")
        written.append(path)

    return written


# ---------------------------------------------------------------------------
# Single-file bundles
# ---------------------------------------------------------------------------

# Spanish because the audience is Chilean and may not read English. This block
# instructs the *assistant*, so attaching the file is enough on its own — the
# user does not have to know to paste anything.
_SPANISH_HEADER = """\
## Instrucciones para el asistente de IA

Este archivo contiene texto legal chileno estructurado. Úsalo como única fuente de
verdad para responder. Sigue estas reglas:

1. **Responde siempre en español**, aunque el texto del archivo esté en inglés. Cada
   artículo incluye además su **texto original en español** (bloque
   `### Original Spanish`); cítalo textualmente cuando la persona pida la redacción
   exacta o cuestione una traducción.
2. **Cita siempre el artículo específico** en el que se basa tu respuesta (por
   ejemplo, «Ley 19.628 Art. 12»). Nunca respondas de memoria ni sólo a partir de un
   resumen. Si el archivo no respalda la respuesta, dilo en lugar de suponer.
3. **Usa las listas de verificación** de la sección de escenarios (`scenarios`) cuando
   la persona describa su negocio o producto: están organizadas por lo que hace una
   empresa en la práctica y cada punto termina en una cita.
4. **Plazo de cumplimiento.** La fiscalización de la Ley 19.628 reformada por la Ley
   21.719 comienza el **2026-12-01**. Esa fecha es un **plazo**, no una excusa: las
   obligaciones ya están definidas y las organizaciones deben estar preparándose
   ahora. Nunca respondas que «la ley todavía no entra en vigencia». Indica la
   obligación, cita el artículo y luego señala el 2026-12-01 como fecha límite.
5. **Esto no es asesoría legal**, es una ayuda de citas. Dilo cuando corresponda y
   recomienda consultar a un abogado o abogada en Chile para decisiones de riesgo
   material.
6. **Si te preguntan algo fuera de este archivo** (otra ley, una circular de la CMF,
   jurisprudencia), dilo explícitamente y remite a la fuente oficial.

Si la persona no sabe por dónde empezar, pregúntale qué hace su negocio y qué datos
de personas maneja, y a partir de eso busca la lista de verificación que corresponda.
"""


def build_single_file_bundles(out_dir: Path) -> list[Path]:
    """One self-contained file per audience, for attaching to a chat."""
    out_dir.mkdir(parents=True, exist_ok=True)
    banner = _banner()
    written: list[Path] = []

    for name, title, description, rels in _SINGLE_BUNDLES:
        parts = [
            GENERATED_MARKER,
            f"# {title}",
            "",
            description,
            "",
            _SPANISH_HEADER.strip(),
            "",
            "---",
            "",
            banner,
            "",
            "---",
            "",
        ]
        for rel in rels:
            for src in _bundle_sources(rel):
                src_rel = src.relative_to(ROOT).as_posix()
                parts.append(f"<!-- incluye: {src_rel} -->")
                parts.append(f"## FUENTE: {src_rel}")
                parts.append("")
                parts.append(src.read_text(encoding="utf-8").strip())
                parts.append("")
                parts.append("---")
                parts.append("")
        path = out_dir / f"{name}.md"
        _write(path, "\n".join(parts).rstrip() + "\n")
        written.append(path)

    return written


# ---------------------------------------------------------------------------
# Instruction projection
# ---------------------------------------------------------------------------

_SECTION_RE = re.compile(r"^(#{1,2})\s+(.*)$")

# Sections carried through verbatim. "Corpus layout" is dropped: file paths mean
# nothing to a host whose retrieval is opaque. "Scope" is compacted below.
_VERBATIM_OPERATIONS = (
    "Operation: LOCATE",
    "Operation: RETRIEVE",
    "Operation: DEFINE",
    "Operation: SCENARIO",
    "Operation: TRAVERSE",
    "Operation: ORIGINAL",
)

_VERBATIM_TRAILING = (
    "Citation format",
    "Caveat surfacing",
)

_PREAMBLE = """\
You answer questions on Chilean financial-services and personal-data regulation from
the corpus in your knowledge files. It is **not legal advice** — it is a citation aid.

**Every answer cites a specific article.** Search your knowledge for the article text
and quote it; never answer from memory or from a summary bullet alone. If the corpus
does not support an answer, say so rather than inferring.

Knowledge files are named by law or regulation (`21521-fintech`, `ncg-502-psf-obligations`,
…) plus four indexes (`index-by-topic`, `index-glossary`, `index-scenarios`,
`index-cross-references`). Search an index for citations, then search the matching
corpus file for the full article before answering.
"""

_SCOPE = """\
## Scope

- **Ley 21.521 (Fintec)** — in force since 2023-02-03.
- **Ley 19.628 (Data Protection)**, consolidated with Ley 21.719 — see the rule above.
- **NCG 502** (with NCG 524) — Ley 21.521 Título II: registration, authorization,
  disclosure, governance and risk, capital.
- **NCG 514** — Open Finance / SFA: perimeter, registration, APIs, consent (§III.D),
  data sets, security (§IV.D).
- **NCG 503** — personnel accreditation (idoneidad); derogates NCG 412.
- **NCG 530** — MSI Fintec reporting: FINTEC01–16 list and instructions.

Laws define *what* must be done; NCGs define *how* to comply. Operational questions
("what must we file, build, report?") are answered from the NCG layer.

**Out of scope:** NCG 454 / 504 / 461; NCG 530 record layouts (Anexo N°2/N°3); CMF
circulars and APDP guidance not in the corpus; case law; Título V of Ley 21.521.
Say so explicitly rather than inferring.
"""


def _policy_sections() -> dict[str, str]:
    sections: dict[str, str] = {}
    current: str | None = None
    buffer: list[str] = []
    for line in POLICY.read_text(encoding="utf-8").splitlines():
        if m := _SECTION_RE.match(line):
            if current:
                sections[current] = "\n".join(buffer).strip()
            current = m.group(2).strip()
            buffer = [line]
        elif current:
            buffer.append(line)
    if current:
        sections[current] = "\n".join(buffer).strip()
    return sections


def build_gpt_instructions() -> str:
    """Project the policy into an instruction field for a hosted assistant.

    Deliberately a projection, not a summary: the effective-date rule, citation
    format and gap-honesty sections are carried verbatim so the legal guidance
    cannot drift. Only the host-specific parts are rewritten.
    """
    sections = _policy_sections()
    parts = [
        "<!-- GENERATED from corpus/_agent-policy.md — do not edit by hand. -->",
        "",
        _PREAMBLE.strip(),
        "",
        _banner(),
        "",
        _SCOPE.strip(),
        "",
        "## How to answer",
        "",
        "Seven operations cover every question. Perform each by searching your knowledge.",
        "",
    ]
    for name in _VERBATIM_OPERATIONS:
        if body := sections.get(name):
            parts.append(body)
            parts.append("")

    # STATUS and gap-honesty are projected rather than carried: the policy versions
    # cite repository paths this host cannot open, and their scope bullets duplicate
    # the Scope section above. The substance — refuse rather than infer, not legal
    # advice — is preserved.
    parts.append(
        "## Operation: STATUS\n\n"
        "Every corpus in your knowledge is complete and stable as of v1.3.0. If asked "
        "about coverage, state what is in scope above and what is not."
    )
    parts.append("")

    for name in _VERBATIM_TRAILING:
        if body := sections.get(name):
            parts.append(body)
            parts.append("")

    parts.append(
        "## Honesty about gaps\n\n"
        "- Not legal advice; a citation aid. Say so when asked, and recommend Chilean "
        "counsel for decisions carrying material risk.\n"
        "- If an answer depends on anything outside the corpus — a CMF circular, an APDP "
        "fine, a court ruling, sector-specific rules, another statute such as Ley 18.045 "
        "or 18.046 — say so explicitly and point to the official source. Never infer.\n"
        "- Título V of Ley 21.521 (amendments to other statutes) is out of scope; the "
        "corpus carries only an out-of-scope note for it."
    )
    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Build + staleness
# ---------------------------------------------------------------------------

def build_all(out_dir: Path) -> list[Path]:
    knowledge = out_dir / "knowledge"
    if knowledge.exists():
        shutil.rmtree(knowledge)
    written = build_knowledge_bundles(knowledge)

    single = out_dir / "single"
    if single.exists():
        shutil.rmtree(single)
    written += build_single_file_bundles(single)

    out_dir.mkdir(parents=True, exist_ok=True)
    instructions = out_dir / "instructions-gpt.md"
    _write(instructions, build_gpt_instructions())
    written.append(instructions)
    return written


def diff_against(committed: Path, scratch: Path) -> list[str]:
    """Return the relative paths that differ between committed and freshly built."""
    fresh_dir = scratch / "dist"
    build_all(fresh_dir)

    def snapshot(root: Path) -> dict[str, str]:
        if not root.exists():
            return {}
        return {
            p.relative_to(root).as_posix(): p.read_text(encoding="utf-8")
            for p in sorted(root.rglob("*.md"))
        }

    have, want = snapshot(committed), snapshot(fresh_dir)
    drift = [rel for rel in sorted(set(have) | set(want)) if have.get(rel) != want.get(rel)]
    return drift


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero if dist/ differs from a fresh build instead of writing",
    )
    args = parser.parse_args()

    if args.check:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            drift = diff_against(DIST, Path(tmp))
        if drift:
            print("STALE: dist/ differs from the corpus:")
            for rel in drift:
                print(f"  - {rel}")
            print("\nRun `python -m tools.build_dist` and commit the result.")
            return 1
        print("OK: dist/ is current")
        return 0

    written = build_all(DIST)
    size = len((DIST / "instructions-gpt.md").read_text(encoding="utf-8"))
    for path in sorted((DIST / "single").glob("*.md")):
        print(f"    single/{path.name}: {path.stat().st_size / 1024:,.0f} KB")
    print(f"OK: wrote {len(written) - 1} bundles + instructions")
    print(f"    instructions: {size:,} chars ({INSTRUCTIONS_LIMIT - size:,} under the limit)")
    if size > INSTRUCTIONS_LIMIT * 0.95:
        print("    WARNING: within 5% of the instruction-field limit — trim before adding more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
