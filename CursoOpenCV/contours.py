# Aula 6 curso OpenCV
# How to identify countours in images

import cv2 as cv
import numpy as np

img = cv.imread('Dogs/Dog3.jfif')
cv.imshow('Dog', img)

# Creating a blank image that will be used to draw the contours
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


# Trying to find the edges of the image
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)


# Trying to find the contours of the image
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) # or none
print(f'{len(contours)} contour(s) found! ')

# Drawing the contours of the image
cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('Contours', blank)



cv.waitKey(0)