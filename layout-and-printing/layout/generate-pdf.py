from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from sys import argv

import json

events_filename = argv[1]
output_filename = argv[2]

with open(events_filename) as f:
    events = json.load(f)

c = canvas.Canvas(output_filename, A4, 0)
c.setLineWidth(.3)
c.setFont('Helvetica', 12)

for i, event in enumerate(events):
    c.drawString(20, (i+1) * 50, str(event))

c.save()
