#06_wirkungsgrad.py
from sympy import *
R0,R1,R2,U1,U2=symbols("R0 R1 R2 U1 U2")
Rg=R0+R1+R2
Ig=U1/Rg
P1=Rg*Ig**2
P2=R2*Ig**2
eta=P2/P1
print(u"\N{GREEK SMALL LETTER ETA} =",eta)