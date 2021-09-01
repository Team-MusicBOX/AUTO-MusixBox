# -해야할 것-
# 코드 함수화(모듈화) -> main에 최대한 코드 줄이기
# 라벨링을 통해서 검출해낸다음에 해당 영역을 30으로 나누기

# --지금 할것--
# 연주 해보기

import cv2
import numpy as np
import functions as fs
from multiprocessing import Process

path = "C:/DevSpace/capstone2/images/"  # 파일 경로
image_name = "music_test.jpg"       # 이미지 파일 이름

note_list = []  # 30노트중 해당 음이 있는자리가 몇번째인지 확인하기 위한 리스트, 자료형은 int
play_notes = [] # 음을 다중 실행 하기 위한 쓰레드를 저장하기 위한 리스트.

music_pic = cv2.imread(path + image_name)
music_pic = cv2.resize(music_pic,dsize=(400,600),interpolation=cv2.INTER_CUBIC)
music_pic = fs.binaryImg(music_pic)

h, w, c = music_pic.shape
cnt = 0

# 'c'를 입력하면 화면을 자름
if music_pic is not None:
    cv2.imshow("music", music_pic)
    if cv2.waitKey(0) == ord('c'):
        img,rec = fs.slice(music_pic)


# 자른 이미지 출력
for i in img:
    if i.mean() > 95:
        note_list.append(cnt)
    # cv2.imshow("piece"+ str(cnt),i)
    print(cnt , i.mean())
    # cv2.moveWindow("piece" + str(cnt) ,30 * cnt ,400)
    cnt = cnt + 1

for i in range(len(note_list)):
    play_notes.append(Process(target=fs.playMusic(note_list[i])))


for i in range(len(note_list)):
    play_notes[i].start



cv2.imshow("marking",rec)
cv2.waitKey(0)

cv2.destroyAllWindows()
