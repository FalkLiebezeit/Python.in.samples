#04_funktion1.py
U,R = 230,460  #Volt, Ohm
t=8.           #Stunden
preis=0.3      #Euro/kWh

def stromstaerke():
    I=U/R
    print("Stromstaerke : ", I, " A")

def leistung():
    P=U**2/R
    print("Leistung     : ", P, " W")
    
def arbeit():
    P=U**2/R
    W=P*t
    print("Arbeit: ", W, " Wh")
    
def kosten():
    I=U/R
    W=U*I*t
    k=W*preis/1000.0
    print("Kosten: ", k, " Euro")

stromstaerke()
leistung()
arbeit()
kosten()

