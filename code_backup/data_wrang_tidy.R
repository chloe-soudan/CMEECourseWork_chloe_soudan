
MyData <- as.matrix(read.csv("../data/pound_hill_data.csv", header = FALSE))

# header = true because we do have metadata headers
MyMetaData <- read.csv("../data/pound_hill_meta_data.csv", header = TRUE, sep = ";")


MyWrangledData <- TempData |>
    tidyr:: pivot_longer(
        cols = -c(Cultivation, Block, Plot, Quadrat),
        names_to = "Species",
        values_to = "Count"
    )