import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('equalization.png',1)
plt.subplot(2,2,1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(2,2,2)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title('Histogram')

plt.subplot(2,2,3)
img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])
img_output = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)
plt.imshow(img_output)
plt.title('Histogram Equalized Image')

plt.subplot(2,2,4)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img_output],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title('Histogram of Equalized Image')

plt.show()

cv.waitKey(0)
