#17_seidel2.py
import numpy as np
from numpy.linalg import inv
A = np.array([[6,2,1],
              [1,5,3],
              [2,1,4]],dtype=float)
b = np.array([13,20,16],dtype=float)
#Gauss-Seidel-Verfahren
def seidel(A, b, N=15):
    L=np.tril(A)
    invL=inv(L)
    R=A-L
    n=np.size(b)
    x=np.zeros(n) #Startwerte
    for k in range(N):
        x = invL@(b - R@x)
        #print(x)
    return x
#Ausgabe
print("Lösungsvektor\n",seidel(A,b))
 