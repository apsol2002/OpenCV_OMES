import cv2 
import numpy as np
import imutils

img1 = cv2.imread('foto2.jpg')

mask = np.zeros((192,315),dtype=np.uint8)
mask = cv2.circle(mask, (150,100),50,(255),-1)
mask_not = cv2.bitwise_not(mask)


cv2.imshow('IMG 1', img1)

img_and = cv2.bitwise_and(img1,img1,mask=mask)
cv2.imshow('IMG AND', img_and)

img_not = cv2.bitwise_and(img1,img1,mask=mask_not)
cv2.imshow('IMG NOT', img_not)



cv2.waitKey(0)
cv2.destroyAllWindows