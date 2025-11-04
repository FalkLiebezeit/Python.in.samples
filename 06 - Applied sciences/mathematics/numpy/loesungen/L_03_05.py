#L_03_05.py
import numpy as np
from numpy.linalg import solve
m=50
np.random.seed(1)
A=np.random.normal(8,4,size=(m,m))
b=np.random.normal(8,4,size=m)
#Lösung
x=solve(A,b)
#Ausgabe
print("Koeffizientenmatrix\n",A)
print("Inhomogenitätsvektor\n",b)
print("Lösung\n",x)