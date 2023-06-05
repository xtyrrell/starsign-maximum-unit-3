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

    x, y = generate_random_image_position(IMAGE_WIDTH, IMAGE_HEIGHT)

    c.drawImage(image=image_path, x=x, y=y, width=IMAGE_WIDTH,
                height=IMAGE_HEIGHT, preserveAspectRatio=True,
                mask='auto')


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

        # name
        # feeling
        # aura image
        # avatar image
        # location
        # star sign
        # animal
        # 
        # {type: 'text' | 'image', content: 'data URL' | 'text content', label: 'name' | 'feeling' etc from the list above}[]
        # 
        # 

    c.save()
