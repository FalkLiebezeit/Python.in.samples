#11_heun_runge.py
from math import exp
def dgl(t,y):
    dy_dt=t*y
    return dy_dt
#Euler-Verfahren
def euler(f,t0,tn,y0,n):
    y=y0
    h=(tn-t0)/n
    lt,ly=[],[y0]
    for i in range(n):
        t=t0 + i*h
        y = y + f(t,y)*h 
        lt.append(t)
        ly.append(y)
    return lt,ly
#Heun-Verfahren
def heun(f,t0,tn,y0,n):
    y=y0
    h=(tn-t0)/n
    lt,ly=[],[y0]
    for i in range(n):
        t=t0 + i*h
        k1=f(t,y)
        k2=f(t+h,y+h*k1)
        y = y + h*(k1+k2)/2
        lt.append(t)
        ly.append(y)
    return lt,ly
#Runge-Kutta-Verfahren
def runge(f,t0,tn,y0,n):
    y=y0
    h=(tn-t0)/n
    lt,ly=[],[y0]
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

n=6
t0,tn=0,1.2
y0=1         #Anfangswert
h=(tn-t0)/n  #Schrittweite
t,y1=euler(dgl,t0,tn,y0,n)
t,y2= heun(dgl,t0,tn,y0,n)
t,y3=runge(dgl,t0,tn,y0,n)
print("Schrittweite h =",round(h,3))
print("t \tEuler \t Heun\t Runge\tgenau")
for i in range(n):
    print("%2.2f %2.6f %2.6f %2.6f %2.6f" \
          %(t[i],y1[i],y2[i],y3[i],exp(t[i]**2/2)))
