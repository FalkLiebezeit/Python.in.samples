#L_06_01c.py
import numpy as np
from numpy.linalg import solve
A = np.array([[5, 4, 3, 2],
              [1, 7, 1, 3],
              [2, 1, 11, 1],
              [7, 3, 1, 13]],dtype=float)
b = np.array([10, 8, 6, 4],dtype=float)
L=solve(A,b)
print("Lösungsvektor\n",L)
