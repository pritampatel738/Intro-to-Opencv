import cv2
import numpy as numpy

img = cv2.imread('m5.jpg')
cv2.circle(img,(100,100),30,(0,0,255),4)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()