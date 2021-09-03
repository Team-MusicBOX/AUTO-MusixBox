import cv2
import numpy as np
from multiprocessing import Process

# do re mi fa sol la si do

import winsound # 윈도우에서만 돌아감 수정필수

#이진화 함수
def makeBinaryImg(img):
    # b_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # b_img[b_img < 110] = 0
    # b_img[b_img >= 110] = 255

    _, b_img = cv2.threshold(img,110,255,cv2.THRESH_BINARY_INV)

    return b_img


def sliceImg(original, CUTLINE):
    x = 39
    y = 62
    w = 11
    h = 16
    img_list = []
    roi = []

    for j in range(0, CUTLINE):
        for i in range(0, 29 + 1):
            roi.append(original[y:y + h, x:x + w])
            img_list.append(roi[i].copy())
            rec = cv2.rectangle(original, (x, y), (x+w, y+h), (255, 0, 0))
            x = x + 12
        y = y + 17
        x = 39
        roi = []

    return img_list, rec

# def playMusic(note_num):
#     notes_index = []
#     duration =  1000 # milliseconds
#     notes = {'c': 65,'d': 73,'g': 98,'a': 110,'b': 123,'c1': 131,'d1': 147, 'e1': 165,'f1': 174,'f1_s':185,
#              'g1':196,'g1_s':207,'a1': 220,'a1_s':233, 'b1':247,'c2':261,'c2_s':277,'d2':293,'d2_s':311,'e2':329,
#              'f2':349,'f2_s':370, 'g2':392,'g2_s':415,'a2':440,'a2_s':466,'b2':494,'c3':523,'d3':587,'e3':659}
#
#     for i in notes.values():
#         notes_index.append(int(i))
#
#     winsound.Beep(notes_index[note_num]*2,duration)

def calAvg(list):             # 입력받은 이미지 리스트를 평균값으로
    avg_list = []
    for i in range(len(list)):
        avg_list.append(list[i].mean())
    return avg_list

def findNote(list):    # 입력받은 평균값 리스트를 이진화로
    for i in range(len(list)):
        if list[i] < 110:
            list[i] = 0
        else:
            list[i] = 1
    return list

def findFirstLine(list):
    if list[22] == 0 and list[25] == 0:  #뒷부분이 흰색이면 악보 들어옴
        return 1
    else:
        return 0

def checkPosition(img_list,CUTLINE):
    note_position = []
    for i in range(CUTLINE):
        cut_position = []
        for j in range(i*30, i*30+30):
            if img_list[j] == 1:
                cut_position.append(j%30)
        note_position.append(cut_position)

    return note_position
