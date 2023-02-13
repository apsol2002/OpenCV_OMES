import cv2 
import numpy as np

img1 = np.zeros((400,600),dtype=np.uint8)
img1[100:300,200:400]=255

img2 = np.zeros((400,600),dtype=np.uint8)
img2 = cv2.circle(img2, (300,200),125,(255),-1)

cv2.imshow('IMG 1', img1)
cv2.imshow('IMG 2', img2)

img_and = cv2.bitwise_and(img1,img2)
cv2.imshow('IMG AND', img_and)

img_and = cv2.bitwise_or(img1,img2)
cv2.imshow('IMG OR', img_and)

img_and = cv2.bitwise_not(img1)
cv2.imshow('IMG NOT', img_and)

img_and = cv2.bitwise_xor(img1,img2)
cv2.imshow('IMG XOR', img_and)

cv2.waitKey(0)
cv2.destroyAllWindows