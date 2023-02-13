from tkinter import font
import cv2
from cv2 import FONT_HERSHEY_SIMPLEX
import numpy as np

imagen = 255*np.ones((200,400,3), dtype=np.uint8)


''' LINEA 
cv2.line(1,2,3,4,5)
       image,(punto inicial X,Y),(punto final X,Y),(color linea BGR), grosor
       Numpy construlle la matriz Filas x columnas y cv2 usa X Y  
'''
cv2.line(imagen,(0,0),(400,200),(0,0,0),5)

''' RECTANGULO  
cv2.rectangle(1,2,3,4,5)
       image,(punto inicial X,Y),(punto final X,Y),(color linea BGR), grosor
       Numpy construlle la matriz Filas x columnas y cv2 usa X Y  
'''
cv2.rectangle(imagen,(100,50),(200,100),(255,0,255),5)

''' CURCULO  
cv2.rectangle(1,2,3,4,5)
       image,(centro X,Y), radio ,(color linea BGR), grosor
       Numpy construlle la matriz Filas x columnas y cv2 usa X Y  
'''
cv2.circle(imagen,(300,100),50,(0,255,0),3)

cv2.circle(imagen,(100,100),50,(0,255,0),-1)

''' TEXTO   
cv2.puttext(1.2.3.4.5.6.7)
       imagen
       texto a visualizar
       coordenadas de ubicacion 
       tipo fuente
       tamaño de la fuente
       color(BGR)
       GROSOR
       tipo de linea.    
'''
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,'HOLA MUNDO!',(150,25),font,0.6,(0,0,0),1,cv2.LINE_AA)

cv2.imshow('IMAGEN', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows