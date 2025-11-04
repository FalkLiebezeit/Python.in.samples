#15_partialbruch.py
from sympy import *
s=symbols("s")
#Parallelschaltung aus R-L-Reihenschaltungen
Yb1=1/(s+1)+1/(2*s+1)+1/(3*s+1)
Yp1=cancel(Yb1)
#Reihenschaltung aus L-C-Parallelschaltungen
Zb2=s/(2*s**2+1)+2*s/(3*s**2+1)+3*s/(4*s**2+1)
Zp2=cancel(Zb2)
#Berechnung der Partialbrüche
pb1=apart(Yp1)
pb2=apart(Zp2)
#Ausgabe
print(Yp1,"=\n",pb1)
print("\n",Zp2,"=\n",pb2)

