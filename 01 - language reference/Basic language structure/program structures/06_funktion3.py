#06_funktion3.py
rho=7.85   #kg/dm^3, Dichte für Stahl 
alpha=1.2  #1/s^2
g=3        #Nachkommastellen

def zylinder(d,l):
    V=round(0.785*d**2*l,g)
    m=round(rho*V,g)
    J=round(0.5*m*(d/2/10)**2,g) #dm in m umwandeln
    Mb=round(alpha*J,g)
    return (V,m,J,Mb)
    #return V,m,J,Mb
    #return [V,m,J,Mb]

d1=1   #dm
l1=10  #dm
T=zylinder(d1, l1)
print("Zylinderdaten: ", T)
print("Volumen:              ", T[0]," dm^3")
print("Masse:                ", T[1]," kg")
print("Traegheitsmoment:     ", T[2]," kgm^2")
print("Beschleunigungsmoment:", T[3]," Nm")



