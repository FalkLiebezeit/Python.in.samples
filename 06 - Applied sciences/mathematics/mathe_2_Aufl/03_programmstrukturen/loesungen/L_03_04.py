#L_02_04.py
#Qudratzahlen für alle ungeraden Zahlen
print("Ausgabe mit for-Schleife")
for x in range(1,20,2):
    y=x**2
    print(y,end='  ')
print("\nAusgabe mit while-Schleife")
x=1
while x <= 20:
    y=x**2
    print(y,end='  ')
    x=x+2