import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Dogs/Dog1.jfif')
cv.imshow('Dog', img)

#plt.imshow(img)
#plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)


# Tomar cuidado quando se está trabalhando com multiplas bibliotecas, pois cada uma trabalha com um padrão diferente
# Por exemplo, o padrão do OpenCV é BGR e da Matplotlib é RGB

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV -> BGR', hsv_bgr)



plt.imshow(rgb)
plt.show()

cv.waitKey(0)