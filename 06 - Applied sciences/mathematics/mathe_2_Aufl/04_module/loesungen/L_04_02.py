#L_04_02.py
import numpy as np
a=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
b=np.array([[9,8,7],
           [6,5,4],
           [3,2,1]])
n=len(a[0])
c=np.zeros([n,n])
for i in range(n):         #Zeilen
    for j in range(n):     #Spalten
        for k in range(n): #Spalten A; Zeilen B
            c[i,j]=c[i,j]+a[i,k]*b[k,j] #Produktsumme
#Ausgaben
print("Matrix A\n",a)
print("Matrix B\n",b)
print("Matrixprodukt\n",c)