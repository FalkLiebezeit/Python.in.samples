#L02_09.py
class Fahrzeug(object):
    
    rho=1.3 #Klassenvariable
    
    def __init__(self,beiwert,querschnitt,geschwindigkeit,zeit):
        self.__cw=beiwert #Instanzenvariable
        self.__A=querschnitt
        self.__v=geschwindigkeit
        self.__t=zeit
           
    def kraft(self):
        return 0.5*self.rho*self.__cw*self.__A*self.__v**2
    
    def leistung(self):
        return self.kraft()*self.__v
    
    def arbeit(self):
        return self.leistung()*self.__t
       
#Hauptprogramm   
F1=Fahrzeug(0.3,1.5,36,120)
print("Kraft:",F1.kraft(),"N")
print("Leistung:",F1.leistung(),"W")
print("Arbeit:  ",F1.arbeit(),"Ws")


