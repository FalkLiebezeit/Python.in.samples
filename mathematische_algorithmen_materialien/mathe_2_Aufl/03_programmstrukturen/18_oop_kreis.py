#18_oop_kreis.py
class Kreis:
    from math import pi
    __pi=pi #Klassenvariable
#Konstruktor
    def __init__(self,radius):
        self.__r=radius #Instanzenvariable
#Methode für Flächenberechnung           
    def flaeche(self):
        return self.__r**2*self.__pi
#Methode für Umfangsberechnung      
    def umfang(self):
        return 2*self.__pi*self.__r
#Hauptprogramm
r=10 #Radius in m
objK=Kreis(r) #Konstruktor
#Kreis.__pi=6.28
print("Kreis")
print("Umfang:",objK.umfang(),"m")
print("Fläche:",objK.flaeche(),"m^2")



