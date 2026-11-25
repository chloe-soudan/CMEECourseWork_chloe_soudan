# !/bin/bash
# Chloe Soudan
# Script: CountLines.sh
# Desc: Counting number of lines in file 
# Date: Oct 2026

# Using the wc -l command to count the number of lines in a file 
NumLines=`wc -l < "$1"`
echo "the file $1 has $NumLines lines"
echo 

# ran the code from CMEECourseWork directory using the following command 
# (used "field nots.csv" data again for testing): bash code/CountLines.sh "data/field notes.csv"
# Output: the file data/field notes.csv has 348 lines
 
