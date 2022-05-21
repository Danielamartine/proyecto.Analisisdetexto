from ast import Break
import cv2
import numpy as np
from gtts import gTTS

#se crea el objeto del video 
captura = cv2.VideoCapture(0)
while True:
    #se captura de camara a camara
    (grabbed ,imagen ) = captura.read()
    if not grabbed:
        break

    cv2.imshow("video Droidcam client",imagen)
    tecla=cv2.waitKey(25) & 0xFF
    if tecla==27:
        break

captura.relase()
cv2.destroyAllWindows()
