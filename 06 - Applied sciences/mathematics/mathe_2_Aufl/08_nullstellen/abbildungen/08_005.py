#08_005.py
from math import *
import numpy as np
import matplotlib.pyplot as plt
#Nullstellengleichung
def f(x):
    y=exp(x/4)-5*x-1
    #y = x-cos(x)           #a)
    #y = x**2-sin(x)        #b)
    #y = exp(x)- x**2/4 - 2  #c)
    #y = log(x+2)-2*x**2     #d)
    return y
#Fixpunktgleichung
def F(x):
    y=4*np.log(5*x+1)
    #y = cos(x)          #a)
    #y = sqrt(sin(x))    #b)
    #y = log(x**2/4+2)   #c)
    #y=sqrt(log(x+2)/2)  #d)
    return y
#Bisektionsverfahren
def  bisektion(f,a,b,n=10):
    x=0
    for i in range(n):
        x=(a+b)/2
        if f(x)*f(a)<0:
            b=x
        else:
            a=x
    return x
#Fixpunktverfahren
def fixpunkt(F,x0,n=10):
    x=x0
    for i in range(n):
        x=F(x)
    return x
#Newton-Verfahren
def newton(f,x,n=10,h=1e-4):
    for i in range(n):
        x = x - 2*h*f(x)/(f(x+h)-f(x-h))
    return x
fig,ax=plt.subplots()
x0=17
#i=np.arange(1,10,1)
for i in range(1,11):
    ax.plot(i,bisektion(f,x0,19,i),'bo')
    ax.plot(i,fixpunkt(F,x0,i),'gx')
    ax.plot(i,newton(f,x0,i),'r*-')
ax.set_ylim(17.7,18.6)
ax.set_xlabel('Schritte')
ax.set_ylabel('Näherung')
# ax.text(7.7,1.1,'* Newton',color='red')
# ax.text(7.7,0.9,'o Fixpunt',color='green')
# ax.text(7.7,0.8,'x Bisektion',color='blue')
#ax.set_title('* Newton o Fixpunt x Bisektion')
ax.annotate('Bisektionsverfahren', xy=(2.2, 18.5),xycoords='data', xytext=(4, 18.55),
            arrowprops=dict(facecolor='black', shrink=0.001),fontsize=12)
ax.annotate('Fixpunktverfahren', xy=(1.2, 17.82),xycoords='data', xytext=(3.1, 17.8),
            arrowprops=dict(facecolor='black', shrink=0.001),fontsize=12)
ax.annotate('Newton-Verfahren', xy=(1.17, 18.275),xycoords='data', xytext=(3.5, 18.4),
            arrowprops=dict(facecolor='black', shrink=0.001),fontsize=12)

plt.show()


#print(x01)