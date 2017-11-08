import numpy as np
import cv2
from PIL import ImageGrab
img = ImageGrab.grab()
img_np = np.array(img)
height, width, channels = img_np.shape
n_h=height/(100)*85
n_w=width/(100)*85
n_h=int(n_h)
n_w=int(n_w)
kirpilmis_ekran = cv2.resize(img_np, (n_w,n_h))
ekran = cv2.cvtColor(kirpilmis_ekran, cv2.COLOR_BGR2GRAY)
cv2.imshow("Ekran", ekran)
cv2.waitKey(0)
cv2.destroyAllWindows()