#L_12_03.py
import matplotlib.pyplot as plt
#Definition der DGL
def dgl(x,y):
    dy_dx=x**2+y**2 
    return dy_dx
#Heun-Verfahren
def heun(f,t0,tn,y0,n=500):
    y=y0
    h=(tn-t0)/n
    lt,ly=[t0],[y0]
    for i in range(n):
        t=t0 + i*h
        k1=f(t,y)
        k2=f(t+h,y+h*k1)
        y = y + h*(k1+k2)/2
        lt.append(t)
        ly.append(y)
    return lt,ly
#Runge-Verfahren
def runge(f,t0,tn,y0,n):
    y=y0
    h=(tn-t0)/n
    lt,ly=[t0],[y0]
    for i in range(n):
        t=t0 + i*h
        k1=f(t,y)
        k2=f(t+h/2,y+h*k1/2)
        k3=f(t+h/2,y+h*k2/2)
        k4=f(t+h,y+h*k3)
        y = y + h*(k1+2*k2+2*k3+k4)/6
        lt.append(t)
        ly.append(y)
    return lt,ly

n1=200
y0=-0.5
x1,x2=-1,1
#x,y=heun(dgl,x1,x2,y0,n1)
x,y=runge(dgl,x1,x2,y0,n1)
#Grafikbereich
fig,ax=plt.subplots()
ax.plot(x,y,'b-')
ax.set_title(r"$y^{\prime} =x^{2}+y^{2}$")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
plt.show()




