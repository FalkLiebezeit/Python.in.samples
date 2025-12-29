#L_02_08.py
dicIntegral={"cos(x)":" sin(x)",
             "sin(x)":"-cos(x)",
             "tan(x)":"-ln cos(x)",
             "cot(x)":" ln sin(x)"}
f=input("Geben Sie eine trigonometrische Funktion ein:")
while f!="":
    if f in dicIntegral.keys():
        print("Die Funktion",f,"hat die Stammfunktion",)
        print(dicIntegral[f])
    else:
        print("Funktion nicht enthalten")
    f=input("Geben Sie eine trigonometrische Funktion ein:")
        
        
    