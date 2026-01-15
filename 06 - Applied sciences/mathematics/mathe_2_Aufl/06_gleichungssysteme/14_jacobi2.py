#14_jacobi2.py
import numpy as np
A = np.array([[6,2,1],
              [1,5,3],
              [2,1,4]],dtype=float)
b = np.array([13,20,16],dtype=float)
#Jacobi-Verfahren
def jacobi(a,b,N=15):
#Dreieckszerlegung
    L=np.tril(a,k=-1)  #links unten
    R=np.triu(a,k=1)   #rechts oben
    n=np.size(b)       #Anzahl der Gleichungen
    x=np.zeros(n)      ##Startwerte
    for k in range(N): #Anzahl der Iterationen
        for i in range(n):
            x[i]=(b[i]-(L[i]+R[i])@x)/a[i,i]
    return x
#Ausgabe
print("Koeffizientenmatrix\n",A)
print("Inhomogenitätsvektor\n",b)
print("links-untere-Dreiecksmatrix\n",np.tril(A,k=-1))
print("rechts-obere-Dreiecksmatrix\n",np.triu(A,k=1))
print("Lösungsvektor\n",jacobi(A,b))

