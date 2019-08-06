import cv2
import numpy as np 


cap = cv2.VideoCapture('vtest.avi')

ret, frame_1 = cap.read()
ret, frame_2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame_1,frame_2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #with disturbances
    #cv2.drawContours(frame_1,contours, -1, (0,255,0), 2)

    for contour in contours:
        (x,y, w, h) = cv2.boundingRect(contour) # x cordinate, y cordinate, width, height

        if cv2.contourArea(contour) < 1000 :
            continue
        
        cv2.rectangle(frame_1, (x,y), (x+w,y+h), (0,255,0), 2)

        cv2.putText(frame_1,"Status: {}".format("Movement"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255),3)


    cv2.imshow("feed", frame_1)
    frame_1 = frame_2
    ret, frame_2 = cap.read()


    if cv2.waitKey(40) ==27:
        break





cv2.destroyAllWindows()
cap.release()