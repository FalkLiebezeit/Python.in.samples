#04_sum_divergenz.py
from sympy import *
n=symbols('n')
an=1/n  #harmonische Folge
bn=n**2 #Folge der Quadratzahlen
S_an=Sum(an,(n,1,oo)).doit()
S_bn=Sum(bn,(n,1,n)).doit()
print("Summe der harmonischen Reihe..:",S_an)
print("Partialsumme der Quadratzahlen:",S_bn)
print("vereinfachte Summenformel.....:",simplify(S_bn))