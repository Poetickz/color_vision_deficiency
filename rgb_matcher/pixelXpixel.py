import numpy as np
import cv2
import random
import colorchange as color


m=cv2.imread("01.jpg")
h,w,bpp = np.shape(m)
cv2.imshow('old', m)
for py in range(0,h):
    for px in range(0,w):
            r=m[py][px][0]
            g=m[py][px][1]
            b=m[py][px][2]
            rgb = (r,g,b)
            r,g,b=color.modify_rgb(rgb,1)
            m[py][px][0]=r
            m[py][px][1]=g
            m[py][px][2]=b



cv2.imshow('new', m)
cv2.waitKey(0)
cv2.imwrite('02.jpg',m)