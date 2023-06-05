from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader

from sys import argv

import json

from randomly_placed_images import generate_random_image_position


IMAGE_WIDTH = 40 * mm
IMAGE_HEIGHT = 40 * mm


def draw_image_element(data_url, c):
    image = ImageReader(data_url)

    x, y = generate_random_image_position(IMAGE_WIDTH, IMAGE_HEIGHT)

    c.drawImage(image=image, x=x, y=y, width=IMAGE_WIDTH,
                height=IMAGE_HEIGHT, preserveAspectRatio=True,
                mask='auto')


def draw_text_element(text, c):
    x, y = generate_random_image_position(IMAGE_WIDTH * 3, IMAGE_HEIGHT)

    c.drawCentredString(x, y, text)


def generate_pdf(items, output_filename):
    c = canvas.Canvas(output_filename, A4)

    for i, element in enumerate(items):
        if element['imageUrl']:
            draw_image_element(element, c)
        if element['text']:
            draw_text_element(element, c)

    c.save()

if __name__ == '__main__':
    items_filename = argv[1]
    output_filename = argv[2]

    with open(items_filename) as f:
        items = json.load(f)
    
    generate_pdf(items, output_filename)
