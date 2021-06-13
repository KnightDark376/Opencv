import cv2 as cv
import numpy as np

img = cv.imread('picture/4.jpg')
cv.imshow('anh4',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b, blank,blank])
green = cv.merge([blank, g,blank])
red = cv.merge([blank, blank,r])
mergered = cv.merge([b, g,r])


cv.imshow('blue',blue)
cv.imshow('red',red)
cv.imshow('green',green)
cv.imshow('mergered',mergered)

cv.waitKey(0)