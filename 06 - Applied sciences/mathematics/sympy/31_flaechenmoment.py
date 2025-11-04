#31_flaechenmoment.py
from sympy import *
Iy,y,z,h,b =symbols('Iy,y,z,h,b')
Iy=z**2
zI=integrate(Iy,(y,-b/2,b/2),(z,-h/2,h/2))
print("Flächenmoment\n Iy =",zI)
