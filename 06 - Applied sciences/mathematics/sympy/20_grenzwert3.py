#20_grenzwert3.py
from sympy import *
a,x,h,n=symbols('a x h n')
f1_1=((x+h)**n-x**n)/h       #Potenzregel
f1_2=(a**(x+h)-a**x)/h       #Exponetialfunktion
f1_3=(sin(x+h)-sin(x))/h     #trigonometrische Funktion
f1_4=(sinh(x+h)-sinh(x))/h   #hyberbolische Funktion
f1_5=(sin(x+h)*cos(x+h)-sin(x)*cos(x))/h #Produktregel
#Ausgabe
print("Grenzwerte für h gegen null")
print("limes",f1_1," = ",simplify(limit(f1_1,h,0)))
print("limes",f1_2," = ",simplify(limit(f1_2,h,0)))
print("limes",f1_3," = ",simplify(limit(f1_3,h,0)))
print("limes",f1_4," = ",simplify(limit(f1_4,h,0)))
print("limes",f1_5," = ",simplify(limit(f1_5,h,0)))

