#13_mulmatrix2.py
import numpy as np
R1=1.
R2=2.
R3=1.
U2=1.
I2=1.
A1q=np.array([[1., 0],
            [1./R1, 1.]])
Al=np.array([[1, R2],
            [0, 1.]])
A2q=np.array([[1., 0],
            [1./R3, 1.]])
A=A1q@Al@A2q
b=np.array([[U2],[I2]])
E=A@b
print("Kettenform A\n",A)
print("Eingangsgrößen\n",E)
print("Eingangsspannung U1=%3.2f V" %E[0])
print("Eingangsstrom    I1=%3.2f A" %E[1])

