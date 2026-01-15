#L_09_04.py
#Ableitungen für ganzrationale  Funktion
from sympy import *
x=symbols('x')
y=(3*x**3 - 2*x**2 + 5*x - 7)/(x**2 + 4)
x0=4
#Berechnung der Ableitungen
df1=diff(y,x,1)
df2=diff(y,x,2)
df3=diff(y,x,3)
df4=diff(y,x,4)
#Berechnung der Steigungen
m1=df1.subs(x,x0)
m2=df2.subs(x,x0)
m3=df3.subs(x,x0)
m4=df4.subs(x,x0)
#Ausgaben
print("Ableitungen der Funktion y =",y)
print("1. Ableitung\n %s an der Stelle %2.2f ist %2.6f\n" %(df1,x0,m1))
print("2. Ableitung\n %s an der Stelle %2.2f ist %2.6f\n" %(df2,x0,m2))
print("3. Ableitung\n %s an der Stelle %2.2f ist %2.6f\n" %(df3,x0,m3))
print("4. Ableitung\n %s an der Stelle %2.2f ist %2.6f\n" %(df4,x0,m4))

