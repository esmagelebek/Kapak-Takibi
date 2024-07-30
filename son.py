import cv2 as cv
import numpy as np

# Siyah bir görüntü oluştur
res = np.zeros((400, 400, 3), np.uint8)

cv.namedWindow("Trackbar")

def fonk(sayi):
    print(sayi)

# Trackbar'ları oluştur
cv.createTrackbar("azM", "Trackbar", 0, 255, fonk)
cv.createTrackbar("cokM", "Trackbar", 0, 255, fonk)
cv.createTrackbar("azY", "Trackbar", 0, 255, fonk)
cv.createTrackbar("cokY", "Trackbar", 0, 255, fonk)
cv.createTrackbar("azK", "Trackbar", 0, 255, fonk)
cv.createTrackbar("cokK", "Trackbar", 0, 255, fonk)

# VideoCapture nesnesini oluştur
takip = cv.VideoCapture("takip.mp4")

if not takip.isOpened():
    print("Video açılamadı.")
    exit()

while True:
    kontrol, yakala = takip.read()
    if not kontrol:
        print("Video sonlandı.")
        break

    azM = cv.getTrackbarPos("azM", "Trackbar")
    cokM = cv.getTrackbarPos("cokM", "Trackbar")
    azY = cv.getTrackbarPos("azY", "Trackbar")
    cokY = cv.getTrackbarPos("cokY", "Trackbar")
    azK = cv.getTrackbarPos("azK", "Trackbar")
    cokK = cv.getTrackbarPos("cokK", "Trackbar")

    az = np.array([azK, azY, azM])
    cok = np.array([cokK, cokY, cokM])

    istenen = cv.inRange(yakala, az, cok)
    son = cv.bitwise_and(yakala, yakala, mask=istenen)

    cv.imshow("Trackbar", res)
    cv.imshow("Video", yakala)
    cv.imshow("Istenen", istenen)
    cv.imshow("Son Hal", son)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

takip.release()
cv.destroyAllWindows()
