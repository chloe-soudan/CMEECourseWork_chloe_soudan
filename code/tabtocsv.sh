
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

fi Ecological and social pressures drive same-sex sexual behaviour in non-human primates

# Reporting a error for unreadable or invalid input

if [ ! -f "$1" ] || [ ! -r "$1" ]; then
    echo "error: unreadable or invalid input" >&2
    exit 2

fi
# making results directory if it doesn't exist yet 
mkdir -p ../results

# stating our task
echo "creating a comma delimited version of $1..."

# converting text file to csv format
cat "$1" | tr "\t" "," >  "../results/$(basename "$1").csv"

 echo "done"




