import cv2
import numpy as np 
from matplotlib import pyplot as plt 


img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)


# 2 by 2 square shape kernel
kernal = np.ones((2,2),np.uint8)

# use dialation transformation to clear the spots in the image
# kernel applied on mask
dialation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal, iterations=1) #erode the edges 
# will be 1 only if all the elements in the kernal are 1. else 0


opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) #erosion followed by the dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal) #dialation followed by the erosion

gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal) # dilation - erosion  
top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal) # image - opening
black_hat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernal) 

titles = ['image','mask','dialation','erosion','opening','closing','gradient','top_hat','black_hat']
images =[img, mask,dialation, erosion, opening,closing,gradient,top_hat,black_hat]


for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()