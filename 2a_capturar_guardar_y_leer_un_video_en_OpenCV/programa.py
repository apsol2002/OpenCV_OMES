import cv2

captura = cv2.VideoCapture(0)
salida = cv2.VideoWriter('elArchivo.avi', cv2.VideoWriter_fourcc(*'XVID'), 20,(640,480))
'''
en caso de querer grabar el video... a probarlo en una pc  que le ande la camara...  X/

salida = ca

'''

while (captura.isOpened()):
        ret, imagen = captura.read()
        if ret is True:
             cv2.imshow('Captura', imagen)
             
             salida.write(imagen)

             if cv2.waitKey(1) & 0xff == ord('s'):
                break

captura.relase()
cv2.destroyAllWindows