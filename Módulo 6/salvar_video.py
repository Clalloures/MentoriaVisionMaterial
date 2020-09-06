import cv2
import numpy as np

# VideoCapture
# colocar um número ira buscar cor alguma camera conectada ao seu dispositivo
# numero 0 padrao quando se tem apenas uma câmera
#

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('your_video.avi', fourcc, 20.0, size)

while (cap.isOpened()):
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()        
cap.release()        
cv2.destroyAllWindows()

