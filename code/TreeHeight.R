#!/usr/bin/env Rscript
# chloe.soudan26@imperial.ac.uk
# CALCULATE TREE HEIGHTS PRACTICAL


library(dplyr)

# loading the data
trees <- read.csv("data/trees.csv")
trees

# inspecting header and few rows
head(trees)
str(trees)

# setting Distance.m and Angle.degrees to be numeric
trees <- trees %>%
    mutate(
        Distance.m = as.numeric(Distance.m),
        Angle.degrees = as.numeric(Angle.degrees))

# performing checks 

num_col <- c("Distance.m", "Angle.degrees")

check_trees <- function(trees) { # creating a function
    col_order <- c("Species", "Distance.m", "Angle.degrees") # setting the column order
    if (!identical(names(trees), col_order)) { # checking that the columns are in the right order
        stop("wrong headers/ header order")}
    
    for (col in num_col) {
        if (any(is.na(trees[[col]]) | trees[[col]] == "")) { # checking for missing values 
            stop(paste("missing", col))} 
        if (any(!is.finite(trees[[col]]))) { #checking if values are valid
            stop(paste("invalid", col))} }
    if (any(trees$Distance.m < 0) | any(trees$Distance.m > 100)) { # checking the range
        stop("Distance.m out of range")}
    if (any(trees$Angle.degrees < 0) | any(trees$Angle.degrees >= 90)) { # checking the range
        stop("Angle.degrees out of range")}
    
    trees <- trees %>% # calculating tree height
        mutate(height_m = Distance.m *tan(Angle.degrees * pi /180)) %>%
        select(Species, Distance.m, Angle.degrees, height_m)
    message("done!") # adding a message to know that the tasks are done
    return(trees)
}

# sources: https://www.w3schools.com/r/r_for_loop.asp

# running the function on the trees data 
trees_height <- check_trees(trees) 
# inspecting the output
head(trees_height)
str(trees_height)
dim(trees_height)

# writing the results into a csv
write.csv(trees_height, "results/TreeHts.csv")
# note: write.csv overwrites file if already exists by default

# ran the code in the bash terminal from project root with following command:
# RScript code/TreeHeight.R
# counted the lines usng wc -l results.TreeHts.csv, which return 121 lines (header + 120 data rows)
# looked at the first few rows using: head results/TreeHts.csv
# columns were in some order as input

# checked height measurement of 'Populus tremula' from porject root:
#if (round(trees_height$height_m[1], digits = 1) == 
#    round(31.66583 * tan(41.28264 * pi /180), digits =1)
#) {
#    print("correct height") 
#} else {
#    print("wrong height")
#}
# printed "correct"

# forming a toy measurement to double-check the formula
toy_measurement <- 8 * tan(45 * pi / 180) 
toy_measurement

# note: output is 8 (as expected)

