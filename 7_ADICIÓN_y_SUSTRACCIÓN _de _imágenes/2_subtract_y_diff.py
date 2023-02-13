import cv2

foto1 = cv2.imread('foto1.jpg',1)
foto2 = cv2.imread('foto2.jpg',1)


foto_suma = cv2.subtract(foto1,foto2)

foto_dif = cv2.absdiff(foto1,foto2)

cv2.imshow('RESTA', foto_suma)

cv2.imshow('diferencia', foto_dif)

print('resta min 0 por mas de exceder ese valor la suma')
print(foto1[0:3,0:3])
print(foto2[0:3,0:3])
print(foto_suma[0:3,0:3])



cv2.waitKey(0)
cv2.destroyAllWindows