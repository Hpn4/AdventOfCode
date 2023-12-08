#!/bin/sh

d=$(($(date +%-d)))
y=$(date +%Y)

curl --cookie "session=$(cat lib/cookie.txt)" https://adventofcode.com/$y/day/$d/input --output input$d.txt
tail -n 5 input$d.txt