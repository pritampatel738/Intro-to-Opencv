import cv2
import numpy as np

img = cv2.imread('m5.jpg')
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()