#11_outer.py
import numpy as np
A=np.array([[1,2,3]])
B=np.array([[4],[5],[6]])
C=np.outer(A,B)
print("Matrix A")
print(A)
print("Matrix B")
print(B)
print("dyadisches Produkt")
print(C)