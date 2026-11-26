
#!/bin/bash
# chloe.soudan26@imperial.ac.uk
# script: csvtospace.sh
# desc: substitute the comma with a tab
# arguments: 1 -> tab delimited file
# date: oct 2026

### CONVERTING CSV-DELIMITED FILES TO SPACE-DELIMITED FILES ####

# made the script executable using: chmod u+x tabtocsv.sh

#Accepting only one readable CSV input path 
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

# stating our task
echo "creating a tab delimited version of $1..."

# if the results directory does not exist, create it
if [ ! -d "results" ]; then
    mkdir results
fi

# converting text file to csv format
# note: asked AI how to do the following  CMEECourseWork/results/<input-filename>.txt
cat "$1" | tr "," "\t" >  "results/$(basename "$1").txt"

echo "done"

# ran the following command into terminal from project root:
# bash code/csvtospace.sh data/temperatures/1800.csv
# output:
# creating a tab delimited version of data/temperatures/1800.csv...
# done

# then ran cat results/1800.csv.txt in the terminal from project root to check conversion output
# note: output was tab delimited version of 1800.csv. Conversion was thus succesful. 