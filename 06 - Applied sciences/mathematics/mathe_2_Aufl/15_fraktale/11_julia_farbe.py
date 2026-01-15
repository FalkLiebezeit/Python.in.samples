#11_julia_farbe.py
from PIL import Image
c = -0.1+0.65j
#c = -1.2  #-1.4 bis +0.2
#c=-0.74543+0.1130j
#c= 0.909 - 0.27j
#c=0 + 0.8j
#c=0.37+0.1j
#c=0.355+0.355j
#c=-0.54+0.54j
#c=-0.4-0.59j
#c=-0.1+0.9j
X,Y = 400,400
x1,x2 = -2,2
y1,y2 = -1.5,1.5
sx=(x2-x1)/X
sy=(y2-y1)/Y
julia = Image.new("RGB",(X,Y),"white")
for x in range(X):
    zx = sx*x + x1
    for y in range(Y):
        zy = sy*y + y1
        z = zx + 1j*zy
        i = 255
        while abs(z)<2 and i>1:
            z=z**2+c
            i = i - 1
            #julia.putpixel((x,y),(i%4*64,i%8*32,i%16*16))
            #julia.putpixel((x,y),(i%16*16,i%8*32,i%4*64))
            julia.putpixel((x,y),((i<<21)+(i<<10)+i*8))
#julia.save("julia_menge.png")
julia.show()

