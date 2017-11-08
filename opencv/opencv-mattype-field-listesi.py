import cv2

isimler = [i for i in dir(cv2) if i.startswith('CV_')]
print(isimler)