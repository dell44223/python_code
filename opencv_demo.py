import cv
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('road.png', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.xticks([])
plt.show()