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

# ran this shell in terminal by using following command: bash variable.sh one two
# was later prompter to enter a new string, and then two integers 