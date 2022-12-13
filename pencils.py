import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops

def proportion(width, height):
    return max(width, height) / min(width, height)

def filling(reg):
    return reg.area / (reg.image.shape[0] * reg.image.shape[1])

minimal_area = 20000
count_of_pencil = 0

for i in range(1, 13):
    image = plt.imread(f"img ({i}).jpg")
    gray = rgb2gray(image)
    th = threshold_otsu(gray)
    binary = (gray < th).astype("int")
    labeled = label(binary)
    regions = regionprops(labeled)
    another_regions = []
    
    for reg in regions:
        if reg.area < minimal_area:
            labeled[np.where(labeled == reg.label)] = 0
        else:
            another_regions.append(reg)

    pencil_on_image = 0


    for region in another_regions:
        width = region.image.shape[1]
        height = region.image.shape[0]
        prptn = proportion(width, height)
        if prptn > 10 and min(width, height) > 100:
            pencil_on_image += 1
            count_of_pencil += 1
        elif filling(region) < 0.23 and max(width, height) > 1800:
            pencil_on_image += 1
            count_of_pencil += 1
    
    print(f"Количество карандашей на img ({i}).jpg: {pencil_on_image}")

print(f"Всего карандашей: {count_of_pencil}")
