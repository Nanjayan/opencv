import cv2

#To read the image
# flag is the second argument
# 1- color , 0- greyscale, -1 - unchanged
img = cv2.imread('lena.jpg',-1)

# above pixels are stored in img variable

# To display the image
cv2.imshow('image', img)  # displays image only for short time

ascii_key = cv2.waitKey(5000)  # wait for 5 seconds
# If you pass 0 in waitkey , it waits forever
# return of waitkey is the ascii code of the character of the key pressed

cv2.destroyAllWindows()

#Copy the image into another file
cv2.imwrite('lena-copy.png',img)