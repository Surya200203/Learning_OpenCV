import os
import cv2

#reading image
img = cv2.imread(os.path.join('.','Learning_OpenCV','data','mustang.jpg'))

#shape
print(img.shape)

#resize image

resized_img = cv2.resize(img,(640,480))

# visualize image
cv2.imshow('img',resized_img)
cv2.waitKey(0)

