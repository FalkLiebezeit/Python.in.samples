#03_linear3.py
while True:
    print("\n---Eingaben---")
    U=float(input("Spannung: "))
    R=float(input("Widerstand: "))
    I=U/R
    P=U*I
    print("\n---Ausgaben---")
    print("Stromstaerke {0:6.2f} A " .format(I))
    print("Leistung     {0:6.2f} W " .format(P))
    

