#31_projekt_welle.py
from math import sqrt,pi
g=9.81     #Erdbeschleunigung
rho=7.85   #kg/dm^3
E=216e3    #N/mm^2
l=120      #mm      
sigma=100  #N/mm^2
m=1        #kg
#Berechnungen
F=m*g
Mb=F*l/4
d=pow((32*Mb)/(pi*sigma),1/3)
d=round(d+0.5)
Ia=pi*d**4/64.0
f=F*l**3/(48*E*Ia)
Rb=48*E*Ia/l**3    #F/f
nk=sqrt(1e3*Rb/m)/(2*pi)
#Ausgaben
print("Durchmesser in mm:",round(d,2))
print("Durchbiegung in mm:",round(f,3))
print("kritische Drehzahl 1/min:",int(60*nk))