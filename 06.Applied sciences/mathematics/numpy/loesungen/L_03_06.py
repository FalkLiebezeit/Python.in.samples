#L_03_06.py
#Maschenstromverfahren für 3 Maschen
import numpy as np
U1=13
R=1
#Koeffizientenmatrix
A=np.array([[2*R, -R, 0],
            [-R, 3*R, -R],
            [0, -R, 3*R]])
#Inhomogenitätsvektor
U=np.array([U1,0,0])
#Llösung
strom=np.linalg.solve(A,U)
#Ausgabe
for k, I in enumerate(strom):
    print("I%i = %0.2f A" %(k+1,I))
    



