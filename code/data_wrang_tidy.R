#!/usr/bin/env Rscript
# Chloe Soudan - chloe.soudan26@imperial.ac.uk
# Script: data_wrang_tidy.R
# Desc: Wrangling the Pound Hill Dataset using the tidyverse library
# Date: Oct 2026

library(tidyverse)

############# Load the dataset ###############
# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("data/pound_hill_data.csv", header = FALSE))

# header = true because we do have metadata headers
MyMetaData <- read.csv("data/pound_hill_meta_data.csv", header = TRUE, sep = ";")


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

dim(TempData)
############ Converting columns to appropriate class using dplyr ############

MyWrangledData <- TempData %>%
    mutate(
        Cultivation = as.factor(Cultivation),
        Block = as.factor(Block),
        Plot = as.factor(Plot),
        Quadrat = as.factor(Quadrat))

############ Converting from wide to long format using dplyr ############

MyWrangledData <- MyWrangledData |>
    tidyr:: pivot_longer(
        cols = -c(Cultivation, Block, Plot, Quadrat),
        names_to = "Species",
        values_to = "Count")

########### Converting count to integer #########
MyWrangledData <- MyWrangledData %>%
    mutate(
    Count = as.integer(Count))


########## Inspecting the outputs ############
head(MyWrangledData)
str(MyWrangledData)
dim(MyWrangledData) # 2419  6, pivot succesful
colnames(MyWrangledData) # "Cultivation","Block","Plot","Quadrat","Species", "Count"