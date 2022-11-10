#!/bin/bash

cd /Users/ruby/Documents/2022/VideoGame/code/layout-and-printing/printing

watchman-make -p 'watched-files-to-print/*.pdf' --run ./print-pdfs.sh
