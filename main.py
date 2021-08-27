import cv2
import functions

file_name = "C:/Users/ghwt0504/Desktop/music.jpg"

music_pic = cv2.imread(file_name, cv2.IMREAD_COLOR)
music_pic = cv2.resize(music_pic,dsize=(400,400),interpolation=cv2.INTER_CUBIC)
h, w, c = music_pic.shape
ryan_img = []
ain = 0

if music_pic is not None:
    cv2.imshow("music", music_pic)
    if cv2.waitKey(0) == ord('c'):
        img,rec = functions.slice(music_pic)

for i in img:

    cv2.imshow("piece"+ str(ain),i)
    cv2.moveWindow("piece" + str(ain) ,30 * ain ,400)
    ain = ain + 1

cv2.imshow("marking",rec)
cv2.waitKey(0)

cv2.destroyAllWindows()