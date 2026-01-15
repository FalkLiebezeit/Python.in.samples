#06_plot_logistisch.py
import matplotlib.pyplot as plt
a=10 #Grenze a/b
b=0.2
#DGL
def dgl(t,y):
    dy_dt=y*(a-b*y)
    return dy_dt
#Lösung der DGL
def euler(f,t0,tn,y0,n=500):
    y=y0  #Anfangswert
    h=(tn-t0)/n
    lt,ly =[t0],[y0]
    for i in range(n):
        t=t0 + i*h
        y = y + f(t,y)*h 
        lt.append(t)
        ly.append(y)
    return lt,ly

y0=0.1 #Anfangswert
t1,t2=0,2
t,y = euler(dgl,t1,t2,y0)
#Grafikbereich
fig,ax = plt.subplots()
ax.plot(t,y,'b-')
ax.plot(t1,y0,'ro',label='Anfangswert')
ax.set_title(r'$\dot{y}=y\cdot\left( a- b\cdot y\right)$')
ax.set(xlabel='t',ylabel='y')
ax.legend(loc='best')
ax.grid(True)
plt.show()

