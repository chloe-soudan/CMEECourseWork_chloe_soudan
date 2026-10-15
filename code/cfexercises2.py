### MORE EXAMPLES OF LOOPS AND CONDITIONALS COMBINED ###

def hello_1(x): # defining hello_1 to be a fucntion where  
    for j in range(x): # for each iteration(j) in range x 
        if j % 3 ==0: # if  the remainder after division of j by 3 is 0
            print('hello') # then print 'hello'
        print (' ') # and print ' ' at the end of each iteration

hello_1(12) # will print hello followed by a space 4 times 
# printed hello followed by a space 4 times
hello_1(13) # will print hello followed by space five times

#############

def hello_3(x,y):
    for i in range(x,y):
        print('hello')
    print(' ')
# for each iteration within the range 3(included) to 17 (not included), print hello, with a space between each iteration

hello_3(3,17) # will print hello 14 times
hello_3(2,5) # will print hello 3 times 

#############

def hello_4(x):
    while x != 15:
        print('hello')
        x=x+3
    print(' ')
# as long as x is not equal to 15 print 'hello' 

hello_4(0) # will print hello 5 times, after 5 iterations x will be euqla to 15 and thus the condition is not met anymore

###################

def hello_5(x): # defining a function where
    while x < 100: # as long as x is smaller than 100
        if x == 31: # when x is equal to 31, print 'hello' 7 times
            for k in range(7):
                print('hello') 
        elif x == 18: # when x is 18, print 'hello'
            print('hello')
        x = x + 1 # increasing x by 1 at each iteration
    print(' ') # print ' ' at the end of each iteration

hello_5(12) # will print hello 8 times 

### while loop with break ###
def hello_6(x,y):
    while x: #while x is true
        print('hello!' + str(y))
        y +=1 # increment y by 1 at each iteration
        if y == 6:
            break
    print(' ')

hello_6(True, 0) # will print hello!5 times (until y =6) followed by the y value