# writing python code 

## testing/running blocks of code

x=11 

for i in range(x):
    if i>3:
        print(i)

## loops 

for i in range(10):
    print(i)

a = range(10)
a

#note: does not generate actual range of numbers

for i in range(1,6):
    print(i)
#note: only goes up to 5 

## iterator vs iterable

my_iterable=[1,2,3]
type(my_iterable)

my_iterator = iter(my_iterable)
type(my_iterator)

next(my_iterator)
next(my_iterator)
next(my_iterator)
next(my_iterator)