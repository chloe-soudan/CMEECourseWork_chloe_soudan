a <- 4
a

a*a

a_squared <- a*a 
a_squared

sqrt(a_squared)

v <- c(0,1,2,3,4)
v

is.vector(v)
mean(v)

var(v)
median(v)
sum(v)
prod(v +1)
length(v)

wing.width.cm <- 1.2
wing.length.cm <- c(4.7, 5.2, 4.8)
wing.length.cm

x <- (1+(2*3)
+
li <- list(c(1,2,3))
class(li)

v <- TRUE
v
class(v)

v <- 3.2 
class(v)

v <- 2L
class(v)
v <- "a string"
class(v)
is.na(b)
b <- 5/0
b
is.nan(b)
is.infinite(b)
is.finite(0/0)


as.integer(3.1)
as.numeric(4)
as.roman(155)
as.character(155)
as.logical(0)
1E4
5e-2
1/3/1e8


# VECTORS

a <- 5
is.vector(a)

v1 <- c(0.2, 0.5, 1)
v2 <- c("a", "bc", "def", "ghij")
v3 <- c(TRUE,TRUE, FALSE)

v1; v2;v3
v1 <- c(0.02, "mary", 1)
v1

v2 <- character(3)
v2
v3 <- numeric(3)
v3

heights_cm <- c(8,12,10,15)
above_threshold <- heights_cm > 10
above_threshold
sum(above_threshold)

mat1 <- matrix(1:25, 5, 5)
mat1
print(mat1)


mat1 <- matrix(1:25, 5,5,  byrow = TRUE)
dim(mat1)
arr1 <- array(1:50, c(5,5,2))
arr1[,,1]
print(arr1)
arr1[,,2]

mat1[1,1] <- "one"
mat1

mylist <- list(species =c("Quercus robur", "Fraxinus excelsior"), age =c(123, 84))
mylist
mylist[[1]]
mylist[[1]][1]

mymat = matrix(1:8, 4,4)
mymat
mydf = as.data.frame(mymat)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
mydf
object.size(mymat)
object.size(mydf)

mat
mat1 <- matrix(1:25, 5,5, byrow = TRUE)
mat1[1,2]
mat1[1,2:4]
mat1[1:2,2:4]
mat1[1,]


a <- c(1,5) +2
a
x <- c(1,2); y <- c(5,3,9,2)
x;y
x+y

x + c(y,1)


v <- c(0,1,2,3,4)
v2 <- v *2
v2

v*v2
t(v)
v %*% t(v) 

v3 <- 1:7
v3
v2
v4 <- c(v2, v3)
v4

# seeding random numbers 


mydata <- read.csv("data/trees.csv")

class(mydata)

head(mydata)
str(mydata)

mydata <- read.csv("data/trees.csv", header = FALSE)
head(mydata)

mydata <- read.table("data/trees.csv", sep = ",", header = TRUE)
head(mydata)

# skip five first lines
mydata <- read.csv("data/trees.csv", skip =5)
head(mydata)

### DATA FRAMES

col1 <- 1:10
col1
