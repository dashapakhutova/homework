import numpy as np
import pyautogui
import mss
import cv2
from time import sleep, time


def grab(bbox):
    img = np.array(sct.grab(bbox))
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    cv2.imshow('image', gray)

    cactus = gray[-1,:]
    bird = gray[1,:]

    cactus_val = np.sum(cactus)
    bird_val = np.sum(bird)
    return cactus_val, bird_val

def key_push(time):
    pyautogui.keyDown('up')
    sleep(time)
    pyautogui.press('down')


with mss.mss() as sct:
    bbox = {"top": 345, "left": 225, "width": 85, "height": 40}
    total_time = 0
    flag = 1
    val = 20995
    
    while True:
        cur_time = time()
        cactus_val, bird_val = grab(bbox)
        if cactus_val < val:
            print(cactus_val)
            if total_time >= 20.0:
                key_push(0.08)
            else:
                pyautogui.keyDown('up')

        if bird_val < val:
            flag = 1
            pyautogui.keyDown('down')
            sleep(0.25)

        if bird_val == val and flag == 1:
            flag = 0
            pyautogui.keyUp('down')

        
        total_time += time() - cur_time
        
        if cv2.waitKey(25) == ord("q"):
            cv2.destroyAllWindows()
            break
