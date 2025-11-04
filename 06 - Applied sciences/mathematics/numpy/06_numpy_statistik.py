#06_numpy_statistik.py
import numpy as np
zeilen=5
spalten=10
np.random.seed(1)
x=np.random.normal(8,4,size=(zeilen,spalten))
mw=np.mean(x)
md=np.median(x)
v=np.var(x)
staw=np.std(x)
minimum=np.amin(x)
maximum=np.amax(x)
min_index=np.where(x==np.amin(x))
max_index=np.where(x==np.amax(x))
#min_index=np.argmin(x)
#max_index=np.argmax(x)
#Ausgabe
print("Zufallszahlen\n",np.round(x,decimals=2),"\n")
print("kleinste Zahl...........:",minimum)
print("größte Zahl.............:",maximum)
print("Index der kleinsten Zahl:",min_index)
print("Index der größten Zahl..:",max_index)
print("Mittelwert..............:",mw)
print("Median..................:",md)
print("Varianz.................:",v)
print("Standardabweichung......:",staw)
print("Type von  x:",type(x))
print("Type von mw:",type(mw))

