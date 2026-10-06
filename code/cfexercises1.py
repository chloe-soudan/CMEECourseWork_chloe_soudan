### FUNCTIONS EXERCISES ###

def foo_1(x):
    return x **0.5
#defining a function foo_1 that return x to the power of 0.5
foo_1(2) # will return 2 to the power of 0.5
# 1.41 

def foo_2(x,y):
    if x>y:
        return x
# defining a function foo_2 that returns x when x is a higher value than y
foo_2(1,2)  #will return nothing because 1(x) is not bigger than 2(y)
# returned nothing
foo_2(2,1) # will return 2(x), because 2(x) is bigger than 1(y)
# returned 2

def foo_3(x, y, z):
    if x > y:
        x, y = y, x # if x is bigger than y, swap x and y
    if x > z: 
        x, z = z, x # if x is bigger than z, swap x and z
    if y > z: 
        y, z = z, y # if y is bigger than z, swap y and z
    return [x, y, z]

foo_3(1,2,3) # will return [1,2,3] because x is not bigger than y, x is not bigger than z, and y is not bigger than z
#returned [1,2,3]
foo_3(3,2,1) # will return [1,2,3] because all the conditions are met and thus the order is swapped around
#returned [1,2,3]
#note: was having indentation errors, so used %cpaste

def foo_4(x):
    result = 1 #starting with result =1
    for i in range (1,x+1):
        result = result * i # for a range of 1-x (including x), the result equals the previous result (starting result is 1) times the iteration
    return result

foo_4(3) # 1*1, 2*1, 3*2 => will return 6
# returned 6
foo_4(4) #1*1 =1, 2*1 =2 , 3*2 =6. 4*6 = 24 => will return 24
#returned 24
# note: was having indentation errors so used %cpaste

def foo_5(x):
    if x <1:
        return 1 # handling the 0! issue
    if x ==1:
        return 1 # if x equals 1 return 1
    return x*foo_5(x-1) #if else, return x times the result of this function for x-1
foo_5(2) #1, 2*1 =2  => will return 2
#returned 2
foo_5(3) # 1, 2*1 =2, 3*(2*1)*1 =6 => will return 6
# returned 6
foo_5(4) #  4* foo_5(3) = 4*6  24 => will return 24
# note: was having some indentation issues so used %cpaste

def foo_6(x):
    facto =1 #starting facto equals 1
    while x >=1: # when x is equal to or bigger than 1 
        facto = facto*x #facto equals facto from previous iteration times x
        x = x-1 #substracting 1 from x, and keep loop going 
    # with x-1 until x >= 1 condition returns false
    return facto

foo_6(1) #1*1 = 1 => will return 1 
# returned 1
foo_6(2) # 1*2 =2 => will return 2
# returned 2
foo_6(3) # (1*3)*(2*1) = 6 => will return 6
# returned 6
foo_6(4) # (4*1)*(4*3)*(3*2)*(2*1) = 24 => will return 24
# returned 24

