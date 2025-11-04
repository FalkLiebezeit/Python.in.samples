#22_dgl_zweimassenschwinger.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
m=1e3    #Masse in kg
c=1e7    #Federkonstante N/m
d=1e3    #Dämpfung kg/s
m1,m2=m,2*m      
c1,c2,c3=c,2*c,3*c
d1,d2,d3=d,2*d,3*d 
tmax=0.2 #Sekunden
#DGL-System
def dgl(t,xa,c1,c2,c3,d1,d2,d3,m1,m2):
    x1,v1,x2,v2=xa
    dx1_dt=v1
    dv1_dt=-(d1*v1+d2*(v1-v2)+c1*x1+c2*(x1-x2))/m1
    dx2_dt=v2
    dv2_dt=-(d3*v2+d2*(v2-v1)+c3*x2+c2*(x2-x1))/m2
    return np.array([dx1_dt,dv1_dt,dx2_dt,dv2_dt])
#Lösung des DGL-Systems
t = np.linspace(0,tmax,500)
x0 = [0.01, 0.0, 0.0, 0.0]#Anfangswerte
parameter=(c1,c2,c3,d1,d2,d3,m1,m2)
z=solve_ivp(dgl,[0,tmax],x0,args=parameter,dense_output=True)
x1,v1,x2,v2 = z.sol(t)
fig,ax=plt.subplots()
#Auslenkung m1
ax.plot(1e3*t, 1e3*x1,'r-',lw=1.5,label=r'Auslenkung von $m_{1}$')
#Auslenkung m2
ax.plot(1e3*t, 1e3*x2,'b-',lw=1.5,label=r'Auslenkung von $m_{2}$')
ax.legend()
ax.set(xlabel='t in ms',ylabel='Auslenkung in mm')
ax.grid(True)
plt.show()

#Quelle für DGL-System: Vöth, S.80

'''
fig.savefig('06_030.png')
fig.savefig('06_030.svg')
'''




