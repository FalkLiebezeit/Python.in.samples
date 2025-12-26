#12_matrixmul1.py
import numpy as np
A=np.array([[1, 2],
            [3, 4]])
B=np.array([[5, 6],
            [7, 8]])
C=A@B
D=B@A
#Ausgabe
print(type(A))
print("Matrix A\n",A)
print("Matrix B\n",B)
print("Produkt A*B\n",C)
print("Produkt B*A\n",D)