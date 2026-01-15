#L_14_02.py
import numpy as np
a=[45,46,47,48,49,50,51,52,53,54,55]
a.append(451)
print("Mittelwert:",np.mean(a))
print("Median    :",np.median(a))
print("Spannweite:",max(a)-min(a))
print("Standardabweichung:",np.std(a)) 
'''
Erkenntnis:
Der Mittelwert ist empfindlich gegenüber Ausreißern als der Median.
'''