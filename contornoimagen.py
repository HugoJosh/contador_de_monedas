from cv2 import cv2
import os
#docs opencv
os.getcwd()
img=cv2.imread('c:/Users/5470/Downloads/python/monedas/img/cont.jpg')
grises=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#aplic2a el umbral simple
_,umbral=cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
cv2.destroyAllWindows()
#(UMBRAL,MODE.METHOD)
#IMAGEN UMBRAL EN BYN
#modo de recuperacion de contorno
#metodo APROX_NONE TODOS LOS PUNTOS APROX_SIMPLE VERTICES
contorno,jerarquia=cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE);
#DRAW CONTORNS, INDICE INDICA CUALES CONTORNOS DIBUJAR
#img,contornos,id,colores,grosor
cv2.drawContours(img,contorno,-1,(255,73,46),3)
cv2.imshow('contorno',img)
cv2.waitKey(0)


