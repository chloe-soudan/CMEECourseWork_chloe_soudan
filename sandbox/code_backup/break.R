#!/usr/bin/env Rscript
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: break.R
# Desc: Some more control flow tools
# Date: Oct 2026


###########
### breaking out of loops

i <- 0 # starting value of i set to 0
    while (i < Inf) { # as long as i is smaller than infinity
        if (i ==10) {
        break # if i = 10, then break the code
    } else { # breaking out of the while loop
        cat ("i equals", i, "\n")
        i <- i +1 # updating i to i +1 
    }
}
# note: runs the code until 10, that's where it's told to break, 
# so it goes until i equals 9

# ran the code block by block (in R environment) , and then fully by running Rscript code/break.R 
# in the bash terminal (from the project root)