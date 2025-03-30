import cv2
img = cv2.imread("Resources/house.png")
print(img.shape)
cv2.imshow("Original shape",img)
resizeimg = cv2.resize(img, (300,200)) #resizes the image width first and height second
print(resizeimg.shape)
cv2.imshow("resize image",resizeimg)
cv2.waitKey(0)