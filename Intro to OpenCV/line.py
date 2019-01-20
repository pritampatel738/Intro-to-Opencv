import cv2
import numpy as numpy

img = cv2.imread('m5.jpg')


cv2.line(img,(10,10),(100,100),(0,0,255),10)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()