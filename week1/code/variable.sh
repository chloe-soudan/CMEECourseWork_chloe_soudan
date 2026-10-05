# !/bin/bash

printf 'this script was called with %s parameters\n' "$#"
printf 'this script was invoked as %s\n' "$0"
printf 'the first argument is <%s>\n' "$!"
printf 'the second argument is <%S>n\' "$2"

my_value='some string'
printf 'current value: <%s>\n' "$my_value"
printf 'please enter a new string: 'IFS= read -r my_value
printf 'new value <%s>\n' "$my_value"

