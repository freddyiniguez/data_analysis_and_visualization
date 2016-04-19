# Lecture 09 - Indexing Arrays
import numpy as np

arr = np.arange(0,11)

# We get the 8th value in the array
arr[8]

# This way we get from value in position 1 to value in position 8
arr[1:5]

# We're telling python that set the valaues from 0 to 5 equal to 100
arr[0:5] = 100

arr = np.arange(0,11)

# This way we are creating a sub-array from the arr array
slice_of_arr = arr[0:6]

# Set the values in all the array equal to 99
slice_of_arr[:] = 99

# REMEMBER!
# In Numpy, the sub-arrays are a image of the original array
# So, any change in the subarray, it will affect the original array

# If you do not wat to modify the original array, you should say:
arr_copy = arr.copy()

# A 2dimensional array
arr_2d = np.array(([5,10,15], [20,25,30], [35,40,45]))

# Get the list in position 1 in the array_2s
arr_2d[1]

# Get the value in line 1 column 0
arr_2d[1][0]

# Get the values from line 0 to line 2, and values from column 1
arr_2d[:2,1:]

# Fancy indexing
arr2d = np.zeros((10,10))
arr_length = arr2d.shape[1]
arr_length

for i in range(arr_length):
	arr2[i]=i
# Fancy indexing allows to do something like this:
# Get the 2nd, 4th, 6th, and 8th index
arr2d[[2,4,6,8]]
