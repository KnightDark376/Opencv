import cv2 as cv
import numpy as np

img = cv.imread('picture/1.jpg')

# cv.imshow('anh1', img)

#Tranformtration
def translate(img, x, y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat,dim)
trabslated = translate(img,1,1)
# cv.imshow('trans',trabslated)

#rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotmat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dim = (width, height)
    return cv.warpAffine(img,rotmat,dim)
Rotate = rotate(img,-45)
# cv.imshow('Roate', Rotate)
# Resize
resized = cv.resize(img,(600,600), cv.INTER_LINEAR)
# cv.imshow('Resized', resized)
#Flipping
fliped = cv.flip(img, -2)
# cv.imshow("flip", fliped)
#Cropping
croped = img[100:200,200:300]
cv.imshow('croped', croped)
cv.waitKey(0)
