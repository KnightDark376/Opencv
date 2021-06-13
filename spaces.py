import cv2
import cv2 as cv
import numpy as np

img = cv.imread('picture/3.jpg')
cv.imshow('anh3',img)
# resized = cv.resize(img,(600,800), interpolation=cv.INTER_LINEAR)
# cv.imshow('resize',resized)

#BGR to Grayscale
gray = cv.cvtColor(img,cv2.COLOR_BGRA2GRAY)
cv.imshow('gray',gray)

#BGR to HSV
HSV = cv.cvtColor(img,cv2.COLOR_BGR2HSV)
cv.imshow('HSV',HSV)

#BGR to LAB
LAB = cv.cvtColor(img,cv2.COLOR_BGR2LAB)
cv.imshow('LAB',LAB)

#HSV to BGR
BGR = cv.cvtColor(HSV,cv2.COLOR_HSV2BGR)
cv.imshow('HSVtoBGR',BGR)



cv.waitKey(0)