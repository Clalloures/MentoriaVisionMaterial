# Importando as bibliotecas
import numpy as np
import cv2

quadro = np.zeros((500,500,3), dtype = 'uint8')
cv2.putText(quadro, "Clarissa Lima Tech", (50,200), cv2.FONT_HERSHEY_DUPLEX,1.3,(255,51,153),2, cv2.LINE_8)

cv2.imshow('Quadro', quadro)
cv2.waitKey(0)
cv2.destroyAllWindows()


# PDF Lista de fontes