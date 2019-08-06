import numpy as np
import cv2


# draw circle on left click 
# and draw lines between them

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,255,0),-1)
        points.append((x,y))
        if len(points) >=2:
            cv2.line(img,points[-1], points[-2], (0,0,255),5)
        cv2.imshow('image',img)
    
    


img = np.zeros((512,512,3),np.uint8)
#img = cv2.imread('lena.jpg')

cv2.imshow('image',img)
points=[]

#to call the mouse event
#1st argument - window name
cv2.setMouseCallback('image', click_event)

cv2.waitKey(10000)
cv2.destroyAllWindows()