#!/usr/bin/env python3
# chloe.soudan26@impreial.ac.uk
# NUMPY IN PYTHON

import scipy
import numpy as np

a = np.array(range(5)) # one-dimensional array a
a

print(type(a))
# output: <class 'numpy.ndarray'>

print(type(a[0]))
#output: <class 'numpy.int64'>

# specifying data type of the array
a = np.array(range(5), float) # data type is float 
a

#checking type
a.dtype 
# output: dtype('float64')

# different manner of getting 1-D array
x = np.arange(5.) # can specify float directly using the decimal
x

x.shape

##  converting to and from python lists
# creating array
b = np.array([i for i in range(10) if i %2 ==1]) # odd numbers between 1 and 10
b
# output: array([1, 3, 5, 7, 9])

# converting back to list
c = b.tolist()
c
# output: [1, 3, 5, 7, 9]

## making a mutrix (needs a 2-D numpy array)
mat = np.array([[0, 1], [2, 3]])
mat

mat.shape # shape = (2,2)

### INDEXING AND ACCESSING ARRAYS
mat[1] # accessing 2nd row 
# output: array([2, 3])

mat[:,1] # accessing whole second column)
# output: array([1, 3])

mat[0,0] # accessing 1st row of 1st column
# output: np.int64(0)

mat[1,0] # accessing 2nd row of 1st column
# output: np.int64(2)

mat[0,-1]  # accessing 1st element of 1st column going back to the start for the end of the array
# output: np.int64(1)

### MNAIPULATING ARRAYS 
#replacing a single element
mat[0,0] = -1 # replacing 1st row of 1st column to be -1
mat

#replacing a whole column
mat[:, 0] = [12,12] # replacing the whole 1st column by [12,12]
mat

# appending row with axis specification
np.append(mat, [[12,12]], axis = 0)

# appending column with axis specification
np.append(mat, [[12], [12]], axis =1)

# creating a new row and appending it
newrow = [[12,12]]
mat = np.append(mat, newrow, axis = 0)
mat

# deleting a row 
np.delete(mat, 2, 0) # deleting 3rd row

# concatenation
mat = np.array([[0,1], [2,3]])
mat0 = np.array([[0,10], [-1,3]])
np.concatenate((mat,mat0), axis = 0) # concatenate rows

### FLATTENING AND RESHAPIUNG ARRAYS 
mat.ravel() #flattening the matrix 
# output: array([0, 1, 2, 3])

# reshaping the matrix
mat.reshape((4,1)) # to 4 rows, 1 column

mat.reshape((1,4)) # to 1 row, 4 columns

mat.reshape((3,1)) # to 3 rows, 1 column
# output: error meesage  because array has size 4 and shape is (3,1)

### PREALOCATING ARRAYS 
np.ones((4,2)) # creates a matrix of 4 rows and 2 columns,filled in with ones 

# repeating the same but filling the matrix with 0s
np.zeros((4,2))

# creating an identity matrix (ones one main diagonal)
m = np.identity(4) 
m

# filling the m matrix with 16s 
m.fill(16)
m
# note: main diagonal is not filled with 1s anymore and is also 16s

### NUMPY MATRICES

## matrix vector operations
mm = np.arange(16) # creating an array ranging from 0 to 15 (included)
mm = mm.reshape(4,4) # converting it to a 4x4 matrix
mm
# transposing mm
mm.transpose()

# sum of matrices
mm + mm.transpose() 

# difference of matrices
mm - mm.transpose()

# mulitplication of matrices
mm * mm.transpose() # element-wise multiplication

# division of martices
mm // mm.transpose() 
# warning: <python-input-46>:1: RuntimeWarning: divide by zero encountered in floor_divide

# avoiding division by 0
mm //(mm +1).transpose()

# multiplication of matrix by pi 
mm * np.pi

# multiplication using matric multiplication 
mm.dot(mm) # multiplies mm by mm using dot product operation 

# exploring the numpy matrix class
mm = np.matrix(mm) # converting the scipy/numpy matrix class
mm

print(type(mm))
# output: <class 'numpy.matrix'>
# then  we can use mm * mm instead of mm.dot(m) for matric multiplication

### THE SCIPY PACKAGE
## spicy stats 

import scipy as sc

# generating 10 samples from the normal distribution
sc.stats.norm.rvs(size =10)
# note: creates an array of 10 elements that are normally distributed

# "seed" random number to get the same sequence every time (for reproducibility)
np.random.seed(1234)
sc.stats.norm.rvs(size=10)

# using random_state argument for eahc specific generation of a set of random numbers
sc.stats.norm.rvs(size =5, random_state = 1234)

# generatig random integers between 0 and 10 
sc.stats.randint.rvs(0,10, size =7) # generating 7 random integers

# generating random integers with a random seed
sc.stats.randint.rvs(0,10, size =7, random_state = 1234)

# using another seed
sc.stats.randint.rvs(0,10, size =7, random_state = 3445)

## numerical integration using scipy
import scipy.integrate as integrate

## Area under a curve
# calculating the area under an arbitrary curve
y = np.array([5,20,18,19,18,7,4]) # creating an array y 

import matplotlib.pylab as p
# plotting the area
p.plot(y)
# returns: [<matplotlib.lines.Line2D object at 0x7b40b1a20c20>]

# calculating the area using the composite trapezoidal rule
area = integrate.trapezoid(y, dx = 2) #dx defines spacing between points of the curve
print("area", area)
# area is 173.0

# calculating the area with a different dx (dx =1)
area = integrate.trapezoid(y, dx = 1)
print("area", area)
# area is 86.5

# another dx (dx =3)
area = integrate.trapezoid(y, dx = 3)
print("area", area)
# area is 259.5

# using Simpson's rule
area = integrate.simpson(y, dx =2)
print("area =", area)
# output: area = 176.666666666

# using dx =1
area = integrate.simpson(y, dx =1)
print("area =", area)
# output: area = 88.33333333

# using dx =3
area = integrate.simpson(y, dx =3)
print("area =", area)
# output: area = 265.0
