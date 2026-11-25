### ERRORS AND DEBUGGING ###

## Trace the error trail
# define nested functions 
outer_function <- function(a) {
    middle_function(a)
}

middle_function <- function(b) {
    inner_function(b)
}

inner_function <- function(c) {
    # intentional error: division by zero
    result <- c / d
    return (result)
}

# call the outer function 
outer_function(1)

# note: error in inner_function(b): object 'd' not found
# did not automatically get the traceback so I called traceback() 

## Debugging using breakpoints 

# using the browser() function

Exponential <- function(NO = 1, r = 1, generations = 10) {
    # runs a simulation of exponential growth
    # returns a vector of length generations

    N <- rep(NA, generations) # creates a vector NA

    N[1] <- NO
    for (t in 2:generations {
        N[t] <- N[t-1] * exp(r)
        browser()
    }
    return (N)
}

plot(Exponential(), type = 'l', main="Exponential growth")

# ran browser.R for R console