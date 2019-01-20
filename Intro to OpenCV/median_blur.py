import cv2
import numpy as np

img = cv2.imread('m5.jpg')

kernel = 3
median = cv2.medianBlur(img,kernel)
#blur = cv2.GaussianBlur(img,kernel,np.std(img))
cv2.imshow('img1',img)
cv2.imshow('img',median)

cv2.waitKey(0)
cv2.destroyAllWindows()