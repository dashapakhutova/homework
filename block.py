import numpy as np
import matplotlib.pyplot as plt

from scipy.misc import face
image = face(True)

def block_mean(image,by_size=8,bx_size=8):
    result = image.copy()
    for y in range(int(image.shape[0]/ by_size)):
        for x in range (int(image.shape[1]/ bx_size)):
            sub = result[y*by_size:by_size*(y+1),x*bx_size:bx_size*(x+1)]
            sub[:] = sub.mean()
    return result
    

plt.subplot(121)
plt.imshow(image, cmap="gray")
plt.subplot(122)
result = block_mean(image,16,16)
plt.imshow(result, cmap="gray")
plt.show()