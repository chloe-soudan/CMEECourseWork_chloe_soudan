#!/usr/bin/env Rscript
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: r_conditionals.R
# Desc: Practicing conditionals in R (if statements)
# Date: Oct 2026

#### 1. Checking in an integer is even 
is.even <- function(n) {  # creating a function with input n
    if(n %% 2 == 0) { # if the remainder of n divided by 2 is 0,
        return(paste(n,'is even!')) #return 'n is even!'
    } else { # otherwhise,
        return(paste(n,'is odd!')) # return 'n is odd!'
    }
}

is.even(6)
# output: "6  is even!" (as expected)

#### 2. Checking if a number is a power of 2
is.power2 <- function(n) {
  if (log2(n) %% 1==0) { # checks if the remainder of log2 of n is 0 (means that it is power of 2)
    return(paste(n, 'is a power of 2!')) 
  } else {
  return(paste(n,'is not a power of 2!'))
    }
}

is.power2(4)
# output: "4 is a power of 2!" (as expected)

#### 3. Checking if a number is prime
is.prime <- function(n) {
  if (n==0) { # checks if n is 0
    return(paste(n,'is a zero!'))
  } else if (n==1) { # checks if n is 1
    return(paste(n,'is just a unit!'))
  }
    
  ints <- 2:(n-1) # setting ints to be a range from 2 to n-1
  
  if (all(n%%ints!=0)) { # if the division of n by each value in ints is different than 0 (prime number) 
    return(paste(n,'is a prime!')) # return 'n is prime!'
  } else { # otherwise, return 'n is a composite!'
  return(paste(n,'is a composite!'))
    }
}

is.prime(3)

# output: "3 is prime!" (as expected)

# ran the code block by block and ran it with source() and Rscript