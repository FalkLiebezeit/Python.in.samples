#05_funktion2.py
def stromstaerke(U,R):
    return U/R

def leistung(U, R):
    return U**2/R

def arbeit(U, R, t):
    P=U**2/R
    W=P*t
    return W

def kosten(U, R,t,preis):
    I=U/R
    W=U*I*t
    k=W*preis/1000.0
    return k

Uq=230
RLast=23
tn=8
preis_aktuell=0.3
print("Stromstaerke : ", stromstaerke(Uq, RLast), " A")
print("Leistung     : ", leistung(Uq, RLast), " W")
print("Arbeit       : ", arbeit(Uq, RLast,tn), " Wh")
print("Kosten       : ", kosten(Uq, RLast,tn,preis_aktuell), " Euro")