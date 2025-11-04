#18_for_for_schleife2.py
a=[5,4,3,2,1] #Liste
print(a)
for i in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i]>a[i+1]: #vergleichen
            a[i],a[i+1]=a[i+1],a[i] #tauschen
    print(a)