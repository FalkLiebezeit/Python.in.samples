#21_pi_vieta_wallis.py
from math import pi,sqrt
#1593
def viete(n):
    a1=sqrt(2)/2
    a=a1
    p=1
    for _ in range(2,n):
        a=sqrt(2+2*a)/2
        p=p*a
    return 2/(a1*p)
#1655
def wallis(n):
    p=1
    for k in range(1,n):
        zaehler=4*k**2
        nenner=(2*k-1)*(2*k+1)
        bruch=zaehler/nenner
        p=p*bruch
    return 2*p
#Anzahl der Schleifendurchläufe
N=10**3
Z=14 #Anzahl der Nachkommastellen
print("\t π\t   n")
print(round(viete(N),Z),N,  "\tViete 1593")
print(round(wallis(N),Z),N, "\tWallis 1655")
print(pi,"Python")



