#02_linear2.py
U=230
R1,R2,R3=0.12,0.52,228
Rg=R1+R2+R3
I=U/Rg
P1=R1*I**2
P2=R2*I**2
P3=R3*I**2
print("Stromstaerke I={0:6.3f} A " .format(I))
print("P1={0:3.2f} W, P2={1:3.2f} W, P3={2:3.2f} W".format(P1,P2,P3))
#print("P1=%3.2f W, P2=%3.2f W, P3=%3.2f W" %(P1,P2,P3))
