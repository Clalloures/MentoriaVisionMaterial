import numpy as np
import cv2

# Criando uma matriz onde todas as posicoes tem valor zero
# 500 , 500 = tamaho
# 3 = canais (RGB)
# uint8 = 8 bits

quadro = np.zeros((500,500,3), dtype = 'uint8')

# Escolhendo o desenho
# https://www.rapidtables.com/web/color/RGB_Color.html#:~:text=RGB%20color%20space%20or%20RGB,*256%3D16777216%20possible%20colors.

#cv2.rectangle(quadro, (350,120), (450,150), (153,51,255),3, lineType=8, shift=0)
cv2.rectangle(quadro, (200,120), (300,150), (255,51,153),3, lineType=8, shift=0)
cv2.line(quadro, (200,350), (300,350), (255,255,0))
cv2.circle(quadro, (250,250), 50, (0, 255,255))

cv2.imshow('Quadro', quadro)
cv2.waitKey(0)
cv2.destroyAllWindows()
