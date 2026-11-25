#!/usr/bin/env python3
# chloe.soudan26@imperial.ac.uk
# FILE INPUT

# open a file for reading
f = open('sandbox/test.txt', 'r')
# use "implicit" for loop:
# if the object is a file, python will cycle over lines
for line in f:
    print(line)

#close the file
f.close()

#note: printed all the lines, but also the blank ones 

# same example, skip blank lines 
f = open('sandbox/test.txt', 'r') # r = read mode
for line in f:
    if len(line.strip()) > 0:
        print(line)

f.close()

# note: printed all the lines, skipping the blank ones 
# ran the full code using python3 code/basic_io1.py in the bash terminal