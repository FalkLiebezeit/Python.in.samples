#16_gleichungssystem.py
import numpy as np
from numpy.linalg import solve
#Koeffizientenmatrix
A = np.array([[1,  1, 1],
              [2, -2, 3],
              [3, -4, 2]])
#Inhomogenitätsvektor
b = np.array([6, 7, 1])
#Lösung
loesung=solve(A,b)
#Ausgabe
print("Lösung eines linearen Gleichungssystems")
print("Koeffizientenmatrix\n",A)
print("Inhomogenitätsvektor\n",b)
print("Lösung:\n",loesung)


'''
print(type(A[0,0]))
print(type(b[0]))
print(type(loesung[0]))
'''
