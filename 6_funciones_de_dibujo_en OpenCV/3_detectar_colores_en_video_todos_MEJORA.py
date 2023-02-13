from time import sleep
import cv2
from cv2 import FONT_HERSHEY_SIMPLEX 
import numpy as np
import imutils


# arreglos umbral AZUL y  mascara
azulBajo1 = np.array([100,100,20],dtype=np.uint8)
azulAlto1 = np.array([125,255,255],dtype=np.uint8)

# arreglos umbral ROJA y  mascara
redBajo1 = np.array([0,180,100],dtype=np.uint8)
redAlto1 = np.array([8,255,255],dtype=np.uint8)
redBajo2 = np.array([175,180,100],dtype=np.uint8)
redAlto2 = np.array([179,255,255],dtype=np.uint8)


def dibujar_mascara(imagen,mascara,color):
        # buscar contornos.
        contornos,_ = cv2.findContours(mascara,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        print(f'Contornos: {len(contornos)}', end= ' ')
        for c in contornos:

                area = cv2.contourArea(c)

                print(f' {area} ' , end= ' ')

                if area > 600:
                        # obtener coordenadas  de la forma detectada...
                        x,y,w,h = cv2.boundingRect(c)

                        if color == (255,0,0):

                                cv2.rectangle(imagen,(x,y),(x+w,y+h),color,3)
                                cv2.line(imagen,(x,y),(x+w,y+h),color,5)

                                font = cv2.FONT_HERSHEY_SIMPLEX
                                cv2.putText(imagen, '{},{}'.format(x,y),(x+10,y),font,0.75,(0,255,0),1,cv2.LINE_AA)

                        if color == (0,0,255):
                                # punto central y coordenadas del punto
                                M = cv2.moments(c)
                                if (M['m00'] == 0): M['m00'] = 1
                                x_centro  =  int( M['m10'] / M['m00'])
                                y_centro  =  int( M['m01'] / M['m00'])
                                radio = x_centro - x 
                                cv2.circle(imagen, (x_centro,y_centro), radio , (0,255,0),3)

                                font = cv2.FONT_HERSHEY_SIMPLEX
                                cv2.putText(imagen, '{},{}'.format(x,y),(x+10,y),font,0.75,(0,255,0),1,cv2.LINE_AA)

                                # suavizar el contorno .... para que no sea irregular
                                #contorno_suavizado_azul = cv2.convexHull(c)
                                
                                #cv2.drawContours(imagen, [contorno_suavizado_azul],0,color,3)

        

captura = cv2.VideoCapture('elVideo2.mp4')

while (captura.isOpened()):
        ret, imagen = captura.read()
        if ret is True:
                imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

                mascara_azul = cv2.inRange(imagenHSV,azulBajo1,azulAlto1)
                
                mascara_roja1 = cv2.inRange(imagenHSV,redBajo1,redAlto1)
                mascara_roja2 = cv2.inRange(imagenHSV,redBajo2,redAlto2)
                mascara_ROJA = cv2.add(mascara_roja1,mascara_roja2)

                

                           
                dibujar_mascara(imagen,mascara_azul,(255,0,0))
                dibujar_mascara(imagen, mascara_ROJA,(0,0,255))

                cv2.imshow('Video ORIGINAL', imagen)
                #cv2.imshow('Mask AZUL', filtro_azul)
                if cv2.waitKey(20) & 0xff == ord('s'):
                        break

captura.relase()
cv2.destroyAllWindows


