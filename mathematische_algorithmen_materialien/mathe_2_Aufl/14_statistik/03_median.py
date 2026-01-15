#03_median.py
import numpy as np
import sortieren as st

def median(xu):
    x=st.selectionSort(xu)
    #x=np.sort(xu)
    n=len(x)
    if n%2!=0: #ungerade
        return x[(n-1)//2]
    else:      #gerade
        return (x[n//2-1]+x[n//2])/2
#Messwerte laden
a=np.loadtxt('daten.txt')
print("Median")
print(median(a))
print(np.median(a),"NumPy")