#15_seidel1.py
import numpy as np
N=15
a = np.array([[6,2,1],
              [1,5,3],
              [2,1,4]],dtype=float)
b = np.array([13,20,16],dtype=float)
x1=np.empty(N+1,dtype=float)
x2=np.empty(N+1,dtype=float)
x3=np.empty(N+1,dtype=float)
x1[0],x2[0],x3[0]=(0.,0.,0.) #Startwerte
print("Gauss-Seidel-Verfahren")
print("%6s %10s %10s" %("x1","x2","x3"))

for k in range(N):
    x1[k+1]=(b[0]-a[0,1]*x2[k]-a[0,2]*x3[k])/a[0,0]
    x2[k+1]=(b[1]-a[1,0]*x1[k+1]-a[1,2]*x3[k])/a[1,1]
    x3[k+1]=(b[2]-a[2,0]*x1[k+1]-a[2,1]*x2[k+1])/a[2,2]
    print("%2.8f %2.8f %2.8f" %(x1[k+1],x2[k+1],x3[k+1]))
'''
#Alternative
x1=x1=x3=0
for k in range(N):
    x1=(b[0]-a[0,1]*x2-a[0,2]*x3)/a[0,0]
    x2=(b[1]-a[1,0]*x1-a[1,2]*x3)/a[1,1]
    x3=(b[2]-a[2,0]*x1-a[2,1]*x2)/a[2,2]
    print("%2.8f %2.8f %2.8f" %(x1[k+1],x2[k+1],x3[k+1]))  
'''