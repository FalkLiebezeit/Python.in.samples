#L_14_05.py
import numpy as np
from scipy.stats import gmean
#5%,4%,3%,2%,1% 
p=[1.05,1.04,1.03,1.02,1.01]
dz = gmean(p)-1
dz=np.round(dz,decimals=2)
print("Durchschnittlicher Zinssatz:",dz*100,"%")
