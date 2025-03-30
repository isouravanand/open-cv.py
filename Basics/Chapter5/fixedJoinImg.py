import cv2
import numpy as np

# Function to stack images dynamically
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

img = cv2.imread("Resources/card.png")

# Convert to Grayscale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

stackedImg = stackImages(0.5, [[img, img, grayImg], [img, img, img]])

cv2.imshow("Stacked Images", stackedImg)
cv2.waitKey(0)

