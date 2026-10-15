#!/usr/bin/env R
# chloe.soudan26@imperial.ac.uk
# FIRST R FUNCTION

# a boilerplate script

myfunction <- function(arg1, arg2) {
    # statements involving the arguments
    # printing the type of arg1 and arg2
    print(paste("argument", as.character(arg1), "is a", class(arg1)))
    print(paste("argument", as.character(arg2), "is a", class(arg2)))
    
    return(c(arg1, arg2))
}

#testing the function
myfunction(1,2) # prints argument 1 is a numeric (same for 2)
myfunction("riki", "tiki") # prints arguments riki is a character (same for tiki)