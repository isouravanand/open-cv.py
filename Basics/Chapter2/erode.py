import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("Resources/cat.jpg")
canny = cv2.Canny(img,150,100)
dialImg = cv2.dilate(canny,kernel,iterations=1) #cv.dilate performs thickening or dilation effect
erodeImg = cv2.erode(dialImg,kernel, iterations=5)# cv.ereode thickening effect
cv2.imshow("Canny Image", canny)
cv2.imshow("Dialated Image",dialImg)
cv2.imshow("Erroded Image",erodeImg)
cv2.waitKey(0)