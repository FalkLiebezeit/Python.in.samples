#d_berechnen.py
from sympy import prime,gcdex,mod_inverse
#geheimen Schlüssel berechnen
def geheimerSchluessel(e,phi):
    gefunden = False
    d = 1
    while d <= phi and not gefunden:
        if (e*d) % phi == 1:
            gefunden = True
        else:
            d = d + 1
    return d
#Hauptprogramm
e=47
p,q=prime(50),prime(60)
phi=(p-1)*(q-1)
print("e =",e,", phi =",phi)
print("d =",geheimerSchluessel(e,phi))
print("d =",gcdex(e,phi)[0])
print("d =",mod_inverse(e,phi))
