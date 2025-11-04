#L_06_03.py
#Kreisflaeche
import numpy as np
import scipy.integrate as integral
r=1

def f(x,r):
    return np.sqrt(r**2-x**2)

a=-r #untere Grenze
b= r #obere Grenze
A1=np.pi*r**2 #genau
A2=2*integral.quad(f,a,b,args=(r))[0]
#Ausgaben
print("Flaeche genau:      ",A1)
print("Flaeche integriert: ",A2)
print("absoluter Fehler:  ",A1-A2)

