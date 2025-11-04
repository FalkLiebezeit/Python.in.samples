#14_korrelation.py
import numpy as np
from scipy import stats

X=np.array([46,53,29,61,36,39,47,49,52,38,55,32,57,54,44])
Y=np.array([12,15,7,17,10,11,11,12,14,9,16,8,18,14,12])

xm=np.mean(X)
ym=np.mean(Y)
sx=np.std(X,ddof=1)
sy=np.std(Y,ddof=1) 
sxy=np.cov(X,Y)
r1=sxy/(sx*sy)
r2=np.corrcoef(X,Y)
m1=sxy[0,1]/sx**2
m2=r2[0,1]*sy/sx
a1=ym-m2*xm
m3, a2, r3, p, e = stats.linregress(X,Y)

print("NumPy1 Steigung:",m1)
print("NumPy2 Steigung:",m2)
print("SciPy  Steigung:",m3)
print("Schnittpunkt mit der y-Achse:",a1)
print("Schnittpunkt mit der y-Achse:",a2)
print("Def.  Korrelationskoeffizient:",r1[0,1])
print("NumPy Korrelationskoeffizient:",r2[0,1])
print("SciPy Korrelationskoeffizient:",r3)
print("geschätzter Fehler:",e)

