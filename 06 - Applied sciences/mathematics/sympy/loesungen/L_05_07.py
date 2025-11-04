#L_05_07.py
from sympy import *
s,C1,L2,C3=symbols("s C1 L2 C3")

A1=Matrix([[1, 1],
           [0, 1]])
A2=Matrix([[1,   0],
           [s*C1,1]])
A3=Matrix([[1,s*L2],
           [0, 1]])
A4=Matrix([[1,  0 ],
           [s*C3,1]])
A5=Matrix([[1, 0],
           [1, 1]])

A=A1*A2*A3*A4*A5

print("A11=",expand(A[0,0]))
