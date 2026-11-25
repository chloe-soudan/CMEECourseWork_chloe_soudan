#!/usr/bin/env python3
# chloe.soudan26@imperial.ac.uk
# REPORTING SUCCESS OR FAILURE 

# ran chmor u+x require_one_terminal.py in bash terminal to make it executable
import sys

def main():
    if len(sys.argv) !=2:
        print("usage: python require_one_argument.py, VALUE", file = sys.stderr)
        return 1
    print(f"received: {sys.argv[1]}")
    return 0

if __name__ == "__main__":
    sys,exit(main())

# ran python3 require_one_argument.py and echo $? 
# got: usage: python require_one_argument.py, VALUE and 1
# ran python3 require_one_argument.py oak and got received: oak, then 
# ran echo $? and got 0
# echo $? represented the status of the immediatly preceding command
# status of 0: immediatly preceding command ran succesfully, 1 indicates failure