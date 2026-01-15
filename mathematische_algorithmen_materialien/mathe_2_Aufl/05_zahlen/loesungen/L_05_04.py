#L_05_04.py
#Bruchrechentrainer
from random import randint
from fractions import Fraction
i=0
pmax=5
p=0
def aufgabe(w):
    global p #Punkte
    z1,n1=randint(1,9),randint(1,9)
    z2,n2=randint(1,9),randint(1,9)
    a=Fraction(z1,n1)
    b=Fraction(z2,n2)
    if w==1:
        c=a+b
        print(a,"+",b,"= ?")
        e=Fraction(input("Ergebis: "))
        if e==c:
            print("Richtig!")
            p=p+1
        else:
            print("Falsch!")
            print("Richtiges Ergebnis:",c)
    elif w==2:
        c=a*b
        print(a,"*",b,"= ?")
        e=Fraction(input("Ergebis: "))
        if e==c:
            print("Richtig!")
            p=p+1
        else:
            print("Falsch!")
            print("Richtiges Ergebnis:",c)
    elif w==3:
        c=a-b
        print(a,"-",b,"= ?")
        e=Fraction(input("Ergebis: "))
        if e==c:
            print("Richtig!")
            p=p+1
        else:
            print("Falsch!")
            print("Richtiges Ergebnis:",c)
    elif w==4:
        c=a/b
        print(a,":",b,"= ?")
        e=Fraction(input("Ergebis: "))
        if e==c:
            print("Richtig!")
            p=p+1
        else:
            print("Falsch!")
            print("Richtiges Ergebnis:",c)

while i<pmax:
    wa=randint(1,4)
    aufgabe(wa)
    i=i+1
print("Erreichte Punktzahl:",p," von ", pmax)
