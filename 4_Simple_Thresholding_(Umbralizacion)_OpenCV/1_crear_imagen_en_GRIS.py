import cv2 
import numpy as np



# Creamos la matriz de ceros
grises = np.zeros((400,600), dtype=np.uint8)
# grises = grises.astype(np.uint8)
# Se prepara el texto a mostrar ... 
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(grises, 'Umbral: T= 150',(100,70),font,1.5,(255),2,cv2.LINE_AA) 

# Agregar otros valores a la matriz 
grises[100:200,:200] = 130
grises[100:200,200:400] = 20
grises[100:200,400:] = 150

grises[200:400,:200] = 220
grises[200:400,200:400] = 60
grises[200:400,400:] = 190

_, binarizada = cv2.threshold(grises,160, 250, cv2.THRESH_BINARY)  


cv2.imshow('GRISES', grises)
cv2.imshow('BINARIZADA', binarizada)

cv2.waitKey(0)
cv2.destroyAllWindows