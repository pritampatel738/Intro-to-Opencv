import cv2
import numpy as np

img = cv2.imread('m5.jpg')

kernel = (7,7)
#print(np.std(img))
blur = cv2.GaussianBlur(img,kernel,np.std(img))

cv2.imshow('img',blur)

cv2.waitKey(0)
cv2.destroyAllWindows()