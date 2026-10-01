#!/bin/bash
# chloe.soudan26@imperial.ac.uk
# script: tabtocsv.sh
# desc: substitute the tabs in the files with commas and saves output into csv file
# date: oct 2026

echo "creating a comma delimited version of $1 ..."
cat $1 | tr -s "\t" "," >> $1.csv

echo "done"

exit