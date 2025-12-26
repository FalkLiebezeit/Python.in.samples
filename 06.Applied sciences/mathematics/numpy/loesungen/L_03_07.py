#L_03_07.py
#Knotenpotentialverfahren fuer 3 Maschen
import numpy as np
I1=8
R=1
Y=1/R #Leitwert
#Koeffizientenmatrix
A=np.array([[2*Y, -Y, 0],
            [-Y, 3*Y, -Y],
            [0, -Y, 2*Y]])
#Inhomogenitaestsvektor
I=np.array([I1,0,0])
#Loesung
U=np.linalg.solve(A,I)
I=np.round(I,decimals=2)
#Ausgabe
print("Spannung 1,0:",U[0],"V")
print("Spannung 2,0:",U[1],"V")
print("Spannung 3,0:",U[2],"V")