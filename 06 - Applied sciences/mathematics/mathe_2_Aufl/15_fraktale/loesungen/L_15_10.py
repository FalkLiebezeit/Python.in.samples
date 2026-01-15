#L_15_10.py
from PIL import Image
X,Y = 800,800
x1,x2 = -2,1
y1,y2 = -1.5,1.5
sx=(x2-x1)/X
sy=(y2-y1)/Y
mandelbrot = Image.new("RGB",(X,Y),"white")
for x in range(X):
    zx = sx*x + x1
    for y in range(Y):
        zy = sy*y + y1
        c = zx + 1j*zy
        z=c
        i = 255
        while abs(z)<2 and i>1:
            z=z**2+c
            i = i - 1
            #mandelbrot.putpixel((x,y),(i%4*64,i%8*32,i%16*16))
            #mandelbrot.putpixel((x,y),(i%16*16,i%8*32,i%4*64))
            mandelbrot.putpixel((x,y),((i<<21)+(i<<10)+i*8))
#mandelbrot.save("mandelbrot_menge.png")
mandelbrot.show()


