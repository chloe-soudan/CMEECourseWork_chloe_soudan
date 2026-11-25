#!/usr/bin/env Rscript
# chloe.soudan26@imperial.ac.uk
# Descr: caculate tree heights from distance and angle measurements
# Script: TreeHeight.R
# Date: Oct 2026

##################
### 1. Loading the required libraries`
library(dplyr)

#######################
### 2. Loading the data
trees <- read.csv("data/trees.csv")
trees

##########################
### 3. inspecting header and few rows
head(trees)
str(trees)


##########################
#### 4. Data wrangling 

# setting Distance.m and Angle.degrees to be numeric
trees <- trees %>%
    mutate(
        Distance.m = as.numeric(Distance.m),
        Angle.degrees = as.numeric(Angle.degrees))

# performing checks 
num_col <- c("Distance.m", "Angle.degrees")

########################## 
### 5. Tree height function 
# Creating a function that calculates tree height from distance and angle measurements
TreeHeight <- function(Angle.degrees, Distance.m) {
    angle_radians <- Angle.degrees * pi / 180
    height_m <- Distance.m * tan(angle_radians)
    return(height_m)
}


####################################################
### 6. Wranlging and validating the data, and calculating tree height

# Creating a function that checks the data and calculates tree height
check_trees <- function(trees) { # creating a function
 
    col_order <- c("Species", "Distance.m", "Angle.degrees") # setting the column order # nolint

    if (!identical(names(trees), col_order)) { # checking that the columns are in the right order
        stop("wrong headers/ header order")}
       
    trees <- trees %>%
    mutate(
        Distance.m = as.numeric(Distance.m),
        Angle.degrees = as.numeric(Angle.degrees))
    num_col <- c("Distance.m", "Angle.degrees")
    
    for (col in num_col) {
        if (any(is.na(trees[[col]])))  { # checking for missing or non-numeric values 
            stop(paste("Missing or non-numeric values in", col))}  
        if (any(!is.finite(trees[[col]]))) { #checking if values are valid
            stop(paste("invalid", col))} }
    if (any(trees$Distance.m <= 0) || any(trees$Distance.m > 100)) { # checking the range
        stop("Distance.m out of range")}
    if (any(trees$Angle.degrees <= 0) || any(trees$Angle.degrees >= 90)) { # checking the range
        stop("Angle.degrees out of range")}
    
    trees <- trees %>% # calculating tree height
        mutate(height_m = TreeHeight(Angle.degrees, Distance.m)) %>%
        select(Species, Distance.m, Angle.degrees, height_m)
    message("done!") # adding a message to know that the tasks are done
    return(trees)
}

###########################
### 6. Testing the functions

## TreeHeight function 
toy_measurement <- 8 * tan(45 * pi / 180) 
toy_measurement
TreeHeight(45, 8) # should return 8
# note: both toy measurement and TreeHeight(45, 8) return 8, as expected
# check successful

## Check_trees function

# a. Column order
wrong_order <- trees[, c("Distance.m", "Angle.degrees", "Species")]
tryCatch(check_trees(wrong_order), error = function(e) print(e$message))
# returns "wrong headers/ header order", as expected
# column order check successful

# b. Column names
wrong_names <- trees
names(wrong_names) <- c("Species", "Distance", "Angle")
tryCatch(check_trees(wrong_names), error = function(e) print(e$message))
# returns "wrong headers/ header order", as expected
# column names check successful

# c.. Missing values
missing_values <- data.frame(
    Species = "Oak",
    Distance.m = "",
    Angle.degrees = "45")
missing_values <- missing_values %>%
    mutate( Distance.m = as.numeric(Distance.m),
        Angle.degrees = as.numeric(Angle.degrees))
tryCatch(check_trees(missing_values), error = function(e) print(e$message))
# returns "Missing or non-numeric values in Distance.m", as expected
# check successful

# d. Infinite values
infinite_values <- data.frame(
    Species = "Oak",
    Distance.m = Inf,
    Angle.degrees = 45)
tryCatch(check_trees(infinite_values), error = function(e) print(e$message))
# returns "invalid Distance.m", as expected 
# infinite values check successful

# e. Non-numeric values
non_numeric_values <- data.frame(
    Species = "Oak",
    Distance.m = 50,
    Angle.degrees = "abc")
non_numeric_values <- non_numeric_values %>%
    mutate(
        Distance.m = as.numeric(Distance.m),
        Angle.degrees = as.numeric(Angle.degrees))
tryCatch(check_trees(non_numeric_values), error = function(e) print(e$message))
# returns "Missing or non-numeric values in Angle.degrees", as expected
# missing and non-numeric values check successful

# f. Out of range distance_m

# just outside of lower boundary
dist_out_of_range1 <- data.frame(
    Species = "Oak",
    Distance.m = 0,
    Angle.degrees = 45)
tryCatch(check_trees(dist_out_of_range1), error = function(e) print(e$message))
# returns "Distance.m out of range", as expected

# just within upper boundary
dist_out_of_range2 <- data.frame(
    Species = "Oak",
    Distance.m = 100,
    Angle.degrees = 45)
tryCatch(check_trees(dist_out_of_range2), error = function(e) print(e$message))
# returns the data frame with the calculated height, as expected (record was valid)

# just outside upper boundary
dist_out_of_range3 <- data.frame(
    Species = "Oak",
    Distance.m = 101,
    Angle.degrees = 45)
tryCatch(check_trees(dist_out_of_range3), error = function(e) print(e$message))
# returns "Distance.m out of range", as expected

# distance range check successful
# g. Out of range angle_degrees

# just outside of lower boundary
angle_out_of_range1 <- data.frame(
    Species = "Oak",
    Distance.m = 50,
    Angle.degrees = 0)
tryCatch(check_trees(angle_out_of_range1), error = function(e) print(e$message))
# returns "Angle.degrees out of range", as expected

# just within upper boundary
angle_out_of_range2 <- data.frame(
    Species = "Oak",
    Distance.m = 50,
    Angle.degrees = 89)
tryCatch(check_trees(angle_out_of_range2), error = function(e) print(e$message))
# returns the data frame with the calculated height, as expected (record was valid)

# just outside upper boundary
angle_out_of_range3 <- data.frame(
    Species = "Oak",
    Distance.m = 50,
    Angle.degrees = 90)
tryCatch(check_trees(angle_out_of_range3), error = function(e) print(e$message))
# returns "Angle.degrees out of range", as expected

# angle range check successful


###########################
### 7. Running the function and inspecting the results

# running the function on the trees data 
trees_height <- check_trees(trees) 
# inspecting the output
head(trees_height)
str(trees_height)
dim(trees_height)
# note: the output has 120 rows and 4 columns
# output looks as expected 

###################################
### 9. Writing the results into a csv file

# writing the results into a csv
write.csv(trees_height, "results/TreeHts.csv", row.names = FALSE)
# note: write.csv overwrites file if already exists by default

# ran the code in the bash terminal from project root with following command:
# RScript code/TreeHeight.R

# counted the lines usng wc -l results.TreeHts.csv, which return 121 lines (header + 120 data rows)
# looked at the first few rows using: head results/TreeHts.csv
# columns were in some order as input

# checked height measurement of 'Populus tremula'
#
if (round(trees_height$height_m[1], digits = 1) == 
round(31.66583 * tan(41.28264 * pi /180), digits =1)) {
    print("correct height") } else {
        print("wrong height")}

#printed "correct"
