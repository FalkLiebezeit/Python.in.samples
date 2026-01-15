#l_05_08.py
#Ableitungen der e-Funktionen berechnen
from sympy import symbols,exp,integrate,diff
x=symbols('x')
f=exp(x)
print("1. Ableitung :",diff(f,x))
print("2. Ableitung :",diff(f,x,2))
print("3. Ableitung :",diff(f,x,3))
print("Stammfunktion:",integrate(f,x))
