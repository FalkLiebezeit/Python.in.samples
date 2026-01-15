#07_cramer.py
import numpy as np
from numpy.linalg import det
#Koeffizientenmatrix
a = np.array([[3,2,1],
              [1,2,3],
              [2,1,4]],dtype=float)
#Inhomogenitätsvektor
b = np.array([10.,14.,16.],dtype=float)
#für 1. Lösung
A1= np.array([[b[0],a[0,1],a[0,2]],
              [b[1],a[1,1],a[1,2]],
              [b[2],a[2,1],a[2,2]]],dtype=float)
#für 2. Lösung
A2= np.array([[a[0,0],b[0],a[0,2]],
              [a[1,0],b[1],a[1,2]],
              [a[2,0],b[2],a[2,2]]],dtype=float)
#für 3. Lösung
A3= np.array([[a[0,0],a[0,1],b[0]],
              [a[1,0],a[1,1],b[1]],
              [a[2,0],a[2,1],b[2]]],dtype=float)
#Systemdeterminante
D=det(a)
D1=det(A1)
D2=det(A2)
D3=det(A3)
#Lösungsvektoren
x1=D1/D
x2=D2/D
x3=D3/D
#Ausgabe
print("Koeffizientenmatrix\n",a)
print("Inhomogenitätsvektor\n",b)
print("D  =",D)
print("D1 =",D1)
print("D2 =",D2)
print("D3 =",D3)
print("x1 =",x1)
print("x2 =",x2)
print("x3 =",x3)
