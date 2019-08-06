import cv2
import numpy as np 
from matplotlib import pyplot as plt 


img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)

#laplacian - gradient - direction change in color or intensity of the image
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) #kernelsize
lap = np.uint8(np.absolute(lap))


#sobel_gradient representation - gradient in x or y direction
#sobel_x
sobelX = cv2.Sobel(img,cv2.CV_64F, 1, 0) #dx,dy - 1,0
sobelX = np.uint8(np.absolute(sobelX))
#sobel_y
sobelY = cv2.Sobel(img,cv2.CV_64F,0, 1) #dx,dy - 0, 1
sobelY = np.uint8(np.absolute(sobelY))

sobel_combined = cv2.bitwise_or(sobelX,sobelY)


canny =cv2.Canny(img,100,200)

titles = ['image','laplacian','sobelX','sobelY',"combined",'canny']
images =[img, lap, sobelX, sobelY, sobel_combined,canny]


for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()