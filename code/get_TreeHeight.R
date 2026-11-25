
#!/usr/bin/env Rscript
# chloe.soudan26@imperial.ac.uk
# Descr: Generalize the tree height script to accept a CSV file as an argument and output a CSV file with calculated tree heights
# Script: get_TreeHeight.R
# Date: Oct 2026


###################
### 1. Loading the required libraries
library(tidyverse) 

####################
### 2. Importing functions from TreeHeight.R
source("code/TreeHeight.R")

###################
### 3. Definining the args function 

# Definign the functions to use commadArgs to accept only one CSV file
args <- commandArgs(trailingOnly = TRUE) # storing the arguments as args

if (length(args) == 0) {  # checking that an argument is provided
    stop("No argument provided")
}

if (length(args) > 1) { # checking thay not more that one argument is provided
    stop("Too many arguments provided")
}

if (!file.exists(args[1]) || dir.exists(args[1])) { # checking that the file exists
    stop("Missing file")
}

if (file.access(args[1], 4) != 0) { # checking that the file is readable
    stop("File is not readable")
}


###################
### 4. Loading the input CSV file and inspecting it

# reads argument as a csv an stores it as trees1
trees1 <- read.csv(args[1])

# inspecting trees1
head(trees1)

######################
### 5. Reusing input checks from TreeHeight.R script

trees_height1 <- check_trees(trees1) # running the check_trees function on trees1   


#####################
### 6. Inspecting the results
head(trees_height1)
str(trees_height1)
dim(trees_height1)


#####################
### 8. Writing the results into a csv file

# creating a resuls folder if it doesn't exist yet
dir.create("results", showWarnings = FALSE)

# creating a file name for the output csv file based on the input file name
filename <- tools:: file_path_sans_ext(basename(args[1]))
write.csv(trees_height1, paste0("results/", filename, "_treeheights.csv"),
row.names = FALSE) 


# checked height calculation with browser():
# added browser before the trees <- trees %>% etc
# this opened the browser mode (Browser[1] > )
# I checked for Distance.m (31.665), and Angle.degrees (41.28264)
# i then calculated height manually and ont the terminal using n, results were the same
# i then removed browser() from my code

