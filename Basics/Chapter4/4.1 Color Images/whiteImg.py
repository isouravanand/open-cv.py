import cv2
import numpy as np

image = np.ones((512,512)) # .ones makes white pixels
cv2.imshow("white image", image)
cv2.waitKey(0)