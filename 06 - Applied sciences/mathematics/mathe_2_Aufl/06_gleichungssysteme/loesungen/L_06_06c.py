#14_seidel2.py
import numpy as np
from numpy.linalg import inv
A = np.array([[5, 4, 3, 2],
              [1, 7, 1, 3],
              [2, 1, 11, 1],
              [7, 3, 1, 13]],dtype=float)
b = np.array([10, 8, 6, 4],dtype=float)
#Gauss-Seidel-Verfahren
def seidel(A, b, N=30):
    L=np.tril(A)
    R=A-L
    invL=inv(L)
    n=np.size(b)
    x=np.zeros(n)
    for _ in range(N):
        x =invL@(b - R@x)
    return x
#Ausgabe
print("Lösungsvektor\n",seidel(A,b))
 
