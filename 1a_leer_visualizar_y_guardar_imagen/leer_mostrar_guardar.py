import cv2


imagen = cv2.imread("C:\\Users\\Carlos\\Documents\\Python_y_OpenCV\\1_OMES\\1a_leer_visualizar_y_guardar_imagen\\huevos.jpg", 1)

cv2.imshow('Titulo a mostrar', imagen)

cv2.waitKey()

cv2.destroyAllWindows