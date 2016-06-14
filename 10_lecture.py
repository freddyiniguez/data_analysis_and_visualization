# Lecture 10 - Array Transposition

import numpy as np

# Create an array of 50 points and reshape it into 
# ten rows and 5 columns
arr = np.arange(50).reshape((10,5))
arr

# To transpose an array, simple type
arr.T

np.dot(arr.T, arr)

# A 3d array, resape of 5 slices each of 5 rows 2 columns
arr3d = np.arange(50).reshape((5,5,2))

# To transpose indexes in an array
arr = np.array([[1,2,3]])
arr.swapaxes(0,1)
