#!/usr/bin/env python3
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: debugme.py
# Desc: Debugging in python practice
# Date: Oct 2026

#def buggyfunc(x):
#    y =x
#    for i in range(x):
#        y = y-1
#        z = x/y
#    return z

# buggyfunc(20)
# ran it with python3 code/debugme.py
#output: ZeroDivisionError message - division by zero
# note: most recent call last, what was the call that led to the error 

# Turned on ipython3
# Turned on python debugger (%pdb) in ipython3
# Running it again %run code/debugme.py
# Showed me where the error was (z = x/y)
# Turned of debugger by running q command in ipdb

## Adding breakpoint
def buggyfunc(x):
    y =x
    for i in range(x):
        y = y-1
        if y == 0:
            breakpoint()
        z = x/y
    return z

buggyfunc(20)

# ran it again using %run code/debugme.py in ipython3 (could also just run it from terminal)
# Ouptut: breaks down every iteration and whetehr it worked or not, and shows where it didn't work
