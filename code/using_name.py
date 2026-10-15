# !/usr/bin/env python3
# chloe.soudan25@imperial.ac.uk
# RECOVERING AND COMPARING EXACT COPIES 

""" Demonstrate the value Python assigns to __name__"""

def module_name():
    """return the name python assigned to this module."""
    return __name__

def main():
    """report the module name during the execution"""
    print(f"this module's name is: {module_name()}")

if __name__ == "__main__":
    main()