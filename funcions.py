import cv2

def binary_img(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img[img < 110] = 0
    img[img >= 110] = 255

    return img

def slice(img,x,y):
    w = 150
    h = 150
    img = img[y:y+h,x:x+w]

    return img