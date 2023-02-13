import cv2

captura = cv2.VideoCapture('elVideo.mp4')

while (captura.isOpened()):
        ret, imagen = captura.read()
        if ret is True:
             cv2.imshow('Captura', imagen)

             if cv2.waitKey(60) & 0xff == ord('s'):
                break

captura.relase()
cv2.destroyAllWindows