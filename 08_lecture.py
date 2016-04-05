# Lecture 08 - Using arrays and scalars

import numpy as np
from __future__ import division

# Now we can divide normally, like 5/2 = 2.5, without having to explicity 5.0
print 5/2

arr1 = np.array([[1,2,3,4], [8,9,10,11]])

# Multiple an array by itself
print arr1 * arr1

# Substract an array by itself
print arr1 - arr1

# Dividing 1 by each element of the array
print 1 / arr1

# Power an array by 3
print arr1 ** 3
