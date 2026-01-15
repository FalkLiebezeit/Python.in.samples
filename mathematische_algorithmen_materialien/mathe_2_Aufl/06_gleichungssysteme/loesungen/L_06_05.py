#L_06_04.py
import numpy as np
A = np.array([[5,2,1],
              [2,4,3],
              [1,3,2]],dtype=float)
L=np.tril(A,k=-1)
R=np.triu(A,k=1)
D=A-R-L
summe=L+D+R
print("Matrix\n",A)
print("strikte untere Dreiecksmatrix\n",L)
print("Dialogmatrix\n",D)
print("strikte obere Dreiecksmatrix\n",R)
print("Summe\n",summe)
