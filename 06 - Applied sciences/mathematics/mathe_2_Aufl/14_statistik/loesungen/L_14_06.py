#L_14_06.py
import numpy as np
from scipy.stats import hmean,gmean
a=[10,200]
am=np.mean(a)
hm=hmean(a)
gm1=gmean(a)
gm2 = np.sqrt(am*hm)
print("arithmetischer Mittelwert :",am)
print("harmonischer Mittelwert   :",hm)
print("geometrischer Mittelwert         :",gm1)
print("aritmetrisch-geometrisches Mittel:",gm2)
