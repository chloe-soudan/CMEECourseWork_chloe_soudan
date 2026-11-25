birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

# printing latin names
latin_names = set(name[0] for name in birds)
print(latin_names)

# printing common names 
common_names = set(name[1] for name in birds)
print(common_names)

# printing body masses
body_masses = set(name[2] for name in birds)
print(body_masses)


# (2) Now do the same using conventional loops (you can choose to do this 
# before 1 !). 

# latin names 
latin_names_loops = set()
for name in birds:
    latin_names_loops.add(name[0])
print(latin_names_loops)

# common names
common_names_loops = set()
for name in birds:
  common_names_loops.add(name[1])

print(common_names_loops)

# body masses 
body_masses_loops = set()
for name in birds:
  body_masses_loops.add(name[2])

print(body_masses_loops)

 