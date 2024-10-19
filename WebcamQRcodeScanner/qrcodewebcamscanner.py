import cv2 as cv
import webbrowser

cap = cv.VideoCapture(0)
detector = cv.QRCodeDetector()

while True:
    _, img = cap.read()

    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        a = data
        break

    cv.imshow("QRCODEscanner", img)

    if cv.waitKey(1) == ord("q"):
        break


if a:
    webbrowser.open(str(a))


cap.release()
cv.destroyAllWindows()
