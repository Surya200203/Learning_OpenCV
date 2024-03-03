import cv2
import os


#read image
image_path = os.path.join('.','Learning_OpenCV','data','war_field.png')

img = cv2.imread(image_path)


# write image

#cv2.imwrite(os.path.join('.','Learning_OpenCV','images','balls_out.jpg'))

# visualize image

cv2.imshow('image',img)   # imshow(windowName , image)
cv2.waitKey(0)          # to tell openCV to wait until I press a Key  (imp.)