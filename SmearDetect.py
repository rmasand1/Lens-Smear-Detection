import os
import glob
import cv2
import numpy as np
import imutils

try:
    #Getting the directory of the images
    files = glob.glob("/home/krishna/Downloads/sample_drive/cam_0/*.jpg")
    img_avg = np.zeros((500,500),np.float)
    for im in glob.glob("/home/krishna/Downloads/sample_drive/cam_0/*.jpg"):
        img = cv2.imread(im)
        img = imutils.resize(img, width=500)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # I am using Gaussianlur because it is highly effective in removing Gaussian noise from the image
        # I can't use Median Blur as it is not appropriate for the assignment
        #img = cv2.GaussianBlur(img, (5, 5), 0)
        img = cv2.equalizeHist(img)
        img_avg = img_avg + img

    img_avg = img_avg/len(files)
    img_avg = np.array(np.round(img_avg), dtype=np.uint8)

    cv2.imwrite("Cam_00.jpg", img_avg)
except FileNotFoundError:
    print("Enter proper Directory")
