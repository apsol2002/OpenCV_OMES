import cv2 
import numpy as np
import imutils

image = cv2.imread('dados.jpg',0)

image = imutils.resize(image,width=200)
# image = cv2.resize(image,[200,160]) # forma 2

_, binarizada = cv2.threshold(image,160, 250, cv2.THRESH_BINARY)  

_, binarizada_inv = cv2.threshold(image,160, 250, cv2.THRESH_BINARY_INV)  

_, truncada = cv2.threshold(image,170, 255, cv2.THRESH_TRUNC)  

_, to_zero = cv2.threshold(image,170, 255, cv2.THRESH_TOZERO)  
_, to_zero_invert = cv2.threshold(image,170, 255, cv2.THRESH_TOZERO_INV)  


cv2.imshow('GRISES', image)
cv2.imshow('BINARIZADA', binarizada)
cv2.imshow('BINARIZADA INVERTIDA', binarizada_inv)

cv2.imshow('TUNCADA ', truncada)

cv2.imshow('TO ZERO ', to_zero)
cv2.imshow('TO ZERO INVERT ', to_zero_invert)

cv2.waitKey(0)
cv2.destroyAllWindows