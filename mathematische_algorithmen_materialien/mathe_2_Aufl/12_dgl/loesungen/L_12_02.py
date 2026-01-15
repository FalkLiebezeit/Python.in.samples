#L_12_02.py
#Genauigkeit des Euler-Verfahrens
import numpy as np
import matplotlib.pyplot as plt
#DGL
def dgl(x,y):
    dy_dx=np.sin(x)
    return dy_dx
#Euler-Verfahren
def euler(f,t0,tn,y0,n=500):
    y=y0  #Anfangswert
    h=(tn-t0)/n
    lt,ly =[],[]
    for i in range(n):
        t=t0 + i*h
        y = y + f(t,y)*h 
        lt.append(t)
        ly.append(y)
    return lt,ly

y0=-1 #Anfangswert
x1,x2=0,2*np.pi
x=np.linspace(x1,x2,200)
t,y=euler(dgl,x1,x2,y0,20)
#Grafikberiech
fig, ax=plt.subplots(figsize=(8,6))
ax.plot(t,y,"rx")
ax.plot(x,-np.cos(x),"b-")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
plt.show()