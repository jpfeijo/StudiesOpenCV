import cv2 as cv
import numpy as np

img = cv.imread('Cats/Cat4.jfif')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2-15, img.shape[0]//2-20), 60, 255, -1)
cv.imshow('Mask', mask)

maskRec = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2+100, img.shape[0]//2+100), 255, -1)
cv.imshow('Rectangle Mask', maskRec)


masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image', masked)

maskedRec = cv.bitwise_and(img,img,mask=maskRec)
cv.imshow('Rectangle Masked Image', maskedRec)


cv.waitKey(0)