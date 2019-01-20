import cv2
import numpy as numpy

img = cv2.imread('m5.jpg',0)
cv2.imshow('img',img)

cv2.imwrite('m55.png',img)

cv2.waitKey(0)
cv2.destroyAllWindows()