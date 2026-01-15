#L_02_03.py
from random import choice
def frage(d):
    a=choice(list(d.keys()))
    print("Stammfunktionen von:",a,"?")
    aw=input("ist: ")
    if aw != d[a]:
        print("falsch!")
        print("Stammfunktionen von:",a,"ist: ",end="")
        for stammmfunktionen in d[a]:
            print(stammfunktionen,end="")
        print() #Zeilenumbruch
    else:
        print("richtig!")
        del d[a]
#dictionary
dicA={'a':'ax',
   '1/x':'ln(x)',
   'exp(x)':'exp(x)',
   'sinh(x)':'cosh(x)',
   'cosh(x)':'sinh(x)',
   'tan(x)':'-ln|cos(x)|',
   }
while dicA:
    frage(dicA)
print("Sie beherrschen alle Stammfunktionen!")


