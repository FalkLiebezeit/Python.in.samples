#15_zweifach_integral.py
import scipy.integrate as integral
b=5   #Breite in cm
h=10  #Höhe in  cm
#Funktionsdefinition
def f(y,z):
    return z**2
#Berechnung   
Iy=integral.dblquad(f,-h/2,h/2,-b/2,b/2)[0]
print("Iy =",Iy,"cm^4")
print("Iy =",b*h**3/12,"cm^4 genau")