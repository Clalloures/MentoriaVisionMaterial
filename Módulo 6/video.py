import cv2
import numpy as np

# VideoCapture
# colocar um número ira buscar cor alguma camera conectada ao seu dispositivo
# numero 0 padrao quando se tem apenas uma câmera
#

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()        
