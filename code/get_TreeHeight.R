
library(tidyverse) 

args <- commandArgs(trailingOnly = TRUE)

if (length(args) == 0) {
    message <- "No argument provided"
}
if (length(args) > 1) {
    message <- "Too many arguments provided"
}

if (!file.exists(args[1])) {
    message <- "Missing file"
}

trees1 <- read.csv(args[1])

head(trees1)



check_trees1 <- function(trees) {
    col_order <- c("Species", "Distance.m", "Angle.degrees")

    if (!identical(names(trees), col_order)) {
        message <- "wrong headers/ header order"}
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

trees_height1 <- check_trees1(trees1)

write.csv(tress_height1, "results/<input-basename-without-.csv>_treeheights.csv")