import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('myhand.jpg',0)
# global thresholding
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# Otsu's thresholding
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# plot all the images and their histograms
images = [img, th1,
          img, th2,
          blur, th3]
titles = ['Original Image','Global Thresholding (v=127)',
          'Original Image',"Otsu's Thresholding",
          'Gaussian filtered Image',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,2,i*2+1),plt.imshow(images[i*2],'gray')
    plt.title(titles[i*2]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,2,i*2+2),plt.imshow(images[i*2+1],'gray')
    plt.title(titles[i*2+1]), plt.xticks([]), plt.yticks([])
plt.show()
