# -해야할 것-
# 코드 함수화(모듈화) -> main에 최대한 코드 줄이기
# 라벨링을 통해서 검출해낸다음에 해당 영역을 30으로 나누기

# --지금 할것--
# 연주 해보기

import cv2
import numpy as np
import switch as switch
from multiprocessing import Process
from time import sleep
import pyglet

import functions as fs
# import playNotes as pn
import playThread as pT

path = "C:/DevSpace/capstone2/images/"  # 파일 경로
image_name = "music_test.jpg"       # 이미지 파일 이름

note_list = []  # 30노트중 해당 음이 있는자리가 몇번째인지 확인하기 위한 리스트, 자료형은 int
play_notes = [] # 음을 다중 실행 하기 위한 쓰레드를 저장하기 위한 리스트.

CUTLINE = 4 # 이미지에서 몇줄을 끊을건지

music_pic = cv2.imread(path + image_name)
music_pic = cv2.resize(music_pic,dsize=(420,400),interpolation=cv2.INTER_CUBIC)
music_pic = fs.makeBinaryImg(music_pic)

cnt = 0 #

img_list = []

# 'c'를 입력하면 화면을 자름
if music_pic is not None:
    cv2.imshow("music", music_pic)
    if cv2.waitKey(0) == ord('c'):
        img_list, rec = fs.sliceImg(music_pic,CUTLINE)

print(len(img_list))


img = fs.calAvg(img_list)
print(img)
img = fs.findNote(img)
print(img)

finalPosition = fs.checkPosition(img,CUTLINE)
print("Final position: ", finalPosition)

pT.playMusic(finalPosition)

cv2.waitKey()
cv2.destroyAllWindows()
