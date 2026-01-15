#L_14_03.py
import numpy as np
from scipy.stats import mode,hmean,gmean
a=[44,45,46,47,48,49,50,50,51,52,53,54,55,56]
md=mode(a)
print("Modus:",md[0])
print("Mittelwert:",np.mean(a))
print("Median    :",np.median(a))
print("harmonischer Mittelwert :",hmean(a))
print("geometrischer Mittelwert:",gmean(a))