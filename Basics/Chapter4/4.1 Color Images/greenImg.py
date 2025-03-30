import cv2
import numpy as np

image = np.zeros((512,512,3),np.uint8)
print(image.shape)
image[:] = 0,255,0 # B,G,R i.e, 0,255,0 for GREEN
cv2.imshow("Green Image", image)
cv2.waitKey(0)