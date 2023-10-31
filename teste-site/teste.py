import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys 

args = sys.argv

print("hello World")

#print("O argumento passado foi: ", args[1])


def executarPlot(imagem):
    img = cv.imread("images/" + imagem)

    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

    plt.show()

