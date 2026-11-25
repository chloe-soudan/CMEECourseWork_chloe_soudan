#!/usr/bin/env Rscript
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: observations_practice.R
# Desc: Practice with observations data
# Date: Oct 2026

# Writing a read_observations(path) function
observations <- read.csv(
    "data/bootcamp_observations.csv", 
colClasses = "character", na.strings = "",
check.names = FALSE)

str(observations)
print(observations)

# note: columnds are site, data, and count
# note: every row has site and date
# note: empty counts marked by <NA>

# Writing a read_observations function that checks the format, column order, etc of the observations
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
    # checking if there are <NA> countsm and if there are, removing 
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

# Running the function with bootcamp_observations_invalid.csv
# (put # in front the the command lines so that script doesn't stop here when running it fully)
#observations_invalid <- read.csv("data/bootcamp_observations_invalid.csv")
#observations_invalid
#read_observations(observations_invalid)
# task got stopped because there was a wrong value (-1) in the non-missing counts

####################
# Writing summarise_observations(data) function

# total_known (sum of non-missing counts)
# missing_count (sum of missing_counts)
# removing duplicated rows (from https://stackoverflow.com/questions/13967063/remove-duplicated-rows)

summarise_observations <- function(observations) {
     # removing duplicated rows (from https://stackoverflow.com/questions/13967063/remove-duplicated-rows)
    
    observations <- observations[!duplicated(observations), ]
    # finding unique sites
    sites <- unique(observations$site)

    results <- list() # creating a list in which to store the results

    for (site in sites) { # looping through each unique site
        # creating objects that will sotre the counts, and setting them to 0
        total_known = 0  
        missing_counts = 0
        known_count = 0
        
        # going through each row in observations
        for (row in 1:nrow(observations)) {
            if (observations$site[row] == site) { #if the row's site is the site currently being analyse
                count <- as.numeric(observations$count[row]) # conver count to numeric
                
                if(is.na(count)) { # if count is NA,
                     missing_counts <- missing_counts + 1 # add 1 to missing count object
                } else { #otherwise, add the count to the total known object
                    total_known <- total_known + count
                    known_count <- known_count +1
                }
            }
        }
        
        # setting known_total to be None if there are no known counts
        if (known_count == 0) {
            total_known <- None
        }
        results[[site]] <- c(total_known, missing_counts)
    }
    results <- as.data.frame(results)
    #naming the results columns
    rownames(results) <- c("total_known", "missing_count")
    return (results)
}

results <- summarise_observations(observations)
results
# Output:
#                A B
# total_known    2 0
# missing_count  1 0

# writing a stopifnot()

stopifnot(
    all(results$A == c(2, 1)),
    all(results$B == c(0, 0)))


