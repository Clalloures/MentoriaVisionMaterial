# Importar bibliotecas
import cv2

imagem = cv2.imread('imagem1.png',0)

altura = imagem.shape[0]
largura = imagem.shape[1]

porcentagem = 40
nova_altura = int(altura * porcentagem / 100)
nova_largura = int(largura * porcentagem / 100)

dim = (nova_largura, nova_altura)

imagem_reduzida = cv2.resize(imagem, dim, interpolation = cv2.INTER_AREA)

cv2.imwrite('resultado_imagem1_cinza.png', imagem_reduzida)



