#03_2dim_array.py
import numpy as np
m=3 #Zeilen
n=4 #Spalten
a=np.arange(m*n).reshape(m,n)
b=a.reshape(n*m,)
print("Type des Arrays",a.shape,"\n",a)
print("Linearisieren\n",b)
print("Transponieren\n",a.T)


'''
print("Transponieren\n",np.transpose(a))
'''