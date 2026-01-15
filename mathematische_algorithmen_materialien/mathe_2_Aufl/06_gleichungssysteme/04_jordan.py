#05_jordan.py
import numpy as np
A = np.array([[3,2,1],
              [1,2,3],
              [2,1,4]],dtype=float)
b=np.array([10,14,16],dtype=float)
#Gauss Jordan-Algorithmus
def jordan(a,b):
    n=len(b)           #Anzahl der Zeilen
    for k in range(n): #Diagonale           
        pivot=a[k,k]
        for j in range(k,n): #Spalten
            a[k,j]=a[k,j]/pivot
        b[k]=b[k]/pivot   
        for i in range(n):   #Zeilen
            if i==k:continue
            f=a[i,k]
            for j in range(k,n):
                a[i,j]=a[i,j] - f*a[k,j]
            #print(a)
            b[i]=b[i]-f*b[k]
    return b,a
x,A_t=jordan(A,b)
#Ausgabe
print("Lösungsvektor\n ",x)
print("Transformierte Koeffizientenmatrix\n",A_t)

