
###### IMPPROVED TABTOCSV SCRIPT #########

#!/bin/bash
# chloe.soudan26@imperial.ac.uk
# script: tabtocsv.sh
# desc: substitute the tab
# date: oct 2026

chmod u+x tabtocsv.sh

#Accepting only one readable input path 
if [ "$#" -ne 1 ]; then
    echo "error: more than one readable input file provided" >&2
    exit 2

fi 

# Reporting a error for unreadable or invalid input
# information from: https://askubuntu.com/questions/558977/checking-for-a-file-and-whether-it-is-readable-and-writable
# https://askubuntu.com/questions/1334801/how-do-multiple-and-work-with-if-statements
if [ ! -f "$1" ] || [ ! -r "$1" ]; then
    echo "error: unreadable or invalid input" >&2
    exit 2

fi

# making results directory if it doesn't exist yet 
mkdir -p ../results

# stating our task
echo "creating a comma delimited version of $1..."

# converting text file to csv format
# note: asked AI how to do the following  ../results/<input-filename>.csv
cat "$1" | tr "\t" "," >  "../results/$(basename "$1").csv"

 echo "done"

### ran the following code separately:
# shell_practice=$(mktemp -d)
# printf 'species\tcount\noak\t12\n' > "$shell_practice/test.txt"
# printf 'Practice data: %s\n' "$shell_practice"
# bash tabtocsv.sh "$shell_practice/test.txt"



