#10_solve2.py
from sympy import *
s,U0,U1,U2,R,C,L = symbols("s,U0,U1,U2,R,C,L")
#Knotengleichungen
I1=(1/R+C*s+1/(L*s))*U1-U2/(L*s)-U0/R
I2=-U1/(L*s)+(1/R+C*s+1/(L*s))*U2
#Lösung der Knotengleichungen
U=solve((I1,I2),U1,U2)
print(U)

'''
from sympy import symbols, solve
'''


