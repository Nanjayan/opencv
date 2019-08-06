import cv2
import numpy as np 


# pyramid
#1. Gaussian pyramid
#2. Laplacian pyramid - developed from gaussian

# they are used to blend the images and
# reconstruct the images


img = cv2.imread("lena.jpg")

layer = img.copy()
gp =[layer]

# gaussian pyramids
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

# laplacian filter
layer = gp[5]
cv2.imshow('upper level gp', layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i),laplacian)

# reduce the resolution, 1/4 or 1/8 of the image
lr = cv2.pyrDown(img)

# increase the resolution
hr = cv2.pyrUp(lr)
# it will be blury as some information has
# been lost in the previous step



cv2.imshow("Original image", img)
cv2.imshow("pyrDown image", lr)
cv2.imshow("pyrup image", hr)
cv2.waitKey(0)
cv2.destroyAllWindows()