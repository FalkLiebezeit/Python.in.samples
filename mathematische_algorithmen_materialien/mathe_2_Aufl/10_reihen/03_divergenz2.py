#03_divergenz2.py
i=9 #Exponent
print("\tn\t∑1/n")
for i in range(1,i):
    summe=0
    for n in range(1,10**i+1):
        summe=summe + 1/n
    print("%9d %4.10f" %(n,summe))