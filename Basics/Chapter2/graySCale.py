import cv2

img = cv2.imread("Resources/cat.jpg")
grayCol = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #cvtColor converts color tp COLOR_BGR2GRAY
cv2.imshow("Grey Scale", grayCol)
cv2.waitKey(0)
