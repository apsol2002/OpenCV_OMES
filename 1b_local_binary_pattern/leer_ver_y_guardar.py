import cv2
from matplotlib import pyplot as plt
from skimage import feature

# vars
radio = 1
puntos = 1

imagenes = []

# Cargar la imagen...
imagen_parque = cv2.imread('parque.jpg', 0)

for r in range(radio, radio+10, 2):
    for p in range(puntos, puntos+10, 2):
        imagen_lbg = feature.local_binary_pattern(imagen_parque, p, r, method="uniform")
        imagenes.append([imagen_lbg, p, r])

print(len(imagenes))


for i in imagenes:
    cv2.imshow(f'Prueba LBP Puntos: {i[1]}  y radio: {i[2]} ', i[0])
    nombre = f'LBP_p{i[1]}_r{i[2]}.jpg'
    cv2.imwrite(nombre, i[0])


cv2.waitKey(0)
cv2.destroyAllWindows()






