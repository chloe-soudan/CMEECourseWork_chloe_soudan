#!/usr/bin/env python3
# chloe.soudan26@imperial.ac.uk
# Python: comprehensions

taxa = [ 'Quercus robur',
         'Fraxinus excelsior',
         'Pinus sylvestris',
         'Quercus cerris',
         'Quercus petraea',
       ]

#defining the is_an_oak function 
def is_an_oak(name): # defining the is_an_oak function, with name as argument
    return name.lower().startswith('quercus') # to return in lower case the names that start with quercus

# using for loops
oaks_loops = set() # creating an empty set called oaks_loops
for species in taxa: # loopint through the species in the taxa list
    if is_an_oak(species): # if the is_an_oak functions returns true (species starts with 'quercus'
        oaks_loops.add(species) # then add the species to the set
print(oaks_loops)

# using list comprehensions
oaks_lc = set([species for species in taxa if is_an_oak(species)])
print(oaks_lc) 
# does the same as previous step, but written as a comprehension

# getting names in upper case using for loops
oaks_loops = set()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species.upper()) # converts to upper case
print(oaks_loops)
# does the same as previous steps but converts the species' names to upper case

# repeating the same as before but using comprehnesions instead of loops
oaks_lc = set([species.upper() for species in taxa if is_an_oak(species)])
print(oaks_lc)