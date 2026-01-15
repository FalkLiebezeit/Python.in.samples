#L_06_01a.py
import numpy as np
A = np.array([[5, 4, 3, 2],
              [1, 7, 1, 3],
              [2, 1, 11, 1],
              [7, 3, 1, 13]],dtype=float)
b = np.array([10, 8, 6, 4],dtype=float)
def gauss(a,b):
    #obere Dreieicksmatrix
    n=b.size #Anzahl der Gleichungen
    for i in range(n):
        for j in range(i+1,n):
            q = a[j,i]/a[i,i]
            b[j]=b[j]-b[i]*q
            for k in range(i,n):
                a[j,k]=a[j,k]-a[i,k]*q           
#Rücksubstitution
    x = np.empty(n)
    for i in range(n-1, -1, -1):
        for j in range(i+1,n):
            b[i]=b[i]-a[i,j]*x[j]
        x[i] = b[i]/a[i,i]
    return x          
L=gauss(A,b)
print("Lösungsvektor\n",L)