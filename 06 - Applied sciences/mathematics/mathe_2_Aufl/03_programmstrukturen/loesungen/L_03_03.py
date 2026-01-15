#L_03_03.py
#Kredit berechnen
kredit=1000 #in Euro
rate=100    #in Euro
zinssatz=5  #in Prozent
zinssatz=zinssatz/100
while kredit>0:
    print("%7.2f €" %kredit)
    zinsen=kredit*zinssatz
    kredit=kredit + zinsen - rate
    