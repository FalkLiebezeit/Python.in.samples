#29_inv_laplace1.py
from sympy import *
s,C,L,R = symbols("s C L R")
t = symbols("t",positive=True)
U1=10
R=2
L=Rational(1,2)
C=Rational(1,4)
U1_s=U1/s
Z_s=R+L*s+1/(C*s)
I_s=U1_s/Z_s
H_s=1/(R + L*s + 1/(C*s))/(C*s)
H_s=expand(H_s) #Übertragungsfunktion
U2_s=U1_s*H_s   #Sprungantwort
uc=inverse_laplace_transform(U2_s,s,t)
ic=inverse_laplace_transform(I_s,s,t)
#Ausgaben
print("Übertragungsfunktion\n",H_s)
print("Spannung am Kondensator\n","uc =",simplify(uc))
print("Kondensatorstrom\n","ic =",ic)
plt=plot(uc,ic,(t, 0, 5),show=False)
plt[0].line_color = 'b'
plt[1].line_color = 'r'
plt.show()

'''
print(type(L))
plt.save('05_011.png')
plt.save('05_011.svg')

'''
