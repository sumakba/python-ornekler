import cv2

resim = cv2.imread('ataturk.jpg', cv2.IMREAD_COLOR)
if resim is not None:
    cv2.imshow('ilk resim', resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Böyle bir resim bulunmuyor.")

# aynı dizinde ataturk.jpg olmalıdır.