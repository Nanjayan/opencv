import numpy as np
import cv2

#img = cv2.imread('lena.jpg',1)

# instead of reading image, we can create a image 
# height,width,color/gray
img = np.ones([512,512,3],np.uint8)*45



# co-ordinates - from 2nd to 3rd argument
#colout = "BGR" - 4rd argument
# thickness - 5th argument
img = cv2.line(img,(0,0),(255,255),(0,255,0),5)

# arrowed line
img = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),5)

#Rectangle
#2nd - top left vertex
#3rd - bottom right vertex
# if we give -1 for thickness, it will be filled
img=cv2.rectangle(img,(300,0),(510,128),(0,0,255),-1)


#Circle
#2nd - center
#3rd - radius
img = cv2.circle(img,(440,60),63,(0,255,0),-1)


# Add text
#2nd - description
#3rd - co ordinates
#4th - font
#5th - font size
#6th color
#7th -thickness
#8th - line type
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255), 10, cv2.LINE_AA)



cv2.imshow('image',img)

cv2.waitKey(5000)
cv2.destroyAllWindows()