#28_funktional.py
rho=7.85  #kg/dm^3
volumen=lambda d,l: 0.785*d**2*l
masse=  lambda d,l: rho*volumen(d,l)
traegheitsmoment=lambda d,l: 0.5*masse(d,l)*(d/2/10)**2
beschleunigungsmoment=lambda d,l,omega:omega*traegheitsmoment(d,l)
#Ausgabe d und l in dm
print("Volumen:",volumen(1,10), "dm^3")
print("Masse:",masse(1,10),"kg")
print("Traegheitsmoment:",traegheitsmoment(1,10),"kgm^2")
print("Beschleunigungsmoment:",beschleunigungsmoment(1,10,1.2),"Nm")