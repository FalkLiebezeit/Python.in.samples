#L_06_07.py
import numpy as np
from  numpy.linalg import solve
A1 = np.array([[-2,5,13],
              [3,12,1],
              [34,2,3]],dtype=float)
A2 = np.array([[34,2,3],
              [3,12,1],
              [-2,5,13]],dtype=float)
b = np.array([47,30,47],dtype=float)
#Jacobi-Verfahren
def jacobi(a,b,N=30):
    L=np.tril(a,k=-1)  #links unten
    R=np.triu(a,k=1)   #rechts oben
    n=np.size(b)       #Anzahl der Gleichungen
    x=np.zeros(n)      #Initialisierung
    for _ in range(N): #Anzahl der Iterationen
        for i in range(n):
            x[i]=(b[i]-(L[i]+R[i])@x)/a[i,i]
    return x
#Ausgabe
print("Lösungsvektor\n",jacobi(A2,b))
print("",solve(A2,b))
'''
Begründung:
Nach dem Zeilentausch ist die Koeffizientenmatrix dialogdominat.
'''

