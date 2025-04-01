import cv2
import numpy as np

#function to stack images
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)

    # Get reference width & height from first image
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(rows):
            for y in range(cols):
                if imgArray[x][y].shape[:2] == (height, width):
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (width, height), None, scale, scale)

                # Convert grayscale to BGR for uniform stacking
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        hor = [np.hstack(imgArray[x]) for x in range(rows)]
        ver = np.vstack(hor)
    else:
        for x in range(rows):
            imgArray[x] = cv2.resize(imgArray[x], (width, height), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        ver = np.hstack(imgArray)

    return ver

def empty():
    pass
path = ("Resources/house.png")
cv2.namedWindow("Track Bars")
cv2.resizeWindow("Track Bars",640,240)
#cv2.createTrackbar("AnyName","nameWindow",startingPt,endingPt,funToBeExeAfterEveryTrackbarCHnage)
cv2.createTrackbar("Hue Min","Track Bars",0,179,empty)
cv2.createTrackbar("Hue Max","Track Bars",179,179,empty)
cv2.createTrackbar("Sat Min","Track Bars",139,255,empty)
cv2.createTrackbar("Sat Max","Track Bars",255,255,empty)
cv2.createTrackbar("Val Min","Track Bars",139,255,empty)
cv2.createTrackbar("Val Max","Track Bars",255,255,empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #BGR color converted to HSV
    h_min = cv2.getTrackbarPos("Hue Min","Track Bars")
    h_max = cv2.getTrackbarPos("Hue Max","Track Bars")
    s_min = cv2.getTrackbarPos("Sat Min","Track Bars")
    s_max = cv2.getTrackbarPos("Sat Max","Track Bars")
    v_min = cv2.getTrackbarPos("Val Min","Track Bars")
    v_max = cv2.getTrackbarPos("Val Max","Track Bars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min,s_min,v_min])
    upper =np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    maskresult = cv2.bitwise_and(img,img,mask=mask)
  

    # cv2.imshow("HSV image", imgHSV)
    # cv2.imshow("Normal image", img)
    # cv2.imshow("Masked Img", mask)
    # cv2.imshow("Result Img", maskresult)

    stackedImg = stackImages(0.2, [[imgHSV, img, mask,maskresult]])

    cv2.imshow("Stacked Images", stackedImg)
    cv2.waitKey(1)