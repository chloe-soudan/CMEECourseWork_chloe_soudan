
# script illustrating file input and output

mydata <- read.csv("data/trees.csv", header = TRUE)

# writingcontaining my data
write.csv(mydata, "results/mydata.csv")
# appending to a column to it
write.table(mydata[1, ], file = "results/mydata.csv", append = TRUE)
# writing row names
write.csv(mydata, "results/mydata.csv", row.names = TRUE) 
# omitting column names 
write.table(mydata, "results/mydata.csv", col.names = FALSE)

print("Script complete")