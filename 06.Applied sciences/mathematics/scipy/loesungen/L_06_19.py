#L_06_19.py
#Butterworth-Koeffizienten TP 5. Grades
from scipy.signal import butter
g=5     #Grad des Filters
fg=1    #Grenzfrequenz in Hz
b,a=butter(g,fg,'lowpass',analog=True)
print(a)

'''
#Zugriff auf die einzelnen Koeffizienten
for i in range(g+1):
    print(a[i])
'''