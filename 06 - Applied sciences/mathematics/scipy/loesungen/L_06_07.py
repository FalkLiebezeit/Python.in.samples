#L_06_07.py
#Dreifachintegral
import scipy.integrate as integral

def dichte(z,x,y):
    return x*y+x*z+y*z
    
a=0.3 #x2
b=0.4 #y2
c=0.5 #

#x1,x2,y1,y2,z1,z2
Q=integral.tplquad(dichte,0,a,0,b,0,c)[0]
print("Ladungsmenge:",Q,"As")


