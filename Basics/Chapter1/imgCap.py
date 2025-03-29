#read images
import cv2
img = cv2.imread("Resources/cat.jpg") #imread reads image from given path
cv2.imshow("Output", img)   #imshow display impage
cv2.waitKey(0)      #waitKey is used to wait for window closure