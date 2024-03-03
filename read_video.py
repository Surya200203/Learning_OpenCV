import os
import cv2


# read video

video_path = os.path.join('.','Learning_OpenCV','data','forest_video.mp4')

video = cv2.VideoCapture(video_path)

#visualize video

ret = True
while True:
    ret, frame = video.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()   # to release memory
cv2.destroyAllWindows()
