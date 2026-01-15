#09_schiefe.py
import numpy as np
from scipy.stats import mode,skew
sw=50
n=100
s=2
a=np.random.normal(sw,s,size=n)
a=np.round(a,decimals=1)
xa=np.mean(a)
xm=np.median(a)
xmod=mode(a)
s=np.std(a,ddof=1)
schiefe1=(xa-xm)/s #Pearson
schiefe2=skew(a)   #SciPy
if xmod[0] < xm < xa:
    print("Die Verteilung ist linkssteil.")
elif xmod[0]==xm==xa:
    print("Die Verteilung ist symmetrische.")
elif xa < xm < xmod[0]:
    print("Die Verteilung ist rechtssteil.")
else:
    print("Keine eindeutige Entscheidung!")
print("Modalwert                :",xmod[0])
print("Median                   :",xm)
print("arithmetischer Mittelwert:",xa)
print("Schiefe",schiefe1,"Pearson")
print("Schiefe",schiefe2,"SciPy")


