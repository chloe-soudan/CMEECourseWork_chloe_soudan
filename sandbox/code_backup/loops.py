
#!/usr/bin/env python3
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: loops.py
# Desc: Practicing python loops
# Date: Oct 2026

# FOr loops
for i in range(5): # for each number in the range (0 to 4),
    print(i) # print the number
#note: prints number from 1 to 4

my_list = [0,2, "geronimo!", 3.0, True, False]
for k in my_list: # for each item in my list,
    print(k) # print the item
#note: prints every item in the list

total = 0
summands=[0,1,11,111,1111]
for s in summands: # for each value in my summands list,
    total = total + s # add the value to the total
print(total)

#WHILE loop
z = 0
while z <100: # while z is smaller than 100
    z=z+1 # increase z by 1
    print(z)

# ran the script in the terminal (from the CMEECourseWork directory) by using the following command:
# python3 code/loops.py