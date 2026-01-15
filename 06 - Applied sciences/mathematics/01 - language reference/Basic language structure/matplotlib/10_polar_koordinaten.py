#10_polar_koordinaten.py
import numpy as np
import matplotlib.pyplot as plt

def theta_rad(winkel1,winkel2):
    theta=[winkel1,winkel2]
    return np.radians(theta)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta_rad(0,90),[1,1],'r',lw=3)
ax.plot(theta_rad(90,180),[1,1],'g',lw=3)
ax.plot(theta_rad(180,270),[1,1],'m',lw=3)
ax.plot(theta_rad(270,0),[1,1],'b',lw=3)
ax.plot(theta_rad(0,45),[0,0.6],'black',lw=3)
ax.grid(True)
plt.show()