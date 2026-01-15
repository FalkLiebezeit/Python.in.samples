#L_06_04.py
import numpy as np
from numpy.linalg import inv
A = np.array([[5,2,1],
              [2,4,3],
              [1,3,2]],dtype=float)
B = np.array([[5,0,0],
              [2,4,0],
              [1,3,2]],dtype=float)
C = np.array([[5,0,0],
              [0,4,0],
              [0,0,2]],dtype=float)
D = np.array([[5,2,1],
              [0,4,3],
              [0,0,25]],dtype=float)
print("A\n",inv(A))
print("B\n",inv(B))
print("C\n",inv(C))
print("D\n",inv(D))