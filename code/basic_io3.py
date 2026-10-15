#!usr/bin/env python3
# chloe.soudan26@imperial.ac.uk
# STORING OBJECTS

# to save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11} #associating "a key" with a value of 10, and "another key" with a value of 11

import pickle

f = open('sandbox/testp.p', 'wb') # writing in binary mode 
pickle.dump(my_dictionary, f) # sabing dictionart to the file (testp.p) we just created
f.close() # closing the file

# loading the data again 
f = open('sandbox/testp.p', 'rb') # opening the file; rb = binary reading mode 
another_dictionary = pickle.load(f) # recreated the dictionary by reading the file
f.close()

print(another_dictionary)
