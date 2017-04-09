import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Assets/Cam_11.jpg',0)
#As Edge detection is susceptible to Noise I am using the Gaussian filter to remove the noise

edges = cv2.Canny(img,300,400,apertureSize=5,L2gradient=True)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()