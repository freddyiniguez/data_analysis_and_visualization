# Lecture 13 - Array Input and Output
import numpy as np

arr = np.arange(5)

# We save an array this way
np.save('myarray',arr)

# We create another rray wth the same name, given that we have saved the first one
arr = np.arange(10)

# This way we charge our first array
np.load('myarray.npy')

arr1 = np.load('myarray.npy')
arr2 = arr

# We save again our arrays, but this time in a zip format
np.savez('ziparray.npz',x=arr1,y=arr2)

archive_array = np.load('ziparray.npz')
archive_array['x']
archive_array['y']

# Save the array in a text file
arr = np.array([1,2,3], [4,5,6])
# We use a delimiter to separe the values in the text file
np.savetxt('mytextarray.txt',arr,delimiter=',')
# And charge again the text value
arr = np.loadtxt('mytextarray.txt',delimiter=',')
