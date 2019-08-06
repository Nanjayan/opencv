import cv2
import numpy as np 


# hough space, where a line in xy space represented by a point
# hough space, a point in xy space will be represented by a line

'''
1. Edge detection - canny edge
2. mapping of edge in hough space
3. Interpretation to infinite lines
4. Conversion of infinite lines to finite lines
'''

'''
Two types of hough line transform
1. standard houghline transform
2. Probabilistic houghline transform
'''


# here standard houghline transform
img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imshow("edges", edges)

# 2nd - rho , normally 1
# 3rd - theta value = pi/180
# 4th - threshold 
lines = cv2.HoughLines(edges, 1, np.pi/180,200)
# we get polar co ordinates

for line in lines:
    rho, theta = line[0]
    
    # converting polar to cartesian co-ordinates
    a = np.cos(theta)
    b = np.sin(theta)

    # origin values
    x0 = a * rho
    y0 = b * rho

    #x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    #y1 stores the rounded off value of (r * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    #x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    #y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow("image",img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()

# here standard houghline transform , lines run from one edge to 
# another edge. there is no stopping and it is computationally expensive
# It can be overcomed by Hough Lines P method