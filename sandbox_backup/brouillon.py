
"""Some functions exemplifying the use of control statements"""

__author__ = 'Chloe Soudan (chloe.soudan26@imperial.ac.uk)'
__version__ = '0.0.1'

import sys
import doctest

# Defining the function even_or_odd that will be tested 
def even_or_odd(x=0): # if not specified, x should take value 0.

    """
    Find whether a number x is even or odd.

    >>> even_or_odd(10)
    '10 is Even!'

    >>> even_or_odd(5)
    '5 is Odd!'

    in case of negative numbers, the positive is taken:
    >>> even_or_odd(-2)
    '-2 is Even!'

    """
    if x % 2 == 0: # if x divided by 2 has a remainder of 0,
        return f"{x} is Even!" # return that x is ever
    return f"{x} is Odd!" # otherwise, return that x is odd

# Defining the main function
def main(argv):
    print(even_or_odd(22))
    print(even_or_odd(33))
    return 0

# Setting a condition that will only run the main function if the script is being run directly 
if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)

# Testing the functions 
doctest.testmod() 


def square(number):
    """
    Return the square of a number. 

    >>> square(4)
    16
    """
    return number * number


# ran the script in the terminal (from the CMEECourseWork directory) by using the following command:
# python3 -m doctest -v code/test_control_flow.py


########### OBSERVATIONS_PRACTICE.PY ###########


# importing the data
import csv

def load_observations(path):
    with open(path, newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))

#loading in the bootcamp data
observations = load_observations("data/bootcamp_observations.csv")

# inspecting the data
if __name__ == "__main__":
    rows = load_observations("data/bootcamp_observations.csv")
    print(rows[0])
    print(rows[2])
# writing the function for site a

def calc_function1(site):
     """writing a reusable function that calculates the results for one 
requested site"""
     site_sum = 0
     site_missing_count = 0
     for count in site:
          if count == "": # when string is empty
               site_missing_count += 1 # adding one to the missing counts sum 
          else:
               site_sum += int(count)
     return site_sum, site_missing_count


# note: site a sum is 4 and there is 1 missing count

def calc_function2(observations):
     """"A reusable function that calculates the results for each
     site"""
     
     results = []

     for site in set(row["site"] for row in observations):
          site_sum = 0
          site_missing_count = 0
          
          for observation in observations:
               if observation["site"] == site:
                    count = observation["count"]
                    if count == "": # when string is empty
                         site_missing_count += 1 # adding one to the missing counts sum 
                    else:
                         site_sum += int(count)
                
          results.append((site, site_sum, site_missing_count))

     return(results)

print(calc_function2(observations))
# ran in bash terminal by running python3 code/observations_practice.py



def parse_count(count_text):
    """guided conversion of count text """
    if count_text== "":
        return None

    count=int(count_text)

    if count <0:
        raise ValueError("Count must be non-negative")

    return count
    
###### TEST_OBSERVATIONS_PRACTICE.PY #############


# importing the data
import csv

def load_observations(path):
    with open(path, newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))

#loading in the bootcamp data
observations = load_observations("data/bootcamp_observations.csv")

# testing for site a


# selecting the site a rows
site_a = [row["count"] for row in observations if row["site"] == "A"]

print(calc_function1(site_a))
# worked, printed (4, 1) as results

print(calc_function2(observations))
# worked printed [('B', 0, 0), ('A', 4, 1)] as results

### Testing parse count 
# Normal case: ordinary count text becomes an integer.
assert parse_count("2") == 2

# Boundary case: zero is a valid known count.
assert parse_count("0") == 0

# Special valid case: blank text represents a missing count.
assert parse_count("") is None

# Failure cases: each invalid value must raise ValueError.
for bad_count in ["-1", "many", 2]:
    try:
        parse_count(bad_count)
    except ValueError:
        pass
    else: 
        raise AssertionError(f"Invalid count accepted: {bad_count!r}")


###### DEBUGME.PY #########


### HANDLING EXPECTED ERRORS 
# using %cpaste in ipython3, ran:

def buggyfunc(x):
    y = x
    for i in range(x):
        try: 
            y = y-1
            z = x/y
        except:
            print(f"This didn't work;{x = }; {y = }")
    return z

buggyfunc(20)


#output: This didn't work; x = 20; y =0 
# tried (try) to do y = y-1 and z = x/y but didn't work so it went to except command

## catch specific errors 
def buggyfunc(x):
    y = x
    for i in range(x):
        try: 
            y = y-1
            z = x/y
        except ZeroDivisionError:
            print(f"The result of dividing a number by zero is undefined")
        except:
            print(f"This didn't work;{x = }; {y = }")
        else:
            print(f"OK; {x = }; {y = }, {z = };")
    return z

buggyfunc(20)

# note: output was a bunch of lines starting with OK, except the last one
# that stated "the result of divding a nunber by zero is undefined"


#### R browser.R ####
## using debug()
buggy_function <- function(n) {
    result <- n + unknown_variable
    return(result)
}

# ran debug(buggy_function) in R terminal
# ran buggy_function(10) in R terminal
