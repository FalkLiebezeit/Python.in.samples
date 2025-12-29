#14_mulmatrix3.py
import numpy as np
R1=1
R2=2
R3=1
U1=5
I1=7
B1q=np.array([[1, 0],
            [-1/R1, 1]])
B2l=np.array([[1, -R2],
            [0, 1]])
B3q=np.array([[1, 0],
            [-1/R3, 1]])
B=B1q@B2l@B3q
b=np.array([[U1],[I1]])
E=B@b
print("Kettenform B\n",B)
print("Ausgangsgrößen\n",E)
print("Ausgangsspannung U2=%3.2fV" %E[0])
print("Ausgangsstrom    I2=%3.2fA" %E[1])