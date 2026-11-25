#!/usr/bin/env python3
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: sysargv.py
# Desc: Inspecting sys.argv
# Date: Oct 2026

# ran chmod u+x sysargv.py in bash erminal to make it executable

""" display the command-line arguments supplied to this program"""

import sys

# Defining a main function that will print the script name, count the number of arguments of that script, and print them
def main(): 
    """ report the script name and its command-line arguments."""
    print(f"script name: {sys.argv[0]}")
    print(f"number of arguments: {len(sys.argv) -1}")
    print(f"arguments: {sys.argv[1:]}")


if __name__ == "__main__":
    main()

# executed: python3 code/sysargv.py and got the following lines
# script name: sysargv.py
# number of arguments: 0
# arguemtns: []

# executed python3 sysargv.py oak12 in the terminal and got:
# script name: sysargv.py
# number of argumetns: 2
# arguments: ['oak', '12']
# note: second run supplied two arguments: 'oak' and '12'