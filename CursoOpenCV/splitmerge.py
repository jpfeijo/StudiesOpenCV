import cv2 as cv
import numpy as np

img = cv.imread('Dogs/Dog1.jfif')
cv.imshow('Dog', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Red', red)
cv.imshow('Green', green)

print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

merged = cv.merge([r,g,b])
cv.imshow('Merged Image', merged)

cv.waitKey(0)