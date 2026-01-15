#L_13_04.py
#y=a0+a1*x+a2*x**2
import numpy as np
from numpy.linalg import inv
x=np.array([-1,0,1,2,3,4])
y=np.array([3,2,9,21,49,81.4])
n=len(x)
A=np.array([np.ones(n),x,x**2]).T
L=inv(A.T@A)@A.T@y
a0,a1,a2=L[0],L[1],L[2]
print(L)
print("a0 = %3.2f\na1 = %3.2f \na2 = %3.2f"%(a0,a1,a2))

