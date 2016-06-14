# Lecture 11 - Universal array functions

import numpy as np

# Let's create a simple array
arr = np.arange(11)

# A universal function is a function that you can apply to 
# every value in an array

# Square
np.sqrt(arr)

# Exponential
np.exp(arr)

# A random normal distribution
A = np.random.randn(10)
B = np.random.randn(10)

# Binary functions that use two arrays

# Adding
np.add(A,B)

# Find the max or min between two arrays (for each element)
np.maximum(A,B)
np.minimum(A,B)

# To open a web link
website = 'http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs'
import webbrowser

webbrowser.open(website)
