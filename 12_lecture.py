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

# 
answer2 = np.where(condition,A,B)
