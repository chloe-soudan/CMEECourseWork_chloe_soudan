#!/usr/bin/env Rscript
# chloe.soudan26@imperial.ac.uk
# POUND HILL PRACTICAL

# installing and loading libraries 
install.packages("ggplot2")
install.packages("tidyverse")
install.packages("languageserver")
library(languageserver)
library(tidyverse)
library(ggplot2)

# loading the data and metadata
data <- as.matrix(read.csv("data/pound_hill_data.csv", header = FALSE))
metadata <- read.csv("data/pound_hill_meta_data.csv", header = TRUE, sep = ";")

# inspecting dimensions, column types, etc.
head(data)
str(data)
dim(data)

head (metadata)
str(metadata)
dim(metadata)


#######################
#### DATA WRANGLING ### 
#######################

# converting blank species to observed zeros 
data[data == ""] = 0
# Note: SpeciesCount (in data) is described as the number of individials of species(count) per quadrat.
# Thus, an empty space means no individuals of that species were counted, and thus should be a 0

# transposing the data set (to get those species into columns and treatments into rows) 
data <- t(data)  
# reinpsecting data and its dimentsion after transposing it
head(data)
dim(data) # dimensions are now 60x45

# converting raw matrix to data frame 
TempData <- as.data.frame(data[-1,],stringsAsFactors = F) #stringsAsFactors = F is important!
colnames(TempData) <- data[1,] # assign column names from original data
colnames(TempData)

# Converting from wide to long format  

mydata <- TempData %>%
    pivot_longer(
        cols = -c("Cultivation", "Block", "Plot", "Quadrat"),
        names_to = "Species",
        values_to = "Count")

mywrangleddata <- mydata %>%
    mutate(
        Cultivation = as.factor(Cultivation), 
        Block = as.factor(Block),
        Plot = as.factor(Plot),
        Quadrat = as.factor(Quadrat),
        Count = as.integer(Count)) 

# checking that counts are not negative
if (any(mywrangleddata$Count < 0)) {
    message <- ("negative counts")}
    
# checking that counts are numeric
if (any(!is.numeric(mywrangleddata$Count))) {
    message <- ("non-numeric counts")} 

# reinspecting the data 
str(mywrangleddata) # verifying that class change was succesfull: it was
head(mywrangleddata)
dim(mywrangleddata) # dimensions: 2419x6

# convert data from data frame to "tibble"
mywrangleddata <- as_tibble(mywrangleddata) 

# determining number of distinct:
# species
length(unique(mywrangleddata$Species))
# 41 distinct species

# quadrats
length(unique(mywrangleddata$Quadrat))
# 6 distinct quadrats

# plots
length(unique(mywrangleddata$Plot))
# 12 distinct quadrats

print(mywrangleddata, n = 50)

#####################################################
######## CALCULATING AND PLOTTING RICHNESS ##########
##################################################### 

# making quadrat-level table of species counts
quadrat_richness_table <- mywrangleddata %>%
    filter(Count > 0 ) %>% # filtering for species that occure (Count > 0)
    group_by(Quadrat, Plot, Cultivation, Block) %>%
        summarise(Richness = length(unique(Species)))

print(quadrat_richness_table, n = 60)

# finding the mean species sum for each quadrat 

# making a plot-level summary of the mean richness
plot_mean_richness_table <- mywrangleddata %>%
    filter(Count > 0 ) %>% # filtering for species that occure (Count > 0)
    group_by(Cultivation, Block, Plot) %>%
        summarise(MeanRichness = mean(length(unique(Species))))

# writing the plot-level summary as a csv file in my results
write.csv(plot_mean_richness_table,"results/pound_hill_plot_richness.csv")

# drawing a figure comparing plot-level mean richness among three cultivation treatments 

plot_mean_richness_fig <- ggplot(plot_mean_richness_table, aes(x = Cultivation, y = MeanRichness, colour = Cultivation)) +
  geom_point(size =4) +
  labs(
    title = "Figure of the mean species richness at each plot, in relation to cultivation",
    x = "Cultivation",
    y = "Mean species richness",
    caption = "Figure dislpaying the mean species richness (y-axis) for each cultivation (x-axis) at all the plots. \n Each point represents a different plot and different colours refer to different cultivations. \n Mean species richness was calculated by taking the mean of the number of the species recorded at each plot, thus removing species with count 0. "
  ) + 
  scale_colour_manual(values = c("march" = "#76BD6A",
    "may" = "#F49335",
    "october" = "#AF4623"
  )) +
  scale_x_discrete(labels = c("march" = "March", "may" = "May", "october" = "October")) +
  theme_bw() + 
  guides(colour = "none") +
  theme(plot.caption = element_text(hjust = 0))

plot_mean_richness_fig

# saving the figure in results folder as a pdf
pdf("results/pound_hill_richness.pdf", 11.7, 8.3)
print(plot_mean_richness_fig)
graphics.off()

