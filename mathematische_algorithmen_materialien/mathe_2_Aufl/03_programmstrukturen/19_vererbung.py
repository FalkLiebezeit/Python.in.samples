#19_vererbung.py
from kreis import *
#Zylinder erbt von Kreis
class Zylinder(Kreis):
    def __init__(self,radius,hoehe):
        super().__init__(radius)
        self.r=radius
        self.h=hoehe
#Methode für Oberflächenberechnung    
    def oberflaeche(self):
        return super().umfang()*self.h+2*super().flaeche()
#Methode für Volumenberechnung       
    def volumen(self):
        return super().flaeche()*self.h
#Hauptprogramm
r=1 #Radius in m
h=5 #Höhe in m
objZ=Zylinder(r,h)
print("Zylinder")
print("Oberfläche:",objZ.oberflaeche(),"m^2")
print("Volumen:   ",objZ.volumen(),"m^3")
#Typabfrage
print(type(Kreis))
print(type(Zylinder))
print(type(Kreis.flaeche))
print(type(Zylinder.volumen))
print(type(objZ.volumen))





