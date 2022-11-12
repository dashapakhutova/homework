import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import binary_erosion
from scipy.ndimage import morphology

image = np.load("stars.npy")

counter = 0

masks = np.array([[[1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1]],
        
        [[0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]]])

labeled = label(image)
print(f"Objects = {np.max(labeled)}")

crosse = binary_erosion(image, masks[0])
labeled_crosse = label(crosse)
print(f"Crosse count = {labeled_crosse.max()}")

pluse = binary_erosion(image, masks[1])
labeled_pluse = label(pluse)
print(f"Pluse count = {labeled_pluse.max()}")

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(labeled)
plt.show()