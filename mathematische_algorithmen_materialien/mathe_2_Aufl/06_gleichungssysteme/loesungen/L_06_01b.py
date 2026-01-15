#L_06_01b.py
import numpy as np
#erweiterte Koeffizientenmatrix
Ab = np.array([[5, 4, 3, 2,10],
              [1, 7, 1, 3, 8],
              [2, 1, 11, 1,6],
              [7, 3, 1, 13,4]],dtype=float)
#Gauss-Jordan-Algorithmus
def jordan(a):
    n=np.size(a,0) #Anzahl der Zeilen
    x=np.zeros(n) #Initialisierung
    for i in range(n):     #Zeilen    
        for j in range(n): #Spalten
            if i != j:
                q = a[j][i]/a[i][i]
                for k in range(n+1):
                    a[j][k] = a[j][k] - q*a[i][k]
            #print(a)
    for i in range(n):
        x[i] = a[i][n]/a[i][i]
    return x.T
#Ausgabe
print("Lösungsvektor\n ",jordan(Ab))

