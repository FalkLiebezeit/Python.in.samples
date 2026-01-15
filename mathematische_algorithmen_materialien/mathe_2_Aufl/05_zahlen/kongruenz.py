def kongruent(a,b,m):
    return a%m==b%m
a=11
b=17
m=5
print(kongruent(a,b,m))
#Rechenreeln
print((a+b)%m,((a%m)+(b%m))%m)
print((a-b)%m,((a%m)-(b%m))%m)
print((a*b)%m,((a%m)*(b%m))%m)
