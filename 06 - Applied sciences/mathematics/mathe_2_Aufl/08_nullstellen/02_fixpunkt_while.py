#02_fixpunkt_while.py
from math import *
#Fixpunktgleichung
def F(x):
    return 4*log(5*x+1)
#1. Ableitung
def diff1(x):
    return 20/(5*x + 1)
#Hauptprogramm
d=6
x=18
eps=10**-d
a,b=17,19
m=9
x1=F(x)
K=round(max(abs(diff1(a)),abs(diff1(b))),4)
Ev=K**m*abs(x-x1)/(1-K)
xa=n=0
print("%2s %8s %15s" %("n","x","F(x)"))
while abs(xa-x) > eps and n<100:
    xa=x
    x=F(x)
    print("%2d  %.10f  %.10f" %(n,x,F(x)))
    n=n+1
#Fehlerabschätzung
En=K/(1.- K)*abs(xa-x)
print("    18.05565017206474  genau")
print("A-priori Fehlerabschätzung    ",round(Ev,d+2))
print("A-posteriori Fehlerabschätzung",round(En,d+2))
print("Kontraktionskonstante K =",K)


# from sympy import *
# x=symbols('x')
# f=exp(x/4)-5*x-1
# F=4*log(5*x+1)
# print(diff(F,x,1))
# print(diff(F,x,2))

# m=np.log(eps*(1-K)/abs(x[0]-x[1]))/np.log(K)
# m=int(m)

# print("%.10f  %.10f" %(x[0],x[1]))
# print("%.10f  %.10f" %(x[n-2],x[n-1]))





