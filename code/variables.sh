# !/bin/bash
# chloe.soudan26@imperial.ac.uk

printf 'this script was called with %s parameters\n' "$#"
printf 'this script was invoked as %s\n' "$0"
printf 'the first argument is <%s>\n' "$1"
printf 'the second argument is <%s>\n' "$2"

my_value='some string'
printf 'current value: <%s>\n' "$my_value"
printf 'please enter a new string: '
IFS= read -r my_value
printf 'new value <%s>\n' "$my_value"

printf 'Enter two integers separated by spaces: '
read -r first_number second_number
printf 'You entered %s and %s\n' "$first_number" "$second_number"
my_sum=$(expr "$first_number" + "$second_number")
printf ' Their sum is: %s\n' "$my_sum"

# ran this shell in terminal by using following command: bash variables.sh 
# note: script worked but first lines printed had empty values for first and second arguments (as no aruguments were passed).
# was later prompted to enter a new string, and then two integers which were summed up.

# ran this shell in terminal by using following command: bash variables.sh "two words"
# note: script worked but terminal cosnidered that only one arguments was passed (because of the quotes)
# was later prompted to enter a new string, and then two integers which were summed up.

# ran this shell in terminal by using following command: bash variables.sh two words
# note: script worked. terminal considered that two arguments were passed (removed the quotes).
# was later prompted to enter a new string, and then two integers which were summed up.

