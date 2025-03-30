import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#cv2.circle(img,(height,width),radius ,(B,G,R),Thickness)
cv2.circle(img,(240,240), 50,(255,255,0),5)
cv2.imshow("Circle", img)
cv2.waitKey(0)