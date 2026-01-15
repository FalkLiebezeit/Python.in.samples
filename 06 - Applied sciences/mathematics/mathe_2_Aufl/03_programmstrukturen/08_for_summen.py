#08_for_summen.py
N=100
#Summe der ungeraden Zahlen
su=0
for n in range(1,N+1,2): 
    su=su+n
#Summe der geraden Zahlen
sg=0
for n in range(2,N+1,2): 
    sg=sg+n
#Summe aller Zahlen
s=0
for n in range(0,N+1,1):
    s=s+n
#Ausgabe
print("Die Summe der ungeraden Zahlen von 1 bis",N,"ist",su)
print("Die Summe der geraden Zahlen von 2 bis",N,"ist",sg)
print("Die Summe der ganzen Zahlen von 1 bis",N,"ist",s)
print("Gausssche Summenformel:",N*(N+1)/2)

'''
import time as t
N=1000000
s=0
t1=t.time() #Sekunden
for n in range(0,N+1,1):
    s=s+n
t2=t.time() #Sekunden
delta_t=(t2-t1)*1e9 #ns
print(delta_t/N,"ns") 
'''

