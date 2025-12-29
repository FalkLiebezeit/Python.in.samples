#17_masche4c.py
import numpy as np
import numpy.linalg
U1=230
U2=-230
U3=230
U4=-230
Z1=1+2j
Z2=2-4j
Z3=3+4j
Z4=2+5j
Z5=1+5j
Z6=2+5j
Z7=4-5j
Z8=1+5j
Z=np.array([[Z1+Z2+Z4,-Z2,-Z4, 0],
            [-Z2,Z2+Z3+Z5, 0,-Z5],
            [-Z4, 0,Z4+Z6+Z7,-Z7],
            [0,-Z5,-Z7,Z5+Z7+Z8]])
U=np.array([U1,-U2,U3,-U4])
strom=np.linalg.solve(Z,U) #numpy.ndarray
for k, I in enumerate(strom,start=1):
    print("I%d = (%0.2f, %0.2fj)A" %(k,I.real,I.imag))


#print(type(strom))
'''
#zum besseren Verständnis
werte=[1.3,3.4,6.1,4.8]
for k in enumerate(werte,start=1):
    print(k)

#enumerate() erzeugt ein Tupel
'''