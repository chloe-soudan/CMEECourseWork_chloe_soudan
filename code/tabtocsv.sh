#!/bin/bash
# chloe.soudan26@imperial.ac.uk
# script: tabtocsv.sh
# desc: substitute the tab
# arguments: 1 -> tab delimited file
# date: oct 2026

###### IMPPROVED TABTOCSV SCRIPT #########

# made the script executable using: chmod u+x tabtocsv.sh

#### 1. Accepting only one readable input path ####
if [ "$#" -ne 1 ]; then
    echo "error: more than one readable input file provided" >&2
    exit 2 # 

fi 

#### 2. Reporting a error for unreadable or invalid input ####

# information from: https://askubuntu.com/questions/558977/checking-for-a-file-and-whether-it-is-readable-and-writable
# https://askubuntu.com/questions/1334801/how-do-multiple-and-work-with-if-statements

if [ ! -f "$1" ] || [ ! -r "$1" ]; then
    echo "error: unreadable or invalid input" >&2
    exit 2

fi


#### 3. converting text file to csv format ###

# stating the  task
echo "creating a comma delimited version of $1..."

# Converting the file
cat "$1" | tr "\t" "," >  "results/$(basename "$1").csv"
# note: asked AI how to do the following  ../results/<input-filename>.csv

#### 4. Printing a completion message ####
echo "done"

exit


# ran the following code separately:
#shell_practice=$(mktemp -d)
#printf 'species\tcount\noak\t12\n' > "$shell_practice/test.txt"
#printf 'Practice data: %s\n' "$shell_practice"

# ran the following code in the terminal from the project root:
# bash code/tabtocsv.sh "$shell_practice/test.txt"
# output:
# creating a comma delimited version of /tmp/tmp.77hRHCA2Vo/test.txt...
# done

# then ran cat results/test.txt.csv in the terminal from project root to check conversion output
# output:
# species,count
# oak,12


