import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Assets/Cam_51.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.imshow(sobely,cmap = 'gray')
plt.axis('off')
plt.savefig('Assets/test1.jpg', bbox_inches='tight', pad_inches = 0)