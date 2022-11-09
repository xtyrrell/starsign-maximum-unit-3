from random import randrange, shuffle
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm

from sys import argv

DOCUMENT_WIDTH = 210 * mm
DOCUMENT_HEIGHT = 297 * mm

MARGIN = 15
# Because we want the document to have margins, the minimum X is not 0, it is 0 + margin
# and so on
MIN_X = MARGIN
MIN_Y = MARGIN
MAX_X = int(DOCUMENT_WIDTH - MARGIN)
MAX_Y = int(DOCUMENT_HEIGHT - MARGIN)


c = canvas.Canvas(f"play-pdfs/{randrange(0,10000)}.pdf", A4, 0)
c.setLineWidth(.3)
c.setFont('Helvetica', 12)


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
            x = randrange(MARGIN, int(MAX_X - width))
            y = randrange(MARGIN, int(MAX_Y - height))
        except ValueError:
            width /= 2
            height /= 2

    return (x, y)


image_paths = ["/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.47.55.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-07-26 at 17.05.25.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/green burger 2.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-07-08 at 12.39.03.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-07-08 at 16.38.02.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-07-26 at 17.05.25.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-07-26 at 17.19.24.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-07-26 at 17.19.39.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-08-02 at 13.32.24.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-10-20 at 18.58.09.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-05 at 19.47.37.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.45.56.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.46.03.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.46.10.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.46.20.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.46.27.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.47.14.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.47.55.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.48.15.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.48.45.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.48.54.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.49.19.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.49.30.png",
               "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.50.08.png",
               ]
shuffle(image_paths)


for image_path in image_paths[0:4]:
    width = randrange(MIN_X, MAX_X)
    height = randrange(MIN_Y, MAX_Y)

    x = None
    y = None

    while x is None or y is None:
        try:
            x = randrange(MARGIN, int(MAX_X - width))
            y = randrange(MARGIN, int(MAX_Y - height))
        except ValueError:
            width /= 2
            height /= 2

    c.drawImage(image=image_path, x=x, y=y, width=width,
                height=height, preserveAspectRatio=True)


c.save()
