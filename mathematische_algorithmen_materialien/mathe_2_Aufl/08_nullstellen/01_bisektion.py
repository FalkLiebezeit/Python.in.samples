#01_bisektion.py
from math import *
#Funktionsdefinition
def f(x):
    return exp(x/4)-5*x-1
#Hauptprogramm
d=6
a,b=17,19
m=log2(b-a)+d*log2(10)+1
Ev=abs(a-b)/(2**(int(m)))
n=0
x=(a+b)/2
eps=10**-d #Genauigkeit
print("%3s %9s %12s %15s %10s"%("n","a","x","b","f(x)"))
while abs(a-b)>eps:
    print(" %2d  %.10f  %.10f  %.10f  %+0.0f" %(n,a,x,b,f(x)))
    x=(a+b)/2
    if f(x)*f(a)<0:
        b=x
    else:
        a=x
    E=abs(a-b)/2
    n=n+1
#Fehlerabschätzung
print("\t\t    18.05565017206474  genau")
print("A-priori Fehlerabschätzung",round(Ev,d))
print(m)
'''
#Wertetabelle
for x in range(17,20,1):
    print(x,f(x))
'''   