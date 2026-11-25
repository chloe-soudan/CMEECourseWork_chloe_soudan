#!/usr/bin/env python3
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: using_name.py
# Desc: Using the __name__ variable 
# Date: Oct 2026

""" Demonstrate the value Python assigns to __name__"""
# Function returning the name of the python file being run 
def module_name():
    """return the name python assigned to this module."""
    return __name__
# Function printing the name of the python module while its being executed  
def main():
    """report the module name during the execution"""
    print(f"this module's name is: {module_name()}")

# Calling the main() function IF the file is being run directly (not imported into another python script)
if __name__ == "__main__":
    main()

# ran the code in the terminal (from CMEECourseWork directory) using the following command:
# python3 code/using_name.py
# returned: this module's name is: __main__ , meaning the the file was bein run directly
