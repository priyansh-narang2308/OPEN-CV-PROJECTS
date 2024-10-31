import numpy as np
import cv2 as cv
import imutils
import datetime

gun_cascade = cv.CascadeClassifier("cascade.xml")
camera = cv.VideoCapture(0)

firstFrame = None
gun_exist = None

while True:

    ret, frame = camera.read()

    frame = imutils.resize(frame, width=500)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    if len(gun) > 0:
        gun_exist = True

    for x, y, w, h in gun:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_fray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]

    if firstFrame is None:
        firstFrame = gray
        continue

    cv.imshow("Security Feed", frame)
    key = cv.waitKey(1) & 0xFF

    if key == ord("q"):
        break

if gun_exist:
    print("Guns Detected!!")
else:
    print("Guns Not Detected!!")

camera.release()
cv.destroyAllWindows
