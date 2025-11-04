from scipy import linalg
import numpy as np

A = np.array([[3, 2], [1, 2]])
b = np.array([2, 0])

x = linalg.solve(A, b)
print("Lösung:", x)