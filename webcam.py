import cv2
import numpy as np
cam=cv2.VideoCapture(0)
while True:
	b, img = cam.read()
	if b:
		cv2.imshow("Window",img)
	else:
		print("The Camera Is Not Working")
		break
	key = cv2.waitKey(1)&0xFF
	if key==ord('q'):
		break
cv2.destroyAllWindows()
cam.release()
