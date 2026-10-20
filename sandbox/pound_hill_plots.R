#!/usr/bin/env R
# chloe.soudan26@imperial.ac.uk
# POUND HILL DATA WRANGLING AND PLOTTING


# starting from root project directory

# load the dataset
MyData <- as.matrix(read.csv("data/pound_hill_data.csv", header = FALSE))

# load the metadata, header = true because we do have metadata headers
MyMetaData <- read.csv("../data/pound_hill_meta_data.csv", header = TRUE, sep = ";")

# inspect the data set
head(MyData) 
str(MyData)
dim(MyData) # 45x60

# transpose the data set
# To get those species into columns and treatments into rows 
MyData <- t(MyData) # transposed columns and rows 
head(MyData)
dim(MyData) # dimensions are now 60x45

# replace species absences with zeros
MyData[MyData == ""] = 0

# Convert raw matrix to data frame 
TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F) #stringsAsFactors = F is important!
colnames(TempData) <- MyData[1,] # assign column names from original data

## Convert from wide to long format  ################ Convert from wide to long format 
# sources: https://www.geeksforgeeks.org/r-language/pivot-longer-in-r/
# https://gist.github.com/ramhiser/93fe37be439c480dc26c4bed8aab03dd
library(tidyverse)

MyData <- TempData %>%
    pivot_longer(
        cols = -c("Cultivation", "Block", "Plot", "Quadrat"),
        names_to = "Species",
        values_to = "Count")

MyWrangledData <- MyData %>%
    mutate(
        Cultivation = as.factor(Cultivation), 
        Block = as.factor(Block),
        Plot = as.factor(Plot),
        Quadrat = as.factor(Quadrat),
        Count = as.integer(Count)) 

# reinspecting the data 

str(MyWrangledData) # verifying that class change was succesfull: it was
head(MyWrangledData)
dim(MyWrangledData) # dimensions: 2419x6

 
# convert data from data frame to "tibble"
MyWrangledData <- as_tibble(MyWrangledData) 


# grouping counts by species, taking the average count for each species
MyWrangleData_avg <- MyWrangledData %>% 
    group_by(Species) %>% 
        summarise(avg = mean(Count)) 
# note: same as this (in base R): aggregate(MYWrangledData$Count, list(MYWrangledData$Species), FUN=mean)

MyWrangleData_avg

# exporting the table of average counts per species as a csv to results/
write.csv(MyWrangleData_avg, "results/pound_hill_avg_species_count.csv")

## plotting the pound hill data
# do distributions of species abundance differ among march, may, october
data <- MyWrangledData

par(mfcol=c(3,1))
par(mfg =c(1,1))

# making base-R histogram for the three months
#march
data_march <- data[data$Cultivation == "march", ]
hist(data_march$Count)
#may
data_may <- data[data$Cultivation == "may", ]
hist(data_may$Count)
#october
data_october <- data[data$Cultivation == "october", ]
hist(data_october$Count)

# recreating with ggplot
library(ggplot2)

march <- ggplot(data_march, aes(x =Count)) + geom_histogram()
march

may <- ggplot(data_may, aes(x =Count)) + geom_histogram()
may

october <- ggplot(data_october, aes(x =Count)) + geom_histogram()
october

comparison_data <- data[data$Cultivation %in% c("march", "may", "october"), ]

pdf("../results/count_frequency_plot.pdf",
    11.7, 8.3)

library(gpglot2)
comparison_data <- data[data$Cultivation %in% c("march", "may", "october"), ]


comparison_plot <- ggplot(comparison_data, aes(x = Count, fill = Cultivation)) +
  geom_histogram(bins = 10, colour = "black") +
  facet_wrap(~ Cultivation) +
  labs(
    title = "Plot of the frequency of counts of individuals per species per quadrat",
    x = "Individuals per species per quadrat",
    y = "Frequency"
  ) + 
  theme_bw()

comparison_plot

graphics.off()