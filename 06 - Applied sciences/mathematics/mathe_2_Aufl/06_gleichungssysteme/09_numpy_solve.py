#10_numpy_solve.py
import numpy as np
from numpy.linalg import solve
#Koeffizientenmatrix
A = np.array([[3,2,1],
              [1,2,3],
              [2,1,4]],dtype=float)
#Inhomogenitätsvektor
b = np.array([10,14,16],dtype=float)
#Lösungsvektor
L=solve(A,b)
#Ausgabe
print("Koeffizientenmatrix\n", A)
print("Inhomogenitätsvektor\n",b)
print("Lösungsvektor\n",type(L))
print("x1 =",L[0])
print("x2 =",L[1])
print("x3 =",L[2])