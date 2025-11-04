#02_euler.py
import numpy as np
r=10
phi=np.radians(30)
z1=r*np.exp(1j*phi)
z2=r*np.cos(phi)+1j*r*np.sin(phi)
#Ausgaben
print("z1:",z1)
print("z2:",z2)
print("Betrag z1:",np.abs(z1))
print("Betrag z2:",np.abs(z2))
print("Type von z1:",type(z1))
print("Type von z2:",type(z2))
