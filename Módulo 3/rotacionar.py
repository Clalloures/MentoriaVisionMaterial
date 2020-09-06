import cv2
import numpy as np

imagem = cv2.imread('imagem2.png')

colunas = imagem.shape[1]
linhas = imagem.shape[0]


centro = (colunas/2,linhas/2)
angulo = 90
print(colunas)
print(linhas)
# mudar para negativo e mostrar o oposto ocorrendo
imagem_rotacao = cv2.warpAffine(imagem, cv2.getRotationMatrix2D(centro, angulo,1), (colunas,linhas))
#imagem_deslocada = cv2.warpAffine(imagem, np.float32([[1,0,-150],[0,1,-70]]), (colunas,linhas))

cv2.imshow('Rotacao', imagem_rotacao)
cv2.waitKey(0)
cv2.destroyAllWindows()