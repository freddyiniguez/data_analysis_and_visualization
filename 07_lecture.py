# Lecture 07 - Creating Arrays

import numpy as np

my_list1 = [1,2,3,4]
# We create an array with the Numpy library like this:
my_array1 = np.array(my_list1)

my_list2 = [11,22,33,44]
# We can combine lists like this
my_lists = [my_list1, my_list2]
my_array2 = mp.array(my_lists)

# Look for the shape of the array
print my_array2.shape

# Look the type of the array
print my_array2.dtype

# Create an array of zeros
my_zero_array = np.zeros(5)

# Create an array of ones
my_one_array = np.ones([5, 5])

# Or create an empty array
my_empty_array = np.empty(5)

# Create an identity matrix
my_identity_matrix = np.eye(5)

# This way to create arrays will be used a lot in this course
my_array = np.arange(5)
print my_array

# Create an array that starts at 5, until 50, in 2 by 2
my_cool_array = np.arange(5, 50, 2)
print my_cool_array
