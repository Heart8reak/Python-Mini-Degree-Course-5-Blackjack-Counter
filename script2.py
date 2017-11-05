import cv2

img1 = cv2.imread('test.jpg', 0)
img2 = cv2.imread('example.jpg',0)

#_, thresh1 = cv2.threshold(img1, 140, 255, cv2.THRESH_BINARY_INV)
_, thresh2 = cv2.threshold(img2, 225, 255, cv2.THRESH_BINARY)

cv2.imshow('tresh2', thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()
