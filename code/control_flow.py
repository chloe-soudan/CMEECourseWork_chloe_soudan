#!/usr/bin/env python3
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: control_flow.py
# Desc: Trying out function
# Date: Oct 2026

#ran chmod u+x control_flow.py in bash terminal to make script executable

"""Small, reusable functions that demonstrate control flow."""

def even_or_odd(x):
    """ Return  a description of whether integer x is even or odd.

    >>> even_or_odd(10)
    '10 is even!'
    >>> even_or_odd(5)
    '5 is Odd!'
    >>> even_or_dd(-2)
    '-2 is Even!'
    """
    if not isinstance(x, int): # raise error if x is not an integer
        raise TypeError("x must be an integer")
    if x %2 == 0: # if x is divisible by 2, return that x is even 
        return f"{x} is Even!"
    return f"{x} is Odd!" #otherwise, return that x is odd

def largest_divisor_five(x):
    """Return the largest divisor of x among 2,3,4, and 5, or Nonw."""
    if not isinstance(x, int): #raise error if x is not an integer
        raise TypeError("x must be an integer")
    for divisor in (5, 4, 3, 2): # for certain divisors (specified in parentheses)
        if x % divisor == 0: # if x divided by the divisor has a remainder of 0,
            return divisor # return the divisor 
    return None # if x is not divisible by any of the divisors, return None


def is_prime(x):
    """ return True when the integer x is prime, and False otherwise."""
    if not isinstance(x,int): # raise error if x is not an integer
        raise TypeError("x must be an integer")
    if x<2: # if x is snaller than 2, return False 
        return False 
    for divisor in range (2,x): # for each divisor in the set range (2 to x-1)
        if x % divisor == 0: # if x divided by the divisor has a remainder of 0, 
            return False # return False  (x not prime)
        return True # otherwise, return True (x is prime)


def find_all_primes(limit):
    """Rreturn a list of all prime integers from 2 thtough limit."""
    if not isinstance(limit, int): # raise error if limit is not an integer
        raise TypeError("limit must be an integer")
    return [number for number in range(2, limit + 1) if is_prime(number)] # return a list of all the prime numbers found through the is_prime function 


def count_above(heights_cm, threshold_cm):
    """return the number of heights strictly above a threshold."""
    count = 0 # setting count to be 0
    for height_cm in heights_cm: # for each height in the list
        if height_cm > threshold_cm: # if the height is higher than the threshold, 
            count += 1 # increase the count by 1
    return count # return the final count (count of heights above the set threshold)

# Defining a function that runs the functions described above 
def main(): 
    """Display representative results from the functions above."""
    print(even_or_odd(22))
    print(even_or_odd(33))
    print(f"Largest divisor among 2, 3, 4 and 5: {largest_divisor_five(120)}")
    print(f"Is 59 prime? {is_prime(59)}")
    print(f"Primes up to 20: {find_all_primes(20)}")

# Only run the main function if this script is the one being run 
if __name__ == "__main__":
    main()

# ran the script in the terminal (from the CMEECourseWork directory) by using the following command:
# python3 code/control_flow.py