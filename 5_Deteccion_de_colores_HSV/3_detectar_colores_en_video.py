import cv2
from cv2 import FONT_HERSHEY_SIMPLEX 
import numpy as np
import imutils

# arreglos umbral AZUL y  mascara
azulBajo1 = np.array([100,100,20],dtype=np.uint8)
azulAlto1 = np.array([125,255,255],dtype=np.uint8)


captura = cv2.VideoCapture('elVideo2.mp4')

while (captura.isOpened()):
        ret, imagen = captura.read()
        if ret is True:

                imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

                mascara_azul = cv2.inRange(imagenHSV,azulBajo1,azulAlto1)
                filtro_azul = cv2.bitwise_and(imagen,imagen,mask=mascara_azul)
                
                # buscar contornos.
                contornos,_ = cv2.findContours(mascara_azul,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                print(f'Contornos: {len(contornos)}', end= ' ')
                for c in contornos:

                        area = cv2.contourArea(c)

                        print(f' {area} ' , end= ' ')

                        if area > 600:

                                # punto central y coordenadas del punto
                                M = cv2.moments(c)
                                if (M['m00'] is 0): M['m00'] = 1
                                x  =  int( M['m10'] / M['m00'])
                                y  =  int( M['m01'] / M['m00'])

                                cv2.circle(imagen, (x,y), 7 , (0,255,0),-1)

                                font = cv2.FONT_HERSHEY_SIMPLEX
                                cv2.putText(imagen, '{},{}'.format(x,y),(x+10,y),font,0.75,(0,255,0),1,cv2.LINE_AA)



                                # suavizar el contorno .... para que no sea irregular
                                contorno_suavizado = cv2.convexHull(c)
                                
                                cv2.drawContours(imagen, [contorno_suavizado],0,(255,0,0),3)

                print()
                cv2.imshow('Video ORIGINAL', imagen)
                #cv2.imshow('Mask AZUL', filtro_azul)
                if cv2.waitKey(40) & 0xff == ord('s'):
                        break

captura.relase()
cv2.destroyAllWindows
