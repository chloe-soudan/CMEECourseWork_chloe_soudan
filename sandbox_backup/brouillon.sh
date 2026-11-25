# Creating a for loop to go over a list of species 
for species in oak pine birch 
do 
printf 'Considering %s\n' "$species" # print a message for each species in the list
done

# removing spaces usig tr -s command
echo "remove     excess    spaces" | tr -s " "

# removing a's g tr -d command 
echo " remove all the a's" | tr -d "a"

#setting case to uppercase using tr command 
echo "set to uppercase" | tr '[:lower:]' '[:upper:]'

# removing all letters and replacing spaces with commans using tr -d and tr -s commands 
echo "10.00 only numbers 1.33" | tr -d '[:alpha:]' | tr -s " " ","