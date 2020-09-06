import cv2
import numpy

imagem = cv2.imread('imagem3.png')
matriz = (15,15)

imagem_blur = cv2.GaussianBlur(imagem, matriz, 0)
cv2.imshow('Gaussian', imagem_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()