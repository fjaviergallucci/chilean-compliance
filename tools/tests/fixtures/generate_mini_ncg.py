"""Generate mini_ncg.pdf — a minimal NCG-shaped fixture for tooling tests.

Mimics a CMF Norma de Carácter General: a title, an ÍNDICE (table of
contents) listing sections with page numbers, then a body with hierarchical
section headings (Roman -> letter -> number).
"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("tools/tests/fixtures/mini_ncg.pdf", pagesize=letter)


def page(lines):
    text = c.beginText(72, 720)
    text.setFont("Courier", 10)
    for line in lines:
        text.textLine(line)
    c.drawText(text)
    c.showPage()


# Page 1: title + índice
page([
    "NORMA DE CARACTER GENERAL N 999",
    "",
    "INDICE",
    "",
    "I. Primera Seccion ......................................... 2",
    "   A. Sub A .................................................. 2",
    "   B. Sub B .................................................. 2",
    "II. Segunda Seccion ........................................ 3",
    "   A. Otra Sub ............................................... 3",
])
# Page 2: section I body
page([
    "I. PRIMERA SECCION",
    "",
    "A. Sub A",
    "Esta es la primera subseccion. Contiene reglas.",
    "",
    "B. Sub B",
    "Esta es la segunda subseccion. Contiene mas reglas.",
])
# Page 3: section II body
page([
    "II. SEGUNDA SECCION",
    "",
    "A. Otra Sub",
    "Esta subseccion pertenece a la segunda seccion.",
])
c.save()
print("Wrote tools/tests/fixtures/mini_ncg.pdf")
