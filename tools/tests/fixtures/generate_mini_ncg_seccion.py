"""Generate mini_ncg_seccion.pdf — a SECCIÓN-style NCG fixture (like NCG 514).

Top-level dividers are 'SECCIÓN <Roman>: TITLE', the ToC marker is
'Índice Norma:', and subsections are lettered A/B with numbered children.
Letters repeat across Secciones (so the extractor must Roman-prefix them).
"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("tools/tests/fixtures/mini_ncg_seccion.pdf", pagesize=letter)


def page(lines):
    text = c.beginText(72, 720)
    text.setFont("Courier", 10)
    for line in lines:
        text.textLine(line)
    c.drawText(text)
    c.showPage()


page([
    "NORMA DE CARACTER GENERAL N 888",
    "",
    "Indice Norma:",
    "",
    "SECCION I: PRIMERA SECCION ............................. 2",
    "   A. Sub Alfa .......................................... 2",
    "   B. Sub Beta .......................................... 2",
    "SECCION II: SEGUNDA SECCION ............................ 3",
    "   A. Otra Alfa ......................................... 3",
])
page([
    "SECCION I: PRIMERA SECCION",
    "",
    "A. Sub Alfa",
    "Contenido de la primera subseccion alfa.",
    "",
    "B. Sub Beta",
    "Contenido de la subseccion beta.",
])
page([
    "SECCION II: SEGUNDA SECCION",
    "",
    "A. Otra Alfa",
    "Contenido de la segunda seccion, subseccion alfa.",
])
c.save()
print("Wrote tools/tests/fixtures/mini_ncg_seccion.pdf")
