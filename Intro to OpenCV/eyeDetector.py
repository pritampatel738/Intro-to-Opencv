import cv2
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
cap = cv2.VideoCapture(0)

eyeCascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')
faceCascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')


while 1:
    
    ret , pic = cap.read()
    #print(ret)
    #print(type(pic))
    
    if not ret:
        break
        
    img = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(img,1.3,5)
    
    #print("The number of faces is : ",len(face))
    
    for (x,y,w,h) in face:
        #cv2.rectangle(pic,(x,y),(x+w,y+h),(255,255,255))
        eyePic = img[y:y+h,x:x+w]
        img1 = pic[y:y+h,x:x+w]
        eye = eyeCascade.detectMultiScale(eyePic,1.3,5)
        print("The number of eyes are : ",len(eye))
        #if len(eye) == 0:
         #   print("Fucked up")
        for (a,b,c,d) in eye:
            cv2.rectangle(img1,(a,b),(a+c,b+d),(255,255,255))
        
        
        
    cv2.imshow('img',pic)
    k = cv2.waitKey(30) & 0xFF
    
    if k==2:
        break
        
cap.release()
#cv2.waitKey(0)
cv2.destroyAllWindows()
    
    