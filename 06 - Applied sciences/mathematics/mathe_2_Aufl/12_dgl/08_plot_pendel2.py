#08_plot_pendel2.py
from math import degrees,radians
import matplotlib.pyplot as plt
g=9.81 #kgm/s^2
l=0.2  #Länge des Pendels in m
m=0.2  #Masse in kg
c=1.0  #N/m Federkonstante
phi1,phi2=3,6 #Auslenkwinkel in °
phi1,phi2=radians(phi1),radians(phi2)
n=500
t1,t2=0,10
dt=(t2-t1)/n
w1=w2=0
w02=g/l 
k=c/m
lt,lw1,lphi1,lw2,lphi2 =[],[],[],[],[]
for i in range(n):
    t=t1+i*dt
    phi1=phi1+w1*dt 
    w1=w1-w02*phi1*dt-k*(phi1-phi2)*dt
    phi2=phi2+w2*dt 
    w2=w2-w02*phi2*dt+k*(phi1-phi2)*dt
    lt.append(t)
    lphi1.append(degrees(phi1))
    lphi2.append(degrees(phi2))
    lw1.append(w1)
    lw2.append(w2)
#Grafikbereich
fig,ax = plt.subplots()   
ax.plot(lt,lphi1,'r-', label=r'$\varphi_1 \left(t\right)$')
ax.plot(lt,lphi2,'b--',label=r'$\varphi_2 \left(t\right)$')
ax.set_title('gekoppeltes Pendel')
ax.set(xlabel='t',ylabel=r'$\varphi \left(t\right)$')
ax.legend(loc='best')
ax.grid(True)
plt.show()


