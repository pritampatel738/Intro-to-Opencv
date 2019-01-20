import cv2
import numpy as np

img = cv2.imread('m5.jpg')

cols = img.shape[1]
rows = img.shape[0]
m = np.float32([[1,0,150],[0,1,70]])
shifted = cv2.warpAffine(img,m,(cols,rows))

cv2.imshow('img',shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()