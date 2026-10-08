### CONVERTING CSV-DELIMITED FILES TO SPACE-DELIMITED FILES ####


#!/bin/bash
# chloe.soudan26@imperial.ac.uk
# script: csvtospace.sh
# desc: substitute the comma with a tab
# date: oct 2026

chmod u+x csvtospace.sh

#Accepting only one readable CSV input path 
if [ "$#" -ne 1 ]; then
    echo "error: more than one readable input file provided" >&2
    exit 2

fi

# Reporting a error for unreadable or invalid input

if [ ! -f "$1" ] || [ ! -r "$1" ]; then
    echo "error: unreadable or invalid input" >&2
    exit 2

fi

# stating our task
echo "creating a tab delimited version of $1..."

# converting text file to csv format
cat "$1" | tr "," "\t" >  "../results/$(basename "$1").txt"

 echo "done"
