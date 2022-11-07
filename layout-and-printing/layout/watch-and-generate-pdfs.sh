#!/bin/bash

watchman-make -p 'watched-event-logs/*.json' --run ./generate-pdfs.sh
