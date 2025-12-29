#L02_02.py
import math
c=3e8 #Lichtgeschwindigkeit
v=2e8
m0=10
a=3
b=4
x=10
#Berechnungen
c1=math.sqrt(a**2+b**2)
m=m0/math.sqrt(1.0-(v/c)**2)
y1=math.log(math.cosh(x))
y2=math.atan(x/a)/a
#Ausgaben
print(c1)
print(m)
print(y1)
print(y2)