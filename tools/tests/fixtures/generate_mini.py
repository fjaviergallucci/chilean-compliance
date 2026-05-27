"""Run once to produce mini.pdf — a minimal fixture for tooling tests."""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("tools/tests/fixtures/mini.pdf", pagesize=letter)
text = c.beginText(72, 720)
text.setFont("Courier", 10)
for line in [
    "LEY NUM. 99.999",
    "LEY DE PRUEBA",
    "",
    "TITULO I",
    "Disposiciones generales",
    "",
    "Articulo 1.- Objeto. Esta ley es de prueba.",
    "",
    "Articulo 2.- Definiciones. Para efectos de esta ley:",
    "a) Cosa: una cosa cualquiera.",
    "b) Otra cosa: otra cosa cualquiera.",
    "",
    "TITULO II",
    "Disposiciones varias",
    "",
    "Articulo 3.- Algo. Esta ley dispone algo.",
]:
    text.textLine(line)
c.drawText(text)
c.save()
print("Wrote tools/tests/fixtures/mini.pdf")
