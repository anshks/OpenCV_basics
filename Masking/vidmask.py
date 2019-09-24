import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

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

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask_final)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask_final)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:  #esc key
        break
        
cap.release()
cv2.destroyAllWindows()
