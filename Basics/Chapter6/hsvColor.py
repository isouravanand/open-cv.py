import cv2 

path = cv2.imread("Resources/house.png")
imgHSV = cv2.cvtColor(path,cv2.COLOR_BGR2HSV) #BGR color converted to HSV
cv2.imshow("HSV image", imgHSV)
cv2.imshow("Normal image", path)
cv2.waitKey(0)