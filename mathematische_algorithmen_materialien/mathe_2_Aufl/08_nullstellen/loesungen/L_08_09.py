#L08_09.py
#n-te Wurzel
a=127
n=5
x=1
for _ in range(20):
    x=x-(x**n-a)/(n*x**(n-1)) #Potenzregel
print(n,"Wurzel aus",a)
print(x)
print(a**(1/n),"genau")

