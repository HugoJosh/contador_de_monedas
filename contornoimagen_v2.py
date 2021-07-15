from cv2 import cv2
import numpy as np
original=cv2.imread(r'C:\Users\5470\Downloads\python\monedas\img\monedassoles.jpg')
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
#suavizado de imagenes, desenfocar
vargauss=7
valorkernel=15
gauss=cv2.GaussianBlur(gris,(vargauss,vargauss),0)
# canny eliminar el ruido
canny=cv2.Canny(gauss,60,100)
kernel=np.ones((valorkernel,valorkernel),np.uint8)

#elimina ruidos internos
# opening = cv2.morphologyEx(canny, cv2.MORPH_OPEN, kernel)
cierre=cv2.morphologyEx(canny, cv2.MORPH_CLOSE,kernel)


#identifica los contornos
contornos,jerarquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print("monedas encontradas: {}".format(len(contornos)))

#dibuja contornos
cv2.drawContours(original,contornos,-1,(255,73,46),3)
cv2.imshow("Imagen",original)
cv2.imshow("Imagen2",gauss)
cv2.imshow("Imagen3",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()