#29_oop.py
class Zylinder:
    
    rho=7.85 #kg/dm^3 Klassenvariable
    
    def __init__(self,durchmesser,laenge,alpha):
        self.__d=durchmesser #Instanzenvariable
        self.__l=laenge
        self.__a=alpha
           
    def volumen(self):
        return 0.785*self.__d**2*self.__l
    
    def masse(self):
        return self.rho*self.volumen()
    
    def traegheitsmoment(self):
        return 0.5*self.masse()*(self.__d/2/10)**2
    
    def beschleunigungsmoment(self):
        return self.__a*self.traegheitsmoment()
#Hauptprogramm d und l in dm   
z=Zylinder(1,10,1.2)
#Zylinder.rho=2.3
#z.__d=100
print("Volumen:",z.volumen(),"dm^3")
print("Masse:  ",z.masse(),"kg")
print("Traegheitsmoment:     ",z.traegheitsmoment(),"kgm^2")
print("Beschleunigungsmoment:",z.beschleunigungsmoment(),"Nm")

