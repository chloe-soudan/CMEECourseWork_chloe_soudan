#!/bin/bash
# Chloe Soudan
# Script: CheckLabel.sh
# Desc: Simple boilerplate for shell scripts
# Date: Oct 2026

## Testing if statements and exit codes 

# If number of arguments not 1, print message and exit with code 2
if [[ $# -ne 1 ]]; then
    printf 'usage: %s oak|pine\n' "$0" >&2
    exit 2
fi

# If arguments is not oak or pine, print message and exit with code 1
if [[ "$1" != "oak" && "$1" != "pine" ]]; then
    printf 'unknown label: %s\n' "$1" >&2
    exit 1
fi

# If argument is oak or pine, print message and print exit code of previous command
printf 'selected species: %s\n' "$1"


## Ran the following lines in bash terminal from the CMEECoursework/code directory:
# bash CheckLabel.sh oak
# echo "$?"  - here was  0

# bash CheckLabel.sh  - output: usage: CheckLabel.sh oak|pine
# echo "$?" - output: 2

# bash CheckLabel.sh birch - output: unknown label: birch
# echo "$?" - output: 1

# bash CheckLabel.sh oak pine - output: usage: CheckLabel.sh oak|pine
# echo "$?" - output: 2
