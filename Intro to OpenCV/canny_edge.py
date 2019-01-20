import cv2
import numpy as np

img = cv2.imread('m5.jpg')

threshold1 = 50
threshold2 = 100

canny = cv2.Canny(img,threshold1,threshold2)

cv2.imshow('img',img)
cv2.imshow('img1',canny)

cv2.waitKey(0)
cv2.destroyAllWindows()