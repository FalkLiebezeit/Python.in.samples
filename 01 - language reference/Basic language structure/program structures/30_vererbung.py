#30_vererbung.py
class Flaeche:
    
    def __init__(self,breite,laenge):
        self.b=breite
        self.l=laenge
        
    def flaeche(self):
        return self.b*self.l
    
class Volumen(Flaeche):
    
    def __init__(self,breite,laenge,hoehe):
        Flaeche.__init__(self,breite,laenge)
        #super().__init__(breite,laenge)
        self.h=hoehe
        
    def volumen(self):
        return Flaeche.flaeche(self)*self.h
        #return super().flaeche()*self.h
    
A=Flaeche(1,2)
V=Volumen(1,2,3)
print("Fläche: ",A.flaeche()," m^2")
print("Volumen:",V.volumen()," m^3")

