#23_liste2.py
ug=1
og=20
p=[(a,b,c)
   for a in range(ug,og)
   for b in range(a,og)
   for c in range(b,og)
   if a**2 + b**2 == c**2]
n=len(p)
print(p)
print("Zwischen %i und %i gibt es %i pythagoreische Tripel." %(ug,og,n))