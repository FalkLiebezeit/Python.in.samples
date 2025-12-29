#L_02_10.py
class Volumen:
    def __init__(self,durchmesser,laenge):
        self.d=durchmesser
        self.l=laenge
        
    def volumen(self):
        return 0.785*self.l*self.d**2
    
class Masse(Volumen):   
    def __init__(self,rho,durchmesser,laenge):
        super().__init__(durchmesser,laenge)
        self.r=rho
        
    def masse(self):
        return Volumen.volumen(self)*self.r

class Traegheitsmoment(Masse):
    def __init__(self,rho,durchmesser,laenge):
        super().__init__(rho,durchmesser,laenge)
    
    def traegheitsmoment(self):
        return Masse.masse(self)*self.d**2/8/100

class Beschleunigungsmoment(Traegheitsmoment):
    def __init__(self,rho,durchmesser,laenge,alpha):
        self.a=alpha
        super().__init__(rho,durchmesser,laenge)
    
    def beschleunigungsmoment(self):
        return Traegheitsmoment.traegheitsmoment(self)*self.a

#Hauptprogramm
d=1           #Durchmesser in dm
l=10          #Laenge in dm
rho1=7.86     #Dichte kg/dm^3
alpha1=1.2    #Winkelbeschleunigung 1/s^2
V=Volumen(d,l)
m=Masse(rho1,d,l)
J=Traegheitsmoment(rho1,d,l)
Mb=Beschleunigungsmoment(rho1,d,l,alpha1)
print("Volumen:",V.volumen()," m^3")
print("Masse:",m.masse()," kg")
print("Trägheitsmoment:",J.traegheitsmoment()," kgm^2")
print("Beschleunigungsmomnet:",Mb.beschleunigungsmoment()," Nm")


