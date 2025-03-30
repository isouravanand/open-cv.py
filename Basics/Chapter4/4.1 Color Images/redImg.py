import cv2
import numpy as np

image = np.zeros((512,512,3),np.uint8)
print(image.shape)
image[:] = 0,0,250# B,G,R i.e, 0,0,255 for RED
cv2.imshow("Red Image", image)
cv2.waitKey(0)