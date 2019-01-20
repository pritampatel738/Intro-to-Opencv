import cv2
import numpy as np

img = cv2.imread('m5.jpg')
pic = np.zeros((500,500,3),dtype='uint8')

# cv2.rectangle(img,start_idx,end_idx,color_of_rectangle,thickness,lineType,shift)
cv2.rectangle(img,(10,10),(150,150),(0,0,255),2,lineType=0,shift=0)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()