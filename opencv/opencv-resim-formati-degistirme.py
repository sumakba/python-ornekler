import cv2

resim = cv2.imread('cevrilecek.jpg')
cv2.imwrite('cevrilmishali.png', resim, [cv2.IMWRITE_JPEG_QUALITY, 10])
print("işlem tamam!")