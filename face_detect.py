import cv2 as cv

camera_id = 0
cap = cv.VideoCapture(camera_id)

while True:

    ret, farme = cap.read()
    gray = cv.cvtColor(farme,cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                               minNeighbors=3)
    print(f'Number of faces found = {len(face_rect)}')
    print(face_rect)
    if len(face_rect) != 0:
        for (x, y, w, h) in face_rect:
            dected = cv.rectangle(farme, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)
        cv.imshow('Face', dected)
    else:
        cv.imshow('Face',farme)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()


# img = cv.imread('picture/face3.jpg')
# cv.imshow('anhgoc', img)
#
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)
#
# haar_cascade = cv.CascadeClassifier('haar_face.xml')
# face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,
#                                           minNeighbors=3)
#
# print(f'Number of faces found = {len(face_rect)}')
# print(face_rect)
# for (x,y,w,h) in face_rect:
#     dected = cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0), thickness= 3)
# cv.imshow('dectec',dected)
#
#
# cv.waitKey(0)