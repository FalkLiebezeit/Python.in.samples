#02_matrixprodukt.py
import numpy as np
A=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
B=np.array([[9,8,7],
           [6,5,4],
           [3,2,1]])
#Matrizenmultiplikation
C=A@B           #Infixoperator
#Ausgaben
print("Matrix A\n",A)
print("Matrix B\n",B)
print("Multiplikation A@B\n",C)

# print(np.transpose(A))
# print(A.T)


