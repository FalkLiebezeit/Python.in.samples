#private_key.py
def privateKey(e,phi):
    a,b,d,u=phi,e,0,1
    while(b!=0):
        q=a//b
        x=b
        b=a-q*b
        a,x=x,u
        u=d+q*u
        d=x
    return d
#
p,q=223,127
phi=(p-1)*(q-1)
e=121
print(privateKey(e,phi))

#Vorlage: Wikipedia
