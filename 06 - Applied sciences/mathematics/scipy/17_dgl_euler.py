#17_dgl_euler.py
import math as math
import matplotlib.pyplot as plt

def f(x,y):
    return x*y

x0=0
xk=2
y=1    #Anfangswert
h=0.25 #Schrittweite
n=int((xk-x0)/h)
lx,lyu,lyg =[],[],[]
for k in range(n):
    x=x0+k*h
    y=y+h*f(x,y) #Euler-Verfahren
    yg=math.exp(x**2/2) #genau
    lx.append(x)
    lyu.append(y)
    lyg.append(yg)
fig, ax = plt.subplots()    
ax.plot(lx,lyu,"b--",label="ungenau")
ax.plot(lx,lyg,"r-",label="genau")
ax.set(xlabel="x",ylabel="y")
ax.legend(loc="best")
plt.show()

