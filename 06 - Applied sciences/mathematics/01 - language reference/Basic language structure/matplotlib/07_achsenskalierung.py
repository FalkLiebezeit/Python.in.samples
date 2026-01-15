#07_achsenskalierung.py
import matplotlib.pyplot as plt
l=[0,0.02,0.1,0.2,1.15,2.2,3.25,4.3,5.4,6.4]
F=[5.7,7.5,7.2,7.3,8.9,10.4,11.3,12,11.4,9.3]
fig, ax = plt.subplots()
ax.plot(l, F,'ro-')
ax.set_xticks([0,1,2.2,3.25,4.3,5.4,6.4])
ax.set_yticks([0,5.7,7.5,8.9,10.4,12,9.3])
#ax.axis([-0.5,7,5,13])
ax.set_xlabel("l in mm")
ax.set_ylabel("F in kN")
plt.show()