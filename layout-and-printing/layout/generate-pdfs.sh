#!/bin/bash

directory=watched-event-logs

# because OpenKiosk is downloading files weirdly named...
for f in $(find $directory -maxdepth 1 -type f -name "*.json"); do
# for f in $(find $directory -maxdepth 1 -type f -name "*.txt.part"); do
  echo "Found file $f"
  python3 generate_pdf.py "$f" "../printing/watched-files-to-print/$(date +%s).pdf"
  sleep 5
  mv "$f" ../../finished
done

# for f in $(find $directory -maxdepth 1 -type f -name "*.json"); do
#   echo "Found file $f"
#   python3 generate_pdf.py $f ../printing/watched-files-to-print/$(date +%s).pdf
# done
