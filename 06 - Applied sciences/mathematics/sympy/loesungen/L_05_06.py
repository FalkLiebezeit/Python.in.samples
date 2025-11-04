#L_05_6.py
from sympy import *
s,t=symbols("s t",positive=True)
Fs=(s**3+16*s-24)/(s**4+20*s**2+64)
Fsp=apart(Fs)
LT_inv=inverse_laplace_transform(Fsp,s,t)
pprint(Fsp)
print(expand(LT_inv))