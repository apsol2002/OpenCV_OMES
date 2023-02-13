import cv2
import numpy as np


def main():
        
        # RGB -> BGR

        bgr = cv2.imread('foto_rgb.jpg')

        print(bgr.shape)

        c1 = bgr[:,:,0]
        c2 = bgr[:,:,1]       
        c3 = bgr[:,:,2]

        cv2.imshow('BGR', np.hstack([c1,c2,c3]))

        gris = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)  

        cv2.imshow('GRIS', gris)

        print(bgr.shape) 


        cv2.waitKey(0)

        cv2.destroyAllWindows()

if __name__ == '__main__':
        main()