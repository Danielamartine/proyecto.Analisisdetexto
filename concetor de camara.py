
from cv2 import *
namedWindow("camara") 

vc=VideoCapture(0)

while True:
    next , Frame=vc.read()
    imshow("camara",Frame)
    if waitKey(50)>=0:
        break

