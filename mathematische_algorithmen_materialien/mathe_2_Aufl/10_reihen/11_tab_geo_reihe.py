#11_tab_geo_reihe.py
from fractions import Fraction
m=10
a=1
zaehler=1
nenner=2
q=Fraction(zaehler,nenner) #q<1
summe=0
print("n\t∑\t∑   \t     a*(q**(n+1)-1)/(q-1)")
for n in range(m+1):
    summe=summe + a*q**n
    sn=a*(q**(n+1)-1)/(q-1)
    print("%2i  %10s  %2.10f %2.10f" %(n,summe,float(summe),float(sn)))
    
