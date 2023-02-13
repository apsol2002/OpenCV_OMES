import cv2 
import numpy as np
import imutils

imagenBGR = cv2.imread('arcoiris.jpg')
imagenHSV = cv2.cvtColor(imagenBGR, cv2.COLOR_BGR2HSV)

# arreglos donde se encuentra el rojo en el umbral--
redBajo1 = np.array([0,100,20],dtype=np.uint8)
redAlto1 = np.array([8,255,255],dtype=np.uint8)

redBajo2 = np.array([175,100,20],dtype=np.uint8)
redAlto2 = np.array([179,255,255],dtype=np.uint8)

# Creando las máscaras ....
maskRed1 = cv2.inRange(imagenHSV,redBajo1,redAlto1)
maskRed2 = cv2.inRange(imagenHSV,redBajo2,redAlto2)

maskRED = cv2.add(maskRed1,maskRed2)

maskRED_REAL = cv2.bitwise_and(imagenBGR,imagenBGR,mask=maskRED)

# ver resultados
cv2.imshow('ORIGINAL', imagenBGR)
cv2.imshow('HSV', imagenHSV)
cv2.imshow('SOLO MASCARA', maskRED)
cv2.imshow('SOLO MASCARA COLOREADA', maskRED_REAL)

cv2.waitKey(0)
cv2.destroyAllWindows