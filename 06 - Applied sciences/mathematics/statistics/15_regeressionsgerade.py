#15_regeressionsgerade.py
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
X=np.array([46,53,29,61,36,39,47,49,52,38,55,32,57,54,44])
Y=np.array([12,15,7,17,10,11,11,12,14,9,16,8,18,14,12])
m, a, r, p, e = stats.linregress(X,Y)
fig, ax=plt.subplots()
ax.plot(X, Y,'rx')
ax.plot(X, m*X+a)
ax.set_xlabel("relative Luftfeuchtigkeit in %")
ax.set_ylabel("Feuchtigkeitsgehalt des Materials")
plt.show()