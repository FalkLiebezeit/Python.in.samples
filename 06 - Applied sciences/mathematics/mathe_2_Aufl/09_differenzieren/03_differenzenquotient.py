#03_differenzenquotient.py
from math import degrees,atan
#Funktionsdefinition
def f(x):
    return x**4/32
#1. Ableitung genau
def df1(x):
    return x**3/8
#Vorwärtsdifferenzenquotient
def diff_v(f,x,h=1e-2):
    return (f(x+h)-f(x))/h
#Rückwärtsdifferenzenquotient
def diff_r(f,x,h=1e-2):
    return (f(x)-f(x-h))/h
#zentraler Differenzenquotient
def diff_z(f,x,h=1e-2):
    return (f(x+h)-f(x-h))/(2*h)
#Hauptprogramm
x0=2   #Stelle der Steigung
h=1e-3 #Schrittweite
m1=diff_v(f,x0,h) #vorwaerts
m2=diff_r(f,x0,h) #rueckwaerts
m3=diff_z(f,x0,h) #zentral
m4=df1(x0) #genau
alpha1=degrees(atan(m1))
alpha2=degrees(atan(m2))
alpha3=degrees(atan(m3))
alpha4=degrees(atan(m3))
print("Funktion y = x**4/32")
print("1. Ableitung: x**3/8")
print("Schrittweite h =",h)
print("Steigung an der Stelle x0 =",x0)
print("Vorwärtsdifferenzenquotient   m = %2.6f %s=%2.1f°"%(m1,chr(945),alpha1))
print("Rückwärtsdifferenzenquotient  m = %2.6f %s=%2.1f°"%(m2,chr(945),alpha2))
print("zentraler Differenzenquotient m = %2.6f %s=%2.1f°"%(m3,chr(945),alpha3))
print("Differentialquotient          m = %2.6f %s=%2.1f°"%(m4,chr(945),alpha4))

Ev=abs(df1(x0)-m1)
Er=abs(df1(x0)-m2)
Ez=abs(df1(x0)-m3)
print("%e" %Ev)
print("%e" %Er)
print("%e" %Ez)
print("%e" %(Ev/Ez))

'''
((2+0.001)**4/32-2**4/32)/0.001
(2**4/32-(2-0.001)**4/32)/0.001
((2+0.001)**4/32-(2-0.001)**4/32)/(2*0.001)
'''
