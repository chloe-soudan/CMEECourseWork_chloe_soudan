#!/bin/bash
# chloe.soudan26@imperial.ac.uk
# script: tabtocsv.sh
# desc: substitute the tab# making data that can be destroyed 
# date: oct 2026

echo "creating a comma delimited version of $1 ..."
cat $1 | tr -s "\t" "," >> $1.csv

echo "done"

exit

shell_practice=$(mktemp -d)
printf 'species\tcount\noak\t12\n' > "$shell_practice/test.txt"
printf 'Practice data: %s\n' "$shell_practice"

sample_pattern="$shell_practice/*.txt"
printf '<%s>\n' "$sample_pattern"
printf '<%s>\n' $sample_pattern