#!/bin/bash
# chloe.soudan26@imperial.ac.uk
# script: tabtocsv.sh
# desc: substitute the tab# making data that can be destroyed 
# date: oct 2026

chmod u+x tabtocsv.sh

echo "creating a comma delimited version of $1 ..."
cat $1 | tr -s "\t" "," >> $1.csv

echo "done"

exit

shell_practice=$(mktemp -d)
printf 'species\tcount\noak\t12\n' > "$shell_practice/test.txt"
printf 'Practice data: %s\n' "$shell_practice"

# running script on temporary output
bash tabtocsv.sh "$shell_practice/test.txt"
# inspecting the output
cat "$shell_practice/test.txt.csv"

# empty fields 
printf 'oak\t\t12\n' | tr -s '\t' ','
# note: oak,12: made the missing field disappear
printf 'oak\t\t12\n' | tr '\t' ','
#note: oak,,12: represented the missing field 

# spaces in the path
cp "$shell_practice/test.txt" "$shell_practice/field notes.txt"
# note: copied contents of test.txt and put them into field notes.txt
bash tabtocsv.sh "$shell_practice/field notes.txt"
echo "$?"
#note: considered field notes.txt to be field and notes.txt, important to not have empty spaces


# wildcarts
sample_pattern="$shell_practice/*.txt"
printf '<%s>\n' "$sample_pattern"
# note: returns </tmp/tmp.zOIlJNs3jQ/*.txt>, prints literal pattern
printf '<%s>\n' $sample_pattern
# note: returns </tmp/tmp.zOIlJNs3jQ/test.txt>, expands the matching paths


##########

# creating test file
shell_practice=$(mktemp -d)
printf 'species\tcount\noak\t12\n' > "$shell_practice/test.txt"
printf 'Practice data: %s\n' "$shell_practice"
############

chmod u+x tabtocsv.sh

shell_practice=$(mktemp -d)

printf 'species\tcount\noak\t12\n' > "$shell_practice/test.txt"

printf 'Practice data: %s\n' "$shell_practice"

bash tabtocsv.sh "$shell_practice/test.txt"

cat "../results/test.txt.csv"
