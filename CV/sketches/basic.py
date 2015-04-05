#!/usr/bin/env python
from PIL import Image
from pylab import *
# read image to array
#im = array(Image.open('../images/Lenna.png').convert('L'))
# plot the image
im = array(Image.open('../images/atlas.jpg'))
#im = array(Image.open('../images/darwin.png'))
print im.shape, im.dtype
#im = array(Image.open('../images/Lenna.png').convert('L'),'f')

im2 = 255 - im
im3 = (100.0/255) * im2 + 100
im4  = 255.0 * (im3 / 255.0)**2
imshow(im2)
figure()
imshow(im3)
figure()
imshow(im4)
show()