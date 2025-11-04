#24_fourier1.py
from scipy.fft import fft,ifft
u_t1=[0,1,2,3,4,5]
#Transformation in den Frequenzbereich
U_fft=fft(u_t1)
#Transformation in den Zeitbereich
u_t2=ifft(U_fft)
print("ursprüngliches Signal :\n",u_t1)
print("transformiertes Signal:\n",U_fft)
print("wiederhergestelltes Signal:\n",u_t2.real)