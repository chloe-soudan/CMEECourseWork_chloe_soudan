#!/usr/bin/env python3
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: boilerplate.py
# Desc: Structuring python programs
# Date: Oct 2026

# ran the following line in bash to make script executable: 
#chmod u+x boilerplate.py

"""A minimal structure for an import-safe Python program. """
# defining a main function that coordinates the proram 
def main():
    """Run the program's main task."""
    print("this is a boilerplate")

if __name__ == "__main__": # if the file is being run directly (not imported into another python script),
    main() # run the main function

# ran the code in the terminal using the following command:
# python3 code/boilerplate.py 
# could also be done just ./boilerplate.py (because of chmod)
# output: this is a boilerplate (the file was indeed ran directly)
