import cv2

img = cv2.imread("Resources/cat.jpg")
blurImg = cv2.GaussianBlur(img,  (23,23),0) #must be in odd we used GaussianBlur
cv2.imshow("Og image", img)
cv2.imshow("blur image", blurImg)
cv2.waitKey(0)
