import os
import cv2


# reading image
img = cv2.resize(cv2.imread(os.path.join('.','Learning_OpenCV','data','freelancer.jpg')),(550,400))


# classical blur() function

k_size = 7
img_blur = cv2.blur(img,(k_size,k_size))

# GaussianBlur() Function

img_gaussianBlur = cv2.GaussianBlur(img,(k_size,k_size),3)

# medianBlur() Function

img_medianBlur = cv2.medianBlur(img,k_size)

# visualize image
cv2.imshow('img',img)
cv2.imshow('img_blur',img_blur)
cv2.imshow('img_gaussianBlur',img_gaussianBlur)
cv2.imshow('img_medianBlur',img_medianBlur)
cv2.waitKey(0)