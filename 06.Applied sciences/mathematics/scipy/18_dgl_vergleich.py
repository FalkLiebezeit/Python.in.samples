#18_dgl_vergleich.py
import numpy as np
from scipy.integrate import odeint,solve_ivp

def dgl(x,y):
    dy_dx=y*x
    return dy_dx

n=5
xmax=1
y0=[1]      #Anfangswert
xi=[0,xmax] #Integrationsbereich
x = np.linspace(0,xmax,n)
#Lösungen
y1 = np.exp(x**2/2)   #genau
y2 = odeint(dgl,y0,x)
#Methoden für solve_ivp
#RK45,RK23,DOP853,Radau,BDF,LSODA
z3 = solve_ivp(dgl,xi,y0,method='RK45',dense_output=True)
y3 = z3.sol(x)
#Vergleich
print("genau :",y1)
print("odeint:",y2.reshape(n,))
print("ivp   :",y3.reshape(n,))

