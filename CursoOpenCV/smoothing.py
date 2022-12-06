import cv2 as cv

img = cv.imread('Cats/Cat3.jfif')
cv.imshow('Cats', img)

# Methods of blurring

# 1. Averaging Blur
average = cv.blur(img, (9,9))
cv.imshow('Average', average)

# 2. Gaussian Blur
gauss = cv.GaussianBlur(img, (9,9), 0)
cv.imshow('Gaussian', gauss)

# 3. Median Blur -> good for noise
median = cv.medianBlur(img, 9)
cv.imshow('Median', median)

# 4. Bilateral Blurring
bilat = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilat)

cv.waitKey(0)