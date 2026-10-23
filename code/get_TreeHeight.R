#!/usr/bin/env R
# chloe.soudan26@imperial.ac.uk
# GENERALIZE TREE-HEIGHT SCRIPT PRACTICAL


library(tidyverse) 

# using commandArgs to only accept one readable CSV path

args <- commandArgs(trailingOnly = TRUE) # storing the arguments as args

if (length(args) == 0) {  # checking that an argument is provided
    stop("No argument provided")
}

if (length(args) > 1) { # checking thay not more that one argument is provided
    message <- "Too many arguments provided"
}

if (!file.exists(args[1])) { # checking that the file exists
    message <- "Missing file"
}


# reads argument as a csv an stores it as trees1
trees1 <- read.csv(args[1])

# inspecting trees1
head(trees1)

# reusing the function from TreeHeight.R

num_col <- c("Distance.m", "Angle.degrees")
check_trees1 <- function(trees) { # creating a function
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

# running the function
trees_height1 <- check_trees1(trees1)

# writing the output in a csv

basename <- tools:: file_path_sans_ext(basename(args[1]))
write.csv(trees_height1, paste0("results/", basename, "_treeheights.csv"))

# note: asked AI to give me hint on how to tackle this, which led me to this webstie:
# https://maple60.github.io/en/posts/2026-02-06-r-extract-filename/
# asked AI for hint to remove.csv after basename, it suggeste tools::file_path_sans_ext

# checked height calculation with browser():
# added browser before the trees <- trees %>% etc
# this opened the browser mode (Browser[1] > )
# I checked for Distance.m (31.665), and Angle.degrees (41.28264)
# i then calculated height manually and ont the terminal using n, results were the same
# i then removed browser() from my code