import cv2

def binary_img(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img[img < 110] = 0
    img[img >= 110] = 255

    return img

def slice(original):
    x = 37
    y = 62
    w = 12
    h = 17
    img = []
    roi = []
    original_copy = original.copy()

    for i in range(0,30+1):
        roi.append(original[y:y+h, x:x+w])
        img.append(roi[i].copy())
        rec = cv2.rectangle(original_copy, (x, y), (x+w, y+h), (255, 0, 0))
        x = x + 11

    return img, rec
