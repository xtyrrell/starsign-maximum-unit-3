from os import path
from tempfile import gettempdir
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

from sys import argv

import json

from download_file import streaming_download_file

from randomly_placed_images import generate_random_image_position

IMAGE_WIDTH = 40 * mm
IMAGE_HEIGHT = 40 * mm


def draw_image_event(event):
    url = event['content']
    filename = event['datetime']

    file_path = path.join(gettempdir(), filename)
    image_path = streaming_download_file(url, file_path)

    x, y = get_image_position(url) or generate_random_image_position(
        IMAGE_WIDTH, IMAGE_HEIGHT)

    c.drawImage(image=image_path, x=x, y=y, width=IMAGE_WIDTH,
                height=IMAGE_HEIGHT, preserveAspectRatio=True,
                mask='auto')


def get_image_position(identifier):
    # TODO: Ruby & Max populate this
    image_positions = {
        'http://localhost:3000/images/Frazier-Bunny-Rabbits.webp': (12 * mm, 150 * mm),
        'http://localhost:3000/images/chess_table.png': (90 * mm, 90 * mm)
    }

    return image_positions.get(identifier, None)


if __name__ == '__main__':
    events_filename = argv[1]
    output_filename = argv[2]

    with open(events_filename) as f:
        events = json.load(f)

    c = canvas.Canvas(output_filename, A4)

    for i, event in enumerate(events):
        if event['contentType'] == 'image':
            draw_image_event(event)

        # c.drawString(20, (i+1) * 50, str(event))

    c.save()
