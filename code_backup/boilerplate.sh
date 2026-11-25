# !/usr/bin/env bash
# Chloe Soudan
# Script: boilerplate.sh
# Desc: Simple boilerplate for shell scripts
# Arguments: None
# Date: Oct 2026

echo -e "\nthis is a shell script \n"
# /n: new line 

echo -e "\ntest \n"

# confirmation code ran correctly

input_file="data/field notes.csv"
printf '<%s>\n' "$input_file" # prints <data/field notes.csv>
printf '<%s>\n' $input_file # prints <data/field> and <notes.csv>: filename split at the space. Should not use spaces in filenames

exit 0

# ran the script from the CMEECourseWork directory using: bash code/boilerplate.sh



