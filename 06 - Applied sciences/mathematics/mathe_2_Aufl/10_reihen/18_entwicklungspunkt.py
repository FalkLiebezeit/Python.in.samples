#18_entwicklungspunkt.py
from sympy import *
x=symbols('x')
n=3     #Anzahl der Glieder
x0=pi/2 #Entwicklungspunkt
f1=sin(x)
r=series(f1,x,x0,n)
f2=r.removeO()
print("sin(x) =",r)
print("sin(x) =",f2)
p1=plot(f1,(x,0,pi),show=False,line_color='blue')
p2=plot(f2,(x,0,pi),show=False,line_color='red')
p1.extend(p2)
p1.show()




