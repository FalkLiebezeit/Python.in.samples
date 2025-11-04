#07_funktion4.py
rho=7.85 #kg/dm^3

def volumen(d,l):
    return 0.785*d**2*l

def masse(d,l):
    return rho*volumen(d,l)

def traegheitsmoment(d,l):
    return 0.5*masse(d,l)*(d/2/10)**2

def beschleunigungsmoment(d,l,alpha):
    return alpha*traegheitsmoment(d,l)

d1=1  #dm
l1=10 #dm
alpha1=1.2 #1/s^2
V=volumen(d1,l1)
m=masse(d1,l1)
J=traegheitsmoment(d1,l1)
Mb=beschleunigungsmoment(d1,l1,alpha1)
print("Volumen:               ", V, " dm^3")
print("Masse:                 ", m, " kg")
print("Traegheitsmoment:      ", J, " kgm^2")
print("Beschleunigungsmoment: ", Mb, " Nm")
