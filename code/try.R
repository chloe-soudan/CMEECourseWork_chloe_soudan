#!/usr/bin/env Rscript
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: try.R
# Desc: Practicing catching errors
# Date: Oct 2026

# Writing a function that involves sampling with replacement and takes mean from sample, only if sufficent samples were obtained
doit <- function(x) { 
    temp_x <- sample(x, replace = TRUE)
    if(length(unique(temp_x)) > 30) { #only takes mean if sample was sufficient (>30)
         print(paste("Mean of this sample was:", as.character(mean(temp_x)))) # print the mean of the temp x
        } 
    else {
        stop("Couldn't calculate mean: too few unique values!")
        }
    }

# generating a population
set.seed(1345) # again, to get the same result for illustration

popn <- rnorm(50)

hist(popn)

# trying to repeat sample exercises 15 times with lapply 
# (put # in front of line so that error does not occur when running script)

# lapply(1:15, function(i) doit(popn))
# note: script eventually failed because of the stop commmand 

# trying to repeat sample exercises 15 times but with try
result <- lapply(1:15, function(i) try(doit(popn), FALSE))
# note: got an error for one of the samples, but kept going 

class(result)
# output: list 

result

# Alternative: storing the results manually by using a loop
result <- vector("list", 15) #Preallocate/Initialize
for(i in 1:15) {
    result[[i]] <- try(doit(popn), FALSE)
    }

# ran the code block by block (in R environment), as well as fully in the terminal
# from the project root using the following command:
# Rscript code/try.R