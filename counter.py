import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import morphology

def types(i):
    strg = ''
    for n in i[::2]:
        strg += str(n[::2])
        strg += '\n'
    return strg

image = np.load("ps.npy.txt")
counter = 0
masks = np.array([[[1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]],
                
                [[1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [1, 1, 1, 1],
                [1, 1, 1, 1]],
                
                [[1, 1, 1, 1],
                [1, 1, 1, 1],
                [0, 0, 1, 1],
                [0, 0, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]],
                
                [[1, 1, 0, 0, 1, 1],
                [1, 1, 0, 0, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]],
                
                [[1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 0, 0, 1, 1],
                [1, 1, 0, 0, 1, 1]],
                
                [[1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]]], dtype=object)


for j in masks:
    res = np.sum(morphology.binary_hit_or_miss(image, j))
    print('Тип объекта: \n', types(j), 'Его количество: ', res, sep = '', end = '\n\n')
    counter += res
print('Всего объектов:', counter)

plt.imshow(image)
plt.show()
