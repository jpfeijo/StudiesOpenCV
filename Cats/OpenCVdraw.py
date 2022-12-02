import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # cria uma imagem preta de 500x500 pixels
cv.imshow('Blank', blank)

img = cv.imread('Dogs/dog2.jfif')
cv.imshow('Dog', img)

# Pintar a imagem de alguma determinada cor
#blank[:] = 0,255,0 # pinta a imagem de verde
#cv.imshow('Green', blank) 

#blank[200:300, 300:400] = 0,255,0 # pinta uma determinada parte da imagem de verde
#cv.imshow('Green', blank) 

# Desenhar um retangulo
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), thickness=cv.FILLED) # desenha um retangulo azul na imagem // cv.FILLED ou -1 pra preencher
cv.imshow('Rectangle', blank) 

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1) # desenha um circulo vermelho na imagem
cv.imshow('Rectangle', blank)

# Desenhar uma linha
cv.line(blank, (100, 250), (300, 400), (255,255,255), thickness=8) # desenha uma linha branca na imagem
cv.imshow('Line', blank)

# Escrever textto na imagem
cv.putText(blank, 'Hello World', (225,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) # Escreve Hello World na imagem
cv.imshow('Text', blank)

cv.waitKey(0)