import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_adaptive
import imutils
import numpy as np

img = cv2.imread('Cam_3.jpg')
img = imutils.resize(img,width=500)
#
# # Converting the image to gray scale
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding and scale it with 255
warped = threshold_adaptive(img, 250, offset=10)
warped_average_image = warped.astype("uint8") * 255

cv2.imshow('image',warped_average_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


