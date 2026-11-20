################################################################
################## Wrangling the Pound Hill Dataset ############
################################################################

############# Load the dataset ###############
# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("../data/pound_hill_data.csv", header = FALSE))

# header = true because we do have metadata headers
MyMetaData <- read.csv("../data/pound_hill_meta_data.csv", header = TRUE, sep = ";")

############# Inspect the dataset ###############
head(MyData) # looking at the first rows of MyData
dim(MyData) # MyData has dimension of 45 x 60 
str(MyData) # looking at the classes of Myata columns
fix(MyData) # opens MyData as a matrix in a different windw
fix(MyMetaData)

############# Transpose ###############
# To get those species into columns and treatments into rows 
MyData <- t(MyData) # transposed columns and rows 
head(MyData)
dim(MyData) # dimensions are now 60x45

############# replace species absences with zeros ###############
MyData[MyData == ""] = 0

############# Convert raw matrix to data frame ###############

TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F) #stringsAsFactors = F is important!
colnames(TempData) <- MyData[1,] # assign column names from original data

############# Convert from wide to long format  ###############
require(reshape2) # load the reshape2 package
# note: error message saying there was no reshape2 package installed

# install reshape2
install.packages("reshape2")
# load reshape2
library(reshape2)

?melt #check out the melt function
# note: melt converts an object into a molten data frame 

MyWrangledData <- melt(TempData, id=c("Cultivation", "Block", "Plot", "Quadrat"), variable.name = "Species", value.name = "Count")

MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])
MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])
# note: setting the class of columns to be facotr or integer  

str(MyWrangledData) # verifying that class change was succesfull: it was
head(MyWrangledData)
dim(MyWrangledData) # dimensions: 2419x6

############# Exploring the data (extend the script below)  ###############

# installing tidyverse
install.packages("tidyverse")

# oading the tidyverse library 
libvrary(tidyverse)

tidyverse_packages(include_self = TRUE) # the include_self = TRUE means list "tidyverse" as well 
# should show the packages included in tidyverse, did not work 
# convert data from data frame to "tibble"
MyWrangledData <- dplyr::as_tibble(MyWrangledData) # dyplr:: calls for the dplyr package
# note: dplyr:: was not necessary, could have just rand as_tibble()
MyWrangledData
class(MyWrangledData)
# class: "tbl_df" "tbl" "data.frame"

# 
glimpse(MyWrangledData)

# make subset keeping only counts higher than 100 
filter(MyWrangledData, Count > 100) 

# look at specific range (row 10-15)
slice(MyWrangledData, 10:15)

# try %>% pipeline (for which)
MyWrangledData %>% # my data where counts are grouped by species
    group_by(Species) %>% # and for which 
        summarise(avg = mean(Count)) # avg is the avg count for each Species group
# note: same as this (in base R): aggregate(MYWrangledData$Count, list(MYWrangledData$Species), FUN=mean)