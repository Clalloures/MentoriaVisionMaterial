# Ajuda a presentar as bordas
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
import cv2
import numpy

imagem = cv2.imread('imagem3.png')
dimention = 15
color = 100
space = 100

imagem_blur = cv2.bilateralFilter(imagem,dimention,color,space)

cv2.imshow('Bilateral', imagem_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()