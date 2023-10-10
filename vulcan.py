import cv2

img = cv2.imread('lena.png', 0)
cv2.imshow('lena', img)
cv2.waitKey(0)
# cv2.imwrite('lena_gray.png', img)