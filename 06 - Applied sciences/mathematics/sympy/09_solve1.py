#09_solve1.py
from sympy import *
x1,x2,x3,x4 = symbols('x1 x2 x3 x4')
#lineares Gleichungssystem
g1=7*x1+5*x2-2*x3+7*x4-9
g2=6*x1+3*x2-4*x3+6*x4-8
g3=3*x1+2*x2-5*x3+5*x4-4
g4=2*x1+9*x2-6*x3+3*x4-2
#Lösung
L=solve((g1,g2,g3,g4),x1,x2,x3,x4)
#Ausgabe
print("Lösungsmenge\n",L)

'''
from sympy import symbols, solve, pprint
'''



