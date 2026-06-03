"""Spot-check: each FINTEC file's verbatim Spanish name appears in the NCG 530 PDF."""
from __future__ import annotations

import re
from pathlib import Path

from tools.check_roundtrip import _extract_pdf_full_text, _normalize_ncg

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "corpus/ncg/530-fintec-reporting/catalog-fintec-files.md"
PDF = ROOT / "sources/ncg_530_2025-2.pdf"

# Table row: | FINTECnn | EN | ES verbatim | parties | purpose |
ROW_RE = re.compile(r"^\|\s*(FINTEC\d{2})\s*\|[^|]*\|\s*([^|]+?)\s*\|", re.MULTILINE)


def _catalog_rows() -> list[tuple[str, str]]:
    text = CATALOG.read_text(encoding="utf-8")
    return [(m.group(1), m.group(2)) for m in ROW_RE.finditer(text)]


def test_catalog_has_sixteen_files():
    rows = _catalog_rows()
    codes = [c for c, _ in rows]
    assert codes == [f"FINTEC{n:02d}" for n in range(1, 17)], codes


def test_each_spanish_name_present_in_pdf():
    pdf_norm = _normalize_ncg(_extract_pdf_full_text(PDF))
    missing = []
    for code, es_name in _catalog_rows():
        if _normalize_ncg(es_name) not in pdf_norm:
            missing.append((code, es_name))
    assert not missing, f"Spanish names not found verbatim in PDF: {missing}"
