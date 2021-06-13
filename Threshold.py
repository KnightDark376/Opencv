import cv2 as cv
import numpy as np

img = cv.imread('picture/7.jpg')
cv.imshow('anh7', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#thresholding simple
threshold, thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('thresh', thresh)
# print(thresh.shape)

#Adaptive Thresholding
Adap_thresh = cv.adaptiveThreshold(gray,255,cv.THRESH_BINARY,cv.ADAPTIVE_THRESH_GAUSSIAN_C,15,5)
cv.imshow('Adaptive Threshold', Adap_thresh)

cv.waitKey(0)