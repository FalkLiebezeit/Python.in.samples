#L_06_03a.py
import numpy as np
A = np.array([[5, 4, 3, 2],
              [1, 7, 1, 3],
              [2, 1, 11, 1],
              [7, 3, 1, 13]],dtype=float)
b = np.array([10, 8, 6, 4],dtype=float)
#Jacobi-Verfahren
def jacobi(a,b,N=30):
#Dreieckszerlegung
    L=np.tril(a,k=-1)  #links unten
    R=np.triu(a,k=1)   #rechts oben
    n=np.size(b)       #Anzahl der Gleichungen
    x=np.zeros(n)      #Initialisierung
    for _ in range(N): #Anzahl der Iterationen
        for i in range(n):
            x[i]=(b[i]-(R[i]+L[i])@x)/a[i,i]
    return x
#Ausgabe
print("Lösungsvektor\n",jacobi(A,b))



