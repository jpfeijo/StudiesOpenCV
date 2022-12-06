import cv2 as cv

img = cv.imread('Cats/Cat1.jfif') #carrega a imagem

cv.imshow('Cat1.jfif', img)#mostra a imagem

#Reading videos
capture = cv.VideoCapture('Dogs/dog.mp4')#pode passar um número ou o diretório do arquivo -> neste caso 0 é a webcam

while True:
    isTrue, frame = capture.read()#isTrue é um booleano que diz se o frame foi lido corretamente, frame é o frame lido -> read() le o video frame a frame

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #se a letra d for pressionada, sai do loop e para o video
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)#espera o usuario apertar uma tecla, neste caso espera infinito




