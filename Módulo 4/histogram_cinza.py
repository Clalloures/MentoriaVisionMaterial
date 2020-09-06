import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


print("OI\n");
img = cv.imread('clateste.jpg',0)
cv.imshow('Imagem', img)
plt.hist(img.ravel(),256,[0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()