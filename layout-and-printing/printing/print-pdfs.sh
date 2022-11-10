#!/bin/bash

directory=watched-files-to-print

for f in $(find $directory -maxdepth 1 -type f -name "*.pdf"); do
  lp $f # this prints $f
  # sleep 3
  mv $f $f.old
done
