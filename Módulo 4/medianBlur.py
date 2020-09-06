import cv2
import numpy

imagem = cv2.imread('imagem3.png')
kernel = 7
imagem_blur = cv2.medianBlur(imagem,kernel)

cv2.imshow('Median', imagem_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()