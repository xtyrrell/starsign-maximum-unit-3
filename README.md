# Starsign Maximum U3

## Todos

### Features to PoC

- [x] log: log each link-image that the user clicks, so that we can list out all the images that a user clicked on
- [x] layout: given a list of images that a user clicked on, layout those images onto a page, with each image having predetermined position
  - [x] generate PDF with text from JSON
  - [ ] generate PDF with images from JSON
  - [ ] map out images' positions so an image X prints in the right spot every time
- [x] print: given a PDF, print that with no user input to the Samsung printer connected to this computer

watching

- [x] watch an event logs folder and whenever one appears, generate a PDF of it and place that in the PDFs folder, then rename it `.old`
- [x] watch a PDFs folder and whenever one appears, print it then rename it `.old`

### Work to do

- [ ] transcribe powerpoint into HTML

## Python utilities to layout a PDF and print it

Dependencies

- Python 3
- reportlab (`$ pip install reportlab`)
- homebrew (`$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`)
- watchman (`$ brew install watchman`)
- Python requests (`$ pip install requests`)

## Setup watcher for downloads folder

Principle of operation: we watch for changes in the Downloads folder (files being added / removed). When a change to the folder happens, we check if there are any .pdf files in the directory, and print them and them rename them to `.old` (this way they will no longer have a .pdf extension so will not be printed twice).

To set this up

0. Configure downloads folder for the browser to point to `layout/watched-event-logs`
1. Ensure `layout/watched-event-logs` and `printing/watched-files-to-print` are empty
2. Run (each in their own terminal)

   ```sh
   $ layout/watch-and-generate-pdfs.sh
   $ printing/watch-and-print-pdfs.sh
   ```

# To add a new image in the website (to have printed)

1. Add the image to /images (must have transparent background)
2. Add it to a page (wrapped in an `a`). Give the `img` the `clickable` HTML class
3. In `layout-and-printing/layout/generate_pdf.py` in `get_image_position()`, add an entry for its position. You may have to do some trial and error to find a position that works well.
