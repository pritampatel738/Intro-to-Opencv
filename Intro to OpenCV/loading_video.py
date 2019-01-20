import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture('1.mp4')
ret = True
while cap.isOpened():

	ret , frame = cap.read()
	cv2.imshow('vid',frame)

	if not ret:
		break


cap.release()
cv2.destroyAllWindows()