#L_13_04.py
#y=a*√(x+1)+b*x
import numpy as np
from numpy.linalg import inv
x=np.array([-1,0,3,8,15,20])
y=np.array([-1,3,10,27,42,54.7])
n=len(x)
A=np.array([np.sqrt(x+1),x]).T
L=inv(A.T@A)@A.T@y
print("Lösungsvektor:",L)
a,b=L[0],L[1]
print("a = %3.3f\nb = %3.3f"%(a,b))
def f(a,b,x):
    return a*np.sqrt(x+1)+b*x
print(f(a,b,20))