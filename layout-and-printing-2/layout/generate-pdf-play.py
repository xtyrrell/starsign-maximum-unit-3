from random import randrange

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate("form_letter.pdf", pagesize=letter,
                        rightMargin=18, leftMargin=18,
                        topMargin=18, bottomMargin=18)
Story = []
images = ["/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-11-07 at 21.47.55.png",
          "/Users/max/workspace/starsign-maximum-unit-3/temp-images/Screenshot 2022-07-26 at 17.05.25.png"]
magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = "03/05/2010"
freeGift = "tin foil hat"

formatted_time = time.ctime()
full_name = "Mike Driscoll"
address_parts = ["64 Greatmore Street.", "Woodstock, Cape Town", "7925"]

for im in images:
    width = randrange(30, 150)
    height = randrange(30, 150)
    Story.append(Image(im, width, height))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
ptext = '%s' % formatted_time

Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))

# Create return address
ptext = '%s' % full_name
Story.append(Paragraph(ptext, styles["Normal"]))
for part in address_parts:
    ptext = '%s' % part.strip()
    Story.append(Paragraph(ptext, styles["Normal"]))

Story.append(Spacer(1, 12))
ptext = 'Dear %s:' % full_name.split()[0].strip()
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))

ptext = 'We would like to welcome you to our subscriber base for %s Magazine! \
        You will receive %s issues at the excellent introductory price of $%s. Please respond by\
        %s to start receiving your subscription and get the following free gift: %s.' % (magName,
                                                                                         issueNum,
                                                                                         subPrice,
                                                                                         limitedDate,
                                                                                         freeGift)
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))


ptext = 'Thank you very much and we look forward to serving you.'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))
ptext = 'Sincerely,'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 48))
ptext = 'Ima Sucker'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
doc.build(Story)
