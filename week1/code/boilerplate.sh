# !/usr/bin/env bash
#Chloe Soudan
# Script: boilerplate.sh
# Desc: Simple boilerplate for shell scripts
# Arguments: None
# Date: Oct 2026
echo -e "\nthis is a shell script \n"
# /n: new line 

echo -e "\ntest \n"

# confirmation code ran correctly

echo input_file = "field_notes.csv"
printf '<%s>\n' "$input_file"
printf '<%s>\n' $input_file

# making data that can be destroyed 
mkdir -p ../sandbox/shell-demo
printf 'species\tcount\noak\t12\n' > ../sandbox/shell-demo/test.txt
cat ../sandbox/shell-demo/test.txt

