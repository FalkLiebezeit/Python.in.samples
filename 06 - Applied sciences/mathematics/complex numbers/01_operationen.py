#01_operationen.py
import numpy as np
n=3
z1=5-12j
z2=np.complex(3,4)
z2conj=np.conjugate(z2)
rez2=np.real(z2)
imz2=np.imag(z2)
betrag=np.abs(z2)
winkel=np.angle(z2)
s=z1+z2
d=z1-z2
p=z1*z2
q=z1/z2
pot=z2**n
w=np.sqrt(z2)
lg=np.log(z2)
hs=np.sinh(z2)
#Ausgaben
print("Komplexe Zahl z1:",z1)
print("Komplexe Zahl z2:",z2)
print("Konjugierte   z2:",z2conj)
print("Realteil      z2:",rez2)
print("Imaginärteil  z2:",imz2)
print("Betrag von    z2:",betrag)
print("Winkel von    z2:",np.angle(z2,deg=True),"°")
print("Summe von  z1+z2:",s)
print("Differenz  z1-z2:",d)
print("Produkt    z1*z2:",p)
print("Quotient   z1/z2:",q)
print("%1d.Potenz"%n,"von  z2:",pot)
print("Wurzel aus    z2:",w)
print("Logarithmus   z2:",lg)
print("sinh          z2:",hs)
print("Type von z1:",type(z1))
print("Type von z2:",type(z2))