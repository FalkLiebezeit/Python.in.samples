#L_05_06.py
#π mit atan berechnen
from sympy import N,pi,atan
#arctan von SymPy !
def stoermer():
    pi_s=44*atan(1/57)+7*atan(1/239)-12*atan(1/682)+24*atan(1/12943)
    return 4*pi_s

dz=20
pi_st=stoermer()
pi_atan=4*atan(1)
print(N(pi_st,dz),"Størmer")
print((N(pi_atan,dz)),"SymPy arctan")
print(N(pi,dz),"SymPy")
print(type(pi_st))
