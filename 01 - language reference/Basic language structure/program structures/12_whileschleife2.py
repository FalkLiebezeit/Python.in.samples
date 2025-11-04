#12_whileschleife2.py
def f(a,x):
    return 0.5*a*x**2

weiter=True
while weiter:
    print("Kinetische Energie....1")
    print("Rotationsenergie......2")
    print("elektrische Energie...3")
    print("magnetische Energie...4")
    auswahl=int(input("Wählen Sie aus:"))
    if auswahl==1:
        m=float(input("Masse m="))
        v=float(input("Geschwindigkeit v="))
        Wkin=f(m,v)
        print("\nDie kinetische Energie beträgt %6.3f Ws\n" %Wkin)
    elif auswahl==2:
        omega=float(input("Winkelgeschwindigkeit \u03C9="))
        J=float(input("Trägheitsmoment J="))
        Wrot=f(J,omega)
        print("\nDie Rotationsenergie beträgt %6.3f Ws\n" %Wrot)
    elif auswahl==3:
        C=float(input("Kapazität C="))
        U=float(input("Spannung U="))
        Wel=f(C,U)
        print("\nDie elektrische Energie beträgt %6.3f Ws\n" %Wel)
    elif auswahl==4:
        L=float(input("Induktivität L="))
        I=float(input("Stromstärke I="))
        Wmag=f(L,I)
        print("\nDie magnetische Energie beträgt %6.3f Ws\n" %Wmag)
    else:
        weiter=False
        
    
    
    