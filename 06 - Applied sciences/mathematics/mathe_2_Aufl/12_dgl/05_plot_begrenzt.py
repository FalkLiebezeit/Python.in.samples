#05_plot_begrenzt.py
import matplotlib.pyplot as plt
a=10
b=1
#DGL
def dgl(t,y):
    dy_dt=a-b*y
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

y0=0 #Anfangswert
t1,t2=0,5
t,y=euler(dgl,t1,t2,y0)
#Grafikbereich
fig,ax  = plt.subplots()
ax.plot(t,y,'b-')
ax.plot(t1,y0,'ro',label='Anfangswert')
ax.set(xlabel='t',ylabel='y',title=r'$\dot{y}=a-b\cdot y$')
ax.legend(loc='best')
ax.grid(True)
plt.show()
