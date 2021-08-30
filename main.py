# -해야할 것-
# 코드 함수화(모듈화) -> main에 최대한 코드 줄이기
# 라벨링을 통해서 검출해낸다음에 해당 영역을 30으로 나누기

# --지금 할것--
# 연주 해보기

import cv2
import numpy as np
import functions as fs

path = "C:/DevSpace/capstone2/images/"  # 파일 경로
image_name = "music_test.jpg"       # 이미지 파일 이름

music_pic = cv2.imread(path + image_name)
music_pic = cv2.resize(music_pic,dsize=(400,400),interpolation=cv2.INTER_CUBIC)
music_pic = fs.binary_img(music_pic)

h, w, c = music_pic.shape
cnt = 0

fs.music_play()

if music_pic is not None:
    cv2.imshow("music", music_pic)
    if cv2.waitKey(0) == ord('c'):
        img,rec = fs.slice(music_pic)

for i in img:

    cv2.imshow("piece"+ str(cnt),i)
    print(cnt , i.mean())
    cv2.moveWindow("piece" + str(cnt) ,30 * cnt ,400)
    cnt = cnt + 1

cv2.imshow("marking",rec)
cv2.waitKey(0)

cv2.destroyAllWindows()
