#08_manelbrot1.py
import numpy as np
C=[-0.5,-1,1,-1+0.1j]
for c in C:
    z=c
    print("\nc =",c,end=':\n')
    for i in range(1,6):
        z=z**2+c
        print(np.round(z,4),end=', ')

