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

        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)  

        c1 = rgb[:,:,0]
        c2 = rgb[:,:,1]       
        c3 = rgb[:,:,2]


        cv2.imshow('RGB', np.hstack([c1,c2,c3]))


        print(type(bgr))
        cv2.waitKey(0)

        cv2.destroyAllWindows()

if __name__ == '__main__':
        main()