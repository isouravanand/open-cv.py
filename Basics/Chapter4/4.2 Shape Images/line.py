import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#cv2.line(img,(0,0),(100,300),(0,255,0)) line making
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0)) #line making with specific height and width
cv2.imshow("line", img)
cv2.waitKey(0)