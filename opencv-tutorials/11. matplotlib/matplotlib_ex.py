import cv2
from matplotlib import pyplot as plt


img = cv2.imread('lena.jpg',-1)

# open cv shoes in BGR method
cv2.imshow('image',img)

#matlab shows in RGB mode
# so convert to Rgb
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)

plt.xticks([]),plt.yticks([]) # to remove the axes lines
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()