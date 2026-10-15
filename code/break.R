#!/usr./bin/env R
# chleo.soudan26@imperial.ac.uk
# SOME MORE CONTROL FLOW TOOLS

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

#############
### using next

for (i in 1:10) {
  if ((i %% 2) == 0) # if i is even
    next # pass to next iteration of loop 
  print(i)
}
# note: printed all the odd values of the range