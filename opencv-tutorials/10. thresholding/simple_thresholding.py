import cv2 as cv
import numpy as np 

img = cv.imread('gradient.png',0)

# threshold the image. pixel under threshold - 0 else - 1
# threshold value - 127
# various types of threshold are there
ret, th1 = cv.threshold(img,127,255, cv.THRESH_BINARY ) # white/black
ret, th2 = cv.threshold(img,127,255, cv.THRESH_BINARY_INV ) # inverte white/black
ret, th3 = cv.threshold(img,127,255, cv.THRESH_TRUNC ) # >threshold is equal to threshold value 
ret, th4 = cv.threshold(img,127,255, cv.THRESH_TOZERO ) # below threshold all are black
ret, th5 = cv.threshold(img,127,255, cv.THRESH_TOZERO_INV ) # above threshold all are black

cv.imshow("Image",img)
cv.imshow("th1",th1)
cv.imshow("th2",th2)
cv.imshow("th3",th3)
cv.imshow("th4",th4)
cv.imshow("th5",th5)

cv.waitKey(0)
cv.destroyAllWindows()