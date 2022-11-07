#!/bin/bash

directory=watched-files-to-print

print () {
  echo "Printing..." $1
  say "Printing $1"
  # lp -d Samsung_M2020_Series $1
}

for f in $(find $directory -maxdepth 1 -type f -name "*.pdf"); do
  print $f
  mv $f $f.old
done
