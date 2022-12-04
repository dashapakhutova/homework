import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.measure import label, regionprops

image = plt.imread("balls_and_rects.png")
hsv = color.rgb2hsv(image)
binary = hsv[:, :, 0].copy()
binary[binary > 0] = 1
labeled = label(binary)
regions = regionprops(labeled)

rects = []
balls = []
counter_rect = 0
counter_ball = 0

for reg in regions:
    cy, cx = reg.centroid
    if reg.area == (reg.image.shape[0] * reg.image.shape[1]):
        rect = rects.append(hsv[int(cy), int(cx), 0])
        counter_rect += 1
    else:
        bals = balls.append(hsv[int(cy), int(cx), 0])
        counter_ball += 1

groups_rects = [[rects[0]],]
delta = np.max(np.diff(rects)) / 2
for i in range(1, len(rects)):
    previous_rect = rects[i-1]
    current_rect = rects[i]
    if current_rect - previous_rect > delta:
        groups_rects.append([])
    groups_rects[-1].append(current_rect)

groups_balls = [[balls[0]],]
delta = np.max(np.diff(balls)) / 2
for i in range(1, len(balls)):
    previous_balls = balls[i-1]
    current_balls = balls[i]
    if current_balls - previous_balls > delta:
        groups_balls.append([])
    groups_balls[-1].append(current_balls)

result_colors_rect = []
result_count_rect = []
result_colors_balls = []
result_count_balls = []

print("Все фигуры:", len(regions))

for grp in groups_rects:
    result_colors_rect.append(np.mean(grp))
    result_count_rect.append(len(grp))
print("Квадраты: ")
print(counter_rect)
print(result_colors_rect)
print(result_count_rect)

print("\n")

for grp in groups_balls:
    result_colors_balls.append(np.mean(grp))
    result_count_balls.append(len(grp))
print("Круги: ")
print(counter_ball)
print(result_colors_balls)
print(result_count_balls)