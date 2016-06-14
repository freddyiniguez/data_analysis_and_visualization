# Lecture 12 - Array Processing

import numpy as np
import matplotlib.pyplot as plt
# In order to see the visualization
%matplotlib inline

# Let's create an array with initial value, stop value and inteval
points = np.arange(-5,5,0.01)

# Create a pair of grids
dx,dy = np.meshgrid(points, points)

# Z values
z = (np.sin(dx) + np.sin(dy))

# Plot this kind of data like this:
plt.imshow(z)

# Add to the plot a title and what the colors mean
plt.imshow(z)
plt.colorbar()
plt.title('Plot for sin(x) + sin(y)')

# Use numpy where
A = np.array([1,2,3,4])
B = np.array([100,200,300,400])

# A boolean array
condition = np.array([True, True, False, False])

# List comprehension
# "Show me the A value is the condition is met, otherwise show me the B value"
answer = [(A_val if cond else B_val for A_val, B_val, cond in zip(A,B,condition)]

# The where sentence in numpy is the short way of a list comprehension
answer2 = np.where(condition,A,B)

from numpy.random import randn

# Create a random normal distribution in a array
arr = randn(5,5)

# In the following numpy-where sentence we're indicating
# that for those number that are less than zero it will
# be converted to zero, otherwise do not touch the number
np.where(arr<0,0,arr)

# A 3 by 3 array
arr = np.array([1,2,3], [4,5,6], [7,8,9])

arr.sum()

# Skip the zero row
arr.sum(0)

# Statistical operations
arr.mean()
arr.std()
arr.var()

bool_arr = np.array([True, False, True])

# It is going to return a boolean if there is a True in the array
bool_arr.any()

# It will return True if all the values in the array are True
bool_arr.all()

# Sorting arrays
arr = randn(5)
arr.sort()

countries = np.array(['France', 'Germany', 'USA', 'Russia', 'USA', 'Mexico', 'Germany'])
# Unique function it will tell me the unique values, not the repeated
np.unique(countries)

# Check if France, USA and Sweden are in the countries array
np.in1d(['France', 'USA', 'Sweden'], countries)
