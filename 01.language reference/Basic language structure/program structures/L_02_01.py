#L_02_01.py
v=36 #m/s
A=1.5 #m^2
cw=0.3
t=120 #Sekunden
rho=1.3
#Berechnungen
F=0.5*rho*cw*A*v**2
P=F*v
W=P*t
#Ausgaben
print("Kraft:",F,"N")
print("Leistung:",P,"W")
print("Arbeit:",W,"Ws")

