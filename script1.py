import cv2

img1 = cv2.imread('test.jpg', 0)
img2 = cv2.imread('test2.jpg',0)

_, thresh1 = cv2.threshold(img1, 140, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('tresh1', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()
