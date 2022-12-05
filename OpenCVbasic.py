import cv2 as cv

# basicos de openCVcv
img = cv.imread('Dogs/dog5.jfif')

cv.imshow('Dog', img)

# Convertendo pra uma escala em cinza

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge cascade (Bordas) -> Quanto menos blur, mais bordas serão detectadas (mais detalhes)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image 
dilated = cv.dilate(canny, (5,5), iterations=1)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (5,5), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
 