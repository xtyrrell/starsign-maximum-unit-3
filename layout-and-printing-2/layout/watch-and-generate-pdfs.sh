#!/bin/bash

cd /Users/ruby/Documents/2022/VideoGame/code/layout-and-printing/layout

echo $(dirname -- $0)

# watching all files because of OpenKiosk downloading with weird extensions
watchman-make -p 'watched-event-logs/*.txt.part' --run ./generate-pdfs.sh