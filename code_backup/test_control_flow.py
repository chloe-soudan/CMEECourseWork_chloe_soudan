#!/usr/bin/env python3
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: test_control_flow.py
# Desc: Testing control_flow.py functions
# Date: Oct 2026

import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "code"))

"""Checks for the small functions in control_flow.py."""

# Importing the functions from control_flow.py 
from control_flow import (
    count_above,
    even_or_odd,
    find_all_primes,
    is_prime,
    largest_divisor_five,)

# Checking if the even_or_odd() function works as expected for normal cases 
# using assert commands (raises error if statement is false)
assert even_or_odd(10) == "10 is Even!"
assert even_or_odd(5) == "5 is Odd!"


# Checking if the even_or_odd() function works as expected for edge cases 
# using assert commands (raises error if statement is false)
assert even_or_odd(0) == "0 is Even!"
assert even_or_odd(-2) == "-2 is Even!"

# 
# Checking if the even_or_odd() function works as expected for a failure case (non integer input)
# using assert commands (raises error if statement is false)
try:
    even_or_odd("10")
except TypeError:
    pass
else:
    raise AssertionError("A non-integer input was accepted")

# Checking if the largest_divisor_five() function works as expected 
assert largest_divisor_five(120) == 5
assert largest_divisor_five(8) == 4
assert largest_divisor_five(7) is None

# Checking if the is_prime() function works as expected for values that are smaller than 2 (not prime), and other values (both prime and not prime)
assert not is_prime(-1)
assert not is_prime(0)
assert not is_prime(1)
assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert find_all_primes(1) == []
assert find_all_primes(10) == [2, 3, 5, 7]

# Checking if the count_above() function works as expected for values above the threshold
assert count_above([8, 12, 10, 15], 10) == 2
# Checking if the count_above() function works as expected for values immediately below, at, and above the threshold
assert count_above([9, 10, 11], 10) == 1

# Checking if the count_above() function works as expected for values an empty collection
assert count_above([], 10) == 0

# ran the script in the terminal (from the CMEECourseWork directory) by using the following command:
# python3 -m doctest -v code/test_control_flow.py 
# Output says: Test passed (the functions thus work as expected)