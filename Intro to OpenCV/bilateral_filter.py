import cv2
import numpy as np

img = cv2.imread('m5.jpg')

dim_pixel = 7
color = 100
space = 100
filter1 = cv2.bilateralFilter(img,dim_pixel,color,space)

cv2.imshow('img1',img)
cv2.imshow('img',filter1)

cv2.waitKey(0)
cv2.destroyAllWindows()