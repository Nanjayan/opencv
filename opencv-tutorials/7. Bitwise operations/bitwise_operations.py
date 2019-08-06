import cv2
import numpy as np 



img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255),-1)

img2 = np.zeros((250,500,3),np.uint8)
img2 = cv2.rectangle(img2, (250,0), (500,250), (255,255,255),-1)


# bit wise operations for two images
bit_and = cv2.bitwise_and(img2,img1)
bit_or = cv2.bitwise_or(img2,img1)
bit_xor = cv2.bitwise_xor(img2,img1)
bit_not1 = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_xor",bit_xor)
cv2.imshow("bit_not1",bit_not1)
cv2.imshow("bit_not2",bit_not2)

cv2.waitKey(5000)
cv2.destroyAllWindows()