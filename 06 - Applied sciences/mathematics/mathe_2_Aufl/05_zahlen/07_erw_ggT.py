#07_erw_ggt.py
#ggT(a,b)=u*a+v*b
def erweitert_ggT(a,b):
    u,v=1,0
    s,t=0,1
    while b!=0:
        q=a//b
        a, b = b, a-q*b
        u, s = s, u-q*s
        v, t = t, v-q*t
    return u,v,a
#Berechnung und Ausgabe
a,b=99,78
print(erweitert_ggT(a,b))


# from sympy import gcdex
# print(gcdex(a,b))

'''
e=47
d=13583
phi=63840
'''
'''
Quelle:
https://hwlang.de/krypto/algo/euklid-erweitert.htm
'''