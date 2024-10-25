import cv2 as cv

cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture = cv.VideoCapture(0)

while True:
    check, frame = video_capture.read()

    gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(gray_image, scaleFactor=2.0, minNeighbors=4)

    for x, y, w, h in face:
        image = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        image[y : y + h, x : x + w] = cv.medianBlur(image[y : y + h, x : x + w], 35)

    cv.imshow("face blurred", frame)
    key = cv.waitKey(1)

    if key == ord("q"):
        break

video_capture.release()
cv.destroyAllWindows()
