#playing video files
import cv2
capVid = cv2.VideoCapture("Resources/catvid.mp4")
while True:
    success, frame = capVid.read()
    cv2.imshow("output", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):  # Press 'q' to exit
        break
