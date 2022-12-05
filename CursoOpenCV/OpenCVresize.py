import cv2 as cv

#img = cv.imread('Cats/Cat1.jfif') #carrega a imagem
#cv.imshow('Cat1.jfif', img)#mostra a imagem

#Resizing and rescaling images and videos in openCV

def rescaleFrame(frame, scale=0.75):
    # Esse método funciona para imagens, videos e webcams 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Esse método funciona apenas para webcams
    capture.set(3,width)
    capture.set(4,height)

#Reading videos
capture = cv.VideoCapture('Dogs/dog.mp4')#pode passar um número ou o diretório do arquivo -> neste caso 0 é a webcam

while True:
    isTrue, frame = capture.read()#isTrue é um booleano que diz se o frame foi lido corretamente, frame é o frame lido -> read() le o video frame a frame

    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): #se a letra d for pressionada, sai do loop e para o video
        break

#cv.imshow('Frame Resized', rescaleFrame(img, scale=0.5))
capture.release()
cv.destroyAllWindows()
