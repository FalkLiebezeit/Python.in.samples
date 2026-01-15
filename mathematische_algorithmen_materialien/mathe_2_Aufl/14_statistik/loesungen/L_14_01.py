#L_14_01.py
import numpy as np
print("Häufigkeitstabelle")
a=np.loadtxt('../daten.txt')
n=len(a)
#k=int(np.sqrt(n))
h=np.histogram(a,bins=32)
kk=h[0]
nn=np.round(h[1],decimals=1)
wp=list(zip(nn,kk))
print(wp)
