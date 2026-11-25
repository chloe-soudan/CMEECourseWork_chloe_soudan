# !/bin/bash
# Chloe Soudan
# Script: ConcatenateTwoFiles.sh
# Desc: Concatenateing two files into a third file
# Date: Oct 2026

# taking contents of first file and writing them into a third file (this step overwrites existing contents of the thid file)
cat "$1" > "$3" 
#  # appending contents of second file to third file (>> appends contents to file rather than overwriting)
cat "$2" >> "$3" 

echo "merged file is"
# printing contents of the third file  
cat "$3"

# from project root (CMEECoursework directory) ran this:
# shell_practice=$(mktemp -d)  
#printf 'oak\n' > "$shell_practice/first.txt"
#printf 'pine\n' > "$shell_practice/second.txt"
# bash code/ConcatenateTwoFiles.sh "$shell_practice/first.txt" "$shell_practice/second.txt" "$shell_practice/combined.txt"

# Output:
#t.txt" "$shell_practice/second.txt" "$shell_practice/combined.txt"
#merged file is
#oak
#pine

# note: rerunning this code would not duplicate the results as the first step's single arrow (>) overwrites the contents of the third file
