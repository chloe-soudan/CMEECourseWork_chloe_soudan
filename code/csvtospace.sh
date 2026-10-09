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
# information from: https://askubuntu.com/questions/558977/checking-for-a-file-and-whether-it-is-readable-and-writable
# https://askubuntu.com/questions/1334801/how-do-multiple-and-work-with-if-statements

if [ ! -f "$1" ] || [ ! -r "$1" ]; then
    echo "error: unreadable or invalid input" >&2
    exit 2

fi

# stating our task
echo "creating a tab delimited version of $1..."

# converting text file to csv format
# note: asked AI how to do the following  ../results/<input-filename>.txt
cat "$1" | tr "," "\t" >  "../results/$(basename "$1").txt"

 echo "done"

# entered the follwing into bash terminal to actually convert the file:
# bash csvtospace.sh ../data/temperatures/1800.csv