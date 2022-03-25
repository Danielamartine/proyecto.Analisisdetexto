import cv2
import numpy as np
from  PIL import ImageGrab


def capture(left, top, right, bottom):
    img = ImageGrab.grab(bbox=(left, top, right, bottom))
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    r, g, b = cv2.split(img)
    cv2.merge([b, g, r], img)
    return img


cv2.imshow("screen", capture(0, 0, 600, 400))
cv2.waitKey(0)
