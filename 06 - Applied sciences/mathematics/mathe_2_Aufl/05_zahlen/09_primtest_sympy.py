#12_primtest_sympy.py
from sympy import isprime
n=2281    #Robinson 1952
M=2**n-1  #Mersenne-Primzahl
print("Ist die Zahl\n",M,"\nmit",len(str(M)),"Stellen eine Primzahl?")
print(isprime(M))

'''
n=17      #Cataldi 1588
n=19      #Cataldi 1588
n=31      #Euler 1772
n=127     #Lucas 1876
n=2281    #Robinson 1952
n=11213   #Gillies 1963
n=19937   #Tuckerman 1971
n=23209   #Noll 1979
n=44497   #Nelson & Slowinski 1979
n=86243   #Slowinski 1982
n=132049  #Slowinski 1983
n=24036583 #Findley 2004
n=32582657 #Cooper, Boone 2006
'''