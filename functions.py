import cv2
import numpy as np

import winsound # 윈도우에서만 돌아감 수정필수

#이진화 함수
def binary_img(img):
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img[img < 110] = 0
    # img[img >= 110] = 255

    _, b_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

    return b_img

def slice(original):
    x = 37
    y = 62
    w = 12
    h = 17
    img = []
    roi = []

    for i in range(0,30+1):
        roi.append(original[y:y+h, x:x+w])
        img.append(roi[i].copy())
        rec = cv2.rectangle(original, (x, y), (x+w, y+h), (255, 0, 0))
        x = x + 11

    return img, rec

def music_play():
    duration =  1000 # milliseconds
    notes = [262 ,294, 330, 349, 392, 440, 494, 523, 587]
    freq = 65
    for i in notes:
        winsound.Beep(i,duration)
