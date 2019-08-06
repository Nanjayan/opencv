import cv2
import numpy as np 
from matplotlib import pyplot as plt 


img = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


# 2 by 2 square shape kernel
kernel = np.ones((5,5),np.float32) / 25   # (1/K.width * K.height) * image

# Homogenous filter
dst =cv2.filter2D(img, -1, kernel)

# blurring
blur = cv2.blur(img, (5, 5))

# gaussian blur 
#3rd argument - sigma_x
g_blur =cv2.GaussianBlur(img,(5,5),0)

#median filter
#kernel should be odd other than 1
# 1 will be similiar tto original image
median = cv2.medianBlur(img,5)

# Bilateral filter 
# edges are preserved  by this method
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image','2D_filt','blur','g_blur','median','bilateral']
images =[img, dst, blur, g_blur,median, bilateral]


for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()