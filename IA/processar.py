import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lambo.jpg')

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))


plt.show()