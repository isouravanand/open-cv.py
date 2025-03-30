import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#cv2.rectangle(img,(0,0),(100,300),(0,0,255),2) here 2 is thickness and make a hollow rectangle
cv2.rectangle(img,(0,0),(150,300),(0,0,255),cv2.FILLED) #cv.FILLED fills rectangle with color
cv2.imshow("line", img)
cv2.waitKey(0)