import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
#cv2.putText(img,"TEXT",(width,height),cv2.FONT, scale, (B,G,R),Thickness)
cv2.putText(img,"OPECV ",(300,100),cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0),1)
cv2.imshow("Text On Image",img)
cv2.waitKey(0)