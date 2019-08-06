import cv2
import numpy as np 
from matplotlib import pyplot as plt 

'''
# it has five steps
1. Noise reduction - gaussian filter
2. Gradient calculation - intensity calculation
3. Non-maximum supression - get rid of spurious response
4. Double threshold - potential edge detection
5. Edge Tracking by Hysteresis - track edges by removing weak
'''


img = cv2.imread("messi5.jpg",0)

canny = cv2.Canny(img,100, 200)

titles =['image','canny']
images = [img,canny]

for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()