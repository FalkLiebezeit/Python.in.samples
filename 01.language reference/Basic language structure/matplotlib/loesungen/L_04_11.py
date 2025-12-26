#L_04_11.py
'''Polygon darstellen'''
import matplotlib.pyplot as plt
import matplotlib.patches as pat
fig, ax = plt.subplots()
ax.axis([-2,2,-2,2])
n=8
r=2
xy=0,0
poly = pat.RegularPolygon(xy, n,radius=r,fill=False)
ax.add_patch(poly)
ax.set_aspect('equal')
plt.show()