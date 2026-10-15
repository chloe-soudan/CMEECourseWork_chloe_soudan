#!/usr/bin/env R
# chloe.soudan@imperial.ac.uk
# CONTROL FLOW TOOLS

#################
#### if statements 
a <- TRUE
if (a) {
    print("a is TRUE")
} else {
    print ("a is FALSE")
}
# note: printed "a is TRUE"

# writing if statement on a single line
z <- runif(1) # generating uniformly distributed random number
if (z <=0.5) {print ("less than half")}
# note: not optimal for readibility so avoid doing that 


##############
#### for loops
for (i in 1:10) { # for values (i) in a range of 1 to 10
    j  <- i *i # set j to be the square of the value i 
    print(paste(i, "square is", j))
}

# looping over a vecotr of strings 
for (species in c('Heliodoxa rubinoides', 'Boissonneaua jardini',
'Sula nebouxii')) {
    print(paste('the species is', species))
}
# note:prints three lines each naming the species

# loop for vector
v1 <- c("a", "bc", "def")
for (i in v1) { 
    print(i)
}
# note: printed "a", "bc", "def"

##########
### while loops

# running an operation until a condition is met
i <- 0 #starting value of i is 0
while(i < 10) { # as long as i is smaller than 10
    i <- i+1 # i becomes i+1
    print(i^2) # and then i square gets printed
}
# note: highest squared value is 100 (i ould have been 9, become 10, and been squared
# becasue i would then not have been smaller than 10 anymore, then next iteration 
# was not executed (condition not met anymore)
