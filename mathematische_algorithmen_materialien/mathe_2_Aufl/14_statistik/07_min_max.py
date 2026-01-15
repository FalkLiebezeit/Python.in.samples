#07_min_max.py
import numpy  as np
#Minimumsuche
def minimum(x):
    n=len(x)
    k=x[0] #kleinster Wert
    for i in range(1,n):
        if x[i]<k:
            k=x[i]
    return k
#Maximumsuche
def maximum(x):
    n=len(x)
    g=x[0] #größter Wert
    for i in range(1,n):
        if x[i]>g:
            g=x[i]
    return g

a=np.loadtxt('daten.txt')
R=maximum(a)-minimum(a) #Spannweite
print("Minimum:",minimum(a))
#print(min(a))
print("Maximum:",maximum(a))
#print(max(a))
print("Spannweite R = ", R)