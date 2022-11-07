from random import randrange, shuffle
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

from sys import argv

import json


c = canvas.Canvas(f"play-pdfs/{randrange(0,10000)}.pdf", A4, 0)
c.setLineWidth(.3)
c.setFont('Helvetica', 12)

# for i, event in enumerate(events):
#     c.drawString(20, (i+1) * 50, str(event))


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

DOCUMENT_WIDTH = 500
DOCUMENT_HEIGHT = 1500
MARGIN = 15

for image_path in image_paths[0:4]:
    width = randrange(100, 150)
    height = randrange(100, 150)

    x = randrange(MARGIN, DOCUMENT_WIDTH - MARGIN - width)
    y = randrange(MARGIN, DOCUMENT_HEIGHT - MARGIN - height)

    c.drawImage(image=image_path, x=x, y=y, width=width,
                height=height, preserveAspectRatio=True)


c.save()
