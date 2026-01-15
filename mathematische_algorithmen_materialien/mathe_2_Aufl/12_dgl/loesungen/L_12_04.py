#L_12_04.py
#Simulation einer Epidemie mit Todesfällen
import numpy as np
import matplotlib.pyplot as plt
#
def dgl(t,x,y,z,v,N,b=0.4,g=0.04,m=0.005):
    dx_dt=-b*x*y/N        #gesund
    dy_dt=b*x*y/N-g*y-m*y #infiziert
    dz_dt=g*y             #genesen
    dv_dt=m*y             #verstorben
    return dx_dt,dy_dt,dz_dt,dv_dt

n=500   #Anzahl der Schritte
t1=0
t2=120
dt=(t2-t1)/(n-1) #Schrittweite
t=np.linspace(t1,t2,n+1)
x0=997 #Gesunde
y0=3   #Infizierte
z0=0   #Genesene
v0=0   #Verstorbene
N=x0+y0+z0-v0
x = np.empty(n+1)
y = np.empty(n+1)
z = np.empty(n+1)
v = np.empty(n+1)
#Anfangswerte
x[0],y[0],z[0],v[0]=(x0,y0,z0,v0)
#Lösen der DGL
for i in range(n):
    dx,dy,dz,dv = dgl(t,x[i],y[i],z[i],v[i],N)
    x[i+1] = x[i] + dx*dt
    y[i+1] = y[i] + dy*dt
    z[i+1] = z[i] + dz*dt
    v[i+1] = v[i] + dv*dt
#Ausgabe
fig, ax = plt.subplots(figsize=(8,6))  
ax.plot(t,x,'b',  label='Gesunde')
ax.plot(t,y,'r--',label='Infizierte')
ax.plot(t,z,'g',ls='dotted',label='Genesene')
ax.plot(t,v,'k-.',label='Verstorbene')
ax.legend(loc='best')
ax.set_xlabel('Zeit')
ax.grid()
plt.show()


