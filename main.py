import cv2

import funcions
import funcions as fc

file_name = "C:/Users/ghwt0504/Desktop/ryan.jpg"
ryan_pic = cv2.imread(file_name, cv2.IMREAD_COLOR)
h, w, c = ryan_pic.shape
ryan_img = []

if ryan_pic is not None:
    cv2.imshow("ryan", ryan_pic)
    if cv2.waitKey(0) == ord('c'):
        for i in range(1,3+1,1):
            x = 40 * i
            ryan_img.append(funcions.slice(ryan_pic,x,50))
            ryan_img[i-1] = fc.binary_img(ryan_img[i-1])
        for i in range(1,3+1,1):
            path = str(i)
            cv2.namedWindow(path)
            cv2.imshow(path,ryan_img[i-1])
            cv2.resizeWindow(path, width=200, height=200)
            cv2.moveWindow(path, x=200*i, y=150)
        cv2.waitKey(0)
cv2.destroyAllWindows()