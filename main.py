import cv2

import funcions
import funcions as fc

file_name = "C:/Users/ghwt0504/Desktop/music.jpg"

music_pic = cv2.imread(file_name, cv2.IMREAD_COLOR)
music_pic = cv2.resize(music_pic,dsize=(400,400),interpolation=cv2.INTER_CUBIC)
h, w, c = music_pic.shape
ryan_img = []
ain = 0
if music_pic is not None:
    cv2.imshow("music", music_pic)
    if cv2.waitKey(0) == ord('c'):
        img,rec = funcions.slice(music_pic)

for i in img:

    cv2.imshow("hdgg"+ str(ain),i)
    cv2.moveWindow("hdgg" + str(ain),100 * ain ,400)

    ain = ain + 1
cv2.imshow("god ",rec)
cv2.waitKey(0)

cv2.destroyAllWindows()