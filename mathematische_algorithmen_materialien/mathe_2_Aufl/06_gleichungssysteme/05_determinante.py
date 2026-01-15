#06_determinante.py
import numpy as np
from numpy.linalg import det
#Koeffizientenmatrix
a = np.array([[3,2,1],
              [1,2,3],
              [2,1,4]],dtype=float)
#Gauss Algorithmus
def determinante(a):
    dm=1
    n=a.shape[0]
    for k in range(0,n):         
        for i in range(k+1,n):   
            f = a[i,k]/a[k,k]
            for j in range(k,n): 
                a[i,j]=a[i,j]-f*a[k,j]
        dm=dm*a[k,k]
    return dm
#Ausgabe
print("Determinante")
print("Gauss:",determinante(a))
print("NumPy:",det(a))
