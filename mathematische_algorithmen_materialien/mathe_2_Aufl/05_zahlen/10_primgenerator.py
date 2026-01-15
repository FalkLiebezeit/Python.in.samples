#13_primgenerator.py
from sympy import sqrt,primerange
def primzahl(us,os):
    primZahlen=[]
    istPrim=False
    n=0
    for zahl in range(us,os):
        istPrim=True
        kmax=int(sqrt(zahl))+1 #größter Teiler
        for k in range(2,kmax): 
            if zahl%k==0:     #ohne Rest teilbar
                istPrim=False #also keine Primzahl
                break
        if istPrim:
            n=n+1  #zähle Primzahlen
            primZahlen.append(zahl)
    return primZahlen,n
#Hauptprogramm
u=2
o=50
pz=primzahl(u,o)
pz_sympy=[i for i in primerange(u,o)]
print(pz)
print("",pz_sympy,len(pz_sympy))

