#03_vektor_gerade.py
import numpy as np
from numpy.linalg import inv
x=np.array([1,2,3,4,5])
y=np.array([6,6.8,10,10.5,10.2])
n=len(x)
A=np.array([x,np.ones(n)]).T 
L=inv(A.T@A)@A.T@y
print("1. Koeffizientenmatrix des überbestimmten Gleichungssystems\n",A)
print("2. transponierte Koeffizientenmatrix\n",A.T)
print("3. Koeffizientenmatrix der Normalgleichungen\n",A.T@A)
print("4. normalisierter Inhomogenitätsvektor\n",A.T@y)
print("5. invertierte Koeffizientenmatrix der Normalgleichung\n",inv(A.T@A))
print("6. Lösungsvektor\n",L)
a,b=L[0],L[1]
print("Steigung        a =",a)
print("Achsenabschnitt b =",b)
