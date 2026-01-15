#10_plot_epidemie.py
import numpy as np
import matplotlib.pyplot as plt
b=0.4  #Infektionsrate
g=0.04 #Genesungsrate
#DGL für SIR-Modell
def dgl(t,y1,y2,y3,N):
    dy1_dt=-b*y1*y2/N     #gesunde
    dy2_dt=b*y1*y2/N-g*y2 #infizierte
    dy3_dt=g*y2           #genesen
    return dy1_dt,dy2_dt,dy3_dt
#Lösung der DGL
n=500   #Anzahl der Schritte
t1,t2=0,120
dt=(t2-t1)/n #Schrittweite
t=np.linspace(t1,t2,n+1)
y10=997 #Gesunde
y20=3   #Infizierte
y30=0   #Genesene
N=y10+y20+y30
y1,y2,y3=np.empty(n+1),np.empty(n+1),np.empty(n+1)
y1[0],y2[0],y3[0]=(y10,y20,y30) #Anfangswerte
for i in range(n):
    dy1,dy2,dy3 = dgl(t,y1[i],y2[i],y3[i],N)
    y1[i+1] = y1[i] + dy1*dt
    y2[i+1] = y2[i] + dy2*dt
    y3[i+1] = y3[i] + dy3*dt
#Grafikbereich
fig,ax = plt.subplots()
ax.plot(t,y1,'b--',label='Gesunde')
ax.plot(t,y2,'r-.',label='Infizierte')
ax.plot(t,y3,'g-',  label='Genesene')
ax.set_xlabel('Zeit')
ax.legend(loc='best')
ax.grid(True)
plt.show()

