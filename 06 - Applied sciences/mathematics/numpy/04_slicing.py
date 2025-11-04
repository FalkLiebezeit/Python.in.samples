#04_slicing.py
import numpy as np
m=4 #Zeilen
n=4 #Spalten
a=np.arange(m*n).reshape(m,n)
#Ausgabe
print(a)
print("erste  Spalte\n",a[:,0])
print("zweite Spalte\n",a[:,1])
print("erste Zeile\n",  a[0,:])
print("zweite Zeile\n", a[1,:])
print("a[1:3,0:2]\n",   a[1:3,0:2])

