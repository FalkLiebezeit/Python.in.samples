#06_while_schleife3.py
n=9
i=0
s=0
print("i\tL-Werte\tR-Wert")
while i < n:
    i=i+1
    sr=s #R-Wert
    s=s+i
    print(i,s,sr,sep='\t')
#zum Testen
summe=n*(n+1)/2
print("Summenformel")
print(summe)
