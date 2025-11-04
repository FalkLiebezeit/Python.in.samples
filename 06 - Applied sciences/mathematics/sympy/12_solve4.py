#12_solve4.py
from sympy import symbols, solve
s,L1,C2,L3,C4,L5 = symbols("s L1 C2 L3 C4 L5")
#Butterworth-Koeffizienten
a=[0,3.236,5.236,5.236,3.236,1]
#nichtlineares Gleichungssystem
g1=L1+L3+L5-a[1]
g2=C2*L1 + C4*L1 + C4*L3-a[2]
g3=C2*L1*L3 + C2*L1*L5 + C4*L1*L5-a[3]
g4=C2*C4*L1*L3-a[4]
g5=C2*C4*L1*L3*L5-a[5]
bauteile=solve((g1,g2,g3,g4,g5),L1,C2,L3,C4,L5,dict=True)
#Ausgabe
print(bauteile[1])
print(bauteile[1].keys())
print(bauteile[1].values())
for item in bauteile[1].items():
    print("%s = %.3f"%item)

'''
for key, value in bauteile[1].items():
    print(key, '=', value)
'''
'''
print("L1 =",bauteile[1][L1])
print("C2 =",bauteile[1][C2])
print("L3 =",bauteile[1][L3])
print("C4 =",bauteile[1][C4])
print("L5 =",bauteile[1][L5])
'''