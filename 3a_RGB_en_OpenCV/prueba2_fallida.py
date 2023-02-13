import cv2
import numpy as np


def main():
        
        # RGB -> BGR

        bgr = cv2.imread('foto_rgb.jpg')

        print(bgr.shape)

        c1 = bgr[:,:,0]
        c2 = bgr[:,:,1]       
        c3 = bgr[:,:,2]

        foto = np.asarray([c1,c2,c3], dtype=np.int8)
        #foto = np.array([c1,c2,c3]).reshape(374, 394, 3)

        print(foto.shape)

        '''
        foto = np.concatenate(c1, axis=0, dtype=np.uint8)
        foto = np.concatenate(c2, axis=0, dtype=np.uint8)
        foto = np.concatenate(c3, axis=0, dtype=np.uint8)
        '''
        #cv2.imshow('RGB', np.hstack([c1,c2,c3]))
       
        cv2.imshow('FOTO ', foto)

        print(type(bgr))
        print(type(foto))

        '''
        bgr[:,:,:] = [255,255,255] # blanco
        bgr[:,:,:] = [0,0,0] # negro
        bgr[:,:,:] = [255,0,0]
        '''        
        
        #print(bgr)

        '''
        cv2.imshow('RGB', bgr)
        cv2.imshow('c1', c1)
        cv2.imshow('c2', c2)
        cv2.imshow('c3', c3)
        '''

        cv2.waitKey(0)

        cv2.destroyAllWindows()

if __name__ == '__main__':
        main()