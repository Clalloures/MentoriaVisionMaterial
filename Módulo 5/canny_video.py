import cv2
import numpy as np
cap = cv2.VideoCapture(0)

#imagem = cv2.imread('imagem4.png')

threshold_min = 50 #10 e 90
threshold_max = 100

while True:
    _, frame = cap.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_image, (5,5),0)
    canny = cv2.Canny(blur, threshold_min,threshold_max)

    cv2.imshow('Canny', canny)

    cv2.waitKey(1)


cv2.destroyAllWindows()