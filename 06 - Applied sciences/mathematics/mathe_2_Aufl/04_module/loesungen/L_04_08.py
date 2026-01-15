#L_04_08.py
from sympy import *
x,a=symbols('x a')
#Funktionsdefinitionen
y1=sin(a*x)
y2=cos(a*x)
#1. Ableitung
df1=diff(y1,x)
df2=diff(y2,x)
#Stammfunktionen
F1=integrate(y1,x)
F2=integrate(y2,x)
#Ausgabe
print("sin(ax)' =",df1)
print("cos(ax)' =",df2)
print("∫sin(ax)dx =",F1)
print("∫cos(ax)dx =",F2)