#!/bin/bash

directory=watched-event-logs

for f in $(find $directory -maxdepth 1 -type f -name "*.json"); do
  python generate-pdf.py $f ../printing/watched-files-to-print/$(date +%s).pdf
done
