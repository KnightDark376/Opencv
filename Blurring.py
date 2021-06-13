import cv2 as cv
import numpy as np
# Id_camera = 0
# cap = cv.VideoCapture(Id_camera)
# while True:
#     sucess, farme = cap.read()
#     # Bilater = cv.bilateralFilter(farme, 5, 180, 150)
#     gauss = cv.GaussianBlur(farme, (9, 13), 0)
#     gray = cv.cvtColor(gauss,cv.COLOR_BGR2GRAY)
#     ret, Thresd = cv.threshold(gray,125,255,cv.THRESH_BINARY)
#     cv.imshow('webcam', Thresd)
#
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()



img = cv.imread('picture/5.jpg')
cv.imshow('anh5',img)

#Averaging
average = cv.blur(img,(3,3))
cv.imshow('Averaging',average)

#Gaussian Blur
gauss = cv.GaussianBlur(img,(3,3), 0)
cv.imshow('gaussian blur', gauss)

#Median Blur
median = cv.medianBlur(img,3)
cv.imshow('Median Blur', median)

#bilateral
Bilater = cv.bilateralFilter(img,5,100,355)
cv.imshow('Bilater', Bilater)

# gray = cv.cvtColor(Bilater,cv.COLOR_BGR2GRAY)
# ret, thresd = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
# cv.imshow('Thresd', thresd)


cv.waitKey(0)