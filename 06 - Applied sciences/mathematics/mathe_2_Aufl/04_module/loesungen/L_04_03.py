#L_04_03.py
import numpy as np
A=np.array([[22,23,32,11],
            [47,56,16,29],
            [76,81,95,43]])
B=np.array([[95,88,73],
            [61,54,42],
            [31,29,18],
            [42,32,17]])
#Matrizenmultiplikation
C=A@B
print(C)