import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, imagem = cap.read()
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(imagem_cinza, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(imagem,(x,y),(x+w,y+h),(255,51,153),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(imagem,'Face ',(x-5,y-5), font,2,(255,51,153),2, cv2.LINE_AA)
        roi_gray = imagem_cinza[y:y+h, x:x+w]
        roi_color = imagem[y:y+h, x:x+w]
    
    
        
    cv2.imshow('img',imagem)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



