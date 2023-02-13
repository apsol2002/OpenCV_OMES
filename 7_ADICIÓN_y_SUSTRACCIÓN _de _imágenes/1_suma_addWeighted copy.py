import cv2

foto1 = cv2.imread('foto1.jpg')
foto2 = cv2.imread('foto2.jpg')


foto_sumaW = cv2.addWeighted(foto1,0.7,foto2,0.3,0)

cv2.imshow('foto', foto_sumaW)


print('SUMA max 255 por mas de exceder ese valor la suma')
print(foto1[0:3,0:3])
print(foto2[0:3,0:3])
print(foto_sumaW[0:3,0:3])



cv2.waitKey(0)
cv2.destroyAllWindows