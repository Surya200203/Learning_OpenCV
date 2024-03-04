import os
import cv2

# reading image

img = cv2.imread(os.path.join('.','Learning_OpenCV','data','bear.jpg'))

# converting image to greyscale

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# simple threshold

ret , thresh = cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY)

# removing noise
noise_removed_thresh = cv2.blur(thresh,(90,90))
ret , noise_removed_thresh = cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY)

# visualize image
# cv2.imshow('img',img)
# cv2.imshow('img_gray',img_gray)
cv2.imshow('thresh',thresh)
cv2.imshow('noise_removed_thresh',noise_removed_thresh)
cv2.waitKey(0)