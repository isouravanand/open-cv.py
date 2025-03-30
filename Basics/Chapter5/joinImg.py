import cv2
import numpy as np

img = cv2.imread("Resources/card.png")
imgHor = np.hstack((img,img))#joins two imahes horizontally

imgVer = np.vstack((img,img))#joins two imahes horizontally
cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)
cv2.waitKey(0)

#issues with this methods
#1. Image resize is difficult adding multiple images fills the or overflows the display
#2. both images must have same rgb value for execution