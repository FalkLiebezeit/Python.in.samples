#07_plot_pendel1.py
from math import degrees,radians,sin
import matplotlib.pyplot as plt
g=9.81    #kgm/s^2
l=0.92    #Länge des Pendels in m
D=0.2     #Abklingkonstante in 1/s
phi=60    #Auslenkwinkel in Grad
phi=radians(phi) 
n=500
t1,t2=0,5
dt=(t2-t1)/n
w=0       #Anfangswinkelgeschwindigkeit
w02=g/l
lt,lw,lphi =[],[],[]
for i in range(n):
    t=t1+i*dt
    phi=phi+w*dt 
    w=w-w02*sin(phi)*dt - D*w*dt
    lt.append(t)
    lw.append(w)
    lphi.append(degrees(phi))
#Grafikbereich
fig,ax = plt.subplots(2,1)
#Auslenkung
ax[0].plot(lt,lphi,'r-')
ax[0].set_title("Fadenpendel")
ax[0].set_ylabel(r"$\varphi \left(t\right)$")
ax[0].grid()
#Winkelgeschwindigkeit
ax[1].plot(lt,lw,'b-')
ax[1].set_xlabel('t')
ax[1].set_ylabel(r"$\omega \left(t\right)$")
ax[1].grid()
plt.show()

