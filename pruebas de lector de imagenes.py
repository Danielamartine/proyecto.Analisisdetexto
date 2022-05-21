
from email.mime import audio, image
from pickle import FRAME
from pydoc import doc
from sre_constants import GROUPREF_EXISTS
from tkinter import Frame
from traceback import FrameSummary
from unittest.mock import patch
import cv2
import numpy as np
import pytesseract
from gtts import gTTS
from playsound import playsound



#variables
cuadro=100
anchocam,altocam =640,480 

#captura de video 
cap=cv2.VideoCapture(0)
cap.set(3,ancho)#diferencia un ancho 
cap.set(4,alto)#diferencia un alto

#funcionesdevoz 
def text(image):
    def voz(archi_text,lenguaje,nom_archi):
        with open(archi_text,"r") as lec:
            lectura =lec.read()
        lect=gTTS(text=lectura,lang=lenguaje,slow=False)
        nombre= nom_archi
        lect.save(nombre)
    
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files(x86)\Tesseract-OCR'
image=cv2.imread("captura.jpg")
gris = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
texto=pytesseract.image_to_string(gris)
print(texto)
dire=open('info.text',"w")
dire.write(texto)
dire.close()
voz=("info.txt","ES","voz.mp3")
print("Reproduciendo:")
audio='voz.mp3'
playsound(audio)
print("Reproduciendo:")

#mensajeprincipal#
while True:
    ret,Frame = cap.read()
    if ret ==False:break
    cv2.putText(Frame,'ubique aqui el texto para leer',(158,80),cv2.FONT_HERSHEY_SIMPLEX,0.71,(255,255,0),2)
    cv2.putText (Frame,'ubique aqui el texto para leer',(160,80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)
    cv2.rectangle(Frame,(cuadro,cuadro),(anchocam-cuadro , altocam-cuadro),(0,0,0),2)
    x1,y1 =cuadro,cuadro
    ancho,alto=(anchocam-cuadro)-x1,(altocam-cuadro)-y1
    x2,y2=x1+ancho,y1+alto
    doc=Frame[y1:y2,x1:x2]
    cv2.imwrite("imatext.jpg",doc)

    cv2.imshow("lector_inteligente",Frame)
    t =cv2.waitKey(1)
    if t ==27:
        break

text(doc)
cap.release()
cv2.destroyAllWindows()



