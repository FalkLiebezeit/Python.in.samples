#L_03_05.py
#dyadische Produkt
import numpy as np
A=np.array([[1,2,3,4]])       #Zeilenvektor
B=np.array([[5],[6],[7],[8]]) #Spaltenvektor
C=np.outer(A,B)
print("Matrix A")
print(A)
print("Matrix B")
print(B)
print("dyadisches Produkt")
print(C)