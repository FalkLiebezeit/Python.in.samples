#08_verzweigung1.py
import math as m
p=-8.
q=7.
D=(p/2)**2 - q
if D >= 0:
    x1 = -p/2 + m.sqrt(D)
    x2 = -p/2 - m.sqrt(D)
    print("x1 =",x1,"\nx2 =",x2)
    print("p =",-(x1+x2),"\nq =",x1*x2)
else:
    print("Die Gleichung ist nicht loesbar!")
    
    
    