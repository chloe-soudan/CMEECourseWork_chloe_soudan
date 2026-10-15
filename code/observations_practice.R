#!/usr/bin/env R
# chloe.soudan26@imperial.ac.uk
## GUIDED: VALIDATE BEFORE CALCULATING

# writing a read_observations(path) function

observations <- read.csv(
    "data/bootcamp_observations.csv", 
colClasses = "character", na.strings = "",
check.names = FALSE
)

str(observations)
print(observations)
# columnds are site, data, and count
# every row has site and date
# empty counts marked by <NA>


# checking columns

read_observations <- function(observations) {
    # checking columns
column_order <- c("site", "date", "count") #setting the expected col order  
if (identical(colnames(observations), column_order)) {
    print("correct column order")} else {
        stop("error: columns in wrong order")}
    # rejecting empty sites or dates 
    #https://statisticsglobe.com/r-is-na-function/
if(any(is.na(observations$site)) ||
any(is.na(observations$date))) {
    stop("error: empty sites or dates")
    } else {
        print("no missing dates or sites")}
    # checking if there are <NA> coutnsm and if there are, removing 
    # rows where count is <NA>
if (any(is.na(observations$count))) {
    observations <- observations[!is.na(observations$count),] }
    # using the grepl on each non-missing value
if (any(!grepl("^(0|[1-9][0-9]*)$", observations$count))) {
    stop("error: wrong values in non-missing counts")}
    # converting to integer 
observations$count <- as.integer(observations$count)

return(observations)
}

read_observations(observations)

# running the function with bootcamp_observations_invalid.csv

observations <- read.csv("data/bootcamp_observations_invalid.csv")
observations
read_observations(observations)
# task got stopped because there was a wrong value (-1) in the non-missing counts