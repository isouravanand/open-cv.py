import cv2
import numpy as np

image = np.zeros((512,512)) #made matrix filled black 512 x 512 pixels
print(image.shape)
cv2.imshow("black image", image)
cv2.waitKey(0)