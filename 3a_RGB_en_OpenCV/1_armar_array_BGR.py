import cv2
import numpy as np


def main():
        
        # RGB -> BGR

        bgr = np.zeros((200,400,3), dtype=np.uint8)

        bgr[:,:,:] = [0,0,255] # negro
        
        '''
        bgr[:,:,:] = [255,255,255] # blanco
        bgr[:,:,:] = [0,0,0] # negro
        bgr[:,:,:] = [255,0,0]
        '''        
        
        cv2.imshow('RGB', bgr)

        cv2.waitKey(0)

        cv2.destroyAllWindows()

if __name__ == '__main__':
        main()


