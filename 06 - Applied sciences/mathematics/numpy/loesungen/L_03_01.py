#L_03_01.py
import numpy as np
a=(3,0,0)
b=(0,4,0)
c=(0,0,5)

S=np.dot(np.cross(a,b),c)
D=np.linalg.det([[a[0],b[0],c[0]],
                 [a[1],b[1],c[1]],
                 [a[2],b[2],c[2]]])

print("Spatprodukt:",S)
print("Determinate:",D)
