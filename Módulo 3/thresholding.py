import cv2
import numpy as numpy

imagem = cv2.imread('imagem2.png',0)

threshold = 0
(T_value,binarythreshold) = cv2.threshold(imagem, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow('Binaria', binarythreshold)
cv2.waitKey(0)
cv2.destroyAllWindows()