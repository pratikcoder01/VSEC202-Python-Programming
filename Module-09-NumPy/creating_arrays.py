"""
Basic NumPy array creation examples.
"""

import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1)

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr2)

# zeros and ones
print("Zeros:", np.zeros((2, 3)))
print("Ones:", np.ones((2, 3)))

# arange and reshape
arr3 = np.arange(1, 10)
print("Arange 1-9:", arr3)
print("Reshaped 3x3:\n", arr3.reshape((3, 3)))
