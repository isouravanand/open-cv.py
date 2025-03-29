#reading from webcam
import cv2
webCap = cv2.VideoCapture(0)
webCap.set(3,640) #3 for width ID
webCap.set(4,480) #4 for height ID
webCap.set(10,100)
while True:
    success, frame = webCap.read()
    cv2.imshow("output", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):  # Press 'q' to exit
        break
