import os
import cv2

# read image

img = cv2.resize(cv2.imread(os.path.join('.','Learning_OpenCV','data','bird.jpg')),(400,600))


# Convert BGR colorspace to RGB colorspace

img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Convert BGR to GRAY scale
img_Gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Convert BGR to HSV
img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


#visualize all colorspace images
cv2.imshow('img',img)
cv2.imshow('img_RGB',img_RGB)
cv2.imshow('img_Gray',img_Gray)
cv2.imshow('img_HSV',img_HSV)
cv2.waitKey(0)