#!/bin/bash

directory=watched-files-to-print

for f in $(find $directory -maxdepth 1 -type f -name "*.pdf"); do
  echo "In dir"
  pwd
  sleep 5
  echo "Printing file \$f: $f"
  lp "$f" # this prints $f
  sleep 5
  mv "$f" "$f.old"
done
