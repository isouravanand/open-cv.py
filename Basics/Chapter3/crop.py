import cv2
image = cv2.imread("Resources/house.png")
print (image.shape) #.shape provides image size
cropImg = image[100:400, 300:600] #first is height and second is width
print (image.shape)
cv2.imshow("Cropped image", cropImg)
cv2.imshow("og iamge", image)
cv2.waitKey(0)