import cv2
import numpy as np

img = cv2.imread('picture/2.jpg')
cv2.imshow('img', img)

blank = np.zeros(img.shape,dtype='uint8')
cv2.imshow('blank', blank)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

blur = cv2.GaussianBlur(gray,(5,5), cv2.BORDER_DEFAULT)
cv2.imshow('blur',blur)

candy = cv2.Canny(blur,125,125)
cv2.imshow('canny edge', candy)

ret, thresd = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
cv2.imshow('thresd', thresd)

coutour, hierarchies = cv2.findContours(thresd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(coutour))
cv2.drawContours(blank,coutour,-1,(0,0,255),2)
# cv2.imshow('blankk', blank)

cv2.waitKey(0)