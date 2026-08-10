"""Resolver over the Chilean compliance corpus.

Implements the seven operations defined in ``corpus/_agent-policy.md`` against
the markdown corpus and the four indexes. No database and no third-party
dependency: the indexes are already rigidly structured, so everything is parsed
into memory on first use and cached.

The MCP server in ``tools/mcp/`` is a thin binding over this module. Keeping the
SDK out of here means the corpus verification suite never depends on it.
"""
from __future__ import annotations

import functools
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
INDEXES = ROOT / "indexes"
PLUGIN_JSON = ROOT / ".claude-plugin/plugin.json"


class CorpusError(Exception):
    """Base class for resolver failures."""


class CitationError(CorpusError):
    """The citation string could not be parsed."""


class NotFoundError(CorpusError):
    """The citation parsed but nothing in the corpus matches it."""


# ---------------------------------------------------------------------------
# Citations
# ---------------------------------------------------------------------------

# Ordinal suffixes Chilean drafting appends to article numbers.
ORDINALS = ("bis", "ter", "quater", "quáter", "quinquies", "sexies", "septies")

_LAW_RE = re.compile(
    r"^(?:Ley\s+)?(?P<body>\d{2}\.\d{3})\s+Art\.?\s*"
    r"(?P<num>\d+)\s*(?P<ord>" + "|".join(ORDINALS) + r")?"
    r"(?:\s*\(\s*(?P<sub>[^)]+?)\s*\))?\s*$",
    re.IGNORECASE,
)

_NCG_RE = re.compile(
    r"^NCG\s+(?P<body>\d{3})\s*(?:§|Sec(?:ci[oó]n)?\.?\s*)\s*(?P<anchor>[A-Za-z0-9.]+?)\s*$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Citation:
    kind: str  # "law" | "ncg"
    body: str  # "19.628" | "502"
    anchor: str  # "8 bis" | "IV.C.3.1"
    sub: str | None = None

    def __str__(self) -> str:
        if self.kind == "law":
            base = f"{self.body} Art. {self.anchor}"
            return f"{base}({self.sub})" if self.sub else base
        return f"NCG {self.body} §{self.anchor}"


def parse_citation(raw: str) -> Citation:
    """Parse a citation string into its parts.

    Accepts both spacings of ordinal suffixes: the adjacency list writes
    ``Art.8bis`` while headings write ``Article 8 bis``. Both normalise to
    ``8 bis``.
    """
    text = " ".join(str(raw).split())
    if m := _LAW_RE.match(text):
        anchor = m.group("num")
        if suffix := m.group("ord"):
            anchor = f"{anchor} {suffix.lower()}"
        return Citation("law", m.group("body"), anchor, m.group("sub"))
    if m := _NCG_RE.match(text):
        return Citation("ncg", m.group("body"), m.group("anchor").upper())
    raise CitationError(f"unrecognised citation: {raw!r}")


def _normalise_anchor(anchor: str) -> str:
    """Collapse spacing so ``8bis``, ``8 bis`` and ``8  BIS`` compare equal."""
    return re.sub(r"\s+", "", anchor).lower()


# ---------------------------------------------------------------------------
# Article blocks
# ---------------------------------------------------------------------------

@dataclass
class Article:
    citation: str
    title: str
    english: str
    spanish: str
    cross_refs: list[str] = field(default_factory=list)
    source_footer: str | None = None
    tn_notes: list[str] = field(default_factory=list)
    path: str = ""


_HEADING_RE = re.compile(r"^##\s+(?:Article\s+)?(?P<anchor>[^—]+?)\s+—\s+(?P<title>.+?)\s*$")

# Which corpus directories hold which law/NCG body.
_LAW_DIRS = {
    "19.628": "19628-data-protection-consolidated",
    "21.521": "21521-fintech",
}
_NCG_DIRS = {
    "502": "ncg/502-psf-obligations-consolidated",
    "503": "ncg/503-idoneidad",
    "514": "ncg/514-open-finance",
    "530": "ncg/530-fintec-reporting",
}


def _corpus_dir(c: Citation) -> Path:
    table = _LAW_DIRS if c.kind == "law" else _NCG_DIRS
    if c.body not in table:
        raise NotFoundError(f"no corpus directory for {c.body!r}")
    return CORPUS / table[c.body]


@functools.lru_cache(maxsize=None)
def _block_index(directory: Path) -> dict[str, tuple[Path, int, int]]:
    """Map normalised anchor -> (file, start line, end line) for one corpus dir.

    Blocks run from their ``## `` heading to the next ``## `` heading or EOF.
    """
    index: dict[str, tuple[Path, int, int]] = {}
    for path in sorted(directory.glob("*.md")):
        if path.name.startswith("_") or path.name == "README.md":
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        starts: list[tuple[int, str]] = []
        for i, line in enumerate(lines):
            if m := _HEADING_RE.match(line):
                starts.append((i, _normalise_anchor(m.group("anchor"))))
        for pos, (start, anchor) in enumerate(starts):
            end = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
            index.setdefault(anchor, (path, start, end))
    return index


def _strip_blockquote(lines: list[str]) -> str:
    out = []
    for line in lines:
        stripped = line.lstrip()
        out.append(stripped[1:].lstrip() if stripped.startswith(">") else line)
    return "\n".join(out).strip()


def get_article(c: Citation) -> Article:
    """RETRIEVE — the full article or section block for a citation."""
    index = _block_index(_corpus_dir(c))
    key = _normalise_anchor(c.anchor)
    if key not in index:
        raise NotFoundError(f"{c} not present in {_corpus_dir(c).name}")
    path, start, end = index[key]
    lines = path.read_text(encoding="utf-8").splitlines()[start:end]

    title = ""
    if m := _HEADING_RE.match(lines[0]):
        title = m.group("title")

    sections: dict[str, list[str]] = {}
    current: str | None = None
    source_footer: str | None = None
    tn_notes: list[str] = []

    for line in lines[1:]:
        if line.startswith("### "):
            current = line[4:].strip().lower()
            sections[current] = []
            continue
        if line.startswith("> **Source:**"):
            source_footer = line.split("**Source:**", 1)[1].strip()
            continue
        if line.startswith("> **TN:**"):
            tn_notes.append(line.split("**TN:**", 1)[1].strip())
            continue
        if current:
            sections[current].append(line)

    english = "\n".join(sections.get("plain-english text", [])).strip()
    spanish = _strip_blockquote(sections.get("original spanish", []))
    cross = [
        ln.lstrip("- ").strip()
        for ln in sections.get("cross-references", [])
        if ln.strip().startswith("-")
    ]

    return Article(
        citation=str(c),
        title=title,
        english=english,
        spanish=spanish,
        cross_refs=cross,
        source_footer=source_footer,
        tn_notes=tn_notes,
        path=path.relative_to(ROOT).as_posix(),
    )


# ---------------------------------------------------------------------------
# TRAVERSE
# ---------------------------------------------------------------------------

_EDGE_RE = re.compile(
    r"^(?P<src_body>[\d.]+|NCG\d+):Art\.(?P<src>\S+)\s*->\s*"
    r"(?P<dst_body>[\d.]+|NCG\d+):Art\.(?P<dst>\S+)\s*\((?P<reason>[^)]*)\)"
)


@functools.lru_cache(maxsize=1)
def _edges() -> dict[tuple[str, str], list[tuple[str, str]]]:
    graph: dict[tuple[str, str], list[tuple[str, str]]] = {}
    text = (INDEXES / "cross-references.md").read_text(encoding="utf-8")
    for line in text.splitlines():
        if not (m := _EDGE_RE.match(line.strip())):
            continue
        src = (m.group("src_body"), _normalise_anchor(m.group("src")))
        target = _format_edge_target(m.group("dst_body"), m.group("dst"))
        graph.setdefault(src, []).append((target, m.group("reason")))
    return graph


def _format_edge_target(body: str, anchor: str) -> str:
    """Render an adjacency-list endpoint back into citation form."""
    spaced = anchor
    for ordinal in ORDINALS:
        if anchor.lower().endswith(ordinal) and len(anchor) > len(ordinal):
            spaced = f"{anchor[: -len(ordinal)]} {ordinal}"
            break
    if body.upper().startswith("NCG"):
        return f"NCG {body[3:]} §{spaced}"
    return f"{body} Art. {spaced}"


def get_cross_references(c: Citation) -> list[tuple[str, str]]:
    """TRAVERSE — outbound edges as ``(target citation, reason)``."""
    body = c.body if c.kind == "law" else f"NCG{c.body}"
    return list(_edges().get((body, _normalise_anchor(c.anchor)), []))


# ---------------------------------------------------------------------------
# DEFINE
# ---------------------------------------------------------------------------

@dataclass
class Definition:
    term: str
    spanish_term: str
    defined_in: str
    english: str
    spanish: str


_GLOSSARY_HEADING_RE = re.compile(r"^##\s+(?P<term>[^(]+?)\s*(?:\((?P<es>[^)]+)\))?\s*$")


@functools.lru_cache(maxsize=1)
def _glossary() -> dict[str, Definition]:
    entries: dict[str, Definition] = {}
    lines = (INDEXES / "glossary.md").read_text(encoding="utf-8").splitlines()
    starts = [i for i, ln in enumerate(lines) if ln.startswith("## ")]
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        m = _GLOSSARY_HEADING_RE.match(lines[start])
        if not m:
            continue
        term = m.group("term").strip()
        block = lines[start + 1 : end]
        defined_in = ""
        english_parts: list[str] = []
        spanish_parts: list[str] = []
        in_spanish = False
        for line in block:
            if line.startswith("**Defined in:**"):
                defined_in = line.split("**Defined in:**", 1)[1].strip()
                continue
            if line.startswith("**Spanish original:**"):
                in_spanish = True
                continue
            (spanish_parts if in_spanish else english_parts).append(line)
        entries[term.lower()] = Definition(
            term=term,
            spanish_term=(m.group("es") or "").strip(),
            defined_in=defined_in,
            english="\n".join(english_parts).strip(),
            spanish=_strip_blockquote(spanish_parts),
        )
    return entries


def get_definition(term: str) -> Definition:
    """DEFINE — glossary entry for a term."""
    key = term.strip().lower()
    glossary = _glossary()
    if key in glossary:
        return glossary[key]
    for name, entry in glossary.items():
        if key in name or key == entry.spanish_term.lower():
            return entry
    raise NotFoundError(f"no glossary entry for {term!r}")


# ---------------------------------------------------------------------------
# LOCATE
# ---------------------------------------------------------------------------

@dataclass
class TopicHit:
    topic: str
    bullet: str
    citations: list[str]


_CITATION_IN_TEXT_RE = re.compile(
    r"(?:Ley\s+)?(\d{2}\.\d{3})\s+Art\.\s*(\d+(?:\s+(?:" + "|".join(ORDINALS) + r"))?)"
    r"|NCG\s+(\d{3})\s*§\s*([A-Z0-9.]+)",
    re.IGNORECASE,
)


def _citations_in(text: str) -> list[str]:
    found: list[str] = []
    for m in _CITATION_IN_TEXT_RE.finditer(text):
        if m.group(1):
            found.append(f"{m.group(1)} Art. {' '.join(m.group(2).split())}")
        else:
            found.append(f"NCG {m.group(3)} §{m.group(4)}")
    return list(dict.fromkeys(found))


@functools.lru_cache(maxsize=1)
def _topic_bullets() -> list[tuple[str, str]]:
    """Group by-topic.md into ``(topic, bullet block)`` pairs.

    A bullet is a top-level ``- `` line plus its indented children, because the
    keyword usually sits on the parent line while the citations sit on the
    children. Matching per-line would drop the citations.
    """
    bullets: list[tuple[str, str]] = []
    topic = ""
    buffer: list[str] = []

    def flush() -> None:
        if buffer:
            bullets.append((topic, "\n".join(buffer).strip()))
            buffer.clear()

    for line in (INDEXES / "by-topic.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## Topic:"):
            flush()
            topic = line.split("## Topic:", 1)[1].strip()
            continue
        if line.startswith("- "):
            flush()
            buffer.append(line)
        elif buffer and (line.startswith((" ", "\t")) or not line.strip()):
            buffer.append(line)
        else:
            flush()
    flush()
    return bullets


def search_topics(query: str) -> list[TopicHit]:
    """LOCATE — topical bullets matching a keyword, with their citations."""
    needle = query.strip().lower()
    if not needle:
        return []
    hits: list[TopicHit] = []
    for topic, block in _topic_bullets():
        if needle not in block.lower():
            continue
        headline = block.splitlines()[0].strip().lstrip("- ").strip()
        hits.append(TopicHit(topic=topic, bullet=headline, citations=_citations_in(block)))
    return hits


# ---------------------------------------------------------------------------
# SCENARIO
# ---------------------------------------------------------------------------

@dataclass
class Scenario:
    number: int
    title: str
    fintech_scope: str
    data_scope: str
    items: list[str]


_SCENARIO_RE = re.compile(r"^##\s+Scenario\s+(?P<num>\d+):\s*(?P<title>.+?)\s*$")


@functools.lru_cache(maxsize=1)
def _scenarios() -> list[Scenario]:
    lines = (INDEXES / "scenarios.md").read_text(encoding="utf-8").splitlines()
    starts = [(i, m) for i, ln in enumerate(lines) if (m := _SCENARIO_RE.match(ln))]
    out: list[Scenario] = []
    for pos, (start, m) in enumerate(starts):
        end = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        block = lines[start + 1 : end]
        joined = "\n".join(block)
        fintech = _labelled(joined, "Likely fintech scope")
        data = _labelled(joined, "Data-protection scope")
        items = [ln.strip()[6:].strip() for ln in block if ln.strip().startswith("- [ ]")]
        out.append(
            Scenario(
                number=int(m.group("num")),
                title=m.group("title"),
                fintech_scope=fintech,
                data_scope=data,
                items=items,
            )
        )
    return out


def _labelled(text: str, label: str) -> str:
    for line in text.splitlines():
        if line.startswith(f"**{label}"):
            return line.split(":**", 1)[-1].strip() if ":**" in line else line.strip()
    return ""


def get_scenario(query: str) -> Scenario:
    """SCENARIO — the checklist whose title or body best matches a feature."""
    needle = query.strip().lower()
    scenarios = _scenarios()
    if needle.isdigit():
        for s in scenarios:
            if s.number == int(needle):
                return s
        raise NotFoundError(f"no scenario numbered {needle}")
    for s in scenarios:
        if needle in s.title.lower():
            return s
    best: tuple[int, Scenario] | None = None
    for s in scenarios:
        haystack = (s.title + " " + " ".join(s.items)).lower()
        score = sum(1 for word in needle.split() if word in haystack)
        if score and (best is None or score > best[0]):
            best = (score, s)
    if best:
        return best[1]
    raise NotFoundError(f"no scenario matches {query!r}")


# ---------------------------------------------------------------------------
# STATUS
# ---------------------------------------------------------------------------

def get_corpus_status() -> dict[str, str]:
    """STATUS — the corpus_status block from the plugin manifest."""
    return json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))["corpus_status"]
