from random import randrange, shuffle
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm

from sys import argv

DOCUMENT_WIDTH = 210 * mm
DOCUMENT_HEIGHT = 297 * mm

MARGIN_X = int(15 * mm)
MARGIN_TOP = int(15 * mm)
MARGIN_BOTTOM = int(50 * mm)
# Because we want the document to have margins, the minimum X is not 0, it is 0 + margin
# and so on
MIN_X = MARGIN_X
MIN_Y = MARGIN_BOTTOM
MAX_X = int(DOCUMENT_WIDTH - MARGIN_X)
MAX_Y = int(DOCUMENT_HEIGHT - MARGIN_TOP)


def generate_random_image_position(width=None, height=None):
    """
    Generates a random x, y pair position for the image that is well-placed in
    the document (all parts of the image will be inside the document,
    including margins).
    """
    width = width or randrange(MIN_X, MAX_X)
    height = height or randrange(MIN_Y, MAX_Y)

    x = None
    y = None

    while x is None or y is None:
        try:
            x = randrange(MARGIN_X, int(MAX_X - width))
            y = randrange(MARGIN_BOTTOM, int(MAX_Y - height))
        except ValueError:
            width /= 2
            height /= 2

    return (x, y)


if __name__ == "__main__":
    # Shows the bounds (line goes through valid area)
    c = canvas.Canvas(f"play-pdfs/lines{randrange(0,10000)}.pdf", A4, 0)
    c.setLineWidth(1)
    c.setFont('Helvetica', 12)

    c.line(MIN_X, MIN_Y, MIN_X, MAX_Y)
    c.line(MIN_X, MIN_Y, MAX_X, MIN_Y)
    c.line(MAX_X, MIN_Y, MAX_X, MAX_Y)
    c.line(MIN_X, MAX_Y, MAX_X, MIN_Y)

    c.save()
