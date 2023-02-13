import cv2

foto1 = cv2.imread('foto1.jpg',1)
foto2 = cv2.imread('foto2.jpg',1)


foto_suma = cv2.add(foto1,foto2)

cv2.imshow('foto', foto_suma)

print('SUMA max 255 por mas de exceder ese valor la suma')
print(foto1[0:3,0:3])
print(foto2[0:3,0:3])
print(foto_suma[0:3,0:3])



cv2.waitKey(0)
cv2.destroyAllWindows