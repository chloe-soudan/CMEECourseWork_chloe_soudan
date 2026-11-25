#!/usr/bin/env python3
# chloe.soudan26@imperial.ac.uk
# FILE OUTPUT

# save the elements of a list to a file
list_to_save = range(100) # creating a sequence ranging from 0 to 99

f = open('sandbox/testout.txt', 'w') #w = write mode
for i in list_to_save:
    f.write(str(i) + '\n') # adding a new line at the end

f.close # closing the file

# ran it from the bash terminal using python3 code/basic_io2.py
# note: created a testout.txt file in my sandbox folder