import cv2

def binary_img(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img[img < 110] = 0
    img[img >= 110] = 255

    return img

def slice(original):
    x = 37;
    y = 62;
    w = 12;
    h = 17
    img = []
    roi = []

    for i in range(0,4+1):
        roi.append(original[y:y+h, x:x+w])
        img.append(roi[i].copy())
        rec = cv2.rectangle(original[i], (0, 0), (w - 1, h - 1), (255, 0, 0))
        x = x + 11
    return img, rec
