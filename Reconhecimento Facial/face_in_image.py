import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Leitura da imagem
imagem = cv2.imread('clateste.JPG')
# Converter para cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# Detectar Faces
faces = face_cascade.detectMultiScale(imagem_cinza, 1.5, 5)

# Desenhar um retangulo para cada face
for (x, y, w, h) in faces:
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (255,51,153), 4)
    
    
# Display the output
cv2.imshow('img', imagem)
cv2.waitKey()


