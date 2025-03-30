import cv2
import numpy as np
img = cv2.imread("Resources/card.png")

width,height = 250,350
pts1 = np.float32([],[],[],[])
pts2 = np.float32([],[],[],[])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOut = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("output", imgOut)