#L_03_20.py
class Rechteck:
#Konstruktor
    def __init__(self,breite,hoehe):
        self.b=breite
        self.h=hoehe
    def umfang(self):
        return 2*(self.b+self.h)
    
    def flaeche(self):
        return self.b*self.h
#Hauptprogramm
a=3  #m
b=10 #m
objR=Rechteck(a,b)
print("Rechteck")
print("Umfang:",objR.umfang(),"m")
print("Fläche:",objR.flaeche(),"m^2")




