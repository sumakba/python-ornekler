import numpy as np
import cv2

kamera = cv2.VideoCapture(0) # kamera görüntüsünü alıyoruz.

while(True):
    ret, goruntu = kamera.read() # kameradan gelen fotoğrafı while döngüsü içinde okuyoruz bu yüzden video şeklinde görüyoruz.
    grigoruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY) # bu şekilde renksizleştiriyoruz.
    cv2.imshow('Ekran',grigoruntu) # gri yaptığımız ekranı imshow ile ekranda gösteriyoruz.
    if cv2.waitKey(1) & 0xFF == ord('q'): # Q'ya basılması halinde görüntüyü kesiyor.
        break

kamera.release()
cv2.destroyAllWindows()