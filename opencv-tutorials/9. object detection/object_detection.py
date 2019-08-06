import cv2
import numpy as np 


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("lower_hue","Tracking", 0, 255, nothing)
cv2.createTrackbar("lower_saturation","Tracking", 0, 255, nothing)
cv2.createTrackbar("lower_value","Tracking", 0, 255, nothing)
cv2.createTrackbar("upper_hue","Tracking", 255, 255, nothing)
cv2.createTrackbar("upper_saturation","Tracking", 255, 255, nothing)
cv2.createTrackbar("upper_value","Tracking", 255, 255, nothing)




while True:

    # using images to detect object
    #frame = cv2.imread('smarties.png')
    
    # using video to detect object
    _,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # make lower bound and upper bound for HSV image
    # HSV - Hue, value , saturation
    l_b_1 = np.array([110,50,50])
    u_b_1 = np.array([130,255,255])


    # get the lower bound and upper bound from trackbar
    l_h = cv2.getTrackbarPos("lower_hue","Tracking")
    l_s = cv2.getTrackbarPos("lower_saturation","Tracking")
    l_v = cv2.getTrackbarPos("lower_value","Tracking")

    u_h = cv2.getTrackbarPos("upper_hue","Tracking")
    u_s = cv2.getTrackbarPos("upper_saturation","Tracking")
    u_v = cv2.getTrackbarPos("upper_value","Tracking")

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv,l_b,u_b)

    res = cv2.bitwise_and(frame, frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()