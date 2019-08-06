import cv2 as cv 
import numpy as np 

# adaptive threshold means threshold in smaller regions of interest
# instead of global image
img = cv.imread('sudoku.png',0)
_, th1 = cv.threshold(img,127,255, cv.THRESH_BINARY)
#threshold is the mean of the neighbourhood
#5th argument - blocksize
#6th argument c - constant
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)

cv.waitKey(0)
cv.destroyAllWindows()