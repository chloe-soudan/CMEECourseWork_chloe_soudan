#!/usr/bin/env R
# chloe.soudan26@imperial.ac.uk
# CALCULATE TREE HEIGHTS PRACTICAL 
library(dplyr)

trees <- read.csv("data/trees.csv")
trees
# inspecting header and few rows
head(trees)
str(trees)

trees <- trees %>%
    mutate(
        Distance.m = as.numeric(Distance.m),
        Angle.degrees = as.numeric(Angle.degrees))

check_trees <- function(trees) {
    col_order <- c("Species", "Distance.m", "Angle.degrees")

    if (!identical(names(trees), col_order)) {
        message <- "wrong headers/ header order"
    }
    if (any(is.na(trees$Distance.m) | trees$Distance.m == "")) {
        message <- "Missing Distance.m"}
    if (any(is.na(trees$Angle.degrees) | trees$Angle.degrees == "")) {
        message <- "Missing Angle.degrees"}
    if (any(trees$Distance.m < 0) | any(trees$Distance.m > 100)) {
        message <- "Distance.m out of range"}
    if (any(trees$Angle.degrees < 0) | any(trees$Angle.degrees >= 90)) {
        message <- "Angle.degrees out of range"}
    if (any(!is.finite(trees$Distance.m))) {
            message <- "Invalid Distance.m"} 
    if (any(!is.finite(trees$Angle.degrees))) {
            message <- "Invalid Angle.degrees"} 
    trees <- trees %>%
        mutate(height_m = Distance.m *tan(Angle.degrees * pi /180))
    select(Species, Distance.m, Angle.degrees, height_m)
    message("done!")
    return(trees)
}

trees_height <- check_trees(trees)
head(trees_height)
str(trees_height)
dim(trees_height)

# writing the results into a csv
write.csv(trees_height, "results/TreeHts.csv")

# ran the code in the bash terminal from project root with following command:
# RScript code/TreeHeight.R
# counted the lines usng wc -l results.TreeHts.csv, which return 121 lines (header + 120 data rows)
# looked at the first few row using: head results/TreeHts.csv

# checked height measurement of 'Populus tremula'
if (
    round(trees_height$height_m[1], digits = 1) == 
    round(31.66583 * tan(41.28264 * pi /180), digits =1)
) {
    print("correct") 
} else {
    print("wrong height")
}
# prints "correct"
# asked AI to help with correcting indents
#

trees_height[1,]
trees_height$height_m[1]



# sources: https://www.statology.org/r-filter-between-two-values/
# https://dplyr.tidyverse.org/reference/filter.html

# sources:
# if row missing https://www.geeksforgeeks.org/r-language/address-errors-in-if-statements-in-r/
# ordering columns: https://www.geeksforgeeks.org/r-language/reorder-the-column-of-dataframe-in-r-using-dplyr/

# the toy thing??
# readme.md stuff