#09_numpyInverse.py
import numpy as np
from numpy.linalg import inv
#Koeffizientenmatrix
A = np.array([[3,2,1],
              [1,2,3],
              [2,1,4]],dtype=float)
#Inhomogenitätsvektor
b = np.array([10.,14.,16.],dtype=float)
#Matrizenmultiplikation
x=inv(A)@b
#x=np.dot(inv(A),b)
#x=np.matmul(inv(A),b)
#Ausgabe
print("Koeffizientenmatrix\n", A)
print("Inhomogenitätsvektor\n",b)
print("Inverse der Koeffizientenmatrix\n",inv(A))
print("Lösungsvektor\n",x)
print("x1 =",x[0])
print("x2 =",x[1])
print("x2 =",x[2])