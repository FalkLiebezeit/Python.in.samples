#21_bruch2.py
from random import randint
from fractions import Fraction
i=0
p=0 #Punkte
pmax=5
while i<pmax:
    z1,n1=randint(1,9),randint(1,9)
    z2,n2=randint(1,9),randint(1,9)
    a=Fraction(z1,n1)
    b=Fraction(z2,n2)
    s=a+b
    print(a,"+",b,"= ?")
    e=Fraction(input("Ergebis: "))
    if e==s:
        print("Richtig!")
        p=p+1
    else:
        print("Falsch!")
        print("Richtiges Ergebnis:",s)
    i=i+1
print("Erreichte Punktzahl:",p," von ", pmax)