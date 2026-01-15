#03_gauss1.py
import numpy as np
#Koeffizientenmatrix
a = np.array([[3,2,1],
              [1,2,3],
              [2,1,4]],dtype=float)
#Inhomogenitätsvektor
b = np.array([10,14,16],dtype=float)
#obere Dreiecksmatrix erzeugen
n=len(b)
for k in range(0,n):         #Diagonale
    pivot=a[k,k]
    for i in range(k+1,n):   #Zeilen
        f = a[i,k]/pivot
        b[i]=b[i]-f*b[k]
        for j in range(k,n): #Spalten
            a[i,j]=a[i,j]-f*a[k,j]
        print(a)
print("Inhomogenitätsvektor\n",b)