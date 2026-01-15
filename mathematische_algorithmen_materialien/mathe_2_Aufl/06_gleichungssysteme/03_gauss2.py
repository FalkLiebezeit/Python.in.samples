#04_gauss2.py
import numpy as np
A = np.array([[3,2,1],
              [1,2,3],
              [2,1,4]],dtype=float)
b = np.array([10,14,16],dtype=float)
#Gauss-Algorithmus
def gauss(a,b):
    #obere Dreieicksmatrix
    n=len(b) #Anzahl der Gleichungen
    for k in range(0,n):         #Diagonale
        pivot=a[k,k]
        for i in range(k+1,n):   #Zeilen
            f = a[i,k]/pivot
            b[i]=b[i]-f*b[k]
            for j in range(k,n): #Spalten
                a[i,j]=a[i,j]-f*a[k,j]          
#Rücksubstitution
    x = np.empty(n)
    for i in range(n-1, -1, -1):
        for j in range(i+1,n):
            b[i]=b[i]-a[i,j]*x[j]
        x[i] = b[i]/a[i,i]
    return x
#Ausgabe    
print("Koeffizientenmatrix\n", A)
print("Inhomogenitätsvektor\n",b)
print("Lösungsvektor\n",gauss(A,b))
