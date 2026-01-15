#L_06_03a.py
import numpy as np
A = np.array([[5, 4, 3, 2],
              [1, 7, 1, 3],
              [2, 1, 11, 1],
              [7, 3, 1, 13]],dtype=float)
b = np.array([10, 8, 6, 4],dtype=float)
def seidel(a, b,N=50):
    x1=x2=x3=x4=0
    for _ in range(N):
        x1=(b[0]-a[0,1]*x2-a[0,2]*x3-a[0,3]*x4)/a[0,0]
        x2=(b[1]-a[1,0]*x1-a[1,2]*x3-a[1,3]*x4)/a[1,1]
        x3=(b[2]-a[2,0]*x1-a[2,1]*x2-a[2,3]*x4)/a[2,2]
        x4=(b[3]-a[3,0]*x1-a[3,1]*x2-a[3,2]*x3)/a[3,3]
    return x1,x2,x3,x4
#Ausgabe
print("  %3.8f  %3.8f %3.8f %3.8f" %(seidel(A,b)))


