import cv2
import numpy as np
import winsound
camera= cv2.VideoCapture(0)
while camera.isOpened():
    success1,frame1=camera.read()
    success2,frame2=camera.read()

    
    frame1=cv2.flip(frame1,1)
    frame2=cv2.flip(frame2,1)
    

    difference=cv2.absdiff(frame1,frame2)
    gray_image= cv2.cvtColor(difference,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray_image,(5,5),0)
    _,thress= cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thress,None, iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    #Looping
    for contour in contours:
        if cv2.contourArea(contour)<4000:
            continue

        x,y,w,h =cv2.boundingRect(contour)
        cv2.putText(frame1 ,'',(x,y-30,cv2.FONT_HERSHEY_PLAIN))

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,255),3)
        winsound.PlaySound("",winsound.SND_ASYNC)
    cv2.imshow('Security Feed',frame1)
    if cv2.waitKey(30) & 0xFF ==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()    



