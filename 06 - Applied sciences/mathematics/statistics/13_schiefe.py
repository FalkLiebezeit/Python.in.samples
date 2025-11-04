#13_schiefe.py
import numpy as np
from scipy import stats
n=50
sollwert=50
s=2
werte=np.random.normal(sollwert,s,size=n)
rwerte=np.around(werte,decimals=2)
modus=stats.mode(rwerte, axis=None)
mw=np.mean(rwerte)
md=np.median(rwerte)
stabw=np.std(rwerte,ddof=1)
S1=(mw-md)/stabw
S2=stats.skew(rwerte)
print(np.sort(rwerte))
print("Modus:             ",modus)
print("Mittelwert:        ",mw)
print("Median:            ",md)
print("Standardabweichung:",stabw)
print("Schiefe (Näherung):",S1)
print("Schiefe (genau):   ",S2)
if S2<0:
    print("rechtssteil")
else:
    print("linkssteil")




