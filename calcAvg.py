import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('Assets/test.jpg')
img2 = cv2.imread('Assets/test1.jpg')

img = img1 + img2

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()