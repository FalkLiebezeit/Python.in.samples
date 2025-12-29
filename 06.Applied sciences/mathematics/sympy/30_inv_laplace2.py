#30_inv_laplace2.py
from sympy import *
s,C,L,R = symbols("s C L R")
t = symbols("t",positive=True)
#Werte der Bauteile
R=1
L=5
C=10
#Matrizen der Längs- und Querglieder
A1=Matrix([[1, R],
           [0, 1]])
A2=Matrix([[1,  0],
           [C*s,1]])
A3=Matrix([[1,L*s],
           [0, 1]])
A4=Matrix([[1,   0],
           [C*s, 1]])
A5=Matrix([[1, L*s],
           [0,   1]])
A6=Matrix([[1,  0],
           [C*s,1]])
A7=Matrix([[1,  0],
           [1/R,1]])
#Matrizenmultiplikation
A=A1*A2*A3*A4*A5*A6*A7
#Übertragungsfunktion
H_s=1/A[0,0]
U2_s=H_s/s
u2=inverse_laplace_transform(U2_s,s,t)
#Ausgaben
print("Übertragungsfunktion\n",expand(H_s))
plot(u2,(t,0,100))