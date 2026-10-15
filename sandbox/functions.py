### ITERATOR vs ITERABLE

my_iterable = [1,2,3]
type(my_iterable)
# it's a list 

my_iterator = iter(my_iterable)
type(my_iterator)

next(my_iterator)
next(my_iterator)
next(my_iterator)
next(my_iterator)

# generators 

heights = [8,12,10]
height_iterator = iter(heights)
print(next(height_iterator))
print(next(height_iterator))
print(next(height_iterator))
print(heights)

height_generator = (height_cm*2 for height_cm in heights)
print(next(height_generator))
print(list(height_generator))
print(list(height_generator))

height_range = range(3)
print(list(height_range))
print(list(height_range))

### LOOPS ###
for i in range(5):
    print(i)

my_list = [0,2, "geronimo!", 3.0, True, False]
for k in my_list:
    print(k)

total = 0 
summands = [0,1,11,111,1111]
for s in summands:
    total = total +s
print(total)

# WHILE loop

z=0
while z < 100:
    z=z+1
print(z)

### FUNCTIONS IN PYTHON ###

def foo(x):
    x *= x
    print(x)
    return x

%whos

foo(2)

def foo(x):
    x *= x 
    print (x)
    return(x)
y = foo(2)

y

type(y)

def foo(x):
    x *= x 
    print (x)

y = foo(2)

y
type(y)

### CONDITIONALS ###

x = 0; y =2

if x < y: 
    print("yes")

# returns 'yes'

if x:
    print('yes')
# no output

if x==0:
    print('yes')
#'yes'

if y:
    print('yes')
# 'yes'

if y == 2:
    print('yes')
# 'yes'

x = True
if x:
    print('yes')
# prints 'yes' but if x = False doesn't print anything 

if x == True:
    print('yes')

### importance of return directive ###

def modify_list_1(some_list):
    print('got', some_list)
    some_list = [1,2,3,4]
    print('set to', some_list)

my_list =[1,2,3]
print('before, my_list', my_list)

modify_list_1(my_list)

print('after, my list =', my_list)

def modify_list_1(some_list):
    print('got', some_list)
    some_list = [1,2,3,4]
    print('set to', some_list)
    return some_list

my_list = modify_list_1(my_list)
print('before, my_list=', my_list)

#### from an algorythm to python ####

heights_cm = [8,12,10,15]
above_threshold = 0
for height_cm in heights_cm:
    if height_cm > 10:
        above_threshold +=1
print(above_threshold)

### worked function ####
def count_above(heights_cm,  threshold_cm):
    above_threshold = 0 
    for height_cm in heights_cm:
        if height_cm > threshold_cm:
            above_threshold +=1
    return above_threshold

assert count_above([8,12,10,15], 10) == 2
assert count_above ([10], 10) == 0

assert count_above() == 1

### COMPREHENSIONS #####

x = [i for i in range(10)]
print(x)

# this prints the same as before
x = []
for i in range (10):
    x.append(i)
print(x)

# using a loop to convert to lower case
x = ["LIST", "COMPREHENSIONS", "ARE", "COOL"]
x_new = []
for i in x:
    x_new.append(i.lower())
print(x_new)

# nested loops

matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened_matrix = []
for row in matrix: # for each row in the matrix
    for n in row: # for every n inside the iterated row
        flattened_matrix.append(n) # add n to the flattened_matrix
print(flattened_matrix) # will result in a list of all the numbers that were in the matrix

# does the same as before but in shorter command
matrix = [[1,2,3],[4,5,6], [7,8,9]]
flattened_matrix = [n for row in matrix for n in row]
print(flattened_matrix)

# set and dictionary comprehensions

words = ["these", "are", "some", "words" ]

first_letters = set()
for w in words: 
    first_letters.add(w[0])

print(first_letters) # prints 's', 'w', 't', 'a', they're unordered
type(first_letters) # type is a set

# same as a set comprehension
words = ["these","are", "some", "words"]
first_letters = {w[0] for w in words}

print(first_letters)
type(first_letters)

# variable scope

i = 1
x = 0
for i in range(10):
    x+=1
print(i)
print(x)
# does change x and i 

i = 1
x = 0 
def a_function(y):
    x=0
    for i in range(y):
        x +=1
        return(x)
a_function(10)

print(i)
print(x)
# doesn't actually change x and i because they are encapsulated in a function

# GLOBAL VARIABLES 

_a_global = 10  

if _a_global >=5:
    _b_global = _a_global +5

print("Before calling a_function, outside the function, the value of _a_global is", _a_global)
print("Before calling a_function, outside the function, the value of _b_global is", _b_global)

def a_function():
    _a_global = 4

    if _a_global >=4:
        _b_global = _a_global +5 

    _a_local =3 

    print("Inside the function, the value of _a_global is", _a_global)
    print("Inside the function, the value of _b_global is", _b_global)
    print("Inside the function, the value of _a_local is", _a_local)

a_function()

print("After calling a_function, outside the function, the value of _a_global is (still)", _a_global)
print("After calling a_function, outside the function, the value of _b_global is (still)", _b_global)
print("After calling a_function, outside the function, the value of _a_local is ", _a_local)

# _a_ local did not exist outside the function
# the globals also were printed as they were outside the function 

# assigning variable outside the function 
_a_global = 10

def a_function():
    _a_local = 4

    print("inside the function, the value _a_local is", _a_local)
    print("inside the function the value _a_global is", _a_global)

a_function()

print("outside the function the value _a_global is", _a_global)

# using the global keywoard to update variable values outside of the function 

_a_global = 10

print("Before calling a_function, outside the function, the value of _a_global is", _a_global)

def a_function():
    global _a_global
    _a_global = 5
    _a_local = 4
    
    print("Inside the function, the value of _a_global is", _a_global)
    print("Inside the function, the value _a_local is", _a_local)
    
a_function()

print("After calling a_function, outside the function, the value of _a_global now is", _a_global)

# global keywoard within a nest function

def a_function():
    _a_global = 10

    def _a_function2():
        global _a_global
        _a_global = 20
    
    print("Before calling a_function2, value of _a_global is", _a_global)

    _a_function2()
    
    print("After calling a_function2, value of _a_global is", _a_global)
    
a_function()

print("The value of a_global in main workspace / namespace now is", _a_global)

# IPMORTANCE OF RETURN DIRECTIVE

def modify_list1(some_list):
    print('got', some_list)
    some_list = [1,2,3,4]
    print('set to', some_list)

my_list = [1,2,3]
print('before, my_list=', my_list)

modify_list1(my_list)
print('after, my list =', my_list)

# original list remains the same, only gets changed inside the function

def modify_list2(some_list):
    print('got', some_list)
    some_list = [1,2,3,4]
    print('set to', some_list)
    return some_list

my_list = modify_list2(my_list)
print('after, my_list=', my_list)
# original list got changed by explicit replacement

def modify_list3(some_list):
    print('got', some_list)
    some_list.append(4) # actual mod of the list
    print('changed to', some_list)

my_list = [1,2,3]
modify_list3(my_list)
print('before, my_list=', my_list)
