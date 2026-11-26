#!/usr/bin/env Rscript
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: basic_io.R
# Desc: Reading data, modifying it, and writing a csv file output
# Date: Oct 2026

# Script illustrating file input and output

MyData <- read.csv("data/trees.csv", header = TRUE)

# creating results folder of it doesn't already exist
dir.create("results", showWarnings = FALSE)

# writingcontaining my data
write.csv(MyData, "results/MyData.csv")
# appending a column to it
write.table(MyData[1, ], file = "results/MyData.csv", append = TRUE)
# writing row names
write.csv(MyData, "results/MyData.csv", row.names = TRUE) 
# omitting column names
write.table(MyData, "results/MyData.csv", col.names = FALSE)

print("Script complete")

# ran the file in the terminal from the project root (CMEECoursework) by using the following command:append
# Rscript code/basic_io.R
# output: script ran. results files where in the results folder, 
# and printed the "complete" message