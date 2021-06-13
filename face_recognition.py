import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben', 'John']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img= cv.imread(r'picture/test.jpg')
# img = cv.resize(img1,(600,420),interpolation=cv.INTER_LINEAR)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=9)
print(faces_rect)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (x,y-10), cv.FONT_ITALIC, 1.0, (0,255,0), thickness=1)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)