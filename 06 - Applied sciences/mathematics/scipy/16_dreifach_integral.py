#16_dreifach_integral.py
import numpy as np
import scipy.integrate as integral
g=9.81     #Erdbeschleunigung
rho_0=1.28 #Luftdichte
p0=10e5    #Luftdruck
alpha=g*rho_0/p0

def dichte(z,x,y):
    return rho_0*np.exp(-alpha*z)
    
a=1 #x2
b=1 #y2
h=8.223e3 #Höhe der Luftsäule in m
#Masse der Luftsäule
m1=a*b*rho_0*(1-np.exp(-alpha*h))/alpha
#x1,x2,y1,y2,z1,z2
m2=integral.tplquad(dichte,0,a,0,b,0,h)[0]
print("Masse der Luftsäule m1:",m1,"kg")
print("Masse der Luftsäule m2:",m2,"kg")
