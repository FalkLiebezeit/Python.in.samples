#23_pi_archimedes.py
from math import pi,sqrt
N=27 #Anzahl der Schleifendurchläufe
n=6
u=6 #innenliegender Kreis
U=4*sqrt(3) #außen liegender Kreis
print("Nr.\t Ecken\t\t Innenradius\tAußenradius")
for i in range(1,N+1):
    U=2*U*u/(U+u) #außen
    u=sqrt(u*U)   #innen
    pii=u/2 #pi aus Innenkreis
    pia=U/2 #pi aus Außenkreis
    print("%3d  %12d  %2.15f  %2.15f" %(i,n,pii,pia))
    n = 2*n  #Verdopplung der Eckenzahl   
print("Anzahl der Ecken:",3*2**N)
print("Innenkreis:",pii)
print("Außenkreis:",pia)
print("genau:     ",pi)
print("Fehler Innenkreis:",pi-pii)
print("Fehler Außenkreis:",pia-pi)