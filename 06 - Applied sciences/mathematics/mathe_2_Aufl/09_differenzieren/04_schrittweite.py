#02_schrittweite.py
#Funktionsdefinition
def f(x):
    return x**4/32
#1. Ableitung genau
def df1(x):
    return x**3/8
#Vorwärtsdifferenzenquotient
def vDiff(f,x,h=1e-1):
    return (f(x+h)-f(x))/h
#zentraler Differenzenquotient
def zDiff(f,x,h=1e-1):
    return (f(x+h)-f(x-h))/(2*h)
#Hauptprogramm
x0=2
print("h\tFehler Ev\tFehler Ez")
for n in range(1,11):
    h=10**(-n)
    E1=abs(df1(x0) - vDiff(f,x0,h))
    E2=abs(df1(x0) - zDiff(f,x0,h))
    print("%1.e %1.12f %1.12f" %(h,E1,E2))
   

    