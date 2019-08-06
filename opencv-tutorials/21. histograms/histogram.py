import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt 

# 1. is using histogram from matplotlib
# 2. Using calculate hist in cv2

img = np.zeros((200,200), np.uint8)
cv.rectangle(img, (0,100), (200,200), (255,255,255),-1)
cv.rectangle(img, (0,50), (100,100), (127),-1) # can give one value in colour instead of three


img = cv.imread("lena.jpg",-1)
b, g, r = cv.split(img)

cv.imshow("Image", img)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

# calculate histogram using matplotlib
plt.hist(img.ravel(),255,[0,255])
plt.hist(b.ravel(),255,[0,255])
plt.hist(g.ravel(),255,[0,255])
plt.hist(r.ravel(),255,[0,255])
plt.show()

img = cv.imread("lena.jpg",0)
# channel 0 for one channel for rgb, give 0,1,2
hist = cv.calcHist([img],[0], None,[256],[0,255])

plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()