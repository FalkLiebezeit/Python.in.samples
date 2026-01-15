#02_plot_euler.py
import matplotlib.pyplot as plt
#Definition der DGL
def dgl(t,a):
    dy_dt=a*t
    return dy_dt
#Lösung der DGL
n=10         #Anzahl der Schritte
t0,tn=0,10   #Intervall
a=1
y=y0=10      #Anfangswert
h=(tn-t0)/n #Schrittweite
lt,ly,lyg =[t0],[y0],[y0]
for i in range(n):
    t=t0 + i*h
    y = y + dgl(t,a)*h #Euler-Verfahren
    yg=a*t**2/2 + y0   #genau
    lt.append(t)
    ly.append(y)
    lyg.append(yg)    
#Darstellung
fig,ax=plt.subplots()
ax.plot(lt,ly, "b--",label="ungenau")
ax.plot(lt,lyg,"r",  label="genau")
ax.plot(t0,y0,"kx")
ax.set(xlabel="t",ylabel="y(t)",title=r"$\dot{y} =a\cdot t$")
ax.legend(loc='best')
ax.grid(True)
plt.show()
