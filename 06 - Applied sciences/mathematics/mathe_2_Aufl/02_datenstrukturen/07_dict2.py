#07_dict2.py
from random import choice
def frage(d):
    a=choice(list(d.keys()))
    print("Ableitung von:",a,"?")
    aw=input("ist: ")
    if aw != d[a]:
        print("falsch!")
        print("Ableitung von:",a,"ist: ",end="")
        for ableitung in d[a]:
            print(ableitung,end="")
        print() #Zeilenumbruch
    else:
        print("richtig!")
        del d[a]
#dictionary
dicA={'x':'1',
   'sin(x)':'cos(x)',
   'cos(x)':'-sin(x)',
   'ln(x)':'1/x',
   'exp(x)':'exp(x)',
   'cosh(x)':'sinh(x)',
   'sinh(x)':'cosh(x)',
   'sin(a*x)':'a*cos(a*x)',
   }
while dicA:
    frage(dicA)
print("Sie beherrschen alle Ableitungen!")

