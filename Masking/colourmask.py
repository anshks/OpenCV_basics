import cv2
import numpy as np
img = cv2.imread('samplecircles.png', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of red color in HSV
lower_range1 = np.array([0, 100, 0], dtype=np.uint8)
upper_range1 = np.array([10, 255, 255], dtype=np.uint8)
lower_range2 = np.array([170, 100, 0], dtype=np.uint8)
upper_range2 = np.array([180, 255, 255], dtype=np.uint8)

# Threshold the HSV image to get only red colors
mask1 = cv2.inRange(hsv, lower_range1, upper_range1)
mask2 = cv2.inRange(hsv, lower_range2, upper_range2)

#final mask
mask_final=mask1 + mask2

cv2.imshow('mask',mask_final)
cv2.imshow('image', img)

while(1):
  k = cv2.waitKey(0)
  if(k == 27):
    break
cv2.destroyAllWindows()

