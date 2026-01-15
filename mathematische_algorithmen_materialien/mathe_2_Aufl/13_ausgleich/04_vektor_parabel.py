#04_vektor_parabel.py
import numpy as np
from numpy.linalg import inv
x=np.array([1,2,3,4,5])
y=np.array([5.1,2.1,1,1.8,5.2])
n=len(x)
A=np.array([x**2,x,np.ones(n)]).T #reshape(5,3)
L=inv(A.T@A)@A.T@y #Lösungsvektor
print("1. Koeffizientenmatrix des überbestimmten Gleichungssystems\n",A)
print("2. transponierte Koeffizientenmatrix\n",A.T)
print("3. Koeffizientenmatrix der Normalgleichungen\n",A.T@A)
print("4. normalisierter Inhomogenitätsvektor\n",A.T@y)
print("5. invertierte Koeffizientenmatrix der Normalgleichung\n",inv(A.T@A))
print("6. Lösungsvektor\n",L)
a,b,c=L[0],L[1],L[2]
print("   a  \t   b\t c")
print("%2.3fx^2 %2.3fx %2.3f" %(a,b,c))



