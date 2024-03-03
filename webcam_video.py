import os
import cv2


# read Webcam

webcam = cv2.VideoCapture(0)    # 0 is number of camera  OR id of webcam


# visualize webcam

while True:
    ret,frame = webcam.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()