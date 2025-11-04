#25_integral3.py
from sympy import *
t = symbols('t')
U0=10
R,C=1,1
I0=U0/R
tau=R*C
uc=U0*(1-exp(-t/tau))     #Spannungsverlauf
ic=I0*exp(-t/tau)         #Stromverlauf
p=uc*ic                   #el. Leistung
Wel=integrate(p,(t,0,oo)) #el. Energie
#Ausgabe
print("gespeicherte el. Energie:",Wel.evalf(3),"Ws")
plt=plot(uc,ic,p,(t,0,5*tau),show=False,legend=True)
plt[0].line_color = 'b'
plt[0].label='Spannung'
plt[1].line_color = 'r'
plt[1].label='Strom'
plt[2].line_color = 'g'
plt[2].label='Leistung'
#plt.save('leistung.png')
plt.show()
