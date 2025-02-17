import cv2
import numpy as np
#inisialisasi kamera
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 #batas warna biru dalam HSV
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
 #masking mendeteksi biru
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
 #menentulan kontur
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 500:
           x, y, w, h = cv2.boundingRect(contour)
           cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
           cv2.putText(frame, "blue", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0),)
 #hasil ditampilkan
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break
cap.release()
cv2.destroyAllWindows()                