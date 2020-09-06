import cv2

import numpy as np

print(cv2.__version__)
imagem = cv2.imread('imagem2.png')
cv2.imshow("Inicial", imagem)
colunas = imagem.shape[1]
linhas = imagem.shape[0]
print(colunas)
print(linhas)

# mudar para negativo e mostrar o oposto ocorrendo
#imagem_deslocada = cv2.warpAffine(imagem, np.float32([[1,0,150],[0,1,70]]), (colunas,linhas))
imagem_deslocada = cv2.warpAffine(imagem, np.float32([[1,0,-150],[0,1,-70]]), (colunas,linhas))

# * valores 1 e 0

cv2.imshow('Deslocada', imagem_deslocada)
cv2.waitKey(0)
cv2.destroyAllWindows()