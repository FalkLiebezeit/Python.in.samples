#12_wahrscheinlichkeit.py
import numpy as np
from scipy.integrate import quad

def f(x,sigma,my):
    y=np.exp(-0.5*(x-my)**2/sigma**2)/(sigma*np.sqrt(2*np.pi))
    return y

s=1
m=0

w1=quad(f,  -s,  s,args=(s,m))
w2=quad(f,-2*s,2*s,args=(s,m))
w3=quad(f,-3*s,3*s,args=(s,m))
wp1,wp2,wp3=100*w1[0],100*w2[0],100*w3[0]

print("Erwartungswert zwischen  -\u03C3 und  +\u03C3: %2.2f%%"%wp1)
print("Erwartungswert zwischen -2\u03C3 und +2\u03C3: %2.2f%%"%wp2)
print("Erwartungswert zwischen -3\u03C3 und +3\u03C3: %2.2f%%"%wp3)