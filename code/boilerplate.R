#!/usr/bin/env Rscript
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: boilerplate.R
# Desc: Function practice
# Date: Oct 2026

# a boilerplate script

myfunction <- function(arg1, arg2) { # creating a function that uses 2 arguments as inputs
    # statements involving the arguments
    # printing the type of arg1 and arg2
    print(paste("argument", as.character(arg1), "is a", class(arg1)))
    print(paste("argument", as.character(arg2), "is a", class(arg2)))
    
    return(c(arg1, arg2)) # returns both arguments
}

#testing the function
myfunction(1,2) # prints argument 1 is a numeric (same for 2), and returns 1 2 (both arguments)
myfunction("riki", "tiki") # prints arguments riki is a character (same for tiki), and returns riki riki (both arguments)

# ran the code from the project root using the following command:
# Rscript code/boilerplate.R