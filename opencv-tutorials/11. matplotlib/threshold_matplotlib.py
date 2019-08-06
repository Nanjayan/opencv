import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

img = cv.imread('gradient.png',0)

# threshold the image. pixel under threshold - 0 else - 1

# various types of threshold are there
ret, th1 = cv.threshold(img,50,255, cv.THRESH_BINARY ) # white/black
ret, th2 = cv.threshold(img,200,255, cv.THRESH_BINARY_INV ) # inverte white/black
ret, th3 = cv.threshold(img,127,255, cv.THRESH_TRUNC ) # >threshold is equal to threshold value 
ret, th4 = cv.threshold(img,127,255, cv.THRESH_TOZERO ) # below threshold all are black
ret, th5 = cv.threshold(img,127,255, cv.THRESH_TOZERO_INV ) # above threshold all are black

titles = ['Original Image', 'Binary', 'BINARY_INV','TRUNC', 'TOZERO', 'TOZERO_INV ' ]
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
