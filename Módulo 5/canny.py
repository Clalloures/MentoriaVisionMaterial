import cv2
import numpy as np

imagem = cv2.imread('imagem4.png')

threshold_min = 50
threshold_max = 100

canny = cv2.Canny(imagem, threshold_min,threshold_max)

cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()