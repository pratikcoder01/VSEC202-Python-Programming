"""
Demonstrates statistical operations using NumPy.
"""

import numpy as np

data = np.array([10, 20, 20, 40, 50])

print("Data:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
