import cv2
import numpy as np
from skimage.filters import threshold_adaptive

img = cv2.imread('Assets/test.jpg',0)
img = cv2.medianBlur(img,23)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2)

cv2.imshow('image',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()