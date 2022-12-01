import cv2 as cv

img = cv.imread('Dogs/dog5  .jfif')

cv.imshow('Dog', img)

# Convertendo pra uma escala em cinza
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)
