from random import randrange, shuffle
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm


c = canvas.Canvas(f"play-pdfs/full.pdf", A4, 1)

c.drawImage(
    "/Users/max/workspace/starsign-maximum-unit-3/temp-images/green burger 2.png",
    0,
    0,
    width=210 * mm,
    height=297 * mm
)

c.save()
