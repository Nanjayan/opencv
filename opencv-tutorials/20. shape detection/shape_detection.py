import numpy as np 
import cv2


img = cv2.imread('shapes.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 225,255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


for contour in contours:
    
    # approximates polygonal curves with atmost precision
    # episilion =0.01 (approximation accuracy)
    # arc length - curve length True - closed contour , False - open contour
    # Last True - closed, False - open
    approx = cv2.approxPolyDP(contour,0.01 * cv2.arcLength(contour,True), True)
    
    # instead of giving number of arguments - we can give in square bracket
    # 0 since we operate only one at a time
    cv2.drawContours(img, [approx], 0, (0,0,0), 5)
    # gives the x and y co-ordinates
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    # based on the contours number, we name the objects
    if len(approx) == 3:
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx) == 4:
        _, _, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        print (aspect_ratio)
        if aspect_ratio >=0.95 and aspect_ratio <= 1.05:
            cv2.putText(img,"Square",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        else:
            cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx) == 5:
        cv2.putText(img,"Pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx) == 6:
        cv2.putText(img,"Hexagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    else :
        cv2.putText(img,"Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

cv2.imshow("shapes", img)

cv2.waitKey(0)
cv2.destroyAllWindows()