#U_01_01.py
summe=0
n=300
for i in range(1,n+1,1):
    summe=summe+1/i**2 #absteigende Werte
print(summe)
summe=0
for i in range(n,0,-1):
    summe=summe+1/i**2 #aufsteigende Werte
print(summe) 
#genau
from sympy.abc import i
from sympy import Sum
s=Sum(1/i**2, (i,1,n)).doit().evalf(20)
print(s)
'''
Faustregel:
Beim Addieren sollte man die Summanden in der Reihenfolge
der aufsteigenden Beträge addieren.
[Knorrenschild:6]
'''