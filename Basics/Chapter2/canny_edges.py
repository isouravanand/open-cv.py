import cv2
img = cv2.imread("Resources/cat.jpg")
canny = cv2.Canny(img,150,100)
cv2.imshow("Canny Image", canny)
cv2.waitKey(0)