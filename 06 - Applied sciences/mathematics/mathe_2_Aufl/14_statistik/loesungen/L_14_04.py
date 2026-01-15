#L_14_05.py
import numpy as np
from scipy.stats import hmean
R=[10,20,30,40,50]
n=len(R)
Rm = hmean(R)
Rm=np.round(Rm,decimals=2)
print("Widerstände:",R)
print("harmonischer Mittelwert:",Rm,"Ω")
print("harmonischer Mittelwert geteilt durch n:",Rm/n,"Ω")