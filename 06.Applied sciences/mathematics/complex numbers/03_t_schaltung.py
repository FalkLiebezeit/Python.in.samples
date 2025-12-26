#03_t_schaltung.py
import numpy as np
U1=230
Z1=1+2j
Z2=10-12j
Z3=1+2j
Z4=10-10j
Zi=Z1*Z2/(Z1+Z2)+Z3
I2=U1/(Zi+Z4)
U2=Z4*I2
P2=U2*I2
print("Innenwiderstand:",np.round(Zi,decimals=2),"Ohm")
print("Ausgangsstrom:  ",np.round(I2,decimals=2),"A")
print("Ausgangsspannung:",np.round(U2,decimals=2),"V")
print("Ausgangsleistung:",np.round(P2,decimals=2),"W")