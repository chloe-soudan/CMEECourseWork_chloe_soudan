#!/usr/bin/env Rscript
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: next.R
# Desc: Some more control flow tools
# Date: Oct 2026


#############
### using next to skip to the next iteration
# function that prints all odd values in a range (1:10)
for (i in 1:10) {
  if ((i %% 2) == 0) # if i is even
    next # pass to next iteration of the loop 
  print(i)
}
# note: printed all the odd values of the range

# ran the code block by block (in R environment) , and then fully by running Rscript code/break.R 
# in the bash terminal (from the project root)