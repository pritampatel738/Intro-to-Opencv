import cv2
import numpy as numpy

img = cv2.imread('m13.jpg',0)

threshold_value = 150
[T_value,binary_threshold] = cv2.threshold(img,threshold_value,255,cv2.THRESH_BINARY)


cv2.imshow('img',binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()