import cv2
import numpy as np

image = np.zeros((512,512,3),np.uint8)
print(image.shape)
image[:] = 255,0,0 # [:] completely fills matrix, B,G,R i.e, 255,0,0 for BLUE
#image[200:300,100:300] adjust the size
cv2.imshow("blue image", image)
cv2.waitKey(0)
#image[200:300,100:300] adjust the size