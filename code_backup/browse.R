#!/usr/bin/env Rscript
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: browse.R
# Desc: Practicing using the browser() function
# Date: Oct 2026


# using the browser() function

Exponential <- function(N0 = 1, r = 1, generations = 10) {
    # runs a simulation of exponential growth
    # returns a vector of length generations

    N <- rep(NA, generations) # creates a vector NA

    N[1] <- N0
    for (t in 2:generations) {
        N[t] <- N[t-1] * exp(r)
        browser()
    }
    return (N)
}

plot(Exponential(), type = "l", main ="Exponential growth")

# ran source("code/browse.R") from R console, which returned
# Called from: Exponential () and Browse[1]>
# examined the varuables using n, c, Q, and ls()
# ls() returned "generations", "N", "N0", "r", and "t"

