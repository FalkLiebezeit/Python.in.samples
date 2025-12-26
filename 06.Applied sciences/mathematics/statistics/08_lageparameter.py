#08_lageparameter.py
import numpy as np
import scipy.stats as sta
werte=np.loadtxt("./DataInput/daten.txt")
mw=np.mean(werte)
md=np.median(werte)
modus=sta.mode(werte)
hm=sta.hmean(werte)
gm=sta.gmean(werte)
print(np.sort(werte))
print("Modus:",modus)
print("arithmetischer Mittelwert:",mw)
print("Median:                   ",md)
print("harmonischer Mittelwert:  ",hm)
print("geometrischer Mittelwert: ",gm)




