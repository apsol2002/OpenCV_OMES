import numpy as np
from PIL import Image

array = np.zeros((3,50,50),dtype=np.int8)

print(array)

array[0,:,:] = 1

print(array)

im = Image.fromarray(array[0,:,:])
im.save('imSabe.jpeg')