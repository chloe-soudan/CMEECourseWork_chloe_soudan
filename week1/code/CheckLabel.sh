#!/bin/bash
if [[ $# -ne 1 ]]; then
printf 'usage: %s oak|pine\n' "$0" >&2

fi

if [[ "$1" != "oak" && "$1" != "pine" ]]; then
printf 'unknown label: %s\n' "$1" >&2

fi

printf 'selected species: %s\n' "$1"

echo "$?"

bash CheckLabel.sh oak
echo "$?"
bash CheckLabel.sh 
echo "$?"
bash CheckLabel.sh birch
echo "$?"
bash CheckLabel.sh oak pine 
echo "$?"

for species in oak pine birch 
do 
printf 'Considering %s\n' "$Species"
done

echo "remove     excess    spaces" | tr -s " "
echo " remove all the a's" | tr -d "a"
echo "set to uppercase" | tr '[:lower:]' '[:upper:]'
echo "10.00 only numbers 1.33" | tr -d '[:alpha:]' | tr -s " " ","