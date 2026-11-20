
def buggyfunc(x):
    y =x
    for i in range(x):
        y = y-1
        z = x/y
    return z

buggyfunc(20)
# ran it with python3 code/debugme.py
# note: most recent call last, what was the call that led to the error 

# turning on python debugger (%pdb)
# running it again %run code/debugme.py




### HANDLING EXPECTED ERRORS 
# using %cpaste in ipython3, ran:

def buggyfunc(x):
    y = x
    for i in range(x):
        try: 
            y = y-1
            z = x/y
        except:
            print(f"This didn't work;{x = }; {y = }")
    return z

buggyfunc(20)


#output: This didn't work; x = 20; y =0 
# tried (try) to do y = y-1 and z = x/y but didn't work so it went to except command

## catch specific errors 
def buggyfunc(x):
    y = x
    for i in range(x):
        try: 
            y = y-1
            z = x/y
        except ZeroDivisionError:
            print(f"The result of dividing a number by zero is undefined")
        except:
            print(f"This didn't work;{x = }; {y = }")
        else:
            print(f"OK; {x = }; {y = }, {z = };")
    return z

buggyfunc(20)

# note: output was a bunch of lines starting with OK, except the last one
# that stated "the result of divding a nu,ber by zero is undefined"
