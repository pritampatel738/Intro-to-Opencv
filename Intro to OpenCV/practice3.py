import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('tom.jpg')
fig = plt.figure(figsize=(3,3))
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()