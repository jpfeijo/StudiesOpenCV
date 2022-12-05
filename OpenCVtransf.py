# Aula 5 curso openCV
# Basic image transformation

import cv2 as cv
import numpy as np

img = cv.imread('Dogs/Dog3.jfif')

cv.imshow('Dog', img)

# Translating
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -> left
# -y -> up
# +x -> right
# +y -> down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# + anlge -> left
# - anlge -> right

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized', resized)

#Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# 0 flips the image vertically
# 1 flips the image horizontally
# -1 flips the image in both ways

#Cropping
cropped = img[200:300, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)