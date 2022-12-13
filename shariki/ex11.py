import cv2
import numpy as np
from random import shuffle
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
# cam.set(cv2.CAP_PROP_EXPOSURE, -3)
# cam.set(cv2.CAP_PROP_AUTO_WB, 0)

#blue
lower_blue = np.array([90, 120, 90])
upper_blue = np.array([130, 190, 190])

#green
lower_green = np.array([50, 20, 120])
upper_green = np.array([90, 120, 255])

#red
lower_red = np.array([170, 100, 90])
upper_red = np.array([255, 255, 255])

lowers = [(lower_green), (lower_red), (lower_blue)]
uppers = [(upper_green), (upper_red), (upper_blue)]

def mask_for_ball(lower, upper):
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    return mask

colors_seq = ["R", "G", "B"]
shuffle(colors_seq)

def take_contours(contrs, image, coloring):
    if len(contrs) > 0:
        c = max(contrs, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        if radius > 20:
            cv2.circle(image, (int(x), int(y)),int(radius), coloring, 2)
        return int(x)
    return 0

while cam.isOpened():
    _, frame = cam.read()
    cv2.putText(frame, str(colors_seq), (60,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255),4)
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_green = mask_for_ball(lowers[0], uppers[0])
    mask_red = mask_for_ball(lowers[1], uppers[1])
    mask_blue = mask_for_ball(lowers[2], uppers[2])

    masks = mask_blue + mask_green + mask_red

    contours_blue, _ = cv2.findContours(mask_blue.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
    contours_red, _ = cv2.findContours(mask_red.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)

    x = [take_contours(contours_blue, frame, (255,0,0)), take_contours(contours_green, frame, (0,255,0)), take_contours(contours_red, frame, (0, 0, 255))]

    clrs = {"R": x[2], "G": x[1], "B": x[0]}
    current_colors = sorted(clrs, key=clrs.get)
    
    if current_colors == colors_seq:
        cv2.putText(frame, "You win!", (120,400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255),4)


    cv2.imshow("Image", frame)
    cv2.imshow("Mask", masks)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break
 
cv2.destroyAllWindows()
