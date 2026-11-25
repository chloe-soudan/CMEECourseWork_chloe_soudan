#!/usr/bin/env R
# chloe.soudan26@imperial.ac.uk
# Beautiful graphics in R

install.packages("ggplot2")
library(ggplot2)

#assigning p to be the plot
p <- ggplot(mydf, aes(x = log(Predator.mass),
                 y = log(Prey.mass),
                 colour = Type.of.feeding.interaction))
p # plots an empty graph 

p + geom_point() # prints an actual plot


# using the "+" sign to concatenate different commands 
p <- ggplot(mydf, aes(x = log(Predator.mass),
                 y = log(Prey.mass),
                 colour = Type.of.feeding.interaction))
q <- p + geom_point(size=I(2), shape  =I(10)) +
theme_bw() +   # making the background white
theme(aspect.ratio =1) # making the plot square
q

# removing the legend
q + theme(legend.position = "none") + theme(aspect.ratio = 1)

# # setting the transparency of the fills
p <- ggplot(mydf, aes(x= log(Prey.mass/Predator.mass), fill = Type.of.feeding.interaction)) +
geom_density(alpha=0.5) 
p

# using facet_wrap to create multifaceted plot
p <- ggplot(mydf, aes(x= log(Prey.mass/Predator.mass), fill = Type.of.feeding.interaction)) +
geom_density(alpha=0.5) + facet_wrap(.~Type.of.feeding.interaction)
# each plot would be a different type of feeding interaction
p

# freeing up the axes so that the axis limits can be data-specific
p <- ggplot(mydf, aes(x= log(Prey.mass/Predator.mass), fill = Type.of.feeding.interaction)) +
geom_density(alpha=0.5) + facet_wrap(.~Type.of.feeding.interaction, scales = "free")
# each plot would be a different type of feeding interaction
p

#plotting the size-ratio distributions by location 
p <- ggplot(mydf, aes(x = log(Prey.mass/Predator.mass))) + geom_density() + facet_wrap( .~Location, scales = "free")
p

#different example
p <- ggplot(mydf, aes( x= log(Prey.mass),
                y = log(Predator.mass))) + geom_point() + facet_wrap( .~Location, scales = "free")
p

# combining categories
p <- ggplot(mydf, aes(x = log(Prey.mass), y = log(Predator.mass))) + geom_point() + facet_wrap( .~Location + Type.of.feeding.interaction, scales = "free")
print(p)

#changing the order of the combination
p <- ggplot(mydf, aes(x = log(Prey.mass), y = log(Predator.mass))) + geom_point() + facet_wrap( .~Type.of.feeding.interaction + Location, scales = "free")
p