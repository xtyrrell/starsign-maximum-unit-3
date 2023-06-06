from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph

from sys import argv

from random import randint

import json

from randomly_placed_images import generate_random_image_position


IMAGE_WIDTH = 140 * mm
IMAGE_HEIGHT = 140 * mm

TEXT_WIDTH = 40 * mm
TEXT_HEIGHT = 40 * mm


def draw_image_element(c, data_url):
    image = ImageReader(data_url)
    imgwidth, imgheight = image.getSize()

    x, y = generate_random_image_position(imgwidth, imgheight)

    c.drawImage(image=image, x=x, y=y, width=imgwidth,
                height=imgheight, preserveAspectRatio=True,
                mask='auto')


def draw_text_element(c, text, fontname='Helvetica', fontsize=16):
    x, y = generate_random_image_position(TEXT_WIDTH * 3, TEXT_HEIGHT)
    
    c.setFont(fontname, fontsize)
    c.drawString(x, y, text)

def draw_text_element_as_border(c, text, fontname='Helvetica', fontsize=16):
    # c = canvas.Canvas('aa', A4)
    c.setFont(fontname, fontsize)

    text = ("  " + text + "  ") * 100

    # c = canvas.Canvas('P')
   
    # Top line
    c.drawCentredString(A4[0] / 2, 10 * mm, text)
    # Bottom line
    c.drawCentredString(A4[0] / 2, A4[1] - (10 * mm), text)
    # Right line
    # c.drawCentredString(A4[0] / 2, A4[1] - (10 * mm), text)

def draw_image_with_text(c, data_url, text, fontname='Helvetica', fontsize=16):
    image = ImageReader(data_url)
    imgwidth, imgheight = image.getSize()

    x, y = generate_random_image_position(imgwidth, imgheight)

    c.drawImage(image=image, x=x, y=y, width=imgwidth,
                height=imgheight, preserveAspectRatio=True,
                mask='auto')
    c.setFont(fontname, fontsize)
    c.drawString(x, y + imgheight + 5 * mm, text)


def draw_scoring(c):
    c.setFont("Times-Italic", 12)

    cyber = randint(0, 100)
    sporty = randint(0, cyber)
    bohemian = 100 - cyber - sporty
    scoring_text = f'Cyber: {cyber}%   Sporty: {sporty}%   Bohemian: {bohemian}%'
    c.drawCentredString(A4[0] / 2, 25 * mm, scoring_text)


def generate_pdf(items, output_filename):
    c = canvas.Canvas(output_filename, A4)

    for i, element in enumerate(items):
        if element.get('label') == 'star-sign':
            draw_text_element_as_border(c, element['text'], 'Times-Italic', 14)
            continue
        if element.get('label') == 'aura':
            draw_image_with_text(c, element['imageUrl'], '** My aura looks like: **', 'Times-Italic', 14)
            continue

        if element.get('imageUrl'):
            draw_image_element(c, element['imageUrl'])
        if element.get('text'):
            draw_text_element(c, element['text'], 'Times-Italic' if element['label'] == 'star-sign' else 'Helvetica', 16)
        
    draw_scoring(c)

    c.save()

if __name__ == '__main__':
    items_filename = argv[1]
    output_filename = argv[2]

    print("Generating PDF from {} to {}".format(items_filename, output_filename))

    with open(items_filename) as f:
        items = json.load(f)
    
    generate_pdf(items, output_filename)
