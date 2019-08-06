import numpy as np 
import cv2

# to work with ROI - Region of interest

img = cv2.imread('messi5.jpg')
img_2 = cv2.imread('opencv-logo.png')

print (img.shape) # returns a tuple of number of rows, columns and channels
print (img.size)  # return Total number of pixels accessed
print (img.dtype) # return Image datatype is obtained

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#get the pixel values of the ROI
ball = img[280:340,330:390]
#copy the ROI in some other part
img[273:333, 100:160] = ball

# Resize images for add operation
img = cv2.resize(img,(512,512))
img_2 = cv2.resize(img_2,(512,512))

#Adding two images
#dst = cv2.add(img,img_2)

# add weighted method for two images merging
# two images and their weight in percentage - 90 % 
# gamma correction - last argument

# weightedsum = (img_1 * alpha)+(img_2 * beta) + gamma
dst = cv2.addWeighted(img, .9, img_2, .1, 0)



cv2.imshow('image', dst)
cv2.waitKey(10000)
cv2.destroyAllWindows()