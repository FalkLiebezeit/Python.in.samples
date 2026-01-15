#04_plot_exponentiell.py
import matplotlib.pyplot as plt
a=1 #Anfangswert
b=1 #Wachstumskonstante
#DGL
def dgl(t,y):
    dy_dt=b*y
    return dy_dt

n=100     #Anzahl der Schritte
t0,tn=0,2 #Zeitintervall
y=a       #Anfangswert
h=(tn-t0)/n
lt,ly=[t0],[y]
for i in range(n):
    t = t0 + i*h
    y = y + dgl(t,y)*h #Euler-Verfahren
    lt.append(t)
    ly.append(y)
#Grafikbereich
fig,ax=plt.subplots()
ax.plot(lt,ly, 'b-')
ax.plot(t0,a,'ro',label="Anfangswert")
ax.set(xlabel='t',ylabel='y(t)',title=r'$\dot{y} =b\cdot y$')
ax.legend(loc='best')
ax.grid(True)
plt.show()


