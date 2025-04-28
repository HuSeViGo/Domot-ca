import cv2

img= cv2.imread('stop.jpg',1)
img_HSV=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_GRAY=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('BGR', img)
cv2.imshow('Escala grises', img_GRAY)
cv2.imshow('HSV', img_HSV)
cv2.waitkey(0)
cv2.destroyAllWindows()