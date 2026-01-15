#L_14_09.py
import numpy as np
from scipy.stats import skew,kurtosis
a=np.loadtxt("../daten.txt")
print("Aritmetisches Mittel:",np.mean(a))
print("Standardabweichung:",np.std(a))
print("Schiefe:",skew(a))
print("Wölbung:",kurtosis(a))